# `tests/unit/test_cadastre_loader_fr.py`

## File identity

- Repository path: `tests/unit/test_cadastre_loader_fr.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `cadastre_loader_fr` contracts exercised in this file.
- Source SHA256: `e724a7ac10433602f93022270b72ad077cec1f8fc679b99eed6e954446f25959`

## 1. Purpose

Provides complete unit and regression coverage for the `cadastre_loader_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

- `from landscout.sources.cadastre_fr import CadastreDownload`
- `from landscout.sources.cadastre_loader_fr import (
    CadastreLoadError,
    EmptyCadastreDatasetError,
    MissingGeometryColumnError,
    UnsupportedGeometryTypeError,
    load_cadastre_parcels,
)`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_write_geojson`

**Exact signature**

```python
def _write_geojson(path: Path, features: list[dict]) -> None:
```

**Purpose**

Serializes geojson; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson` via `_write_geojson`.

**Complete source-ordered implementation**

```python
def _write_geojson(path: Path, features: list[dict]) -> None:
    content = {"type": "FeatureCollection", "features": features}
    path.write_text(json.dumps(content), encoding="utf-8")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_gzipped_geojson`

**Exact signature**

```python
def _write_gzipped_geojson(path: Path, features: list[dict]) -> None:
```

**Purpose**

Serializes gzipped geojson; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes` via `_write_gzipped_geojson`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails` via `_write_gzipped_geojson`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails` via `_write_gzipped_geojson`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing` via `_write_gzipped_geojson`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing` via `_write_gzipped_geojson`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_write_gzipped_geojson`.

**Complete source-ordered implementation**

```python
def _write_gzipped_geojson(path: Path, features: list[dict]) -> None:
    content = json.dumps({"type": "FeatureCollection", "features": features}).encode()
    path.write_bytes(gzip.compress(content))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_download`

**Exact signature**

```python
def _download(path: Path, **changes: object) -> CadastreDownload:
```

**Purpose**

Acquires, verifies, and records download; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CadastreDownload`.
- Every observed return expression is reproduced without truncation:
```python
CadastreDownload(**values)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `path.is_file`, `path.read_bytes`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(content).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: `values`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_missing_file_fails` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_invalid_file_fails` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_missing_geometry_column_fails` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing` via `_download`.
- direct call: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_download`.

**Complete source-ordered implementation**

```python
def _download(path: Path, **changes: object) -> CadastreDownload:
    content = path.read_bytes() if path.is_file() else b"missing"
    values: dict[str, object] = {
        "source_url": "https://cadastre.data.gouv.fr/test/parcels.json.gz",
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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_load_valid_geojson_preserves_attributes`

**Purpose**

Exercises `load valid geojson preserves attributes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "parcels.json.gz"
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
```

**Action**

```python
parcels = load_cadastre_parcels(_download(path))
```

**Expected result**

```python
assert len(parcels) == 2
assert list(parcels.columns) == ["id", "section", "numero", "geometry"]
assert set(parcels.geometry.geom_type) == {"Polygon", "MultiPolygon"}
assert parcels.crs is not None
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_load_valid_geojson_preserves_attributes(tmp_path: Path) -> None:
    path = tmp_path / "parcels.json.gz"
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

    parcels = load_cadastre_parcels(_download(path))

    assert len(parcels) == 2
    assert list(parcels.columns) == ["id", "section", "numero", "geometry"]
    assert set(parcels.geometry.geom_type) == {"Polygon", "MultiPolygon"}
    assert parcels.crs is not None
```

### `test_load_valid_gzipped_geojson`

**Purpose**

Exercises `load valid gzipped geojson`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
plain_path = tmp_path / "parcels.geojson"
gzip_path = tmp_path / "parcels.json.gz"
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
```

**Action**

```python
parcels = load_cadastre_parcels(_download(gzip_path))
```

**Expected result**

```python
assert len(parcels) == 1
assert parcels.iloc[0]["id"] == "parcel-1"
```

**Regression protected**

Locks `load valid gzipped geojson` through the exact asserted conditions: `len(parcels) == 1`; `parcels.iloc[0]['id'] == 'parcel-1'`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_load_valid_gzipped_geojson(tmp_path: Path) -> None:
    plain_path = tmp_path / "parcels.geojson"
    gzip_path = tmp_path / "parcels.json.gz"
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

    parcels = load_cadastre_parcels(_download(gzip_path))

    assert len(parcels) == 1
    assert parcels.iloc[0]["id"] == "parcel-1"
```

### `test_empty_dataset_fails`

**Purpose**

Exercises `empty dataset fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "empty.json.gz"
_write_gzipped_geojson(path, [])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(EmptyCadastreDatasetError):
        load_cadastre_parcels(_download(path))
```

**Regression protected**

Locks `empty dataset fails`: the reproduced adversarial input must raise `EmptyCadastreDatasetError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_empty_dataset_fails(tmp_path: Path) -> None:
    path = tmp_path / "empty.json.gz"
    _write_gzipped_geojson(path, [])

    with pytest.raises(EmptyCadastreDatasetError):
        load_cadastre_parcels(_download(path))
```

### `test_missing_file_fails`

**Purpose**

Exercises `missing file fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreLoadError, match="exist"):
        load_cadastre_parcels(_download(tmp_path / "missing.json.gz"))
```

**Regression protected**

Locks `missing file fails`: the reproduced adversarial input must raise `CadastreLoadError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_missing_file_fails(tmp_path: Path) -> None:
    with pytest.raises(CadastreLoadError, match="exist"):
        load_cadastre_parcels(_download(tmp_path / "missing.json.gz"))
```

### `test_invalid_file_fails`

**Purpose**

Exercises `invalid file fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "invalid.json.gz"
path.write_bytes(gzip.compress(b"not GeoJSON"))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreLoadError):
        load_cadastre_parcels(_download(path))
```

**Regression protected**

Locks `invalid file fails`: the reproduced adversarial input must raise `CadastreLoadError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_invalid_file_fails(tmp_path: Path) -> None:
    path = tmp_path / "invalid.json.gz"
    path.write_bytes(gzip.compress(b"not GeoJSON"))

    with pytest.raises(CadastreLoadError):
        load_cadastre_parcels(_download(path))
```

### `test_missing_geometry_column_fails`

**Purpose**

Exercises `missing geometry column fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "parcels.json.gz"
path.write_bytes(gzip.compress(b'{' + b' ' * 5 + b'}'))
frame_without_geometry = gpd.GeoDataFrame({"id": ["parcel-1"]})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            return_value=frame_without_geometry,
        ),
        pytest.raises(MissingGeometryColumnError),
    ):
        load_cadastre_parcels(_download(path))
```

**Regression protected**

Locks `missing geometry column fails`: the reproduced adversarial input must raise `MissingGeometryColumnError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_geometry_column_fails(tmp_path: Path) -> None:
    path = tmp_path / "parcels.json.gz"
    path.write_bytes(gzip.compress(b'{' + b' ' * 5 + b'}'))
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

### `test_unsupported_geometry_type_fails`

**Purpose**

Exercises `unsupported geometry type fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "points.json.gz"
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(UnsupportedGeometryTypeError, match="Point"):
        load_cadastre_parcels(_download(path))
```

**Regression protected**

Locks `unsupported geometry type fails`: the reproduced adversarial input must raise `UnsupportedGeometryTypeError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unsupported_geometry_type_fails(tmp_path: Path) -> None:
    path = tmp_path / "points.json.gz"
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

### `test_malformed_verified_download_is_rejected_before_parsing`

**Purpose**

Exercises `malformed verified download is rejected before parsing`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `changes`, `message`.

**Setup**

```python
path = tmp_path / "parcels.json.gz"
_write_gzipped_geojson(path, [])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match=message),
    ):
        load_cadastre_parcels(_download(path, **changes))
```

**Regression protected**

Locks `malformed verified download is rejected before parsing`: the reproduced adversarial input must raise `CadastreLoadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_verified_download_is_rejected_before_parsing(
    tmp_path: Path,
    changes: dict[str, object],
    message: str,
) -> None:
    path = tmp_path / "parcels.json.gz"
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

### `test_wrong_public_input_type_is_controlled`

**Purpose**

Exercises `wrong public input type is controlled`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(CadastreLoadError, match="CadastreDownload"):
        load_cadastre_parcels(Path("untrusted.json.gz"))
```

**Regression protected**

Locks `wrong public input type is controlled`: the reproduced adversarial input must raise `CadastreLoadError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_public_input_type_is_controlled() -> None:
    with pytest.raises(CadastreLoadError, match="CadastreDownload"):
        load_cadastre_parcels(Path("untrusted.json.gz"))
```

### `test_physical_mutation_after_download_is_rejected_before_parsing`

**Purpose**

Exercises `physical mutation after download is rejected before parsing`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "parcels.json.gz"
_write_gzipped_geojson(path, [])
download = _download(path)
content = bytearray(path.read_bytes())
content[-1] ^= 1
path.write_bytes(content)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=AssertionError("parser must not run"),
        ),
        pytest.raises(CadastreLoadError, match="SHA|checksum|gzip"),
    ):
        load_cadastre_parcels(download)
```

**Regression protected**

Locks `physical mutation after download is rejected before parsing`: the reproduced adversarial input must raise `CadastreLoadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_physical_mutation_after_download_is_rejected_before_parsing(
    tmp_path: Path,
) -> None:
    path = tmp_path / "parcels.json.gz"
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

### `test_physical_change_during_read_is_rejected_by_post_read_verification`

**Purpose**

Exercises `physical change during read is rejected by post read verification`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "parcels.json.gz"
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.cadastre_loader_fr.gpd.read_file",
            side_effect=mutate_after_read,
        ),
        pytest.raises(CadastreLoadError, match="changed|SHA|size"),
    ):
        load_cadastre_parcels(download)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_physical_change_during_read_is_rejected_by_post_read_verification(
    tmp_path: Path,
) -> None:
    path = tmp_path / "parcels.json.gz"
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

### `test_physical_change_during_read_is_rejected_by_post_read_verification.mutate_after_read`

**Exact signature**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for mutate after read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=mutate_after_read)`.

**Complete source-ordered implementation**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        path.write_bytes(gzip.compress(b'{"type":"FeatureCollection","features":[]}'))
        return frame
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.


## 7. Data contracts

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


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the test flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
