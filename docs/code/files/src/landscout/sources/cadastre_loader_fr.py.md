# `src/landscout/sources/cadastre_loader_fr.py`

## File identity

- Repository path: `src/landscout/sources/cadastre_loader_fr.py`
- File type: Python source
- Layer: source adapter
- Domain: official source acquisition and physical authority
- Responsibility: Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data.
- Source SHA256: `84541082877632e63708f090cb7d02d8f3ea224afad50341fb788273b4685d13`

## 1. STEP 7F.1A.4 contract delta

- Introduces the frozen Cadastre parcel-source envelope and source-complete physical gzip reread/exact-frame comparison returned to downstream normalization.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data.

The file belongs to the **source adapter** layer and **official source acquisition and physical authority** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import gzip`
- `import re`
- `from dataclasses import dataclass`
- `from datetime import UTC, datetime`
- `from hashlib import sha256`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pyogrio.errors import DataSourceError`

### Internal LandScout imports

- `from landscout.sources.cadastre_fr import (
    CadastreDownload,
    build_cadastre_parcelles_url,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "CadastreLoadError",
    "CadastreParcelSource",
    "EmptyCadastreDatasetError",
    "MissingGeometryColumnError",
    "UnsupportedGeometryTypeError",
    "load_cadastre_parcels",
    "revalidate_cadastre_parcel_source",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `CadastreLoadError`
  - `CadastreParcelSource`
  - `EmptyCadastreDatasetError`
  - `MissingGeometryColumnError`
  - `UnsupportedGeometryTypeError`
  - `load_cadastre_parcels`
  - `revalidate_cadastre_parcel_source`

### `SUPPORTED_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `CadastreLoadError`

**Source purpose:** Base error for controlled cadastre loading failures.

- Exact decorators: none.
- Exact bases: `RuntimeError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- constructor call: `landscout.sources.cadastre_loader_fr::_physical_integrity` via `CadastreLoadError`
- value/type reference: `landscout.sources.cadastre_loader_fr::_physical_integrity` via `CadastreLoadError`
- constructor call: `landscout.sources.cadastre_loader_fr::_validate_download` via `CadastreLoadError`
- value/type reference: `landscout.sources.cadastre_loader_fr::_validate_download` via `CadastreLoadError`
- constructor call: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `CadastreLoadError`
- value/type reference: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `CadastreLoadError`
- constructor call: `landscout.sources.cadastre_loader_fr::_compare_parcel_frames` via `CadastreLoadError`
- value/type reference: `landscout.sources.cadastre_loader_fr::_compare_parcel_frames` via `CadastreLoadError`
- constructor call: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `CadastreLoadError`
- value/type reference: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `CadastreLoadError`
- import: `landscout.stages.normalize_cadastre::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `CadastreLoadError`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_missing_file_fails` via `CadastreLoadError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_invalid_file_fails` via `CadastreLoadError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_malformed_verified_download_is_rejected_before_parsing` via `CadastreLoadError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_wrong_public_input_type_is_controlled` via `CadastreLoadError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_mutation_after_download_is_rejected_before_parsing` via `CadastreLoadError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_change_during_read_is_rejected_by_post_read_verification` via `CadastreLoadError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `CadastreLoadError`

**Exact class source**

```python
class CadastreLoadError(RuntimeError):
    """Base error for controlled cadastre loading failures."""
```

### `EmptyCadastreDatasetError`

**Source purpose:** Raised when a cadastre dataset contains no parcel records.

- Exact decorators: none.
- Exact bases: `CadastreLoadError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- constructor call: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `EmptyCadastreDatasetError`
- value/type reference: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `EmptyCadastreDatasetError`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_empty_dataset_fails` via `EmptyCadastreDatasetError`

**Exact class source**

```python
class EmptyCadastreDatasetError(CadastreLoadError):
    """Raised when a cadastre dataset contains no parcel records."""
```

### `MissingGeometryColumnError`

**Source purpose:** Raised when a cadastre dataset has no active geometry column.

- Exact decorators: none.
- Exact bases: `CadastreLoadError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- constructor call: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `MissingGeometryColumnError`
- value/type reference: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `MissingGeometryColumnError`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_missing_geometry_column_fails` via `MissingGeometryColumnError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_noncanonical_active_geometry_name_fails_with_controlled_error` via `MissingGeometryColumnError`

**Exact class source**

```python
class MissingGeometryColumnError(CadastreLoadError):
    """Raised when a cadastre dataset has no active geometry column."""
```

### `UnsupportedGeometryTypeError`

**Source purpose:** Raised when a cadastre dataset contains non-parcel geometry types.

- Exact decorators: none.
- Exact bases: `CadastreLoadError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- constructor call: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `UnsupportedGeometryTypeError`
- value/type reference: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `UnsupportedGeometryTypeError`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_unsupported_geometry_type_fails` via `UnsupportedGeometryTypeError`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_three_dimensional_cadastre_geometry_is_rejected` via `UnsupportedGeometryTypeError`

**Exact class source**

```python
class UnsupportedGeometryTypeError(CadastreLoadError):
    """Raised when a cadastre dataset contains non-parcel geometry types."""
```

### `CadastreParcelSource`

**Source purpose:** One physical Cadastre download bound to its parsed parcel frame.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `download` | `CadastreDownload` | `required` | `download: CadastreDownload` |
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- constructor call: `landscout.sources.cadastre_loader_fr::load_cadastre_parcels` via `CadastreParcelSource`
- value/type reference: `landscout.sources.cadastre_loader_fr::load_cadastre_parcels` via `CadastreParcelSource`
- value/type reference: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `CadastreParcelSource`
- import: `landscout.stages.normalize_cadastre::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `CadastreParcelSource`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_public_sources_export_the_source_bound_cadastre_api` via `CadastreParcelSource`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_load_valid_geojson_preserves_attributes` via `CadastreParcelSource`
- import: `tests.unit.test_normalize_cadastre::<module>` via `from landscout.sources.cadastre_loader_fr import CadastreParcelSource`
- constructor call: `tests.unit.test_normalize_cadastre::_bound_source` via `CadastreParcelSource`
- value/type reference: `tests.unit.test_normalize_cadastre::_bound_source` via `CadastreParcelSource`

**Exact class source**

```python
class CadastreParcelSource:
    """One physical Cadastre download bound to its parsed parcel frame."""

    download: CadastreDownload
    parcels: gpd.GeoDataFrame
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_is_link_or_junction`

**Purpose:** Implements `is link or junction` within the file role: Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data.

**Exact signature**

```python
def _is_link_or_junction(path: Path) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `path.is_symlink() or path.is_junction()`
  - `True`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_loader_fr::_validate_download` via `_is_link_or_junction`
- value/type reference: `landscout.sources.cadastre_loader_fr::_validate_download` via `_is_link_or_junction`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_symlink` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.is_junction` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_physical_integrity`

**Purpose:** Implements `physical integrity` within the file role: Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data.

**Exact signature**

```python
def _physical_integrity(path: Path) -> tuple[int, str]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[int, str]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `size, digest`
- Explicit raise paths:
  - `CadastreLoadError(f"Cannot inspect cadastre dataset: {path}")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_loader_fr::_validate_download` via `_physical_integrity`
- value/type reference: `landscout.sources.cadastre_loader_fr::_validate_download` via `_physical_integrity`
- direct call: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `_physical_integrity`
- value/type reference: `landscout.sources.cadastre_loader_fr::_read_physical_parcels` via `_physical_integrity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(path.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreLoadError` | `landscout.sources.cadastre_loader_fr.CadastreLoadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.stat`<br>`sha256(path.read_bytes()).hexdigest`<br>`path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(path.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_validate_download`

**Purpose:** Implements `validate download` within the file role: Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data.

**Exact signature**

```python
def _validate_download(download: object) -> CadastreDownload:
```

- Exact decorators: none.
- Declared return annotation: `CadastreDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `download`
- Explicit raise paths:
  - `TypeError("Cadastre source must be an exact CadastreDownload")` under lexical guard `type(download) is not CadastreDownload`.
  - `TypeError("Cadastre commune code is invalid")` under lexical guard `type(download.commune_code) is not str`.
  - `ValueError("Cadastre download source URL is not the official URL")` under lexical guard `download.source_url != official_url`.
  - `ValueError("Cadastre download filename is not official")` under lexical guard `download.filename != official_filename`.
  - `TypeError("Cadastre download path must be a pathlib.Path")` under lexical guard `not isinstance(path, Path)`.
  - `ValueError("Cadastre dataset must exist as a regular non-linked file")` under lexical guard `_is_link_or_junction(path) or not path.is_file()`.
  - `ValueError("Cadastre download filename does not match its path")` under lexical guard `path.name != official_filename`.
  - `TypeError("Cadastre download size must be a strict positive integer")` under lexical guard `type(download.file_size) is not int or download.file_size <= 0`.
  - `ValueError("Cadastre download SHA256 must be lowercase hexadecimal")` under lexical guard `type(download.sha256) is not str<br>            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None`.
  - `TypeError("Cadastre download timestamp must be an exact string")` under lexical guard `type(download.download_timestamp) is not str`.
  - `ValueError("Cadastre download timestamp must be timezone-aware UTC")` under lexical guard `downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(<br>            None<br>        )`.
  - `TypeError("Cadastre cache-hit state must be an exact Boolean")` under lexical guard `type(download.cache_hit) is not bool`.
  - `ValueError("Cadastre physical size differs from verified download")` under lexical guard `size != download.file_size`.
  - `ValueError("Cadastre physical SHA256 differs from verified download")` under lexical guard `digest != download.sha256`.
  - `ValueError("Cadastre verified source is not valid gzip")`.
  - `re-raise`.
  - `CadastreLoadError(detail)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_loader_fr::load_cadastre_parcels` via `_validate_download`
- value/type reference: `landscout.sources.cadastre_loader_fr::load_cadastre_parcels` via `_validate_download`
- direct call: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `_validate_download`
- value/type reference: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `_validate_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `build_cadastre_parcelles_url` | `landscout.sources.cadastre_fr.build_cadastre_parcelles_url` |
| `official_url.rsplit` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_link_or_junction` | `landscout.sources.cadastre_loader_fr._is_link_or_junction` |
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `re.fullmatch` | `re.fullmatch` |
| `datetime.fromisoformat` | `datetime.datetime.fromisoformat` |
| `downloaded_at.utcoffset` | `unresolved local/third-party receiver; no ownership inferred` |
| `UTC.utcoffset` | `datetime.UTC.utcoffset` |
| `_physical_integrity` | `landscout.sources.cadastre_loader_fr._physical_integrity` |
| `gzip.open` | `gzip.open` |
| `stream.read` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreLoadError` | `landscout.sources.cadastre_loader_fr.CadastreLoadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`gzip.open` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_download(download: object) -> CadastreDownload:
    try:
        if type(download) is not CadastreDownload:
            raise TypeError("Cadastre source must be an exact CadastreDownload")
        if type(download.commune_code) is not str:
            raise TypeError("Cadastre commune code is invalid")
        official_url = build_cadastre_parcelles_url(download.commune_code)
        official_filename = official_url.rsplit("/", maxsplit=1)[-1]
        if download.source_url != official_url:
            raise ValueError("Cadastre download source URL is not the official URL")
        if download.filename != official_filename:
            raise ValueError("Cadastre download filename is not official")
        path = download.path
        if not isinstance(path, Path):
            raise TypeError("Cadastre download path must be a pathlib.Path")
        if _is_link_or_junction(path) or not path.is_file():
            raise ValueError("Cadastre dataset must exist as a regular non-linked file")
        if path.name != official_filename:
            raise ValueError("Cadastre download filename does not match its path")
        if type(download.file_size) is not int or download.file_size <= 0:
            raise TypeError("Cadastre download size must be a strict positive integer")
        if (
            type(download.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
        ):
            raise ValueError("Cadastre download SHA256 must be lowercase hexadecimal")
        if type(download.download_timestamp) is not str:
            raise TypeError("Cadastre download timestamp must be an exact string")
        downloaded_at = datetime.fromisoformat(download.download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            raise ValueError("Cadastre download timestamp must be timezone-aware UTC")
        if type(download.cache_hit) is not bool:
            raise TypeError("Cadastre cache-hit state must be an exact Boolean")
        size, digest = _physical_integrity(path)
        if size != download.file_size:
            raise ValueError("Cadastre physical size differs from verified download")
        if digest != download.sha256:
            raise ValueError("Cadastre physical SHA256 differs from verified download")
        try:
            with gzip.open(path, "rb") as stream:
                while stream.read(1024 * 1024):
                    pass
        except (EOFError, OSError) as error:
            raise ValueError("Cadastre verified source is not valid gzip") from error
        return download
    except CadastreLoadError:
        raise
    except Exception as error:
        detail = str(error) or "Cadastre download envelope is invalid"
        raise CadastreLoadError(detail) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_read_physical_parcels`

**Purpose:** Implements `read physical parcels` within the file role: Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data.

**Exact signature**

```python
def _read_physical_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `CadastreDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parcels`
- Explicit raise paths:
  - `CadastreLoadError(f"Unable to read cadastre dataset: {path}")`.
  - `CadastreLoadError("Cadastre physical source changed during parsing")` under lexical guard `size_after != download.file_size or digest_after != download.sha256`.
  - `EmptyCadastreDatasetError(f"Cadastre dataset is empty: {path}")` under lexical guard `parcels.empty`.
  - `MissingGeometryColumnError("Cadastre dataset has no geometry column")` under lexical guard `geometry_column is None or geometry_column not in parcels.columns`.
  - `MissingGeometryColumnError(<br>            "Cadastre dataset active geometry must use the canonical geometry name"<br>        )` under lexical guard `geometry_column != "geometry"`.
  - `UnsupportedGeometryTypeError(<br>            f"Unsupported cadastre geometry types: {formatted_types}"<br>        )` under lexical guard `unsupported_types`.
  - `UnsupportedGeometryTypeError(<br>            "Cadastre parcel geometry must be exactly 2D"<br>        )` under lexical guard `any(bool(value) for value in non_null.has_z)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_loader_fr::load_cadastre_parcels` via `_read_physical_parcels`
- value/type reference: `landscout.sources.cadastre_loader_fr::load_cadastre_parcels` via `_read_physical_parcels`
- direct call: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `_read_physical_parcels`
- value/type reference: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `_read_physical_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.resolve().as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.resolve` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `CadastreLoadError` | `landscout.sources.cadastre_loader_fr.CadastreLoadError` |
| `_physical_integrity` | `landscout.sources.cadastre_loader_fr._physical_integrity` |
| `EmptyCadastreDatasetError` | `landscout.sources.cadastre_loader_fr.EmptyCadastreDatasetError` |
| `MissingGeometryColumnError` | `landscout.sources.cadastre_loader_fr.MissingGeometryColumnError` |
| `parcels.geometry.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `non_null.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `UnsupportedGeometryTypeError` | `landscout.sources.cadastre_loader_fr.UnsupportedGeometryTypeError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `MissingGeometryColumnError`<br>`parcels.geometry.dropna`<br>`non_null.geom_type.dropna`<br>`UnsupportedGeometryTypeError` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _read_physical_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
    path = download.path
    source_path = f"/vsigzip/{path.resolve().as_posix()}"
    try:
        parcels = gpd.read_file(source_path, engine="pyogrio")
    except (DataSourceError, OSError, ValueError) as error:
        raise CadastreLoadError(f"Unable to read cadastre dataset: {path}") from error

    size_after, digest_after = _physical_integrity(path)
    if size_after != download.file_size or digest_after != download.sha256:
        raise CadastreLoadError("Cadastre physical source changed during parsing")
    if parcels.empty:
        raise EmptyCadastreDatasetError(f"Cadastre dataset is empty: {path}")
    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise MissingGeometryColumnError("Cadastre dataset has no geometry column")
    if geometry_column != "geometry":
        raise MissingGeometryColumnError(
            "Cadastre dataset active geometry must use the canonical geometry name"
        )
    non_null = parcels.geometry.dropna()
    unsupported_types = set(non_null.geom_type.dropna()) - SUPPORTED_GEOMETRY_TYPES
    if unsupported_types:
        formatted_types = ", ".join(sorted(unsupported_types))
        raise UnsupportedGeometryTypeError(
            f"Unsupported cadastre geometry types: {formatted_types}"
        )
    if any(bool(value) for value in non_null.has_z):
        raise UnsupportedGeometryTypeError(
            "Cadastre parcel geometry must be exactly 2D"
        )
    return parcels
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `_compare_parcel_frames`

**Purpose:** Implements `compare parcel frames` within the file role: Returns `CadastreParcelSource` and source-completely rereads/exact-compares official commune-bound physical parcel data.

**Exact signature**

```python
def _compare_parcel_frames(
    supplied: object,
    expected: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `supplied` | positional-or-keyword | `object` | `required` |
| `expected` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `TypeError("supplied parcels are not a GeoDataFrame")` under lexical guard `not isinstance(supplied, gpd.GeoDataFrame)`.
  - `AssertionError("columns differ")` under lexical guard `tuple(supplied.columns) != tuple(expected.columns)`.
  - `AssertionError("dtypes differ")` under lexical guard `tuple(str(dtype) for dtype in supplied.dtypes) != tuple(<br>            str(dtype) for dtype in expected.dtypes<br>        )`.
  - `AssertionError("index type differs")` under lexical guard `type(supplied.index) is not type(expected.index)`.
  - `AssertionError("index differs")` under lexical guard `supplied.index.names != expected.index.names or not supplied.index.equals(<br>            expected.index<br>        )`.
  - `AssertionError("active geometry differs")` under lexical guard `supplied.active_geometry_name != expected.active_geometry_name`.
  - `AssertionError("CRS differs")` under lexical guard `supplied.crs != expected.crs`.
  - `AssertionError("geometry is missing")` under lexical guard `geometry_name is None`.
  - `AssertionError("geometry WKB differs")` under lexical guard `supplied.geometry.to_wkb(hex=True).tolist()<br>            != expected.geometry.to_wkb(hex=True).tolist()`.
  - `AssertionError("frame attributes differ")` under lexical guard `supplied.attrs != expected.attrs`.
  - `CadastreLoadError(<br>            "Supplied Cadastre parcels differ from freshly read physical source"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `_compare_parcel_frames`
- value/type reference: `landscout.sources.cadastre_loader_fr::revalidate_cadastre_parcel_source` via `_compare_parcel_frames`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `supplied.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.geometry.to_wkb(hex=True).tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `supplied.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.geometry.to_wkb(hex=True).tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreLoadError` | `landscout.sources.cadastre_loader_fr.CadastreLoadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `supplied.geometry.to_wkb(hex=True).tolist`<br>`supplied.geometry.to_wkb`<br>`expected.geometry.to_wkb(hex=True).tolist`<br>`expected.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | `supplied.drop(columns=geometry_name)`<br>`expected.drop(columns=geometry_name)` |
| Direct parameter mutation | `supplied.drop(columns=geometry_name)`<br>`expected.drop(columns=geometry_name)` |

**Complete source-ordered implementation**

```python
def _compare_parcel_frames(
    supplied: object,
    expected: gpd.GeoDataFrame,
) -> None:
    try:
        if not isinstance(supplied, gpd.GeoDataFrame):
            raise TypeError("supplied parcels are not a GeoDataFrame")
        if tuple(supplied.columns) != tuple(expected.columns):
            raise AssertionError("columns differ")
        if tuple(str(dtype) for dtype in supplied.dtypes) != tuple(
            str(dtype) for dtype in expected.dtypes
        ):
            raise AssertionError("dtypes differ")
        if type(supplied.index) is not type(expected.index):
            raise AssertionError("index type differs")
        if supplied.index.names != expected.index.names or not supplied.index.equals(
            expected.index
        ):
            raise AssertionError("index differs")
        if supplied.active_geometry_name != expected.active_geometry_name:
            raise AssertionError("active geometry differs")
        if supplied.crs != expected.crs:
            raise AssertionError("CRS differs")
        geometry_name = expected.active_geometry_name
        if geometry_name is None:
            raise AssertionError("geometry is missing")
        pd.testing.assert_frame_equal(
            pd.DataFrame(supplied.drop(columns=geometry_name)),
            pd.DataFrame(expected.drop(columns=geometry_name)),
            check_dtype=True,
            check_index_type=True,
            check_column_type=True,
            check_names=True,
            check_exact=True,
        )
        if (
            supplied.geometry.to_wkb(hex=True).tolist()
            != expected.geometry.to_wkb(hex=True).tolist()
        ):
            raise AssertionError("geometry WKB differs")
        if supplied.attrs != expected.attrs:
            raise AssertionError("frame attributes differ")
    except Exception as error:
        raise CadastreLoadError(
            "Supplied Cadastre parcels differ from freshly read physical source"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `load_cadastre_parcels`

**Purpose:** Load parcels while retaining the verified physical source authority.

**Exact signature**

```python
def load_cadastre_parcels(download: CadastreDownload) -> CadastreParcelSource:
```

- Exact decorators: none.
- Declared return annotation: `CadastreParcelSource`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `download` | positional-or-keyword | `CadastreDownload` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `CadastreParcelSource(<br>        download=verified,<br>        parcels=_read_physical_parcels(verified),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_public_sources_export_the_source_bound_cadastre_api` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_load_valid_geojson_preserves_attributes` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_load_valid_geojson_preserves_attributes` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_load_valid_gzipped_geojson` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_load_valid_gzipped_geojson` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_empty_dataset_fails` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_empty_dataset_fails` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_missing_file_fails` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_missing_file_fails` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_invalid_file_fails` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_invalid_file_fails` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_missing_geometry_column_fails` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_missing_geometry_column_fails` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_noncanonical_active_geometry_name_fails_with_controlled_error` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_noncanonical_active_geometry_name_fails_with_controlled_error` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_unsupported_geometry_type_fails` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_unsupported_geometry_type_fails` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_three_dimensional_cadastre_geometry_is_rejected` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_three_dimensional_cadastre_geometry_is_rejected` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_malformed_verified_download_is_rejected_before_parsing` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_malformed_verified_download_is_rejected_before_parsing` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_wrong_public_input_type_is_controlled` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_wrong_public_input_type_is_controlled` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_physical_mutation_after_download_is_rejected_before_parsing` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_mutation_after_download_is_rejected_before_parsing` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_physical_change_during_read_is_rejected_by_post_read_verification` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_change_during_read_is_rejected_by_post_read_verification` via `load_cadastre_parcels`
- direct call: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `load_cadastre_parcels`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `load_cadastre_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_download` | `landscout.sources.cadastre_loader_fr._validate_download` |
| `CadastreParcelSource` | `landscout.sources.cadastre_loader_fr.CadastreParcelSource` |
| `_read_physical_parcels` | `landscout.sources.cadastre_loader_fr._read_physical_parcels` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_cadastre_parcels(download: CadastreDownload) -> CadastreParcelSource:
    """Load parcels while retaining the verified physical source authority."""

    verified = _validate_download(download)
    return CadastreParcelSource(
        download=verified,
        parcels=_read_physical_parcels(verified),
    )
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.

### `revalidate_cadastre_parcel_source`

**Purpose:** Fresh-read and exact-compare one supplied Cadastre parcel source.

**Exact signature**

```python
def revalidate_cadastre_parcel_source(
    source: object,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `fresh`
- Explicit raise paths:
  - `TypeError("Cadastre parcel source type is invalid")` under lexical guard `type(source) is not CadastreParcelSource`.
  - `re-raise`.
  - `CadastreLoadError(<br>            "Cadastre source-complete revalidation failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.sources::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- import: `landscout.stages.normalize_cadastre::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    revalidate_cadastre_parcel_source,
)`
- direct call: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `revalidate_cadastre_parcel_source`
- value/type reference: `landscout.stages.normalize_cadastre::normalize_cadastre_parcels` via `revalidate_cadastre_parcel_source`
- import: `tests.unit.test_cadastre_loader_fr::<module>` via `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_public_sources_export_the_source_bound_cadastre_api` via `revalidate_cadastre_parcel_source`
- direct call: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `revalidate_cadastre_parcel_source`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `revalidate_cadastre_parcel_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `TypeError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_download` | `landscout.sources.cadastre_loader_fr._validate_download` |
| `_read_physical_parcels` | `landscout.sources.cadastre_loader_fr._read_physical_parcels` |
| `_compare_parcel_frames` | `landscout.sources.cadastre_loader_fr._compare_parcel_frames` |
| `CadastreLoadError` | `landscout.sources.cadastre_loader_fr.CadastreLoadError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def revalidate_cadastre_parcel_source(
    source: object,
) -> gpd.GeoDataFrame:
    """Fresh-read and exact-compare one supplied Cadastre parcel source."""

    try:
        if type(source) is not CadastreParcelSource:
            raise TypeError("Cadastre parcel source type is invalid")
        verified = _validate_download(source.download)
        fresh = _read_physical_parcels(verified)
        _compare_parcel_frames(source.parcels, fresh)
        return fresh
    except CadastreLoadError:
        raise
    except Exception as error:
        raise CadastreLoadError(
            "Cadastre source-complete revalidation failed"
        ) from error
```

**Business boundary**

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: none at module scope.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `CadastreLoadError` | `landscout.sources.cadastre_loader_fr.CadastreLoadError` |
| `CadastreParcelSource` | `landscout.sources.cadastre_loader_fr.CadastreParcelSource` |
| `EmptyCadastreDatasetError` | `landscout.sources.cadastre_loader_fr.EmptyCadastreDatasetError` |
| `MissingGeometryColumnError` | `landscout.sources.cadastre_loader_fr.MissingGeometryColumnError` |
| `UnsupportedGeometryTypeError` | `landscout.sources.cadastre_loader_fr.UnsupportedGeometryTypeError` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `revalidate_cadastre_parcel_source` | `landscout.sources.cadastre_loader_fr.revalidate_cadastre_parcel_source` |

## 9. Trust, provenance, side effects, and business boundary

- This adapter establishes source/provenance and factual physical data only; it does not interpret suitability, rank parcels, score, or create a legal conclusion.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Source-bound loading and physical revalidation for Cadastre parcels."""

import gzip
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyogrio.errors import DataSourceError  # type: ignore[import-untyped]

from landscout.sources.cadastre_fr import (
    CadastreDownload,
    build_cadastre_parcelles_url,
)

__all__ = [
    "CadastreLoadError",
    "CadastreParcelSource",
    "EmptyCadastreDatasetError",
    "MissingGeometryColumnError",
    "UnsupportedGeometryTypeError",
    "load_cadastre_parcels",
    "revalidate_cadastre_parcel_source",
]

SUPPORTED_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})


class CadastreLoadError(RuntimeError):
    """Base error for controlled cadastre loading failures."""


class EmptyCadastreDatasetError(CadastreLoadError):
    """Raised when a cadastre dataset contains no parcel records."""


class MissingGeometryColumnError(CadastreLoadError):
    """Raised when a cadastre dataset has no active geometry column."""


class UnsupportedGeometryTypeError(CadastreLoadError):
    """Raised when a cadastre dataset contains non-parcel geometry types."""


@dataclass(frozen=True)
class CadastreParcelSource:
    """One physical Cadastre download bound to its parsed parcel frame."""

    download: CadastreDownload
    parcels: gpd.GeoDataFrame


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _physical_integrity(path: Path) -> tuple[int, str]:
    try:
        size = path.stat().st_size
        digest = sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        raise CadastreLoadError(f"Cannot inspect cadastre dataset: {path}") from error
    return size, digest


def _validate_download(download: object) -> CadastreDownload:
    try:
        if type(download) is not CadastreDownload:
            raise TypeError("Cadastre source must be an exact CadastreDownload")
        if type(download.commune_code) is not str:
            raise TypeError("Cadastre commune code is invalid")
        official_url = build_cadastre_parcelles_url(download.commune_code)
        official_filename = official_url.rsplit("/", maxsplit=1)[-1]
        if download.source_url != official_url:
            raise ValueError("Cadastre download source URL is not the official URL")
        if download.filename != official_filename:
            raise ValueError("Cadastre download filename is not official")
        path = download.path
        if not isinstance(path, Path):
            raise TypeError("Cadastre download path must be a pathlib.Path")
        if _is_link_or_junction(path) or not path.is_file():
            raise ValueError("Cadastre dataset must exist as a regular non-linked file")
        if path.name != official_filename:
            raise ValueError("Cadastre download filename does not match its path")
        if type(download.file_size) is not int or download.file_size <= 0:
            raise TypeError("Cadastre download size must be a strict positive integer")
        if (
            type(download.sha256) is not str
            or re.fullmatch(r"[0-9a-f]{64}", download.sha256) is None
        ):
            raise ValueError("Cadastre download SHA256 must be lowercase hexadecimal")
        if type(download.download_timestamp) is not str:
            raise TypeError("Cadastre download timestamp must be an exact string")
        downloaded_at = datetime.fromisoformat(download.download_timestamp)
        if downloaded_at.tzinfo is None or downloaded_at.utcoffset() != UTC.utcoffset(
            None
        ):
            raise ValueError("Cadastre download timestamp must be timezone-aware UTC")
        if type(download.cache_hit) is not bool:
            raise TypeError("Cadastre cache-hit state must be an exact Boolean")
        size, digest = _physical_integrity(path)
        if size != download.file_size:
            raise ValueError("Cadastre physical size differs from verified download")
        if digest != download.sha256:
            raise ValueError("Cadastre physical SHA256 differs from verified download")
        try:
            with gzip.open(path, "rb") as stream:
                while stream.read(1024 * 1024):
                    pass
        except (EOFError, OSError) as error:
            raise ValueError("Cadastre verified source is not valid gzip") from error
        return download
    except CadastreLoadError:
        raise
    except Exception as error:
        detail = str(error) or "Cadastre download envelope is invalid"
        raise CadastreLoadError(detail) from error


def _read_physical_parcels(download: CadastreDownload) -> gpd.GeoDataFrame:
    path = download.path
    source_path = f"/vsigzip/{path.resolve().as_posix()}"
    try:
        parcels = gpd.read_file(source_path, engine="pyogrio")
    except (DataSourceError, OSError, ValueError) as error:
        raise CadastreLoadError(f"Unable to read cadastre dataset: {path}") from error

    size_after, digest_after = _physical_integrity(path)
    if size_after != download.file_size or digest_after != download.sha256:
        raise CadastreLoadError("Cadastre physical source changed during parsing")
    if parcels.empty:
        raise EmptyCadastreDatasetError(f"Cadastre dataset is empty: {path}")
    geometry_column = parcels.active_geometry_name
    if geometry_column is None or geometry_column not in parcels.columns:
        raise MissingGeometryColumnError("Cadastre dataset has no geometry column")
    if geometry_column != "geometry":
        raise MissingGeometryColumnError(
            "Cadastre dataset active geometry must use the canonical geometry name"
        )
    non_null = parcels.geometry.dropna()
    unsupported_types = set(non_null.geom_type.dropna()) - SUPPORTED_GEOMETRY_TYPES
    if unsupported_types:
        formatted_types = ", ".join(sorted(unsupported_types))
        raise UnsupportedGeometryTypeError(
            f"Unsupported cadastre geometry types: {formatted_types}"
        )
    if any(bool(value) for value in non_null.has_z):
        raise UnsupportedGeometryTypeError(
            "Cadastre parcel geometry must be exactly 2D"
        )
    return parcels


def _compare_parcel_frames(
    supplied: object,
    expected: gpd.GeoDataFrame,
) -> None:
    try:
        if not isinstance(supplied, gpd.GeoDataFrame):
            raise TypeError("supplied parcels are not a GeoDataFrame")
        if tuple(supplied.columns) != tuple(expected.columns):
            raise AssertionError("columns differ")
        if tuple(str(dtype) for dtype in supplied.dtypes) != tuple(
            str(dtype) for dtype in expected.dtypes
        ):
            raise AssertionError("dtypes differ")
        if type(supplied.index) is not type(expected.index):
            raise AssertionError("index type differs")
        if supplied.index.names != expected.index.names or not supplied.index.equals(
            expected.index
        ):
            raise AssertionError("index differs")
        if supplied.active_geometry_name != expected.active_geometry_name:
            raise AssertionError("active geometry differs")
        if supplied.crs != expected.crs:
            raise AssertionError("CRS differs")
        geometry_name = expected.active_geometry_name
        if geometry_name is None:
            raise AssertionError("geometry is missing")
        pd.testing.assert_frame_equal(
            pd.DataFrame(supplied.drop(columns=geometry_name)),
            pd.DataFrame(expected.drop(columns=geometry_name)),
            check_dtype=True,
            check_index_type=True,
            check_column_type=True,
            check_names=True,
            check_exact=True,
        )
        if (
            supplied.geometry.to_wkb(hex=True).tolist()
            != expected.geometry.to_wkb(hex=True).tolist()
        ):
            raise AssertionError("geometry WKB differs")
        if supplied.attrs != expected.attrs:
            raise AssertionError("frame attributes differ")
    except Exception as error:
        raise CadastreLoadError(
            "Supplied Cadastre parcels differ from freshly read physical source"
        ) from error


def load_cadastre_parcels(download: CadastreDownload) -> CadastreParcelSource:
    """Load parcels while retaining the verified physical source authority."""

    verified = _validate_download(download)
    return CadastreParcelSource(
        download=verified,
        parcels=_read_physical_parcels(verified),
    )


def revalidate_cadastre_parcel_source(
    source: object,
) -> gpd.GeoDataFrame:
    """Fresh-read and exact-compare one supplied Cadastre parcel source."""

    try:
        if type(source) is not CadastreParcelSource:
            raise TypeError("Cadastre parcel source type is invalid")
        verified = _validate_download(source.download)
        fresh = _read_physical_parcels(verified)
        _compare_parcel_frames(source.parcels, fresh)
        return fresh
    except CadastreLoadError:
        raise
    except Exception as error:
        raise CadastreLoadError(
            "Cadastre source-complete revalidation failed"
        ) from error
```
