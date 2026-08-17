# `src/landscout/sources/cadastre_loader_fr.py`

## File identity

- Repository path: `src/landscout/sources/cadastre_loader_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: cadastre
- Responsibility: Validates a supplied CadastreDownload envelope and its current gzip bytes, then parses the source parcel attributes and polygon geometry without adding lineage columns.
- Source SHA256: `214f64a50a996dc9995b004b2efb03811a88b30ef4a2377a85bc2f8317ec5f07`

## 1. Purpose

Validates a supplied CadastreDownload envelope and its current gzip bytes, then parses the source parcel attributes and polygon geometry without adding lineage columns.

## 2. Position in LandScout architecture

This file belongs to the **source adapter** layer and the **cadastre** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import gzip`
- `import re`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from urllib.parse import urlparse`

### Third-party packages

- `import geopandas as gpd`
- `from pyogrio.errors import DataSourceError`

### Internal LandScout imports

- `from landscout.sources.cadastre_fr import CadastreDownload`

## 4. Contract taxonomy

### A. Python constants

#### `SUPPORTED_GEOMETRY_TYPES`

```python
SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `CadastreLoadError`

**Purpose:** Base error for controlled cadastre loading failures.

**Kind:** controlled exception.

**Inheritance:** `RuntimeError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::_physical_integrity` via `CadastreLoadError`.
- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::_validate_download` via `CadastreLoadError`.
- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `CadastreLoadError`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_missing_file_fails` via `pytest.raises(CadastreLoadError, match='exist')`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_invalid_file_fails` via `pytest.raises(CadastreLoadError)`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing` via `pytest.raises(CadastreLoadError, match=message)`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_wrong_public_input_type_is_controlled` via `pytest.raises(CadastreLoadError, match='CadastreDownload')`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing` via `pytest.raises(CadastreLoadError, match='SHA|checksum|gzip')`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `pytest.raises(CadastreLoadError, match='changed|SHA|size')`.
- import/re-export: `tests/unit/test_cadastre_loader_fr.py::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
)`.

**Exact class source**

```python
class CadastreLoadError(RuntimeError):
    """Base error for controlled cadastre loading failures."""
```

### `EmptyCadastreDatasetError`

**Purpose:** Raised when a cadastre dataset contains no parcel records.

**Kind:** controlled exception.

**Inheritance:** `CadastreLoadError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `EmptyCadastreDatasetError`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails` via `pytest.raises(EmptyCadastreDatasetError)`.
- import/re-export: `tests/unit/test_cadastre_loader_fr.py::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
)`.

**Exact class source**

```python
class EmptyCadastreDatasetError(CadastreLoadError):
    """Raised when a cadastre dataset contains no parcel records."""
```

### `MissingGeometryColumnError`

**Purpose:** Raised when a cadastre dataset has no active geometry column.

**Kind:** controlled exception.

**Inheritance:** `CadastreLoadError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `MissingGeometryColumnError`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_missing_geometry_column_fails` via `pytest.raises(MissingGeometryColumnError)`.
- import/re-export: `tests/unit/test_cadastre_loader_fr.py::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
)`.

**Exact class source**

```python
class MissingGeometryColumnError(CadastreLoadError):
    """Raised when a cadastre dataset has no active geometry column."""
```

### `UnsupportedGeometryTypeError`

**Purpose:** Raised when a cadastre dataset contains non-parcel geometry types.

**Kind:** controlled exception.

**Inheritance:** `CadastreLoadError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `UnsupportedGeometryTypeError`.
- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails` via `pytest.raises(UnsupportedGeometryTypeError, match='Point')`.
- import/re-export: `tests/unit/test_cadastre_loader_fr.py::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
)`.

**Exact class source**

```python
class UnsupportedGeometryTypeError(CadastreLoadError):
    """Raised when a cadastre dataset contains non-parcel geometry types."""
```


## 6. Functions and methods

### `_physical_integrity`

**Exact signature**

```python
def _physical_integrity(path: Path) -> tuple[int, str]:
```

**Purpose**

Private `cadastre` helper for physical integrity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[int, str]`.
- Every observed return expression is reproduced without truncation:
```python
(size, digest)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `CadastreLoadError(f'Cannot inspect cadastre dataset: {path}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.read_bytes`, `path.stat`, `sha256(path.read_bytes()).hexdigest`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(path.read_bytes()).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::_validate_download` via `_physical_integrity`.
- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `_physical_integrity`.

**Complete source-ordered implementation**

```python
def _physical_integrity(path: Path) -> tuple[int, str]:
    try:
        size = path.stat().st_size
        digest = sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        raise CadastreLoadError(f"Cannot inspect cadastre dataset: {path}") from error
    return size, digest
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_download`

**Exact signature**

```python
def _validate_download(download: object) -> CadastreDownload:
```

**Purpose**

Rejects malformed or inconsistent download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CadastreDownload`.
- Every observed return expression is reproduced without truncation:
```python
download
```

**Validation and exceptions**

- Guard with a raise path: `type(download) is not CadastreDownload`.
- Guard with a raise path: `not isinstance(path, Path)`.
- Guard with a raise path: `not path.is_file()`.
- Guard with a raise path: `not isinstance(download.source_url, str) or not download.source_url or download.source_url != download.source_url.strip() or (urlparse(download.source_url).scheme not in {'http', 'https'})`.
- Guard with a raise path: `not isinstance(download.filename, str) or not download.filename or download.filename != download.filename.strip() or (download.filename != path.name)`.
- Guard with a raise path: `type(download.file_size) is not int or download.file_size <= 0`.
- Guard with a raise path: `not isinstance(download.sha256, str) or re.fullmatch('[0-9a-f]{64}', download.sha256) is None`.
- Guard with a raise path: `size != download.file_size`.
- Guard with a raise path: `digest != download.sha256`.
- Explicit raise expressions: `CadastreLoadError('Cadastre download SHA256 must be lowercase hexadecimal')`, `CadastreLoadError('Cadastre download filename does not match its path')`, `CadastreLoadError('Cadastre download path must be a Path')`, `CadastreLoadError('Cadastre download size must be a strict positive integer')`, `CadastreLoadError('Cadastre download source URL is invalid')`, `CadastreLoadError('Cadastre physical SHA256 differs from verified download')`, `CadastreLoadError('Cadastre physical size differs from verified download')`, `CadastreLoadError('Cadastre source must be an exact CadastreDownload')`, `CadastreLoadError('Cadastre verified source is not valid gzip')`, `CadastreLoadError(f'Cadastre dataset does not exist: {path}')`.

**Side effects**

- Network I/O: `download.filename.strip`, `download.source_url.strip`.
- Filesystem read: `gzip.open`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::load_cadastre_parcels` via `_validate_download`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_validate_download`.

**Complete source-ordered implementation**

```python
def _validate_download(download: object) -> CadastreDownload:
    if type(download) is not CadastreDownload:
        raise CadastreLoadError("Cadastre source must be an exact CadastreDownload")
    path = download.path
    if not isinstance(path, Path):
        raise CadastreLoadError("Cadastre download path must be a Path")
    if not path.is_file():
        raise CadastreLoadError(f"Cadastre dataset does not exist: {path}")
    if (
        not isinstance(download.source_url, str)
        or not download.source_url
        or download.source_url != download.source_url.strip()
        or urlparse(download.source_url).scheme not in {"http", "https"}
    ):
        raise CadastreLoadError("Cadastre download source URL is invalid")
    if (
        not isinstance(download.filename, str)
        or not download.filename
        or download.filename != download.filename.strip()
        or download.filename != path.name
    ):
        raise CadastreLoadError("Cadastre download filename does not match its path")
    if type(download.file_size) is not int or download.file_size <= 0:
        raise CadastreLoadError("Cadastre download size must be a strict positive integer")
    if (
        not isinstance(download.sha256, str)
        or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
    ):
        raise CadastreLoadError("Cadastre download SHA256 must be lowercase hexadecimal")
    size, digest = _physical_integrity(path)
    if size != download.file_size:
        raise CadastreLoadError("Cadastre physical size differs from verified download")
    if digest != download.sha256:
        raise CadastreLoadError("Cadastre physical SHA256 differs from verified download")
    try:
        with gzip.open(path, "rb") as stream:
            while stream.read(1024 * 1024):
                pass
    except (EOFError, OSError) as error:
        raise CadastreLoadError("Cadastre verified source is not valid gzip") from error
    return download
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `load_cadastre_parcels`

**Exact signature**

```python
def load_cadastre_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
```

**Purpose**

Load parcels from one byte-verified cadastral download envelope.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
parcels
```

**Validation and exceptions**

- Guard with a raise path: `size_after != verified.file_size or digest_after != verified.sha256`.
- Guard with a raise path: `parcels.empty`.
- Guard with a raise path: `geometry_column is None or geometry_column not in parcels.columns`.
- Guard with a raise path: `unsupported_types`.
- Explicit raise expressions: `CadastreLoadError('Cadastre physical source changed during parsing')`, `CadastreLoadError(f'Unable to read cadastre dataset: {path}')`, `EmptyCadastreDatasetError(f'Cadastre dataset is empty: {path}')`, `MissingGeometryColumnError('Cadastre dataset has no geometry column')`, `UnsupportedGeometryTypeError(f'Unsupported cadastre geometry types: {formatted_types}')`.

**Side effects**

- Network I/O: `_validate_download`.
- Filesystem read: `gpd.read_file`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `MissingGeometryColumnError`, `UnsupportedGeometryTypeError`, `parcels.geometry.geom_type.dropna`, `parcels.geometry.geom_type.dropna().unique`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_missing_file_fails` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_invalid_file_fails` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_missing_geometry_column_fails` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_wrong_public_input_type_is_controlled` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing` via `load_cadastre_parcels`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `load_cadastre_parcels`.
- import/re-export: `tests/unit/test_cadastre_loader_fr.py::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
)`.

**Complete source-ordered implementation**

```python
def load_cadastre_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
    """Load parcels from one byte-verified cadastral download envelope."""

    verified = _validate_download(download)
    path = verified.path

    source = f"/vsigzip/{path.resolve().as_posix()}"
    try:
        parcels = gpd.read_file(source, engine="pyogrio")
    except (DataSourceError, OSError, ValueError) as error:
        raise CadastreLoadError(f"Unable to read cadastre dataset: {path}") from error

    size_after, digest_after = _physical_integrity(path)
    if size_after != verified.file_size or digest_after != verified.sha256:
        raise CadastreLoadError("Cadastre physical source changed during parsing")

    if parcels.empty:
        raise EmptyCadastreDatasetError(f"Cadastre dataset is empty: {path}")
    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise MissingGeometryColumnError("Cadastre dataset has no geometry column")

    geometry_types = set(parcels.geometry.geom_type.dropna().unique())
    unsupported_types = geometry_types - SUPPORTED_GEOMETRY_TYPES
    if unsupported_types:
        formatted_types = ", ".join(sorted(unsupported_types))
        raise UnsupportedGeometryTypeError(
            f"Unsupported cadastre geometry types: {formatted_types}"
        )
    return parcels
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.


## 7. Data contracts

### Frame-preservation and semantic notes

- `load_cadastre_parcels` returns the columns parsed from the GeoJSON plus its active geometry. It adds no provider, URL, timestamp, size, SHA256, or other lineage column; those facts remain only in the validated `CadastreDownload` argument.

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.

- Configured source identity: trusts the supplied exact CadastreDownload envelope; this loader does not independently pin the official hostname.
- URL validation: accepts an exact non-empty source_url whose scheme is currently http or https; this is a genuine narrower-than-adapter-origin code contract.
- Physical bytes: compares current size/SHA, fully reads gzip, parses, and compares size/SHA again.
- Returned frame: parsed source attributes plus geometry only; no provider/download/SHA lineage columns are added.

## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the cadastre flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
