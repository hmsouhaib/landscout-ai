# `tests/unit/test_assess_road_proximity_coverage.py`

## File identity

- Repository path: `tests/unit/test_assess_road_proximity_coverage.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.
- Source SHA256: `c596dc762bf271879f6ca0361a2126147f9b251eb0710d1d6613ac6597a926c1`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for assess road proximity coverage; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError, replace`
- `from importlib import import_module`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `SOURCE_CONFIG`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARCHIVE_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARCHIVE_SHA256 = "a" * 64
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `GEOPACKAGE_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
GEOPACKAGE_SHA256 = "b" * 64
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EDITION`

- Category: module constant or closed domain.
- Exact declaration:

```python
EDITION = "2026-06-15"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ELIGIBLE_CLASSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ELIGIBLE_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "UNKNOWN_REVIEW",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `GENERAL_VEHICLE_PROXY`
  - `LIMITED_VEHICLE_PROXY`
  - `RESTRICTED_REVIEW`
  - `NOT_GENERAL_VEHICLE_PROXY`
  - `UNKNOWN_REVIEW`

### `ALL_CLASSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ALL_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "NOT_DISTANCE_PROXY",
    "UNKNOWN_REVIEW",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `GENERAL_VEHICLE_PROXY`
  - `LIMITED_VEHICLE_PROXY`
  - `RESTRICTED_REVIEW`
  - `NOT_GENERAL_VEHICLE_PROXY`
  - `NOT_DISTANCE_PROXY`
  - `UNKNOWN_REVIEW`

### `DIAGNOSTIC_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    "road_source_coverage_provider",
    "road_source_coverage_product",
    "road_source_coverage_department_code",
    "road_source_coverage_edition",
    "road_source_coverage_product_version",
    "road_source_coverage_archive_sha256",
    "road_source_coverage_layer",
    "road_source_coverage_spatial_role",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `road_source_boundary_distance_m`
  - `road_source_coverage_position`
  - `road_proximity_coverage_status`
  - `road_source_coverage_provider`
  - `road_source_coverage_product`
  - `road_source_coverage_department_code`
  - `road_source_coverage_edition`
  - `road_source_coverage_product_version`
  - `road_source_coverage_archive_sha256`
  - `road_source_coverage_layer`
  - `road_source_coverage_spatial_role`

### `SELECTED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
SELECTED_COLUMNS = (
    "nearest_road_proxy_distance_m",
    "nearest_road_feature_id",
    "nearest_source_feature_id",
    "nearest_road_tie_count",
    "nearest_road_primary_rule",
    "nearest_road_rule_trace_json",
    "nearest_road_unknown_fields_json",
    "nearest_road_toll_evidence",
    "nearest_nature_raw",
    "nearest_importance_raw",
    "nearest_asset_status_raw",
    "nearest_private_raw",
    "nearest_light_vehicle_access_raw",
    "nearest_carriageway_width_raw",
    "nearest_closure_period_raw",
    "nearest_restriction_nature_raw",
    "nearest_source_layer",
    "nearest_source_department_code",
    "nearest_source_edition",
    "nearest_source_archive_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `nearest_road_proxy_distance_m`
  - `nearest_road_feature_id`
  - `nearest_source_feature_id`
  - `nearest_road_tie_count`
  - `nearest_road_primary_rule`
  - `nearest_road_rule_trace_json`
  - `nearest_road_unknown_fields_json`
  - `nearest_road_toll_evidence`
  - `nearest_nature_raw`
  - `nearest_importance_raw`
  - `nearest_asset_status_raw`
  - `nearest_private_raw`
  - `nearest_light_vehicle_access_raw`
  - `nearest_carriageway_width_raw`
  - `nearest_closure_period_raw`
  - `nearest_restriction_nature_raw`
  - `nearest_source_layer`
  - `nearest_source_department_code`
  - `nearest_source_edition`
  - `nearest_source_archive_sha256`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_archive`

**Purpose:** Implements `archive` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _archive() -> IgnBdTopoDownload:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDownload`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoDownload(<br>        provider=SOURCE_CONFIG.provider,<br>        product=SOURCE_CONFIG.product,<br>        department_code="31",<br>        edition=EDITION,<br>        product_version="3.5",<br>        projection="EPSG:2154",<br>        package_format="GPKG",<br>        archive_format="7z",<br>        source_url=str(SOURCE_CONFIG.source_url),<br>        checksum_url=None,<br>        download_timestamp="2026-08-11T15:32:03+00:00",<br>        filename="BDTOPO.7z",<br>        file_size=123,<br>        sha256=ARCHIVE_SHA256,<br>        official_checksum_algorithm=None,<br>        official_checksum=None,<br>        official_checksum_validated=False,<br>        path=Path("synthetic/BDTOPO.7z"),<br>        cache_hit=True,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::_extraction` via `_archive`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_extraction` via `_archive`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoDownload` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDownload` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _archive() -> IgnBdTopoDownload:
    return IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product=SOURCE_CONFIG.product,
        department_code="31",
        edition=EDITION,
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=str(SOURCE_CONFIG.source_url),
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO.7z",
        file_size=123,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("synthetic/BDTOPO.7z"),
        cache_hit=True,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_extraction`

**Purpose:** Implements `extraction` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _extraction() -> IgnBdTopoExtraction:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoExtraction`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoExtraction(<br>        archive=_archive(),<br>        extraction_path=Path("synthetic/extracted"),<br>        geopackage_path=Path("synthetic/extracted/data.gpkg"),<br>        geopackage_filename="data.gpkg",<br>        geopackage_size_bytes=456,<br>        geopackage_sha256=GEOPACKAGE_SHA256,<br>        all_layer_names=(<br>            "ligne_electrique",<br>            "poste_de_transformation",<br>            "troncon_de_route",<br>            "departement",<br>            "zone_administrative",<br>        ),<br>        electric_lines_layer="ligne_electrique",<br>        transformation_posts_layer="poste_de_transformation",<br>        road_segments_layer="troncon_de_route",<br>        department_layer="departement",<br>        cache_hit=True,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::_road_source` via `_extraction`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_road_source` via `_extraction`
- direct call: `tests.unit.test_assess_road_proximity_coverage::_coverage` via `_extraction`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_coverage` via `_extraction`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoExtraction` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoExtraction` |
| `_archive` | `tests.unit.test_assess_road_proximity_coverage._archive` |
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
def _extraction() -> IgnBdTopoExtraction:
    return IgnBdTopoExtraction(
        archive=_archive(),
        extraction_path=Path("synthetic/extracted"),
        geopackage_path=Path("synthetic/extracted/data.gpkg"),
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=456,
        geopackage_sha256=GEOPACKAGE_SHA256,
        all_layer_names=(
            "ligne_electrique",
            "poste_de_transformation",
            "troncon_de_route",
            "departement",
            "zone_administrative",
        ),
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        road_segments_layer="troncon_de_route",
        department_layer="departement",
        cache_hit=True,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_road_source`

**Purpose:** Implements `road source` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _road_source(
    extraction: IgnBdTopoExtraction | None = None,
) -> IgnBdTopoRoadData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoRoadData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `IgnBdTopoExtraction \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoRoadData(package, roads, summary)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_wrong_public_input_type_is_controlled_and_fast` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_wrong_public_input_type_is_controlled_and_fast` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_proximity_failure_stops_coverage_loading` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_proximity_failure_stops_coverage_loading` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_package_lineage_must_match_road_archive` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_package_lineage_must_match_road_archive` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_must_retain_same_extraction_object` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_must_retain_same_extraction_object` via `_road_source`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_road_source`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_road_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction` | `tests.unit.test_assess_road_proximity_coverage._extraction` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `LineString` | `shapely.geometry.LineString` |
| `IgnBdTopoLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoLayerSummary` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoRoadData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` |

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
def _road_source(
    extraction: IgnBdTopoExtraction | None = None,
) -> IgnBdTopoRoadData:
    package = extraction or _extraction()
    roads = gpd.GeoDataFrame(
        {"cleabs": ["ROAD-1"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    summary = IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name="troncon_de_route",
        crs="EPSG:2154",
        feature_count=1,
        columns=tuple(str(column) for column in roads.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in roads.dtypes.items()
        ),
        null_geometry_count=0,
        empty_geometry_count=0,
        invalid_geometry_count=0,
        geometry_types=("LineString",),
    )
    return IgnBdTopoRoadData(package, roads, summary)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_coverage`

**Purpose:** Implements `coverage` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _coverage(
    extraction: IgnBdTopoExtraction | None = None,
    *,
    geometries: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    layer: str = "departement",
    department_code: str = "31",
    provider: str | None = None,
    product: str | None = None,
    edition: str = EDITION,
    product_version: str | None = "3.5",
    archive_sha256: str = ARCHIVE_SHA256,
) -> IgnBdTopoDepartmentCoverage:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoDepartmentCoverage`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `extraction` | positional-or-keyword | `IgnBdTopoExtraction \| None` | `None` |
| `geometries` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `layer` | keyword-only | `str` | `'departement'` |
| `department_code` | keyword-only | `str` | `'31'` |
| `provider` | keyword-only | `str \| None` | `None` |
| `product` | keyword-only | `str \| None` | `None` |
| `edition` | keyword-only | `str` | `EDITION` |
| `product_version` | keyword-only | `str \| None` | `'3.5'` |
| `archive_sha256` | keyword-only | `str` | `ARCHIVE_SHA256` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoDepartmentCoverage(<br>        extraction=package,<br>        coverage=selected,<br>        summary=summary,<br>        source_provider=cast(str, lineage["source_provider"]),<br>        source_product=cast(str, lineage["source_product"]),<br>        source_department_code=department_code,<br>        source_edition=edition,<br>        source_product_version=product_version,<br>        source_archive_sha256=archive_sha256,<br>        source_layer=layer,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_package_lineage_must_match_road_archive` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_package_lineage_must_match_road_archive` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_selected_department_identity_is_exact` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_selected_department_identity_is_exact` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_must_retain_same_extraction_object` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_must_retain_same_extraction_object` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_invalid_coverage_geometry_is_rejected` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_invalid_coverage_geometry_is_rejected` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_polygonal_coverage_geometry_is_accepted` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_polygonal_coverage_geometry_is_accepted` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_exact_coverage_lineage_is_appended_to_every_row` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_exact_coverage_lineage_is_appended_to_every_row` via `_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_extraction` | `tests.unit.test_assess_road_proximity_coverage._extraction` |
| `Polygon` | `shapely.geometry.Polygon` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `lineage.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoCoverageLayerSummary` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoCoverageLayerSummary` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `raw.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null & geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_empty & ~geometry.is_valid).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoDepartmentCoverage` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoDepartmentCoverage` |
| `cast` | `typing.cast` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry.isna().sum`<br>`(non_null & geometry.is_empty).sum`<br>`(non_empty & ~geometry.is_valid).sum`<br>`geometry.geom_type.dropna().unique`<br>`geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | `selected[column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _coverage(
    extraction: IgnBdTopoExtraction | None = None,
    *,
    geometries: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    layer: str = "departement",
    department_code: str = "31",
    provider: str | None = None,
    product: str | None = None,
    edition: str = EDITION,
    product_version: str | None = "3.5",
    archive_sha256: str = ARCHIVE_SHA256,
) -> IgnBdTopoDepartmentCoverage:
    package = extraction or _extraction()
    values = geometries
    if values is None:
        values = [Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]
    raw = gpd.GeoDataFrame(
        {
            "code_insee": [department_code] * len(values),
            "nom_officiel": [
                f"Department {position}" for position in range(len(values))
            ],
        },
        geometry=values,
        crs=crs,
    )
    lineage = {
        "source_provider": provider or package.archive.provider,
        "source_product": product or package.archive.product,
        "source_department_code": department_code,
        "source_edition": edition,
        "source_product_version": product_version,
        "source_archive_sha256": archive_sha256,
        "source_layer": layer,
        "spatial_role": "SOURCE_COVERAGE_BOUNDARY",
    }
    selected = raw.copy()
    for column, value in lineage.items():
        selected[column] = value
    geometry = raw.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name=layer,
        crs="" if crs is None else str(raw.crs),
        source_feature_count=len(raw),
        selected_feature_count=len(raw),
        columns=tuple(str(column) for column in raw.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in raw.dtypes.items()),
        null_geometry_count=int(geometry.isna().sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
        geometry_types=tuple(
            sorted(str(value) for value in geometry.geom_type.dropna().unique())
        ),
        department_code_field="code_insee",
        selected_department_code=department_code,
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=package,
        coverage=selected,
        summary=summary,
        source_provider=cast(str, lineage["source_provider"]),
        source_product=cast(str, lineage["source_product"]),
        source_department_code=department_code,
        source_edition=edition,
        source_product_version=product_version,
        source_archive_sha256=archive_sha256,
        source_layer=layer,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_metric_parcels`

**Purpose:** Implements `metric parcels` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[str] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {"parcel_id": ids, "preserved_value": list(range(len(values)))},<br>        geometry=values,<br>        crs="EPSG:2154",<br>        index=[20 + position for position in range(len(values))],<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::_parcels` via `_metric_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_parcels` via `_metric_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])
    ]
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(len(values))]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "preserved_value": list(range(len(values)))},
        geometry=values,
        crs="EPSG:2154",
        index=[20 + position for position in range(len(values))],
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[str] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_metric_parcels(geometries, identifiers=identifiers).to_crs("EPSG:4326")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_wrong_public_input_type_is_controlled_and_fast` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_wrong_public_input_type_is_controlled_and_fast` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_proximity_failure_stops_coverage_loading` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_proximity_failure_stops_coverage_loading` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_matched_outside_or_crossing_status` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_matched_outside_or_crossing_status` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::_corrupt_generated` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_corrupt_generated` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_inconsistent_generated_status_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_inconsistent_generated_status_is_rejected` via `_parcels`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_result_is_frozen_and_has_no_business_decision_fields` via `_parcels`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_is_frozen_and_has_no_business_decision_fields` via `_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_metric_parcels(geometries, identifiers=identifiers).to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metric_parcels` | `tests.unit.test_assess_road_proximity_coverage._metric_parcels` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_metric_parcels(geometries, identifiers=identifiers).to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(geometries, identifiers=identifiers).to_crs("EPSG:4326")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_proximity`

**Purpose:** Implements `proximity` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _proximity(
    parcels: gpd.GeoDataFrame | None = None,
    *,
    distances: dict[str, float] | None = None,
) -> ParcelRoadProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelRoadProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `distances` | keyword-only | `dict[str, float] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `ParcelRoadProximityResult(source_parcels.copy(), table, coverage)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_matched_outside_or_crossing_status` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_matched_outside_or_crossing_status` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_matched_road_lineage_must_match_coverage` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_matched_road_lineage_must_match_coverage` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::_corrupt_generated` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_corrupt_generated` via `_proximity`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_inconsistent_generated_status_is_rejected` via `_proximity`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_inconsistent_generated_status_is_rejected` via `_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `configured_distances.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `table[<br>        "nearest_road_proxy_distance_m"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["nearest_road_tie_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["nearest_road_toll_evidence"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProxyClassCoverage` | `landscout.stages.enrich_road_proximity.RoadProxyClassCoverage` |
| `ParcelRoadProximityResult` | `landscout.stages.enrich_road_proximity.ParcelRoadProximityResult` |
| `source_parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `configured_distances.get`<br>`table[<br>        "nearest_road_proxy_distance_m"<br>    ].astype` |
| External process/environment | None directly present. |
| In-memory mutation | `rows.append(<br>                {<br>                    "parcel_id": parcel_id,<br>                    "road_proxy_class": road_class,<br>                    "nearest_road_proxy_distance_m": distance_m,<br>                    "nearest_road_feature_id": f"ROAD-{road_class}",<br>                    "nearest_source_feature_id": f"SOURCE-{road_class}",<br>                    "nearest_road_tie_count": 1,<br>                    "nearest_road_primary_rule": primary_rule,<br>                    "nearest_road_rule_trace_json": f'["{primary_rule}"]',<br>                    "nearest_road_unknown_fields_json": "[]",<br>                    "nearest_road_toll_evidence": False,<br>                    "nearest_nature_raw": "Route à 1 chaussée",<br>                    "nearest_importance_raw": "2",<br>                    "nearest_asset_status_raw": "En service",<br>                    "nearest_private_raw": 0.0,<br>                    "nearest_light_vehicle_access_raw": "Libre",<br>                    "nearest_carriageway_width_raw": 7.0,<br>                    "nearest_closure_period_raw": None,<br>                    "nearest_restriction_nature_raw": None,<br>                    "nearest_source_layer": "troncon_de_route",<br>                    "nearest_source_department_code": "31",<br>                    "nearest_source_edition": EDITION,<br>                    "nearest_source_archive_sha256": ARCHIVE_SHA256,<br>                    "road_proxy_policy_id": policy.policy_id,<br>                    "road_proxy_policy_schema_version": policy.schema_version,<br>                    "road_proxy_policy_config_sha256": policy.config_sha256,<br>                    "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,<br>                    "proximity_scope": "WITHIN_VERIFIED_SOURCE_PACKAGE",<br>                }<br>            )`<br>`table["nearest_road_proxy_distance_m"] = table[<br>        "nearest_road_proxy_distance_m"<br>    ].astype("float64")`<br>`table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")`<br>`table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(<br>        "boolean"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _proximity(
    parcels: gpd.GeoDataFrame | None = None,
    *,
    distances: dict[str, float] | None = None,
) -> ParcelRoadProximityResult:
    source_parcels = parcels if parcels is not None else _parcels()
    policy = load_ign_road_vehicle_proxy_policy()
    configured_distances = distances or {}
    primary_rules = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }
    rows: list[dict[str, object]] = []
    for parcel_id in source_parcels["parcel_id"]:
        for position, road_class in enumerate(ELIGIBLE_CLASSES):
            distance_m = configured_distances.get(road_class, 50.0 + position)
            primary_rule = primary_rules[road_class]
            rows.append(
                {
                    "parcel_id": parcel_id,
                    "road_proxy_class": road_class,
                    "nearest_road_proxy_distance_m": distance_m,
                    "nearest_road_feature_id": f"ROAD-{road_class}",
                    "nearest_source_feature_id": f"SOURCE-{road_class}",
                    "nearest_road_tie_count": 1,
                    "nearest_road_primary_rule": primary_rule,
                    "nearest_road_rule_trace_json": f'["{primary_rule}"]',
                    "nearest_road_unknown_fields_json": "[]",
                    "nearest_road_toll_evidence": False,
                    "nearest_nature_raw": "Route à 1 chaussée",
                    "nearest_importance_raw": "2",
                    "nearest_asset_status_raw": "En service",
                    "nearest_private_raw": 0.0,
                    "nearest_light_vehicle_access_raw": "Libre",
                    "nearest_carriageway_width_raw": 7.0,
                    "nearest_closure_period_raw": None,
                    "nearest_restriction_nature_raw": None,
                    "nearest_source_layer": "troncon_de_route",
                    "nearest_source_department_code": "31",
                    "nearest_source_edition": EDITION,
                    "nearest_source_archive_sha256": ARCHIVE_SHA256,
                    "road_proxy_policy_id": policy.policy_id,
                    "road_proxy_policy_schema_version": policy.schema_version,
                    "road_proxy_policy_config_sha256": policy.config_sha256,
                    "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
                    "proximity_scope": "WITHIN_VERIFIED_SOURCE_PACKAGE",
                }
            )
    table = pd.DataFrame(rows, columns=CLASS_PROXIMITY_COLUMNS)
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")
    table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    coverage = tuple(
        RoadProxyClassCoverage(
            road_proxy_class=road_class,
            feature_count=1,
            distance_eligible=road_class != "NOT_DISTANCE_PROXY",
        )
        for road_class in ALL_CLASSES
    )
    return ParcelRoadProximityResult(source_parcels.copy(), table, coverage)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_without_match`

**Purpose:** Implements `without match` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _without_match(
    proximity: ParcelRoadProximityResult,
    road_class: str = "UNKNOWN_REVIEW",
) -> ParcelRoadProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelRoadProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `proximity` | positional-or-keyword | `ParcelRoadProximityResult` | `required` |
| `road_class` | positional-or-keyword | `str` | `'UNKNOWN_REVIEW'` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(proximity, class_proximity=table, class_coverage=coverage)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_without_match`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_without_match`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `proximity.class_proximity.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["road_proxy_class"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[<br>        "nearest_road_proxy_distance_m"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["nearest_road_tie_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["nearest_road_toll_evidence"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `table[<br>        "nearest_road_proxy_distance_m"<br>    ].astype` |
| External process/environment | None directly present. |
| In-memory mutation | `table.loc[mask, column] = pd.NA`<br>`table["nearest_road_proxy_distance_m"] = table[<br>        "nearest_road_proxy_distance_m"<br>    ].astype("float64")`<br>`table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")`<br>`table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(<br>        "boolean"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _without_match(
    proximity: ParcelRoadProximityResult,
    road_class: str = "UNKNOWN_REVIEW",
) -> ParcelRoadProximityResult:
    table = proximity.class_proximity.copy()
    mask = table["road_proxy_class"].eq(road_class)
    for column in SELECTED_COLUMNS:
        table.loc[mask, column] = pd.NA
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")
    table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    coverage = tuple(
        replace(item, feature_count=0) if item.road_proxy_class == road_class else item
        for item in proximity.class_coverage
    )
    return replace(proximity, class_proximity=table, class_coverage=coverage)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_measured_boundary_distance`

**Purpose:** Implements `measured boundary distance` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _measured_boundary_distance(
    parcels: gpd.GeoDataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> float:
```

- Exact decorators: none.
- Declared return annotation: `float`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_measured_boundary_distance`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_measured_boundary_distance`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_measured_boundary_distance`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_measured_boundary_distance`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_measured_boundary_distance`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_measured_boundary_distance`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.distance` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.to_crs`<br>`geometry.distance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _measured_boundary_distance(
    parcels: gpd.GeoDataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> float:
    geometry = parcels.to_crs("EPSG:2154").geometry.iloc[0]
    return float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_assess`

**Purpose:** Implements `assess` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _assess(
    *,
    parcels: gpd.GeoDataFrame | None = None,
    proximity: object | None = None,
    coverage: IgnBdTopoDepartmentCoverage | None = None,
    road_source: IgnBdTopoRoadData | None = None,
    source_config: IgnBdTopoSourceConfig = SOURCE_CONFIG,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
```

- Exact decorators: none.
- Declared return annotation: `RoadProximityCoverageAssessmentResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | keyword-only | `gpd.GeoDataFrame \| None` | `None` |
| `proximity` | keyword-only | `object \| None` | `None` |
| `coverage` | keyword-only | `IgnBdTopoDepartmentCoverage \| None` | `None` |
| `road_source` | keyword-only | `IgnBdTopoRoadData \| None` | `None` |
| `source_config` | keyword-only | `IgnBdTopoSourceConfig` | `SOURCE_CONFIG` |
| `policy_path` | keyword-only | `Path \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `assess_road_proximity_coverage(<br>            selected_parcels,<br>            selected_source,<br>            source_config,<br>            policy_path,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_stage_does_not_construct_a_road_spatial_index` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_stage_does_not_construct_a_road_spatial_index` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_package_lineage_must_match_road_archive` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_package_lineage_must_match_road_archive` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_selected_department_identity_is_exact` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_selected_department_identity_is_exact` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_must_retain_same_extraction_object` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_must_retain_same_extraction_object` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_invalid_coverage_geometry_is_rejected` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_invalid_coverage_geometry_is_rejected` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_polygonal_coverage_geometry_is_accepted` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_polygonal_coverage_geometry_is_accepted` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_strict_boundary_status_logic` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_matched_outside_or_crossing_status` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_matched_outside_or_crossing_status` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_exact_coverage_lineage_is_appended_to_every_row` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_exact_coverage_lineage_is_appended_to_every_row` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_matched_road_lineage_must_match_coverage` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_matched_road_lineage_must_match_coverage` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::_corrupt_generated` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_corrupt_generated` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_inconsistent_generated_status_is_rejected` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_inconsistent_generated_status_is_rejected` via `_assess`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_result_is_frozen_and_has_no_business_decision_fields` via `_assess`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_is_frozen_and_has_no_business_decision_fields` via `_assess`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
| `patch` | `unittest.mock.patch` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |

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
def _assess(
    *,
    parcels: gpd.GeoDataFrame | None = None,
    proximity: object | None = None,
    coverage: IgnBdTopoDepartmentCoverage | None = None,
    road_source: IgnBdTopoRoadData | None = None,
    source_config: IgnBdTopoSourceConfig = SOURCE_CONFIG,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
    selected_parcels = parcels if parcels is not None else _parcels()
    selected_proximity = (
        proximity if proximity is not None else _proximity(selected_parcels)
    )
    selected_coverage = coverage or _coverage()
    selected_source = road_source or _road_source(selected_coverage.extraction)
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=selected_proximity,
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=selected_coverage,
        ),
    ):
        return assess_road_proximity_coverage(
            selected_parcels,
            selected_source,
            source_config,
            policy_path,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_first_row`

**Purpose:** Implements `first row` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _first_row(
    result: RoadProximityCoverageAssessmentResult,
    road_class: str = "GENERAL_VEHICLE_PROXY",
) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `RoadProximityCoverageAssessmentResult` | `required` |
| `road_class` | positional-or-keyword | `str` | `'GENERAL_VEHICLE_PROXY'` |

**Return and exception contract**

- Exact observed return expressions:
  - `result.class_proximity.loc[<br>        result.class_proximity["road_proxy_class"].eq(road_class)<br>    ].iloc[0]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_first_row`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_full_parcel_coverage_position_is_conservative` via `_first_row`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_first_row`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_position_uses_full_geometry_not_centroid` via `_first_row`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_first_row`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_no_match_takes_precedence_over_coverage_position` via `_first_row`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_first_row`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_classes_are_diagnosed_independently` via `_first_row`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.class_proximity["road_proxy_class"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _first_row(
    result: RoadProximityCoverageAssessmentResult,
    road_class: str = "GENERAL_VEHICLE_PROXY",
) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_api_exports_only_stable_symbols`

**Purpose:** Regression invariant: public api exports only stable symbols. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_api_exports_only_stable_symbols() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(module.__all__) == expected`
  - `assert expected <= set(stages.__all__)`
  - `assert all(hasattr(stages, symbol) for symbol in expected)`
  - `assert not hasattr(stages, "_coverage_positions")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `import_module` | `importlib.import_module` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_api_exports_only_stable_symbols() -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    expected = {
        "RoadProximityCoverageError",
        "RoadProximityCoverageAssessmentResult",
        "assess_road_proximity_coverage",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_coverage_positions")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_public_input_type_is_controlled_and_fast`

**Purpose:** Regression invariant: wrong public input type is controlled and fast. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_public_input_type_is_controlled_and_fast(argument: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "argument", ["parcels", "road_source", "source_config", "policy_path"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `argument` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |
| `cast` | `typing.cast` |
| `proximity_stage.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `coverage_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_wrong_public_input_type_is_controlled_and_fast(argument: str) -> None:
    kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "road_source": _road_source(),
        "source_config": SOURCE_CONFIG,
        "policy_path": None,
    }
    kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity"
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(**cast(Any, kwargs))
    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_chain_calls_proximity_then_coverage_exactly_once`

**Purpose:** Regression invariant: source chain calls proximity then coverage exactly once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_chain_calls_proximity_then_coverage_exactly_once() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `Path` | `pathlib.Path` |
| `patch` | `unittest.mock.patch` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |
| `proximity_stage.assert_called_once_with` | `unresolved local/third-party receiver; no ownership inferred` |
| `coverage_loader.assert_called_once_with` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_source_chain_calls_proximity_then_coverage_exactly_once() -> None:
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity(parcels)
    policy_path = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=proximity,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=coverage,
        ) as coverage_loader,
    ):
        assess_road_proximity_coverage(parcels, road_source, SOURCE_CONFIG, policy_path)
    proximity_stage.assert_called_once_with(
        parcels, road_source, SOURCE_CONFIG, policy_path
    )
    coverage_loader.assert_called_once_with(road_source.extraction, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_proximity_failure_stops_coverage_loading`

**Purpose:** Regression invariant: proximity failure stops coverage loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_proximity_failure_stops_coverage_loading() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
| `coverage_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_proximity_failure_stops_coverage_loading() -> None:
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            side_effect=ValueError("bad proximity"),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(_parcels(), _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_loader_failure_is_controlled`

**Purpose:** Regression invariant: coverage loader failure is controlled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_loader_failure_is_controlled() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `patch` | `unittest.mock.patch` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
| `coverage_loader.assert_called_once` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_coverage_loader_failure_is_controlled() -> None:
    parcels = _parcels()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=_proximity(parcels),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            side_effect=ValueError("bad coverage"),
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_called_once()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stage_does_not_construct_a_road_spatial_index`

**Purpose:** Regression invariant: stage does not construct a road spatial index. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stage_does_not_construct_a_road_spatial_index() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert "STRtree(" not in source`
  - `assert "query_nearest(" not in source`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `Path("src/landscout/stages/assess_road_proximity_coverage.py").read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path("src/landscout/stages/assess_road_proximity_coverage.py").read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_stage_does_not_construct_a_road_spatial_index() -> None:
    with patch("shapely.STRtree", side_effect=AssertionError("forbidden")):
        _assess()
    source = Path("src/landscout/stages/assess_road_proximity_coverage.py").read_text(
        encoding="utf-8"
    )
    assert "STRtree(" not in source
    assert "query_nearest(" not in source
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_upstream_result_fails_before_coverage_load`

**Purpose:** Regression invariant: malformed upstream result fails before coverage load. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_upstream_result_fails_before_coverage_load(mutation: Any) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        lambda result: object(),
        lambda result: replace(result, parcels=result.parcels.drop(columns="geometry")),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.drop(
                columns="nearest_road_proxy_distance_m"
            ),
        ),
        lambda result: replace(
            result, class_proximity=result.class_proximity.iloc[:-1].copy()
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.iloc[
                [1, 0, *range(2, 5)]
            ].reset_index(drop=True),
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.assign(
                proximity_scope="GLOBAL_NEAREST"
            ),
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.assign(
                road_proxy_policy_config_sha256=["c" * 64, *["d" * 64] * 4]
            ),
        ),
    ],
    ids=[
        "wrong-type",
        "bad-parcels",
        "missing-column",
        "row-count",
        "order",
        "scope",
        "policy-sha",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `Any` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `mutation` | `unresolved local/third-party receiver; no ownership inferred` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
| `coverage_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_malformed_upstream_result_fails_before_coverage_load(mutation: Any) -> None:
    parcels = _parcels()
    malformed = mutation(_proximity(parcels))
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=malformed,
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_package_lineage_must_match_road_archive`

**Purpose:** Regression invariant: coverage package lineage must match road archive. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_package_lineage_must_match_road_archive(
    field: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_provider", "Other provider"),
        ("source_product", "Other product"),
        ("source_department_code", "32"),
        ("source_edition", "2099-01-01"),
        ("source_product_version", "99"),
        ("source_archive_sha256", "c" * 64),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        RoadProximityCoverageError, match="package\|lineage\|provider\|product"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `coverage.coverage.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `cast` | `typing.cast` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
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
| In-memory mutation | `frame[field] = value`<br>`frame[coverage.summary.department_code_field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coverage_package_lineage_must_match_road_archive(
    field: str, value: object
) -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[field] = value
    if field == "source_department_code":
        frame[coverage.summary.department_code_field] = value
        summary = replace(coverage.summary, selected_department_code=cast(str, value))
    else:
        summary = coverage.summary
    forged = replace(coverage, coverage=frame, summary=summary, **{field: value})
    with pytest.raises(
        RoadProximityCoverageError, match="package|lineage|provider|product"
    ):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`

**Purpose:** Regression invariant: configured coverage layer cannot be replaced by real alternate layer. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError, match="configured\|layer")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |

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
def test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer() -> None:
    coverage = _coverage(layer="zone_administrative")
    with pytest.raises(RoadProximityCoverageError, match="configured|layer"):
        _assess(coverage=coverage, road_source=_road_source(coverage.extraction))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_selected_department_identity_is_exact`

**Purpose:** Regression invariant: selected department identity is exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_selected_department_identity_is_exact() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError, match="department")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `coverage.coverage.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |

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
| In-memory mutation | `frame[coverage.summary.department_code_field] = "32"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_selected_department_identity_is_exact() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[coverage.summary.department_code_field] = "32"
    forged = replace(
        coverage,
        coverage=frame,
        summary=replace(coverage.summary, selected_department_code="32"),
    )
    with pytest.raises(RoadProximityCoverageError, match="department"):
        _assess(coverage=forged)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_spatial_role_and_source_type_are_controlled`

**Purpose:** Regression invariant: coverage spatial role and source type are controlled. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_spatial_role_and_source_type_are_controlled() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError, match="spatial\|lineage")`
  - `pytest.raises(RoadProximityCoverageError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `coverage.coverage.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `cast` | `typing.cast` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `patch` | `unittest.mock.patch` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |

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
| In-memory mutation | `frame["spatial_role"] = "PROXY_GEOMETRY"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coverage_spatial_role_and_source_type_are_controlled() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame["spatial_role"] = "PROXY_GEOMETRY"
    wrong_role = replace(
        coverage,
        coverage=frame,
        summary=replace(
            coverage.summary,
            spatial_role=cast(Any, "PROXY_GEOMETRY"),
        ),
        spatial_role=cast(Any, "PROXY_GEOMETRY"),
    )
    with pytest.raises(RoadProximityCoverageError, match="spatial|lineage"):
        _assess(coverage=wrong_role)

    parcels = _parcels()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=_proximity(parcels),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=object(),
        ),
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coverage_must_retain_same_extraction_object`

**Purpose:** Regression invariant: coverage must retain same extraction object. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coverage_must_retain_same_extraction_object() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError, match="extraction")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |

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
def test_coverage_must_retain_same_extraction_object() -> None:
    coverage = _coverage()
    forged = replace(coverage, extraction=replace(coverage.extraction))
    with pytest.raises(RoadProximityCoverageError, match="extraction"):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_coverage_geometry_is_rejected`

**Purpose:** Regression invariant: invalid coverage geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_coverage_geometry_is_rejected(
    geometries: list[object], crs: str | None, message: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometries", "crs", "message"),
    [
        ([], "EPSG:2154", "one|exactly"),
        (
            [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])] * 2,
            "EPSG:2154",
            "one|exactly",
        ),
        ([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])], None, "CRS"),
        ([Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])], "EPSG:4326", "2154"),
        ([None], "EPSG:2154", "null"),
        ([Polygon()], "EPSG:2154", "empty"),
        ([Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])], "EPSG:2154", "valid"),
        ([Point(0, 0)], "EPSG:2154", "Polygon"),
        ([LineString([(0, 0), (10, 10)])], "EPSG:2154", "Polygon"),
    ],
    ids=[
        "zero",
        "two",
        "no-crs",
        "wrong-crs",
        "null",
        "empty",
        "invalid",
        "point",
        "line",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object]` | `required` |
| `crs` | positional-or-keyword | `str \| None` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `Point` | `shapely.geometry.Point` |
| `LineString` | `shapely.geometry.LineString` |

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
def test_invalid_coverage_geometry_is_rejected(
    geometries: list[object], crs: str | None, message: str
) -> None:
    coverage = _coverage(geometries=geometries, crs=crs)
    with pytest.raises(RoadProximityCoverageError, match=message):
        _assess(coverage=coverage)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_polygonal_coverage_geometry_is_accepted`

**Purpose:** Regression invariant: polygonal coverage geometry is accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
        MultiPolygon([Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(_assess(coverage=_coverage(geometries=[geometry])).parcels) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |

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
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    assert len(_assess(coverage=_coverage(geometries=[geometry])).parcels) == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_full_parcel_coverage_position_is_conservative`

**Purpose:** Regression invariant: full parcel coverage position is conservative. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_full_parcel_coverage_position_is_conservative(
    geometry: Polygon, position: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry", "position"),
    [
        (
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            "FULLY_COVERED",
        ),
        (
            Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
        (
            Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
        (
            Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
    ],
    ids=["inside", "touching", "crossing", "outside"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `Polygon` | `required` |
| `position` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.road_source_coverage_position == position`
  - `assert row.road_source_boundary_distance_m == 0.0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_first_row` | `tests.unit.test_assess_road_proximity_coverage._first_row` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |

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
def test_full_parcel_coverage_position_is_conservative(
    geometry: Polygon, position: str
) -> None:
    parcels = _parcels([geometry])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == position
    if position != "FULLY_COVERED":
        assert row.road_source_boundary_distance_m == 0.0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_position_uses_full_geometry_not_centroid`

**Purpose:** Regression invariant: position uses full geometry not centroid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_position_uses_full_geometry_not_centroid() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.road_source_coverage_position == "OUTSIDE_OR_CROSSING_COVERAGE"`
  - `assert row.road_source_boundary_distance_m == 0.0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_first_row` | `tests.unit.test_assess_road_proximity_coverage._first_row` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |

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
def test_position_uses_full_geometry_not_centroid() -> None:
    crossing_with_inside_centroid = Polygon(
        [(-10, 100), (-10, 200), (300, 200), (300, 100), (-10, 100)]
    )
    parcels = _parcels([crossing_with_inside_centroid])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert row.road_source_boundary_distance_m == 0.0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`

**Purpose:** Regression invariant: internal boundary distance is full geometry finite and nonnegative. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert values.eq(expected).all()`
  - `assert np.isfinite(values).all()`
  - `assert values.ge(0).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `_measured_boundary_distance` | `tests.unit.test_assess_road_proximity_coverage._measured_boundary_distance` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `values.eq(expected).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite(values).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `values.ge(0).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.ge` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_measured_boundary_distance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative() -> None:
    parcels = _parcels()
    coverage = _coverage()
    expected = _measured_boundary_distance(parcels, coverage)
    result = _assess(parcels=parcels, proximity=_proximity(parcels), coverage=coverage)
    values = result.class_proximity["road_source_boundary_distance_m"]
    assert values.eq(expected).all()
    assert np.isfinite(values).all()
    assert values.ge(0).all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_strict_boundary_status_logic`

**Purpose:** Regression invariant: strict boundary status logic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_strict_boundary_status_logic(offset: float, expected: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("offset", "expected"),
    [
        (-50.0, "NOT_BOUNDARY_LIMITED"),
        (-0.001, "NOT_BOUNDARY_LIMITED"),
        (0.0, "BOUNDARY_LIMITED"),
        (50.0, "BOUNDARY_LIMITED"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `offset` | positional-or-keyword | `float` | `required` |
| `expected` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.class_proximity["road_proximity_coverage_status"].eq(expected).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `_measured_boundary_distance` | `tests.unit.test_assess_road_proximity_coverage._measured_boundary_distance` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `result.class_proximity["road_proximity_coverage_status"].eq(expected).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.class_proximity["road_proximity_coverage_status"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_measured_boundary_distance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_strict_boundary_status_logic(offset: float, expected: str) -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels,
        distances={road_class: margin + offset for road_class in ELIGIBLE_CLASSES},
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert result.class_proximity["road_proximity_coverage_status"].eq(expected).all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_matched_outside_or_crossing_status`

**Purpose:** Regression invariant: matched outside or crossing status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_matched_outside_or_crossing_status(geometry: Polygon) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),
        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
    ],
    ids=["crossing", "touching", "outside"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        result.class_proximity["road_proximity_coverage_status"]<br>        .eq("OUTSIDE_OR_CROSSING_COVERAGE")<br>        .all()<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `result.class_proximity["road_proximity_coverage_status"]<br>        .eq("OUTSIDE_OR_CROSSING_COVERAGE")<br>        .all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.class_proximity["road_proximity_coverage_status"]<br>        .eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |

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
def test_matched_outside_or_crossing_status(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    result = _assess(parcels=parcels, proximity=_proximity(parcels))
    assert (
        result.class_proximity["road_proximity_coverage_status"]
        .eq("OUTSIDE_OR_CROSSING_COVERAGE")
        .all()
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_match_takes_precedence_over_coverage_position`

**Purpose:** Regression invariant: no match takes precedence over coverage position. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_match_takes_precedence_over_coverage_position(geometry: Polygon) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
    ],
    ids=["inside", "outside"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        _first_row(result, "UNKNOWN_REVIEW").road_proximity_coverage_status<br>        == "NO_MATCH"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_without_match` | `tests.unit.test_assess_road_proximity_coverage._without_match` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_first_row` | `tests.unit.test_assess_road_proximity_coverage._first_row` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |

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
def test_no_match_takes_precedence_over_coverage_position(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    proximity = _without_match(_proximity(parcels))
    result = _assess(parcels=parcels, proximity=proximity)
    assert (
        _first_row(result, "UNKNOWN_REVIEW").road_proximity_coverage_status
        == "NO_MATCH"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_classes_are_diagnosed_independently`

**Purpose:** Regression invariant: classes are diagnosed independently. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_classes_are_diagnosed_independently() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        _first_row(result, "GENERAL_VEHICLE_PROXY").road_proximity_coverage_status<br>        == "NOT_BOUNDARY_LIMITED"<br>    )`
  - `assert (<br>        _first_row(result, "RESTRICTED_REVIEW").road_proximity_coverage_status<br>        == "BOUNDARY_LIMITED"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `_measured_boundary_distance` | `tests.unit.test_assess_road_proximity_coverage._measured_boundary_distance` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `_first_row` | `tests.unit.test_assess_road_proximity_coverage._first_row` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_measured_boundary_distance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_classes_are_diagnosed_independently() -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels,
        distances={
            "GENERAL_VEHICLE_PROXY": margin - 1,
            "RESTRICTED_REVIEW": margin + 1,
        },
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert (
        _first_row(result, "GENERAL_VEHICLE_PROXY").road_proximity_coverage_status
        == "NOT_BOUNDARY_LIMITED"
    )
    assert (
        _first_row(result, "RESTRICTED_REVIEW").road_proximity_coverage_status
        == "BOUNDARY_LIMITED"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_coverage_lineage_is_appended_to_every_row`

**Purpose:** Regression invariant: exact coverage lineage is appended to every row. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_coverage_lineage_is_appended_to_every_row() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.class_proximity[column].eq(value).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `expected.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.class_proximity[column].eq(value).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.class_proximity[column].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_exact_coverage_lineage_is_appended_to_every_row() -> None:
    coverage = _coverage()
    result = _assess(coverage=coverage)
    expected = {
        "road_source_coverage_provider": coverage.source_provider,
        "road_source_coverage_product": coverage.source_product,
        "road_source_coverage_department_code": coverage.source_department_code,
        "road_source_coverage_edition": coverage.source_edition,
        "road_source_coverage_product_version": coverage.source_product_version,
        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,
        "road_source_coverage_layer": coverage.source_layer,
        "road_source_coverage_spatial_role": coverage.spatial_role,
    }
    for column, value in expected.items():
        assert result.class_proximity[column].eq(value).all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_matched_road_lineage_must_match_coverage`

**Purpose:** Regression invariant: matched road lineage must match coverage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_matched_road_lineage_must_match_coverage(column: str, value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_source_department_code", "32"),
        ("nearest_source_edition", "2099-01-01"),
        ("nearest_source_archive_sha256", "c" * 64),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError, match="lineage\|package")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `proximity.class_proximity.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `replace` | `dataclasses.replace` |
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
| In-memory mutation | `table[column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_matched_road_lineage_must_match_coverage(column: str, value: str) -> None:
    proximity = _proximity()
    table = proximity.class_proximity.copy()
    table[column] = value
    with pytest.raises(RoadProximityCoverageError, match="lineage|package"):
        _assess(proximity=replace(proximity, class_proximity=table))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_preserves_every_upstream_fact_and_input_object`

**Purpose:** Regression invariant: result preserves every upstream fact and input object. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_preserves_every_upstream_fact_and_input_object() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert road_source.road_segments_summary == road_summary_before`
  - `assert road_source.extraction is extraction_before`
  - `assert SOURCE_CONFIG.model_dump(mode="python") == config_before`
  - `assert (<br>        tuple(result.class_proximity.columns[: len(CLASS_PROXIMITY_COLUMNS)])<br>        == CLASS_PROXIMITY_COLUMNS<br>    )`
  - `assert (<br>        tuple(result.class_proximity.columns[len(CLASS_PROXIMITY_COLUMNS) :])<br>        == DIAGNOSTIC_COLUMNS<br>    )`
  - `assert result.class_coverage is proximity.class_coverage`
  - `assert result.source_coverage is coverage`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `_coverage` | `tests.unit.test_assess_road_proximity_coverage._coverage` |
| `_road_source` | `tests.unit.test_assess_road_proximity_coverage._road_source` |
| `deepcopy` | `copy.deepcopy` |
| `SOURCE_CONFIG.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_result_preserves_every_upstream_fact_and_input_object() -> None:
    parcels = _parcels(
        [
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            Polygon([(300, 300), (300, 400), (400, 400), (400, 300), (300, 300)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    proximity = _proximity(parcels)
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels_before = deepcopy(parcels)
    proximity_parcels_before = deepcopy(proximity.parcels)
    table_before = deepcopy(proximity.class_proximity)
    coverage_before = deepcopy(coverage.coverage)
    roads_before = deepcopy(road_source.road_segments)
    road_summary_before = road_source.road_segments_summary
    extraction_before = road_source.extraction
    config_before = SOURCE_CONFIG.model_dump(mode="python")
    result = _assess(
        parcels=parcels,
        proximity=proximity,
        coverage=coverage,
        road_source=road_source,
    )

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(proximity.parcels, proximity_parcels_before)
    assert_frame_equal(proximity.class_proximity, table_before)
    assert_geodataframe_equal(coverage.coverage, coverage_before)
    assert_geodataframe_equal(road_source.road_segments, roads_before)
    assert road_source.road_segments_summary == road_summary_before
    assert road_source.extraction is extraction_before
    assert SOURCE_CONFIG.model_dump(mode="python") == config_before
    assert_geodataframe_equal(result.parcels, proximity_parcels_before)
    assert_frame_equal(
        result.class_proximity.loc[:, list(CLASS_PROXIMITY_COLUMNS)],
        table_before,
        check_dtype=True,
        check_index_type=True,
    )
    assert (
        tuple(result.class_proximity.columns[: len(CLASS_PROXIMITY_COLUMNS)])
        == CLASS_PROXIMITY_COLUMNS
    )
    assert (
        tuple(result.class_proximity.columns[len(CLASS_PROXIMITY_COLUMNS) :])
        == DIAGNOSTIC_COLUMNS
    )
    assert result.class_coverage is proximity.class_coverage
    assert result.source_coverage is coverage
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_corrupt_generated`

**Purpose:** Implements `corrupt generated` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def _corrupt_generated(column: str, value: object, *, outside: bool = False) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |
| `outside` | keyword-only | `bool` | `False` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError)`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_malformed_generated_value_is_rejected` via `_corrupt_generated`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_malformed_generated_value_is_rejected` via `_corrupt_generated`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_outside_position_requires_zero_boundary_distance` via `_corrupt_generated`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_outside_position_requires_zero_boundary_distance` via `_corrupt_generated`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `import_module` | `importlib.import_module` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |

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
def _corrupt_generated(column: str, value: object, *, outside: bool = False) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    geometry = (
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)])
        if outside
        else None
    )
    parcels = _parcels([geometry]) if geometry is not None else _parcels()
    proximity = _proximity(parcels)
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output[column] = output[column].astype("object")
        output.at[0, column] = value
        return output

    with (
        patch.object(module, "_diagnosed_class_proximity", side_effect=corrupt),
        pytest.raises(RoadProximityCoverageError),
    ):
        _assess(parcels=parcels, proximity=proximity)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_corrupt_generated.corrupt`

**Purpose:** Implements `corrupt` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original` | `unresolved local/third-party receiver; no ownership inferred` |
| `output[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `output[column] = output[column].astype("object")`<br>`output.at[0, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output[column] = output[column].astype("object")
        output.at[0, column] = value
        return output
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_generated_value_is_rejected`

**Purpose:** Regression invariant: malformed generated value is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_generated_value_is_rejected(column: str, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("road_source_boundary_distance_m", -1.0),
        ("road_source_boundary_distance_m", float("nan")),
        ("road_source_boundary_distance_m", float("inf")),
        ("road_source_coverage_position", "INVENTED"),
        ("road_proximity_coverage_status", "INVENTED"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_corrupt_generated` | `tests.unit.test_assess_road_proximity_coverage._corrupt_generated` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_malformed_generated_value_is_rejected(column: str, value: object) -> None:
    _corrupt_generated(column, value)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inconsistent_generated_status_is_rejected`

**Purpose:** Regression invariant: inconsistent generated status is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inconsistent_generated_status_is_rejected(
    distance: float, wrong_status: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("distance", "wrong_status"),
    [(50.0, "BOUNDARY_LIMITED"), (150.0, "NOT_BOUNDARY_LIMITED")],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `distance` | positional-or-keyword | `float` | `required` |
| `wrong_status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityCoverageError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `import_module` | `importlib.import_module` |
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `_proximity` | `tests.unit.test_assess_road_proximity_coverage._proximity` |
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
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
def test_inconsistent_generated_status_is_rejected(
    distance: float, wrong_status: str
) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    parcels = _parcels()
    proximity = _proximity(
        parcels, distances={road_class: distance for road_class in ELIGIBLE_CLASSES}
    )
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output.at[0, "road_proximity_coverage_status"] = wrong_status
        return output

    with (
        patch.object(module, "_diagnosed_class_proximity", side_effect=corrupt),
        pytest.raises(RoadProximityCoverageError),
    ):
        _assess(parcels=parcels, proximity=proximity)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inconsistent_generated_status_is_rejected.corrupt`

**Purpose:** Implements `corrupt` within the file role: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

**Exact signature**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `output.at[0, "road_proximity_coverage_status"] = wrong_status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output.at[0, "road_proximity_coverage_status"] = wrong_status
        return output
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_outside_position_requires_zero_boundary_distance`

**Purpose:** Regression invariant: outside position requires zero boundary distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_outside_position_requires_zero_boundary_distance() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_corrupt_generated` | `tests.unit.test_assess_road_proximity_coverage._corrupt_generated` |

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
def test_outside_position_requires_zero_boundary_distance() -> None:
    _corrupt_generated("road_source_boundary_distance_m", 1.0, outside=True)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_is_frozen_and_has_no_business_decision_fields`

**Purpose:** Regression invariant: result is frozen and has no business decision fields. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_is_frozen_and_has_no_business_decision_fields() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(FrozenInstanceError)`
- Exact assertions:
  - `assert forbidden.isdisjoint(result.parcels.columns)`
  - `assert forbidden.isdisjoint(result.class_proximity.columns)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_assess` | `tests.unit.test_assess_road_proximity_coverage._assess` |
| `pytest.raises` | `pytest.raises` |
| `_parcels` | `tests.unit.test_assess_road_proximity_coverage._parcels` |
| `forbidden.isdisjoint` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `forbidden.isdisjoint` |
| External process/environment | None directly present. |
| In-memory mutation | `result.parcels = _parcels()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_result_is_frozen_and_has_no_business_decision_fields() -> None:
    result = _assess()
    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    forbidden = {
        "accessible",
        "road_access_ok",
        "legal_access",
        "truck_access",
        "bess_access",
        "score",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **28**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_public_api_exports_only_stable_symbols` | none | none | 4 | Proves public api exports only stable symbols using the exact source reproduced in section 7. |
| `test_wrong_public_input_type_is_controlled_and_fast` | pytest.mark.parametrize(<br>    "argument", ["parcels", "road_source", "source_config", "policy_path"]<br>) | pytest.raises(RoadProximityCoverageError) | 0 | Proves wrong public input type is controlled and fast using the exact source reproduced in section 7. |
| `test_source_chain_calls_proximity_then_coverage_exactly_once` | none | none | 0 | Proves source chain calls proximity then coverage exactly once using the exact source reproduced in section 7. |
| `test_proximity_failure_stops_coverage_loading` | none | pytest.raises(RoadProximityCoverageError) | 0 | Proves proximity failure stops coverage loading using the exact source reproduced in section 7. |
| `test_coverage_loader_failure_is_controlled` | none | pytest.raises(RoadProximityCoverageError) | 0 | Proves coverage loader failure is controlled using the exact source reproduced in section 7. |
| `test_stage_does_not_construct_a_road_spatial_index` | none | none | 2 | Proves stage does not construct a road spatial index using the exact source reproduced in section 7. |
| `test_malformed_upstream_result_fails_before_coverage_load` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        lambda result: object(),<br>        lambda result: replace(result, parcels=result.parcels.drop(columns="geometry")),<br>        lambda result: replace(<br>            result,<br>            class_proximity=result.class_proximity.drop(<br>                columns="nearest_road_proxy_distance_m"<br>            ),<br>        ),<br>        lambda result: replace(<br>            result, class_proximity=result.class_proximity.iloc[:-1].copy()<br>        ),<br>        lambda result: replace(<br>            result,<br>            class_proximity=result.class_proximity.iloc[<br>                [1, 0, *range(2, 5)]<br>            ].reset_index(drop=True),<br>        ),<br>        lambda result: replace(<br>            result,<br>            class_proximity=result.class_proximity.assign(<br>                proximity_scope="GLOBAL_NEAREST"<br>            ),<br>        ),<br>        lambda result: replace(<br>            result,<br>            class_proximity=result.class_proximity.assign(<br>                road_proxy_policy_config_sha256=["c" * 64, *["d" * 64] * 4]<br>            ),<br>        ),<br>    ],<br>    ids=[<br>        "wrong-type",<br>        "bad-parcels",<br>        "missing-column",<br>        "row-count",<br>        "order",<br>        "scope",<br>        "policy-sha",<br>    ],<br>) | pytest.raises(RoadProximityCoverageError) | 0 | Proves malformed upstream result fails before coverage load using the exact source reproduced in section 7. |
| `test_coverage_package_lineage_must_match_road_archive` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("source_provider", "Other provider"),<br>        ("source_product", "Other product"),<br>        ("source_department_code", "32"),<br>        ("source_edition", "2099-01-01"),<br>        ("source_product_version", "99"),<br>        ("source_archive_sha256", "c" * 64),<br>    ],<br>) | pytest.raises(<br>        RoadProximityCoverageError, match="package\|lineage\|provider\|product"<br>    ) | 0 | Proves coverage package lineage must match road archive using the exact source reproduced in section 7. |
| `test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` | none | pytest.raises(RoadProximityCoverageError, match="configured\|layer") | 0 | Proves configured coverage layer cannot be replaced by real alternate layer using the exact source reproduced in section 7. |
| `test_selected_department_identity_is_exact` | none | pytest.raises(RoadProximityCoverageError, match="department") | 0 | Proves selected department identity is exact using the exact source reproduced in section 7. |
| `test_coverage_spatial_role_and_source_type_are_controlled` | none | pytest.raises(RoadProximityCoverageError, match="spatial\|lineage"); pytest.raises(RoadProximityCoverageError) | 0 | Proves coverage spatial role and source type are controlled using the exact source reproduced in section 7. |
| `test_coverage_must_retain_same_extraction_object` | none | pytest.raises(RoadProximityCoverageError, match="extraction") | 0 | Proves coverage must retain same extraction object using the exact source reproduced in section 7. |
| `test_invalid_coverage_geometry_is_rejected` | pytest.mark.parametrize(<br>    ("geometries", "crs", "message"),<br>    [<br>        ([], "EPSG:2154", "one\|exactly"),<br>        (<br>            [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])] * 2,<br>            "EPSG:2154",<br>            "one\|exactly",<br>        ),<br>        ([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])], None, "CRS"),<br>        ([Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])], "EPSG:4326", "2154"),<br>        ([None], "EPSG:2154", "null"),<br>        ([Polygon()], "EPSG:2154", "empty"),<br>        ([Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])], "EPSG:2154", "valid"),<br>        ([Point(0, 0)], "EPSG:2154", "Polygon"),<br>        ([LineString([(0, 0), (10, 10)])], "EPSG:2154", "Polygon"),<br>    ],<br>    ids=[<br>        "zero",<br>        "two",<br>        "no-crs",<br>        "wrong-crs",<br>        "null",<br>        "empty",<br>        "invalid",<br>        "point",<br>        "line",<br>    ],<br>) | pytest.raises(RoadProximityCoverageError, match=message) | 0 | Proves invalid coverage geometry is rejected using the exact source reproduced in section 7. |
| `test_polygonal_coverage_geometry_is_accepted` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),<br>        MultiPolygon([Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]),<br>    ],<br>) | none | 1 | Proves polygonal coverage geometry is accepted using the exact source reproduced in section 7. |
| `test_full_parcel_coverage_position_is_conservative` | pytest.mark.parametrize(<br>    ("geometry", "position"),<br>    [<br>        (<br>            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),<br>            "FULLY_COVERED",<br>        ),<br>        (<br>            Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),<br>            "OUTSIDE_OR_CROSSING_COVERAGE",<br>        ),<br>        (<br>            Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),<br>            "OUTSIDE_OR_CROSSING_COVERAGE",<br>        ),<br>        (<br>            Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),<br>            "OUTSIDE_OR_CROSSING_COVERAGE",<br>        ),<br>    ],<br>    ids=["inside", "touching", "crossing", "outside"],<br>) | none | 2 | Proves full parcel coverage position is conservative using the exact source reproduced in section 7. |
| `test_position_uses_full_geometry_not_centroid` | none | none | 2 | Proves position uses full geometry not centroid using the exact source reproduced in section 7. |
| `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` | none | none | 3 | Proves internal boundary distance is full geometry finite and nonnegative using the exact source reproduced in section 7. |
| `test_strict_boundary_status_logic` | pytest.mark.parametrize(<br>    ("offset", "expected"),<br>    [<br>        (-50.0, "NOT_BOUNDARY_LIMITED"),<br>        (-0.001, "NOT_BOUNDARY_LIMITED"),<br>        (0.0, "BOUNDARY_LIMITED"),<br>        (50.0, "BOUNDARY_LIMITED"),<br>    ],<br>) | none | 1 | Proves strict boundary status logic using the exact source reproduced in section 7. |
| `test_matched_outside_or_crossing_status` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),<br>        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),<br>        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),<br>    ],<br>    ids=["crossing", "touching", "outside"],<br>) | none | 1 | Proves matched outside or crossing status using the exact source reproduced in section 7. |
| `test_no_match_takes_precedence_over_coverage_position` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),<br>        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),<br>    ],<br>    ids=["inside", "outside"],<br>) | none | 1 | Proves no match takes precedence over coverage position using the exact source reproduced in section 7. |
| `test_classes_are_diagnosed_independently` | none | none | 2 | Proves classes are diagnosed independently using the exact source reproduced in section 7. |
| `test_exact_coverage_lineage_is_appended_to_every_row` | none | none | 1 | Proves exact coverage lineage is appended to every row using the exact source reproduced in section 7. |
| `test_matched_road_lineage_must_match_coverage` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("nearest_source_department_code", "32"),<br>        ("nearest_source_edition", "2099-01-01"),<br>        ("nearest_source_archive_sha256", "c" * 64),<br>    ],<br>) | pytest.raises(RoadProximityCoverageError, match="lineage\|package") | 0 | Proves matched road lineage must match coverage using the exact source reproduced in section 7. |
| `test_result_preserves_every_upstream_fact_and_input_object` | none | none | 7 | Proves result preserves every upstream fact and input object using the exact source reproduced in section 7. |
| `test_malformed_generated_value_is_rejected` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("road_source_boundary_distance_m", -1.0),<br>        ("road_source_boundary_distance_m", float("nan")),<br>        ("road_source_boundary_distance_m", float("inf")),<br>        ("road_source_coverage_position", "INVENTED"),<br>        ("road_proximity_coverage_status", "INVENTED"),<br>    ],<br>) | none | 0 | Proves malformed generated value is rejected using the exact source reproduced in section 7. |
| `test_inconsistent_generated_status_is_rejected` | pytest.mark.parametrize(<br>    ("distance", "wrong_status"),<br>    [(50.0, "BOUNDARY_LIMITED"), (150.0, "NOT_BOUNDARY_LIMITED")],<br>) | pytest.raises(RoadProximityCoverageError) | 0 | Proves inconsistent generated status is rejected using the exact source reproduced in section 7. |
| `test_outside_position_requires_zero_boundary_distance` | none | none | 0 | Proves outside position requires zero boundary distance using the exact source reproduced in section 7. |
| `test_result_is_frozen_and_has_no_business_decision_fields` | none | pytest.raises(FrozenInstanceError) | 2 | Proves result is frozen and has no business decision fields using the exact source reproduced in section 7. |

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
from __future__ import annotations

from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from importlib import import_module
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import LineString, MultiPolygon, Point, Polygon

from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)
from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)
from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)
from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)

SOURCE_CONFIG = load_ign_bdtopo_source_config()
ARCHIVE_SHA256 = "a" * 64
GEOPACKAGE_SHA256 = "b" * 64
EDITION = "2026-06-15"
ELIGIBLE_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "UNKNOWN_REVIEW",
)
ALL_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "NOT_DISTANCE_PROXY",
    "UNKNOWN_REVIEW",
)
DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    "road_source_coverage_provider",
    "road_source_coverage_product",
    "road_source_coverage_department_code",
    "road_source_coverage_edition",
    "road_source_coverage_product_version",
    "road_source_coverage_archive_sha256",
    "road_source_coverage_layer",
    "road_source_coverage_spatial_role",
)
SELECTED_COLUMNS = (
    "nearest_road_proxy_distance_m",
    "nearest_road_feature_id",
    "nearest_source_feature_id",
    "nearest_road_tie_count",
    "nearest_road_primary_rule",
    "nearest_road_rule_trace_json",
    "nearest_road_unknown_fields_json",
    "nearest_road_toll_evidence",
    "nearest_nature_raw",
    "nearest_importance_raw",
    "nearest_asset_status_raw",
    "nearest_private_raw",
    "nearest_light_vehicle_access_raw",
    "nearest_carriageway_width_raw",
    "nearest_closure_period_raw",
    "nearest_restriction_nature_raw",
    "nearest_source_layer",
    "nearest_source_department_code",
    "nearest_source_edition",
    "nearest_source_archive_sha256",
)


def _archive() -> IgnBdTopoDownload:
    return IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product=SOURCE_CONFIG.product,
        department_code="31",
        edition=EDITION,
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=str(SOURCE_CONFIG.source_url),
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO.7z",
        file_size=123,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("synthetic/BDTOPO.7z"),
        cache_hit=True,
    )


def _extraction() -> IgnBdTopoExtraction:
    return IgnBdTopoExtraction(
        archive=_archive(),
        extraction_path=Path("synthetic/extracted"),
        geopackage_path=Path("synthetic/extracted/data.gpkg"),
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=456,
        geopackage_sha256=GEOPACKAGE_SHA256,
        all_layer_names=(
            "ligne_electrique",
            "poste_de_transformation",
            "troncon_de_route",
            "departement",
            "zone_administrative",
        ),
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        road_segments_layer="troncon_de_route",
        department_layer="departement",
        cache_hit=True,
    )


def _road_source(
    extraction: IgnBdTopoExtraction | None = None,
) -> IgnBdTopoRoadData:
    package = extraction or _extraction()
    roads = gpd.GeoDataFrame(
        {"cleabs": ["ROAD-1"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    summary = IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name="troncon_de_route",
        crs="EPSG:2154",
        feature_count=1,
        columns=tuple(str(column) for column in roads.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in roads.dtypes.items()
        ),
        null_geometry_count=0,
        empty_geometry_count=0,
        invalid_geometry_count=0,
        geometry_types=("LineString",),
    )
    return IgnBdTopoRoadData(package, roads, summary)


def _coverage(
    extraction: IgnBdTopoExtraction | None = None,
    *,
    geometries: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    layer: str = "departement",
    department_code: str = "31",
    provider: str | None = None,
    product: str | None = None,
    edition: str = EDITION,
    product_version: str | None = "3.5",
    archive_sha256: str = ARCHIVE_SHA256,
) -> IgnBdTopoDepartmentCoverage:
    package = extraction or _extraction()
    values = geometries
    if values is None:
        values = [Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]
    raw = gpd.GeoDataFrame(
        {
            "code_insee": [department_code] * len(values),
            "nom_officiel": [
                f"Department {position}" for position in range(len(values))
            ],
        },
        geometry=values,
        crs=crs,
    )
    lineage = {
        "source_provider": provider or package.archive.provider,
        "source_product": product or package.archive.product,
        "source_department_code": department_code,
        "source_edition": edition,
        "source_product_version": product_version,
        "source_archive_sha256": archive_sha256,
        "source_layer": layer,
        "spatial_role": "SOURCE_COVERAGE_BOUNDARY",
    }
    selected = raw.copy()
    for column, value in lineage.items():
        selected[column] = value
    geometry = raw.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name=layer,
        crs="" if crs is None else str(raw.crs),
        source_feature_count=len(raw),
        selected_feature_count=len(raw),
        columns=tuple(str(column) for column in raw.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in raw.dtypes.items()),
        null_geometry_count=int(geometry.isna().sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
        geometry_types=tuple(
            sorted(str(value) for value in geometry.geom_type.dropna().unique())
        ),
        department_code_field="code_insee",
        selected_department_code=department_code,
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=package,
        coverage=selected,
        summary=summary,
        source_provider=cast(str, lineage["source_provider"]),
        source_product=cast(str, lineage["source_product"]),
        source_department_code=department_code,
        source_edition=edition,
        source_product_version=product_version,
        source_archive_sha256=archive_sha256,
        source_layer=layer,
    )


def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])
    ]
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(len(values))]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "preserved_value": list(range(len(values)))},
        geometry=values,
        crs="EPSG:2154",
        index=[20 + position for position in range(len(values))],
    )


def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(geometries, identifiers=identifiers).to_crs("EPSG:4326")


def _proximity(
    parcels: gpd.GeoDataFrame | None = None,
    *,
    distances: dict[str, float] | None = None,
) -> ParcelRoadProximityResult:
    source_parcels = parcels if parcels is not None else _parcels()
    policy = load_ign_road_vehicle_proxy_policy()
    configured_distances = distances or {}
    primary_rules = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }
    rows: list[dict[str, object]] = []
    for parcel_id in source_parcels["parcel_id"]:
        for position, road_class in enumerate(ELIGIBLE_CLASSES):
            distance_m = configured_distances.get(road_class, 50.0 + position)
            primary_rule = primary_rules[road_class]
            rows.append(
                {
                    "parcel_id": parcel_id,
                    "road_proxy_class": road_class,
                    "nearest_road_proxy_distance_m": distance_m,
                    "nearest_road_feature_id": f"ROAD-{road_class}",
                    "nearest_source_feature_id": f"SOURCE-{road_class}",
                    "nearest_road_tie_count": 1,
                    "nearest_road_primary_rule": primary_rule,
                    "nearest_road_rule_trace_json": f'["{primary_rule}"]',
                    "nearest_road_unknown_fields_json": "[]",
                    "nearest_road_toll_evidence": False,
                    "nearest_nature_raw": "Route à 1 chaussée",
                    "nearest_importance_raw": "2",
                    "nearest_asset_status_raw": "En service",
                    "nearest_private_raw": 0.0,
                    "nearest_light_vehicle_access_raw": "Libre",
                    "nearest_carriageway_width_raw": 7.0,
                    "nearest_closure_period_raw": None,
                    "nearest_restriction_nature_raw": None,
                    "nearest_source_layer": "troncon_de_route",
                    "nearest_source_department_code": "31",
                    "nearest_source_edition": EDITION,
                    "nearest_source_archive_sha256": ARCHIVE_SHA256,
                    "road_proxy_policy_id": policy.policy_id,
                    "road_proxy_policy_schema_version": policy.schema_version,
                    "road_proxy_policy_config_sha256": policy.config_sha256,
                    "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
                    "proximity_scope": "WITHIN_VERIFIED_SOURCE_PACKAGE",
                }
            )
    table = pd.DataFrame(rows, columns=CLASS_PROXIMITY_COLUMNS)
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")
    table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    coverage = tuple(
        RoadProxyClassCoverage(
            road_proxy_class=road_class,
            feature_count=1,
            distance_eligible=road_class != "NOT_DISTANCE_PROXY",
        )
        for road_class in ALL_CLASSES
    )
    return ParcelRoadProximityResult(source_parcels.copy(), table, coverage)


def _without_match(
    proximity: ParcelRoadProximityResult,
    road_class: str = "UNKNOWN_REVIEW",
) -> ParcelRoadProximityResult:
    table = proximity.class_proximity.copy()
    mask = table["road_proxy_class"].eq(road_class)
    for column in SELECTED_COLUMNS:
        table.loc[mask, column] = pd.NA
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype("Int64")
    table["nearest_road_toll_evidence"] = table["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    coverage = tuple(
        replace(item, feature_count=0) if item.road_proxy_class == road_class else item
        for item in proximity.class_coverage
    )
    return replace(proximity, class_proximity=table, class_coverage=coverage)


def _measured_boundary_distance(
    parcels: gpd.GeoDataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> float:
    geometry = parcels.to_crs("EPSG:2154").geometry.iloc[0]
    return float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))


def _assess(
    *,
    parcels: gpd.GeoDataFrame | None = None,
    proximity: object | None = None,
    coverage: IgnBdTopoDepartmentCoverage | None = None,
    road_source: IgnBdTopoRoadData | None = None,
    source_config: IgnBdTopoSourceConfig = SOURCE_CONFIG,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
    selected_parcels = parcels if parcels is not None else _parcels()
    selected_proximity = (
        proximity if proximity is not None else _proximity(selected_parcels)
    )
    selected_coverage = coverage or _coverage()
    selected_source = road_source or _road_source(selected_coverage.extraction)
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=selected_proximity,
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=selected_coverage,
        ),
    ):
        return assess_road_proximity_coverage(
            selected_parcels,
            selected_source,
            source_config,
            policy_path,
        )


def _first_row(
    result: RoadProximityCoverageAssessmentResult,
    road_class: str = "GENERAL_VEHICLE_PROXY",
) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]


def test_public_api_exports_only_stable_symbols() -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    expected = {
        "RoadProximityCoverageError",
        "RoadProximityCoverageAssessmentResult",
        "assess_road_proximity_coverage",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_coverage_positions")


@pytest.mark.parametrize(
    "argument", ["parcels", "road_source", "source_config", "policy_path"]
)
def test_wrong_public_input_type_is_controlled_and_fast(argument: str) -> None:
    kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "road_source": _road_source(),
        "source_config": SOURCE_CONFIG,
        "policy_path": None,
    }
    kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity"
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(**cast(Any, kwargs))
    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()


def test_source_chain_calls_proximity_then_coverage_exactly_once() -> None:
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity(parcels)
    policy_path = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=proximity,
        ) as proximity_stage,
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=coverage,
        ) as coverage_loader,
    ):
        assess_road_proximity_coverage(parcels, road_source, SOURCE_CONFIG, policy_path)
    proximity_stage.assert_called_once_with(
        parcels, road_source, SOURCE_CONFIG, policy_path
    )
    coverage_loader.assert_called_once_with(road_source.extraction, SOURCE_CONFIG)


def test_proximity_failure_stops_coverage_loading() -> None:
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            side_effect=ValueError("bad proximity"),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(_parcels(), _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()


def test_coverage_loader_failure_is_controlled() -> None:
    parcels = _parcels()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=_proximity(parcels),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            side_effect=ValueError("bad coverage"),
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_called_once()


def test_stage_does_not_construct_a_road_spatial_index() -> None:
    with patch("shapely.STRtree", side_effect=AssertionError("forbidden")):
        _assess()
    source = Path("src/landscout/stages/assess_road_proximity_coverage.py").read_text(
        encoding="utf-8"
    )
    assert "STRtree(" not in source
    assert "query_nearest(" not in source


@pytest.mark.parametrize(
    "mutation",
    [
        lambda result: object(),
        lambda result: replace(result, parcels=result.parcels.drop(columns="geometry")),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.drop(
                columns="nearest_road_proxy_distance_m"
            ),
        ),
        lambda result: replace(
            result, class_proximity=result.class_proximity.iloc[:-1].copy()
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.iloc[
                [1, 0, *range(2, 5)]
            ].reset_index(drop=True),
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.assign(
                proximity_scope="GLOBAL_NEAREST"
            ),
        ),
        lambda result: replace(
            result,
            class_proximity=result.class_proximity.assign(
                road_proxy_policy_config_sha256=["c" * 64, *["d" * 64] * 4]
            ),
        ),
    ],
    ids=[
        "wrong-type",
        "bad-parcels",
        "missing-column",
        "row-count",
        "order",
        "scope",
        "policy-sha",
    ],
)
def test_malformed_upstream_result_fails_before_coverage_load(mutation: Any) -> None:
    parcels = _parcels()
    malformed = mutation(_proximity(parcels))
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=malformed,
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
        ) as coverage_loader,
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_provider", "Other provider"),
        ("source_product", "Other product"),
        ("source_department_code", "32"),
        ("source_edition", "2099-01-01"),
        ("source_product_version", "99"),
        ("source_archive_sha256", "c" * 64),
    ],
)
def test_coverage_package_lineage_must_match_road_archive(
    field: str, value: object
) -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[field] = value
    if field == "source_department_code":
        frame[coverage.summary.department_code_field] = value
        summary = replace(coverage.summary, selected_department_code=cast(str, value))
    else:
        summary = coverage.summary
    forged = replace(coverage, coverage=frame, summary=summary, **{field: value})
    with pytest.raises(
        RoadProximityCoverageError, match="package|lineage|provider|product"
    ):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))


def test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer() -> None:
    coverage = _coverage(layer="zone_administrative")
    with pytest.raises(RoadProximityCoverageError, match="configured|layer"):
        _assess(coverage=coverage, road_source=_road_source(coverage.extraction))


def test_selected_department_identity_is_exact() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[coverage.summary.department_code_field] = "32"
    forged = replace(
        coverage,
        coverage=frame,
        summary=replace(coverage.summary, selected_department_code="32"),
    )
    with pytest.raises(RoadProximityCoverageError, match="department"):
        _assess(coverage=forged)


def test_coverage_spatial_role_and_source_type_are_controlled() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame["spatial_role"] = "PROXY_GEOMETRY"
    wrong_role = replace(
        coverage,
        coverage=frame,
        summary=replace(
            coverage.summary,
            spatial_role=cast(Any, "PROXY_GEOMETRY"),
        ),
        spatial_role=cast(Any, "PROXY_GEOMETRY"),
    )
    with pytest.raises(RoadProximityCoverageError, match="spatial|lineage"):
        _assess(coverage=wrong_role)

    parcels = _parcels()
    with (
        patch(
            "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
            return_value=_proximity(parcels),
        ),
        patch(
            "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
            return_value=object(),
        ),
        pytest.raises(RoadProximityCoverageError),
    ):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)


def test_coverage_must_retain_same_extraction_object() -> None:
    coverage = _coverage()
    forged = replace(coverage, extraction=replace(coverage.extraction))
    with pytest.raises(RoadProximityCoverageError, match="extraction"):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))


@pytest.mark.parametrize(
    ("geometries", "crs", "message"),
    [
        ([], "EPSG:2154", "one|exactly"),
        (
            [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])] * 2,
            "EPSG:2154",
            "one|exactly",
        ),
        ([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])], None, "CRS"),
        ([Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])], "EPSG:4326", "2154"),
        ([None], "EPSG:2154", "null"),
        ([Polygon()], "EPSG:2154", "empty"),
        ([Polygon([(0, 0), (10, 10), (10, 0), (0, 10), (0, 0)])], "EPSG:2154", "valid"),
        ([Point(0, 0)], "EPSG:2154", "Polygon"),
        ([LineString([(0, 0), (10, 10)])], "EPSG:2154", "Polygon"),
    ],
    ids=[
        "zero",
        "two",
        "no-crs",
        "wrong-crs",
        "null",
        "empty",
        "invalid",
        "point",
        "line",
    ],
)
def test_invalid_coverage_geometry_is_rejected(
    geometries: list[object], crs: str | None, message: str
) -> None:
    coverage = _coverage(geometries=geometries, crs=crs)
    with pytest.raises(RoadProximityCoverageError, match=message):
        _assess(coverage=coverage)


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)]),
        MultiPolygon([Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])]),
    ],
)
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    assert len(_assess(coverage=_coverage(geometries=[geometry])).parcels) == 1


@pytest.mark.parametrize(
    ("geometry", "position"),
    [
        (
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            "FULLY_COVERED",
        ),
        (
            Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
        (
            Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
        (
            Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
            "OUTSIDE_OR_CROSSING_COVERAGE",
        ),
    ],
    ids=["inside", "touching", "crossing", "outside"],
)
def test_full_parcel_coverage_position_is_conservative(
    geometry: Polygon, position: str
) -> None:
    parcels = _parcels([geometry])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == position
    if position != "FULLY_COVERED":
        assert row.road_source_boundary_distance_m == 0.0


def test_position_uses_full_geometry_not_centroid() -> None:
    crossing_with_inside_centroid = Polygon(
        [(-10, 100), (-10, 200), (300, 200), (300, 100), (-10, 100)]
    )
    parcels = _parcels([crossing_with_inside_centroid])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert row.road_source_boundary_distance_m == 0.0


def test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative() -> None:
    parcels = _parcels()
    coverage = _coverage()
    expected = _measured_boundary_distance(parcels, coverage)
    result = _assess(parcels=parcels, proximity=_proximity(parcels), coverage=coverage)
    values = result.class_proximity["road_source_boundary_distance_m"]
    assert values.eq(expected).all()
    assert np.isfinite(values).all()
    assert values.ge(0).all()


@pytest.mark.parametrize(
    ("offset", "expected"),
    [
        (-50.0, "NOT_BOUNDARY_LIMITED"),
        (-0.001, "NOT_BOUNDARY_LIMITED"),
        (0.0, "BOUNDARY_LIMITED"),
        (50.0, "BOUNDARY_LIMITED"),
    ],
)
def test_strict_boundary_status_logic(offset: float, expected: str) -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels,
        distances={road_class: margin + offset for road_class in ELIGIBLE_CLASSES},
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert result.class_proximity["road_proximity_coverage_status"].eq(expected).all()


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(-10, 100), (-10, 200), (100, 200), (100, 100), (-10, 100)]),
        Polygon([(0, 100), (0, 200), (100, 200), (100, 100), (0, 100)]),
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
    ],
    ids=["crossing", "touching", "outside"],
)
def test_matched_outside_or_crossing_status(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    result = _assess(parcels=parcels, proximity=_proximity(parcels))
    assert (
        result.class_proximity["road_proximity_coverage_status"]
        .eq("OUTSIDE_OR_CROSSING_COVERAGE")
        .all()
    )


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)]),
    ],
    ids=["inside", "outside"],
)
def test_no_match_takes_precedence_over_coverage_position(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    proximity = _without_match(_proximity(parcels))
    result = _assess(parcels=parcels, proximity=proximity)
    assert (
        _first_row(result, "UNKNOWN_REVIEW").road_proximity_coverage_status
        == "NO_MATCH"
    )


def test_classes_are_diagnosed_independently() -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels,
        distances={
            "GENERAL_VEHICLE_PROXY": margin - 1,
            "RESTRICTED_REVIEW": margin + 1,
        },
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert (
        _first_row(result, "GENERAL_VEHICLE_PROXY").road_proximity_coverage_status
        == "NOT_BOUNDARY_LIMITED"
    )
    assert (
        _first_row(result, "RESTRICTED_REVIEW").road_proximity_coverage_status
        == "BOUNDARY_LIMITED"
    )


def test_exact_coverage_lineage_is_appended_to_every_row() -> None:
    coverage = _coverage()
    result = _assess(coverage=coverage)
    expected = {
        "road_source_coverage_provider": coverage.source_provider,
        "road_source_coverage_product": coverage.source_product,
        "road_source_coverage_department_code": coverage.source_department_code,
        "road_source_coverage_edition": coverage.source_edition,
        "road_source_coverage_product_version": coverage.source_product_version,
        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,
        "road_source_coverage_layer": coverage.source_layer,
        "road_source_coverage_spatial_role": coverage.spatial_role,
    }
    for column, value in expected.items():
        assert result.class_proximity[column].eq(value).all()


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_source_department_code", "32"),
        ("nearest_source_edition", "2099-01-01"),
        ("nearest_source_archive_sha256", "c" * 64),
    ],
)
def test_matched_road_lineage_must_match_coverage(column: str, value: str) -> None:
    proximity = _proximity()
    table = proximity.class_proximity.copy()
    table[column] = value
    with pytest.raises(RoadProximityCoverageError, match="lineage|package"):
        _assess(proximity=replace(proximity, class_proximity=table))


def test_result_preserves_every_upstream_fact_and_input_object() -> None:
    parcels = _parcels(
        [
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            Polygon([(300, 300), (300, 400), (400, 400), (400, 300), (300, 300)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    proximity = _proximity(parcels)
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels_before = deepcopy(parcels)
    proximity_parcels_before = deepcopy(proximity.parcels)
    table_before = deepcopy(proximity.class_proximity)
    coverage_before = deepcopy(coverage.coverage)
    roads_before = deepcopy(road_source.road_segments)
    road_summary_before = road_source.road_segments_summary
    extraction_before = road_source.extraction
    config_before = SOURCE_CONFIG.model_dump(mode="python")
    result = _assess(
        parcels=parcels,
        proximity=proximity,
        coverage=coverage,
        road_source=road_source,
    )

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(proximity.parcels, proximity_parcels_before)
    assert_frame_equal(proximity.class_proximity, table_before)
    assert_geodataframe_equal(coverage.coverage, coverage_before)
    assert_geodataframe_equal(road_source.road_segments, roads_before)
    assert road_source.road_segments_summary == road_summary_before
    assert road_source.extraction is extraction_before
    assert SOURCE_CONFIG.model_dump(mode="python") == config_before
    assert_geodataframe_equal(result.parcels, proximity_parcels_before)
    assert_frame_equal(
        result.class_proximity.loc[:, list(CLASS_PROXIMITY_COLUMNS)],
        table_before,
        check_dtype=True,
        check_index_type=True,
    )
    assert (
        tuple(result.class_proximity.columns[: len(CLASS_PROXIMITY_COLUMNS)])
        == CLASS_PROXIMITY_COLUMNS
    )
    assert (
        tuple(result.class_proximity.columns[len(CLASS_PROXIMITY_COLUMNS) :])
        == DIAGNOSTIC_COLUMNS
    )
    assert result.class_coverage is proximity.class_coverage
    assert result.source_coverage is coverage


def _corrupt_generated(column: str, value: object, *, outside: bool = False) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    geometry = (
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)])
        if outside
        else None
    )
    parcels = _parcels([geometry]) if geometry is not None else _parcels()
    proximity = _proximity(parcels)
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output[column] = output[column].astype("object")
        output.at[0, column] = value
        return output

    with (
        patch.object(module, "_diagnosed_class_proximity", side_effect=corrupt),
        pytest.raises(RoadProximityCoverageError),
    ):
        _assess(parcels=parcels, proximity=proximity)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("road_source_boundary_distance_m", -1.0),
        ("road_source_boundary_distance_m", float("nan")),
        ("road_source_boundary_distance_m", float("inf")),
        ("road_source_coverage_position", "INVENTED"),
        ("road_proximity_coverage_status", "INVENTED"),
    ],
)
def test_malformed_generated_value_is_rejected(column: str, value: object) -> None:
    _corrupt_generated(column, value)


@pytest.mark.parametrize(
    ("distance", "wrong_status"),
    [(50.0, "BOUNDARY_LIMITED"), (150.0, "NOT_BOUNDARY_LIMITED")],
)
def test_inconsistent_generated_status_is_rejected(
    distance: float, wrong_status: str
) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    parcels = _parcels()
    proximity = _proximity(
        parcels, distances={road_class: distance for road_class in ELIGIBLE_CLASSES}
    )
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output.at[0, "road_proximity_coverage_status"] = wrong_status
        return output

    with (
        patch.object(module, "_diagnosed_class_proximity", side_effect=corrupt),
        pytest.raises(RoadProximityCoverageError),
    ):
        _assess(parcels=parcels, proximity=proximity)


def test_outside_position_requires_zero_boundary_distance() -> None:
    _corrupt_generated("road_source_boundary_distance_m", 1.0, outside=True)


def test_result_is_frozen_and_has_no_business_decision_fields() -> None:
    result = _assess()
    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    forbidden = {
        "accessible",
        "road_access_ok",
        "legal_access",
        "truck_access",
        "bess_access",
        "score",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)
```
