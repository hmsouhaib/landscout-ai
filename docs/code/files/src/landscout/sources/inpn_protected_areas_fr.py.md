# `src/landscout/sources/inpn_protected_areas_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_fr.py`
- File type: Python source
- Layer/domain: official source acquisition and archive/extraction authority
- Responsibility: Acquires the pinned PatriNat/INPN EP archive and proves extraction bytes against one immutable archive snapshot.
- Source SHA256: `7f545038d3b0369eb435ef61ca45575e0351c61900499d727dbfb0f4a7e27c24`

## 1. Architectural contract

The pinned archive is source authority. STEP 7F.1B.1.1 requires `pinned EP.zip bytes -> validated ZIP members -> archive-derived uncompressed regular-member inventory -> marker/physical/caller equality`. The marker remains cache evidence and cannot override archive member bytes. Valid local caches remain fully offline; invalid extraction caches may be rebuilt from the valid local archive without network.

## 2. Imports and dependencies

```python
from __future__ import annotations
```

```python
import io
```

```python
import json
```

```python
import re
```

```python
import shutil
```

```python
import stat
```

```python
import unicodedata
```

```python
import zipfile
```

```python
import zlib
```

```python
from dataclasses import dataclass
```

```python
from datetime import UTC, datetime
```

```python
from hashlib import sha256
```

```python
from math import isfinite
```

```python
from numbers import Real
```

```python
from pathlib import Path, PurePosixPath, PureWindowsPath
```

```python
from shutil import copy2, copyfileobj
```

```python
from typing import Annotated, Literal, Self
```

```python
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
    model_validator,
)
```

```python
from landscout.common.safe_http import SafeHttpsError, open_safe_https
```

```python
from landscout.common.strict_json import loads_strict_json_object
```

```python
from landscout.common.strict_yaml import loads_strict_yaml
```

## 3. Constants, aliases, and exact module declarations

### `DEFAULT_CONFIG_PATH`

```python
DEFAULT_CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `DOWNLOAD_CHUNK_SIZE`

```python
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `DOWNLOAD_METADATA_SCHEMA_VERSION`

```python
DOWNLOAD_METADATA_SCHEMA_VERSION: Literal[1] = 1
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `EXTRACTION_METADATA_SCHEMA_VERSION`

```python
EXTRACTION_METADATA_SCHEMA_VERSION: Literal[1] = 1
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `EXTRACTION_METADATA_FILENAME`

```python
EXTRACTION_METADATA_FILENAME = ".landscout-extraction.json"
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `OFFICIAL_REFERENCE_PAGE_URL`

```python
OFFICIAL_REFERENCE_PAGE_URL = (
    "https://www.patrinat.fr/fr/"
    "page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"
)
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `OFFICIAL_ARCHIVE_URL`

```python
OFFICIAL_ARCHIVE_URL = "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `OFFICIAL_DATASET_NAME`

```python
OFFICIAL_DATASET_NAME = "Base de référence des espaces protégés français"
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `CanonicalSha256`

```python
CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `DeclaredVersion`

```python
DeclaredVersion = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:0[1-9]|1[0-2])/\d{4}$"),
]
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `StrictPositiveInt`

```python
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `StrictNonNegativeInt`

```python
StrictNonNegativeInt = Annotated[int, Field(strict=True, ge=0)]
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `_WINDOWS_RESERVED_BASENAMES`

```python
_WINDOWS_RESERVED_BASENAMES = frozenset(
    {
        "con",
        "prn",
        "aux",
        "nul",
        "clock$",
        *(f"com{index}" for index in range(1, 10)),
        *(f"lpt{index}" for index in range(1, 10)),
    }
)
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

### `__all__`

```python
__all__ = [
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasSourceConfig",
    "InpnProtectedAreasSourceError",
    "download_inpn_protected_areas_archive",
    "extract_inpn_protected_areas_archive",
    "load_inpn_protected_areas_source_config",
    "validate_inpn_protected_areas_extraction",
]
```

- Role: exact source identity, schema, strict domain, filesystem token, or public export declaration consumed only by the source locations reproduced below.

## 4. Exceptions and immutable/strict models

### `InpnProtectedAreasSourceError`

- Bases: `ValueError`.
- Decorators: `none`.
- Purpose: Raised when the pinned INPN source cannot be handled safely.
- Exact fields: none declared.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `InpnProtectedAreasSourceConfig`

- Bases: `BaseModel`.
- Decorators: `none`.
- Purpose: Strict identity of one reviewed PatriNat protected-areas snapshot.
- Exact fields:

  - `provider: Literal['PatriNat']`; default `required`.
  - `authority: Literal['MNHN']`; default `required`.
  - `program: Literal['INPN']`; default `required`.
  - `dataset_id: Literal['EP']`; default `required`.
  - `dataset_name: Literal['Base de référence des espaces protégés français']`; default `required`.
  - `declared_version: DeclaredVersion`; default `required`.
  - `reference_page_url: HttpUrl`; default `required`.
  - `archive_url: HttpUrl`; default `required`.
  - `archive_filename: Literal['EP.zip']`; default `required`.
  - `expected_archive_size_bytes: StrictPositiveInt`; default `required`.
  - `expected_archive_sha256: CanonicalSha256`; default `required`.
  - `cache_root: Path`; default `required`.
- Validators/methods:

  - `def _pinned_official_urls(self) -> Self`; decorators `model_validator(mode='after')`; calls `ValueError`, `model_validator`, `str`; explicit raises `ValueError('reference_page_url must be the reviewed PatriNat page')`, `ValueError('archive_url must be the reviewed official EP archive')`.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `InpnProtectedAreasDownload`

- Bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: Internal validation or immutable source evidence.
- Exact fields:

  - `provider: str`; default `required`.
  - `authority: str`; default `required`.
  - `program: str`; default `required`.
  - `dataset_id: str`; default `required`.
  - `dataset_name: str`; default `required`.
  - `declared_version: str`; default `required`.
  - `reference_page_url: str`; default `required`.
  - `archive_url: str`; default `required`.
  - `download_timestamp: str`; default `required`.
  - `filename: str`; default `required`.
  - `file_size: int`; default `required`.
  - `sha256: str`; default `required`.
  - `path: Path`; default `required`.
  - `cache_hit: bool`; default `required`.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `InpnProtectedAreasExtractedFile`

- Bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: Internal validation or immutable source evidence.
- Exact fields:

  - `relative_path: str`; default `required`.
  - `file_size: int`; default `required`.
  - `sha256: str`; default `required`.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `InpnProtectedAreasExtraction`

- Bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: Internal validation or immutable source evidence.
- Exact fields:

  - `download: InpnProtectedAreasDownload`; default `required`.
  - `extraction_path: Path`; default `required`.
  - `files: tuple[InpnProtectedAreasExtractedFile, ...]`; default `required`.
  - `cache_hit: bool`; default `required`.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `_DownloadMetadata`

- Bases: `BaseModel`.
- Decorators: `none`.
- Purpose: Internal validation or immutable source evidence.
- Exact fields:

  - `schema_version: Literal[1]`; default `required`.
  - `provider: Literal['PatriNat']`; default `required`.
  - `authority: Literal['MNHN']`; default `required`.
  - `program: Literal['INPN']`; default `required`.
  - `dataset_id: Literal['EP']`; default `required`.
  - `dataset_name: Literal['Base de référence des espaces protégés français']`; default `required`.
  - `declared_version: DeclaredVersion`; default `required`.
  - `reference_page_url: str`; default `required`.
  - `archive_url: str`; default `required`.
  - `filename: Literal['EP.zip']`; default `required`.
  - `download_timestamp: str`; default `required`.
  - `file_size: StrictPositiveInt`; default `required`.
  - `sha256: CanonicalSha256`; default `required`.
- Validators/methods:

  - `def _strict_schema_version(cls, value: object) -> object`; decorators `field_validator('schema_version', mode='before'), classmethod`; calls `ValueError`, `field_validator`, `type`; explicit raises `ValueError('Download metadata schema_version must be exact integer 1')`.
  - `def _exact_reference_page(cls, value: str) -> str`; decorators `field_validator('reference_page_url'), classmethod`; calls `ValueError`, `field_validator`; explicit raises `ValueError('Cached reference page identity differs')`.
  - `def _exact_archive_url(cls, value: str) -> str`; decorators `field_validator('archive_url'), classmethod`; calls `ValueError`, `field_validator`; explicit raises `ValueError('Cached archive URL identity differs')`.
  - `def _aware_utc_timestamp(cls, value: str) -> str`; decorators `field_validator('download_timestamp'), classmethod`; calls `_validate_utc_timestamp`, `field_validator`; explicit raises none.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `_ExtractedFileMetadata`

- Bases: `BaseModel`.
- Decorators: `none`.
- Purpose: Internal validation or immutable source evidence.
- Exact fields:

  - `relative_path: str`; default `required`.
  - `file_size: StrictNonNegativeInt`; default `required`.
  - `sha256: CanonicalSha256`; default `required`.
- Validators/methods:

  - `def _canonical_path(cls, value: str) -> str`; decorators `field_validator('relative_path'), classmethod`; calls `_validate_inventory_relative_path`, `field_validator`; explicit raises none.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `_ExtractionMetadata`

- Bases: `BaseModel`.
- Decorators: `none`.
- Purpose: Internal validation or immutable source evidence.
- Exact fields:

  - `schema_version: Literal[1]`; default `required`.
  - `archive_sha256: CanonicalSha256`; default `required`.
  - `archive_size: StrictPositiveInt`; default `required`.
  - `files: tuple[_ExtractedFileMetadata, ...]`; default `Field(min_length=1)`.
- Validators/methods:

  - `def _strict_schema_version(cls, value: object) -> object`; decorators `field_validator('schema_version', mode='before'), classmethod`; calls `ValueError`, `field_validator`, `type`; explicit raises `ValueError('Extraction metadata schema_version must be exact integer 1')`.
  - `def _deterministic_files(cls, value: tuple[_ExtractedFileMetadata, ...]) -> tuple[_ExtractedFileMetadata, ...]`; decorators `field_validator('files'), classmethod`; calls `ValueError`, `field_validator`, `len`, `set`, `sorted`, `tuple`; explicit raises `ValueError('Extraction inventory must be unique and lexically ordered')`.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

### `_ValidatedZipMember`

- Bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: Internal validation or immutable source evidence.
- Exact fields:

  - `info: zipfile.ZipInfo`; default `required`.
  - `destination: PurePosixPath`; default `required`.
  - `is_directory: bool`; default `required`.
- Canonicality: the declared frozen/strict model contract is supplemented by exact public boundary reconstruction and scalar/tuple validation.

## 5. Function-by-function inventory

### `_validate_utc_timestamp`

- Exact signature: `def _validate_utc_timestamp(value: object) -> None`
- Purpose: Validate utc timestamp.
- Inputs: `value: object`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 240: branch/fail closed on `type(value) is not str or not value or value != value.strip()`.
2. line 242: derive `parsed`.
3. line 243: derive `offset`.
4. line 244: branch/fail closed on `parsed.tzinfo is None or offset is None`.
5. line 246: branch/fail closed on `offset.total_seconds() != 0`.

- Validation: `ValueError('download_timestamp must be an exact non-empty string')`; `ValueError('download_timestamp must be timezone-aware')`; `ValueError('download_timestamp must use UTC')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `ValueError`, `datetime.fromisoformat`, `offset.total_seconds`, `parsed.utcoffset`, `type`, `value.strip`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_validated_config`

- Exact signature: `def _validated_config(config: object) -> InpnProtectedAreasSourceConfig`
- Purpose: Validated config.
- Inputs: `config: object`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasSourceConfig`.
- Ordered algorithm:

1. line 251: branch/fail closed on `type(config) is not InpnProtectedAreasSourceConfig`.
2. line 255: controlled try/except boundary for `(AttributeError, TypeError, ValueError, ValidationError)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('config must be an exact InpnProtectedAreasSourceConfig')`; `InpnProtectedAreasSourceError('INPN protected-areas config is invalid')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceConfig.model_validate`, `InpnProtectedAreasSourceError`, `config.model_dump`, `type`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `load_inpn_protected_areas_source_config`

- Exact signature: `def load_inpn_protected_areas_source_config(path: Path=DEFAULT_CONFIG_PATH) -> InpnProtectedAreasSourceConfig`
- Purpose: Load the explicit, version-pinned PatriNat EP source configuration.
- Inputs: `path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasSourceConfig`.
- Ordered algorithm:

1. line 268: perform `'Load the explicit, version-pinned PatriNat EP source configuration.'`.
2. line 270: branch/fail closed on `not isinstance(path, Path)`.
3. line 272: controlled try/except boundary for `(OSError, TypeError, ValueError, ValidationError)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('Config path must be a pathlib Path')`; `ValueError('Expected a YAML mapping')`; `InpnProtectedAreasSourceError(f'Cannot load INPN protected-areas source config: {path}')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `path.read_bytes`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceConfig.model_validate`, `InpnProtectedAreasSourceError`, `ValueError`, `isinstance`, `loads_strict_yaml`, `path.read_bytes`, `type`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_checked_in_config_loads_with_exact_source_identity`, `test_source_config_yaml_rejects_duplicate_keys`, `test_loaded_source_config_is_immutable`, `test_config_rejects_noncanonical_values`, `test_download_timeout_is_strict_finite_positive`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_cache_directory`

- Exact signature: `def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path`
- Purpose: Cache directory.
- Inputs: `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `Path`.
- Ordered algorithm:

1. line 284: derive `version`.
2. line 285: return `config.cache_root / config.dataset_id / version`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `config.declared_version.replace`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `config.declared_version.replace`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_archive_path`

- Exact signature: `def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path`
- Purpose: Archive path.
- Inputs: `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `Path`.
- Ordered algorithm:

1. line 289: return `_cache_directory(config) / config.archive_filename`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `_cache_directory`.
- Internal caller/callee relationship: directly calls `_cache_directory`; the public flows below establish external entry points.
- Direct tests: `test_transient_archive_path_swap_cannot_change_extracted_member_bytes`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_metadata_path`

- Exact signature: `def _metadata_path(archive_path: Path) -> Path`
- Purpose: Metadata path.
- Inputs: `archive_path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `Path`.
- Ordered algorithm:

1. line 293: return `archive_path.with_name(f'{archive_path.name}.metadata.json')`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `archive_path.with_name`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_valid_zip_download_binds_exact_bytes_and_lineage`, `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`, `test_invalid_download_cache_is_a_miss`, `test_successful_first_and_replacement_publication`, `test_rollback_failure_preserves_recovery_material`, `test_failed_replacement_restores_a_still_reusable_valid_download_pair`, `test_extraction_inventory_is_complete_ordered_and_hashed`, `test_invalid_extraction_cache_is_rebuilt`, `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`, `test_cache_path_binds_version_and_filename`, `test_archive_derived_inventory_equals_marker_physical_and_caller`, `test_invalid_coordinated_cache_rebuilds_from_local_archive_without_network`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_sha256_file`

- Exact signature: `def _sha256_file(path: Path) -> str`
- Purpose: Sha256 file.
- Inputs: `path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `str`.
- Ordered algorithm:

1. line 297: derive `digest`.
2. line 298: use and deterministically close `path.open('rb')`.
3. line 301: return `digest.hexdigest()`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `path.open`
- Hashing effects: `sha256`
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `digest.hexdigest`, `digest.update`, `iter`, `path.open`, `sha256`, `stream.read`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_is_link_or_junction`

- Exact signature: `def _is_link_or_junction(path: Path) -> bool`
- Purpose: Is link or junction.
- Inputs: `path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `bool`.
- Ordered algorithm:

1. line 305: controlled try/except boundary for `OSError` with visible cleanup/finalization.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `path.is_junction`, `path.is_symlink`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_extraction_revalidation_rejects_link_or_junction_file`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_is_regular_file`

- Exact signature: `def _is_regular_file(path: Path) -> bool`
- Purpose: Is regular file.
- Inputs: `path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `bool`.
- Ordered algorithm:

1. line 312: return `not _is_link_or_junction(path) and path.is_file()`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `_is_link_or_junction`, `path.is_file`.
- Internal caller/callee relationship: directly calls `_is_link_or_junction`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_read_strict_json`

- Exact signature: `def _read_strict_json(path: Path) -> dict[str, object]`
- Purpose: Read strict json.
- Inputs: `path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `dict[str, object]`.
- Ordered algorithm:

1. line 316: return `loads_strict_json_object(path.read_bytes())`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `path.read_bytes`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `loads_strict_json_object`, `path.read_bytes`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_windows_component_key`

- Exact signature: `def _windows_component_key(component: str) -> str`
- Purpose: Windows component key.
- Inputs: `component: str`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `str`.
- Ordered algorithm:

1. line 320: derive `normalized`.
2. line 321: branch/fail closed on `not normalized or normalized in {'.', '..'} or normalized != normalized.strip() or normalized.endswith((' ', '.')) or any((ord(character) < 32 or ord(character) == 127 for character in normalized)) or any((character in '<>:"/\\|?*' for character in normalized))`.
3. line 332: derive `stem`.
4. line 333: branch/fail closed on `stem in _WINDOWS_RESERVED_BASENAMES`.
5. line 337: return `normalized.casefold()`.

- Validation: `InpnProtectedAreasSourceError(f'Unsafe Windows-compatible ZIP component: {component}')`; `InpnProtectedAreasSourceError(f'Reserved Windows device name in ZIP member: {component}')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `any`, `normalized.casefold`, `normalized.endswith`, `normalized.split`, `normalized.split('.', 1)[0].casefold`, `normalized.strip`, `ord`, `unicodedata.normalize`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_canonical_member_destination`

- Exact signature: `def _canonical_member_destination(name: str) -> tuple[PurePosixPath, tuple[str, ...]]`
- Purpose: Canonical member destination.
- Inputs: `name: str`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `tuple[PurePosixPath, tuple[str, ...]]`.
- Ordered algorithm:

1. line 341: branch/fail closed on `type(name) is not str or not name or '\x00' in name`.
2. line 343: branch/fail closed on `any((ord(character) < 32 or ord(character) == 127 for character in name))`.
3. line 347: derive `posix`.
4. line 348: derive `windows`.
5. line 349: branch/fail closed on `posix.is_absolute() or windows.is_absolute() or bool(windows.drive)`.
6. line 353: branch/fail closed on `'..' in posix.parts`.
7. line 355: derive `parts`.
8. line 356: branch/fail closed on `not parts`.
9. line 358: derive `canonical`.
10. line 359: branch/fail closed on `canonical[0] == EXTRACTION_METADATA_FILENAME.casefold()`.
11. line 363: return `(PurePosixPath(*parts), canonical)`.

- Validation: `InpnProtectedAreasSourceError('ZIP member name is empty or invalid')`; `InpnProtectedAreasSourceError('ZIP member name contains control characters')`; `InpnProtectedAreasSourceError(f'Absolute ZIP member path is unsafe: {name}')`; `InpnProtectedAreasSourceError(f'ZIP member traversal is unsafe: {name}')`; `InpnProtectedAreasSourceError('ZIP member has no normalized destination')`; `InpnProtectedAreasSourceError('ZIP member collides with the extraction metadata path')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `name.replace`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `EXTRACTION_METADATA_FILENAME.casefold`, `InpnProtectedAreasSourceError`, `PurePosixPath`, `PureWindowsPath`, `_windows_component_key`, `any`, `bool`, `name.replace`, `ord`, `posix.is_absolute`, `tuple`, `type`, `windows.is_absolute`.
- Internal caller/callee relationship: directly calls `_windows_component_key`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_validated_zip_members`

- Exact signature: `def _validated_zip_members(archive: zipfile.ZipFile) -> tuple[_ValidatedZipMember, ...]`
- Purpose: Validates the full ZIP namespace, entry kinds, collisions, encryption flags, and CRCs on an already-open archive snapshot.
- Inputs: `archive: zipfile.ZipFile`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `tuple[_ValidatedZipMember, ...]`.
- Ordered algorithm:

1. line 369: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(NotImplementedError, OSError, RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('ZIP archive contains no members')`; `InpnProtectedAreasSourceError('ZIP archive contains no regular files')`; `InpnProtectedAreasSourceError(f'Corrupt ZIP member: {bad_member}')`; `InpnProtectedAreasSourceError('Cannot validate ZIP archive')`; `InpnProtectedAreasSourceError(f'duplicate ZIP member name: {name}')`; `InpnProtectedAreasSourceError(f'Encrypted ZIP members are unsupported: {name}')`; `InpnProtectedAreasSourceError(f'ZIP symbolic links are forbidden: {name}')`; `InpnProtectedAreasSourceError(f'ZIP special files are forbidden: {name}')`; `InpnProtectedAreasSourceError(f'ZIP members collide at one normalized destination: {explicit[canonical]} / {name}')`; `InpnProtectedAreasSourceError(f'colliding ZIP file/directory destination: {name}')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `_ValidatedZipMember`, `_canonical_member_destination`, `any`, `archive.infolist`, `archive.testzip`, `directories.add`, `directories.update`, `files.add`, `info.is_dir`, `len`, `name.endswith`, `range`, `raw_names.add`, `set`, `stat.S_IFMT`, `stat.S_ISDIR`, `stat.S_ISLNK`, `tuple`, `validated.append`.
- Internal caller/callee relationship: directly calls `_canonical_member_destination`; the public flows below establish external entry points.
- Direct tests: `test_public_api_exports_only_stable_high_level_symbols`, `test_archive_derived_inventory_equals_marker_physical_and_caller`, `test_transient_archive_path_swap_cannot_change_extracted_member_bytes`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_archive_regular_file_inventory`

- Exact signature: `def _archive_regular_file_inventory(archive: zipfile.ZipFile, members: tuple[_ValidatedZipMember, ...]) -> tuple[InpnProtectedAreasExtractedFile, ...]`
- Purpose: Streams and hashes every validated uncompressed regular member from that archive object into the authoritative ordered inventory.
- Inputs: `archive: zipfile.ZipFile`, `members: tuple[_ValidatedZipMember, ...]`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `tuple[InpnProtectedAreasExtractedFile, ...]`.
- Ordered algorithm:

1. line 453: derive `files`.
2. line 454: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(NotImplementedError, OSError, RuntimeError, ValueError, zipfile.BadZipFile, zlib.error)` with visible cleanup/finalization.
3. line 488: perform `files.sort(key=lambda item: item.relative_path)`.
4. line 489: derive `paths`.
5. line 490: branch/fail closed on `not files or len(paths) != len(set(paths))`.
6. line 494: return `tuple(files)`.

- Validation: `InpnProtectedAreasSourceError('Archive-derived regular-file inventory is empty or ambiguous')`; `InpnProtectedAreasSourceError('Cannot inventory regular files from the verified archive snapshot')`; `InpnProtectedAreasSourceError(f'ZIP member size changed while reading: {member.info.filename}')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `archive.open`
- Hashing effects: `sha256`
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasExtractedFile`, `InpnProtectedAreasSourceError`, `archive.open`, `digest.hexdigest`, `digest.update`, `files.append`, `files.sort`, `iter`, `len`, `member.destination.as_posix`, `set`, `sha256`, `source.read`, `tuple`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_archive_derived_inventory_equals_marker_physical_and_caller`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_download_metadata`

- Exact signature: `def _download_metadata(config: InpnProtectedAreasSourceConfig, result: InpnProtectedAreasDownload) -> _DownloadMetadata`
- Purpose: Download metadata.
- Inputs: `config: InpnProtectedAreasSourceConfig`, `result: InpnProtectedAreasDownload`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `_DownloadMetadata`.
- Ordered algorithm:

1. line 501: return `_DownloadMetadata(schema_version=DOWNLOAD_METADATA_SCHEMA_VERSION, provider=config.provider, authority=config.authority, program=config.program, dataset_id=config.dataset_id, dataset_name=config.dataset_name, declared_version=config.declared_version, reference_page_url=str(config.reference_page_url), archive_url=str(config.archive_url), filename=config.archive_filename, download_timestamp=result.download_timestamp, file_size=result.file_size, sha256=result.sha256)`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `_DownloadMetadata`, `str`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_valid_zip_download_binds_exact_bytes_and_lineage`, `test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit`, `test_invalid_download_cache_is_a_miss`, `test_successful_first_and_replacement_publication`, `test_rollback_failure_preserves_recovery_material`, `test_failed_replacement_restores_a_still_reusable_valid_download_pair`, `test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits`, `test_cache_path_binds_version_and_filename`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_load_cached_download`

- Exact signature: `def _load_cached_download(archive_path: Path, metadata_path: Path, config: InpnProtectedAreasSourceConfig) -> InpnProtectedAreasDownload | None`
- Purpose: Load cached download.
- Inputs: `archive_path: Path`, `metadata_path: Path`, `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasDownload | None`.
- Ordered algorithm:

1. line 523: branch/fail closed on `not _is_regular_file(archive_path) or not _is_regular_file(metadata_path)`.
2. line 525: controlled try/except boundary for `(InpnProtectedAreasSourceError, OSError, TypeError, ValueError, ValidationError, json.JSONDecodeError)` with visible cleanup/finalization.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasDownload`, `_DownloadMetadata.model_validate`, `_is_regular_file`, `_read_strict_json`, `_validate_download`, `any`, `expected.items`, `getattr`, `str`.
- Internal caller/callee relationship: directly calls `_is_regular_file`, `_read_strict_json`, `_validate_download`; the public flows below establish external entry points.
- Direct tests: `test_rollback_failure_preserves_recovery_material`, `test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_replace_file`

- Exact signature: `def _replace_file(source: Path, target: Path) -> None`
- Purpose: Replace file.
- Inputs: `source: Path`, `target: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 569: perform `source.replace(target)`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `source.replace`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `source.replace`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_publication_failure_restores_old_pair`, `test_rollback_failure_preserves_recovery_material`, `test_failed_replacement_restores_a_still_reusable_valid_download_pair`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_publish_cache_pair`

- Exact signature: `def _publish_cache_pair(temporary_archive: Path, temporary_metadata: Path, archive_path: Path, metadata_path: Path) -> None`
- Purpose: Publish cache pair.
- Inputs: `temporary_archive: Path`, `temporary_metadata: Path`, `archive_path: Path`, `metadata_path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 578: derive `archive_backup`.
2. line 579: derive `metadata_backup`.
3. line 580: branch/fail closed on `any((path.exists() or _is_link_or_junction(path) for path in (archive_backup, metadata_backup)))`.
4. line 587: derive `archive_existed`.
5. line 588: derive `metadata_existed`.
6. line 589: controlled try/except boundary for `OSError` with visible cleanup/finalization.
7. line 599: controlled try/except boundary for `OSError` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('Cache recovery backup already exists; manual recovery is required')`; `InpnProtectedAreasSourceError('INPN cache publication failed')`; `InpnProtectedAreasSourceError('INPN cache publication and rollback both failed')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `archive_backup.unlink`, `archive_path.unlink`, `metadata_backup.unlink`, `metadata_path.unlink`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `_is_link_or_junction`, `_replace_file`, `any`, `archive_backup.unlink`, `archive_path.is_file`, `archive_path.unlink`, `archive_path.with_name`, `copy2`, `metadata_backup.unlink`, `metadata_path.is_file`, `metadata_path.unlink`, `metadata_path.with_name`, `path.exists`.
- Internal caller/callee relationship: directly calls `_is_link_or_junction`, `_replace_file`; the public flows below establish external entry points.
- Direct tests: `test_broken_download_recovery_symlink_is_rejected`, `test_existing_normal_download_recovery_backup_remains_unchanged`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_download_archive_bytes`

- Exact signature: `def _download_archive_bytes(configured_url: str, timeout_seconds: float, destination: Path) -> None`
- Purpose: Download archive bytes.
- Inputs: `configured_url: str`, `timeout_seconds: float`, `destination: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 631: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(SafeHttpsError, OSError, TypeError, ValueError)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('Official INPN archive download failed')`; `InpnProtectedAreasSourceError('HTTP response headers are invalid')`; `InpnProtectedAreasSourceError('HTML response cannot be used as a ZIP')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `destination.open`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `callable`, `content_type.casefold`, `copyfileobj`, `destination.open`, `getattr`, `header_get`, `open_safe_https`, `str`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `download_inpn_protected_areas_archive`

- Exact signature: `def download_inpn_protected_areas_archive(config: InpnProtectedAreasSourceConfig, *, timeout_seconds: float=120.0) -> InpnProtectedAreasDownload`
- Purpose: Download or reuse the exact configured official EP ZIP bytes.
- Inputs: `config: InpnProtectedAreasSourceConfig`, `timeout_seconds: float`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasDownload`.
- Ordered algorithm:

1. line 661: perform `'Download or reuse the exact configured official EP ZIP bytes.'`.
2. line 663: derive `validated_config`.
3. line 664: branch/fail closed on `isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, Real)`.
4. line 668: controlled try/except boundary for `(OverflowError, TypeError, ValueError)` with visible cleanup/finalization.
5. line 674: branch/fail closed on `not isfinite(validated_timeout) or validated_timeout <= 0`.
6. line 678: derive `archive_path`.
7. line 679: derive `metadata_path`.
8. line 680: derive `cached`.
9. line 681: branch/fail closed on `cached is not None`.
10. line 684: derive `temporary_archive`.
11. line 685: derive `temporary_metadata`.
12. line 686: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(OSError, TypeError, ValueError, ValidationError)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('timeout_seconds must be a strict finite positive number')`; `InpnProtectedAreasSourceError('Downloaded INPN archive differs from the configured snapshot')`; `InpnProtectedAreasSourceError('Official INPN archive download or cache publication failed')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `archive_path.parent.mkdir`, `temporary_archive.read_bytes`, `temporary_archive.unlink`, `temporary_metadata.unlink`, `temporary_metadata.write_text`, `temporary_path.unlink`
- Hashing effects: `sha256`, `sha256(archive_bytes).hexdigest`
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasDownload`, `InpnProtectedAreasSourceError`, `_archive_path`, `_download_archive_bytes`, `_download_metadata`, `_load_cached_download`, `_metadata_path`, `_publish_cache_pair`, `_validated_config`, `_validated_zip_members`, `archive_path.parent.mkdir`, `archive_path.with_name`, `datetime.now`, `datetime.now(UTC).isoformat`, `float`, `io.BytesIO`, `isfinite`, `isinstance`, `len`, `metadata.model_dump_json`, `metadata_path.with_name`, `sha256`, `sha256(archive_bytes).hexdigest`, `str`, `temporary_archive.read_bytes`, `temporary_archive.unlink`, `temporary_metadata.unlink`, `temporary_metadata.write_text`, `temporary_path.unlink`, `zipfile.ZipFile`.
- Internal caller/callee relationship: directly calls `_archive_path`, `_download_archive_bytes`, `_download_metadata`, `_load_cached_download`, `_metadata_path`, `_publish_cache_pair`, `_validated_config`, `_validated_zip_members`; the public flows below establish external entry points.
- Direct tests: `test_wrong_download_config_type_has_controlled_error`, `test_download_timeout_is_strict_finite_positive`, `test_download_api_has_no_arbitrary_http_session_injection`, `test_valid_physical_and_metadata_cache_is_reused`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_validate_download_envelope`

- Exact signature: `def _validate_download_envelope(download: object, config: InpnProtectedAreasSourceConfig) -> InpnProtectedAreasDownload`
- Purpose: Revalidates exact download lineage, canonical scalars, timestamp, configured path identity, and safe regular-file status without reading content.
- Inputs: `download: object`, `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasDownload`.
- Ordered algorithm:

1. line 752: branch/fail closed on `type(download) is not InpnProtectedAreasDownload`.
2. line 756: derive `expected`.
3. line 767: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(AttributeError, OSError, TypeError, ValueError)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('download must be an exact InpnProtectedAreasDownload')`; `ValueError('Download lineage differs from config')`; `ValueError('Download path differs from configured cache identity')`; `ValueError('Download cache_hit must be boolean')`; `ValueError('Download integrity scalars are invalid')`; `ValueError('Downloaded archive path is missing or unsafe')`; `InpnProtectedAreasSourceError('INPN protected-areas download is stale or invalid')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `ValueError`, `_archive_path`, `_is_regular_file`, `_validate_utc_timestamp`, `any`, `expected.items`, `getattr`, `isinstance`, `re.fullmatch`, `str`, `type`.
- Internal caller/callee relationship: directly calls `_archive_path`, `_is_regular_file`, `_validate_utc_timestamp`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_read_verified_archive_bytes`

- Exact signature: `def _read_verified_archive_bytes(download: object, config: InpnProtectedAreasSourceConfig) -> bytes`
- Purpose: Revalidates exact config/download authority, reads the archive path once, and accepts the immutable built-in bytes only at exact configured size/SHA.
- Inputs: `download: object`, `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `bytes`.
- Ordered algorithm:

1. line 801: derive `validated_config`.
2. line 802: derive `validated_download`.
3. line 803: controlled try/except boundary for `(AttributeError, OSError, TypeError, ValueError)` with visible cleanup/finalization.

- Validation: `ValueError('Downloaded archive snapshot is empty or non-canonical')`; `ValueError('Downloaded archive size changed')`; `ValueError('Downloaded archive SHA256 changed')`; `InpnProtectedAreasSourceError('INPN protected-areas archive byte snapshot is stale or invalid')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `validated_download.path.read_bytes`
- Hashing effects: `sha256`, `sha256(archive_bytes).hexdigest`
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `ValueError`, `_validate_download_envelope`, `_validated_config`, `len`, `sha256`, `sha256(archive_bytes).hexdigest`, `type`, `validated_download.path.read_bytes`.
- Internal caller/callee relationship: directly calls `_validate_download_envelope`, `_validated_config`; the public flows below establish external entry points.
- Direct tests: `test_archive_derived_inventory_equals_marker_physical_and_caller`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_validate_download`

- Exact signature: `def _validate_download(download: object, config: InpnProtectedAreasSourceConfig) -> InpnProtectedAreasDownload`
- Purpose: Validates a download and ZIP member structure from one verified immutable archive byte snapshot.
- Inputs: `download: object`, `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasDownload`.
- Ordered algorithm:

1. line 829: derive `validated_download`.
2. line 830: derive `archive_bytes`.
3. line 831: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(NotImplementedError, OSError, RuntimeError, ValueError, zipfile.BadZipFile, zlib.error)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('INPN protected-areas download is stale or invalid')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `_read_verified_archive_bytes`, `_validate_download_envelope`, `_validated_zip_members`, `io.BytesIO`, `zipfile.ZipFile`.
- Internal caller/callee relationship: directly calls `_read_verified_archive_bytes`, `_validate_download_envelope`, `_validated_zip_members`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_validate_inventory_relative_path`

- Exact signature: `def _validate_inventory_relative_path(value: object) -> None`
- Purpose: Validate inventory relative path.
- Inputs: `value: object`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 851: branch/fail closed on `type(value) is not str or not value or value != value.strip()`.
2. line 853: derive `(destination, _)`.
3. line 854: branch/fail closed on `destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME`.

- Validation: `ValueError('Inventory relative_path must be an exact non-empty string')`; `ValueError('Inventory relative_path is not canonical POSIX form')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `ValueError`, `_canonical_member_destination`, `destination.as_posix`, `type`, `value.strip`.
- Internal caller/callee relationship: directly calls `_canonical_member_destination`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_inventory`

- Exact signature: `def _inventory(root: Path) -> tuple[InpnProtectedAreasExtractedFile, ...]`
- Purpose: Inventory.
- Inputs: `root: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `tuple[InpnProtectedAreasExtractedFile, ...]`.
- Ordered algorithm:

1. line 859: branch/fail closed on `_is_link_or_junction(root) or not root.is_dir()`.
2. line 863: derive `files`.
3. line 864: iterate `path` over `root.rglob('*')` in source order.
4. line 893: perform `files.sort(key=lambda item: item.relative_path)`.
5. line 894: branch/fail closed on `not files`.
6. line 898: return `tuple(files)`.

- Validation: `InpnProtectedAreasSourceError('Extraction root must be a regular directory')`; `InpnProtectedAreasSourceError('Extracted INPN archive contains no regular files')`; `InpnProtectedAreasSourceError(f'Extracted link or junction is forbidden: {path}')`; `InpnProtectedAreasSourceError(f'Extracted special filesystem entry is forbidden: {path}')`; `InpnProtectedAreasSourceError(f'Cannot inventory extracted file: {relative_path}')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `path.stat`, `root.rglob`
- Hashing effects: `_sha256_file`
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasExtractedFile`, `InpnProtectedAreasSourceError`, `_is_link_or_junction`, `_sha256_file`, `_validate_inventory_relative_path`, `files.append`, `files.sort`, `path.is_dir`, `path.is_file`, `path.relative_to`, `path.relative_to(root).as_posix`, `path.stat`, `root.is_dir`, `root.rglob`, `tuple`.
- Internal caller/callee relationship: directly calls `_is_link_or_junction`, `_sha256_file`, `_validate_inventory_relative_path`; the public flows below establish external entry points.
- Direct tests: `test_complete_zip_inventory_is_validated_before_member_copy`, `test_extraction_validates_complete_inventory_before_copying`, `test_extraction_inventory_is_complete_ordered_and_hashed`, `test_public_api_exports_only_stable_high_level_symbols`, `test_result_schemas_are_factual_inventory_only`, `test_exact_file_inventory_does_not_omit_unknown_suffixes`, `test_extraction_revalidation_rejects_forged_file_inventory`, `test_extraction_revalidation_rejects_physical_inventory_mutation`, `test_archive_derived_inventory_equals_marker_physical_and_caller`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_extraction_metadata`

- Exact signature: `def _extraction_metadata(download: InpnProtectedAreasDownload, files: tuple[InpnProtectedAreasExtractedFile, ...]) -> _ExtractionMetadata`
- Purpose: Extraction metadata.
- Inputs: `download: InpnProtectedAreasDownload`, `files: tuple[InpnProtectedAreasExtractedFile, ...]`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `_ExtractionMetadata`.
- Ordered algorithm:

1. line 905: return `_ExtractionMetadata(schema_version=EXTRACTION_METADATA_SCHEMA_VERSION, archive_sha256=download.sha256, archive_size=download.file_size, files=tuple((_ExtractedFileMetadata(relative_path=item.relative_path, file_size=item.file_size, sha256=item.sha256) for item in files)))`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `_ExtractedFileMetadata`, `_ExtractionMetadata`, `tuple`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_extraction_inventory_is_complete_ordered_and_hashed`, `test_invalid_extraction_cache_is_rebuilt`, `test_archive_derived_inventory_equals_marker_physical_and_caller`, `test_invalid_coordinated_cache_rebuilds_from_local_archive_without_network`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_validate_extraction_cache`

- Exact signature: `def _validate_extraction_cache(root: Path, download: InpnProtectedAreasDownload, archive_files: tuple[InpnProtectedAreasExtractedFile, ...]) -> tuple[InpnProtectedAreasExtractedFile, ...]`
- Purpose: Proves exact equality of archive-derived, schema-v1 marker, and freshly hashed physical inventories.
- Inputs: `root: Path`, `download: InpnProtectedAreasDownload`, `archive_files: tuple[InpnProtectedAreasExtractedFile, ...]`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `tuple[InpnProtectedAreasExtractedFile, ...]`.
- Ordered algorithm:

1. line 925: derive `marker`.
2. line 926: branch/fail closed on `not _is_regular_file(marker)`.
3. line 930: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(OSError, TypeError, ValueError, ValidationError, json.JSONDecodeError)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('Extraction integrity metadata is missing or unsafe')`; `ValueError('Extraction metadata archive lineage differs')`; `ValueError('Archive, extraction metadata, and physical files differ')`; `InpnProtectedAreasSourceError('Extraction cache archive and physical inventory validation failed')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasExtractedFile`, `InpnProtectedAreasSourceError`, `ValueError`, `_ExtractionMetadata.model_validate`, `_inventory`, `_is_regular_file`, `_read_strict_json`, `tuple`.
- Internal caller/callee relationship: directly calls `_inventory`, `_is_regular_file`, `_read_strict_json`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_path_exists`

- Exact signature: `def _path_exists(path: Path) -> bool`
- Purpose: Path exists.
- Inputs: `path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `bool`.
- Ordered algorithm:

1. line 964: return `path.exists() or path.is_symlink() or _is_link_or_junction(path)`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `_is_link_or_junction`, `path.exists`, `path.is_symlink`.
- Internal caller/callee relationship: directly calls `_is_link_or_junction`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_remove_path`

- Exact signature: `def _remove_path(path: Path) -> None`
- Purpose: Remove path.
- Inputs: `path: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 968: branch/fail closed on `path.is_junction()`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `path.unlink`, `shutil.rmtree`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `path.exists`, `path.is_file`, `path.is_junction`, `path.is_symlink`, `path.rmdir`, `path.unlink`, `shutil.rmtree`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_replace_directory`

- Exact signature: `def _replace_directory(source: Path, target: Path) -> None`
- Purpose: Replace directory.
- Inputs: `source: Path`, `target: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 977: perform `source.replace(target)`.

- Validation: delegated to the exact callees and library contracts shown.
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `source.replace`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `source.replace`.
- Internal caller/callee relationship: directly calls no module helper; the public flows below establish external entry points.
- Direct tests: `test_first_extraction_publication_failure_leaves_no_half_root`, `test_extraction_replacement_failure_restores_old_tree`, `test_extraction_rollback_failure_preserves_backup`, `test_extraction_backup_move_failure_leaves_old_tree_untouched`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `_publish_extraction_directory`

- Exact signature: `def _publish_extraction_directory(temporary_root: Path, root: Path) -> None`
- Purpose: Publish extraction directory.
- Inputs: `temporary_root: Path`, `root: Path`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 981: derive `backup`.
2. line 982: branch/fail closed on `_path_exists(backup)`.
3. line 986: derive `old_moved`.
4. line 987: branch/fail closed on `_path_exists(root)`.
5. line 995: controlled try/except boundary for `OSError` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('Extraction recovery backup already exists; manual recovery is required')`; `InpnProtectedAreasSourceError('INPN extraction publication failed')`; `InpnProtectedAreasSourceError('Cannot stage existing INPN extraction for publication')`; `InpnProtectedAreasSourceError('INPN extraction publication and rollback both failed')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasSourceError`, `_path_exists`, `_remove_path`, `_replace_directory`, `root.with_name`.
- Internal caller/callee relationship: directly calls `_path_exists`, `_remove_path`, `_replace_directory`; the public flows below establish external entry points.
- Direct tests: covered transitively through public acquisition/extraction tests.
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `extract_inpn_protected_areas_archive`

- Exact signature: `def extract_inpn_protected_areas_archive(download: InpnProtectedAreasDownload, config: InpnProtectedAreasSourceConfig) -> InpnProtectedAreasExtraction`
- Purpose: Returns a four-way-valid cache hit or transactionally rebuilds extraction by streaming from the same snapshot used for member validation/inventory.
- Inputs: `download: InpnProtectedAreasDownload`, `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasExtraction`.
- Ordered algorithm:

1. line 1017: perform `'Safely extract all regular files and bind an exact factual inventory.'`.
2. line 1019: derive `validated_config`.
3. line 1020: derive `validated_download`.
4. line 1021: derive `archive_bytes`.
5. line 1022: derive `root`.
6. line 1023: derive `temporary_root`.
7. line 1024: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(NotImplementedError, OSError, RuntimeError, ValueError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('Extracted files differ from the verified archive inventory')`; `InpnProtectedAreasSourceError('Cannot safely extract the INPN protected-areas archive')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: `(temporary_root / EXTRACTION_METADATA_FILENAME).write_text`, `archive.open`, `root.parent.mkdir`, `target.mkdir`, `target.open`, `target.parent.mkdir`, `temporary_root.mkdir`
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `(temporary_root / EXTRACTION_METADATA_FILENAME).write_text`, `InpnProtectedAreasExtraction`, `InpnProtectedAreasSourceError`, `_archive_regular_file_inventory`, `_extraction_metadata`, `_inventory`, `_is_link_or_junction`, `_publish_extraction_directory`, `_read_verified_archive_bytes`, `_remove_path`, `_validate_download_envelope`, `_validate_extraction_cache`, `_validated_config`, `_validated_zip_members`, `archive.open`, `copyfileobj`, `io.BytesIO`, `metadata.model_dump_json`, `root.is_dir`, `root.parent.mkdir`, `root.with_name`, `target.mkdir`, `target.open`, `target.parent.mkdir`, `temporary_root.joinpath`, `temporary_root.mkdir`, `zipfile.ZipFile`.
- Internal caller/callee relationship: directly calls `_archive_regular_file_inventory`, `_extraction_metadata`, `_inventory`, `_is_link_or_junction`, `_publish_extraction_directory`, `_read_verified_archive_bytes`, `_remove_path`, `_validate_download_envelope`, `_validate_extraction_cache`, `_validated_config`, `_validated_zip_members`; the public flows below establish external entry points.
- Direct tests: `test_extraction_validates_complete_inventory_before_copying`, `test_extraction_inventory_is_complete_ordered_and_hashed`, `test_valid_extraction_cache_is_reused`, `test_invalid_extraction_cache_is_rebuilt`, `test_first_extraction_publication_failure_leaves_no_half_root`, `test_extraction_replacement_failure_restores_old_tree`, `test_extraction_rollback_failure_preserves_backup`, `test_extraction_backup_move_failure_leaves_old_tree_untouched`, `test_extraction_rejects_wrong_download_type`, `test_extraction_rejects_wrong_config_type`, `test_extraction_cache_setup_failure_is_controlled`, `test_extraction_rejects_stale_download_bytes`, `test_result_dataclasses_are_frozen`, `test_exact_file_inventory_does_not_omit_unknown_suffixes`, `test_archive_and_extraction_cache_reuse_are_independent`, `test_no_stale_parts_after_download_or_extraction_success`, `test_extraction_revalidation_returns_fresh_source_bound_result`, `test_extraction_revalidation_rejects_wrong_path`, `test_extraction_revalidation_rejects_forged_file_inventory`, `test_extraction_revalidation_rejects_physical_inventory_mutation`, `test_extraction_revalidation_rejects_link_or_junction_file`, `test_archive_derived_inventory_equals_marker_physical_and_caller`, `test_coordinated_marker_physical_and_caller_forgery_cannot_override_archive`, `test_invalid_coordinated_cache_rebuilds_from_local_archive_without_network`, `test_transient_archive_path_swap_cannot_change_extracted_member_bytes`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

### `validate_inpn_protected_areas_extraction`

- Exact signature: `def validate_inpn_protected_areas_extraction(extraction: InpnProtectedAreasExtraction, config: InpnProtectedAreasSourceConfig) -> InpnProtectedAreasExtraction`
- Purpose: Reconstructs the public source authority and returns archive-derived files after archive/marker/physical/caller equality.
- Inputs: `extraction: InpnProtectedAreasExtraction`, `config: InpnProtectedAreasSourceConfig`; exact defaults/keyword-only placement are in the signature and source snapshot.
- Output: `InpnProtectedAreasExtraction`.
- Ordered algorithm:

1. line 1101: perform `'Rebuild one extraction envelope from its current verified physical files.'`.
2. line 1103: controlled try/except boundary for `InpnProtectedAreasSourceError`, `(AttributeError, OSError, TypeError, ValueError)` with visible cleanup/finalization.

- Validation: `InpnProtectedAreasSourceError('extraction must be an exact InpnProtectedAreasExtraction')`; `InpnProtectedAreasSourceError('extraction download must be an exact InpnProtectedAreasDownload')`; `InpnProtectedAreasSourceError('extraction path must be a pathlib Path')`; `InpnProtectedAreasSourceError('extraction cache_hit must be boolean')`; `InpnProtectedAreasSourceError('extraction inventory must be an exact immutable file tuple')`; `InpnProtectedAreasSourceError('extraction path differs from the configured source identity')`; `InpnProtectedAreasSourceError('archive, marker, physical, and caller extraction inventory differs')`; `InpnProtectedAreasSourceError('INPN protected-areas extraction revalidation failed safely')`; `InpnProtectedAreasSourceError('extraction inventory file size must be a non-negative integer')`; `InpnProtectedAreasSourceError('extraction inventory file SHA256 is invalid')`
- Exceptions: explicit source errors above plus only those library errors not contained by a visible controlled boundary; public APIs normalize failures to `InpnProtectedAreasSourceError`.
- Filesystem effects: none directly; any effects are delegated.
- Hashing effects: none directly.
- Pyogrio calls: none; this adapter does not inspect GeoPackages.
- Callees: `InpnProtectedAreasDownload`, `InpnProtectedAreasExtraction`, `InpnProtectedAreasSourceError`, `_archive_regular_file_inventory`, `_read_verified_archive_bytes`, `_validate_download_envelope`, `_validate_extraction_cache`, `_validate_inventory_relative_path`, `_validated_config`, `_validated_zip_members`, `any`, `io.BytesIO`, `isinstance`, `re.fullmatch`, `type`, `zipfile.ZipFile`.
- Internal caller/callee relationship: directly calls `_archive_regular_file_inventory`, `_read_verified_archive_bytes`, `_validate_download_envelope`, `_validate_extraction_cache`, `_validate_inventory_relative_path`, `_validated_config`, `_validated_zip_members`; the public flows below establish external entry points.
- Direct tests: `test_extraction_revalidation_returns_fresh_source_bound_result`, `test_extraction_revalidation_rejects_wrong_type`, `test_extraction_revalidation_rejects_wrong_path`, `test_extraction_revalidation_rejects_forged_file_inventory`, `test_extraction_revalidation_rejects_physical_inventory_mutation`, `test_extraction_revalidation_rejects_link_or_junction_file`, `test_archive_derived_inventory_equals_marker_physical_and_caller`, `test_coordinated_marker_physical_and_caller_forgery_cannot_override_archive`, `test_invalid_coordinated_cache_rebuilds_from_local_archive_without_network`
- Business boundary: official byte acquisition, cache integrity, ZIP safety, extraction, and factual file inventory only.
- Explicit non-goals: no GeoPackage opening, EP feature rows, categories, Natura 2000/ZNIEFF meaning, geometry normalization, parcels, intersections, exclusions, scores, or rankings.

## 6. Public flows, side effects, and trust ordering

1. `load_inpn_protected_areas_source_config` parses strict YAML into the frozen pinned identity.
2. `download_inpn_protected_areas_archive` validates local cache bytes before any transport and otherwise preserves the established safe-HTTPS transactional publication/recovery behavior.
3. `_read_verified_archive_bytes` reads a safe archive path exactly once and binds built-in bytes to configured/download size and SHA.
4. `_validated_zip_members` and `_archive_regular_file_inventory` consume the same open `ZipFile(BytesIO(snapshot))`; extraction streams the same validated members from it.
5. `_validate_extraction_cache` exact-compares archive-derived, marker, and physical inventories. The public validator additionally exact-compares caller `files` and returns archive-derived evidence.

## 7. Exact public exports

```python
__all__ = [
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasSourceConfig",
    "InpnProtectedAreasSourceError",
    "download_inpn_protected_areas_archive",
    "extract_inpn_protected_areas_archive",
    "load_inpn_protected_areas_source_config",
    "validate_inpn_protected_areas_extraction",
]
```

`validate_inpn_protected_areas_extraction` is present in the exact production `__all__` declaration and is the catalog's source-complete trust boundary.

## 8. Test and change-impact map

`tests/unit/test_inpn_protected_areas_fr.py` contains 147 collected cases. It covers strict config/download models, cache hit/miss/recovery, safe transport delegation, ZIP namespace/content attacks, extraction transactionality, fresh revalidation, archive-derived equality, coordinated marker/file forgery, local offline rebuild, and archive path-swap isolation. Catalog regressions separately prove corruption is rejected before Pyogrio.

Changes require both INPN focused suites, the controlled zero-network real EP run, source SHA synchronization, full pytest, Ruff, mypy, uv lock/pip checks, and `git diff --check`.

## 9. Exact complete current file content

The raw-byte SHA above binds this complete current source snapshot.

```python
"""Verified acquisition and factual inventory of the official INPN EP archive.

This source adapter deliberately stops at byte acquisition, safe extraction,
and exact file inventory.  It does not interpret protected-area categories,
open spatial files, intersect parcels, or produce environmental decisions.
"""

from __future__ import annotations

import io
import json
import re
import shutil
import stat
import unicodedata
import zipfile
import zlib
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from math import isfinite
from numbers import Real
from pathlib import Path, PurePosixPath, PureWindowsPath
from shutil import copy2, copyfileobj
from typing import Annotated, Literal, Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    ValidationError,
    field_validator,
    model_validator,
)

from landscout.common.safe_http import SafeHttpsError, open_safe_https
from landscout.common.strict_json import loads_strict_json_object
from landscout.common.strict_yaml import loads_strict_yaml

DEFAULT_CONFIG_PATH = Path("configs/sources/inpn_protected_areas_fr.yaml")
DOWNLOAD_CHUNK_SIZE = 1024 * 1024
DOWNLOAD_METADATA_SCHEMA_VERSION: Literal[1] = 1
EXTRACTION_METADATA_SCHEMA_VERSION: Literal[1] = 1
EXTRACTION_METADATA_FILENAME = ".landscout-extraction.json"

OFFICIAL_REFERENCE_PAGE_URL = (
    "https://www.patrinat.fr/fr/"
    "page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353"
)
OFFICIAL_ARCHIVE_URL = "https://assets.patrinat.fr/files/donnees/ep/EP.zip"
OFFICIAL_DATASET_NAME = "Base de référence des espaces protégés français"

CanonicalSha256 = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^[0-9a-f]{64}$"),
]
DeclaredVersion = Annotated[
    str,
    StringConstraints(strict=True, pattern=r"^(?:0[1-9]|1[0-2])/\d{4}$"),
]
StrictPositiveInt = Annotated[int, Field(strict=True, gt=0)]
StrictNonNegativeInt = Annotated[int, Field(strict=True, ge=0)]

_WINDOWS_RESERVED_BASENAMES = frozenset(
    {
        "con",
        "prn",
        "aux",
        "nul",
        "clock$",
        *(f"com{index}" for index in range(1, 10)),
        *(f"lpt{index}" for index in range(1, 10)),
    }
)


class InpnProtectedAreasSourceError(ValueError):
    """Raised when the pinned INPN source cannot be handled safely."""


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


@dataclass(frozen=True)
class InpnProtectedAreasDownload:
    provider: str
    authority: str
    program: str
    dataset_id: str
    dataset_name: str
    declared_version: str
    reference_page_url: str
    archive_url: str
    download_timestamp: str
    filename: str
    file_size: int
    sha256: str
    path: Path
    cache_hit: bool


@dataclass(frozen=True)
class InpnProtectedAreasExtractedFile:
    relative_path: str
    file_size: int
    sha256: str


@dataclass(frozen=True)
class InpnProtectedAreasExtraction:
    download: InpnProtectedAreasDownload
    extraction_path: Path
    files: tuple[InpnProtectedAreasExtractedFile, ...]
    cache_hit: bool


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


@dataclass(frozen=True)
class _ValidatedZipMember:
    info: zipfile.ZipInfo
    destination: PurePosixPath
    is_directory: bool


def _validate_utc_timestamp(value: object) -> None:
    if type(value) is not str or not value or value != value.strip():
        raise ValueError("download_timestamp must be an exact non-empty string")
    parsed = datetime.fromisoformat(value)
    offset = parsed.utcoffset()
    if parsed.tzinfo is None or offset is None:
        raise ValueError("download_timestamp must be timezone-aware")
    if offset.total_seconds() != 0:
        raise ValueError("download_timestamp must use UTC")


def _validated_config(config: object) -> InpnProtectedAreasSourceConfig:
    if type(config) is not InpnProtectedAreasSourceConfig:
        raise InpnProtectedAreasSourceError(
            "config must be an exact InpnProtectedAreasSourceConfig"
        )
    try:
        return InpnProtectedAreasSourceConfig.model_validate(
            config.model_dump(mode="python")
        )
    except (AttributeError, TypeError, ValueError, ValidationError) as error:
        raise InpnProtectedAreasSourceError(
            "INPN protected-areas config is invalid"
        ) from error


def load_inpn_protected_areas_source_config(
    path: Path = DEFAULT_CONFIG_PATH,
) -> InpnProtectedAreasSourceConfig:
    """Load the explicit, version-pinned PatriNat EP source configuration."""

    if not isinstance(path, Path):
        raise InpnProtectedAreasSourceError("Config path must be a pathlib Path")
    try:
        payload = loads_strict_yaml(path.read_bytes())
        if type(payload) is not dict:
            raise ValueError("Expected a YAML mapping")
        return InpnProtectedAreasSourceConfig.model_validate(payload)
    except (OSError, TypeError, ValueError, ValidationError) as error:
        raise InpnProtectedAreasSourceError(
            f"Cannot load INPN protected-areas source config: {path}"
        ) from error


def _cache_directory(config: InpnProtectedAreasSourceConfig) -> Path:
    version = config.declared_version.replace("/", "-")
    return config.cache_root / config.dataset_id / version


def _archive_path(config: InpnProtectedAreasSourceConfig) -> Path:
    return _cache_directory(config) / config.archive_filename


def _metadata_path(archive_path: Path) -> Path:
    return archive_path.with_name(f"{archive_path.name}.metadata.json")


def _sha256_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(DOWNLOAD_CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _is_regular_file(path: Path) -> bool:
    return not _is_link_or_junction(path) and path.is_file()


def _read_strict_json(path: Path) -> dict[str, object]:
    return loads_strict_json_object(path.read_bytes())


def _windows_component_key(component: str) -> str:
    normalized = unicodedata.normalize("NFKC", component)
    if (
        not normalized
        or normalized in {".", ".."}
        or normalized != normalized.strip()
        or normalized.endswith((" ", "."))
        or any(ord(character) < 32 or ord(character) == 127 for character in normalized)
        or any(character in '<>:"/\\|?*' for character in normalized)
    ):
        raise InpnProtectedAreasSourceError(
            f"Unsafe Windows-compatible ZIP component: {component}"
        )
    stem = normalized.split(".", 1)[0].casefold()
    if stem in _WINDOWS_RESERVED_BASENAMES:
        raise InpnProtectedAreasSourceError(
            f"Reserved Windows device name in ZIP member: {component}"
        )
    return normalized.casefold()


def _canonical_member_destination(name: str) -> tuple[PurePosixPath, tuple[str, ...]]:
    if type(name) is not str or not name or "\x00" in name:
        raise InpnProtectedAreasSourceError("ZIP member name is empty or invalid")
    if any(ord(character) < 32 or ord(character) == 127 for character in name):
        raise InpnProtectedAreasSourceError(
            "ZIP member name contains control characters"
        )
    posix = PurePosixPath(name.replace("\\", "/"))
    windows = PureWindowsPath(name)
    if posix.is_absolute() or windows.is_absolute() or bool(windows.drive):
        raise InpnProtectedAreasSourceError(
            f"Absolute ZIP member path is unsafe: {name}"
        )
    if ".." in posix.parts:
        raise InpnProtectedAreasSourceError(f"ZIP member traversal is unsafe: {name}")
    parts = tuple(part for part in posix.parts if part not in {"", "."})
    if not parts:
        raise InpnProtectedAreasSourceError("ZIP member has no normalized destination")
    canonical = tuple(_windows_component_key(part) for part in parts)
    if canonical[0] == EXTRACTION_METADATA_FILENAME.casefold():
        raise InpnProtectedAreasSourceError(
            "ZIP member collides with the extraction metadata path"
        )
    return PurePosixPath(*parts), canonical


def _validated_zip_members(
    archive: zipfile.ZipFile,
) -> tuple[_ValidatedZipMember, ...]:
    try:
        infos = archive.infolist()
        if not infos:
            raise InpnProtectedAreasSourceError("ZIP archive contains no members")
        raw_names: set[str] = set()
        explicit: dict[tuple[str, ...], str] = {}
        files: set[tuple[str, ...]] = set()
        directories: set[tuple[str, ...]] = set()
        validated: list[_ValidatedZipMember] = []
        regular_count = 0
        for info in infos:
            name = info.filename
            if name in raw_names:
                raise InpnProtectedAreasSourceError(
                    f"duplicate ZIP member name: {name}"
                )
            raw_names.add(name)
            if info.flag_bits & 0x1:
                raise InpnProtectedAreasSourceError(
                    f"Encrypted ZIP members are unsupported: {name}"
                )
            destination, canonical = _canonical_member_destination(name)
            mode = info.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise InpnProtectedAreasSourceError(
                    f"ZIP symbolic links are forbidden: {name}"
                )
            file_type = stat.S_IFMT(mode)
            if file_type not in {0, stat.S_IFREG, stat.S_IFDIR}:
                raise InpnProtectedAreasSourceError(
                    f"ZIP special files are forbidden: {name}"
                )
            is_directory = (
                info.is_dir() or name.endswith(("/", "\\")) or stat.S_ISDIR(mode)
            )
            if canonical in explicit:
                raise InpnProtectedAreasSourceError(
                    "ZIP members collide at one normalized destination: "
                    f"{explicit[canonical]} / {name}"
                )
            explicit[canonical] = name
            parents = tuple(canonical[:index] for index in range(1, len(canonical)))
            if any(parent in files for parent in parents):
                raise InpnProtectedAreasSourceError(
                    f"colliding ZIP file/directory destination: {name}"
                )
            if is_directory:
                if canonical in files:
                    raise InpnProtectedAreasSourceError(
                        f"colliding ZIP file/directory destination: {name}"
                    )
                directories.add(canonical)
            else:
                if canonical in directories:
                    raise InpnProtectedAreasSourceError(
                        f"colliding ZIP file/directory destination: {name}"
                    )
                files.add(canonical)
                regular_count += 1
            directories.update(parents)
            validated.append(_ValidatedZipMember(info, destination, is_directory))
        if regular_count == 0:
            raise InpnProtectedAreasSourceError("ZIP archive contains no regular files")
        bad_member = archive.testzip()
        if bad_member is not None:
            raise InpnProtectedAreasSourceError(f"Corrupt ZIP member: {bad_member}")
        return tuple(validated)
    except InpnProtectedAreasSourceError:
        raise
    except (
        NotImplementedError,
        OSError,
        RuntimeError,
        zipfile.BadZipFile,
        zipfile.LargeZipFile,
        zlib.error,
    ) as error:
        raise InpnProtectedAreasSourceError("Cannot validate ZIP archive") from error


def _archive_regular_file_inventory(
    archive: zipfile.ZipFile,
    members: tuple[_ValidatedZipMember, ...],
) -> tuple[InpnProtectedAreasExtractedFile, ...]:
    files: list[InpnProtectedAreasExtractedFile] = []
    try:
        for member in members:
            if member.is_directory:
                continue
            digest = sha256()
            file_size = 0
            with archive.open(member.info) as source:
                for chunk in iter(lambda: source.read(DOWNLOAD_CHUNK_SIZE), b""):
                    file_size += len(chunk)
                    digest.update(chunk)
            if file_size != member.info.file_size:
                raise InpnProtectedAreasSourceError(
                    f"ZIP member size changed while reading: {member.info.filename}"
                )
            files.append(
                InpnProtectedAreasExtractedFile(
                    relative_path=member.destination.as_posix(),
                    file_size=file_size,
                    sha256=digest.hexdigest(),
                )
            )
    except InpnProtectedAreasSourceError:
        raise
    except (
        NotImplementedError,
        OSError,
        RuntimeError,
        ValueError,
        zipfile.BadZipFile,
        zlib.error,
    ) as error:
        raise InpnProtectedAreasSourceError(
            "Cannot inventory regular files from the verified archive snapshot"
        ) from error
    files.sort(key=lambda item: item.relative_path)
    paths = tuple(item.relative_path for item in files)
    if not files or len(paths) != len(set(paths)):
        raise InpnProtectedAreasSourceError(
            "Archive-derived regular-file inventory is empty or ambiguous"
        )
    return tuple(files)


def _download_metadata(
    config: InpnProtectedAreasSourceConfig,
    result: InpnProtectedAreasDownload,
) -> _DownloadMetadata:
    return _DownloadMetadata(
        schema_version=DOWNLOAD_METADATA_SCHEMA_VERSION,
        provider=config.provider,
        authority=config.authority,
        program=config.program,
        dataset_id=config.dataset_id,
        dataset_name=config.dataset_name,
        declared_version=config.declared_version,
        reference_page_url=str(config.reference_page_url),
        archive_url=str(config.archive_url),
        filename=config.archive_filename,
        download_timestamp=result.download_timestamp,
        file_size=result.file_size,
        sha256=result.sha256,
    )


def _load_cached_download(
    archive_path: Path,
    metadata_path: Path,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload | None:
    if not _is_regular_file(archive_path) or not _is_regular_file(metadata_path):
        return None
    try:
        metadata = _DownloadMetadata.model_validate(_read_strict_json(metadata_path))
        expected = {
            "provider": config.provider,
            "authority": config.authority,
            "program": config.program,
            "dataset_id": config.dataset_id,
            "dataset_name": config.dataset_name,
            "declared_version": config.declared_version,
            "reference_page_url": str(config.reference_page_url),
            "archive_url": str(config.archive_url),
            "filename": config.archive_filename,
        }
        if any(getattr(metadata, key) != value for key, value in expected.items()):
            return None
        candidate = InpnProtectedAreasDownload(
            provider=metadata.provider,
            authority=metadata.authority,
            program=metadata.program,
            dataset_id=metadata.dataset_id,
            dataset_name=metadata.dataset_name,
            declared_version=metadata.declared_version,
            reference_page_url=metadata.reference_page_url,
            archive_url=metadata.archive_url,
            download_timestamp=metadata.download_timestamp,
            filename=metadata.filename,
            file_size=metadata.file_size,
            sha256=metadata.sha256,
            path=archive_path,
            cache_hit=True,
        )
        return _validate_download(candidate, config)
    except (
        InpnProtectedAreasSourceError,
        OSError,
        TypeError,
        ValueError,
        ValidationError,
        json.JSONDecodeError,
    ):
        return None


def _replace_file(source: Path, target: Path) -> None:
    source.replace(target)


def _publish_cache_pair(
    temporary_archive: Path,
    temporary_metadata: Path,
    archive_path: Path,
    metadata_path: Path,
) -> None:
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    if any(
        path.exists() or _is_link_or_junction(path)
        for path in (archive_backup, metadata_backup)
    ):
        raise InpnProtectedAreasSourceError(
            "Cache recovery backup already exists; manual recovery is required"
        )
    archive_existed = archive_path.is_file()
    metadata_existed = metadata_path.is_file()
    try:
        if archive_existed:
            copy2(archive_path, archive_backup)
        if metadata_existed:
            copy2(metadata_path, metadata_backup)
    except OSError:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise

    try:
        _replace_file(temporary_archive, archive_path)
        _replace_file(temporary_metadata, metadata_path)
    except OSError as publication_error:
        try:
            if archive_existed:
                _replace_file(archive_backup, archive_path)
            else:
                archive_path.unlink(missing_ok=True)
            if metadata_existed:
                _replace_file(metadata_backup, metadata_path)
            else:
                metadata_path.unlink(missing_ok=True)
        except OSError as rollback_error:
            raise InpnProtectedAreasSourceError(
                "INPN cache publication and rollback both failed"
            ) from rollback_error
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)
        raise InpnProtectedAreasSourceError(
            "INPN cache publication failed"
        ) from publication_error
    else:
        archive_backup.unlink(missing_ok=True)
        metadata_backup.unlink(missing_ok=True)


def _download_archive_bytes(
    configured_url: str,
    timeout_seconds: float,
    destination: Path,
) -> None:
    try:
        with open_safe_https(
            configured_url,
            timeout=timeout_seconds,
            headers={"User-Agent": "LandScout-AI/0.1"},
        ) as response:
            response_headers = getattr(response, "headers", None)
            header_get = getattr(response_headers, "get", None)
            if not callable(header_get):
                raise InpnProtectedAreasSourceError("HTTP response headers are invalid")
            content_type = str(header_get("Content-Type", ""))
            if "text/html" in content_type.casefold():
                raise InpnProtectedAreasSourceError(
                    "HTML response cannot be used as a ZIP"
                )
            with destination.open("xb") as output:
                copyfileobj(response, output, length=DOWNLOAD_CHUNK_SIZE)
    except InpnProtectedAreasSourceError:
        raise
    except (SafeHttpsError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "Official INPN archive download failed"
        ) from error


def download_inpn_protected_areas_archive(
    config: InpnProtectedAreasSourceConfig,
    *,
    timeout_seconds: float = 120.0,
) -> InpnProtectedAreasDownload:
    """Download or reuse the exact configured official EP ZIP bytes."""

    validated_config = _validated_config(config)
    if isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, Real):
        raise InpnProtectedAreasSourceError(
            "timeout_seconds must be a strict finite positive number"
        )
    try:
        validated_timeout = float(timeout_seconds)
    except (OverflowError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "timeout_seconds must be a strict finite positive number"
        ) from error
    if not isfinite(validated_timeout) or validated_timeout <= 0:
        raise InpnProtectedAreasSourceError(
            "timeout_seconds must be a strict finite positive number"
        )
    archive_path = _archive_path(validated_config)
    metadata_path = _metadata_path(archive_path)
    cached = _load_cached_download(archive_path, metadata_path, validated_config)
    if cached is not None:
        return cached

    temporary_archive = archive_path.with_name(f"{archive_path.name}.part")
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    try:
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_archive.unlink(missing_ok=True)
        temporary_metadata.unlink(missing_ok=True)
        _download_archive_bytes(
            str(validated_config.archive_url),
            validated_timeout,
            temporary_archive,
        )
        archive_bytes = temporary_archive.read_bytes()
        file_size = len(archive_bytes)
        checksum = sha256(archive_bytes).hexdigest()
        if (
            file_size != validated_config.expected_archive_size_bytes
            or checksum != validated_config.expected_archive_sha256
        ):
            raise InpnProtectedAreasSourceError(
                "Downloaded INPN archive differs from the configured snapshot"
            )
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
            _validated_zip_members(archive)
        result = InpnProtectedAreasDownload(
            provider=validated_config.provider,
            authority=validated_config.authority,
            program=validated_config.program,
            dataset_id=validated_config.dataset_id,
            dataset_name=validated_config.dataset_name,
            declared_version=validated_config.declared_version,
            reference_page_url=str(validated_config.reference_page_url),
            archive_url=str(validated_config.archive_url),
            download_timestamp=datetime.now(UTC).isoformat(),
            filename=validated_config.archive_filename,
            file_size=file_size,
            sha256=checksum,
            path=archive_path,
            cache_hit=False,
        )
        metadata = _download_metadata(validated_config, result)
        temporary_metadata.write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        _publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
        return result
    except InpnProtectedAreasSourceError:
        raise
    except (OSError, TypeError, ValueError, ValidationError) as error:
        raise InpnProtectedAreasSourceError(
            "Official INPN archive download or cache publication failed"
        ) from error
    finally:
        for temporary_path in (temporary_archive, temporary_metadata):
            try:
                temporary_path.unlink(missing_ok=True)
            except OSError:
                pass


def _validate_download_envelope(
    download: object,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload:
    if type(download) is not InpnProtectedAreasDownload:
        raise InpnProtectedAreasSourceError(
            "download must be an exact InpnProtectedAreasDownload"
        )
    expected = {
        "provider": config.provider,
        "authority": config.authority,
        "program": config.program,
        "dataset_id": config.dataset_id,
        "dataset_name": config.dataset_name,
        "declared_version": config.declared_version,
        "reference_page_url": str(config.reference_page_url),
        "archive_url": str(config.archive_url),
        "filename": config.archive_filename,
    }
    try:
        if any(getattr(download, key) != value for key, value in expected.items()):
            raise ValueError("Download lineage differs from config")
        if not isinstance(download.path, Path) or download.path != _archive_path(
            config
        ):
            raise ValueError("Download path differs from configured cache identity")
        if type(download.cache_hit) is not bool:
            raise ValueError("Download cache_hit must be boolean")
        if (
            type(download.file_size) is not int
            or download.file_size <= 0
            or download.file_size != config.expected_archive_size_bytes
            or type(download.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
            or download.sha256 != config.expected_archive_sha256
        ):
            raise ValueError("Download integrity scalars are invalid")
        _validate_utc_timestamp(download.download_timestamp)
        if not _is_regular_file(download.path):
            raise ValueError("Downloaded archive path is missing or unsafe")
        return download
    except InpnProtectedAreasSourceError:
        raise
    except (AttributeError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "INPN protected-areas download is stale or invalid"
        ) from error


def _read_verified_archive_bytes(
    download: object,
    config: InpnProtectedAreasSourceConfig,
) -> bytes:
    validated_config = _validated_config(config)
    validated_download = _validate_download_envelope(download, validated_config)
    try:
        archive_bytes = validated_download.path.read_bytes()
        if type(archive_bytes) is not bytes or not archive_bytes:
            raise ValueError("Downloaded archive snapshot is empty or non-canonical")
        if (
            len(archive_bytes) != validated_download.file_size
            or len(archive_bytes) != validated_config.expected_archive_size_bytes
        ):
            raise ValueError("Downloaded archive size changed")
        checksum = sha256(archive_bytes).hexdigest()
        if (
            checksum != validated_download.sha256
            or checksum != validated_config.expected_archive_sha256
        ):
            raise ValueError("Downloaded archive SHA256 changed")
        return archive_bytes
    except (AttributeError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "INPN protected-areas archive byte snapshot is stale or invalid"
        ) from error


def _validate_download(
    download: object,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasDownload:
    validated_download = _validate_download_envelope(download, config)
    archive_bytes = _read_verified_archive_bytes(validated_download, config)
    try:
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
            _validated_zip_members(archive)
        return validated_download
    except InpnProtectedAreasSourceError:
        raise
    except (
        NotImplementedError,
        OSError,
        RuntimeError,
        ValueError,
        zipfile.BadZipFile,
        zlib.error,
    ) as error:
        raise InpnProtectedAreasSourceError(
            "INPN protected-areas download is stale or invalid"
        ) from error


def _validate_inventory_relative_path(value: object) -> None:
    if type(value) is not str or not value or value != value.strip():
        raise ValueError("Inventory relative_path must be an exact non-empty string")
    destination, _ = _canonical_member_destination(value)
    if destination.as_posix() != value or value == EXTRACTION_METADATA_FILENAME:
        raise ValueError("Inventory relative_path is not canonical POSIX form")


def _inventory(root: Path) -> tuple[InpnProtectedAreasExtractedFile, ...]:
    if _is_link_or_junction(root) or not root.is_dir():
        raise InpnProtectedAreasSourceError(
            "Extraction root must be a regular directory"
        )
    files: list[InpnProtectedAreasExtractedFile] = []
    for path in root.rglob("*"):
        if _is_link_or_junction(path):
            raise InpnProtectedAreasSourceError(
                f"Extracted link or junction is forbidden: {path}"
            )
        if path.is_dir():
            continue
        if not path.is_file():
            raise InpnProtectedAreasSourceError(
                f"Extracted special filesystem entry is forbidden: {path}"
            )
        relative_path = path.relative_to(root).as_posix()
        if relative_path == EXTRACTION_METADATA_FILENAME:
            continue
        try:
            _validate_inventory_relative_path(relative_path)
            file_size = path.stat().st_size
            checksum = _sha256_file(path)
        except (OSError, ValueError) as error:
            raise InpnProtectedAreasSourceError(
                f"Cannot inventory extracted file: {relative_path}"
            ) from error
        files.append(
            InpnProtectedAreasExtractedFile(
                relative_path=relative_path,
                file_size=file_size,
                sha256=checksum,
            )
        )
    files.sort(key=lambda item: item.relative_path)
    if not files:
        raise InpnProtectedAreasSourceError(
            "Extracted INPN archive contains no regular files"
        )
    return tuple(files)


def _extraction_metadata(
    download: InpnProtectedAreasDownload,
    files: tuple[InpnProtectedAreasExtractedFile, ...],
) -> _ExtractionMetadata:
    return _ExtractionMetadata(
        schema_version=EXTRACTION_METADATA_SCHEMA_VERSION,
        archive_sha256=download.sha256,
        archive_size=download.file_size,
        files=tuple(
            _ExtractedFileMetadata(
                relative_path=item.relative_path,
                file_size=item.file_size,
                sha256=item.sha256,
            )
            for item in files
        ),
    )


def _validate_extraction_cache(
    root: Path,
    download: InpnProtectedAreasDownload,
    archive_files: tuple[InpnProtectedAreasExtractedFile, ...],
) -> tuple[InpnProtectedAreasExtractedFile, ...]:
    marker = root / EXTRACTION_METADATA_FILENAME
    if not _is_regular_file(marker):
        raise InpnProtectedAreasSourceError(
            "Extraction integrity metadata is missing or unsafe"
        )
    try:
        metadata = _ExtractionMetadata.model_validate(_read_strict_json(marker))
        if (
            metadata.archive_sha256 != download.sha256
            or metadata.archive_size != download.file_size
        ):
            raise ValueError("Extraction metadata archive lineage differs")
        expected = tuple(
            InpnProtectedAreasExtractedFile(
                relative_path=item.relative_path,
                file_size=item.file_size,
                sha256=item.sha256,
            )
            for item in metadata.files
        )
        actual = _inventory(root)
        if expected != archive_files or actual != archive_files:
            raise ValueError("Archive, extraction metadata, and physical files differ")
        return actual
    except InpnProtectedAreasSourceError:
        raise
    except (
        OSError,
        TypeError,
        ValueError,
        ValidationError,
        json.JSONDecodeError,
    ) as error:
        raise InpnProtectedAreasSourceError(
            "Extraction cache archive and physical inventory validation failed"
        ) from error


def _path_exists(path: Path) -> bool:
    return path.exists() or path.is_symlink() or _is_link_or_junction(path)


def _remove_path(path: Path) -> None:
    if path.is_junction():
        path.rmdir()
    elif path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)


def _replace_directory(source: Path, target: Path) -> None:
    source.replace(target)


def _publish_extraction_directory(temporary_root: Path, root: Path) -> None:
    backup = root.with_name(f"{root.name}.bak")
    if _path_exists(backup):
        raise InpnProtectedAreasSourceError(
            "Extraction recovery backup already exists; manual recovery is required"
        )
    old_moved = False
    if _path_exists(root):
        try:
            _replace_directory(root, backup)
        except OSError as staging_error:
            raise InpnProtectedAreasSourceError(
                "Cannot stage existing INPN extraction for publication"
            ) from staging_error
        old_moved = True
    try:
        _replace_directory(temporary_root, root)
    except OSError as publication_error:
        try:
            _remove_path(root)
            if old_moved:
                _replace_directory(backup, root)
        except OSError as rollback_error:
            raise InpnProtectedAreasSourceError(
                "INPN extraction publication and rollback both failed"
            ) from rollback_error
        raise InpnProtectedAreasSourceError(
            "INPN extraction publication failed"
        ) from publication_error
    else:
        _remove_path(backup)


def extract_inpn_protected_areas_archive(
    download: InpnProtectedAreasDownload,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasExtraction:
    """Safely extract all regular files and bind an exact factual inventory."""

    validated_config = _validated_config(config)
    validated_download = _validate_download_envelope(download, validated_config)
    archive_bytes = _read_verified_archive_bytes(validated_download, validated_config)
    root = validated_download.path.parent / "x" / validated_download.sha256
    temporary_root = root.with_name(f"{root.name}.part")
    try:
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
            members = _validated_zip_members(archive)
            archive_files = _archive_regular_file_inventory(archive, members)
            if root.is_dir() and not _is_link_or_junction(root):
                try:
                    files = _validate_extraction_cache(
                        root,
                        validated_download,
                        archive_files,
                    )
                    return InpnProtectedAreasExtraction(
                        download=validated_download,
                        extraction_path=root,
                        files=files,
                        cache_hit=True,
                    )
                except (InpnProtectedAreasSourceError, OSError):
                    pass

            root.parent.mkdir(parents=True, exist_ok=True)
            _remove_path(temporary_root)
            temporary_root.mkdir(parents=True)
            for member in members:
                target = temporary_root.joinpath(*member.destination.parts)
                if member.is_directory:
                    target.mkdir(parents=True, exist_ok=True)
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member.info) as source, target.open("xb") as output:
                    copyfileobj(source, output, length=DOWNLOAD_CHUNK_SIZE)
        files = _inventory(temporary_root)
        if files != archive_files:
            raise InpnProtectedAreasSourceError(
                "Extracted files differ from the verified archive inventory"
            )
        metadata = _extraction_metadata(validated_download, archive_files)
        (temporary_root / EXTRACTION_METADATA_FILENAME).write_text(
            metadata.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        files = _validate_extraction_cache(
            temporary_root,
            validated_download,
            archive_files,
        )
        _publish_extraction_directory(temporary_root, root)
        return InpnProtectedAreasExtraction(
            download=validated_download,
            extraction_path=root,
            files=files,
            cache_hit=False,
        )
    except InpnProtectedAreasSourceError:
        raise
    except (
        NotImplementedError,
        OSError,
        RuntimeError,
        ValueError,
        zipfile.BadZipFile,
        zipfile.LargeZipFile,
        zlib.error,
    ) as error:
        raise InpnProtectedAreasSourceError(
            "Cannot safely extract the INPN protected-areas archive"
        ) from error
    finally:
        try:
            _remove_path(temporary_root)
        except OSError:
            pass


def validate_inpn_protected_areas_extraction(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasExtraction:
    """Rebuild one extraction envelope from its current verified physical files."""

    try:
        validated_config = _validated_config(config)
        if type(extraction) is not InpnProtectedAreasExtraction:
            raise InpnProtectedAreasSourceError(
                "extraction must be an exact InpnProtectedAreasExtraction"
            )
        if type(extraction.download) is not InpnProtectedAreasDownload:
            raise InpnProtectedAreasSourceError(
                "extraction download must be an exact InpnProtectedAreasDownload"
            )
        if not isinstance(extraction.extraction_path, Path):
            raise InpnProtectedAreasSourceError(
                "extraction path must be a pathlib Path"
            )
        if type(extraction.cache_hit) is not bool:
            raise InpnProtectedAreasSourceError("extraction cache_hit must be boolean")
        if type(extraction.files) is not tuple or any(
            type(item) is not InpnProtectedAreasExtractedFile
            for item in extraction.files
        ):
            raise InpnProtectedAreasSourceError(
                "extraction inventory must be an exact immutable file tuple"
            )
        for item in extraction.files:
            _validate_inventory_relative_path(item.relative_path)
            if type(item.file_size) is not int or item.file_size < 0:
                raise InpnProtectedAreasSourceError(
                    "extraction inventory file size must be a non-negative integer"
                )
            if (
                type(item.sha256) is not str
                or re.fullmatch(r"[0-9a-f]{64}", item.sha256) is None
            ):
                raise InpnProtectedAreasSourceError(
                    "extraction inventory file SHA256 is invalid"
                )

        validated_download = _validate_download_envelope(
            extraction.download,
            validated_config,
        )
        archive_bytes = _read_verified_archive_bytes(
            validated_download,
            validated_config,
        )
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
            members = _validated_zip_members(archive)
            archive_files = _archive_regular_file_inventory(archive, members)
        expected_root = validated_download.path.parent / "x" / validated_download.sha256
        if extraction.extraction_path != expected_root:
            raise InpnProtectedAreasSourceError(
                "extraction path differs from the configured source identity"
            )
        fresh_files = _validate_extraction_cache(
            expected_root,
            validated_download,
            archive_files,
        )
        if extraction.files != archive_files or fresh_files != archive_files:
            raise InpnProtectedAreasSourceError(
                "archive, marker, physical, and caller extraction inventory differs"
            )
        fresh_download = InpnProtectedAreasDownload(
            provider=validated_download.provider,
            authority=validated_download.authority,
            program=validated_download.program,
            dataset_id=validated_download.dataset_id,
            dataset_name=validated_download.dataset_name,
            declared_version=validated_download.declared_version,
            reference_page_url=validated_download.reference_page_url,
            archive_url=validated_download.archive_url,
            download_timestamp=validated_download.download_timestamp,
            filename=validated_download.filename,
            file_size=validated_download.file_size,
            sha256=validated_download.sha256,
            path=validated_download.path,
            cache_hit=validated_download.cache_hit,
        )
        return InpnProtectedAreasExtraction(
            download=fresh_download,
            extraction_path=expected_root,
            files=archive_files,
            cache_hit=extraction.cache_hit,
        )
    except InpnProtectedAreasSourceError:
        raise
    except (AttributeError, OSError, TypeError, ValueError) as error:
        raise InpnProtectedAreasSourceError(
            "INPN protected-areas extraction revalidation failed safely"
        ) from error


__all__ = [
    "InpnProtectedAreasDownload",
    "InpnProtectedAreasExtractedFile",
    "InpnProtectedAreasExtraction",
    "InpnProtectedAreasSourceConfig",
    "InpnProtectedAreasSourceError",
    "download_inpn_protected_areas_archive",
    "extract_inpn_protected_areas_archive",
    "load_inpn_protected_areas_source_config",
    "validate_inpn_protected_areas_extraction",
]
```
