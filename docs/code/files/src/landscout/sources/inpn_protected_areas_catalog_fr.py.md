# `src/landscout/sources/inpn_protected_areas_catalog_fr.py`

## File identity

- Repository path: `src/landscout/sources/inpn_protected_areas_catalog_fr.py`
- File type: Python source
- Layer/domain: official source physical metadata authority
- Responsibility: Builds and independently validates the schema-2 metadata-only catalog from immutable verified package bytes.
- Source SHA256: `1483af5b8353f04053f2ca57b51fc0a7b1aa5653f2673af29876f815187eec57`

## 1. Architectural contract

The source file below is authoritative. STEP 7F.1B.1.1 binds the chain `pinned archive bytes -> archive-derived uncompressed-member inventory -> marker/physical/caller equality -> immutable package bytes -> exact GPKG metadata -> schema-2 catalog`. The extraction marker is cache evidence and cannot override the archive. Every physical catalog fact is metadata evidence only.

## 2. Imports and dependencies

Every import is listed exactly; these dependencies define the filesystem, hashing, ZIP, CRS, Pyogrio, strict-validation, and source-boundary mechanisms.

```python
from __future__ import annotations
```

```python
import json
```

```python
import math
```

```python
import re
```

```python
import unicodedata
```

```python
from collections.abc import Mapping
```

```python
from dataclasses import dataclass
```

```python
from hashlib import sha256
```

```python
from numbers import Real
```

```python
from pathlib import Path, PurePosixPath, PureWindowsPath
```

```python
from typing import SupportsFloat, cast
```

```python
import pyogrio
```

```python
from pyproj import CRS
```

```python
from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    validate_inpn_protected_areas_extraction,
)
```

## 3. Constants, aliases, and module declarations

### `CATALOG_HASH_SCHEMA_VERSION`

- Exact declaration:

```python
CATALOG_HASH_SCHEMA_VERSION = 2
```

- Role: module-level immutable identity, schema, validation domain, or lookup used exactly where referenced in the source snapshot. Any schema constant is persisted/hash-significant only through its explicit consumers.

### `_SHA_PATTERN`

- Exact declaration:

```python
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

- Role: module-level immutable identity, schema, validation domain, or lookup used exactly where referenced in the source snapshot. Any schema constant is persisted/hash-significant only through its explicit consumers.

### `__all__`

- Exact declaration:

```python
__all__ = [
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
    "InpnProtectedAreasLayerCatalog",
    "build_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_catalog",
]
```

- Role: module-level immutable identity, schema, validation domain, or lookup used exactly where referenced in the source snapshot. Any schema constant is persisted/hash-significant only through its explicit consumers.

## 4. Exceptions and models

### `InpnProtectedAreasCatalogError`

- Exact bases: `ValueError`.
- Decorators: `none`.
- Purpose: Raised when exact EP GeoPackage metadata cannot be proven safely.
- Fields: none declared directly.
- Mutability/canonicality: frozen dataclass or frozen strict Pydantic configuration where declared; public intrinsic/boundary validation still checks exact runtime representation.

### `InpnProtectedAreasFieldCatalog`

- Exact bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: One source-ordered physical attribute-field metadata record.
- Fields:

  - `name: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `source_dtype: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `position: int`; default `required`; owns exactly the named validated factual or integrity value.
- Mutability/canonicality: frozen dataclass or frozen strict Pydantic configuration where declared; public intrinsic/boundary validation still checks exact runtime representation.

### `InpnProtectedAreasLayerCatalog`

- Exact bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: One source-ordered OGR layer metadata record without feature rows.
- Fields:

  - `layer_name: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `layer_position: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `feature_count: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `geometry_type_raw: str | None`; default `required`; owns exactly the named validated factual or integrity value.
  - `is_spatial: bool`; default `required`; owns exactly the named validated factual or integrity value.
  - `crs_raw: str | None`; default `required`; owns exactly the named validated factual or integrity value.
  - `crs_authority_name: str | None`; default `required`; owns exactly the named validated factual or integrity value.
  - `crs_authority_code: str | None`; default `required`; owns exactly the named validated factual or integrity value.
  - `crs_wkt: str | None`; default `required`; owns exactly the named validated factual or integrity value.
  - `total_bounds: tuple[float, float, float, float] | None`; default `required`; owns exactly the named validated factual or integrity value.
  - `fields: tuple[InpnProtectedAreasFieldCatalog, ...]`; default `required`; owns exactly the named validated factual or integrity value.
- Mutability/canonicality: frozen dataclass or frozen strict Pydantic configuration where declared; public intrinsic/boundary validation still checks exact runtime representation.

### `InpnProtectedAreasGeoPackageCatalog`

- Exact bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: One extraction-ordered verified GeoPackage and all of its OGR layers.
- Fields:

  - `relative_path: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `file_size: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `file_sha256: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `package_position: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `driver_name: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `layers: tuple[InpnProtectedAreasLayerCatalog, ...]`; default `required`; owns exactly the named validated factual or integrity value.
- Mutability/canonicality: frozen dataclass or frozen strict Pydantic configuration where declared; public intrinsic/boundary validation still checks exact runtime representation.

### `InpnProtectedAreasCatalog`

- Exact bases: `object`.
- Decorators: `dataclass(frozen=True)`.
- Purpose: Portable factual metadata catalog bound to one verified INPN EP snapshot.
- Fields:

  - `catalog_schema_version: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `provider: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `authority: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `program: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `dataset_id: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `dataset_name: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `declared_version: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `reference_page_url: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `archive_url: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `archive_filename: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `archive_size: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `archive_sha256: str`; default `required`; owns exactly the named validated factual or integrity value.
  - `packages: tuple[InpnProtectedAreasGeoPackageCatalog, ...]`; default `required`; owns exactly the named validated factual or integrity value.
  - `package_count: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `layer_count: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `field_count: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `total_feature_count: int`; default `required`; owns exactly the named validated factual or integrity value.
  - `complete_catalog_content_sha256: str`; default `required`; owns exactly the named validated factual or integrity value.
- Mutability/canonicality: frozen dataclass or frozen strict Pydantic configuration where declared; public intrinsic/boundary validation still checks exact runtime representation.

## 5. Function-by-function contract

### `_exact_text`

- Exact signature: `def _exact_text(value: object, label: str) -> str`
- Purpose: Exact text.
- Inputs: `value: object`, `label: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `str`.
- Ordered algorithm:

1. line 98: validates/branches on `type(value) is not str or not value or value != value.strip()`.
2. line 100: returns `value`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'{label} must be an exact string')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `type`, `value.strip`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_identity_key`

- Exact signature: `def _identity_key(value: str) -> str`
- Purpose: Identity key.
- Inputs: `value: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `str`.
- Ordered algorithm:

1. line 104: returns `unicodedata.normalize('NFKC', value).casefold()`.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `unicodedata.normalize`, `unicodedata.normalize('NFKC', value).casefold`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_require_unique_identities`

- Exact signature: `def _require_unique_identities(values: tuple[str, ...], label: str) -> None`
- Purpose: Require unique identities.
- Inputs: `values: tuple[str, ...]`, `label: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 108: validates/branches on `len(set(values)) != len(values)`.
2. line 110: derives `normalized` for subsequent validation or output construction.
3. line 111: validates/branches on `len(set(normalized)) != len(normalized)`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'{label} contains duplicate exact names')`; `InpnProtectedAreasCatalogError(f'{label} contains Unicode-NFKC/casefold collisions')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_identity_key`, `len`, `set`, `tuple`.
- Internal caller/callee relationship: directly invokes `_identity_key`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_is_link_or_junction`

- Exact signature: `def _is_link_or_junction(path: Path) -> bool`
- Purpose: Is link or junction.
- Inputs: `path: Path`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `bool`.
- Ordered algorithm:

1. line 118: executes a controlled error boundary catching `OSError` and performs any declared cleanup/finalization.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `path.is_junction`, `path.is_symlink`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_extraction_revalidation_rejects_link_or_junction_file`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_safe_package_path`

- Exact signature: `def _safe_package_path(extraction: InpnProtectedAreasExtraction, item: InpnProtectedAreasExtractedFile) -> Path`
- Purpose: Resolves one canonical package path below the extraction root while rejecting links, junctions, traversal, and special entries.
- Inputs: `extraction: InpnProtectedAreasExtraction`, `item: InpnProtectedAreasExtractedFile`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `Path`.
- Ordered algorithm:

1. line 128: derives `relative` for subsequent validation or output construction.
2. line 129: derives `windows` for subsequent validation or output construction.
3. line 130: validates/branches on `relative.is_absolute() or windows.is_absolute() or bool(windows.drive) or ('..' in relative.parts) or (relative.as_posix() != item.relative_path)`.
4. line 140: derives `root` for subsequent validation or output construction.
5. line 141: validates/branches on `_is_link_or_junction(root) or not root.is_dir()`.
6. line 143: derives `path` for subsequent validation or output construction.
7. line 144: derives `root_resolved` for subsequent validation or output construction.
8. line 145: derives `path_resolved` for subsequent validation or output construction.
9. line 146: validates/branches on `path_resolved == root_resolved or not path_resolved.is_relative_to(root_resolved)`.
10. line 152: derives `current` for subsequent validation or output construction.
11. line 153: iterates `component` over `relative.parts` in source order.
12. line 159: validates/branches on `not path.is_file()`.
13. line 163: returns `path`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {item.relative_path}: relative path is not canonical')`; `InpnProtectedAreasCatalogError('extraction root is missing or unsafe')`; `InpnProtectedAreasCatalogError(f'package {item.relative_path}: path escapes the extraction root')`; `InpnProtectedAreasCatalogError(f'package {item.relative_path}: source is not a regular file')`; `InpnProtectedAreasCatalogError(f'package {item.relative_path}: links or junctions are forbidden')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: `path.resolve`, `root.resolve`
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `PurePosixPath`, `PureWindowsPath`, `_is_link_or_junction`, `bool`, `path.is_file`, `path.resolve`, `path_resolved.is_relative_to`, `relative.as_posix`, `relative.is_absolute`, `root.is_dir`, `root.joinpath`, `root.resolve`, `windows.is_absolute`.
- Internal caller/callee relationship: directly invokes `_is_link_or_junction`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_read_verified_package_bytes`

- Exact signature: `def _read_verified_package_bytes(extraction: InpnProtectedAreasExtraction, item: InpnProtectedAreasExtractedFile) -> bytes`
- Purpose: Reads one package path exactly once and returns built-in immutable bytes after exact size and SHA validation.
- Inputs: `extraction: InpnProtectedAreasExtraction`, `item: InpnProtectedAreasExtractedFile`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `bytes`.
- Ordered algorithm:

1. line 170: derives `path` for subsequent validation or output construction.
2. line 171: executes a controlled error boundary catching `OSError` and performs any declared cleanup/finalization.
3. line 177: validates/branches on `type(package_bytes) is not bytes or len(package_bytes) != item.file_size or sha256(package_bytes).hexdigest() != item.sha256`.
4. line 185: returns `package_bytes`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {item.relative_path}: physical byte identity changed')`; `InpnProtectedAreasCatalogError(f'package {item.relative_path}: cannot read physical byte snapshot')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: `path.read_bytes`
- Hashing effects: `sha256`, `sha256(package_bytes).hexdigest`
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_safe_package_path`, `len`, `path.read_bytes`, `sha256`, `sha256(package_bytes).hexdigest`, `type`.
- Internal caller/callee relationship: directly invokes `_safe_package_path`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_metadata_sequence`

- Exact signature: `def _metadata_sequence(value: object, label: str) -> tuple[object, ...]`
- Purpose: Metadata sequence.
- Inputs: `value: object`, `label: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `tuple[object, ...]`.
- Ordered algorithm:

1. line 189: validates/branches on `isinstance(value, (str, bytes, bytearray, Mapping))`.
2. line 191: executes a controlled error boundary catching `(AttributeError, TypeError, ValueError)` and performs any declared cleanup/finalization.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'{label} metadata array is malformed')`; `TypeError` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `cast`, `hasattr`, `isinstance`, `tuple`, `type`, `value.tolist`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_layer_enumeration`

- Exact signature: `def _layer_enumeration(value: object, relative_path: str) -> tuple[tuple[str, str | None], ...]`
- Purpose: Layer enumeration.
- Inputs: `value: object`, `relative_path: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `tuple[tuple[str, str | None], ...]`.
- Ordered algorithm:

1. line 205: derives `rows` for subsequent validation or output construction.
2. line 206: validates/branches on `not rows`.
3. line 210: derives `result` for subsequent validation or output construction.
4. line 211: iterates `(position, raw_row)` over `enumerate(rows)` in source order.
5. line 231: performs `_require_unique_identities(tuple((name for name, _ in result)), f'package {relative_path} layer identities')`.
6. line 235: returns `tuple(result)`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path}: no OGR-visible layer')`; `InpnProtectedAreasCatalogError(f'package {relative_path}: layer enumeration row is malformed')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_exact_text`, `_metadata_sequence`, `_require_unique_identities`, `enumerate`, `len`, `result.append`, `tuple`.
- Internal caller/callee relationship: directly invokes `_exact_text`, `_metadata_sequence`, `_require_unique_identities`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_layer_enumeration_and_read_info_geometry_must_agree`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_metadata_mapping`

- Exact signature: `def _metadata_mapping(value: object, relative_path: str, layer_name: str) -> Mapping[object, object]`
- Purpose: Metadata mapping.
- Inputs: `value: object`, `relative_path: str`, `layer_name: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `Mapping[object, object]`.
- Ordered algorithm:

1. line 241: validates/branches on `not isinstance(value, Mapping)`.
2. line 245: returns `value`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: metadata is not a mapping')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `isinstance`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_required_metadata`

- Exact signature: `def _required_metadata(metadata: Mapping[object, object], key: str, relative_path: str, layer_name: str) -> object`
- Purpose: Required metadata.
- Inputs: `metadata: Mapping[object, object]`, `key: str`, `relative_path: str`, `layer_name: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `object`.
- Ordered algorithm:

1. line 254: validates/branches on `key not in metadata`.
2. line 258: returns `metadata[key]`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: missing {key} metadata')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_field_catalogs`

- Exact signature: `def _field_catalogs(metadata: Mapping[object, object], relative_path: str, layer_name: str) -> tuple[InpnProtectedAreasFieldCatalog, ...]`
- Purpose: Field catalogs.
- Inputs: `metadata: Mapping[object, object]`, `relative_path: str`, `layer_name: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `tuple[InpnProtectedAreasFieldCatalog, ...]`.
- Ordered algorithm:

1. line 266: derives `names` for subsequent validation or output construction.
2. line 270: derives `dtypes` for subsequent validation or output construction.
3. line 274: validates/branches on `len(names) != len(dtypes)`.
4. line 278: derives `fields` for subsequent validation or output construction.
5. line 279: iterates `(position, (raw_name, raw_dtype))` over `enumerate(zip(names, dtypes, strict=True))` in source order.
6. line 295: performs `_require_unique_identities(tuple((field.name for field in fields)), f'package {relative_path} layer {layer_name} field identities')`.
7. line 299: returns `tuple(fields)`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: field/dtype lengths differ')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `InpnProtectedAreasFieldCatalog`, `_exact_text`, `_metadata_sequence`, `_require_unique_identities`, `_required_metadata`, `enumerate`, `fields.append`, `len`, `tuple`, `zip`.
- Internal caller/callee relationship: directly invokes `_exact_text`, `_metadata_sequence`, `_require_unique_identities`, `_required_metadata`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_feature_count`

- Exact signature: `def _feature_count(value: object, relative_path: str, layer_name: str) -> int`
- Purpose: Feature count.
- Inputs: `value: object`, `relative_path: str`, `layer_name: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `int`.
- Ordered algorithm:

1. line 303: validates/branches on `type(value) is not int or value < 0`.
2. line 308: returns `value`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: feature count must be an exact non-negative integer')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `type`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_one_valid_geopackage_with_one_spatial_layer_is_cataloged`, `test_exact_non_negative_feature_count_is_accepted`, `test_boolean_or_negative_feature_count_is_rejected`, `test_metadata_calls_use_exact_forced_metadata_only_api`, `test_feature_count_rejects_non_exact_integers`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_missing_bound`

- Exact signature: `def _missing_bound(value: object) -> bool`
- Purpose: Missing bound.
- Inputs: `value: object`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `bool`.
- Ordered algorithm:

1. line 312: returns `value is None or (isinstance(value, Real) and (not isinstance(value, bool)) and math.isnan(float(value)))`.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `float`, `isinstance`, `math.isnan`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_empty_spatial_layer_with_partially_missing_bounds_is_rejected`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_bounds_sequence`

- Exact signature: `def _bounds_sequence(value: object, relative_path: str, layer_name: str) -> tuple[object, object, object, object]`
- Purpose: Bounds sequence.
- Inputs: `value: object`, `relative_path: str`, `layer_name: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `tuple[object, object, object, object]`.
- Ordered algorithm:

1. line 324: derives `values` for subsequent validation or output construction.
2. line 328: validates/branches on `len(values) != 4`.
3. line 332: returns `(values[0], values[1], values[2], values[3])`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: bounds must have four values')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_metadata_sequence`, `len`.
- Internal caller/callee relationship: directly invokes `_metadata_sequence`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_validated_bounds`

- Exact signature: `def _validated_bounds(value: object, *, is_spatial: bool, feature_count: int, relative_path: str, layer_name: str) -> tuple[float, float, float, float] | None`
- Purpose: Validated bounds.
- Inputs: `value: object`, `is_spatial: bool`, `feature_count: int`, `relative_path: str`, `layer_name: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `tuple[float, float, float, float] | None`.
- Ordered algorithm:

1. line 343: validates/branches on `not is_spatial`.
2. line 349: validates/branches on `value is None`.
3. line 355: derives `values` for subsequent validation or output construction.
4. line 356: derives `missing` for subsequent validation or output construction.
5. line 357: validates/branches on `any(missing)`.
6. line 363: validates/branches on `feature_count == 0`.
7. line 367: validates/branches on `any((isinstance(member, bool) or not isinstance(member, Real) for member in values))`.
8. line 373: derives `bounds` for subsequent validation or output construction.
9. line 374: validates/branches on `not all((math.isfinite(member) for member in bounds))`.
10. line 378: derives `(min_x, min_y, max_x, max_y)` for subsequent validation or output construction.
11. line 379: validates/branches on `min_x > max_x or min_y > max_y`.
12. line 383: returns `(min_x, min_y, max_x, max_y)`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: populated spatial bounds are missing')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: bounds are partially missing')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: empty spatial bounds must be null')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: bounds must be numeric')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: bounds must be finite')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: bounds are reversed')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: non-spatial bounds must be null')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_bounds_sequence`, `_missing_bound`, `all`, `any`, `cast`, `float`, `isinstance`, `math.isfinite`, `tuple`.
- Internal caller/callee relationship: directly invokes `_bounds_sequence`, `_missing_bound`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_canonical_crs`

- Exact signature: `def _canonical_crs(value: object, relative_path: str, layer_name: str) -> tuple[str, str | None, str | None, str]`
- Purpose: Canonical crs.
- Inputs: `value: object`, `relative_path: str`, `layer_name: str`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `tuple[str, str | None, str | None, str]`.
- Ordered algorithm:

1. line 391: derives `raw` for subsequent validation or output construction.
2. line 395: executes a controlled error boundary catching `Exception` and performs any declared cleanup/finalization.
3. line 403: validates/branches on `type(wkt) is not str or not wkt`.
4. line 407: validates/branches on `authority is None`.
5. line 409: validates/branches on `type(authority) is not tuple or len(authority) != 2 or any((type(member) is not str or not member for member in authority))`.
6. line 417: returns `(raw, authority[0], authority[1], wkt)`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: canonical CRS WKT is missing')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: CRS authority is malformed')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: CRS is not parseable')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `CRS.from_user_input`, `InpnProtectedAreasCatalogError`, `_exact_text`, `any`, `crs.to_authority`, `crs.to_wkt`, `len`, `type`.
- Internal caller/callee relationship: directly invokes `_exact_text`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_inspect_layer`

- Exact signature: `def _inspect_layer(package_bytes: bytes, relative_path: str, layer_name: str, layer_position: int, listed_geometry_type: str | None) -> tuple[InpnProtectedAreasLayerCatalog, str]`
- Purpose: Calls metadata-only Pyogrio inspection on package bytes and builds one strict ordered layer record, including exact GPKG driver evidence.
- Inputs: `package_bytes: bytes`, `relative_path: str`, `layer_name: str`, `layer_position: int`, `listed_geometry_type: str | None`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `tuple[InpnProtectedAreasLayerCatalog, str]`.
- Ordered algorithm:

1. line 427: executes a controlled error boundary catching `Exception`, `InpnProtectedAreasCatalogError` and performs any declared cleanup/finalization.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: driver must be exact GPKG')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: reported layer name differs')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: layer enumeration and metadata geometry types differ')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: metadata inspection failed')`; `InpnProtectedAreasCatalogError(f'package {relative_path} layer {layer_name}: non-spatial CRS must be null')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: `pyogrio.read_info`
- Callees: `InpnProtectedAreasCatalogError`, `InpnProtectedAreasLayerCatalog`, `_canonical_crs`, `_exact_text`, `_feature_count`, `_field_catalogs`, `_metadata_mapping`, `_required_metadata`, `_validated_bounds`, `pyogrio.read_info`.
- Internal caller/callee relationship: directly invokes `_canonical_crs`, `_exact_text`, `_feature_count`, `_field_catalogs`, `_metadata_mapping`, `_required_metadata`, `_validated_bounds`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_inspect_package`

- Exact signature: `def _inspect_package(extraction: InpnProtectedAreasExtraction, item: InpnProtectedAreasExtractedFile, package_position: int) -> InpnProtectedAreasGeoPackageCatalog`
- Purpose: Uses one package byte snapshot for layer enumeration and every layer metadata call, then records one exact-GPKG package.
- Inputs: `extraction: InpnProtectedAreasExtraction`, `item: InpnProtectedAreasExtractedFile`, `package_position: int`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `InpnProtectedAreasGeoPackageCatalog`.
- Ordered algorithm:

1. line 529: validates/branches on `PurePosixPath(item.relative_path).suffix.casefold() != '.gpkg'`.
2. line 533: executes a controlled error boundary catching `Exception`, `InpnProtectedAreasCatalogError` and performs any declared cleanup/finalization.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError(f'extracted file {item.relative_path} is not a GeoPackage and cannot be ignored')`; `InpnProtectedAreasCatalogError(f'package {item.relative_path}: layer driver metadata is inconsistent')`; `InpnProtectedAreasCatalogError(f'package {item.relative_path}: physical inspection failed')`; `InpnProtectedAreasCatalogError(f'package {item.relative_path}: OGR layer enumeration failed')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: `pyogrio.list_layers`
- Callees: `InpnProtectedAreasCatalogError`, `InpnProtectedAreasGeoPackageCatalog`, `PurePosixPath`, `PurePosixPath(item.relative_path).suffix.casefold`, `_inspect_layer`, `_layer_enumeration`, `_read_verified_package_bytes`, `enumerate`, `len`, `pyogrio.list_layers`, `set`, `tuple`.
- Internal caller/callee relationship: directly invokes `_inspect_layer`, `_layer_enumeration`, `_read_verified_package_bytes`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_public_api_exports_only_trusted_catalog_symbols`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_field_payload`

- Exact signature: `def _field_payload(field: InpnProtectedAreasFieldCatalog) -> dict[str, object]`
- Purpose: Field payload.
- Inputs: `field: InpnProtectedAreasFieldCatalog`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `dict[str, object]`.
- Ordered algorithm:

1. line 579: returns `{'name': field.name, 'source_dtype': field.source_dtype, 'position': field.position}`.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: none.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_layer_payload`

- Exact signature: `def _layer_payload(layer: InpnProtectedAreasLayerCatalog) -> dict[str, object]`
- Purpose: Layer payload.
- Inputs: `layer: InpnProtectedAreasLayerCatalog`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `dict[str, object]`.
- Ordered algorithm:

1. line 587: returns `{'layer_name': layer.layer_name, 'layer_position': layer.layer_position, 'feature_count': layer.feature_count, 'geometry_type_raw': layer.geometry_type_raw, 'is_spatial': layer.is_spatial, 'crs_raw': layer.crs_raw, 'crs_authority_name': layer.crs_authority_name, 'crs_authority_code': layer.crs_authority_code, 'crs_wkt': layer.crs_wkt, 'total_bounds': layer.total_bounds, 'fields': [_field_payload(field) for field in layer.fields]}`.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `_field_payload`.
- Internal caller/callee relationship: directly invokes `_field_payload`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_package_payload`

- Exact signature: `def _package_payload(package: InpnProtectedAreasGeoPackageCatalog) -> dict[str, object]`
- Purpose: Package payload.
- Inputs: `package: InpnProtectedAreasGeoPackageCatalog`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `dict[str, object]`.
- Ordered algorithm:

1. line 603: returns `{'relative_path': package.relative_path, 'file_size': package.file_size, 'file_sha256': package.file_sha256, 'package_position': package.package_position, 'driver_name': package.driver_name, 'layers': [_layer_payload(layer) for layer in package.layers]}`.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `_layer_payload`.
- Internal caller/callee relationship: directly invokes `_layer_payload`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_catalog_payload`

- Exact signature: `def _catalog_payload(catalog: InpnProtectedAreasCatalog) -> dict[str, object]`
- Purpose: Catalog payload.
- Inputs: `catalog: InpnProtectedAreasCatalog`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `dict[str, object]`.
- Ordered algorithm:

1. line 614: returns `{'catalog_schema_version': catalog.catalog_schema_version, 'provider': catalog.provider, 'authority': catalog.authority, 'program': catalog.program, 'dataset_id': catalog.dataset_id, 'dataset_name': catalog.dataset_name, 'declared_version': catalog.declared_version, 'reference_page_url': catalog.reference_page_url, 'archive_url': catalog.archive_url, 'archive_filename': catalog.archive_filename, 'archive_size': catalog.archive_size, 'archive_sha256': catalog.archive_sha256, 'packages': [_package_payload(package) for package in catalog.packages], 'package_count': catalog.package_count, 'layer_count': catalog.layer_count, 'field_count': catalog.field_count, 'total_feature_count': catalog.total_feature_count}`.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `_package_payload`.
- Internal caller/callee relationship: directly invokes `_package_payload`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_catalog_hash_excludes_absolute_paths_and_cache_state`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_catalog_content_sha256`

- Exact signature: `def _catalog_content_sha256(catalog: InpnProtectedAreasCatalog) -> str`
- Purpose: Hashes canonical portable JSON containing every catalog fact, including schema-2 driver identity, while excluding local/cache state.
- Inputs: `catalog: InpnProtectedAreasCatalog`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `str`.
- Ordered algorithm:

1. line 636: executes a controlled error boundary catching `(TypeError, ValueError)` and performs any declared cleanup/finalization.
2. line 648: returns `sha256(encoded).hexdigest()`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError('catalog content is not canonical JSON')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: `sha256`, `sha256(encoded).hexdigest`
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_catalog_payload`, `json.dumps`, `json.dumps(_catalog_payload(catalog), sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode`, `sha256`, `sha256(encoded).hexdigest`.
- Internal caller/callee relationship: directly invokes `_catalog_payload`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_one_valid_geopackage_with_one_spatial_layer_is_cataloged`, `test_package_layer_field_ordering_produces_deterministic_hash`, `test_absolute_extraction_path_does_not_affect_portable_catalog_hash`, `test_cache_hit_values_do_not_affect_portable_catalog_hash`, `test_public_api_exports_only_trusted_catalog_symbols`, `test_driver_is_hash_bound_and_coordinated_forgery_fails_rebuild`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_build_catalog`

- Exact signature: `def _build_catalog(extraction: InpnProtectedAreasExtraction) -> InpnProtectedAreasCatalog`
- Purpose: Build catalog.
- Inputs: `extraction: InpnProtectedAreasExtraction`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `InpnProtectedAreasCatalog`.
- Ordered algorithm:

1. line 654: derives `packages` for subsequent validation or output construction.
2. line 658: derives `download` for subsequent validation or output construction.
3. line 659: derives `catalog` for subsequent validation or output construction.
4. line 683: returns `InpnProtectedAreasCatalog(**{**catalog.__dict__, 'complete_catalog_content_sha256': _catalog_content_sha256(catalog)})`.

- Validation and exceptions: No explicit raise appears; validation is delegated to the listed callees and Python/library contracts. Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: `_catalog_content_sha256`
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalog`, `_catalog_content_sha256`, `_inspect_package`, `enumerate`, `len`, `sum`, `tuple`.
- Internal caller/callee relationship: directly invokes `_catalog_content_sha256`, `_inspect_package`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_validate_catalog_intrinsic`

- Exact signature: `def _validate_catalog_intrinsic(catalog: object) -> InpnProtectedAreasCatalog`
- Purpose: Proves exact canonical runtime types, domains, ordering, aggregates, nested record types, driver identity, and content hash.
- Inputs: `catalog: object`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `InpnProtectedAreasCatalog`.
- Ordered algorithm:

1. line 692: validates/branches on `type(catalog) is not InpnProtectedAreasCatalog`.
2. line 696: validates/branches on `type(catalog.catalog_schema_version) is not int or catalog.catalog_schema_version != CATALOG_HASH_SCHEMA_VERSION`.
3. line 701: iterates `name` over `('provider', 'authority', 'program', 'dataset_id', 'dataset_name', 'declared_version', 'reference_page_url', 'archive_url', 'archive_filename')` in source order.
4. line 713: validates/branches on `type(catalog.archive_size) is not int or catalog.archive_size <= 0`.
5. line 715: validates/branches on `type(catalog.archive_sha256) is not str or _SHA_PATTERN.fullmatch(catalog.archive_sha256) is None`.
6. line 720: validates/branches on `type(catalog.packages) is not tuple or not catalog.packages`.
7. line 725: derives `package_names` for subsequent validation or output construction.
8. line 726: derives `layer_count` for subsequent validation or output construction.
9. line 727: derives `field_count` for subsequent validation or output construction.
10. line 728: derives `feature_count` for subsequent validation or output construction.
11. line 729: iterates `(package_position, package)` over `enumerate(catalog.packages)` in source order.
12. line 862: performs `_require_unique_identities(tuple(package_names), 'catalog package identities')`.
13. line 863: validates/branches on `tuple(package_names) != tuple(sorted(package_names))`.
14. line 865: derives `expected_counts` for subsequent validation or output construction.
15. line 871: derives `actual_counts` for subsequent validation or output construction.
16. line 877: validates/branches on `any((type(value) is not int or value < 0 for value in actual_counts)) or actual_counts != expected_counts`.
17. line 881: validates/branches on `type(catalog.complete_catalog_content_sha256) is not str or _SHA_PATTERN.fullmatch(catalog.complete_catalog_content_sha256) is None or _catalog_content_sha256(catalog) != catalog.complete_catalog_content_sha256`.
18. line 887: returns `catalog`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError('catalog must be an exact InpnProtectedAreasCatalog')`; `InpnProtectedAreasCatalogError('catalog schema version is invalid')`; `InpnProtectedAreasCatalogError('catalog archive size is invalid')`; `InpnProtectedAreasCatalogError('catalog archive SHA256 is invalid')`; `InpnProtectedAreasCatalogError('catalog packages must be a non-empty tuple')`; `InpnProtectedAreasCatalogError('catalog package paths are not ordered')`; `InpnProtectedAreasCatalogError('catalog aggregate counts are invalid')`; `InpnProtectedAreasCatalogError('catalog content SHA256 is invalid')`; `InpnProtectedAreasCatalogError('catalog package type is invalid')`; `InpnProtectedAreasCatalogError('catalog package path is invalid')`; `InpnProtectedAreasCatalogError('catalog package order is invalid')`; `InpnProtectedAreasCatalogError('catalog package size is invalid')`; `InpnProtectedAreasCatalogError('catalog package SHA256 is invalid')`; `InpnProtectedAreasCatalogError('catalog package driver must be exact GPKG')`; `InpnProtectedAreasCatalogError('catalog package layers are invalid')`; `InpnProtectedAreasCatalogError('catalog layer type is invalid')`; `InpnProtectedAreasCatalogError('catalog layer order is invalid')`; `InpnProtectedAreasCatalogError('catalog spatial flag is invalid')`; `InpnProtectedAreasCatalogError('catalog bounds representation is not canonical')`; `InpnProtectedAreasCatalogError('catalog fields must be a tuple')`; `InpnProtectedAreasCatalogError('catalog spatial geometry type is invalid')`; `InpnProtectedAreasCatalogError('catalog CRS metadata is not canonical')`; `InpnProtectedAreasCatalogError('catalog non-spatial metadata is inconsistent')`; `InpnProtectedAreasCatalogError('catalog field type is invalid')`; `InpnProtectedAreasCatalogError('catalog field order is invalid')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: `_catalog_content_sha256`
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `PurePosixPath`, `_SHA_PATTERN.fullmatch`, `_canonical_crs`, `_catalog_content_sha256`, `_exact_text`, `_feature_count`, `_require_unique_identities`, `_validated_bounds`, `any`, `enumerate`, `field_names.append`, `getattr`, `layer_names.append`, `len`, `package_names.append`, `pure.as_posix`, `pure.is_absolute`, `pure.suffix.casefold`, `sorted`, `tuple`, `type`.
- Internal caller/callee relationship: directly invokes `_canonical_crs`, `_catalog_content_sha256`, `_exact_text`, `_feature_count`, `_require_unique_identities`, `_validated_bounds`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `_validate_source_locks`

- Exact signature: `def _validate_source_locks(catalog: InpnProtectedAreasCatalog, extraction: InpnProtectedAreasExtraction) -> None`
- Purpose: Validate source locks.
- Inputs: `catalog: InpnProtectedAreasCatalog`, `extraction: InpnProtectedAreasExtraction`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 894: derives `download` for subsequent validation or output construction.
2. line 895: derives `expected` for subsequent validation or output construction.
3. line 908: derives `actual` for subsequent validation or output construction.
4. line 921: validates/branches on `actual != expected`.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError('catalog source/archive lineage differs from the verified extraction')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`.
- Internal caller/callee relationship: directly invokes no module helper; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: covered transitively through public-boundary tests or class validators.
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `build_inpn_protected_areas_catalog`

- Exact signature: `def build_inpn_protected_areas_catalog(extraction: InpnProtectedAreasExtraction, config: InpnProtectedAreasSourceConfig) -> InpnProtectedAreasCatalog`
- Purpose: Source-completely builds a metadata-only schema-2 catalog between full extraction validations.
- Inputs: `extraction: InpnProtectedAreasExtraction`, `config: InpnProtectedAreasSourceConfig`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `InpnProtectedAreasCatalog`.
- Ordered algorithm:

1. line 931: performs `'Build a portable metadata-only catalog from one verified EP extraction.'`.
2. line 933: executes a controlled error boundary catching `Exception`, `InpnProtectedAreasCatalogError`, `InpnProtectedAreasSourceError` and performs any declared cleanup/finalization.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError('extraction physical inventory changed during metadata inspection')`; `InpnProtectedAreasCatalogError('INPN extraction byte identity changed or failed source-complete catalog validation')`; `InpnProtectedAreasCatalogError('INPN protected-areas metadata catalog cannot be built safely')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_build_catalog`, `_validate_catalog_intrinsic`, `validate_inpn_protected_areas_extraction`.
- Internal caller/callee relationship: directly invokes `_build_catalog`, `_validate_catalog_intrinsic`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_one_valid_geopackage_with_one_spatial_layer_is_cataloged`, `test_package_with_multiple_layers_preserves_physical_order`, `test_multiple_geopackages_remain_in_extraction_order`, `test_non_geopackage_extracted_file_is_not_silently_ignored`, `test_zero_visible_layers_is_rejected`, `test_layer_name_with_edge_whitespace_is_rejected`, `test_duplicate_casefold_or_nfkc_layer_identity_is_rejected`, `test_file_byte_mutation_during_metadata_inspection_is_rejected`, `test_exact_field_and_dtype_order_is_preserved`, `test_field_and_dtype_length_mismatch_is_rejected`, `test_empty_or_edge_whitespace_field_name_is_rejected`, `test_duplicate_casefold_or_nfkc_field_identity_is_rejected`, `test_malformed_source_dtype_is_rejected`, `test_exact_non_negative_feature_count_is_accepted`, `test_boolean_or_negative_feature_count_is_rejected`, `test_populated_spatial_layer_without_crs_is_rejected`, `test_unparseable_crs_is_rejected`, `test_valid_crs_authority_and_canonical_wkt_are_recorded`, `test_finite_ordered_bounds_are_accepted`, `test_non_finite_populated_bounds_are_rejected`, `test_reversed_bounds_are_rejected`, `test_empty_spatial_layer_normalizes_all_nan_bounds_to_null`, `test_non_spatial_layer_with_crs_or_bounds_is_rejected`, `test_package_layer_field_ordering_produces_deterministic_hash`, `test_caller_package_reordering_is_rejected`, `test_coordinated_metadata_and_hash_mutation_is_rejected_by_rebuild`, `test_absolute_extraction_path_does_not_affect_portable_catalog_hash`, `test_cache_hit_values_do_not_affect_portable_catalog_hash`, `test_catalog_validation_detects_changed_physical_metadata`, `test_catalog_construction_never_materializes_feature_rows`, `test_metadata_calls_use_exact_forced_metadata_only_api`, `test_empty_spatial_layer_with_partially_missing_bounds_is_rejected`, `test_layer_enumeration_and_read_info_geometry_must_agree`, `test_feature_count_rejects_non_exact_integers`, `test_catalog_hash_excludes_absolute_paths_and_cache_state`, `test_pyogrio_metadata_apis_receive_one_identical_package_byte_snapshot`, `test_transient_package_path_swap_cannot_inject_other_package_metadata`, `test_catalog_rejects_coordinated_valid_package_marker_and_caller_forgery_before_pyogrio`, `test_exact_gpkg_driver_is_recorded`, `test_missing_null_or_wrong_driver_is_rejected`, `test_inconsistent_layer_driver_values_are_rejected`, `test_renamed_geojson_content_with_gpkg_suffix_is_rejected`, `test_driver_is_hash_bound_and_coordinated_forgery_fails_rebuild`, `test_catalog_schema_two_rejects_schema_one_catalog`, `test_noncanonical_supplied_bounds_are_rejected_before_rebuild`, `test_noncanonical_optional_crs_string_subclasses_are_rejected`, `test_builder_output_uses_only_exact_canonical_runtime_types`, `test_correct_exact_float_tuple_and_optional_strings_validate`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

### `validate_inpn_protected_areas_catalog`

- Exact signature: `def validate_inpn_protected_areas_catalog(extraction: InpnProtectedAreasExtraction, config: InpnProtectedAreasSourceConfig, catalog: InpnProtectedAreasCatalog) -> None`
- Purpose: Validates intrinsic/source locks, independently rebuilds from verified package snapshots, and exact-compares the complete catalog.
- Inputs: `extraction: InpnProtectedAreasExtraction`, `config: InpnProtectedAreasSourceConfig`, `catalog: InpnProtectedAreasCatalog`; defaults and keyword-only status are fixed by the exact signature and source snapshot.
- Output: `None`.
- Ordered algorithm:

1. line 960: performs `'Independently rebuild and exact-compare one supplied physical catalog.'`.
2. line 962: executes a controlled error boundary catching `Exception`, `InpnProtectedAreasCatalogError`, `InpnProtectedAreasSourceError` and performs any declared cleanup/finalization.

- Validation and exceptions: Explicit fail-closed raises: `InpnProtectedAreasCatalogError('catalog differs from the independently rebuilt physical metadata')`; `InpnProtectedAreasCatalogError('INPN extraction failed catalog source-lock validation')`; `InpnProtectedAreasCatalogError('INPN protected-areas catalog validation failed safely')` Library errors are contained by the function's visible error boundary when one exists.
- Filesystem effects: none directly; any effects belong to named callees.
- Hashing effects: none directly.
- Pyogrio calls: none.
- Callees: `InpnProtectedAreasCatalogError`, `_validate_catalog_intrinsic`, `_validate_source_locks`, `build_inpn_protected_areas_catalog`, `validate_inpn_protected_areas_extraction`.
- Internal caller/callee relationship: directly invokes `_validate_catalog_intrinsic`, `_validate_source_locks`, `build_inpn_protected_areas_catalog`; module callers are enumerated by the exact call graph and public flow below.
- Direct regression references: `test_one_valid_geopackage_with_one_spatial_layer_is_cataloged`, `test_caller_package_reordering_is_rejected`, `test_coordinated_metadata_and_hash_mutation_is_rejected_by_rebuild`, `test_catalog_validation_detects_changed_physical_metadata`, `test_catalog_validator_rejects_wrong_runtime_type`, `test_driver_is_hash_bound_and_coordinated_forgery_fails_rebuild`, `test_catalog_schema_two_rejects_schema_one_catalog`, `test_noncanonical_supplied_bounds_are_rejected_before_rebuild`, `test_noncanonical_optional_crs_string_subclasses_are_rejected`, `test_correct_exact_float_tuple_and_optional_strings_validate`
- Business boundary: factual acquisition, integrity, or physical metadata evidence only.
- Explicit non-goals: no EP feature-row materialization, protected-area category interpretation, Natura 2000/ZNIEFF meaning, parcel relation, exclusion, scoring, or ranking.

## 6. Public flow, side effects, and hashing

- Acquisition validates configuration and download lineage, reuses a valid local cache offline, or performs the existing safe HTTPS download and transactional cache publication.
- Archive authority is one built-in `bytes` snapshot. ZIP validation, member hashing, and extraction streaming use that same snapshot object.
- Extraction cache validation proves exact ordered path/size/SHA equality across archive inventory, marker, physical files, and caller evidence.
- Cataloging validates the extraction before and after metadata inspection, reads each package path once, and gives the same built-in `bytes` object to `pyogrio.list_layers` and every `pyogrio.read_info` call for that package.
- Only metadata APIs run. No API that materializes feature rows or geometries is called.
- Schema 2 hashes canonical JSON including exact package driver identity. Absolute paths, timestamps, cache-hit flags, Python repr, and object identity remain excluded.

## 7. Public exports

Exact declaration and order:

```python
__all__ = [
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
    "InpnProtectedAreasLayerCatalog",
    "build_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_catalog",
]
```

For `inpn_protected_areas_fr.py`, `validate_inpn_protected_areas_extraction` is explicitly present. For the catalog module, only the supported immutable records, controlled exception, builder, and independent validator are public.

## 8. Tests and change impact

- `tests/unit/test_inpn_protected_areas_fr.py` proves archive/download/cache/ZIP/extraction behavior, including coordinated marker/file corruption, archive-derived inventory, local offline rebuild, and archive-path swap isolation.
- `tests/unit/test_inpn_protected_areas_catalog_fr.py` proves byte-only Pyogrio metadata calls, package swap isolation, persistent mutation rejection, exact driver identity, schema 2, canonical final runtime types, hashing, independent rebuild, and zero feature materialization.
- Any change requires both focused suites, controlled offline EP verification, companion SHA synchronization, full pytest, Ruff check/format, mypy, uv lock/pip checks, and `git diff --check`.

## 9. Exact complete current file content

This snapshot reproduces every current source line; the raw-byte SHA above is the binding authority.

```python
"""Source-bound metadata-only catalog of verified INPN EP GeoPackages."""

from __future__ import annotations

import json
import math
import re
import unicodedata
from collections.abc import Mapping
from dataclasses import dataclass
from hashlib import sha256
from numbers import Real
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import SupportsFloat, cast

import pyogrio  # type: ignore[import-untyped]
from pyproj import CRS

from landscout.sources.inpn_protected_areas_fr import (
    InpnProtectedAreasExtractedFile,
    InpnProtectedAreasExtraction,
    InpnProtectedAreasSourceConfig,
    InpnProtectedAreasSourceError,
    validate_inpn_protected_areas_extraction,
)

CATALOG_HASH_SCHEMA_VERSION = 2
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")


class InpnProtectedAreasCatalogError(ValueError):
    """Raised when exact EP GeoPackage metadata cannot be proven safely."""


@dataclass(frozen=True)
class InpnProtectedAreasFieldCatalog:
    """One source-ordered physical attribute-field metadata record."""

    name: str
    source_dtype: str
    position: int


@dataclass(frozen=True)
class InpnProtectedAreasLayerCatalog:
    """One source-ordered OGR layer metadata record without feature rows."""

    layer_name: str
    layer_position: int
    feature_count: int
    geometry_type_raw: str | None
    is_spatial: bool
    crs_raw: str | None
    crs_authority_name: str | None
    crs_authority_code: str | None
    crs_wkt: str | None
    total_bounds: tuple[float, float, float, float] | None
    fields: tuple[InpnProtectedAreasFieldCatalog, ...]


@dataclass(frozen=True)
class InpnProtectedAreasGeoPackageCatalog:
    """One extraction-ordered verified GeoPackage and all of its OGR layers."""

    relative_path: str
    file_size: int
    file_sha256: str
    package_position: int
    driver_name: str
    layers: tuple[InpnProtectedAreasLayerCatalog, ...]


@dataclass(frozen=True)
class InpnProtectedAreasCatalog:
    """Portable factual metadata catalog bound to one verified INPN EP snapshot."""

    catalog_schema_version: int
    provider: str
    authority: str
    program: str
    dataset_id: str
    dataset_name: str
    declared_version: str
    reference_page_url: str
    archive_url: str
    archive_filename: str
    archive_size: int
    archive_sha256: str
    packages: tuple[InpnProtectedAreasGeoPackageCatalog, ...]
    package_count: int
    layer_count: int
    field_count: int
    total_feature_count: int
    complete_catalog_content_sha256: str


def _exact_text(value: object, label: str) -> str:
    if type(value) is not str or not value or value != value.strip():
        raise InpnProtectedAreasCatalogError(f"{label} must be an exact string")
    return value


def _identity_key(value: str) -> str:
    return unicodedata.normalize("NFKC", value).casefold()


def _require_unique_identities(values: tuple[str, ...], label: str) -> None:
    if len(set(values)) != len(values):
        raise InpnProtectedAreasCatalogError(f"{label} contains duplicate exact names")
    normalized = tuple(_identity_key(value) for value in values)
    if len(set(normalized)) != len(normalized):
        raise InpnProtectedAreasCatalogError(
            f"{label} contains Unicode-NFKC/casefold collisions"
        )


def _is_link_or_junction(path: Path) -> bool:
    try:
        return path.is_symlink() or path.is_junction()
    except OSError:
        return True


def _safe_package_path(
    extraction: InpnProtectedAreasExtraction,
    item: InpnProtectedAreasExtractedFile,
) -> Path:
    relative = PurePosixPath(item.relative_path)
    windows = PureWindowsPath(item.relative_path)
    if (
        relative.is_absolute()
        or windows.is_absolute()
        or bool(windows.drive)
        or ".." in relative.parts
        or relative.as_posix() != item.relative_path
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: relative path is not canonical"
        )
    root = extraction.extraction_path
    if _is_link_or_junction(root) or not root.is_dir():
        raise InpnProtectedAreasCatalogError("extraction root is missing or unsafe")
    path = root.joinpath(*relative.parts)
    root_resolved = root.resolve(strict=True)
    path_resolved = path.resolve(strict=True)
    if path_resolved == root_resolved or not path_resolved.is_relative_to(
        root_resolved
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: path escapes the extraction root"
        )
    current = root
    for component in relative.parts:
        current = current / component
        if _is_link_or_junction(current):
            raise InpnProtectedAreasCatalogError(
                f"package {item.relative_path}: links or junctions are forbidden"
            )
    if not path.is_file():
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: source is not a regular file"
        )
    return path


def _read_verified_package_bytes(
    extraction: InpnProtectedAreasExtraction,
    item: InpnProtectedAreasExtractedFile,
) -> bytes:
    path = _safe_package_path(extraction, item)
    try:
        package_bytes = path.read_bytes()
    except OSError as error:
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: cannot read physical byte snapshot"
        ) from error
    if (
        type(package_bytes) is not bytes
        or len(package_bytes) != item.file_size
        or sha256(package_bytes).hexdigest() != item.sha256
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: physical byte identity changed"
        )
    return package_bytes


def _metadata_sequence(value: object, label: str) -> tuple[object, ...]:
    if isinstance(value, (str, bytes, bytearray, Mapping)):
        raise InpnProtectedAreasCatalogError(f"{label} metadata array is malformed")
    try:
        converted = value.tolist() if hasattr(value, "tolist") else value
        if type(converted) not in (list, tuple):
            raise TypeError
        return tuple(cast(list[object] | tuple[object, ...], converted))
    except (AttributeError, TypeError, ValueError) as error:
        raise InpnProtectedAreasCatalogError(
            f"{label} metadata array is malformed"
        ) from error


def _layer_enumeration(
    value: object, relative_path: str
) -> tuple[tuple[str, str | None], ...]:
    rows = _metadata_sequence(value, f"package {relative_path} layer enumeration")
    if not rows:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path}: no OGR-visible layer"
        )
    result: list[tuple[str, str | None]] = []
    for position, raw_row in enumerate(rows):
        row = _metadata_sequence(
            raw_row,
            f"package {relative_path} layer {position}",
        )
        if len(row) != 2:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path}: layer enumeration row is malformed"
            )
        name = _exact_text(
            row[0],
            f"package {relative_path} layer name at position {position}",
        )
        raw_geometry = row[1]
        if raw_geometry is not None:
            raw_geometry = _exact_text(
                raw_geometry,
                f"package {relative_path} layer {name} geometry type",
            )
        result.append((name, raw_geometry))
    _require_unique_identities(
        tuple(name for name, _ in result),
        f"package {relative_path} layer identities",
    )
    return tuple(result)


def _metadata_mapping(
    value: object, relative_path: str, layer_name: str
) -> Mapping[object, object]:
    if not isinstance(value, Mapping):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: metadata is not a mapping"
        )
    return value


def _required_metadata(
    metadata: Mapping[object, object],
    key: str,
    relative_path: str,
    layer_name: str,
) -> object:
    if key not in metadata:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: missing {key} metadata"
        )
    return metadata[key]


def _field_catalogs(
    metadata: Mapping[object, object],
    relative_path: str,
    layer_name: str,
) -> tuple[InpnProtectedAreasFieldCatalog, ...]:
    names = _metadata_sequence(
        _required_metadata(metadata, "fields", relative_path, layer_name),
        f"package {relative_path} layer {layer_name} fields",
    )
    dtypes = _metadata_sequence(
        _required_metadata(metadata, "dtypes", relative_path, layer_name),
        f"package {relative_path} layer {layer_name} dtypes",
    )
    if len(names) != len(dtypes):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: field/dtype lengths differ"
        )
    fields: list[InpnProtectedAreasFieldCatalog] = []
    for position, (raw_name, raw_dtype) in enumerate(zip(names, dtypes, strict=True)):
        name = _exact_text(
            raw_name,
            f"package {relative_path} layer {layer_name} field name at position {position}",
        )
        source_dtype = _exact_text(
            raw_dtype,
            f"package {relative_path} layer {layer_name} dtype for field {name}",
        )
        fields.append(
            InpnProtectedAreasFieldCatalog(
                name=name,
                source_dtype=source_dtype,
                position=position,
            )
        )
    _require_unique_identities(
        tuple(field.name for field in fields),
        f"package {relative_path} layer {layer_name} field identities",
    )
    return tuple(fields)


def _feature_count(value: object, relative_path: str, layer_name: str) -> int:
    if type(value) is not int or value < 0:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: feature count must be "
            "an exact non-negative integer"
        )
    return value


def _missing_bound(value: object) -> bool:
    return value is None or (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and math.isnan(float(value))
    )


def _bounds_sequence(
    value: object,
    relative_path: str,
    layer_name: str,
) -> tuple[object, object, object, object]:
    values = _metadata_sequence(
        value,
        f"package {relative_path} layer {layer_name} bounds",
    )
    if len(values) != 4:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds must have four values"
        )
    return values[0], values[1], values[2], values[3]


def _validated_bounds(
    value: object,
    *,
    is_spatial: bool,
    feature_count: int,
    relative_path: str,
    layer_name: str,
) -> tuple[float, float, float, float] | None:
    if not is_spatial:
        if value is not None:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: non-spatial bounds must be null"
            )
        return None
    if value is None:
        if feature_count == 0:
            return None
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: populated spatial bounds are missing"
        )
    values = _bounds_sequence(value, relative_path, layer_name)
    missing = tuple(_missing_bound(member) for member in values)
    if any(missing):
        if feature_count == 0 and all(missing):
            return None
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds are partially missing"
        )
    if feature_count == 0:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: empty spatial bounds must be null"
        )
    if any(
        isinstance(member, bool) or not isinstance(member, Real) for member in values
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds must be numeric"
        )
    bounds = tuple(float(cast(SupportsFloat, member)) for member in values)
    if not all(math.isfinite(member) for member in bounds):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds must be finite"
        )
    min_x, min_y, max_x, max_y = bounds
    if min_x > max_x or min_y > max_y:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: bounds are reversed"
        )
    return min_x, min_y, max_x, max_y


def _canonical_crs(
    value: object,
    relative_path: str,
    layer_name: str,
) -> tuple[str, str | None, str | None, str]:
    raw = _exact_text(
        value,
        f"package {relative_path} layer {layer_name} CRS",
    )
    try:
        crs = CRS.from_user_input(raw)
        wkt = crs.to_wkt(version="WKT2_2019", pretty=False)
        authority = crs.to_authority()
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: CRS is not parseable"
        ) from error
    if type(wkt) is not str or not wkt:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: canonical CRS WKT is missing"
        )
    if authority is None:
        return raw, None, None, wkt
    if (
        type(authority) is not tuple
        or len(authority) != 2
        or any(type(member) is not str or not member for member in authority)
    ):
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: CRS authority is malformed"
        )
    return raw, authority[0], authority[1], wkt


def _inspect_layer(
    package_bytes: bytes,
    relative_path: str,
    layer_name: str,
    layer_position: int,
    listed_geometry_type: str | None,
) -> tuple[InpnProtectedAreasLayerCatalog, str]:
    try:
        raw_metadata = pyogrio.read_info(
            package_bytes,
            layer=layer_name,
            force_feature_count=True,
            force_total_bounds=True,
        )
        metadata = _metadata_mapping(raw_metadata, relative_path, layer_name)
        driver_name = _exact_text(
            _required_metadata(metadata, "driver", relative_path, layer_name),
            f"package {relative_path} layer {layer_name} driver",
        )
        if driver_name != "GPKG":
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: driver must be exact GPKG"
            )
        reported_name = _exact_text(
            _required_metadata(metadata, "layer_name", relative_path, layer_name),
            f"package {relative_path} layer {layer_name} reported name",
        )
        if reported_name != layer_name:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: reported layer name differs"
            )
        raw_geometry = _required_metadata(
            metadata,
            "geometry_type",
            relative_path,
            layer_name,
        )
        geometry_type = (
            None
            if raw_geometry is None
            else _exact_text(
                raw_geometry,
                f"package {relative_path} layer {layer_name} geometry type",
            )
        )
        if geometry_type != listed_geometry_type:
            raise InpnProtectedAreasCatalogError(
                f"package {relative_path} layer {layer_name}: layer enumeration and "
                "metadata geometry types differ"
            )
        is_spatial = geometry_type is not None
        count = _feature_count(
            _required_metadata(metadata, "features", relative_path, layer_name),
            relative_path,
            layer_name,
        )
        raw_crs = _required_metadata(metadata, "crs", relative_path, layer_name)
        crs_raw: str | None
        authority_name: str | None
        authority_code: str | None
        crs_wkt: str | None
        if is_spatial:
            crs_raw, authority_name, authority_code, crs_wkt = _canonical_crs(
                raw_crs,
                relative_path,
                layer_name,
            )
        else:
            if raw_crs is not None:
                raise InpnProtectedAreasCatalogError(
                    f"package {relative_path} layer {layer_name}: non-spatial CRS must be null"
                )
            crs_raw = authority_name = authority_code = crs_wkt = None
        bounds = _validated_bounds(
            _required_metadata(metadata, "total_bounds", relative_path, layer_name),
            is_spatial=is_spatial,
            feature_count=count,
            relative_path=relative_path,
            layer_name=layer_name,
        )
        return (
            InpnProtectedAreasLayerCatalog(
                layer_name=layer_name,
                layer_position=layer_position,
                feature_count=count,
                geometry_type_raw=geometry_type,
                is_spatial=is_spatial,
                crs_raw=crs_raw,
                crs_authority_name=authority_name,
                crs_authority_code=authority_code,
                crs_wkt=crs_wkt,
                total_bounds=bounds,
                fields=_field_catalogs(metadata, relative_path, layer_name),
            ),
            driver_name,
        )
    except InpnProtectedAreasCatalogError:
        raise
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            f"package {relative_path} layer {layer_name}: metadata inspection failed"
        ) from error


def _inspect_package(
    extraction: InpnProtectedAreasExtraction,
    item: InpnProtectedAreasExtractedFile,
    package_position: int,
) -> InpnProtectedAreasGeoPackageCatalog:
    if PurePosixPath(item.relative_path).suffix.casefold() != ".gpkg":
        raise InpnProtectedAreasCatalogError(
            f"extracted file {item.relative_path} is not a GeoPackage and cannot be ignored"
        )
    try:
        package_bytes = _read_verified_package_bytes(extraction, item)
        try:
            enumeration = _layer_enumeration(
                pyogrio.list_layers(package_bytes),
                item.relative_path,
            )
        except InpnProtectedAreasCatalogError:
            raise
        except Exception as error:
            raise InpnProtectedAreasCatalogError(
                f"package {item.relative_path}: OGR layer enumeration failed"
            ) from error
        inspected = tuple(
            _inspect_layer(
                package_bytes,
                item.relative_path,
                layer_name,
                layer_position,
                geometry_type,
            )
            for layer_position, (layer_name, geometry_type) in enumerate(enumeration)
        )
        layers = tuple(layer for layer, _ in inspected)
        drivers = tuple(driver for _, driver in inspected)
        if len(set(drivers)) != 1 or drivers[0] != "GPKG":
            raise InpnProtectedAreasCatalogError(
                f"package {item.relative_path}: layer driver metadata is inconsistent"
            )
        return InpnProtectedAreasGeoPackageCatalog(
            relative_path=item.relative_path,
            file_size=item.file_size,
            file_sha256=item.sha256,
            package_position=package_position,
            driver_name=drivers[0],
            layers=layers,
        )
    except InpnProtectedAreasCatalogError:
        raise
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            f"package {item.relative_path}: physical inspection failed"
        ) from error


def _field_payload(field: InpnProtectedAreasFieldCatalog) -> dict[str, object]:
    return {
        "name": field.name,
        "source_dtype": field.source_dtype,
        "position": field.position,
    }


def _layer_payload(layer: InpnProtectedAreasLayerCatalog) -> dict[str, object]:
    return {
        "layer_name": layer.layer_name,
        "layer_position": layer.layer_position,
        "feature_count": layer.feature_count,
        "geometry_type_raw": layer.geometry_type_raw,
        "is_spatial": layer.is_spatial,
        "crs_raw": layer.crs_raw,
        "crs_authority_name": layer.crs_authority_name,
        "crs_authority_code": layer.crs_authority_code,
        "crs_wkt": layer.crs_wkt,
        "total_bounds": layer.total_bounds,
        "fields": [_field_payload(field) for field in layer.fields],
    }


def _package_payload(package: InpnProtectedAreasGeoPackageCatalog) -> dict[str, object]:
    return {
        "relative_path": package.relative_path,
        "file_size": package.file_size,
        "file_sha256": package.file_sha256,
        "package_position": package.package_position,
        "driver_name": package.driver_name,
        "layers": [_layer_payload(layer) for layer in package.layers],
    }


def _catalog_payload(catalog: InpnProtectedAreasCatalog) -> dict[str, object]:
    return {
        "catalog_schema_version": catalog.catalog_schema_version,
        "provider": catalog.provider,
        "authority": catalog.authority,
        "program": catalog.program,
        "dataset_id": catalog.dataset_id,
        "dataset_name": catalog.dataset_name,
        "declared_version": catalog.declared_version,
        "reference_page_url": catalog.reference_page_url,
        "archive_url": catalog.archive_url,
        "archive_filename": catalog.archive_filename,
        "archive_size": catalog.archive_size,
        "archive_sha256": catalog.archive_sha256,
        "packages": [_package_payload(package) for package in catalog.packages],
        "package_count": catalog.package_count,
        "layer_count": catalog.layer_count,
        "field_count": catalog.field_count,
        "total_feature_count": catalog.total_feature_count,
    }


def _catalog_content_sha256(catalog: InpnProtectedAreasCatalog) -> str:
    try:
        encoded = json.dumps(
            _catalog_payload(catalog),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise InpnProtectedAreasCatalogError(
            "catalog content is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _build_catalog(
    extraction: InpnProtectedAreasExtraction,
) -> InpnProtectedAreasCatalog:
    packages = tuple(
        _inspect_package(extraction, item, position)
        for position, item in enumerate(extraction.files)
    )
    download = extraction.download
    catalog = InpnProtectedAreasCatalog(
        catalog_schema_version=CATALOG_HASH_SCHEMA_VERSION,
        provider=download.provider,
        authority=download.authority,
        program=download.program,
        dataset_id=download.dataset_id,
        dataset_name=download.dataset_name,
        declared_version=download.declared_version,
        reference_page_url=download.reference_page_url,
        archive_url=download.archive_url,
        archive_filename=download.filename,
        archive_size=download.file_size,
        archive_sha256=download.sha256,
        packages=packages,
        package_count=len(packages),
        layer_count=sum(len(package.layers) for package in packages),
        field_count=sum(
            len(layer.fields) for package in packages for layer in package.layers
        ),
        total_feature_count=sum(
            layer.feature_count for package in packages for layer in package.layers
        ),
        complete_catalog_content_sha256="",
    )
    return InpnProtectedAreasCatalog(
        **{
            **catalog.__dict__,
            "complete_catalog_content_sha256": _catalog_content_sha256(catalog),
        }
    )


def _validate_catalog_intrinsic(catalog: object) -> InpnProtectedAreasCatalog:
    if type(catalog) is not InpnProtectedAreasCatalog:
        raise InpnProtectedAreasCatalogError(
            "catalog must be an exact InpnProtectedAreasCatalog"
        )
    if (
        type(catalog.catalog_schema_version) is not int
        or catalog.catalog_schema_version != CATALOG_HASH_SCHEMA_VERSION
    ):
        raise InpnProtectedAreasCatalogError("catalog schema version is invalid")
    for name in (
        "provider",
        "authority",
        "program",
        "dataset_id",
        "dataset_name",
        "declared_version",
        "reference_page_url",
        "archive_url",
        "archive_filename",
    ):
        _exact_text(getattr(catalog, name), f"catalog {name}")
    if type(catalog.archive_size) is not int or catalog.archive_size <= 0:
        raise InpnProtectedAreasCatalogError("catalog archive size is invalid")
    if (
        type(catalog.archive_sha256) is not str
        or _SHA_PATTERN.fullmatch(catalog.archive_sha256) is None
    ):
        raise InpnProtectedAreasCatalogError("catalog archive SHA256 is invalid")
    if type(catalog.packages) is not tuple or not catalog.packages:
        raise InpnProtectedAreasCatalogError(
            "catalog packages must be a non-empty tuple"
        )

    package_names: list[str] = []
    layer_count = 0
    field_count = 0
    feature_count = 0
    for package_position, package in enumerate(catalog.packages):
        if type(package) is not InpnProtectedAreasGeoPackageCatalog:
            raise InpnProtectedAreasCatalogError("catalog package type is invalid")
        relative_path = _exact_text(package.relative_path, "catalog package path")
        pure = PurePosixPath(relative_path)
        if (
            pure.as_posix() != relative_path
            or pure.is_absolute()
            or ".." in pure.parts
            or pure.suffix.casefold() != ".gpkg"
        ):
            raise InpnProtectedAreasCatalogError("catalog package path is invalid")
        package_names.append(relative_path)
        if type(package.package_position) is not int or (
            package.package_position != package_position
        ):
            raise InpnProtectedAreasCatalogError("catalog package order is invalid")
        if type(package.file_size) is not int or package.file_size <= 0:
            raise InpnProtectedAreasCatalogError("catalog package size is invalid")
        if (
            type(package.file_sha256) is not str
            or _SHA_PATTERN.fullmatch(package.file_sha256) is None
        ):
            raise InpnProtectedAreasCatalogError("catalog package SHA256 is invalid")
        driver_name = _exact_text(package.driver_name, "catalog package driver")
        if driver_name != "GPKG":
            raise InpnProtectedAreasCatalogError(
                "catalog package driver must be exact GPKG"
            )
        if type(package.layers) is not tuple or not package.layers:
            raise InpnProtectedAreasCatalogError("catalog package layers are invalid")
        layer_names: list[str] = []
        for layer_position, layer in enumerate(package.layers):
            if type(layer) is not InpnProtectedAreasLayerCatalog:
                raise InpnProtectedAreasCatalogError("catalog layer type is invalid")
            layer_name = _exact_text(layer.layer_name, "catalog layer name")
            layer_names.append(layer_name)
            if type(layer.layer_position) is not int or (
                layer.layer_position != layer_position
            ):
                raise InpnProtectedAreasCatalogError("catalog layer order is invalid")
            count = _feature_count(layer.feature_count, relative_path, layer_name)
            if type(layer.is_spatial) is not bool:
                raise InpnProtectedAreasCatalogError("catalog spatial flag is invalid")
            if layer.is_spatial:
                geometry_type = _exact_text(
                    layer.geometry_type_raw,
                    f"catalog layer {layer_name} geometry type",
                )
                if not geometry_type:
                    raise InpnProtectedAreasCatalogError(
                        "catalog spatial geometry type is invalid"
                    )
                _exact_text(layer.crs_raw, f"catalog layer {layer_name} CRS")
                if layer.crs_authority_name is not None:
                    _exact_text(
                        layer.crs_authority_name,
                        f"catalog layer {layer_name} CRS authority name",
                    )
                if layer.crs_authority_code is not None:
                    _exact_text(
                        layer.crs_authority_code,
                        f"catalog layer {layer_name} CRS authority code",
                    )
                _exact_text(layer.crs_wkt, f"catalog layer {layer_name} CRS WKT")
                expected_crs = _canonical_crs(
                    layer.crs_raw,
                    relative_path,
                    layer_name,
                )
                if expected_crs != (
                    layer.crs_raw,
                    layer.crs_authority_name,
                    layer.crs_authority_code,
                    layer.crs_wkt,
                ):
                    raise InpnProtectedAreasCatalogError(
                        "catalog CRS metadata is not canonical"
                    )
            elif any(
                value is not None
                for value in (
                    layer.geometry_type_raw,
                    layer.crs_raw,
                    layer.crs_authority_name,
                    layer.crs_authority_code,
                    layer.crs_wkt,
                )
            ):
                raise InpnProtectedAreasCatalogError(
                    "catalog non-spatial metadata is inconsistent"
                )
            if layer.total_bounds is not None and (
                type(layer.total_bounds) is not tuple
                or len(layer.total_bounds) != 4
                or any(type(member) is not float for member in layer.total_bounds)
            ):
                raise InpnProtectedAreasCatalogError(
                    "catalog bounds representation is not canonical"
                )
            bounds = _validated_bounds(
                layer.total_bounds,
                is_spatial=layer.is_spatial,
                feature_count=count,
                relative_path=relative_path,
                layer_name=layer_name,
            )
            if bounds != layer.total_bounds or (
                bounds is not None
                and any(type(member) is not float for member in bounds)
            ):
                raise InpnProtectedAreasCatalogError(
                    "catalog bounds representation is not canonical"
                )
            if type(layer.fields) is not tuple:
                raise InpnProtectedAreasCatalogError("catalog fields must be a tuple")
            field_names: list[str] = []
            for position, field in enumerate(layer.fields):
                if type(field) is not InpnProtectedAreasFieldCatalog:
                    raise InpnProtectedAreasCatalogError(
                        "catalog field type is invalid"
                    )
                field_names.append(_exact_text(field.name, "catalog field name"))
                _exact_text(field.source_dtype, "catalog source dtype")
                if type(field.position) is not int or field.position != position:
                    raise InpnProtectedAreasCatalogError(
                        "catalog field order is invalid"
                    )
            _require_unique_identities(tuple(field_names), "catalog field identities")
            field_count += len(layer.fields)
            feature_count += count
        _require_unique_identities(tuple(layer_names), "catalog layer identities")
        layer_count += len(package.layers)
    _require_unique_identities(tuple(package_names), "catalog package identities")
    if tuple(package_names) != tuple(sorted(package_names)):
        raise InpnProtectedAreasCatalogError("catalog package paths are not ordered")
    expected_counts = (
        len(catalog.packages),
        layer_count,
        field_count,
        feature_count,
    )
    actual_counts = (
        catalog.package_count,
        catalog.layer_count,
        catalog.field_count,
        catalog.total_feature_count,
    )
    if any(type(value) is not int or value < 0 for value in actual_counts) or (
        actual_counts != expected_counts
    ):
        raise InpnProtectedAreasCatalogError("catalog aggregate counts are invalid")
    if (
        type(catalog.complete_catalog_content_sha256) is not str
        or _SHA_PATTERN.fullmatch(catalog.complete_catalog_content_sha256) is None
        or _catalog_content_sha256(catalog) != catalog.complete_catalog_content_sha256
    ):
        raise InpnProtectedAreasCatalogError("catalog content SHA256 is invalid")
    return catalog


def _validate_source_locks(
    catalog: InpnProtectedAreasCatalog,
    extraction: InpnProtectedAreasExtraction,
) -> None:
    download = extraction.download
    expected = (
        download.provider,
        download.authority,
        download.program,
        download.dataset_id,
        download.dataset_name,
        download.declared_version,
        download.reference_page_url,
        download.archive_url,
        download.filename,
        download.file_size,
        download.sha256,
    )
    actual = (
        catalog.provider,
        catalog.authority,
        catalog.program,
        catalog.dataset_id,
        catalog.dataset_name,
        catalog.declared_version,
        catalog.reference_page_url,
        catalog.archive_url,
        catalog.archive_filename,
        catalog.archive_size,
        catalog.archive_sha256,
    )
    if actual != expected:
        raise InpnProtectedAreasCatalogError(
            "catalog source/archive lineage differs from the verified extraction"
        )


def build_inpn_protected_areas_catalog(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
) -> InpnProtectedAreasCatalog:
    """Build a portable metadata-only catalog from one verified EP extraction."""

    try:
        fresh_before = validate_inpn_protected_areas_extraction(extraction, config)
        catalog = _build_catalog(fresh_before)
        fresh_after = validate_inpn_protected_areas_extraction(fresh_before, config)
        if fresh_after != fresh_before:
            raise InpnProtectedAreasCatalogError(
                "extraction physical inventory changed during metadata inspection"
            )
        return _validate_catalog_intrinsic(catalog)
    except InpnProtectedAreasCatalogError:
        raise
    except InpnProtectedAreasSourceError as error:
        raise InpnProtectedAreasCatalogError(
            "INPN extraction byte identity changed or failed source-complete "
            "catalog validation"
        ) from error
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            "INPN protected-areas metadata catalog cannot be built safely"
        ) from error


def validate_inpn_protected_areas_catalog(
    extraction: InpnProtectedAreasExtraction,
    config: InpnProtectedAreasSourceConfig,
    catalog: InpnProtectedAreasCatalog,
) -> None:
    """Independently rebuild and exact-compare one supplied physical catalog."""

    try:
        validated = _validate_catalog_intrinsic(catalog)
        fresh_extraction = validate_inpn_protected_areas_extraction(
            extraction,
            config,
        )
        _validate_source_locks(validated, fresh_extraction)
        rebuilt = build_inpn_protected_areas_catalog(fresh_extraction, config)
        if validated != rebuilt:
            raise InpnProtectedAreasCatalogError(
                "catalog differs from the independently rebuilt physical metadata"
            )
    except InpnProtectedAreasCatalogError:
        raise
    except InpnProtectedAreasSourceError as error:
        raise InpnProtectedAreasCatalogError(
            "INPN extraction failed catalog source-lock validation"
        ) from error
    except Exception as error:
        raise InpnProtectedAreasCatalogError(
            "INPN protected-areas catalog validation failed safely"
        ) from error


__all__ = [
    "InpnProtectedAreasCatalog",
    "InpnProtectedAreasCatalogError",
    "InpnProtectedAreasFieldCatalog",
    "InpnProtectedAreasGeoPackageCatalog",
    "InpnProtectedAreasLayerCatalog",
    "build_inpn_protected_areas_catalog",
    "validate_inpn_protected_areas_catalog",
]
```
