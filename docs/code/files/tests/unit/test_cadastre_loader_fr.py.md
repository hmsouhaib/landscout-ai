# `tests/unit/test_cadastre_loader_fr.py`

## File identity

- Repository path: `tests/unit/test_cadastre_loader_fr.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Exercises source-package exports, real temporary gzip/GeoJSON byte-bound loading and pre/post-read mutation rejection, supplemented by explicitly mocked reader-envelope geometry guards and ten malformed download-envelope controls; no network acquisition or real Cadastre cache is used.
- Source SHA256: `11133b8fec1b86b6fef37300aa005c152cbdc577b02b2354041f57fdd7f3df18`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for cadastre loader fr; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Exercises source-package exports, real temporary gzip/GeoJSON byte-bound loading and pre/post-read mutation rejection, supplemented by explicitly mocked reader-envelope geometry guards and ten malformed download-envelope controls; no network acquisition or real Cadastre cache is used.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import gzip`
- `import json`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import pytest`

### Internal LandScout imports

- `import landscout.sources.cadastre_loader_fr as cadastre_loader`
- `from landscout import sources`
- `from landscout.sources.cadastre_fr import CadastreDownload`
- `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `COMMUNE_CODE`

- Category: module constant or closed domain.
- Exact declaration:

```python
COMMUNE_CODE = "31395"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OFFICIAL_FILENAME`

- Category: module constant or closed domain.
- Exact declaration:

```python
OFFICIAL_FILENAME = f"cadastre-{COMMUNE_CODE}-parcelles.json.gz"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OFFICIAL_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
OFFICIAL_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"
    f"31/{COMMUNE_CODE}/{OFFICIAL_FILENAME}"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `test_public_sources_export_the_source_bound_cadastre_api`

**Purpose:** Regression invariant: public sources export the source bound cadastre api. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_sources_export_the_source_bound_cadastre_api() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert sources.CadastreParcelSource is CadastreParcelSource`
  - `assert sources.load_cadastre_parcels is load_cadastre_parcels`
  - `assert (<br>        sources.revalidate_cadastre_parcel_source is revalidate_cadastre_parcel_source<br>    )`
  - `assert set(cadastre_loader.__all__) == expected`
  - `assert expected <= set(sources.__all__)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_sources_export_the_source_bound_cadastre_api() -> None:
    expected = {
        "CadastreLoadError",
        "CadastreParcelSource",
        "EmptyCadastreDatasetError",
        "MissingGeometryColumnError",
        "UnsupportedGeometryTypeError",
        "load_cadastre_parcels",
        "revalidate_cadastre_parcel_source",
    }
    assert sources.CadastreParcelSource is CadastreParcelSource
    assert sources.load_cadastre_parcels is load_cadastre_parcels
    assert (
        sources.revalidate_cadastre_parcel_source is revalidate_cadastre_parcel_source
    )
    assert set(cadastre_loader.__all__) == expected
    assert expected <= set(sources.__all__)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_geojson`

**Purpose:** Write an uncompressed UTF-8 FeatureCollection fixture at the supplied temporary path.

**Exact signature**

```python
def _write_geojson(path: Path, features: list[dict]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `features` | positional-or-keyword | `list[dict]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_cadastre_loader_fr::test_load_valid_gzipped_geojson` via `_write_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_load_valid_gzipped_geojson` via `_write_geojson`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_geojson(path: Path, features: list[dict]) -> None:
    content = {"type": "FeatureCollection", "features": features}
    path.write_text(json.dumps(content), encoding="utf-8")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_gzipped_geojson`

**Purpose:** Serialize a FeatureCollection to UTF-8 bytes, compress in memory and write gzip bytes to the temporary path. gzip.compress performs no filesystem read.

**Exact signature**

```python
def _write_gzipped_geojson(path: Path, features: list[dict]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `features` | positional-or-keyword | `list[dict]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_cadastre_loader_fr::test_load_valid_geojson_preserves_attributes` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_load_valid_geojson_preserves_attributes` via `_write_gzipped_geojson`
- direct call: `tests.unit.test_cadastre_loader_fr::test_empty_dataset_fails` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_empty_dataset_fails` via `_write_gzipped_geojson`
- direct call: `tests.unit.test_cadastre_loader_fr::test_unsupported_geometry_type_fails` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_unsupported_geometry_type_fails` via `_write_gzipped_geojson`
- direct call: `tests.unit.test_cadastre_loader_fr::test_three_dimensional_cadastre_geometry_is_rejected` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_three_dimensional_cadastre_geometry_is_rejected` via `_write_gzipped_geojson`
- direct call: `tests.unit.test_cadastre_loader_fr::test_malformed_verified_download_is_rejected_before_parsing` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_malformed_verified_download_is_rejected_before_parsing` via `_write_gzipped_geojson`
- direct call: `tests.unit.test_cadastre_loader_fr::test_physical_mutation_after_download_is_rejected_before_parsing` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_mutation_after_download_is_rejected_before_parsing` via `_write_gzipped_geojson`
- direct call: `tests.unit.test_cadastre_loader_fr::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_write_gzipped_geojson`
- direct call: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `_write_gzipped_geojson`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `_write_gzipped_geojson`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps({"type": "FeatureCollection", "features": features}).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `gzip.compress` | `gzip.compress` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present; gzip.compress operates on in-memory bytes. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_gzipped_geojson(path: Path, features: list[dict]) -> None:
    content = json.dumps({"type": "FeatureCollection", "features": features}).encode()
    path.write_bytes(gzip.compress(content))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_download`

**Purpose:** Construct a synthetic download envelope using the temporary file's actual size/SHA256 or the fallback bytes missing when no file exists, official-shaped commune URL, fixed timestamp, and arbitrary test overrides. It does not execute a download.

**Exact signature**

```python
def _download(path: Path, **changes: object) -> CadastreDownload:
```

- Exact decorators: none.
- Declared return annotation: `CadastreDownload`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `**changes` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `CadastreDownload(**values)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_cadastre_loader_fr::test_load_valid_geojson_preserves_attributes` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_load_valid_geojson_preserves_attributes` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_load_valid_gzipped_geojson` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_load_valid_gzipped_geojson` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_empty_dataset_fails` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_empty_dataset_fails` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_missing_file_fails` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_missing_file_fails` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_invalid_file_fails` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_invalid_file_fails` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_missing_geometry_column_fails` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_missing_geometry_column_fails` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_noncanonical_active_geometry_name_fails_with_controlled_error` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_noncanonical_active_geometry_name_fails_with_controlled_error` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_unsupported_geometry_type_fails` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_unsupported_geometry_type_fails` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_three_dimensional_cadastre_geometry_is_rejected` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_three_dimensional_cadastre_geometry_is_rejected` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_malformed_verified_download_is_rejected_before_parsing` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_malformed_verified_download_is_rejected_before_parsing` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_physical_mutation_after_download_is_rejected_before_parsing` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_mutation_after_download_is_rejected_before_parsing` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_download`
- direct call: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `_download`
- value/type reference: `tests.unit.test_cadastre_loader_fr::test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` via `_download`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.is_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(content).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `values.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `CadastreDownload` | `landscout.sources.cadastre_fr.CadastreDownload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.is_file`<br>`path.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(content).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `values.update(changes)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _download(path: Path, **changes: object) -> CadastreDownload:
    content = path.read_bytes() if path.is_file() else b"missing"
    values: dict[str, object] = {
        "commune_code": COMMUNE_CODE,
        "source_url": OFFICIAL_URL,
        "download_timestamp": "2026-08-16T10:00:00+00:00",
        "filename": path.name,
        "file_size": len(content),
        "sha256": sha256(content).hexdigest(),
        "path": path,
        "cache_hit": True,
    }
    values.update(changes)
    return CadastreDownload(**values)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_load_valid_geojson_preserves_attributes`

**Purpose:** Actually read a temporary gzipped Polygon/MultiPolygon FeatureCollection; assert exact source-envelope type, two rows, ordered id/section/numero/geometry columns, both geometry types and present CRS. Not every attribute value is asserted.

**Exact signature**

```python
def test_load_valid_geojson_preserves_attributes(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert type(source) is CadastreParcelSource`
  - `assert len(parcels) == 2`
  - `assert list(parcels.columns) == ["id", "section", "numero", "geometry"]`
  - `assert set(parcels.geometry.geom_type) == {"Polygon", "MultiPolygon"}`
  - `assert parcels.crs is not None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_load_valid_geojson_preserves_attributes(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1", "section": "AB", "numero": "42"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            },
            {
                "type": "Feature",
                "properties": {"id": "parcel-2", "section": "AC", "numero": "7"},
                "geometry": {
                    "type": "MultiPolygon",
                    "coordinates": [[[[3, 43], [4, 43], [4, 44], [3, 43]]]],
                },
            },
        ],
    )

    source = load_cadastre_parcels(_download(path))
    assert type(source) is CadastreParcelSource
    parcels = source.parcels

    assert len(parcels) == 2
    assert list(parcels.columns) == ["id", "section", "numero", "geometry"]
    assert set(parcels.geometry.geom_type) == {"Polygon", "MultiPolygon"}
    assert parcels.crs is not None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_load_valid_gzipped_geojson`

**Purpose:** Write plain GeoJSON, gzip its actual bytes, run the public byte-verifying loader and assert one row with parcel-1 ID.

**Exact signature**

```python
def test_load_valid_gzipped_geojson(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(parcels) == 1`
  - `assert parcels.iloc[0]["id"] == "parcel-1"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_geojson` | `tests.unit.test_cadastre_loader_fr._write_geojson` |
| `gzip_path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `gzip.compress` | `gzip.compress` |
| `plain_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `plain_path.read_bytes`; compression itself is in memory. |
| Filesystem/archive write or publication | `gzip_path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_load_valid_gzipped_geojson(tmp_path: Path) -> None:
    plain_path = tmp_path / "parcels.geojson"
    gzip_path = tmp_path / OFFICIAL_FILENAME
    _write_geojson(
        plain_path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    gzip_path.write_bytes(gzip.compress(plain_path.read_bytes()))

    parcels = load_cadastre_parcels(_download(gzip_path)).parcels

    assert len(parcels) == 1
    assert parcels.iloc[0]["id"] == "parcel-1"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_empty_dataset_fails`

**Purpose:** Write a valid gzipped empty FeatureCollection and require EmptyCadastreDatasetError.

**Exact signature**

```python
def test_empty_dataset_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(EmptyCadastreDatasetError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |

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
def test_empty_dataset_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])

    with pytest.raises(EmptyCadastreDatasetError):
        load_cadastre_parcels(_download(path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_file_fails`

**Purpose:** Supply a synthetic envelope for an absent file and require a controlled existence error.

**Exact signature**

```python
def test_missing_file_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreLoadError, match="exist")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |

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
def test_missing_file_fails(tmp_path: Path) -> None:
    with pytest.raises(CadastreLoadError, match="exist"):
        load_cadastre_parcels(_download(tmp_path / OFFICIAL_FILENAME))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_file_fails`

**Purpose:** Write valid gzip wrapping invalid GeoJSON text and require CadastreLoadError from the public loader.

**Exact signature**

```python
def test_invalid_file_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreLoadError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `gzip.compress` | `gzip.compress` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present; gzip.compress operates on in-memory bytes. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_file_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"not GeoJSON"))

    with pytest.raises(CadastreLoadError):
        load_cadastre_parcels(_download(path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_geometry_column_fails`

**Purpose:** Keep a real gzip fixture but mock gpd.read_file to return a frame without geometry; require MissingGeometryColumnError. This targets the returned-frame contract, not native parser behavior.

**Exact signature**

```python
def test_missing_geometry_column_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(MissingGeometryColumnError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `gzip.compress` | `gzip.compress` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present; gzip.compress operates on in-memory bytes. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_geometry_column_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"{" + b" " * 5 + b"}"))
    frame_without_geometry = gpd.GeoDataFrame({"id": ["parcel-1"]})

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame_without_geometry,
        ),
        pytest.raises(MissingGeometryColumnError),
    ):
        load_cadastre_parcels(_download(path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_noncanonical_active_geometry_name_fails_with_controlled_error`

**Purpose:** Mock the reader to return points under a noncanonical active geometry name and require the canonical-geometry-name guard before geometry-type interpretation.

**Exact signature**

```python
def test_noncanonical_active_geometry_name_fails_with_controlled_error(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(MissingGeometryColumnError, match="canonical geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `gzip.compress` | `gzip.compress` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `gpd.points_from_xy` | `geopandas.points_from_xy` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present; gzip.compress operates on in-memory bytes. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_noncanonical_active_geometry_name_fails_with_controlled_error(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"{}"))
    frame = gpd.GeoDataFrame(
        {"id": ["parcel-1"], "shape": [gpd.points_from_xy([1], [43])[0]]},
        geometry="shape",
        crs="EPSG:4326",
    )

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame,
        ),
        pytest.raises(MissingGeometryColumnError, match="canonical geometry"),
    ):
        load_cadastre_parcels(_download(path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsupported_geometry_type_fails`

**Purpose:** Read a real gzipped Point feature and require UnsupportedGeometryTypeError mentioning Point.

**Exact signature**

```python
def test_unsupported_geometry_type_fails(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(UnsupportedGeometryTypeError, match="Point")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |

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
def test_unsupported_geometry_type_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "point-1"},
                "geometry": {"type": "Point", "coordinates": [1, 43]},
            }
        ],
    )

    with pytest.raises(UnsupportedGeometryTypeError, match="Point"):
        load_cadastre_parcels(_download(path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_three_dimensional_cadastre_geometry_is_rejected`

**Purpose:** Read real XYZ Polygon and MultiPolygon fixtures and require the 2D error; these two cases do not exercise XYM.

**Exact signature**

```python
def test_three_dimensional_cadastre_geometry_is_rejected(
    tmp_path: Path,
    geometry: dict[str, object],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        {
            "type": "Polygon",
            "coordinates": [[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]],
        },
        {
            "type": "MultiPolygon",
            "coordinates": [[[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]]],
        },
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `geometry` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(UnsupportedGeometryTypeError, match="2D")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_three_dimensional_cadastre_geometry_is_rejected(
    tmp_path: Path,
    geometry: dict[str, object],
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [{"type": "Feature", "properties": {"id": "parcel"}, "geometry": geometry}],
    )

    with pytest.raises(UnsupportedGeometryTypeError, match="2D"):
        load_cadastre_parcels(_download(path))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_verified_download_is_rejected_before_parsing`

**Purpose:** Cross ten wrong hash/size/filename/URL/commune envelope mutations with a parser sentinel that would raise AssertionError if called; require the corresponding controlled pre-parser error.

**Exact signature**

```python
def test_malformed_verified_download_is_rejected_before_parsing(
    tmp_path: Path,
    changes: dict[str, object],
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"sha256": "0" * 64}, "SHA|checksum"),
        ({"sha256": "A" * 64}, "SHA"),
        ({"sha256": "a" * 63}, "SHA"),
        ({"file_size": True}, "size"),
        ({"file_size": 0}, "size"),
        ({"filename": "other.json.gz"}, "filename"),
        ({"source_url": ""}, "URL"),
        ({"source_url": OFFICIAL_URL.replace("https://", "http://")}, "URL"),
        (
            {"source_url": OFFICIAL_URL.replace("cadastre.data.gouv.fr", "evil.test")},
            "URL",
        ),
        ({"commune_code": "31446"}, "URL|commune"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `changes` | positional-or-keyword | `dict[str, object]` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreLoadError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `patch` | `unittest.mock.patch` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `OFFICIAL_URL.replace` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present; OFFICIAL_URL.replace constructs text only. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_verified_download_is_rejected_before_parsing(
    tmp_path: Path,
    changes: dict[str, object],
    message: str,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match=message),
    ):
        load_cadastre_parcels(_download(path, **changes))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_public_input_type_is_controlled`

**Purpose:** Pass a Path instead of CadastreDownload and require the public input-type error.

**Exact signature**

```python
def test_wrong_public_input_type_is_controlled() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreLoadError, match="CadastreDownload")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `Path` | `pathlib.Path` |

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
def test_wrong_public_input_type_is_controlled() -> None:
    with pytest.raises(CadastreLoadError, match="CadastreDownload"):
        load_cadastre_parcels(Path("untrusted.json.gz"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_mutation_after_download_is_rejected_before_parsing`

**Purpose:** After constructing correct size/SHA metadata, flip the final physical gzip byte; protect the parser with an AssertionError sentinel and require SHA/checksum/gzip rejection before parsing.

**Exact signature**

```python
def test_physical_mutation_after_download_is_rejected_before_parsing(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreLoadError, match="SHA\|checksum\|gzip")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |
| `bytearray` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes` |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `content[-1] ^= 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_physical_mutation_after_download_is_rejected_before_parsing(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])
    download = _download(path)
    content = bytearray(path.read_bytes())
    content[-1] ^= 1
    path.write_bytes(content)

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match="SHA|checksum|gzip"),
    ):
        load_cadastre_parcels(download)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_change_during_read_is_rejected_by_post_read_verification`

**Purpose:** Wrap the real GeoPandas read with a callback that changes archive bytes after it returns; require changed/SHA/size rejection from the loader postcondition.

**Exact signature**

```python
def test_physical_change_during_read_is_rejected_by_post_read_verification(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreLoadError, match="changed\|SHA\|size")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |

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
def test_physical_change_during_read_is_rejected_by_post_read_verification(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    download = _download(path)
    original_read = gpd.read_file

    def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        path.write_bytes(gzip.compress(b'{"type":"FeatureCollection","features":[]}'))
        return frame

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=mutate_after_read,
        ),
        pytest.raises(CadastreLoadError, match="changed|SHA|size"),
    ):
        load_cadastre_parcels(download)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_change_during_read_is_rejected_by_post_read_verification.mutate_after_read`

**Purpose:** Call the captured real GeoPandas reader, overwrite the closed-over archive path with different compressed bytes, then return the previously read frame.

**Exact signature**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_read` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `gzip.compress` | `gzip.compress` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read` invokes the captured real GeoPandas file reader; gzip.compress itself is in memory. |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        path.write_bytes(gzip.compress(b'{"type":"FeatureCollection","features":[]}'))
        return frame
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread`

**Purpose:** Load a real temporary archive, mutate the retained frame's id to FORGED, and require fresh-reread mismatch on source revalidation.

**Exact signature**

```python
def test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(CadastreLoadError, match="freshly read")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_write_gzipped_geojson` | `tests.unit.test_cadastre_loader_fr._write_gzipped_geojson` |
| `load_cadastre_parcels` | `landscout.sources.cadastre_loader_fr.load_cadastre_parcels` |
| `_download` | `tests.unit.test_cadastre_loader_fr._download` |
| `pytest.raises` | `pytest.raises` |
| `revalidate_cadastre_parcel_source` | `landscout.sources.cadastre_loader_fr.revalidate_cadastre_parcel_source` |

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
| In-memory mutation | `source.parcels.loc[0, "id"] = "FORGED"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "313950000A0001"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    source = load_cadastre_parcels(_download(path))
    source.parcels.loc[0, "id"] = "FORGED"

    with pytest.raises(CadastreLoadError, match="freshly read"):
        revalidate_cadastre_parcel_source(source)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

Exercises source-package exports, real temporary gzip/GeoJSON byte-bound loading and pre/post-read mutation rejection, supplemented by explicitly mocked reader-envelope geometry guards and ten malformed download-envelope controls; no network acquisition or real Cadastre cache is used.

The 15 test definitions expand statically to 25 cases; no test run is claimed by this audit. gzip.compress is an in-memory codec, string replace is non-I/O, and temporary file access through fixture helpers/public loaders is delegated I/O.

- Test functions: **15**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_public_sources_export_the_source_bound_cadastre_api` | none | none | 5 | Assert class/loader/revalidator object identity across source package exports, the loader module's exact seven-name __all__, and inclusion of those names in source-package __all__. |
| `test_load_valid_geojson_preserves_attributes` | none | none | 5 | Actually read a temporary gzipped Polygon/MultiPolygon FeatureCollection; assert exact source-envelope type, two rows, ordered id/section/numero/geometry columns, both geometry types and present CRS. Not every attribute value is asserted. |
| `test_load_valid_gzipped_geojson` | none | none | 2 | Write plain GeoJSON, gzip its actual bytes, run the public byte-verifying loader and assert one row with parcel-1 ID. |
| `test_empty_dataset_fails` | none | pytest.raises(EmptyCadastreDatasetError) | 0 | Write a valid gzipped empty FeatureCollection and require EmptyCadastreDatasetError. |
| `test_missing_file_fails` | none | pytest.raises(CadastreLoadError, match="exist") | 0 | Supply a synthetic envelope for an absent file and require a controlled existence error. |
| `test_invalid_file_fails` | none | pytest.raises(CadastreLoadError) | 0 | Write valid gzip wrapping invalid GeoJSON text and require CadastreLoadError from the public loader. |
| `test_missing_geometry_column_fails` | none | pytest.raises(MissingGeometryColumnError) | 0 | Keep a real gzip fixture but mock gpd.read_file to return a frame without geometry; require MissingGeometryColumnError. This targets the returned-frame contract, not native parser behavior. |
| `test_noncanonical_active_geometry_name_fails_with_controlled_error` | none | pytest.raises(MissingGeometryColumnError, match="canonical geometry") | 0 | Mock the reader to return points under a noncanonical active geometry name and require the canonical-geometry-name guard before geometry-type interpretation. |
| `test_unsupported_geometry_type_fails` | none | pytest.raises(UnsupportedGeometryTypeError, match="Point") | 0 | Read a real gzipped Point feature and require UnsupportedGeometryTypeError mentioning Point. |
| `test_three_dimensional_cadastre_geometry_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        {<br>            "type": "Polygon",<br>            "coordinates": [[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]],<br>        },<br>        {<br>            "type": "MultiPolygon",<br>            "coordinates": [[[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]]],<br>        },<br>    ],<br>) | pytest.raises(UnsupportedGeometryTypeError, match="2D") | 0 | Read real XYZ Polygon and MultiPolygon fixtures and require the 2D error; these two cases do not exercise XYM. |
| `test_malformed_verified_download_is_rejected_before_parsing` | pytest.mark.parametrize(<br>    ("changes", "message"),<br>    [<br>        ({"sha256": "0" * 64}, "SHA\|checksum"),<br>        ({"sha256": "A" * 64}, "SHA"),<br>        ({"sha256": "a" * 63}, "SHA"),<br>        ({"file_size": True}, "size"),<br>        ({"file_size": 0}, "size"),<br>        ({"filename": "other.json.gz"}, "filename"),<br>        ({"source_url": ""}, "URL"),<br>        ({"source_url": OFFICIAL_URL.replace("https://", "http://")}, "URL"),<br>        (<br>            {"source_url": OFFICIAL_URL.replace("cadastre.data.gouv.fr", "evil.test")},<br>            "URL",<br>        ),<br>        ({"commune_code": "31446"}, "URL\|commune"),<br>    ],<br>) | pytest.raises(CadastreLoadError, match=message) | 0 | Cross ten wrong hash/size/filename/URL/commune envelope mutations with a parser sentinel that would raise AssertionError if called; require the corresponding controlled pre-parser error. |
| `test_wrong_public_input_type_is_controlled` | none | pytest.raises(CadastreLoadError, match="CadastreDownload") | 0 | Pass a Path instead of CadastreDownload and require the public input-type error. |
| `test_physical_mutation_after_download_is_rejected_before_parsing` | none | pytest.raises(CadastreLoadError, match="SHA\|checksum\|gzip") | 0 | After constructing correct size/SHA metadata, flip the final physical gzip byte; protect the parser with an AssertionError sentinel and require SHA/checksum/gzip rejection before parsing. |
| `test_physical_change_during_read_is_rejected_by_post_read_verification` | none | pytest.raises(CadastreLoadError, match="changed\|SHA\|size") | 0 | Wrap the real GeoPandas read with a callback that changes archive bytes after it returns; require changed/SHA/size rejection from the loader postcondition. |
| `test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread` | none | pytest.raises(CadastreLoadError, match="freshly read") | 0 | Load a real temporary archive, mutate the retained frame's id to FORGED, and require fresh-reread mismatch on source revalidation. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
import gzip
import json
from hashlib import sha256
from pathlib import Path
from unittest.mock import patch

import geopandas as gpd
import pytest

import landscout.sources.cadastre_loader_fr as cadastre_loader
from landscout import sources
from landscout.sources.cadastre_fr import CadastreDownload
from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    CadastreParcelSource,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
    revalidate_cadastre_parcel_source,
)

COMMUNE_CODE = "31395"
OFFICIAL_FILENAME = f"cadastre-{COMMUNE_CODE}-parcelles.json.gz"
OFFICIAL_URL = (
    "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"
    f"31/{COMMUNE_CODE}/{OFFICIAL_FILENAME}"
)


def test_public_sources_export_the_source_bound_cadastre_api() -> None:
    expected = {
        "CadastreLoadError",
        "CadastreParcelSource",
        "EmptyCadastreDatasetError",
        "MissingGeometryColumnError",
        "UnsupportedGeometryTypeError",
        "load_cadastre_parcels",
        "revalidate_cadastre_parcel_source",
    }
    assert sources.CadastreParcelSource is CadastreParcelSource
    assert sources.load_cadastre_parcels is load_cadastre_parcels
    assert (
        sources.revalidate_cadastre_parcel_source is revalidate_cadastre_parcel_source
    )
    assert set(cadastre_loader.__all__) == expected
    assert expected <= set(sources.__all__)


def _write_geojson(path: Path, features: list[dict]) -> None:
    content = {"type": "FeatureCollection", "features": features}
    path.write_text(json.dumps(content), encoding="utf-8")


def _write_gzipped_geojson(path: Path, features: list[dict]) -> None:
    content = json.dumps({"type": "FeatureCollection", "features": features}).encode()
    path.write_bytes(gzip.compress(content))


def _download(path: Path, **changes: object) -> CadastreDownload:
    content = path.read_bytes() if path.is_file() else b"missing"
    values: dict[str, object] = {
        "commune_code": COMMUNE_CODE,
        "source_url": OFFICIAL_URL,
        "download_timestamp": "2026-08-16T10:00:00+00:00",
        "filename": path.name,
        "file_size": len(content),
        "sha256": sha256(content).hexdigest(),
        "path": path,
        "cache_hit": True,
    }
    values.update(changes)
    return CadastreDownload(**values)  # type: ignore[arg-type]


def test_load_valid_geojson_preserves_attributes(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1", "section": "AB", "numero": "42"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            },
            {
                "type": "Feature",
                "properties": {"id": "parcel-2", "section": "AC", "numero": "7"},
                "geometry": {
                    "type": "MultiPolygon",
                    "coordinates": [[[[3, 43], [4, 43], [4, 44], [3, 43]]]],
                },
            },
        ],
    )

    source = load_cadastre_parcels(_download(path))
    assert type(source) is CadastreParcelSource
    parcels = source.parcels

    assert len(parcels) == 2
    assert list(parcels.columns) == ["id", "section", "numero", "geometry"]
    assert set(parcels.geometry.geom_type) == {"Polygon", "MultiPolygon"}
    assert parcels.crs is not None


def test_load_valid_gzipped_geojson(tmp_path: Path) -> None:
    plain_path = tmp_path / "parcels.geojson"
    gzip_path = tmp_path / OFFICIAL_FILENAME
    _write_geojson(
        plain_path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    gzip_path.write_bytes(gzip.compress(plain_path.read_bytes()))

    parcels = load_cadastre_parcels(_download(gzip_path)).parcels

    assert len(parcels) == 1
    assert parcels.iloc[0]["id"] == "parcel-1"


def test_empty_dataset_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])

    with pytest.raises(EmptyCadastreDatasetError):
        load_cadastre_parcels(_download(path))


def test_missing_file_fails(tmp_path: Path) -> None:
    with pytest.raises(CadastreLoadError, match="exist"):
        load_cadastre_parcels(_download(tmp_path / OFFICIAL_FILENAME))


def test_invalid_file_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"not GeoJSON"))

    with pytest.raises(CadastreLoadError):
        load_cadastre_parcels(_download(path))


def test_missing_geometry_column_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"{" + b" " * 5 + b"}"))
    frame_without_geometry = gpd.GeoDataFrame({"id": ["parcel-1"]})

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame_without_geometry,
        ),
        pytest.raises(MissingGeometryColumnError),
    ):
        load_cadastre_parcels(_download(path))


def test_noncanonical_active_geometry_name_fails_with_controlled_error(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    path.write_bytes(gzip.compress(b"{}"))
    frame = gpd.GeoDataFrame(
        {"id": ["parcel-1"], "shape": [gpd.points_from_xy([1], [43])[0]]},
        geometry="shape",
        crs="EPSG:4326",
    )

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame,
        ),
        pytest.raises(MissingGeometryColumnError, match="canonical geometry"),
    ):
        load_cadastre_parcels(_download(path))


def test_unsupported_geometry_type_fails(tmp_path: Path) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "point-1"},
                "geometry": {"type": "Point", "coordinates": [1, 43]},
            }
        ],
    )

    with pytest.raises(UnsupportedGeometryTypeError, match="Point"):
        load_cadastre_parcels(_download(path))


@pytest.mark.parametrize(
    "geometry",
    [
        {
            "type": "Polygon",
            "coordinates": [[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]],
        },
        {
            "type": "MultiPolygon",
            "coordinates": [[[[1, 43, 1], [2, 43, 1], [2, 44, 1], [1, 43, 1]]]],
        },
    ],
)
def test_three_dimensional_cadastre_geometry_is_rejected(
    tmp_path: Path,
    geometry: dict[str, object],
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [{"type": "Feature", "properties": {"id": "parcel"}, "geometry": geometry}],
    )

    with pytest.raises(UnsupportedGeometryTypeError, match="2D"):
        load_cadastre_parcels(_download(path))


@pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"sha256": "0" * 64}, "SHA|checksum"),
        ({"sha256": "A" * 64}, "SHA"),
        ({"sha256": "a" * 63}, "SHA"),
        ({"file_size": True}, "size"),
        ({"file_size": 0}, "size"),
        ({"filename": "other.json.gz"}, "filename"),
        ({"source_url": ""}, "URL"),
        ({"source_url": OFFICIAL_URL.replace("https://", "http://")}, "URL"),
        (
            {"source_url": OFFICIAL_URL.replace("cadastre.data.gouv.fr", "evil.test")},
            "URL",
        ),
        ({"commune_code": "31446"}, "URL|commune"),
    ],
)
def test_malformed_verified_download_is_rejected_before_parsing(
    tmp_path: Path,
    changes: dict[str, object],
    message: str,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match=message),
    ):
        load_cadastre_parcels(_download(path, **changes))


def test_wrong_public_input_type_is_controlled() -> None:
    with pytest.raises(CadastreLoadError, match="CadastreDownload"):
        load_cadastre_parcels(Path("untrusted.json.gz"))  # type: ignore[arg-type]


def test_physical_mutation_after_download_is_rejected_before_parsing(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(path, [])
    download = _download(path)
    content = bytearray(path.read_bytes())
    content[-1] ^= 1
    path.write_bytes(content)

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match="SHA|checksum|gzip"),
    ):
        load_cadastre_parcels(download)


def test_physical_change_during_read_is_rejected_by_post_read_verification(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "parcel-1"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    download = _download(path)
    original_read = gpd.read_file

    def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        path.write_bytes(gzip.compress(b'{"type":"FeatureCollection","features":[]}'))
        return frame

    with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=mutate_after_read,
        ),
        pytest.raises(CadastreLoadError, match="changed|SHA|size"),
    ):
        load_cadastre_parcels(download)


def test_supplied_cadastre_frame_mutation_is_rejected_by_fresh_reread(
    tmp_path: Path,
) -> None:
    path = tmp_path / OFFICIAL_FILENAME
    _write_gzipped_geojson(
        path,
        [
            {
                "type": "Feature",
                "properties": {"id": "313950000A0001"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[1, 43], [2, 43], [2, 44], [1, 43]]],
                },
            }
        ],
    )
    source = load_cadastre_parcels(_download(path))
    source.parcels.loc[0, "id"] = "FORGED"

    with pytest.raises(CadastreLoadError, match="freshly read"):
        revalidate_cadastre_parcel_source(source)
```
