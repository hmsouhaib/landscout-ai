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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson` via `_write_geojson`.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes` via `_write_gzipped_geojson`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails` via `_write_gzipped_geojson`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails` via `_write_gzipped_geojson`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing` via `_write_gzipped_geojson`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing` via `_write_gzipped_geojson`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_write_gzipped_geojson`.

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

- Network I/O: `CadastreDownload`.
- Filesystem read: `path.read_bytes`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(content).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_geojson_preserves_attributes` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_load_valid_gzipped_geojson` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_empty_dataset_fails` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_missing_file_fails` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_invalid_file_fails` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_missing_geometry_column_fails` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_unsupported_geometry_type_fails` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_malformed_verified_download_is_rejected_before_parsing` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_physical_mutation_after_download_is_rejected_before_parsing` via `_download`.
- direct call or construction: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_successful_download_persists_sha_and_sidecar` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_fresh_cache_is_reused` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_expired_cache_is_refreshed` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_failed_refresh_preserves_previous_cache` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_metadata_publication_failure_rolls_back_both_cache_files` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_tampered_sidecar_invalidates_cache` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_extraction_inventory_and_cache` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_stale_download_object_rejects_replaced_valid_archive` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_extraction_rejects_archive_object_inconsistent_with_path` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_tampered_extraction_is_rebuilt_from_verified_archive` via `_download`.
- direct call or construction: `tests/unit/test_gpu_fr.py::test_cached_document_lineage_change_forces_refresh` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_coordinated_cache_and_metadata_snapshot_change_is_not_a_cache_hit` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_physical_and_metadata_cache_is_reused` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_download_cache_is_a_miss` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_successful_first_and_replacement_publication` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_publication_failure_restores_old_pair` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_rollback_failure_preserves_recovery_material` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_failed_replacement_restores_a_still_reusable_valid_download_pair` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_validates_complete_inventory_before_copying` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_normal_nested_members_are_accepted` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_inventory_is_complete_ordered_and_hashed` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_valid_extraction_cache_is_reused` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_invalid_extraction_cache_is_rebuilt` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_first_extraction_publication_failure_leaves_no_half_root` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_replacement_failure_restores_old_tree` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rollback_failure_preserves_backup` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_backup_move_failure_leaves_old_tree_untouched` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_wrong_config_type` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_cache_setup_failure_is_controlled` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_extraction_rejects_stale_download_bytes` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_result_dataclasses_are_frozen` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_strict_metadata_rejects_boolean_numeric_values_as_cache_hits` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_cache_path_binds_version_and_filename` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_exact_file_inventory_does_not_omit_unknown_suffixes` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_archive_and_extraction_cache_reuse_are_independent` via `_download`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::test_no_stale_parts_after_download_or_extraction_success` via `_download`.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

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

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_cadastre_loader_fr.py::test_physical_change_during_read_is_rejected_by_post_read_verification` via `patch('landscout.sources.cadastre_loader_fr.gpd.read_file', side_effect=mutate_after_read)`.
- callback/function object: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_source_change_after_physical_read` via `patch.object(ign_bdtopo_fr.gpd, 'read_file', side_effect=mutate_after_read)`.

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
