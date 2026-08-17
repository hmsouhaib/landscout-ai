# `tests/unit/test_ign_bdtopo_fr.py`

## File identity

- Repository path: `tests/unit/test_ign_bdtopo_fr.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `ign_bdtopo_fr` contracts exercised in this file.
- Source SHA256: `66176bddf663845755562d64498f79e295a814b911aaed7ae1f0872e4459a9f6`

## 1. Purpose

Provides complete unit and regression coverage for the `ign_bdtopo_fr` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `import io`
- `import json`
- `from datetime import UTC, datetime, timedelta`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from unittest.mock import patch`
- `from urllib.error import HTTPError`

### Third-party packages

- `import geopandas as gpd`
- `import py7zr`
- `import pyogrio`
- `import pytest`
- `import yaml`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pydantic import ValidationError`
- `from shapely.geometry import LineString, MultiLineString, MultiPolygon, Polygon`

### Internal LandScout imports

- `from landscout import sources`
- `from landscout.sources import ign_bdtopo_fr`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoArchiveError,
    IgnBdTopoDownload,
    IgnBdTopoDownloadError,
    IgnBdTopoExtraction,
    IgnBdTopoLayerError,
    IgnBdTopoSourceConfig,
    discover_ign_bdtopo_geopackage,
    discover_ign_bdtopo_layers,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
    list_ign_bdtopo_layers,
    load_ign_bdtopo_department_coverage,
    load_ign_bdtopo_electricity,
    load_ign_bdtopo_layer,
    load_ign_bdtopo_source_config,
    validate_ign_bdtopo_archive,
)`

## 4. Contract taxonomy

### A. Python constants

#### `PROJECT_ROOT`

```python
PROJECT_ROOT = Path(__file__).parents[2]
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::<module>` (value reference).

#### `CONFIG_PATH`

```python
CONFIG_PATH = PROJECT_ROOT / "configs/sources/ign_bdtopo_fr.yaml"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::_config_data` (value reference), `tests/unit/test_ign_bdtopo_fr.py::source_config` (value reference).

#### `SYNTHETIC_SOURCE_URL`

```python
SYNTHETIC_SOURCE_URL = "https://example.test/BDTOPO_TEST_D031.7z"
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `tests/unit/test_ign_bdtopo_fr.py::_synthetic_config` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` (value reference).

#### `LINE_LAYER`

```python
LINE_LAYER = "LIGNE_ELECTRIQUE"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_layer_loader_retains_crs_counts_and_null_geometries` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_geographic_crs_is_rejected` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` (value reference).

#### `POST_LAYER`

```python
POST_LAYER = "POSTE_DE_TRANSFORMATION"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_invalid_geometry_is_preserved_without_repair` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` (value reference).

#### `DEPARTMENT_LAYER`

```python
DEPARTMENT_LAYER = "DEPARTEMENT"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` (value reference).

#### `ROAD_LAYER`

```python
ROAD_LAYER = "TRONCON_DE_ROUTE"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` (value reference), `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_config_data`

**Exact signature**

```python
def _config_data() -> dict:
```

**Purpose**

Private `test` helper for config data; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict`.
- Every observed return expression is reproduced without truncation:
```python
yaml.safe_load(stream)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `CONFIG_PATH.open`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_invalid_department_coverage_config_fails` via `_config_data`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_required_source_field_fails` via `_config_data`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_invalid_source_configuration_fails` via `_config_data`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_unknown_source_config_field_is_rejected` via `_config_data`.

**Complete source-ordered implementation**

```python
def _config_data() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_synthetic_config`

**Exact signature**

```python
def _synthetic_config(
    source_config: IgnBdTopoSourceConfig,
    *,
    official_checksum: str | None = None,
) -> IgnBdTopoSourceConfig:
```

**Purpose**

Private `test` helper for synthetic config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoSourceConfig`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoSourceConfig.model_validate(content)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `content`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `_synthetic_config`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `_synthetic_config`.

**Complete source-ordered implementation**

```python
def _synthetic_config(
    source_config: IgnBdTopoSourceConfig,
    *,
    official_checksum: str | None = None,
) -> IgnBdTopoSourceConfig:
    content = source_config.model_dump(mode="json")
    content.update(
        {
            "source_url": SYNTHETIC_SOURCE_URL,
            "checksum_url": None,
            "official_checksum_algorithm": (
                "sha256" if official_checksum is not None else None
            ),
            "official_checksum": official_checksum,
            "expected_archive_size_bytes": None,
        }
    )
    return IgnBdTopoSourceConfig.model_validate(content)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_gpkg`

**Exact signature**

```python
def _write_gpkg(
    path: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    line_layer: str = LINE_LAYER,
    post_layer: str = POST_LAYER,
    crs: str | None = "EPSG:2154",
    invalid_post: bool = False,
    include_department: bool = False,
    department_layer: str = DEPARTMENT_LAYER,
    department_codes: list[str] | None = None,
    department_geometries: list[object] | None = None,
    include_roads: bool = False,
    road_layer: str = ROAD_LAYER,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> None:
```

**Purpose**

Serializes gpkg; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.parent.mkdir`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `geometries`, `object_ids`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::_synthetic_archive_bytes` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_geopackage_is_discovered_recursively` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_multiple_geopackages_are_rejected_as_ambiguous` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_real_layer_names_are_listed_and_discovered` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_electric_line_layer_fails` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_transformation_post_layer_fails` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_electric_line_layers_fail` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_layer_loader_retains_crs_counts_and_null_geometries` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_invalid_geometry_is_preserved_without_repair` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_geographic_crs_is_rejected` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `_write_gpkg`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `_write_gpkg`.

**Complete source-ordered implementation**

```python
def _write_gpkg(
    path: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    line_layer: str = LINE_LAYER,
    post_layer: str = POST_LAYER,
    crs: str | None = "EPSG:2154",
    invalid_post: bool = False,
    include_department: bool = False,
    department_layer: str = DEPARTMENT_LAYER,
    department_codes: list[str] | None = None,
    department_geometries: list[object] | None = None,
    include_roads: bool = False,
    road_layer: str = ROAD_LAYER,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    layer_written = False
    if include_lines:
        lines = gpd.GeoDataFrame(
            {
                "object_id": ["L_VALID", "L_NULL"],
                "nature": ["HT", "UNKNOWN"],
                "tension": ["225 kV", None],
            },
            geometry=[LineString([(0, 0), (100, 100)]), None],
            crs=crs,
        )
        pyogrio.write_dataframe(
            lines,
            path,
            layer=line_layer,
            driver="GPKG",
        )
        layer_written = True
    if include_posts:
        invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
        geometries = [
            Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)]),
            None,
        ]
        object_ids = ["P_VALID", "P_NULL"]
        if invalid_post:
            geometries.append(invalid)
            object_ids.append("P_INVALID")
        posts = gpd.GeoDataFrame(
            {
                "object_id": object_ids,
                "nature": ["POSTE"] * len(object_ids),
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            posts,
            path,
            layer=post_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_roads:
        if road_geometry_kind == "line":
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                LineString([(200, 200), (300, 260)]),
            ]
        elif road_geometry_kind == "multiline":
            road_geometries = [
                MultiLineString([[(0, 0), (100, 100)]]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        else:
            road_geometries = [
                LineString([(0, 0), (100, 100)]),
                MultiLineString(
                    [
                        [(200, 200), (250, 250)],
                        [(250, 250), (300, 260)],
                    ]
                ),
            ]
        roads = gpd.GeoDataFrame(
            {
                "object_id": ["R_LINE", "R_MULTI"],
                "nature": ["Route à 1 chaussée", "Bretelle"],
            },
            geometry=road_geometries,
            crs=road_crs or crs,
        )
        pyogrio.write_dataframe(
            roads,
            path,
            layer=road_layer,
            driver="GPKG",
            append=layer_written,
        )
        layer_written = True
    if include_department:
        codes = department_codes or ["31", "32"]
        geometries = department_geometries or [
            MultiPolygon(
                [Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]
            ),
            MultiPolygon(
                [
                    Polygon(
                        [
                            (1000, 0),
                            (1000, 1000),
                            (2000, 1000),
                            (2000, 0),
                            (1000, 0),
                        ]
                    )
                ]
            ),
        ][: len(codes)]
        departments = gpd.GeoDataFrame(
            {
                "code_insee": codes,
                "nom_officiel": [f"Department {code}" for code in codes],
            },
            geometry=geometries,
            crs=crs,
        )
        pyogrio.write_dataframe(
            departments,
            path,
            layer=department_layer,
            driver="GPKG",
            append=layer_written,
        )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_pack_7z`

**Exact signature**

```python
def _pack_7z(
    archive_path: Path,
    members: list[tuple[Path, str]],
) -> bytes:
```

**Purpose**

Private `test` helper for pack 7z; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
archive_path.read_bytes()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `archive_path.read_bytes`.
- Filesystem write: `archive_path.parent.mkdir`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::_synthetic_archive_bytes` via `_pack_7z`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `_pack_7z`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `_pack_7z`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `_pack_7z`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `_pack_7z`.

**Complete source-ordered implementation**

```python
def _pack_7z(
    archive_path: Path,
    members: list[tuple[Path, str]],
) -> bytes:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with py7zr.SevenZipFile(archive_path, "w") as archive:
        for source, archive_name in members:
            archive.write(source, arcname=archive_name)
    return archive_path.read_bytes()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_synthetic_archive_bytes`

**Exact signature**

```python
def _synthetic_archive_bytes(
    root: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    invalid_post: bool = False,
    include_department: bool = False,
    include_roads: bool = False,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> bytes:
```

**Purpose**

Private `test` helper for synthetic archive bytes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
_pack_7z(root / 'fixture.7z', [(gpkg_path, 'BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg')])
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `_synthetic_archive_bytes`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `_synthetic_archive_bytes`.

**Complete source-ordered implementation**

```python
def _synthetic_archive_bytes(
    root: Path,
    *,
    include_lines: bool = True,
    include_posts: bool = True,
    invalid_post: bool = False,
    include_department: bool = False,
    include_roads: bool = False,
    road_crs: str | None = None,
    road_geometry_kind: str = "mixed",
) -> bytes:
    gpkg_path = root / "fixture" / "BDTOPO_TEST.gpkg"
    _write_gpkg(
        gpkg_path,
        include_lines=include_lines,
        include_posts=include_posts,
        invalid_post=invalid_post,
        include_department=include_department,
        include_roads=include_roads,
        road_crs=road_crs,
        road_geometry_kind=road_geometry_kind,
    )
    return _pack_7z(
        root / "fixture.7z",
        [(gpkg_path, "BDTOPO_TEST/GPKG/BDTOPO_TEST.gpkg")],
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_response`

**Exact signature**

```python
def _response(content: bytes) -> io.BytesIO:
```

**Purpose**

Private `test` helper for response; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `io.BytesIO`.
- Every observed return expression is reproduced without truncation:
```python
io.BytesIO(content)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::_extracted_fixture` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_fresh_cache_is_reused_without_network` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_stale_recovery_backup_rejects_cache_before_network` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_official_checksum_mismatch_is_rejected` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_unsafe_parent_archive_member_is_rejected` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_synthetic_archive_extracts_and_discovers_required_layers` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_default_extraction_path_is_short_and_content_addressed` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_electricity_loader_retains_both_layer_counts` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_discovery_loads_selected_physical_layer` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_road_layer_fails_safely` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_ambiguous_road_layer_fails_safely` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_wrong_archive_config_department` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_changed_layer_inventory` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_geographic_crs` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_layer_does_not_change_electricity_loading_or_cache_shape` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_loader_selects_configured_identity` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_one_authoritative_feature` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_requires_configured_identity_field` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_missing_department_coverage_layer_fails` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_department_coverage_layer_discovery_must_be_unambiguous` via `_response`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `_response`.

**Complete source-ordered implementation**

```python
def _response(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metadata_path`

**Exact signature**

```python
def _metadata_path(archive_path: Path) -> Path:
```

**Purpose**

Private `test` helper for metadata path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
archive_path.parent / f'{archive_path.name}.metadata.json'
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_successful_archive_download_persists_sha256` via `_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_metadata_path`.

**Complete source-ordered implementation**

```python
def _metadata_path(archive_path: Path) -> Path:
    return archive_path.parent / f"{archive_path.name}.metadata.json"
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extraction_metadata_path`

**Exact signature**

```python
def _extraction_metadata_path(extraction_path: Path) -> Path:
```

**Purpose**

Private `test` helper for extraction metadata path; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `Path`.
- Every observed return expression is reproduced without truncation:
```python
extraction_path / '.landscout-extraction.json'
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_schema_v2_extraction_metadata_binds_physical_geopackage` via `_extraction_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_forged_extraction_metadata_never_returns_cache_hit` via `_extraction_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_sha_is_not_trusted` via `_extraction_metadata_path`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_size_is_not_trusted` via `_extraction_metadata_path`.

**Complete source-ordered implementation**

```python
def _extraction_metadata_path(extraction_path: Path) -> Path:
    return extraction_path / ".landscout-extraction.json"
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extracted_fixture`

**Exact signature**

```python
def _extracted_fixture(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    *,
    include_roads: bool = False,
) -> tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]:
```

**Purpose**

Private `test` helper for extracted fixture; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]`.
- Every observed return expression is reproduced without truncation:
```python
(config, download, extraction)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `download_ign_bdtopo_archive`.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_schema_v2_extraction_metadata_binds_physical_geopackage` via `_extracted_fixture`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_same_size_geopackage_tamper_invalidates_extraction_cache` via `_extracted_fixture`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_forged_extraction_metadata_never_returns_cache_hit` via `_extracted_fixture`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_sha_is_not_trusted` via `_extracted_fixture`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_malformed_geopackage_size_is_not_trusted` via `_extracted_fixture`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_physical_layer_cannot_collide_with_electricity_roles` via `_extracted_fixture`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_direct_consumers_reject_same_inventory_content_tampering` via `_extracted_fixture`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_source_change_after_physical_read` via `_extracted_fixture`.

**Complete source-ordered implementation**

```python
def _extracted_fixture(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    *,
    include_roads: bool = False,
) -> tuple[IgnBdTopoSourceConfig, IgnBdTopoDownload, IgnBdTopoExtraction]:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=include_roads,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
    return config, download, extraction
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_expire_cache`

**Exact signature**

```python
def _expire_cache(metadata_path: Path) -> bytes:
```

**Purpose**

Private `test` helper for expire cache; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
metadata_path.read_bytes()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `metadata_path.read_bytes`, `metadata_path.read_text`.
- Filesystem write: `metadata_path.write_text`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `metadata['download_timestamp']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_expired_cache_is_refreshed` via `_expire_cache`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_failed_refresh_preserves_valid_cache` via `_expire_cache`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_corrupt_refresh_preserves_valid_cache` via `_expire_cache`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `_expire_cache`.
- direct call: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `_expire_cache`.

**Complete source-ordered implementation**

```python
def _expire_cache(metadata_path: Path) -> bytes:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["download_timestamp"] = (
        datetime.now(UTC) - timedelta(days=365)
    ).isoformat()
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
    return metadata_path.read_bytes()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `source_config` — pytest fixture

- Scope: `function` (decorator `pytest.fixture`).
- Returned/yielded object expression(s): `load_ign_bdtopo_source_config(CONFIG_PATH)`.
- Tests requesting it by parameter injection: `_synthetic_config`, `_extracted_fixture`, `test_valid_source_config_loads`, `test_successful_archive_download_persists_sha256`, `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`, `test_fresh_cache_is_reused_without_network`, `test_stale_recovery_backup_rejects_cache_before_network`, `test_expired_cache_is_refreshed`, `test_failed_refresh_preserves_valid_cache`, `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`, `test_corrupt_refresh_preserves_valid_cache`, `test_metadata_publication_failure_restores_previous_cache_pair`, `test_cleanup_failure_does_not_mask_double_failure_recovery_error`, `test_official_checksum_mismatch_is_rejected`, `test_unsafe_parent_archive_member_is_rejected`, `test_real_layer_names_are_listed_and_discovered`, `test_missing_electric_line_layer_fails`, `test_missing_transformation_post_layer_fails`, `test_ambiguous_electric_line_layers_fail`, `test_synthetic_archive_extracts_and_discovers_required_layers`, `test_schema_v2_extraction_metadata_binds_physical_geopackage`, `test_same_size_geopackage_tamper_invalidates_extraction_cache`, `test_forged_extraction_metadata_never_returns_cache_hit`, `test_malformed_geopackage_sha_is_not_trusted`, `test_malformed_geopackage_size_is_not_trusted`, `test_default_extraction_path_is_short_and_content_addressed`, `test_electricity_loader_retains_both_layer_counts`, `test_road_layer_discovery_loads_selected_physical_layer`, `test_road_physical_layer_cannot_collide_with_electricity_roles`, `test_missing_road_layer_fails_safely`, `test_ambiguous_road_layer_fails_safely`, `test_road_loader_rejects_wrong_archive_config_department`, `test_road_loader_rejects_changed_layer_inventory`, `test_road_loader_rejects_geographic_crs`, `test_road_loader_preserves_lambert93_lines_unchanged`, `test_road_layer_does_not_change_electricity_loading_or_cache_shape`, `test_department_coverage_loader_selects_configured_identity`, `test_department_coverage_requires_one_authoritative_feature`, `test_department_coverage_requires_configured_identity_field`, `test_missing_department_coverage_layer_fails`, `test_department_coverage_layer_discovery_must_be_unambiguous`, `test_direct_consumers_reject_same_inventory_content_tampering`, `test_road_loader_rejects_source_change_after_physical_read`.

**Complete fixture implementation**

```python
def source_config() -> IgnBdTopoSourceConfig:
    return load_ign_bdtopo_source_config(CONFIG_PATH)
```

### `test_valid_source_config_loads`

**Purpose**

Exercises `valid source config loads`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `source_config` (local fixture, scope `function`).
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
assert "IGN" in source_config.provider
assert source_config.department_code == "31"
assert source_config.projection == "EPSG:2154"
assert source_config.format == "GPKG"
assert source_config.edition == "2026-06-15"
assert source_config.access.road_segments.class_label == "Tronçon de route"
assert source_config.access.road_segments.match_tokens == ("tronçon", "route")
assert source_config.coverage.department_layer.match_tokens == ("departement",)
assert (
        source_config.coverage.department_layer.department_code_field
        == "code_insee"
    )
```

**Regression protected**

Locks `valid source config loads` through the exact asserted conditions: `'IGN' in source_config.provider`; `source_config.department_code == '31'`; `source_config.projection == 'EPSG:2154'`; `source_config.format == 'GPKG'`; plus 5 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_source_config_loads(source_config: IgnBdTopoSourceConfig) -> None:
    assert "IGN" in source_config.provider
    assert source_config.department_code == "31"
    assert source_config.projection == "EPSG:2154"
    assert source_config.format == "GPKG"
    assert source_config.edition == "2026-06-15"
    assert source_config.access.road_segments.class_label == "Tronçon de route"
    assert source_config.access.road_segments.match_tokens == ("tronçon", "route")
    assert source_config.coverage.department_layer.match_tokens == ("departement",)
    assert (
        source_config.coverage.department_layer.department_code_field
        == "code_insee"
    )
```

### `test_invalid_department_coverage_config_fails`

**Purpose**

Exercises `invalid department coverage config fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
content = _config_data()
if mutation == "missing":
        del content["coverage"]
    elif mutation == "blank_field":
        content["coverage"]["department_layer"]["department_code_field"] = " "
    else:
        content["coverage"]["department_layer"]["match_tokens"] = []
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Regression protected**

Locks `invalid department coverage config fails`: the reproduced adversarial input must raise `ValidationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_department_coverage_config_fails(mutation: str) -> None:
    content = _config_data()
    if mutation == "missing":
        del content["coverage"]
    elif mutation == "blank_field":
        content["coverage"]["department_layer"]["department_code_field"] = " "
    else:
        content["coverage"]["department_layer"]["match_tokens"] = []

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

### `test_missing_required_source_field_fails`

**Purpose**

Exercises `missing required source field fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
content = _config_data()
del content[field]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Regression protected**

Locks `missing required source field fails`: the reproduced adversarial input must raise `ValidationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_required_source_field_fails(field: str) -> None:
    content = _config_data()
    del content[field]

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

### `test_invalid_source_configuration_fails`

**Purpose**

Exercises `invalid source configuration fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
content = _config_data()
content[field] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Regression protected**

Locks `invalid source configuration fails`: the reproduced adversarial input must raise `ValidationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_source_configuration_fails(field: str, value: str) -> None:
    content = _config_data()
    content[field] = value

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

### `test_unknown_source_config_field_is_rejected`

**Purpose**

Exercises `unknown source config field is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
content = _config_data()
content["invented"] = "not allowed"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

**Regression protected**

Locks `unknown source config field is rejected`: the reproduced adversarial input must raise `ValidationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_source_config_field_is_rejected() -> None:
    content = _config_data()
    content["invented"] = "not allowed"

    with pytest.raises(ValidationError):
        IgnBdTopoSourceConfig.model_validate(content)
```

### `test_successful_archive_download_persists_sha256`

**Purpose**

Exercises `successful archive download persists sha256`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path)
config = _synthetic_config(source_config)
metadata = json.loads(_metadata_path(result.path).read_text(encoding="utf-8"))
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        result = download_ign_bdtopo_archive(config, tmp_path / "cache")
```

**Expected result**

```python
assert result.cache_hit is False
assert result.path.read_bytes() == archive_content
assert result.file_size == len(archive_content)
assert result.sha256 == sha256(archive_content).hexdigest()
assert metadata["sha256"] == result.sha256
assert metadata["source_url"] == SYNTHETIC_SOURCE_URL
assert metadata["official_checksum"] is None
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_successful_archive_download_persists_sha256(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        result = download_ign_bdtopo_archive(config, tmp_path / "cache")

    assert result.cache_hit is False
    assert result.path.read_bytes() == archive_content
    assert result.file_size == len(archive_content)
    assert result.sha256 == sha256(archive_content).hexdigest()
    metadata = json.loads(_metadata_path(result.path).read_text(encoding="utf-8"))
    assert metadata["sha256"] == result.sha256
    assert metadata["source_url"] == SYNTHETIC_SOURCE_URL
    assert metadata["official_checksum"] is None
```

### `test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum`

**Purpose**

Exercises `archive integrity reports local sha256 and no fabricated checksum`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "fixture.7z"
archive_content = _synthetic_archive_bytes(tmp_path / "source")
archive_path.write_bytes(archive_content)
```

**Action**

```python
integrity = validate_ign_bdtopo_archive(
        archive_path,
        _synthetic_config(source_config),
    )
```

**Expected result**

```python
assert integrity.file_size == len(archive_content)
assert integrity.sha256 == sha256(archive_content).hexdigest()
assert integrity.official_checksum is None
assert integrity.official_checksum_algorithm is None
assert integrity.official_checksum_validated is False
```

**Regression protected**

Locks `archive integrity reports local sha256 and no fabricated checksum` through the exact asserted conditions: `integrity.file_size == len(archive_content)`; `integrity.sha256 == sha256(archive_content).hexdigest()`; `integrity.official_checksum is None`; `integrity.official_checksum_algorithm is None`; plus 1 additional reproduced assertion(s).

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_archive_integrity_reports_local_sha256_and_no_fabricated_checksum(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_path = tmp_path / "fixture.7z"
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    archive_path.write_bytes(archive_content)

    integrity = validate_ign_bdtopo_archive(
        archive_path,
        _synthetic_config(source_config),
    )

    assert integrity.file_size == len(archive_content)
    assert integrity.sha256 == sha256(archive_content).hexdigest()
    assert integrity.official_checksum is None
    assert integrity.official_checksum_algorithm is None
    assert integrity.official_checksum_validated is False
```

### `test_fresh_cache_is_reused_without_network`

**Purpose**

Exercises `fresh cache is reused without network`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
content = _synthetic_archive_bytes(tmp_path)
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        side_effect=AssertionError("network must not be called"),
    ):
        second = download_ign_bdtopo_archive(config, cache_dir)
```

**Expected result**

```python
assert second.cache_hit is True
assert second.path == first.path
assert second.sha256 == first.sha256
assert second.download_timestamp == first.download_timestamp
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_fresh_cache_is_reused_without_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        side_effect=AssertionError("network must not be called"),
    ):
        second = download_ign_bdtopo_archive(config, cache_dir)

    assert second.cache_hit is True
    assert second.path == first.path
    assert second.sha256 == first.sha256
    assert second.download_timestamp == first.download_timestamp
```

### `test_stale_recovery_backup_rejects_cache_before_network`

**Purpose**

Exercises `stale recovery backup rejects cache before network`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
content = _synthetic_archive_bytes(tmp_path)
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
recovery_path = first.path.with_name(f"{first.path.name}.bak")
recovery_bytes = b"manual IGN recovery material"
recovery_path.write_bytes(recovery_bytes)
opener.assert_not_called()
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            side_effect=AssertionError("stale recovery must fail before network"),
        ) as opener,
        pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)
assert recovery_path.read_bytes() == recovery_bytes
assert first.path.read_bytes() == content
```

**Regression protected**

Locks `stale recovery backup rejects cache before network`: the reproduced adversarial input must raise `IgnBdTopoDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_stale_recovery_backup_rejects_cache_before_network(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    recovery_path = first.path.with_name(f"{first.path.name}.bak")
    recovery_bytes = b"manual IGN recovery material"
    recovery_path.write_bytes(recovery_bytes)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            side_effect=AssertionError("stale recovery must fail before network"),
        ) as opener,
        pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    opener.assert_not_called()
    assert recovery_path.read_bytes() == recovery_bytes
    assert first.path.read_bytes() == content
```

### `test_expired_cache_is_refreshed`

**Purpose**

Exercises `expired cache is refreshed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
old_content = _synthetic_archive_bytes(tmp_path / "v1")
new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
_expire_cache(_metadata_path(first.path))
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(new_content),
    ) as opener:
        refreshed = download_ign_bdtopo_archive(config, cache_dir)
```

**Expected result**

```python
assert opener.call_count == 1
assert refreshed.cache_hit is False
assert refreshed.path.read_bytes() == new_content
assert refreshed.sha256 != first.sha256
assert not list(cache_dir.glob("*.part"))
assert not list(cache_dir.glob("*.bak"))
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_expired_cache_is_refreshed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    _expire_cache(_metadata_path(first.path))

    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(new_content),
    ) as opener:
        refreshed = download_ign_bdtopo_archive(config, cache_dir)

    assert opener.call_count == 1
    assert refreshed.cache_hit is False
    assert refreshed.path.read_bytes() == new_content
    assert refreshed.sha256 != first.sha256
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

### `test_failed_refresh_preserves_valid_cache`

**Purpose**

Exercises `failed refresh preserves valid cache`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
content = _synthetic_archive_bytes(tmp_path)
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
metadata_path = _metadata_path(first.path)
old_archive = first.path.read_bytes()
expired_metadata = _expire_cache(metadata_path)
error = HTTPError(SYNTHETIC_SOURCE_URL, 503, "Unavailable", None, None)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
```

**Expected result**

```python
with (
        patch("landscout.sources.ign_bdtopo_fr.open_safe_https", side_effect=error),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)
assert first.path.read_bytes() == old_archive
assert metadata_path.read_bytes() == expired_metadata
assert not list(cache_dir.glob("*.part"))
assert not list(cache_dir.glob("*.bak"))
```

**Regression protected**

Locks `failed refresh preserves valid cache`: the reproduced adversarial input must raise `IgnBdTopoDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_failed_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    error = HTTPError(SYNTHETIC_SOURCE_URL, 503, "Unavailable", None, None)

    with (
        patch("landscout.sources.ign_bdtopo_fr.open_safe_https", side_effect=error),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

### `test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned`

**Purpose**

Exercises `corrupt new archive is rejected and temporary files are cleaned`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"not a 7z archive"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)
assert not list(cache_dir.glob("*.7z"))
assert not list(cache_dir.glob("*.part"))
assert not list(cache_dir.glob("*.bak"))
```

**Regression protected**

Locks `corrupt new archive is rejected and temporary files are cleaned`: the reproduced adversarial input must raise `IgnBdTopoArchiveError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_corrupt_new_archive_is_rejected_and_temporary_files_are_cleaned(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"not a 7z archive"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

### `test_corrupt_refresh_preserves_valid_cache`

**Purpose**

Exercises `corrupt refresh preserves valid cache`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
content = _synthetic_archive_bytes(tmp_path)
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
metadata_path = _metadata_path(first.path)
old_archive = first.path.read_bytes()
expired_metadata = _expire_cache(metadata_path)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"broken refresh"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)
assert first.path.read_bytes() == old_archive
assert metadata_path.read_bytes() == expired_metadata
assert not list(cache_dir.glob("*.part"))
```

**Regression protected**

Locks `corrupt refresh preserves valid cache`: the reproduced adversarial input must raise `IgnBdTopoArchiveError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_corrupt_refresh_preserves_valid_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https", return_value=_response(content)
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(b"broken refresh"),
        ),
        pytest.raises(IgnBdTopoArchiveError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
```

### `test_metadata_publication_failure_restores_previous_cache_pair`

**Purpose**

Exercises `metadata publication failure restores previous cache pair`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
old_content = _synthetic_archive_bytes(tmp_path / "v1")
new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
metadata_path = _metadata_path(first.path)
old_archive = first.path.read_bytes()
expired_metadata = _expire_cache(metadata_path)
original_replace = ign_bdtopo_fr._replace_file
failure_injected = False
def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source.name.endswith(".metadata.json.part") and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata lock")
        original_replace(source, target)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)
assert failure_injected
assert first.path.read_bytes() == old_archive
assert metadata_path.read_bytes() == expired_metadata
assert not list(cache_dir.glob("*.part"))
assert not list(cache_dir.glob("*.bak"))
```

**Regression protected**

Locks `metadata publication failure restores previous cache pair`: the reproduced adversarial input must raise `IgnBdTopoDownloadError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_metadata_publication_failure_restores_previous_cache_pair(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    expired_metadata = _expire_cache(metadata_path)
    original_replace = ign_bdtopo_fr._replace_file
    failure_injected = False

    def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source.name.endswith(".metadata.json.part") and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata lock")
        original_replace(source, target)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_metadata_publication,
        ),
        pytest.raises(IgnBdTopoDownloadError),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert failure_injected
    assert first.path.read_bytes() == old_archive
    assert metadata_path.read_bytes() == expired_metadata
    assert not list(cache_dir.glob("*.part"))
    assert not list(cache_dir.glob("*.bak"))
```

### `test_metadata_publication_failure_restores_previous_cache_pair.fail_metadata_publication`

**Exact signature**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail metadata publication; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.name.endswith('.metadata.json.part') and target == metadata_path`.
- Explicit raise expressions: `PermissionError('simulated persistent metadata lock')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_ign_bdtopo_fr.py::test_metadata_publication_failure_restores_previous_cache_pair` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_metadata_publication)`.

**Complete source-ordered implementation**

```python
def fail_metadata_publication(source: Path, target: Path) -> None:
        nonlocal failure_injected
        if source.name.endswith(".metadata.json.part") and target == metadata_path:
            failure_injected = True
            raise PermissionError("simulated persistent metadata lock")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups`

**Purpose**

Exercises `publication and rollback failure preserves exact recovery backups`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "cached.7z"
metadata_path = tmp_path / "cached.7z.metadata.json"
temporary_archive = tmp_path / "cached.7z.part"
temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
old_archive = b"exact old archive"
old_metadata = b"exact old metadata"
archive_path.write_bytes(old_archive)
metadata_path.write_bytes(old_metadata)
temporary_archive.write_bytes(b"replacement archive")
temporary_metadata.write_bytes(b"replacement metadata")
archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
original_replace = ign_bdtopo_fr._replace_file
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
assert archive_backup.read_bytes() == old_archive
assert metadata_backup.read_bytes() == old_metadata
```

**Regression protected**

Prevents cache publication/rollback failures from destroying the last recoverable bytes; the exact old archive/metadata or extraction tree asserted below must survive in recovery material.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_publication_and_rollback_failure_preserves_exact_recovery_backups(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    old_archive = b"exact old archive"
    old_metadata = b"exact old metadata"
    archive_path.write_bytes(old_archive)
    metadata_path.write_bytes(old_metadata)
    temporary_archive.write_bytes(b"replacement archive")
    temporary_metadata.write_bytes(b"replacement metadata")
    archive_backup = archive_path.with_name(f"{archive_path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    with (
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

### `test_publication_and_rollback_failure_preserves_exact_recovery_backups.fail_publication_and_rollback`

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail publication and rollback; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Guard with a raise path: `source == archive_backup and target == archive_path`.
- Explicit raise expressions: `OSError('simulated archive rollback failure')`, `OSError('simulated metadata publication failure')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_ign_bdtopo_fr.py::test_publication_and_rollback_failure_preserves_exact_recovery_backups` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == archive_path:
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error`

**Purpose**

Exercises `cleanup failure does not mask double failure recovery error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
old_content = _synthetic_archive_bytes(tmp_path / "v1")
new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
metadata_path = _metadata_path(first.path)
old_archive = first.path.read_bytes()
old_metadata = _expire_cache(metadata_path)
temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
archive_backup = first.path.with_name(f"{first.path.name}.bak")
metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
original_replace = ign_bdtopo_fr._replace_file
original_unlink = Path.unlink
rollback_failed = False
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        patch.object(Path, "unlink", new=fail_temporary_cleanup),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)
assert archive_backup.read_bytes() == old_archive
assert metadata_backup.read_bytes() == old_metadata
```

**Regression protected**

Prevents failed cache publication and failed rollback from deleting the last recoverable backup bytes.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_cleanup_failure_does_not_mask_double_failure_recovery_error(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    old_content = _synthetic_archive_bytes(tmp_path / "v1")
    new_content = _synthetic_archive_bytes(tmp_path / "v2", invalid_post=True)
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(old_content),
    ):
        first = download_ign_bdtopo_archive(config, cache_dir)
    metadata_path = _metadata_path(first.path)
    old_archive = first.path.read_bytes()
    old_metadata = _expire_cache(metadata_path)
    temporary_metadata = metadata_path.with_name(f"{metadata_path.name}.part")
    archive_backup = first.path.with_name(f"{first.path.name}.bak")
    metadata_backup = metadata_path.with_name(f"{metadata_path.name}.bak")
    original_replace = ign_bdtopo_fr._replace_file
    original_unlink = Path.unlink
    rollback_failed = False

    def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)

    def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(new_content),
        ),
        patch.object(
            ign_bdtopo_fr,
            "_replace_file",
            side_effect=fail_publication_and_rollback,
        ),
        patch.object(Path, "unlink", new=fail_temporary_cleanup),
        pytest.raises(IgnBdTopoDownloadError, match="rollback"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert archive_backup.read_bytes() == old_archive
    assert metadata_backup.read_bytes() == old_metadata
```

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback`

**Exact signature**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
```

**Purpose**

Private `test` helper for fail publication and rollback; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source == temporary_metadata and target == metadata_path`.
- Guard with a raise path: `source == archive_backup and target == first.path`.
- Explicit raise expressions: `OSError('simulated archive rollback failure')`, `OSError('simulated metadata publication failure')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(ign_bdtopo_fr, '_replace_file', side_effect=fail_publication_and_rollback)`.

**Complete source-ordered implementation**

```python
def fail_publication_and_rollback(source: Path, target: Path) -> None:
        nonlocal rollback_failed
        if source == temporary_metadata and target == metadata_path:
            raise OSError("simulated metadata publication failure")
        if source == archive_backup and target == first.path:
            rollback_failed = True
            raise OSError("simulated archive rollback failure")
        original_replace(source, target)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_temporary_cleanup`

**Exact signature**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
```

**Purpose**

Private `test` helper for fail temporary cleanup; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `rollback_failed and path == temporary_metadata`.
- Explicit raise expressions: `PermissionError('simulated temporary cleanup failure')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_ign_bdtopo_fr.py::test_cleanup_failure_does_not_mask_double_failure_recovery_error` via `patch.object(Path, 'unlink', new=fail_temporary_cleanup)`.

**Complete source-ordered implementation**

```python
def fail_temporary_cleanup(path: Path, *, missing_ok: bool = False) -> None:
        if rollback_failed and path == temporary_metadata:
            raise PermissionError("simulated temporary cleanup failure")
        original_unlink(path, missing_ok=missing_ok)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_stale_cache_recovery_backup_fails_closed_without_destroying_it`

**Purpose**

Exercises `stale cache recovery backup fails closed without destroying it`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_path = tmp_path / "cached.7z"
metadata_path = tmp_path / "cached.7z.metadata.json"
temporary_archive = tmp_path / "cached.7z.part"
temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
archive_backup = tmp_path / "cached.7z.bak"
archive_path.write_bytes(b"old archive")
metadata_path.write_bytes(b"old metadata")
temporary_archive.write_bytes(b"new archive")
temporary_metadata.write_bytes(b"new metadata")
archive_backup.write_bytes(b"manual recovery archive")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )
assert archive_path.read_bytes() == b"old archive"
assert metadata_path.read_bytes() == b"old metadata"
assert archive_backup.read_bytes() == b"manual recovery archive"
```

**Regression protected**

Locks `stale cache recovery backup fails closed without destroying it`: the reproduced adversarial input must raise `IgnBdTopoDownloadError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_stale_cache_recovery_backup_fails_closed_without_destroying_it(
    tmp_path: Path,
) -> None:
    archive_path = tmp_path / "cached.7z"
    metadata_path = tmp_path / "cached.7z.metadata.json"
    temporary_archive = tmp_path / "cached.7z.part"
    temporary_metadata = tmp_path / "cached.7z.metadata.json.part"
    archive_backup = tmp_path / "cached.7z.bak"
    archive_path.write_bytes(b"old archive")
    metadata_path.write_bytes(b"old metadata")
    temporary_archive.write_bytes(b"new archive")
    temporary_metadata.write_bytes(b"new metadata")
    archive_backup.write_bytes(b"manual recovery archive")

    with pytest.raises(IgnBdTopoDownloadError, match="backup|recovery|manual"):
        ign_bdtopo_fr._publish_cache_pair(
            temporary_archive,
            temporary_metadata,
            archive_path,
            metadata_path,
        )

    assert archive_path.read_bytes() == b"old archive"
    assert metadata_path.read_bytes() == b"old metadata"
    assert archive_backup.read_bytes() == b"manual recovery archive"
```

### `test_official_checksum_mismatch_is_rejected`

**Purpose**

Exercises `official checksum mismatch is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path)
config = _synthetic_config(source_config, official_checksum="0" * 64)
cache_dir = tmp_path / "cache"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ),
        pytest.raises(IgnBdTopoArchiveError, match="checksum|SHA"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)
assert not list(cache_dir.glob("*.7z"))
assert not list(cache_dir.glob("*.part"))
```

**Regression protected**

Locks `official checksum mismatch is rejected`: the reproduced adversarial input must raise `IgnBdTopoArchiveError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_official_checksum_mismatch_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path)
    config = _synthetic_config(source_config, official_checksum="0" * 64)
    cache_dir = tmp_path / "cache"

    with (
        patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ),
        pytest.raises(IgnBdTopoArchiveError, match="checksum|SHA"),
    ):
        download_ign_bdtopo_archive(config, cache_dir)

    assert not list(cache_dir.glob("*.7z"))
    assert not list(cache_dir.glob("*.part"))
```

### `test_unsafe_parent_archive_member_is_rejected`

**Purpose**

Exercises `unsafe parent archive member is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "unsafe-source.gpkg"
_write_gpkg(gpkg_path)
archive_content = _pack_7z(
        tmp_path / "unsafe.7z",
        [(gpkg_path, "../escape.gpkg")],
    )
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
```

**Expected result**

```python
with pytest.raises(IgnBdTopoArchiveError, match="unsafe|member|path"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )
assert not (tmp_path / "escape.gpkg").exists()
assert not list(tmp_path.glob("*.part"))
```

**Regression protected**

Locks `unsafe parent archive member is rejected`: the reproduced adversarial input must raise `IgnBdTopoArchiveError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_unsafe_parent_archive_member_is_rejected(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "unsafe-source.gpkg"
    _write_gpkg(gpkg_path)
    archive_content = _pack_7z(
        tmp_path / "unsafe.7z",
        [(gpkg_path, "../escape.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    with pytest.raises(IgnBdTopoArchiveError, match="unsafe|member|path"):
        extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "extracted",
        )

    assert not (tmp_path / "escape.gpkg").exists()
    assert not list(tmp_path.glob("*.part"))
```

### `test_geopackage_is_discovered_recursively`

**Purpose**

Exercises `geopackage is discovered recursively`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "nested" / "data" / "bdtopo.gpkg"
_write_gpkg(gpkg_path)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path
```

**Regression protected**

Locks `geopackage is discovered recursively` through the exact asserted conditions: `discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_geopackage_is_discovered_recursively(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "nested" / "data" / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    assert discover_ign_bdtopo_geopackage(tmp_path) == gpkg_path
```

### `test_multiple_geopackages_are_rejected_as_ambiguous`

**Purpose**

Exercises `multiple geopackages are rejected as ambiguous`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_write_gpkg(tmp_path / "a" / "one.gpkg")
_write_gpkg(tmp_path / "b" / "two.gpkg")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnBdTopoArchiveError, match="GeoPackage|exactly one|ambiguous"):
        discover_ign_bdtopo_geopackage(tmp_path)
```

**Regression protected**

Locks `multiple geopackages are rejected as ambiguous`: the reproduced adversarial input must raise `IgnBdTopoArchiveError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_multiple_geopackages_are_rejected_as_ambiguous(tmp_path: Path) -> None:
    _write_gpkg(tmp_path / "a" / "one.gpkg")
    _write_gpkg(tmp_path / "b" / "two.gpkg")

    with pytest.raises(IgnBdTopoArchiveError, match="GeoPackage|exactly one|ambiguous"):
        discover_ign_bdtopo_geopackage(tmp_path)
```

### `test_real_layer_names_are_listed_and_discovered`

**Purpose**

Exercises `real layer names are listed and discovered`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "bdtopo.gpkg"
_write_gpkg(gpkg_path)
```

**Action**

```python
all_layers = list_ign_bdtopo_layers(gpkg_path)
selection = discover_ign_bdtopo_layers(gpkg_path, source_config)
```

**Expected result**

```python
assert set(all_layers) == {LINE_LAYER, POST_LAYER}
assert selection.electric_lines_layer == LINE_LAYER
assert selection.transformation_posts_layer == POST_LAYER
assert set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}
```

**Regression protected**

Locks `real layer names are listed and discovered` through the exact asserted conditions: `set(all_layers) == {LINE_LAYER, POST_LAYER}`; `selection.electric_lines_layer == LINE_LAYER`; `selection.transformation_posts_layer == POST_LAYER`; `set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_real_layer_names_are_listed_and_discovered(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    all_layers = list_ign_bdtopo_layers(gpkg_path)
    selection = discover_ign_bdtopo_layers(gpkg_path, source_config)

    assert set(all_layers) == {LINE_LAYER, POST_LAYER}
    assert selection.electric_lines_layer == LINE_LAYER
    assert selection.transformation_posts_layer == POST_LAYER
    assert set(selection.all_layer_names) == {LINE_LAYER, POST_LAYER}
```

### `test_missing_electric_line_layer_fails`

**Purpose**

Exercises `missing electric line layer fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "posts-only.gpkg"
_write_gpkg(gpkg_path, include_lines=False)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="electric|line|Ligne"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

**Regression protected**

Locks `missing electric line layer fails`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_missing_electric_line_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "posts-only.gpkg"
    _write_gpkg(gpkg_path, include_lines=False)

    with pytest.raises(IgnBdTopoLayerError, match="electric|line|Ligne"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

### `test_missing_transformation_post_layer_fails`

**Purpose**

Exercises `missing transformation post layer fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "lines-only.gpkg"
_write_gpkg(gpkg_path, include_posts=False)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="transformation|post|Poste"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

**Regression protected**

Locks `missing transformation post layer fails`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_missing_transformation_post_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "lines-only.gpkg"
    _write_gpkg(gpkg_path, include_posts=False)

    with pytest.raises(IgnBdTopoLayerError, match="transformation|post|Poste"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

### `test_ambiguous_electric_line_layers_fail`

**Purpose**

Exercises `ambiguous electric line layers fail`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "ambiguous-lines.gpkg"
_write_gpkg(gpkg_path)
secondary_lines = gpd.GeoDataFrame(
        {"object_id": ["L_SECONDARY"]},
        geometry=[LineString([(0, 0), (50, 50)])],
        crs="EPSG:2154",
    )
pyogrio.write_dataframe(
        secondary_lines,
        gpkg_path,
        layer="LIGNE_ELECTRIQUE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_ambiguous_electric_line_layers_fail(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "ambiguous-lines.gpkg"
    _write_gpkg(gpkg_path)
    secondary_lines = gpd.GeoDataFrame(
        {"object_id": ["L_SECONDARY"]},
        geometry=[LineString([(0, 0), (50, 50)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary_lines,
        gpkg_path,
        layer="LIGNE_ELECTRIQUE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        discover_ign_bdtopo_layers(gpkg_path, source_config)
```

### `test_synthetic_archive_extracts_and_discovers_required_layers`

**Purpose**

Exercises `synthetic archive extracts and discovers required layers`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source")
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
```

**Expected result**

```python
assert extraction.geopackage_path.is_file()
assert extraction.electric_lines_layer == LINE_LAYER
assert extraction.transformation_posts_layer == POST_LAYER
```

**Regression protected**

Locks `synthetic archive extracts and discovers required layers` through the exact asserted conditions: `extraction.geopackage_path.is_file()`; `extraction.electric_lines_layer == LINE_LAYER`; `extraction.transformation_posts_layer == POST_LAYER`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_synthetic_archive_extracts_and_discovers_required_layers(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")

    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    assert extraction.geopackage_path.is_file()
    assert extraction.electric_lines_layer == LINE_LAYER
    assert extraction.transformation_posts_layer == POST_LAYER
```

### `test_schema_v2_extraction_metadata_binds_physical_geopackage`

**Purpose**

Exercises `schema v2 extraction metadata binds physical geopackage`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, extraction = _extracted_fixture(tmp_path, source_config)
metadata = json.loads(
        _extraction_metadata_path(extraction.extraction_path).read_text(
            encoding="utf-8"
        )
    )
```

**Action**

```python
cached = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )
```

**Expected result**

```python
assert metadata["schema_version"] == 2
assert metadata["geopackage_size_bytes"] == extraction.geopackage_path.stat().st_size
assert metadata["geopackage_sha256"] == sha256(
        extraction.geopackage_path.read_bytes()
    ).hexdigest()
assert extraction.geopackage_size_bytes == metadata["geopackage_size_bytes"]
assert extraction.geopackage_sha256 == metadata["geopackage_sha256"]
assert cached.cache_hit is True
assert cached.geopackage_size_bytes == metadata["geopackage_size_bytes"]
assert cached.geopackage_sha256 == metadata["geopackage_sha256"]
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_schema_v2_extraction_metadata_binds_physical_geopackage(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata = json.loads(
        _extraction_metadata_path(extraction.extraction_path).read_text(
            encoding="utf-8"
        )
    )

    assert metadata["schema_version"] == 2
    assert metadata["geopackage_size_bytes"] == extraction.geopackage_path.stat().st_size
    assert metadata["geopackage_sha256"] == sha256(
        extraction.geopackage_path.read_bytes()
    ).hexdigest()
    assert extraction.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert extraction.geopackage_sha256 == metadata["geopackage_sha256"]

    cached = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )
    assert cached.cache_hit is True
    assert cached.geopackage_size_bytes == metadata["geopackage_size_bytes"]
    assert cached.geopackage_sha256 == metadata["geopackage_sha256"]
```

### `test_same_size_geopackage_tamper_invalidates_extraction_cache`

**Purpose**

Exercises `same size geopackage tamper invalidates extraction cache`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, download, extraction = _extracted_fixture(tmp_path, source_config)
original = extraction.geopackage_path.read_bytes()
tampered = bytearray(original)
tampered[-1] ^= 1
extraction.geopackage_path.write_bytes(tampered)
```

**Action**

```python
rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )
```

**Expected result**

```python
assert extraction.geopackage_path.stat().st_size == len(original)
assert rebuilt.cache_hit is False
assert rebuilt.geopackage_path.read_bytes() == original
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_same_size_geopackage_tamper_invalidates_extraction_cache(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    original = extraction.geopackage_path.read_bytes()
    tampered = bytearray(original)
    tampered[-1] ^= 1
    extraction.geopackage_path.write_bytes(tampered)
    assert extraction.geopackage_path.stat().st_size == len(original)

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False
    assert rebuilt.geopackage_path.read_bytes() == original
```

### `test_forged_extraction_metadata_never_returns_cache_hit`

**Purpose**

Exercises `forged extraction metadata never returns cache hit`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
config, download, extraction = _extracted_fixture(tmp_path, source_config)
metadata_path = _extraction_metadata_path(extraction.extraction_path)
metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
metadata[field] = value
metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
```

**Action**

```python
rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )
```

**Expected result**

```python
assert rebuilt.cache_hit is False
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_forged_extraction_metadata_never_returns_cache_hit(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    field: str,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata[field] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=extraction.extraction_path,
    )

    assert rebuilt.cache_hit is False
```

### `test_malformed_geopackage_sha_is_not_trusted`

**Purpose**

Exercises `malformed geopackage sha is not trusted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
config, download, extraction = _extracted_fixture(tmp_path, source_config)
metadata_path = _extraction_metadata_path(extraction.extraction_path)
metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
metadata["geopackage_sha256"] = value
metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
```

**Action**

```python
rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )
```

**Expected result**

```python
assert rebuilt.cache_hit is False
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_geopackage_sha_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: str,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_sha256"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False
```

### `test_malformed_geopackage_size_is_not_trusted`

**Purpose**

Exercises `malformed geopackage size is not trusted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
config, download, extraction = _extracted_fixture(tmp_path, source_config)
metadata_path = _extraction_metadata_path(extraction.extraction_path)
metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
metadata["geopackage_size_bytes"] = value
metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
```

**Action**

```python
rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )
```

**Expected result**

```python
assert rebuilt.cache_hit is False
```

**Regression protected**

Pins verified cache reuse and ensures the successful local path avoids the external operation asserted by the test.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_geopackage_size_is_not_trusted(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    value: object,
) -> None:
    config, download, extraction = _extracted_fixture(tmp_path, source_config)
    metadata_path = _extraction_metadata_path(extraction.extraction_path)
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["geopackage_size_bytes"] = value
    metadata_path.write_text(json.dumps(metadata), encoding="utf-8")

    rebuilt = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction.extraction_path
    )

    assert rebuilt.cache_hit is False
```

### `test_default_extraction_path_is_short_and_content_addressed`

**Purpose**

Exercises `default extraction path is short and content addressed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source")
config = _synthetic_config(source_config)
cache_dir = tmp_path / "cache"
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, cache_dir)
extraction = extract_ign_bdtopo_archive(download, config)
```

**Expected result**

```python
assert extraction.extraction_path == cache_dir / "x" / download.sha256[:16]
assert len(extraction.extraction_path.name) == 16
assert extraction.geopackage_path.is_file()
```

**Regression protected**

Locks `default extraction path is short and content addressed` through the exact asserted conditions: `extraction.extraction_path == cache_dir / 'x' / download.sha256[:16]`; `len(extraction.extraction_path.name) == 16`; `extraction.geopackage_path.is_file()`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_default_extraction_path_is_short_and_content_addressed(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    cache_dir = tmp_path / "cache"
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, cache_dir)

    extraction = extract_ign_bdtopo_archive(download, config)

    assert extraction.extraction_path == cache_dir / "x" / download.sha256[:16]
    assert len(extraction.extraction_path.name) == 16
    assert extraction.geopackage_path.is_file()
```

### `test_layer_loader_retains_crs_counts_and_null_geometries`

**Purpose**

Exercises `layer loader retains crs counts and null geometries`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "bdtopo.gpkg"
_write_gpkg(gpkg_path)
frame = loaded.data
summary = loaded.summary
```

**Action**

```python
loaded = load_ign_bdtopo_layer(
        gpkg_path,
        LINE_LAYER,
        "electric_lines",
    )
```

**Expected result**

```python
assert frame.crs is not None
assert frame.crs.to_epsg() == 2154
assert len(frame) == 2
assert frame["object_id"].tolist() == ["L_VALID", "L_NULL"]
assert frame.geometry.isna().sum() == 1
assert summary.feature_count == 2
assert summary.null_geometry_count == 1
assert summary.invalid_geometry_count == 0
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_layer_loader_retains_crs_counts_and_null_geometries(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path)

    loaded = load_ign_bdtopo_layer(
        gpkg_path,
        LINE_LAYER,
        "electric_lines",
    )
    frame = loaded.data
    summary = loaded.summary

    assert frame.crs is not None
    assert frame.crs.to_epsg() == 2154
    assert len(frame) == 2
    assert frame["object_id"].tolist() == ["L_VALID", "L_NULL"]
    assert frame.geometry.isna().sum() == 1
    assert summary.feature_count == 2
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 0
```

### `test_invalid_geometry_is_preserved_without_repair`

**Purpose**

Exercises `invalid geometry is preserved without repair`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "bdtopo.gpkg"
_write_gpkg(gpkg_path, invalid_post=True)
frame = loaded.data
summary = loaded.summary
invalid_row = frame.loc[frame["object_id"] == "P_INVALID"].iloc[0]
```

**Action**

```python
loaded = load_ign_bdtopo_layer(
        gpkg_path,
        POST_LAYER,
        "transformation_posts",
    )
```

**Expected result**

```python
assert len(frame) == 3
assert invalid_row.geometry.is_valid is False
assert summary.feature_count == 3
assert summary.null_geometry_count == 1
assert summary.invalid_geometry_count == 1
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_geometry_is_preserved_without_repair(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "bdtopo.gpkg"
    _write_gpkg(gpkg_path, invalid_post=True)

    loaded = load_ign_bdtopo_layer(
        gpkg_path,
        POST_LAYER,
        "transformation_posts",
    )
    frame = loaded.data
    summary = loaded.summary

    invalid_row = frame.loc[frame["object_id"] == "P_INVALID"].iloc[0]
    assert len(frame) == 3
    assert invalid_row.geometry.is_valid is False
    assert summary.feature_count == 3
    assert summary.null_geometry_count == 1
    assert summary.invalid_geometry_count == 1
```

### `test_geographic_crs_is_rejected`

**Purpose**

Exercises `geographic crs is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "geographic.gpkg"
_write_gpkg(gpkg_path, include_posts=False, crs="EPSG:4326")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        load_ign_bdtopo_layer(gpkg_path, LINE_LAYER, "electric_lines")
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_geographic_crs_is_rejected(tmp_path: Path) -> None:
    gpkg_path = tmp_path / "geographic.gpkg"
    _write_gpkg(gpkg_path, include_posts=False, crs="EPSG:4326")

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        load_ign_bdtopo_layer(gpkg_path, LINE_LAYER, "electric_lines")
```

### `test_electricity_loader_retains_both_layer_counts`

**Purpose**

Exercises `electricity loader retains both layer counts`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(
        tmp_path / "source", invalid_post=True
    )
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
electricity = load_ign_bdtopo_electricity(extraction, config)
```

**Expected result**

```python
assert len(electricity.electric_lines) == 2
assert len(electricity.transformation_posts) == 3
assert electricity.electric_lines.crs.to_epsg() == 2154
assert electricity.transformation_posts.crs.to_epsg() == 2154
assert electricity.transformation_posts_summary.invalid_geometry_count == 1
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_electricity_loader_retains_both_layer_counts(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source", invalid_post=True
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 3
    assert electricity.electric_lines.crs.to_epsg() == 2154
    assert electricity.transformation_posts.crs.to_epsg() == 2154
    assert electricity.transformation_posts_summary.invalid_geometry_count == 1
```

### `test_road_layer_discovery_loads_selected_physical_layer`

**Purpose**

Exercises `road layer discovery loads selected physical layer`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
config = _synthetic_config(source_config)
loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
```

**Expected result**

```python
assert loaded.extraction is extraction
assert loaded.road_segments_summary.source_layer_name == ROAD_LAYER
assert loaded.road_segments_summary.logical_name == "road_segments"
assert loaded.road_segments["object_id"].tolist() == ["R_LINE", "R_MULTI"]
assert loaded.road_segments_summary.spatial_role == "PROXY_GEOMETRY"
```

**Regression protected**

Locks `road layer discovery loads selected physical layer` through the exact asserted conditions: `loaded.extraction is extraction`; `loaded.road_segments_summary.source_layer_name == ROAD_LAYER`; `loaded.road_segments_summary.logical_name == 'road_segments'`; `loaded.road_segments['object_id'].tolist() == ['R_LINE', 'R_MULTI']`; plus 1 additional reproduced assertion(s).

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_road_layer_discovery_loads_selected_physical_layer(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert loaded.extraction is extraction
    assert loaded.road_segments_summary.source_layer_name == ROAD_LAYER
    assert loaded.road_segments_summary.logical_name == "road_segments"
    assert loaded.road_segments["object_id"].tolist() == ["R_LINE", "R_MULTI"]
    assert loaded.road_segments_summary.spatial_role == "PROXY_GEOMETRY"
```

### `test_road_physical_layer_cannot_collide_with_electricity_roles`

**Purpose**

Exercises `road physical layer cannot collide with electricity roles`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `role`.

**Setup**

```python
config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
content = config.model_dump(mode="json")
selected = content["logical_layers"][role]
content["access"]["road_segments"] = selected
colliding = IgnBdTopoSourceConfig.model_validate(content)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="same layer|collid|role"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, colliding)
```

**Regression protected**

Locks `road physical layer cannot collide with electricity roles`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_road_physical_layer_cannot_collide_with_electricity_roles(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    role: str,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    content = config.model_dump(mode="json")
    selected = content["logical_layers"][role]
    content["access"]["road_segments"] = selected
    colliding = IgnBdTopoSourceConfig.model_validate(content)

    with pytest.raises(IgnBdTopoLayerError, match="same layer|collid|role"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, colliding)
```

### `test_missing_road_layer_fails_safely`

**Purpose**

Exercises `missing road layer fails safely`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source")
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="road|route|found 0"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Regression protected**

Locks `missing road layer fails safely`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_missing_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 0"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

### `test_ambiguous_road_layer_fails_safely`

**Purpose**

Exercises `ambiguous road layer fails safely`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "source" / "ambiguous-roads.gpkg"
_write_gpkg(gpkg_path, include_roads=True)
secondary = gpd.GeoDataFrame(
        {"object_id": ["R_SECONDARY"]},
        geometry=[LineString([(0, 0), (10, 10)])],
        crs="EPSG:2154",
    )
pyogrio.write_dataframe(
        secondary,
        gpkg_path,
        layer="TRONCON_DE_ROUTE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
archive_content = _pack_7z(
        tmp_path / "ambiguous-roads.7z",
        [(gpkg_path, "PACKAGE/ambiguous-roads.gpkg")],
    )
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="road|route|found 2"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_ambiguous_road_layer_fails_safely(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous-roads.gpkg"
    _write_gpkg(gpkg_path, include_roads=True)
    secondary = gpd.GeoDataFrame(
        {"object_id": ["R_SECONDARY"]},
        geometry=[LineString([(0, 0), (10, 10)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        secondary,
        gpkg_path,
        layer="TRONCON_DE_ROUTE_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous-roads.7z",
        [(gpkg_path, "PACKAGE/ambiguous-roads.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="road|route|found 2"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

### `test_road_loader_rejects_wrong_archive_config_department`

**Purpose**

Exercises `road loader rejects wrong archive config department`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
config = _synthetic_config(source_config)
other_department = IgnBdTopoSourceConfig.model_validate(
        {**config.model_dump(mode="json"), "department_code": "32"}
    )
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="department|archive|lineage"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, other_department)
```

**Regression protected**

Locks `road loader rejects wrong archive config department`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_road_loader_rejects_wrong_archive_config_department(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    other_department = IgnBdTopoSourceConfig.model_validate(
        {**config.model_dump(mode="json"), "department_code": "32"}
    )

    with pytest.raises(IgnBdTopoLayerError, match="department|archive|lineage"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, other_department)
```

### `test_road_loader_rejects_changed_layer_inventory`

**Purpose**

Exercises `road loader rejects changed layer inventory`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
config = _synthetic_config(source_config)
added = gpd.GeoDataFrame(
        {"object_id": ["ADDED"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
pyogrio.write_dataframe(
        added,
        extraction.geopackage_path,
        layer="ADDED_AFTER_EXTRACTION",
        driver="GPKG",
        append=True,
    )
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="inventory|changed"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_road_loader_rejects_changed_layer_inventory(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    added = gpd.GeoDataFrame(
        {"object_id": ["ADDED"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        added,
        extraction.geopackage_path,
        layer="ADDED_AFTER_EXTRACTION",
        driver="GPKG",
        append=True,
    )

    with pytest.raises(IgnBdTopoLayerError, match="inventory|changed"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

### `test_road_loader_rejects_geographic_crs`

**Purpose**

Exercises `road loader rejects geographic crs`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(
        tmp_path / "source", include_roads=True, road_crs="EPSG:4326"
    )
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_road_loader_rejects_geographic_crs(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source", include_roads=True, road_crs="EPSG:4326"
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    with pytest.raises(IgnBdTopoLayerError, match="2154|Lambert|projected|CRS"):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

### `test_road_loader_preserves_lambert93_lines_unchanged`

**Purpose**

Exercises `road loader preserves lambert93 lines unchanged`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `expected_geometry_type`, `road_geometry_kind`.

**Setup**

```python
archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=True,
        road_geometry_kind=road_geometry_kind,
    )
config = _synthetic_config(source_config)
expected = gpd.read_file(
        extraction.geopackage_path, layer=ROAD_LAYER, engine="pyogrio"
    )
loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
assert_geodataframe_equal(loaded.road_segments, expected, check_crs=True)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
```

**Expected result**

```python
assert loaded.road_segments.crs.to_epsg() == 2154
assert loaded.road_segments_summary.geometry_types == (expected_geometry_type,)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_road_loader_preserves_lambert93_lines_unchanged(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    road_geometry_kind: str,
    expected_geometry_type: str,
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_roads=True,
        road_geometry_kind=road_geometry_kind,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
    expected = gpd.read_file(
        extraction.geopackage_path, layer=ROAD_LAYER, engine="pyogrio"
    )

    loaded = ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)

    assert_geodataframe_equal(loaded.road_segments, expected, check_crs=True)
    assert loaded.road_segments.crs.to_epsg() == 2154
    assert loaded.road_segments_summary.geometry_types == (expected_geometry_type,)
```

### `test_road_layer_does_not_change_electricity_loading_or_cache_shape`

**Purpose**

Exercises `road layer does not change electricity loading or cache shape`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
config = _synthetic_config(source_config)
metadata = json.loads(
        (extraction.extraction_path / ".landscout-extraction.json").read_text(
            encoding="utf-8"
        )
    )
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )
electricity = load_ign_bdtopo_electricity(extraction, config)
```

**Expected result**

```python
assert len(electricity.electric_lines) == 2
assert len(electricity.transformation_posts) == 2
assert electricity.electric_lines_summary.source_layer_name == LINE_LAYER
assert electricity.transformation_posts_summary.source_layer_name == POST_LAYER
assert "road_segments_layer" not in metadata
assert set(metadata) == {
        "schema_version",
        "archive_sha256",
        "geopackage_relative_path",
        "geopackage_size_bytes",
        "geopackage_sha256",
        "all_layer_names",
        "electric_lines_layer",
        "transformation_posts_layer",
        "spatial_role",
    }
```

**Regression protected**

Locks `road layer does not change electricity loading or cache shape` through the exact asserted conditions: `len(electricity.electric_lines) == 2`; `len(electricity.transformation_posts) == 2`; `electricity.electric_lines_summary.source_layer_name == LINE_LAYER`; `electricity.transformation_posts_summary.source_layer_name == POST_LAYER`; plus 2 additional reproduced assertion(s).

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_road_layer_does_not_change_electricity_loading_or_cache_shape(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source", include_roads=True)
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=tmp_path / "extracted"
    )

    electricity = load_ign_bdtopo_electricity(extraction, config)
    metadata = json.loads(
        (extraction.extraction_path / ".landscout-extraction.json").read_text(
            encoding="utf-8"
        )
    )

    assert len(electricity.electric_lines) == 2
    assert len(electricity.transformation_posts) == 2
    assert electricity.electric_lines_summary.source_layer_name == LINE_LAYER
    assert electricity.transformation_posts_summary.source_layer_name == POST_LAYER
    assert "road_segments_layer" not in metadata
    assert set(metadata) == {
        "schema_version",
        "archive_sha256",
        "geopackage_relative_path",
        "geopackage_size_bytes",
        "geopackage_sha256",
        "all_layer_names",
        "electric_lines_layer",
        "transformation_posts_layer",
        "spatial_role",
    }
```

### `test_public_sources_export_only_stable_road_api`

**Purpose**

Exercises `public sources export only stable road api`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
assert sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData
assert sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads
assert "IgnBdTopoRoadData" in sources.__all__
assert "load_ign_bdtopo_roads" in sources.__all__
assert not hasattr(sources, "_discover_road_layer")
```

**Regression protected**

Locks `public sources export only stable road api` through the exact asserted conditions: `sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData`; `sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads`; `'IgnBdTopoRoadData' in sources.__all__`; `'load_ign_bdtopo_roads' in sources.__all__`; plus 1 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_sources_export_only_stable_road_api() -> None:
    assert sources.IgnBdTopoRoadData is ign_bdtopo_fr.IgnBdTopoRoadData
    assert sources.load_ign_bdtopo_roads is ign_bdtopo_fr.load_ign_bdtopo_roads
    assert "IgnBdTopoRoadData" in sources.__all__
    assert "load_ign_bdtopo_roads" in sources.__all__
    assert not hasattr(sources, "_discover_road_layer")
```

### `test_department_coverage_loader_selects_configured_identity`

**Purpose**

Exercises `department coverage loader selects configured identity`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
loaded = load_ign_bdtopo_department_coverage(extraction, config)
```

**Expected result**

```python
assert loaded.source_layer == DEPARTMENT_LAYER
assert loaded.source_department_code == "31"
assert loaded.spatial_role == "SOURCE_COVERAGE_BOUNDARY"
assert len(loaded.coverage) == 1
assert loaded.coverage.loc[0, "code_insee"] == "31"
assert loaded.coverage.loc[0, "source_department_code"] == "31"
assert loaded.coverage.loc[0, "source_archive_sha256"] == download.sha256
assert loaded.coverage.loc[0, "spatial_role"] == "SOURCE_COVERAGE_BOUNDARY"
assert loaded.coverage.crs.to_epsg() == 2154
assert loaded.summary.source_feature_count == 2
assert loaded.summary.selected_feature_count == 1
assert loaded.summary.department_code_field == "code_insee"
assert loaded.summary.geometry_types == ("MultiPolygon",)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_department_coverage_loader_selects_configured_identity(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    loaded = load_ign_bdtopo_department_coverage(extraction, config)

    assert loaded.source_layer == DEPARTMENT_LAYER
    assert loaded.source_department_code == "31"
    assert loaded.spatial_role == "SOURCE_COVERAGE_BOUNDARY"
    assert len(loaded.coverage) == 1
    assert loaded.coverage.loc[0, "code_insee"] == "31"
    assert loaded.coverage.loc[0, "source_department_code"] == "31"
    assert loaded.coverage.loc[0, "source_archive_sha256"] == download.sha256
    assert loaded.coverage.loc[0, "spatial_role"] == "SOURCE_COVERAGE_BOUNDARY"
    assert loaded.coverage.crs.to_epsg() == 2154
    assert loaded.summary.source_feature_count == 2
    assert loaded.summary.selected_feature_count == 1
    assert loaded.summary.department_code_field == "code_insee"
    assert loaded.summary.geometry_types == ("MultiPolygon",)
```

### `test_department_coverage_requires_one_authoritative_feature`

**Purpose**

Exercises `department coverage requires one authoritative feature`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `department_codes`.

**Setup**

```python
gpkg_path = tmp_path / "source" / "coverage.gpkg"
geometries = [
        Polygon([(0, 0), (0, 100), (100, 100), (100, 0), (0, 0)])
        for _ in department_codes
    ]
_write_gpkg(
        gpkg_path,
        include_department=True,
        department_codes=department_codes,
        department_geometries=geometries,
    )
archive_content = _pack_7z(
        tmp_path / "coverage.7z",
        [(gpkg_path, "PACKAGE/coverage.gpkg")],
    )
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="exactly one|found"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

**Regression protected**

Locks `department coverage requires one authoritative feature`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_department_coverage_requires_one_authoritative_feature(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    department_codes: list[str],
) -> None:
    gpkg_path = tmp_path / "source" / "coverage.gpkg"
    geometries = [
        Polygon([(0, 0), (0, 100), (100, 100), (100, 0), (0, 0)])
        for _ in department_codes
    ]
    _write_gpkg(
        gpkg_path,
        include_department=True,
        department_codes=department_codes,
        department_geometries=geometries,
    )
    archive_content = _pack_7z(
        tmp_path / "coverage.7z",
        [(gpkg_path, "PACKAGE/coverage.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="exactly one|found"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

### `test_department_coverage_requires_configured_identity_field`

**Purpose**

Exercises `department coverage requires configured identity field`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
content = _synthetic_config(source_config).model_dump(mode="json")
content["coverage"]["department_layer"]["department_code_field"] = (
        "missing_code"
    )
config = IgnBdTopoSourceConfig.model_validate(content)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="identity field|missing_code"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

**Regression protected**

Locks `department coverage requires configured identity field`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_department_coverage_requires_configured_identity_field(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(
        tmp_path / "source",
        include_department=True,
    )
    content = _synthetic_config(source_config).model_dump(mode="json")
    content["coverage"]["department_layer"]["department_code_field"] = (
        "missing_code"
    )
    config = IgnBdTopoSourceConfig.model_validate(content)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="identity field|missing_code"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

### `test_missing_department_coverage_layer_fails`

**Purpose**

Exercises `missing department coverage layer fails`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_content = _synthetic_archive_bytes(tmp_path / "source")
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="department|found 0"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

**Regression protected**

Locks `missing department coverage layer fails`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_missing_department_coverage_layer_fails(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    archive_content = _synthetic_archive_bytes(tmp_path / "source")
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="department|found 0"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

### `test_department_coverage_layer_discovery_must_be_unambiguous`

**Purpose**

Exercises `department coverage layer discovery must be unambiguous`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
gpkg_path = tmp_path / "source" / "ambiguous.gpkg"
_write_gpkg(gpkg_path, include_department=True)
second = gpd.GeoDataFrame(
        {"code_insee": ["31"]},
        geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])],
        crs="EPSG:2154",
    )
pyogrio.write_dataframe(
        second,
        gpkg_path,
        layer="DEPARTEMENT_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
archive_content = _pack_7z(
        tmp_path / "ambiguous.7z",
        [(gpkg_path, "PACKAGE/ambiguous.gpkg")],
    )
config = _synthetic_config(source_config)
```

**Action**

```python
with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )
```

**Expected result**

```python
with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_department_coverage_layer_discovery_must_be_unambiguous(
    tmp_path: Path, source_config: IgnBdTopoSourceConfig
) -> None:
    gpkg_path = tmp_path / "source" / "ambiguous.gpkg"
    _write_gpkg(gpkg_path, include_department=True)
    second = gpd.GeoDataFrame(
        {"code_insee": ["31"]},
        geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])],
        crs="EPSG:2154",
    )
    pyogrio.write_dataframe(
        second,
        gpkg_path,
        layer="DEPARTEMENT_SECONDAIRE",
        driver="GPKG",
        append=True,
    )
    archive_content = _pack_7z(
        tmp_path / "ambiguous.7z",
        [(gpkg_path, "PACKAGE/ambiguous.gpkg")],
    )
    config = _synthetic_config(source_config)
    with patch(
        "landscout.sources.ign_bdtopo_fr.open_safe_https",
        return_value=_response(archive_content),
    ):
        download = download_ign_bdtopo_archive(config, tmp_path / "cache")
    extraction = extract_ign_bdtopo_archive(
        download,
        config,
        extraction_dir=tmp_path / "extracted",
    )

    with pytest.raises(IgnBdTopoLayerError, match="unambiguous|found 2"):
        load_ign_bdtopo_department_coverage(extraction, config)
```

### `test_direct_consumers_reject_same_inventory_content_tampering`

**Purpose**

Exercises `direct consumers reject same inventory content tampering`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: `consumer`, `layer`, `new_bytes`, `old_bytes`.

**Setup**

```python
config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
size_before = extraction.geopackage_path.stat().st_size
content = extraction.geopackage_path.read_bytes()
extraction.geopackage_path.write_bytes(content.replace(old_bytes, new_bytes, 1))
```

**Action**

```python
if consumer == "coverage":
        # Rebuild once with the configured department layer present.
        archive_content = _synthetic_archive_bytes(
            tmp_path / "coverage-source",
            include_roads=True,
            include_department=True,
        )
        with patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ):
            download = download_ign_bdtopo_archive(config, tmp_path / "coverage-cache")
        extraction = extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "coverage-extracted",
        )
```

**Expected result**

```python
assert old_bytes in content
assert extraction.geopackage_path.stat().st_size == size_before
with pytest.raises(IgnBdTopoLayerError, match="integrity|SHA|physical|changed"):
        if consumer == "electricity":
            load_ign_bdtopo_electricity(extraction, config)
        elif consumer == "roads":
            ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
        else:
            load_ign_bdtopo_department_coverage(extraction, config)
```

**Regression protected**

Locks `direct consumers reject same inventory content tampering`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Network behavior is fake/blocked and does not contact the live source.

**Complete test implementation**

```python
def test_direct_consumers_reject_same_inventory_content_tampering(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
    consumer: str,
    layer: str,
    old_bytes: bytes,
    new_bytes: bytes,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    if consumer == "coverage":
        # Rebuild once with the configured department layer present.
        archive_content = _synthetic_archive_bytes(
            tmp_path / "coverage-source",
            include_roads=True,
            include_department=True,
        )
        with patch(
            "landscout.sources.ign_bdtopo_fr.open_safe_https",
            return_value=_response(archive_content),
        ):
            download = download_ign_bdtopo_archive(config, tmp_path / "coverage-cache")
        extraction = extract_ign_bdtopo_archive(
            download,
            config,
            extraction_dir=tmp_path / "coverage-extracted",
        )

    size_before = extraction.geopackage_path.stat().st_size
    content = extraction.geopackage_path.read_bytes()
    assert old_bytes in content
    extraction.geopackage_path.write_bytes(content.replace(old_bytes, new_bytes, 1))
    assert extraction.geopackage_path.stat().st_size == size_before

    with pytest.raises(IgnBdTopoLayerError, match="integrity|SHA|physical|changed"):
        if consumer == "electricity":
            load_ign_bdtopo_electricity(extraction, config)
        elif consumer == "roads":
            ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
        else:
            load_ign_bdtopo_department_coverage(extraction, config)
```

### `test_road_loader_rejects_source_change_after_physical_read`

**Purpose**

Exercises `road loader rejects source change after physical read`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `source_config` (local fixture, scope `function`).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
original_read = ign_bdtopo_fr.gpd.read_file
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        content = extraction.geopackage_path.read_bytes()
        extraction.geopackage_path.write_bytes(
            content.replace(b"Bretelle", b"BretellX", 1)
        )
        return frame
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with (
        patch.object(ign_bdtopo_fr.gpd, "read_file", side_effect=mutate_after_read),
        pytest.raises(IgnBdTopoLayerError, match="changed|integrity|SHA"),
    ):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

**Regression protected**

Locks `road loader rejects source change after physical read`: the reproduced adversarial input must raise `IgnBdTopoLayerError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_road_loader_rejects_source_change_after_physical_read(
    tmp_path: Path,
    source_config: IgnBdTopoSourceConfig,
) -> None:
    config, _, extraction = _extracted_fixture(
        tmp_path,
        source_config,
        include_roads=True,
    )
    original_read = ign_bdtopo_fr.gpd.read_file

    def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        content = extraction.geopackage_path.read_bytes()
        extraction.geopackage_path.write_bytes(
            content.replace(b"Bretelle", b"BretellX", 1)
        )
        return frame

    with (
        patch.object(ign_bdtopo_fr.gpd, "read_file", side_effect=mutate_after_read),
        pytest.raises(IgnBdTopoLayerError, match="changed|integrity|SHA"),
    ):
        ign_bdtopo_fr.load_ign_bdtopo_roads(extraction, config)
```

### `test_road_loader_rejects_source_change_after_physical_read.mutate_after_read`

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
- Filesystem read: `extraction.geopackage_path.read_bytes`.
- Filesystem write: `extraction.geopackage_path.write_bytes`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_rejects_source_change_after_physical_read` via `patch.object(ign_bdtopo_fr.gpd, 'read_file', side_effect=mutate_after_read)`.

**Complete source-ordered implementation**

```python
def mutate_after_read(*args: object, **kwargs: object) -> gpd.GeoDataFrame:
        frame = original_read(*args, **kwargs)
        content = extraction.geopackage_path.read_bytes()
        extraction.geopackage_path.write_bytes(
            content.replace(b"Bretelle", b"BretellX", 1)
        )
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
