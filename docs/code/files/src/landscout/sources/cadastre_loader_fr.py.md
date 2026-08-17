# `src/landscout/sources/cadastre_loader_fr.py`

## File identity

- Repository path: `src/landscout/sources/cadastre_loader_fr.py`
- File type: Python source
- Primary responsibility: Physically verifies and parses a Cadastre download into source-complete parcel geometry and lineage.
- Layer / domain: `source adapter` / `cadastre`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `214f64a50a996dc9995b004b2efb03811a88b30ef4a2377a85bc2f8317ec5f07`

## 1. Purpose

Physically verifies and parses a Cadastre download into source-complete parcel geometry and lineage.

## 2. Position in LandScout architecture

This file is a `source adapter` artifact in the `cadastre` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `import gzip` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from urllib.parse import urlparse` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `from pyogrio.errors import DataSourceError` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.cadastre_fr import CadastreDownload` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SUPPORTED_GEOMETRY_TYPES` | `frozenset({"Polygon", "MultiPolygon"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `CadastreLoadError`

**Purpose:** Base error for controlled cadastre loading failures.

**Inheritance:** `RuntimeError`.

**Model form and mutability:** class inheriting from `RuntimeError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `EmptyCadastreDatasetError`

**Purpose:** Raised when a cadastre dataset contains no parcel records.

**Inheritance:** `CadastreLoadError`.

**Model form and mutability:** class inheriting from `CadastreLoadError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `MissingGeometryColumnError`

**Purpose:** Raised when a cadastre dataset has no active geometry column.

**Inheritance:** `CadastreLoadError`.

**Model form and mutability:** class inheriting from `CadastreLoadError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `UnsupportedGeometryTypeError`

**Purpose:** Raised when a cadastre dataset contains non-parcel geometry types.

**Inheritance:** `CadastreLoadError`.

**Model form and mutability:** class inheriting from `CadastreLoadError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `_physical_integrity`

**Signature**

```python
def _physical_integrity(path: Path) -> tuple[int, str]:
```

**Purpose**

Implements physical integrity according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[int, str]`. Observed return expression(s): `(size, digest)`.

**Algorithm**

1. Runs guarded operation: Computes `size` from `path.stat().st_size`. Computes `digest` from `sha256(path.read_bytes()).hexdigest()`. Handles `OSError`.
2. Returns `(size, digest)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `CadastreLoadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `path.read_bytes`, `sha256(path.read_bytes()).hexdigest`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreLoadError`, `path.read_bytes`, `path.stat`, `sha256`, `sha256(path.read_bytes()).hexdigest`.

**Known repository callers**

- `src/landscout/sources/cadastre_loader_fr.py` — `_validate_download`
- `src/landscout/sources/cadastre_loader_fr.py` — `load_cadastre_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `_validate_download`

**Signature**

```python
def _validate_download(download: object) -> CadastreDownload:
```

**Purpose**

Validates and rejects malformed download according to the exact implementation and guards in this file.

**Inputs**

- `download` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CadastreDownload`. Observed return expression(s): `download`.

**Algorithm**

1. Checks `type(download) is not CadastreDownload`. When true: Raises `CadastreLoadError('Cadastre source must be an exact CadastreDownload')`.
2. Computes `path` from `download.path`.
3. Checks `not isinstance(path, Path)`. When true: Raises `CadastreLoadError('Cadastre download path must be a Path')`.
4. Checks `not path.is_file()`. When true: Raises `CadastreLoadError(f'Cadastre dataset does not exist: {path}')`.
5. Checks `not isinstance(download.source_url, str) or not download.source_url or download.source_url != download.source_url.strip() or (urlparse(download.source_url).scheme not in {'http', 'https'})`. When true: Raises `CadastreLoadError('Cadastre download source URL is invalid')`.
6. Checks `not isinstance(download.filename, str) or not download.filename or download.filename != download.filename.strip() or (download.filename != path.name)`. When true: Raises `CadastreLoadError('Cadastre download filename does not match its path')`.
7. Checks `type(download.file_size) is not int or download.file_size <= 0`. When true: Raises `CadastreLoadError('Cadastre download size must be a strict positive integer')`.
8. Checks `not isinstance(download.sha256, str) or re.fullmatch('[0-9a-f]{64}', download.sha256) is None`. When true: Raises `CadastreLoadError('Cadastre download SHA256 must be lowercase hexadecimal')`.
9. Computes `(size, digest)` from `_physical_integrity(path)`.
10. Checks `size != download.file_size`. When true: Raises `CadastreLoadError('Cadastre physical size differs from verified download')`.
11. Checks `digest != download.sha256`. When true: Raises `CadastreLoadError('Cadastre physical SHA256 differs from verified download')`.
12. Runs guarded operation: Enters managed context(s) `gzip.open(path, 'rb')` and executes: Repeats the guarded body while `stream.read(1024 * 1024)` remains true. Handles `(EOFError, OSError)`.
13. Returns `download`.

**Validation and invariants**

- Rejects or diverts the path when `type(download) is not CadastreDownload` is true.
- Rejects or diverts the path when `not isinstance(path, Path)` is true.
- Rejects or diverts the path when `not path.is_file()` is true.
- Rejects or diverts the path when `not isinstance(download.source_url, str) or not download.source_url or download.source_url != download.source_url.strip() or (urlparse(download.source_url).scheme not in {'http', 'https'})` is true.
- Rejects or diverts the path when `not isinstance(download.filename, str) or not download.filename or download.filename != download.filename.strip() or (download.filename != path.name)` is true.
- Rejects or diverts the path when `type(download.file_size) is not int or download.file_size <= 0` is true.
- Rejects or diverts the path when `not isinstance(download.sha256, str) or re.fullmatch('[0-9a-f]{64}', download.sha256) is None` is true.
- Rejects or diverts the path when `size != download.file_size` is true.
- Rejects or diverts the path when `digest != download.sha256` is true.

**Exceptions**

- Explicitly raises: `CadastreLoadError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `download.filename.strip`, `download.source_url.strip`, `gzip.open`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CadastreLoadError`, `_physical_integrity`, `download.filename.strip`, `download.source_url.strip`, `gzip.open`, `isinstance`, `path.is_file`, `re.fullmatch`, `stream.read`, `type`, `urlparse`.

**Known repository callers**

- `src/landscout/sources/cadastre_loader_fr.py` — `load_cadastre_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

### `load_cadastre_parcels`

**Signature**

```python
def load_cadastre_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
```

**Purpose**

Load parcels from one byte-verified cadastral download envelope.

**Inputs**

- `download` (`CadastreDownload`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `parcels`.

**Algorithm**

1. Computes `verified` from `_validate_download(download)`.
2. Computes `path` from `verified.path`.
3. Computes `source` from `f'/vsigzip/{path.resolve().as_posix()}'`.
4. Runs guarded operation: Computes `parcels` from `gpd.read_file(source, engine='pyogrio')`. Handles `(DataSourceError, OSError, ValueError)`.
5. Computes `(size_after, digest_after)` from `_physical_integrity(path)`.
6. Checks `size_after != verified.file_size or digest_after != verified.sha256`. When true: Raises `CadastreLoadError('Cadastre physical source changed during parsing')`.
7. Checks `parcels.empty`. When true: Raises `EmptyCadastreDatasetError(f'Cadastre dataset is empty: {path}')`.
8. Computes `geometry_column` from `parcels.active_geometry_name`.
9. Checks `geometry_column is None or geometry_column not in parcels.columns`. When true: Raises `MissingGeometryColumnError('Cadastre dataset has no geometry column')`.
10. Computes `geometry_types` from `set(parcels.geometry.geom_type.dropna().unique())`.
11. Computes `unsupported_types` from `geometry_types - SUPPORTED_GEOMETRY_TYPES`.
12. Checks `unsupported_types`. When true: Computes `formatted_types` from `', '.join(sorted(unsupported_types))`. Raises `UnsupportedGeometryTypeError(f'Unsupported cadastre geometry types: {formatted_types}')`.
13. Returns `parcels`.

**Validation and invariants**

- Rejects or diverts the path when `size_after != verified.file_size or digest_after != verified.sha256` is true.
- Rejects or diverts the path when `parcels.empty` is true.
- Rejects or diverts the path when `geometry_column is None or geometry_column not in parcels.columns` is true.
- Rejects or diverts the path when `unsupported_types` is true.

**Exceptions**

- Explicitly raises: `CadastreLoadError`, `EmptyCadastreDatasetError`, `MissingGeometryColumnError`, `UnsupportedGeometryTypeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_validate_download`, `gpd.read_file`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `', '.join`, `CadastreLoadError`, `EmptyCadastreDatasetError`, `MissingGeometryColumnError`, `UnsupportedGeometryTypeError`, `_physical_integrity`, `_validate_download`, `gpd.read_file`, `parcels.geometry.geom_type.dropna`, `parcels.geometry.geom_type.dropna().unique`, `path.resolve`, `path.resolve().as_posix`, `set`, `sorted`.

**Known repository callers**

- `tests/unit/test_cadastre_loader_fr.py` — `test_empty_dataset_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_invalid_file_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_load_valid_geojson_preserves_attributes`
- `tests/unit/test_cadastre_loader_fr.py` — `test_load_valid_gzipped_geojson`
- `tests/unit/test_cadastre_loader_fr.py` — `test_malformed_verified_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py` — `test_missing_file_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_missing_geometry_column_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_physical_change_during_read_is_rejected_by_post_read_verification`
- `tests/unit/test_cadastre_loader_fr.py` — `test_physical_mutation_after_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py` — `test_unsupported_geometry_type_fails`
- `tests/unit/test_cadastre_loader_fr.py` — `test_wrong_public_input_type_is_controlled`

**Tests**

- `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_invalid_file_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes`
- `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson`
- `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py::test_missing_file_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_missing_geometry_column_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification`
- `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing`
- `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails`
- `tests/unit/test_cadastre_loader_fr.py::test_wrong_public_input_type_is_controlled`

**Business interpretation**

This symbol contributes to the `cadastre` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `cadastre` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
