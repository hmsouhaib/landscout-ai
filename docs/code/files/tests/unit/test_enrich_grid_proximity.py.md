# `tests/unit/test_enrich_grid_proximity.py`

## File identity

- Repository path: `tests/unit/test_enrich_grid_proximity.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.
- Source SHA256: `436de7dd475f09b28356502b0b4eaed66ead17253da7bf6d3869aaf8bbcee728`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for enrich grid proximity; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `from copy import deepcopy`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pyogrio`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.api.types import is_float_dtype, is_integer_dtype`
- `from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)`
- `from landscout.stages import (
    enrich_parcel_grid_proximity as public_enrich_parcel_grid_proximity,
)`
- `from landscout.stages.enrich_grid_proximity import (
    VOLTAGE_PROXIMITY_COLUMNS,
)`
- `from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)`
- `from landscout.stages.normalize_grid_ign import NormalizedIgnElectricityData`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `OVERFLOWING_INTEGER`

- Category: module constant or closed domain.
- Exact declaration:

```python
OVERFLOWING_INTEGER = 10**10000
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `SOURCE_CONFIG`

- Category: module constant or closed domain.
- Exact declaration:

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_geometry_status`

**Purpose:** Implements `geometry status` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _geometry_status(geometry: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"NULL"`
  - `"EMPTY"`
  - `"INVALID"`
  - `"VALID"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_lines` via `_geometry_status`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_lines` via `_geometry_status`
- direct call: `tests.unit.test_enrich_grid_proximity::_posts` via `_geometry_status`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_posts` via `_geometry_status`

Outbound call expressions and conservative ownership:
- No calls.

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
def _geometry_status(geometry: object) -> str:
    if geometry is None:
        return "NULL"
    if geometry.is_empty:
        return "EMPTY"
    if not geometry.is_valid:
        return "INVALID"
    return "VALID"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `index` | keyword-only | `list[object] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {"parcel_id": ids, "source_value": list(range(count))},<br>        geometry=values,<br>        crs=crs,<br>        index=source_index,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_wrong_source_boundary_types` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_wrong_source_boundary_types` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_reproduces_configured_electricity_roles` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_reproduces_configured_electricity_roles` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_source_normalization_failure_stops_grid_computation` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_source_normalization_failure_stops_grid_computation` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_generated_parcel_column_before_normalization` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_generated_parcel_column_before_normalization` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_parcels`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    source_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_lines`

**Purpose:** Implements `lines` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _lines(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    voltage_statuses: list[str] | None = None,
    voltages: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[str] \| None` | `None` |
| `statuses` | keyword-only | `list[str] \| None` | `None` |
| `voltage_statuses` | keyword-only | `list[str] \| None` | `None` |
| `voltages` | keyword-only | `list[object] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `feature_types` | keyword-only | `list[str] \| None` | `None` |
| `spatial_roles` | keyword-only | `list[str] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "grid_feature_id": ids,<br>            "grid_feature_type": feature_types or ["ELECTRIC_LINE"] * count,<br>            "source_feature_id": [f"SOURCE-{value}" for value in ids],<br>            "source_department_code": ["31"] * count,<br>            "source_edition": ["2026-06-15"] * count,<br>            "source_archive_sha256": ["a" * 64] * count,<br>            "source_layer": ["CUSTOM_LINE_LAYER"] * count,<br>            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,<br>            "geometry_status": geometry_statuses,<br>            "voltage_raw": [<br>                f"{value:g} kV" if isinstance(value, (int, float)) else None<br>                for value in normalized_voltages<br>            ],<br>            "voltage_status": normalized_voltage_statuses,<br>            "voltage_kv": normalized_voltages,<br>            "voltage_upper_bound_kv": [np.nan] * count,<br>            "manager_name": ["TEST MANAGER"] * count,<br>            "asset_status_raw": ["En service"] * count,<br>        },<br>        geometry=values,<br>        crs=crs,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_electricity_source` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_electricity_source` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_lines`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `_lines`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `_lines`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `LineString` | `shapely.geometry.LineString` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geometry_status` | `tests.unit.test_enrich_grid_proximity._geometry_status` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_geometry_status` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _lines(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    voltage_statuses: list[str] | None = None,
    voltages: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [LineString([(110, -20), (110, 30)])]
    count = len(values)
    ids = identifiers or [f"LINE-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    normalized_voltage_statuses = voltage_statuses or ["EXACT"] * count
    normalized_voltages = voltages or [110.0] * count
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["ELECTRIC_LINE"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_LINE_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "voltage_raw": [
                f"{value:g} kV" if isinstance(value, (int, float)) else None
                for value in normalized_voltages
            ],
            "voltage_status": normalized_voltage_statuses,
            "voltage_kv": normalized_voltages,
            "voltage_upper_bound_kv": [np.nan] * count,
            "manager_name": ["TEST MANAGER"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_posts`

**Purpose:** Implements `posts` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _posts(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object] \| None` | `None` |
| `identifiers` | keyword-only | `list[str] \| None` | `None` |
| `statuses` | keyword-only | `list[str] \| None` | `None` |
| `crs` | keyword-only | `str \| None` | `'EPSG:2154'` |
| `feature_types` | keyword-only | `list[str] \| None` | `None` |
| `spatial_roles` | keyword-only | `list[str] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "grid_feature_id": ids,<br>            "grid_feature_type": feature_types or ["TRANSFORMATION_POST"] * count,<br>            "source_feature_id": [f"SOURCE-{value}" for value in ids],<br>            "source_department_code": ["31"] * count,<br>            "source_edition": ["2026-06-15"] * count,<br>            "source_archive_sha256": ["a" * 64] * count,<br>            "source_layer": ["CUSTOM_POST_LAYER"] * count,<br>            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,<br>            "geometry_status": geometry_statuses,<br>            "name": ["Test post"] * count,<br>            "importance_raw": ["5"] * count,<br>            "asset_status_raw": ["En service"] * count,<br>        },<br>        geometry=values,<br>        crs=crs,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_electricity_source` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_electricity_source` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_two_parcel_two_voltage_result` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_separated_distance_uses_parcel_edge_not_centroid` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_touching_line_has_zero_distance` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_post_distance_uses_parcel_and_post_polygons` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_epsg2154_parcel_input_remains_epsg2154` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_valid_parcel_id_is_preserved_exactly` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_parcel_id_hygiene_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_parcel_polygon_geometry_is_preserved` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_semantically_wrong_parcel_geometry_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_crs_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_crs_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_z_line_has_same_horizontal_distance_as_xy_line` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_grid_feature_type_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_grid_feature_id_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_wrong_spatial_role_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_unsupported_valid_grid_geometry_type_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_supported_multi_geometries_are_accepted` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_any_line_preserves_every_voltage_status` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_missing_parcel_column_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_null_parcel_id_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_duplicate_parcel_id_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_bad_parcel_geometry_is_rejected` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_distance_profile_is_threshold_free_and_tracks_ties` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_allows_consistent_missing_manager_and_asset_status` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_posts`
- direct call: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `_posts`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_no_valid_required_grid_feature_is_rejected` via `_posts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `_geometry_status` | `tests.unit.test_enrich_grid_proximity._geometry_status` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_geometry_status` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _posts(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(110, 0), (110, 10), (120, 10), (120, 0), (110, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"POST-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["TRANSFORMATION_POST"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_POST_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "name": ["Test post"] * count,
            "importance_raw": ["5"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_electricity_source`

**Purpose:** Implements `electricity source` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _electricity_source(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `lines` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `posts` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoElectricityData(<br>        extraction=cast(Any, None),<br>        electric_lines=lines if lines is not None else _lines(),<br>        transformation_posts=posts if posts is not None else _posts(),<br>        electric_lines_summary=cast(Any, None),<br>        transformation_posts_summary=cast(Any, None),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_normalizes_verified_source_exactly_once` via `_electricity_source`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_wrong_source_boundary_types` via `_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_wrong_source_boundary_types` via `_electricity_source`
- direct call: `tests.unit.test_enrich_grid_proximity::test_source_normalization_failure_stops_grid_computation` via `_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_source_normalization_failure_stops_grid_computation` via `_electricity_source`
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_generated_parcel_column_before_normalization` via `_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_generated_parcel_column_before_normalization` via `_electricity_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoElectricityData` | `landscout.sources.IgnBdTopoElectricityData` |
| `cast` | `typing.cast` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |

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
def _electricity_source(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
    return IgnBdTopoElectricityData(
        extraction=cast(Any, None),
        electric_lines=lines if lines is not None else _lines(),
        transformation_posts=posts if posts is not None else _posts(),
        electric_lines_summary=cast(Any, None),
        transformation_posts_summary=cast(Any, None),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_physical_line_source`

**Purpose:** Implements `physical line source` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _physical_line_source(
    identifier: str,
    geometry: LineString,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `LineString` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "cleabs": [identifier],<br>            "voltage": ["225 kV"],<br>            "gestionnaire": ["Test manager"],<br>            "siren_gestionnaire": ["444619258"],<br>            "etat_de_l_objet": ["En service"],<br>            "sources": ["Synthetic physical source"],<br>            "identifiants_sources": [f"SOURCE-{identifier}"],<br>            "date_creation": pd.to_datetime(["2024-01-01"]),<br>            "date_modification": pd.to_datetime(["2025-01-01"]),<br>            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),<br>            "methode_d_acquisition_planimetrique": ["Synthetic"],<br>            "precision_planimetrique": [1.0],<br>        },<br>        geometry=[geometry],<br>        crs="EPSG:2154",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_physical_electricity_source` via `_physical_line_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_physical_electricity_source` via `_physical_line_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.to_datetime` | `pandas.to_datetime` |

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
def _physical_line_source(
    identifier: str,
    geometry: LineString,
) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "cleabs": [identifier],
            "voltage": ["225 kV"],
            "gestionnaire": ["Test manager"],
            "siren_gestionnaire": ["444619258"],
            "etat_de_l_objet": ["En service"],
            "sources": ["Synthetic physical source"],
            "identifiants_sources": [f"SOURCE-{identifier}"],
            "date_creation": pd.to_datetime(["2024-01-01"]),
            "date_modification": pd.to_datetime(["2025-01-01"]),
            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),
            "methode_d_acquisition_planimetrique": ["Synthetic"],
            "precision_planimetrique": [1.0],
        },
        geometry=[geometry],
        crs="EPSG:2154",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_physical_post_source`

**Purpose:** Implements `physical post source` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _physical_post_source(
    identifier: str,
    geometry: Polygon,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `Polygon` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "cleabs": [identifier],<br>            "toponyme": ["Test post"],<br>            "statut_du_toponyme": ["Valid"],<br>            "importance": ["5"],<br>            "etat_de_l_objet": ["En service"],<br>            "sources": ["Synthetic physical source"],<br>            "identifiants_sources": [f"SOURCE-{identifier}"],<br>            "date_creation": pd.to_datetime(["2024-01-01"]),<br>            "date_modification": pd.to_datetime(["2025-01-01"]),<br>            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),<br>            "methode_d_acquisition_planimetrique": ["Synthetic"],<br>            "precision_planimetrique": [1.0],<br>        },<br>        geometry=[geometry],<br>        crs="EPSG:2154",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_physical_electricity_source` via `_physical_post_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_physical_electricity_source` via `_physical_post_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.to_datetime` | `pandas.to_datetime` |

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
def _physical_post_source(
    identifier: str,
    geometry: Polygon,
) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "cleabs": [identifier],
            "toponyme": ["Test post"],
            "statut_du_toponyme": ["Valid"],
            "importance": ["5"],
            "etat_de_l_objet": ["En service"],
            "sources": ["Synthetic physical source"],
            "identifiants_sources": [f"SOURCE-{identifier}"],
            "date_creation": pd.to_datetime(["2024-01-01"]),
            "date_modification": pd.to_datetime(["2025-01-01"]),
            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),
            "methode_d_acquisition_planimetrique": ["Synthetic"],
            "precision_planimetrique": [1.0],
        },
        geometry=[geometry],
        crs="EPSG:2154",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_physical_summary`

**Purpose:** Implements `physical summary` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _physical_summary(
    frame: gpd.GeoDataFrame,
    *,
    logical_name: str,
    layer_name: str,
) -> IgnBdTopoLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `logical_name` | keyword-only | `str` | `required` |
| `layer_name` | keyword-only | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoLayerSummary(<br>        logical_name=cast(Any, logical_name),<br>        source_layer_name=layer_name,<br>        crs=str(frame.crs),<br>        feature_count=len(frame),<br>        columns=tuple(str(column) for column in frame.columns),<br>        dtypes=tuple(<br>            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()<br>        ),<br>        null_geometry_count=int(null_mask.sum()),<br>        empty_geometry_count=int(empty_mask.sum()),<br>        invalid_geometry_count=int(invalid_mask.sum()),<br>        geometry_types=tuple(<br>            sorted(<br>                str(value) for value in geometry[~null_mask].geom_type.dropna().unique()<br>            )<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_physical_electricity_source` via `_physical_summary`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_physical_electricity_source` via `_physical_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `IgnBdTopoLayerSummary` | `landscout.sources.IgnBdTopoLayerSummary` |
| `cast` | `typing.cast` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `null_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `empty_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_mask.sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry[~null_mask].geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry[~null_mask].geom_type.dropna().unique`<br>`geometry[~null_mask].geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _physical_summary(
    frame: gpd.GeoDataFrame,
    *,
    logical_name: str,
    layer_name: str,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    return IgnBdTopoLayerSummary(
        logical_name=cast(Any, logical_name),
        source_layer_name=layer_name,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=tuple(
            sorted(
                str(value) for value in geometry[~null_mask].geom_type.dropna().unique()
            )
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_physical_electricity_source`

**Purpose:** Implements `physical electricity source` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _physical_electricity_source(
    tmp_path: Path,
    *,
    alternate_roles: bool,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `alternate_roles` | keyword-only | `bool` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoElectricityData(<br>        extraction=extraction,<br>        electric_lines=selected_lines,<br>        transformation_posts=selected_posts,<br>        electric_lines_summary=_physical_summary(<br>            selected_lines,<br>            logical_name="electric_lines",<br>            layer_name=selected_line_layer,<br>        ),<br>        transformation_posts_summary=_physical_summary(<br>            selected_posts,<br>            logical_name="transformation_posts",<br>            layer_name=selected_post_layer,<br>        ),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::_alternate_role_electricity_source` via `_physical_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_alternate_role_electricity_source` via `_physical_electricity_source`
- direct call: `tests.unit.test_enrich_grid_proximity::_configured_role_electricity_source` via `_physical_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::_configured_role_electricity_source` via `_physical_electricity_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_physical_line_source` | `tests.unit.test_enrich_grid_proximity._physical_line_source` |
| `LineString` | `shapely.geometry.LineString` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_physical_post_source` | `tests.unit.test_enrich_grid_proximity._physical_post_source` |
| `extraction_path.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.write_dataframe` | `pyogrio.write_dataframe` |
| `gpd.read_file` | `geopandas.read_file` |
| `geopackage_path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pyogrio.list_layers` | `pyogrio.list_layers` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `(extraction_path / ".landscout-extraction.json").write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `IgnBdTopoDownload` | `landscout.sources.IgnBdTopoDownload` |
| `Path` | `pathlib.Path` |
| `IgnBdTopoExtraction` | `landscout.sources.IgnBdTopoExtraction` |
| `IgnBdTopoElectricityData` | `landscout.sources.IgnBdTopoElectricityData` |
| `_physical_summary` | `tests.unit.test_enrich_grid_proximity._physical_summary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file`<br>`geopackage_path.read_bytes` |
| Filesystem/archive write or publication | `extraction_path.mkdir`<br>`(extraction_path / ".landscout-extraction.json").write_text` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _physical_electricity_source(
    tmp_path: Path,
    *,
    alternate_roles: bool,
) -> IgnBdTopoElectricityData:
    configured_line_layer = "LIGNE_ELECTRIQUE_CONFIGURED"
    configured_post_layer = "POSTE_DE_TRANSFORMATION_CONFIGURED"
    alternate_line_layer = "CABLE_SOURCE_ALTERNATE"
    alternate_post_layer = "INSTALLATION_SOURCE_ALTERNATE"
    frames = (
        (
            configured_line_layer,
            _physical_line_source(
                "CONFIGURED-LINE",
                LineString([(500, -20), (500, 30)]),
            ),
        ),
        (
            "TRONCON_DE_ROUTE",
            gpd.GeoDataFrame(
                {"id": ["ROAD"]},
                geometry=[LineString([(0, 0), (1, 1)])],
                crs="EPSG:2154",
            ),
        ),
        (
            "DEPARTEMENT",
            gpd.GeoDataFrame(
                {"code_insee": ["31"]},
                geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])],
                crs="EPSG:2154",
            ),
        ),
        (
            configured_post_layer,
            _physical_post_source(
                "CONFIGURED-POST",
                Polygon([(500, 0), (500, 10), (510, 10), (510, 0), (500, 0)]),
            ),
        ),
        (
            alternate_line_layer,
            _physical_line_source(
                "ALTERNATE-LINE",
                LineString([(10, -20), (10, 30)]),
            ),
        ),
        (
            alternate_post_layer,
            _physical_post_source(
                "ALTERNATE-POST",
                Polygon([(10, 0), (10, 10), (20, 10), (20, 0), (10, 0)]),
            ),
        ),
    )
    selected_line_layer = (
        alternate_line_layer if alternate_roles else configured_line_layer
    )
    selected_post_layer = (
        alternate_post_layer if alternate_roles else configured_post_layer
    )
    extraction_path = tmp_path / (
        "alternate-electricity-extraction"
        if alternate_roles
        else "configured-electricity-extraction"
    )
    extraction_path.mkdir()
    geopackage_path = extraction_path / "electricity.gpkg"
    for position, (layer_name, frame) in enumerate(frames):
        pyogrio.write_dataframe(
            frame,
            geopackage_path,
            layer=layer_name,
            driver="GPKG",
            append=position > 0,
        )
    selected_lines = gpd.read_file(
        geopackage_path,
        layer=selected_line_layer,
        engine="pyogrio",
    )
    selected_posts = gpd.read_file(
        geopackage_path,
        layer=selected_post_layer,
        engine="pyogrio",
    )
    payload = geopackage_path.read_bytes()
    digest = sha256(payload).hexdigest()
    layer_names = tuple(
        str(record[0]) for record in pyogrio.list_layers(geopackage_path)
    )
    marker = {
        "schema_version": 3,
        "archive_sha256": "a" * 64,
        "geopackage_relative_path": geopackage_path.name,
        "geopackage_size_bytes": len(payload),
        "geopackage_sha256": digest,
        "all_layer_names": list(layer_names),
        "electric_lines_layer": selected_line_layer,
        "transformation_posts_layer": selected_post_layer,
        "road_segments_layer": "TRONCON_DE_ROUTE",
        "department_layer": "DEPARTEMENT",
        "extracted_entries": [
            {
                "relative_path": geopackage_path.name,
                "kind": "file",
                "size_bytes": len(payload),
                "sha256": digest,
            }
        ],
        "spatial_role": "PROXY_GEOMETRY",
    }
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(marker),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product=SOURCE_CONFIG.product,
        department_code=SOURCE_CONFIG.department_code,
        edition=SOURCE_CONFIG.edition,
        product_version=SOURCE_CONFIG.product_version,
        projection=SOURCE_CONFIG.projection,
        package_format=SOURCE_CONFIG.format,
        archive_format=SOURCE_CONFIG.archive_format,
        source_url=str(SOURCE_CONFIG.source_url),
        checksum_url=(
            str(SOURCE_CONFIG.checksum_url)
            if SOURCE_CONFIG.checksum_url is not None
            else None
        ),
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename=Path(str(SOURCE_CONFIG.source_url)).name,
        file_size=SOURCE_CONFIG.expected_archive_size_bytes or 1,
        sha256="a" * 64,
        official_checksum_algorithm=SOURCE_CONFIG.official_checksum_algorithm,
        official_checksum=SOURCE_CONFIG.official_checksum,
        official_checksum_validated=(SOURCE_CONFIG.official_checksum is not None),
        path=tmp_path / Path(str(SOURCE_CONFIG.source_url)).name,
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename=geopackage_path.name,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer=selected_line_layer,
        transformation_posts_layer=selected_post_layer,
        road_segments_layer="TRONCON_DE_ROUTE",
        department_layer="DEPARTEMENT",
        cache_hit=True,
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=selected_lines,
        transformation_posts=selected_posts,
        electric_lines_summary=_physical_summary(
            selected_lines,
            logical_name="electric_lines",
            layer_name=selected_line_layer,
        ),
        transformation_posts_summary=_physical_summary(
            selected_posts,
            logical_name="transformation_posts",
            layer_name=selected_post_layer,
        ),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_alternate_role_electricity_source`

**Purpose:** Implements `alternate role electricity source` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _alternate_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_physical_electricity_source(tmp_path, alternate_roles=True)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_reproduces_configured_electricity_roles` via `_alternate_role_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_reproduces_configured_electricity_roles` via `_alternate_role_electricity_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_physical_electricity_source` | `tests.unit.test_enrich_grid_proximity._physical_electricity_source` |

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
def _alternate_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
    return _physical_electricity_source(tmp_path, alternate_roles=True)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_configured_role_electricity_source`

**Purpose:** Implements `configured role electricity source` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _configured_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoElectricityData`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_physical_electricity_source(tmp_path, alternate_roles=False)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_configured_role_electricity_source`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_configured_role_electricity_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_physical_electricity_source` | `tests.unit.test_enrich_grid_proximity._physical_electricity_source` |

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
def _configured_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
    return _physical_electricity_source(tmp_path, alternate_roles=False)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_two_parcel_two_voltage_result`

**Purpose:** Implements `two parcel two voltage result` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _two_parcel_two_voltage_result() -> GridProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `GridProximityResult`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `enrich_parcel_grid_proximity(parcels, lines, _posts())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::test_voltage_table_is_exact_ordered_cartesian_product` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_voltage_table_is_exact_ordered_cartesian_product` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_voltage_cartesian_row` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_voltage_cartesian_row` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_duplicate_parcel_voltage_pair` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_duplicate_parcel_voltage_pair` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_voltage_rows_out_of_parcel_order` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_voltage_rows_out_of_parcel_order` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_distance` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_distance` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_identity` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_identity` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_metadata` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_metadata` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_tie_count` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_tie_count` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_tie_count` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_tie_count` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_tie_count` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_tie_count` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_main_match_feature_id` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_main_match_feature_id` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_distance` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_distance` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_exact_match_voltage` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_exact_match_voltage` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_result_parcel_id` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_result_parcel_id` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_required_proximity_column` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_required_proximity_column` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nondeterministic_or_duplicate_coverage` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nondeterministic_or_duplicate_coverage` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_voltage_coverage_level` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_voltage_coverage_level` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_voltage_coverage_feature_count` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_voltage_coverage_feature_count` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_long_table_voltage` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_long_table_voltage` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_long_table_match_lineage` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_long_table_match_lineage` via `_two_parcel_two_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_distance` via `_two_parcel_two_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_distance` via `_two_parcel_two_voltage_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |

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
def _two_parcel_two_voltage_result() -> GridProximityResult:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(40, 0), (40, 10), (50, 10), (50, 0), (40, 0)]),
        ],
        identifiers=["PARCEL-2", "PARCEL-1"],
    )
    lines = _lines(
        [
            LineString([(200, -20), (200, 30)]),
            LineString([(100, -20), (100, 30)]),
        ],
        identifiers=["LINE-275", "LINE-110"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[275.0, 110.0],
    )
    return enrich_parcel_grid_proximity(parcels, lines, _posts())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_mutate_parcel_result`

**Purpose:** Implements `mutate parcel result` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _mutate_parcel_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `GridProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `GridProximityResult` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(result, parcels=parcels)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_distance` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_distance` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_identity` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_identity` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_metadata` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_metadata` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_tie_count` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_inconsistent_global_exact_tie_count` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_tie_count` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_tie_count` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_main_match_feature_id` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_main_match_feature_id` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_distance` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_required_match_distance` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_exact_match_voltage` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_exact_match_voltage` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_result_parcel_id` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_result_parcel_id` via `_mutate_parcel_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_mutate_parcel_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_mutate_parcel_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `parcels[column] = parcels[column].astype("object")`<br>`parcels.at[0, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _mutate_parcel_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    parcels = result.parcels.copy()
    parcels[column] = parcels[column].astype("object")
    parcels.at[0, column] = value
    return replace(result, parcels=parcels)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_mutate_voltage_result`

**Purpose:** Implements `mutate voltage result` within the file role: Provides complete unit and regression coverage for the `enrich_grid_proximity` contracts exercised in this file.

**Exact signature**

```python
def _mutate_voltage_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `GridProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `GridProximityResult` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(result, voltage_level_proximity=table)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `_mutate_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `_mutate_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_tie_count` via `_mutate_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_tie_count` via `_mutate_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_long_table_voltage` via `_mutate_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_invalid_long_table_voltage` via `_mutate_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_long_table_match_lineage` via `_mutate_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_missing_long_table_match_lineage` via `_mutate_voltage_result`
- direct call: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_distance` via `_mutate_voltage_result`
- value/type reference: `tests.unit.test_enrich_grid_proximity::test_profile_rejects_bad_long_table_distance` via `_mutate_voltage_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.voltage_level_proximity.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `table[column] = table[column].astype("object")`<br>`table.at[0, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _mutate_voltage_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    table = result.voltage_level_proximity.copy()
    table[column] = table[column].astype("object")
    table.at[0, column] = value
    return replace(result, voltage_level_proximity=table)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_clean_high_level_api_is_exported`

**Purpose:** Regression invariant: clean high level api is exported. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_clean_high_level_api_is_exported() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert stages.enrich_parcel_grid_proximity is public_enrich_parcel_grid_proximity`
  - `assert stages.profile_grid_proximity is profile_grid_proximity`
  - `assert "enrich_parcel_grid_proximity" in stages.__all__`
  - `assert "profile_grid_proximity" in stages.__all__`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
- No calls.

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
def test_clean_high_level_api_is_exported() -> None:
    assert stages.enrich_parcel_grid_proximity is public_enrich_parcel_grid_proximity
    assert stages.profile_grid_proximity is profile_grid_proximity
    assert "enrich_parcel_grid_proximity" in stages.__all__
    assert "profile_grid_proximity" in stages.__all__
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_proximity_normalizes_verified_source_exactly_once`

**Purpose:** Regression invariant: public proximity normalizes verified source exactly once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_proximity_normalizes_verified_source_exactly_once() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"`
  - `assert result.parcels.loc[0, "nearest_post_grid_feature_id"] == "POST-1"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `_electricity_source` | `tests.unit.test_enrich_grid_proximity._electricity_source` |
| `NormalizedIgnElectricityData` | `landscout.stages.normalize_grid_ign.NormalizedIgnElectricityData` |
| `patch` | `unittest.mock.patch` |
| `public_enrich_parcel_grid_proximity` | `landscout.stages.enrich_parcel_grid_proximity` |
| `normalizer.assert_called_once_with` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_proximity_normalizes_verified_source_exactly_once() -> None:
    parcels = _parcels()
    lines = _lines()
    posts = _posts()
    source = _electricity_source(lines, posts)
    normalized = NormalizedIgnElectricityData(lines, posts)

    with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        return_value=normalized,
        create=True,
    ) as normalizer:
        result = public_enrich_parcel_grid_proximity(parcels, source, SOURCE_CONFIG)

    normalizer.assert_called_once_with(source, SOURCE_CONFIG)
    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
    assert result.parcels.loc[0, "nearest_post_grid_feature_id"] == "POST-1"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_proximity_rejects_wrong_source_boundary_types`

**Purpose:** Regression invariant: public proximity rejects wrong source boundary types. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_proximity_rejects_wrong_source_boundary_types(
    argument: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("argument", ["parcels", "electricity_source", "source_config"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `argument` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_electricity_source` | `tests.unit.test_enrich_grid_proximity._electricity_source` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `public_enrich_parcel_grid_proximity` | `landscout.stages.enrich_parcel_grid_proximity` |
| `cast` | `typing.cast` |
| `normalizer.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_public_proximity_rejects_wrong_source_boundary_types(
    argument: str,
) -> None:
    kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "electricity_source": _electricity_source(),
        "source_config": SOURCE_CONFIG,
    }
    kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
            create=True,
        ) as normalizer,
        pytest.raises(GridProximityError),
    ):
        public_enrich_parcel_grid_proximity(**cast(Any, kwargs))

    normalizer.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_caller_crafted_normalized_grid_frame_is_not_a_public_source`

**Purpose:** Regression invariant: caller crafted normalized grid frame is not a public source. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_caller_crafted_normalized_grid_frame_is_not_a_public_source() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>            GridProximityError,<br>            match="IgnBdTopoElectricityData\|electricity source",<br>        )`
- Exact assertions:
  - `assert forged_lines["source_department_code"].eq("31").all()`
  - `assert forged_lines["source_edition"].eq("2026-06-15").all()`
  - `assert forged_lines["source_archive_sha256"].eq("a" * 64).all()`
  - `assert forged_lines["spatial_role"].eq("PROXY_GEOMETRY").all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `forged_lines["source_department_code"].eq("31").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_lines["source_department_code"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_lines["source_edition"].eq("2026-06-15").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_lines["source_edition"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_lines["source_archive_sha256"].eq("a" * 64).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_lines["source_archive_sha256"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_lines["spatial_role"].eq("PROXY_GEOMETRY").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `forged_lines["spatial_role"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `public_enrich_parcel_grid_proximity` | `landscout.stages.enrich_parcel_grid_proximity` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `cast` | `typing.cast` |
| `normalizer.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `forged_lines["source_archive_sha256"].eq("a" * 64).all`<br>`forged_lines["source_archive_sha256"].eq` |
| CRS/geometry/spatial calculation | `forged_lines["spatial_role"].eq("PROXY_GEOMETRY").all` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_caller_crafted_normalized_grid_frame_is_not_a_public_source() -> None:
    forged_lines = _lines(
        [LineString([(10, -20), (10, 30)])],
        identifiers=["IGN_BDTOPO:ELECTRIC_LINE:FORGED"],
    )
    assert forged_lines["source_department_code"].eq("31").all()
    assert forged_lines["source_edition"].eq("2026-06-15").all()
    assert forged_lines["source_archive_sha256"].eq("a" * 64).all()
    assert forged_lines["spatial_role"].eq("PROXY_GEOMETRY").all()

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
            create=True,
        ) as normalizer,
        pytest.raises(
            GridProximityError,
            match="IgnBdTopoElectricityData|electricity source",
        ),
    ):
        public_enrich_parcel_grid_proximity(
            _parcels(),
            cast(Any, forged_lines),
            SOURCE_CONFIG,
        )

    normalizer.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_proximity_reproduces_configured_electricity_roles`

**Purpose:** Regression invariant: public proximity reproduces configured electricity roles. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_proximity_reproduces_configured_electricity_roles(
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
  - `pytest.raises(GridProximityError)`
- Exact assertions:
  - `assert forged.extraction.electric_lines_layer == "CABLE_SOURCE_ALTERNATE"`
  - `assert (<br>        forged.extraction.transformation_posts_layer == "INSTALLATION_SOURCE_ALTERNATE"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_alternate_role_electricity_source` | `tests.unit.test_enrich_grid_proximity._alternate_role_electricity_source` |
| `pytest.raises` | `pytest.raises` |
| `public_enrich_parcel_grid_proximity` | `landscout.stages.enrich_parcel_grid_proximity` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |

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
def test_public_proximity_reproduces_configured_electricity_roles(
    tmp_path: Path,
) -> None:
    forged = _alternate_role_electricity_source(tmp_path)
    assert forged.extraction.electric_lines_layer == "CABLE_SOURCE_ALTERNATE"
    assert (
        forged.extraction.transformation_posts_layer == "INSTALLATION_SOURCE_ALTERNATE"
    )

    with pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_proximity_rejects_archive_lineage_differing_from_config`

**Purpose:** Regression invariant: public proximity rejects archive lineage differing from config. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_proximity_rejects_archive_lineage_differing_from_config(
    tmp_path: Path,
    archive_changes: dict[str, object],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "archive_changes",
    [
        pytest.param({"provider": "IGN"}, id="provider"),
        pytest.param({"product": "BDTOPO"}, id="product"),
        pytest.param({"edition": "2026-06-16"}, id="edition"),
        pytest.param({"product_version": "3.6"}, id="product-version"),
        pytest.param(
            {"projection": "urn:ogc:def:crs:EPSG::2154"},
            id="projection",
        ),
        pytest.param({"package_format": "SHP"}, id="package-format"),
        pytest.param({"archive_format": "zip"}, id="archive-format"),
        pytest.param(
            {"source_url": "https://example.test/other-package.7z"},
            id="source-url",
        ),
        pytest.param(
            {"checksum_url": "https://example.test/other-package.md5"},
            id="checksum-url",
        ),
        pytest.param(
            {
                "official_checksum_algorithm": "sha256",
                "official_checksum": "b" * 64,
                "official_checksum_validated": True,
            },
            id="official-checksum",
        ),
        pytest.param(
            {"file_size": (SOURCE_CONFIG.expected_archive_size_bytes or 1) + 1},
            id="archive-size",
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `archive_changes` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_configured_role_electricity_source` | `tests.unit.test_enrich_grid_proximity._configured_role_electricity_source` |
| `replace` | `dataclasses.replace` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `public_enrich_parcel_grid_proximity` | `landscout.stages.enrich_parcel_grid_proximity` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `computation.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `pytest.param` | `pytest.param` |

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
def test_public_proximity_rejects_archive_lineage_differing_from_config(
    tmp_path: Path,
    archive_changes: dict[str, object],
) -> None:
    source = _configured_role_electricity_source(tmp_path)
    forged_archive = replace(source.extraction.archive, **archive_changes)
    forged = replace(
        source,
        extraction=replace(source.extraction, archive=forged_archive),
    )

    with (
        patch(
            "landscout.stages.enrich_grid_proximity."
            "_enrich_parcel_grid_proximity_from_normalized",
        ) as computation,
        pytest.raises(GridProximityError),
    ):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)

    computation.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_normalization_failure_stops_grid_computation`

**Purpose:** Regression invariant: source normalization failure stops grid computation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_normalization_failure_stops_grid_computation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_electricity_source` | `tests.unit.test_enrich_grid_proximity._electricity_source` |
| `patch` | `unittest.mock.patch` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `public_enrich_parcel_grid_proximity` | `landscout.stages.enrich_parcel_grid_proximity` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `normalizer.assert_called_once_with` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_source_normalization_failure_stops_grid_computation() -> None:
    source = _electricity_source()

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
            side_effect=ValueError("physical source changed"),
            create=True,
        ) as normalizer,
        pytest.raises(GridProximityError),
    ):
        public_enrich_parcel_grid_proximity(_parcels(), source, SOURCE_CONFIG)

    normalizer.assert_called_once_with(source, SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_separated_distance_uses_parcel_edge_not_centroid`

**Purpose:** Regression invariant: separated distance uses parcel edge not centroid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_separated_distance_uses_parcel_edge_not_centroid() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(<br>        100.0<br>    )`
  - `assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(<br>        100.0<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.approx` | `pytest.approx` |

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
def test_separated_distance_uses_parcel_edge_not_centroid() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0
    )
    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        100.0
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_touching_line_has_zero_distance`

**Purpose:** Regression invariant: touching line has zero distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_touching_line_has_zero_distance() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == 0.0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |

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
def test_touching_line_has_zero_distance() -> None:
    touching = _lines([LineString([(10, -20), (10, 30)])])

    result = enrich_parcel_grid_proximity(_parcels(), touching, _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == 0.0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_post_distance_uses_parcel_and_post_polygons`

**Purpose:** Regression invariant: post distance uses parcel and post polygons. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_post_distance_uses_parcel_and_post_polygons() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(50.0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `Polygon` | `shapely.geometry.Polygon` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `pytest.approx` | `pytest.approx` |

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
def test_post_distance_uses_parcel_and_post_polygons() -> None:
    posts = _posts([Polygon([(60, 0), (60, 10), (70, 10), (70, 0), (60, 0)])])

    result = enrich_parcel_grid_proximity(_parcels(), _lines(), posts)

    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(50.0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_epsg4326_input_is_calculated_in_lambert93_and_preserved`

**Purpose:** Regression invariant: epsg4326 input is calculated in lambert93 and preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_epsg4326_input_is_calculated_in_lambert93_and_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.crs == geographic.crs`
  - `assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(<br>        100.0, abs=1e-6<br>    )`
  - `assert result.parcels.geometry.geom_equals_exact(<br>        before_geometry.reset_index(drop=True), tolerance=0<br>    ).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `projected.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `geographic.geometry.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.approx` | `pytest.approx` |
| `result.parcels.geometry.geom_equals_exact(<br>        before_geometry.reset_index(drop=True), tolerance=0<br>    ).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.geometry.geom_equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |
| `before_geometry.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `projected.to_crs`<br>`geographic.geometry.copy`<br>`result.parcels.geometry.geom_equals_exact(<br>        before_geometry.reset_index(drop=True), tolerance=0<br>    ).all`<br>`result.parcels.geometry.geom_equals_exact`<br>`before_geometry.reset_index` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_epsg4326_input_is_calculated_in_lambert93_and_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    before_geometry = geographic.geometry.copy()

    result = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    assert result.parcels.crs == geographic.crs
    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )
    assert result.parcels.geometry.geom_equals_exact(
        before_geometry.reset_index(drop=True), tolerance=0
    ).all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_epsg2154_parcel_input_remains_epsg2154`

**Purpose:** Regression invariant: epsg2154 parcel input remains epsg2154. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_epsg2154_parcel_input_remains_epsg2154() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.crs is not None`
  - `assert result.parcels.crs.to_epsg() == 2154`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `result.parcels.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_epsg2154_parcel_input_remains_epsg2154() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.crs is not None
    assert result.parcels.crs.to_epsg() == 2154
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_parcel_id_is_preserved_exactly`

**Purpose:** Regression invariant: valid parcel id is preserved exactly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_parcel_id_is_preserved_exactly() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels["parcel_id"].tolist() == ["FR-31-VALID-ID"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `result.parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_valid_parcel_id_is_preserved_exactly() -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(identifiers=["FR-31-VALID-ID"]), _lines(), _posts()
    )

    assert result.parcels["parcel_id"].tolist() == ["FR-31-VALID-ID"]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_proximity_rejects_generated_parcel_column_before_normalization`

**Purpose:** Regression invariant: public proximity rejects generated parcel column before normalization. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_proximity_rejects_generated_parcel_column_before_normalization() -> (
    None
):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="collides.*generated")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `public_enrich_parcel_grid_proximity` | `landscout.stages.enrich_parcel_grid_proximity` |
| `_electricity_source` | `tests.unit.test_enrich_grid_proximity._electricity_source` |
| `normalize.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `parcels["nearest_line_proxy_distance_m"] = 123.0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_public_proximity_rejects_generated_parcel_column_before_normalization() -> (
    None
):
    parcels = _parcels()
    parcels["nearest_line_proxy_distance_m"] = 123.0

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity"
        ) as normalize,
        pytest.raises(GridProximityError, match="collides.*generated"),
    ):
        public_enrich_parcel_grid_proximity(
            parcels,
            _electricity_source(),
            SOURCE_CONFIG,
        )

    normalize.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_parcel_id_hygiene_is_rejected`

**Purpose:** Regression invariant: invalid parcel id hygiene is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_parcel_id_hygiene_is_rejected(identifier: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " PARCEL-1", "PARCEL-1 ", 123],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `identifier` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
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
def test_invalid_parcel_id_hygiene_is_rejected(identifier: object) -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[identifier]), _lines(), _posts()
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_supported_parcel_polygon_geometry_is_preserved`

**Purpose:** Regression invariant: supported parcel polygon geometry is preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_supported_parcel_polygon_geometry_is_preserved(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        MultiPolygon([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]),
        Polygon([(0, 0, 5), (0, 10, 5), (10, 10, 5), (10, 0, 5), (0, 0, 5)]),
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
  - `assert result.parcels.geometry.iloc[0].equals_exact(geometry, tolerance=0)`
  - `assert result.parcels.geometry.iloc[0].has_z == geometry.has_z`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `result.parcels.geometry.iloc[0].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |
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
| CRS/geometry/spatial calculation | `result.parcels.geometry.iloc[0].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_supported_parcel_polygon_geometry_is_preserved(geometry: object) -> None:
    result = enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())

    assert result.parcels.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert result.parcels.geometry.iloc[0].has_z == geometry.has_z
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_semantically_wrong_parcel_geometry_is_rejected`

**Purpose:** Regression invariant: semantically wrong parcel geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_semantically_wrong_parcel_geometry_is_rejected(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Point(1, 1),
        LineString([(0, 0), (10, 10)]),
        MultiLineString([[(0, 0), (10, 10)]]),
        GeometryCollection([Point(1, 1)]),
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
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="Polygon\|MultiPolygon")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Point` | `shapely.geometry.Point` |
| `LineString` | `shapely.geometry.LineString` |
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `GeometryCollection` | `shapely.geometry.GeometryCollection` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `GeometryCollection` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_semantically_wrong_parcel_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(GridProximityError, match="Polygon|MultiPolygon"):
        enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_crs_is_rejected`

**Purpose:** Regression invariant: missing crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_crs_is_rejected(kind: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("kind", ["parcel", "line", "post"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
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
def test_missing_crs_is_rejected(kind: str) -> None:
    parcels = _parcels(crs=None if kind == "parcel" else "EPSG:2154")
    lines = _lines(crs=None if kind == "line" else "EPSG:2154")
    posts = _posts(crs=None if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="CRS"):
        enrich_parcel_grid_proximity(parcels, lines, posts)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_grid_crs_is_rejected`

**Purpose:** Regression invariant: wrong grid crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_grid_crs_is_rejected(kind: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("kind", ["line", "post"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="2154")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
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
def test_wrong_grid_crs_is_rejected(kind: str) -> None:
    lines = _lines(crs="EPSG:4326" if kind == "line" else "EPSG:2154")
    posts = _posts(crs="EPSG:4326" if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="2154"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_z_line_has_same_horizontal_distance_as_xy_line`

**Purpose:** Regression invariant: z line has same horizontal distance as xy line. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_z_line_has_same_horizontal_distance_as_xy_line() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert xyz.geometry.iloc[0].has_z`
  - `assert xyz_result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(<br>        xy_result.parcels.loc[0, "nearest_line_proxy_distance_m"]<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.approx` | `pytest.approx` |

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
def test_z_line_has_same_horizontal_distance_as_xy_line() -> None:
    xy = _lines([LineString([(110, -20), (110, 30)])])
    xyz = _lines([LineString([(110, -20, 500), (110, 30, 900)])])

    xy_result = enrich_parcel_grid_proximity(_parcels(), xy, _posts())
    xyz_result = enrich_parcel_grid_proximity(_parcels(), xyz, _posts())

    assert xyz.geometry.iloc[0].has_z
    assert xyz_result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        xy_result.parcels.loc[0, "nearest_line_proxy_distance_m"]
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_tie_is_counted_and_lexical_feature_id_wins`

**Purpose:** Regression invariant: line tie is counted and lexical feature id wins. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_tie_is_counted_and_lexical_feature_id_wins() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["nearest_line_proxy_distance_m"] == pytest.approx(100.0)`
  - `assert row["nearest_line_tie_count"] == 2`
  - `assert row["nearest_line_grid_feature_id"] == "A-LINE"`
  - `assert row["nearest_exact_line_tie_count"] == 2`
  - `assert row["nearest_exact_line_grid_feature_id"] == "A-LINE"`
  - `assert result.voltage_level_proximity.loc[0, "tie_count"] == 2`
  - `assert (<br>        result.voltage_level_proximity.loc[0, "nearest_line_grid_feature_id"]<br>        == "A-LINE"<br>    )`
  - `assert len(result.parcels) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.approx` | `pytest.approx` |
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
def test_line_tie_is_counted_and_lexical_feature_id_wins() -> None:
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_proxy_distance_m"] == pytest.approx(100.0)
    assert row["nearest_line_tie_count"] == 2
    assert row["nearest_line_grid_feature_id"] == "A-LINE"
    assert row["nearest_exact_line_tie_count"] == 2
    assert row["nearest_exact_line_grid_feature_id"] == "A-LINE"
    assert result.voltage_level_proximity.loc[0, "tie_count"] == 2
    assert (
        result.voltage_level_proximity.loc[0, "nearest_line_grid_feature_id"]
        == "A-LINE"
    )
    assert len(result.parcels) == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cross_voltage_tie_uses_lexical_global_feature_id`

**Purpose:** Regression invariant: cross voltage tie uses lexical global feature id. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cross_voltage_tie_uses_lexical_global_feature_id() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["nearest_exact_line_proxy_distance_m"] == pytest.approx(100.0)`
  - `assert row["nearest_exact_line_grid_feature_id"] == "A-LINE-275"`
  - `assert row["nearest_exact_line_voltage_kv"] == 275.0`
  - `assert row["nearest_exact_line_tie_count"] == 2`
  - `assert result.voltage_level_proximity[<br>        "nearest_line_proxy_distance_m"<br>    ].tolist() == pytest.approx([100.0, 100.0])`
  - `assert result.voltage_level_proximity["tie_count"].tolist() == [1, 1]`
  - `assert profile.nearest_exact_line.tie_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `pytest.approx` | `pytest.approx` |
| `result.voltage_level_proximity[<br>        "nearest_line_proxy_distance_m"<br>    ].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity["tie_count"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.voltage_level_proximity[<br>        "nearest_line_proxy_distance_m"<br>    ].tolist` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_cross_voltage_tie_uses_lexical_global_feature_id() -> None:
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE-110", "A-LINE-275"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[110.0, 275.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
    profile = profile_grid_proximity(result)

    row = result.parcels.iloc[0]
    assert row["nearest_exact_line_proxy_distance_m"] == pytest.approx(100.0)
    assert row["nearest_exact_line_grid_feature_id"] == "A-LINE-275"
    assert row["nearest_exact_line_voltage_kv"] == 275.0
    assert row["nearest_exact_line_tie_count"] == 2
    assert result.voltage_level_proximity[
        "nearest_line_proxy_distance_m"
    ].tolist() == pytest.approx([100.0, 100.0])
    assert result.voltage_level_proximity["tie_count"].tolist() == [1, 1]
    assert profile.nearest_exact_line.tie_count == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_nonvalid_grid_geometries_are_excluded_without_row_loss`

**Purpose:** Regression invariant: nonvalid grid geometries are excluded without row loss. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_nonvalid_grid_geometries_are_excluded_without_row_loss() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.parcels) == 1`
  - `assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "VALID"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
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
def test_nonvalid_grid_geometries_are_excluded_without_row_loss() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    lines = _lines(
        [None, LineString(), invalid, LineString([(110, -20), (110, 30)])],
        identifiers=["NULL", "EMPTY", "INVALID", "VALID"],
        voltage_statuses=["UNKNOWN", "UNKNOWN", "UNKNOWN", "EXACT"],
        voltages=[None, None, None, 110.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert len(result.parcels) == 1
    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "VALID"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_grid_feature_type_is_rejected`

**Purpose:** Regression invariant: wrong grid feature type is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_grid_feature_type_is_rejected(kind: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("kind", ["line", "post"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="grid_feature_type")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
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
def test_wrong_grid_feature_type_is_rejected(kind: str) -> None:
    lines = _lines(feature_types=["WRONG"] if kind == "line" else None)
    posts = _posts(feature_types=["WRONG"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="grid_feature_type"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_grid_feature_id_is_rejected`

**Purpose:** Regression invariant: duplicate grid feature id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_grid_feature_id_is_rejected(kind: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("kind", ["line", "post"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
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
def test_duplicate_grid_feature_id_is_rejected(kind: str) -> None:
    if kind == "line":
        lines = _lines(
            [LineString([(100, 0), (100, 10)])] * 2,
            identifiers=["DUPLICATE", "DUPLICATE"],
        )
        posts = _posts()
    else:
        lines = _lines()
        posts = _posts(
            [
                Polygon([(50, 0), (50, 5), (55, 5), (55, 0), (50, 0)]),
                Polygon([(60, 0), (60, 5), (65, 5), (65, 0), (60, 0)]),
            ],
            identifiers=["DUPLICATE", "DUPLICATE"],
        )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_spatial_role_is_rejected`

**Purpose:** Regression invariant: wrong spatial role is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_spatial_role_is_rejected(kind: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("kind", ["line", "post"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="PROXY_GEOMETRY")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
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
def test_wrong_spatial_role_is_rejected(kind: str) -> None:
    lines = _lines(spatial_roles=["EXACT"] if kind == "line" else None)
    posts = _posts(spatial_roles=["EXACT"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="PROXY_GEOMETRY"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unsupported_valid_grid_geometry_type_is_rejected`

**Purpose:** Regression invariant: unsupported valid grid geometry type is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unsupported_valid_grid_geometry_type_is_rejected(
    kind: str, geometry: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("kind", "geometry"),
    [
        ("line", Point(100, 0)),
        ("line", Polygon([(100, 0), (100, 5), (105, 5), (105, 0), (100, 0)])),
        ("post", Point(100, 0)),
        ("post", LineString([(100, 0), (100, 10)])),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="geometry types")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Point` | `shapely.geometry.Point` |
| `Polygon` | `shapely.geometry.Polygon` |
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
def test_unsupported_valid_grid_geometry_type_is_rejected(
    kind: str, geometry: object
) -> None:
    lines = _lines([geometry]) if kind == "line" else _lines()
    posts = _posts([geometry]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="geometry types"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_supported_multi_geometries_are_accepted`

**Purpose:** Regression invariant: supported multi geometries are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_supported_multi_geometries_are_accepted() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.parcels) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |
| `Polygon` | `shapely.geometry.Polygon` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
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
def test_supported_multi_geometries_are_accepted() -> None:
    lines = _lines(
        [MultiLineString([[(110, -20), (110, 30)], [(120, -20), (120, 30)]])]
    )
    posts = _posts(
        [MultiPolygon([Polygon([(110, 0), (110, 5), (115, 5), (115, 0), (110, 0)])])]
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, posts)

    assert len(result.parcels) == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_nearest_any_line_preserves_every_voltage_status`

**Purpose:** Regression invariant: nearest any line preserves every voltage status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_nearest_any_line_preserves_every_voltage_status(status: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "status", ["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.loc[0, "nearest_line_voltage_status"] == status`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
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
def test_nearest_any_line_preserves_every_voltage_status(status: str) -> None:
    voltage = 110.0 if status == "EXACT" else None
    lines = _lines(voltage_statuses=[status], voltages=[voltage])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_voltage_status"] == status
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_nearest_exact_and_voltage_table_exclude_nonexact_lines`

**Purpose:** Regression invariant: nearest exact and voltage table exclude nonexact lines. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_nearest_exact_and_voltage_table_exclude_nonexact_lines() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row["nearest_line_grid_feature_id"] == "BELOW"`
  - `assert row["nearest_exact_line_grid_feature_id"] == "EXACT-110"`
  - `assert row["nearest_exact_line_voltage_kv"] == 110.0`
  - `assert result.voltage_level_proximity["voltage_kv"].tolist() == [110.0, 275.0]`
  - `assert len(result.voltage_level_proximity) == 2`
  - `assert list(result.voltage_level_proximity.columns) == list(<br>        VOLTAGE_PROXIMITY_COLUMNS<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `result.voltage_level_proximity["voltage_kv"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_nearest_exact_and_voltage_table_exclude_nonexact_lines() -> None:
    lines = _lines(
        [
            LineString([(20, -20), (20, 30)]),
            LineString([(110, -20), (110, 30)]),
            LineString([(210, -20), (210, 30)]),
        ],
        identifiers=["BELOW", "EXACT-110", "EXACT-275"],
        voltage_statuses=["BELOW", "EXACT", "EXACT"],
        voltages=[None, 110.0, 275.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_grid_feature_id"] == "BELOW"
    assert row["nearest_exact_line_grid_feature_id"] == "EXACT-110"
    assert row["nearest_exact_line_voltage_kv"] == 110.0
    assert result.voltage_level_proximity["voltage_kv"].tolist() == [110.0, 275.0]
    assert len(result.voltage_level_proximity) == 2
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_voltage_table_is_exact_ordered_cartesian_product`

**Purpose:** Regression invariant: voltage table is exact ordered cartesian product. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_voltage_table_is_exact_ordered_cartesian_product() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(item.voltage_kv for item in result.voltage_level_coverage) == (<br>        110.0,<br>        275.0,<br>    )`
  - `assert len(result.voltage_level_proximity) == 4`
  - `assert not result.voltage_level_proximity.duplicated(<br>        ["parcel_id", "voltage_kv"]<br>    ).any()`
  - `assert rows["parcel_id"].tolist() == ["PARCEL-2", "PARCEL-1"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity.duplicated(<br>        ["parcel_id", "voltage_kv"]<br>    ).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_voltage_table_is_exact_ordered_cartesian_product() -> None:
    result = _two_parcel_two_voltage_result()

    assert tuple(item.voltage_kv for item in result.voltage_level_coverage) == (
        110.0,
        275.0,
    )
    assert len(result.voltage_level_proximity) == 4
    assert not result.voltage_level_proximity.duplicated(
        ["parcel_id", "voltage_kv"]
    ).any()
    for voltage_kv in (110.0, 275.0):
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == voltage_kv
        ]
        assert rows["parcel_id"].tolist() == ["PARCEL-2", "PARCEL-1"]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_exact_voltage_values_are_not_used_as_exact`

**Purpose:** Regression invariant: invalid exact voltage values are not used as exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_exact_voltage_values_are_not_used_as_exact() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()`
  - `assert result.voltage_level_proximity.empty`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `result.parcels["nearest_exact_line_proxy_distance_m"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_proxy_distance_m"].isna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels["nearest_exact_line_proxy_distance_m"].isna().all`<br>`result.parcels["nearest_exact_line_proxy_distance_m"].isna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_exact_voltage_values_are_not_used_as_exact() -> None:
    lines = _lines(
        [LineString([(20, -20), (20, 30)])] * 4,
        identifiers=["ZERO", "NEGATIVE", "INFINITE", "TEXT"],
        voltage_statuses=["EXACT"] * 4,
        voltages=[0.0, -1.0, float("inf"), "110"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.voltage_level_proximity.empty
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table`

**Purpose:** Regression invariant: no exact voltage preserves parcels and returns empty long table. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"`
  - `assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()`
  - `assert result.parcels["nearest_exact_line_grid_feature_id"].isna().all()`
  - `assert result.voltage_level_proximity.empty`
  - `assert list(result.voltage_level_proximity.columns) == list(<br>        VOLTAGE_PROXIMITY_COLUMNS<br>    )`
  - `assert is_float_dtype(result.parcels["nearest_exact_line_proxy_distance_m"].dtype)`
  - `assert is_float_dtype(result.parcels["nearest_exact_line_voltage_kv"].dtype)`
  - `assert is_integer_dtype(result.parcels["nearest_exact_line_tie_count"].dtype)`
  - `assert str(result.parcels["nearest_exact_line_tie_count"].dtype) == "Int64"`
  - `assert is_float_dtype(result.voltage_level_proximity["voltage_kv"].dtype)`
  - `assert is_float_dtype(<br>        result.voltage_level_proximity["nearest_line_proxy_distance_m"].dtype<br>    )`
  - `assert str(result.voltage_level_proximity["tie_count"].dtype) == "Int64"`
  - `assert result.voltage_level_coverage == ()`
  - `assert profile.nearest_exact_line.count == 0`
  - `assert profile.nearest_exact_line.missing_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `result.parcels["nearest_exact_line_proxy_distance_m"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_proxy_distance_m"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_grid_feature_id"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_grid_feature_id"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `is_float_dtype` | `pandas.api.types.is_float_dtype` |
| `is_integer_dtype` | `pandas.api.types.is_integer_dtype` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels["nearest_exact_line_proxy_distance_m"].isna().all`<br>`result.parcels["nearest_exact_line_proxy_distance_m"].isna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table() -> None:
    lines = _lines(voltage_statuses=["UNKNOWN"], voltages=[None])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_grid_feature_id"].isna().all()
    assert result.voltage_level_proximity.empty
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
    assert is_float_dtype(result.parcels["nearest_exact_line_proxy_distance_m"].dtype)
    assert is_float_dtype(result.parcels["nearest_exact_line_voltage_kv"].dtype)
    assert is_integer_dtype(result.parcels["nearest_exact_line_tie_count"].dtype)
    assert str(result.parcels["nearest_exact_line_tie_count"].dtype) == "Int64"
    assert is_float_dtype(result.voltage_level_proximity["voltage_kv"].dtype)
    assert is_float_dtype(
        result.voltage_level_proximity["nearest_line_proxy_distance_m"].dtype
    )
    assert str(result.voltage_level_proximity["tie_count"].dtype) == "Int64"
    assert result.voltage_level_coverage == ()
    profile = profile_grid_proximity(result)
    assert profile.nearest_exact_line.count == 0
    assert profile.nearest_exact_line.missing_count == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_parcel_column_is_rejected`

**Purpose:** Regression invariant: missing parcel column is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_parcel_column_is_rejected(column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["parcel_id", "geometry"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match=column)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels().drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
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
| In-memory mutation | `_parcels().drop(columns=column)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_parcel_column_is_rejected(column: str) -> None:
    parcels = _parcels().drop(columns=column)

    with pytest.raises(GridProximityError, match=column):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_parcel_id_is_rejected`

**Purpose:** Regression invariant: null parcel id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_parcel_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |

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
def test_null_parcel_id_is_rejected() -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(_parcels(identifiers=[None]), _lines(), _posts())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_id_is_rejected`

**Purpose:** Regression invariant: duplicate parcel id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |

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
def test_duplicate_parcel_id_is_rejected() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_bad_parcel_geometry_is_rejected`

**Purpose:** Regression invariant: bad parcel geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_bad_parcel_geometry_is_rejected(geometry: object, message: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null"),
        (Polygon(), "empty"),
        (
            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),
            "valid",
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
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
def test_bad_parcel_geometry_is_rejected(geometry: object, message: str) -> None:
    with pytest.raises(GridProximityError, match=message):
        enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved`

**Purpose:** Regression invariant: inputs are not mutated and parcel order and ids are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels["parcel_id"].tolist() == [<br>        "SECOND-SPATIAL",<br>        "FIRST-SPATIAL",<br>    ]`
  - `assert isinstance(result.parcels.index, pd.RangeIndex)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `deepcopy` | `copy.deepcopy` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `result.parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved() -> None:
    parcels = _parcels(
        [
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND-SPATIAL", "FIRST-SPATIAL"],
        index=[99, 99],
    )
    lines = _lines()
    posts = _posts()
    parcels_before = deepcopy(parcels)
    lines_before = deepcopy(lines)
    posts_before = deepcopy(posts)

    result = enrich_parcel_grid_proximity(parcels, lines, posts)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(lines, lines_before)
    assert_geodataframe_equal(posts, posts_before)
    assert result.parcels["parcel_id"].tolist() == [
        "SECOND-SPATIAL",
        "FIRST-SPATIAL",
    ]
    assert isinstance(result.parcels.index, pd.RangeIndex)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_distance_profile_is_threshold_free_and_tracks_ties`

**Purpose:** Regression invariant: distance profile is threshold free and tracks ties. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_distance_profile_is_threshold_free_and_tracks_ties() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.parcel_count == 2`
  - `assert profile.nearest_line.count == 2`
  - `assert profile.nearest_line.missing_count == 0`
  - `assert profile.nearest_line.minimum == pytest.approx(50.0)`
  - `assert profile.nearest_line.p50 == pytest.approx(75.0)`
  - `assert profile.nearest_line.maximum == pytest.approx(100.0)`
  - `assert profile.nearest_line.tie_count == 1`
  - `assert profile.voltage_levels[0].voltage_kv == 110.0`
  - `assert profile.voltage_levels[0].line_feature_count == 2`
  - `assert profile.voltage_levels[0].parcel_proximity_count == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `LineString` | `shapely.geometry.LineString` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `pytest.approx` | `pytest.approx` |

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
def test_distance_profile_is_threshold_free_and_tracks_ties() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )
    result = enrich_parcel_grid_proximity(parcels, lines, _posts())

    profile = profile_grid_proximity(result)

    assert profile.parcel_count == 2
    assert profile.nearest_line.count == 2
    assert profile.nearest_line.missing_count == 0
    assert profile.nearest_line.minimum == pytest.approx(50.0)
    assert profile.nearest_line.p50 == pytest.approx(75.0)
    assert profile.nearest_line.maximum == pytest.approx(100.0)
    assert profile.nearest_line.tie_count == 1
    assert profile.voltage_levels[0].voltage_kv == 110.0
    assert profile.voltage_levels[0].line_feature_count == 2
    assert profile.voltage_levels[0].parcel_proximity_count == 2
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_missing_voltage_cartesian_row`

**Purpose:** Regression invariant: profile rejects missing voltage cartesian row. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_missing_voltage_cartesian_row() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `result.voltage_level_proximity.iloc[:-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `replace` | `dataclasses.replace` |

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
def test_profile_rejects_missing_voltage_cartesian_row() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[:-1].copy()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_unknown_voltage_parcel_with_same_total_count`

**Purpose:** Regression invariant: profile rejects unknown voltage parcel with same total count. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_unknown_voltage_parcel_with_same_total_count() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `_mutate_voltage_result` | `tests.unit.test_enrich_grid_proximity._mutate_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |

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
def test_profile_rejects_unknown_voltage_parcel_with_same_total_count() -> None:
    result = _two_parcel_two_voltage_result()
    corrupted = _mutate_voltage_result(result, "parcel_id", "UNKNOWN-PARCEL")

    with pytest.raises(GridProximityError):
        profile_grid_proximity(corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_duplicate_parcel_voltage_pair`

**Purpose:** Regression invariant: profile rejects duplicate parcel voltage pair. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_duplicate_parcel_voltage_pair() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `result.voltage_level_proximity.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `table.at[1, "parcel_id"] = table.at[0, "parcel_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_profile_rejects_duplicate_parcel_voltage_pair() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.copy()
    table.at[1, "parcel_id"] = table.at[0, "parcel_id"]

    with pytest.raises(GridProximityError, match="unique"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_voltage_rows_out_of_parcel_order`

**Purpose:** Regression invariant: profile rejects voltage rows out of parcel order. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_voltage_rows_out_of_parcel_order() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="exact parcel set")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `replace` | `dataclasses.replace` |

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
def test_profile_rejects_voltage_rows_out_of_parcel_order() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index(drop=True)

    with pytest.raises(GridProximityError, match="exact parcel set"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_inconsistent_global_exact_distance`

**Purpose:** Regression invariant: profile rejects inconsistent global exact distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_inconsistent_global_exact_distance() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="exact-line distance")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |

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
def test_profile_rejects_inconsistent_global_exact_distance() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="exact-line distance"):
        profile_grid_proximity(
            _mutate_parcel_result(
                result,
                "nearest_exact_line_proxy_distance_m",
                5000.0,
            )
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_inconsistent_global_exact_identity`

**Purpose:** Regression invariant: profile rejects inconsistent global exact identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_inconsistent_global_exact_identity(
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_exact_line_grid_feature_id", "OTHER-LINE"),
        ("nearest_exact_line_source_feature_id", "OTHER-SOURCE"),
        ("nearest_exact_line_voltage_kv", 275.0),
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
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="inconsistent")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |
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
def test_profile_rejects_inconsistent_global_exact_identity(
    column: str,
    value: object,
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_inconsistent_global_exact_metadata`

**Purpose:** Regression invariant: profile rejects inconsistent global exact metadata. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_inconsistent_global_exact_metadata(
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_exact_line_manager_name", "OTHER MANAGER"),
        ("nearest_exact_line_asset_status_raw", "OTHER STATUS"),
        ("nearest_exact_line_source_department_code", "32"),
        ("nearest_exact_line_source_edition", "2026-09-15"),
        ("nearest_exact_line_source_archive_sha256", "b" * 64),
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
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="inconsistent")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |
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
def test_profile_rejects_inconsistent_global_exact_metadata(
    column: str,
    value: object,
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_inconsistent_global_exact_tie_count`

**Purpose:** Regression invariant: profile rejects inconsistent global exact tie count. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_inconsistent_global_exact_tie_count() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="tie count")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |

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
def test_profile_rejects_inconsistent_global_exact_tie_count() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie count"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_tie_count", 2)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_bad_required_match_tie_count`

**Purpose:** Regression invariant: profile rejects bad required match tie count. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_bad_required_match_tie_count(
    column: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    [
        0,
        -1,
        1.5,
        float("inf"),
        "2",
        None,
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)`, `pytest.mark.parametrize(
    "column",
    [
        "nearest_line_tie_count",
        "nearest_exact_line_tie_count",
        "nearest_post_tie_count",
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
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="tie_count\|match")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.param` | `pytest.param` |

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
def test_profile_rejects_bad_required_match_tie_count(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_bad_long_table_tie_count`

**Purpose:** Regression invariant: profile rejects bad long table tie count. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_bad_long_table_tie_count(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    [
        0,
        -1,
        1.5,
        float("inf"),
        "2",
        None,
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="tie_count\|match")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_voltage_result` | `tests.unit.test_enrich_grid_proximity._mutate_voltage_result` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.param` | `pytest.param` |

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
def test_profile_rejects_bad_long_table_tie_count(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_voltage_result(result, "tie_count", value))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_missing_main_match_feature_id`

**Purpose:** Regression invariant: profile rejects missing main match feature id. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_missing_main_match_feature_id(column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    [
        "nearest_line_grid_feature_id",
        "nearest_line_source_feature_id",
        "nearest_exact_line_grid_feature_id",
        "nearest_exact_line_source_feature_id",
        "nearest_post_grid_feature_id",
        "nearest_post_source_feature_id",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="require")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |
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
def test_profile_rejects_missing_main_match_feature_id(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_parcel_result(result, column, None))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_bad_required_match_distance`

**Purpose:** Regression invariant: profile rejects bad required match distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_bad_required_match_distance(
    column: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_line_proxy_distance_m", None),
        ("nearest_line_proxy_distance_m", "100"),
        ("nearest_exact_line_proxy_distance_m", float("inf")),
        ("nearest_post_proxy_distance_m", -1),
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
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |
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
def test_profile_rejects_bad_required_match_distance(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_bad_exact_match_voltage`

**Purpose:** Regression invariant: profile rejects bad exact match voltage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_bad_exact_match_voltage(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    [None, 0, -1, float("inf"), "110", 999.0],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="voltage\|match")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |
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
def test_profile_rejects_bad_exact_match_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="voltage|match"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_voltage_kv", value)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_bad_result_parcel_id`

**Purpose:** Regression invariant: profile rejects bad result parcel id. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_bad_result_parcel_id() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="parcel_id")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |

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
def test_profile_rejects_bad_result_parcel_id() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="parcel_id"):
        profile_grid_proximity(_mutate_parcel_result(result, "parcel_id", " BAD "))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_missing_required_proximity_column`

**Purpose:** Regression invariant: profile rejects missing required proximity column. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_missing_required_proximity_column() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="Missing proximity")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `result.parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `replace` | `dataclasses.replace` |

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
| In-memory mutation | `result.parcels.drop(columns="nearest_line_grid_feature_id")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_profile_rejects_missing_required_proximity_column() -> None:
    result = _two_parcel_two_voltage_result()
    parcels = result.parcels.drop(columns="nearest_line_grid_feature_id")

    with pytest.raises(GridProximityError, match="Missing proximity"):
        profile_grid_proximity(replace(result, parcels=parcels))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_nondeterministic_or_duplicate_coverage`

**Purpose:** Regression invariant: profile rejects nondeterministic or duplicate coverage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_nondeterministic_or_duplicate_coverage(
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["reversed", "duplicate"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="coverage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_profile_rejects_nondeterministic_or_duplicate_coverage(
    mutation: str,
) -> None:
    result = _two_parcel_two_voltage_result()
    if mutation == "reversed":
        coverage = tuple(reversed(result.voltage_level_coverage))
    else:
        coverage = (*result.voltage_level_coverage, result.voltage_level_coverage[0])

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_invalid_voltage_coverage_level`

**Purpose:** Regression invariant: profile rejects invalid voltage coverage level. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_invalid_voltage_coverage_level(voltage_kv: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "voltage_kv",
    [
        0,
        -1,
        float("inf"),
        "110",
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `voltage_kv` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="coverage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `VoltageLevelCoverage` | `landscout.stages.VoltageLevelCoverage` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.param` | `pytest.param` |

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
def test_profile_rejects_invalid_voltage_coverage_level(voltage_kv: object) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (VoltageLevelCoverage(voltage_kv=voltage_kv, line_feature_count=1),)

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_invalid_voltage_coverage_feature_count`

**Purpose:** Regression invariant: profile rejects invalid voltage coverage feature count. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_invalid_voltage_coverage_feature_count(
    feature_count: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("feature_count", [0, -1, 1.5, float("inf"), True, "2"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `feature_count` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="line_feature_count")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `VoltageLevelCoverage` | `landscout.stages.VoltageLevelCoverage` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `replace` | `dataclasses.replace` |
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
def test_profile_rejects_invalid_voltage_coverage_feature_count(
    feature_count: object,
) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (
        VoltageLevelCoverage(voltage_kv=110.0, line_feature_count=feature_count),
    )

    with pytest.raises(GridProximityError, match="line_feature_count"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_invalid_long_table_voltage`

**Purpose:** Regression invariant: profile rejects invalid long table voltage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_invalid_long_table_voltage(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    [None, 0, -1, float("inf"), "110", 220.0],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="Voltage proximity")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_voltage_result` | `tests.unit.test_enrich_grid_proximity._mutate_voltage_result` |
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
def test_profile_rejects_invalid_long_table_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="Voltage proximity"):
        profile_grid_proximity(_mutate_voltage_result(result, "voltage_kv", value))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_missing_long_table_match_lineage`

**Purpose:** Regression invariant: profile rejects missing long table match lineage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_missing_long_table_match_lineage(column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    [
        "nearest_line_grid_feature_id",
        "nearest_line_source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="require")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_voltage_result` | `tests.unit.test_enrich_grid_proximity._mutate_voltage_result` |
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
def test_profile_rejects_missing_long_table_match_lineage(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_voltage_result(result, column, None))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_bad_long_table_distance`

**Purpose:** Regression invariant: profile rejects bad long table distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_bad_long_table_distance(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "value",
    [
        None,
        -1,
        float("inf"),
        "100",
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_two_parcel_two_voltage_result` | `tests.unit.test_enrich_grid_proximity._two_parcel_two_voltage_result` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_voltage_result` | `tests.unit.test_enrich_grid_proximity._mutate_voltage_result` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.param` | `pytest.param` |

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
def test_profile_rejects_bad_long_table_distance(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(
            _mutate_voltage_result(result, "nearest_line_proxy_distance_m", value)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_allows_consistent_missing_manager_and_asset_status`

**Purpose:** Regression invariant: profile allows consistent missing manager and asset status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_allows_consistent_missing_manager_and_asset_status() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.parcel_count == 1`
  - `assert result.parcels["nearest_exact_line_manager_name"].isna().all()`
  - `assert result.parcels["nearest_exact_line_asset_status_raw"].isna().all()`
  - `assert result.voltage_level_proximity["manager_name"].isna().all()`
  - `assert result.voltage_level_proximity["asset_status_raw"].isna().all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `result.parcels["nearest_exact_line_manager_name"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_manager_name"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_asset_status_raw"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["nearest_exact_line_asset_status_raw"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity["manager_name"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity["manager_name"].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity["asset_status_raw"].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.voltage_level_proximity["asset_status_raw"].isna` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `lines["manager_name"] = None`<br>`lines["asset_status_raw"] = None` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_profile_allows_consistent_missing_manager_and_asset_status() -> None:
    lines = _lines()
    lines["manager_name"] = None
    lines["asset_status_raw"] = None
    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    profile = profile_grid_proximity(result)

    assert profile.parcel_count == 1
    assert result.parcels["nearest_exact_line_manager_name"].isna().all()
    assert result.parcels["nearest_exact_line_asset_status_raw"].isna().all()
    assert result.voltage_level_proximity["manager_name"].isna().all()
    assert result.voltage_level_proximity["asset_status_raw"].isna().all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_rejects_nonnull_exact_field_without_exact_coverage`

**Purpose:** Regression invariant: profile rejects nonnull exact field without exact coverage. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_rejects_nonnull_exact_field_without_exact_coverage(
    column: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_exact_line_proxy_distance_m", 1.0),
        ("nearest_exact_line_grid_feature_id", "LINE"),
        ("nearest_exact_line_source_feature_id", "SOURCE"),
        ("nearest_exact_line_tie_count", 1),
        ("nearest_exact_line_voltage_kv", 110.0),
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
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="unmatched\|entirely")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.raises` | `pytest.raises` |
| `profile_grid_proximity` | `landscout.stages.profile_grid_proximity` |
| `_mutate_parcel_result` | `tests.unit.test_enrich_grid_proximity._mutate_parcel_result` |
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
def test_profile_rejects_nonnull_exact_field_without_exact_coverage(
    column: str, value: object
) -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(),
        _lines(voltage_statuses=["UNKNOWN"], voltages=[None]),
        _posts(),
    )

    with pytest.raises(GridProximityError, match="unmatched|entirely"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_valid_required_grid_feature_is_rejected`

**Purpose:** Regression invariant: no valid required grid feature is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_valid_required_grid_feature_is_rejected(kind: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("kind", ["line", "post"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(GridProximityError, match="No VALID")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lines` | `tests.unit.test_enrich_grid_proximity._lines` |
| `_posts` | `tests.unit.test_enrich_grid_proximity._posts` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity._enrich_parcel_grid_proximity_from_normalized` |
| `_parcels` | `tests.unit.test_enrich_grid_proximity._parcels` |
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
def test_no_valid_required_grid_feature_is_rejected(kind: str) -> None:
    lines = _lines([None]) if kind == "line" else _lines()
    posts = _posts([None]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="No VALID"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **63**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_clean_high_level_api_is_exported` | none | none | 4 | Proves clean high level api is exported using the exact source reproduced in section 7. |
| `test_public_proximity_normalizes_verified_source_exactly_once` | none | none | 2 | Proves public proximity normalizes verified source exactly once using the exact source reproduced in section 7. |
| `test_public_proximity_rejects_wrong_source_boundary_types` | pytest.mark.parametrize("argument", ["parcels", "electricity_source", "source_config"]) | pytest.raises(GridProximityError) | 0 | Proves public proximity rejects wrong source boundary types using the exact source reproduced in section 7. |
| `test_caller_crafted_normalized_grid_frame_is_not_a_public_source` | none | pytest.raises(<br>            GridProximityError,<br>            match="IgnBdTopoElectricityData\|electricity source",<br>        ) | 4 | Proves caller crafted normalized grid frame is not a public source using the exact source reproduced in section 7. |
| `test_public_proximity_reproduces_configured_electricity_roles` | none | pytest.raises(GridProximityError) | 2 | Proves public proximity reproduces configured electricity roles using the exact source reproduced in section 7. |
| `test_public_proximity_rejects_archive_lineage_differing_from_config` | pytest.mark.parametrize(<br>    "archive_changes",<br>    [<br>        pytest.param({"provider": "IGN"}, id="provider"),<br>        pytest.param({"product": "BDTOPO"}, id="product"),<br>        pytest.param({"edition": "2026-06-16"}, id="edition"),<br>        pytest.param({"product_version": "3.6"}, id="product-version"),<br>        pytest.param(<br>            {"projection": "urn:ogc:def:crs:EPSG::2154"},<br>            id="projection",<br>        ),<br>        pytest.param({"package_format": "SHP"}, id="package-format"),<br>        pytest.param({"archive_format": "zip"}, id="archive-format"),<br>        pytest.param(<br>            {"source_url": "https://example.test/other-package.7z"},<br>            id="source-url",<br>        ),<br>        pytest.param(<br>            {"checksum_url": "https://example.test/other-package.md5"},<br>            id="checksum-url",<br>        ),<br>        pytest.param(<br>            {<br>                "official_checksum_algorithm": "sha256",<br>                "official_checksum": "b" * 64,<br>                "official_checksum_validated": True,<br>            },<br>            id="official-checksum",<br>        ),<br>        pytest.param(<br>            {"file_size": (SOURCE_CONFIG.expected_archive_size_bytes or 1) + 1},<br>            id="archive-size",<br>        ),<br>    ],<br>) | pytest.raises(GridProximityError) | 0 | Proves public proximity rejects archive lineage differing from config using the exact source reproduced in section 7. |
| `test_source_normalization_failure_stops_grid_computation` | none | pytest.raises(GridProximityError) | 0 | Proves source normalization failure stops grid computation using the exact source reproduced in section 7. |
| `test_separated_distance_uses_parcel_edge_not_centroid` | none | none | 2 | Proves separated distance uses parcel edge not centroid using the exact source reproduced in section 7. |
| `test_touching_line_has_zero_distance` | none | none | 1 | Proves touching line has zero distance using the exact source reproduced in section 7. |
| `test_post_distance_uses_parcel_and_post_polygons` | none | none | 1 | Proves post distance uses parcel and post polygons using the exact source reproduced in section 7. |
| `test_epsg4326_input_is_calculated_in_lambert93_and_preserved` | none | none | 3 | Proves epsg4326 input is calculated in lambert93 and preserved using the exact source reproduced in section 7. |
| `test_epsg2154_parcel_input_remains_epsg2154` | none | none | 2 | Proves epsg2154 parcel input remains epsg2154 using the exact source reproduced in section 7. |
| `test_valid_parcel_id_is_preserved_exactly` | none | none | 1 | Proves valid parcel id is preserved exactly using the exact source reproduced in section 7. |
| `test_public_proximity_rejects_generated_parcel_column_before_normalization` | none | pytest.raises(GridProximityError, match="collides.*generated") | 0 | Proves public proximity rejects generated parcel column before normalization using the exact source reproduced in section 7. |
| `test_invalid_parcel_id_hygiene_is_rejected` | pytest.mark.parametrize(<br>    "identifier",<br>    [None, "", "   ", " PARCEL-1", "PARCEL-1 ", 123],<br>) | pytest.raises(GridProximityError, match="parcel_id") | 0 | Proves invalid parcel id hygiene is rejected using the exact source reproduced in section 7. |
| `test_supported_parcel_polygon_geometry_is_preserved` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),<br>        MultiPolygon([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]),<br>        Polygon([(0, 0, 5), (0, 10, 5), (10, 10, 5), (10, 0, 5), (0, 0, 5)]),<br>    ],<br>) | none | 2 | Proves supported parcel polygon geometry is preserved using the exact source reproduced in section 7. |
| `test_semantically_wrong_parcel_geometry_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Point(1, 1),<br>        LineString([(0, 0), (10, 10)]),<br>        MultiLineString([[(0, 0), (10, 10)]]),<br>        GeometryCollection([Point(1, 1)]),<br>    ],<br>) | pytest.raises(GridProximityError, match="Polygon\|MultiPolygon") | 0 | Proves semantically wrong parcel geometry is rejected using the exact source reproduced in section 7. |
| `test_missing_crs_is_rejected` | pytest.mark.parametrize("kind", ["parcel", "line", "post"]) | pytest.raises(GridProximityError, match="CRS") | 0 | Proves missing crs is rejected using the exact source reproduced in section 7. |
| `test_wrong_grid_crs_is_rejected` | pytest.mark.parametrize("kind", ["line", "post"]) | pytest.raises(GridProximityError, match="2154") | 0 | Proves wrong grid crs is rejected using the exact source reproduced in section 7. |
| `test_z_line_has_same_horizontal_distance_as_xy_line` | none | none | 2 | Proves z line has same horizontal distance as xy line using the exact source reproduced in section 7. |
| `test_line_tie_is_counted_and_lexical_feature_id_wins` | none | none | 8 | Proves line tie is counted and lexical feature id wins using the exact source reproduced in section 7. |
| `test_cross_voltage_tie_uses_lexical_global_feature_id` | none | none | 7 | Proves cross voltage tie uses lexical global feature id using the exact source reproduced in section 7. |
| `test_nonvalid_grid_geometries_are_excluded_without_row_loss` | none | none | 2 | Proves nonvalid grid geometries are excluded without row loss using the exact source reproduced in section 7. |
| `test_wrong_grid_feature_type_is_rejected` | pytest.mark.parametrize("kind", ["line", "post"]) | pytest.raises(GridProximityError, match="grid_feature_type") | 0 | Proves wrong grid feature type is rejected using the exact source reproduced in section 7. |
| `test_duplicate_grid_feature_id_is_rejected` | pytest.mark.parametrize("kind", ["line", "post"]) | pytest.raises(GridProximityError, match="unique") | 0 | Proves duplicate grid feature id is rejected using the exact source reproduced in section 7. |
| `test_wrong_spatial_role_is_rejected` | pytest.mark.parametrize("kind", ["line", "post"]) | pytest.raises(GridProximityError, match="PROXY_GEOMETRY") | 0 | Proves wrong spatial role is rejected using the exact source reproduced in section 7. |
| `test_unsupported_valid_grid_geometry_type_is_rejected` | pytest.mark.parametrize(<br>    ("kind", "geometry"),<br>    [<br>        ("line", Point(100, 0)),<br>        ("line", Polygon([(100, 0), (100, 5), (105, 5), (105, 0), (100, 0)])),<br>        ("post", Point(100, 0)),<br>        ("post", LineString([(100, 0), (100, 10)])),<br>    ],<br>) | pytest.raises(GridProximityError, match="geometry types") | 0 | Proves unsupported valid grid geometry type is rejected using the exact source reproduced in section 7. |
| `test_supported_multi_geometries_are_accepted` | none | none | 1 | Proves supported multi geometries are accepted using the exact source reproduced in section 7. |
| `test_nearest_any_line_preserves_every_voltage_status` | pytest.mark.parametrize(<br>    "status", ["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]<br>) | none | 1 | Proves nearest any line preserves every voltage status using the exact source reproduced in section 7. |
| `test_nearest_exact_and_voltage_table_exclude_nonexact_lines` | none | none | 6 | Proves nearest exact and voltage table exclude nonexact lines using the exact source reproduced in section 7. |
| `test_voltage_table_is_exact_ordered_cartesian_product` | none | none | 4 | Proves voltage table is exact ordered cartesian product using the exact source reproduced in section 7. |
| `test_invalid_exact_voltage_values_are_not_used_as_exact` | none | none | 2 | Proves invalid exact voltage values are not used as exact using the exact source reproduced in section 7. |
| `test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` | none | none | 15 | Proves no exact voltage preserves parcels and returns empty long table using the exact source reproduced in section 7. |
| `test_missing_parcel_column_is_rejected` | pytest.mark.parametrize("column", ["parcel_id", "geometry"]) | pytest.raises(GridProximityError, match=column) | 0 | Proves missing parcel column is rejected using the exact source reproduced in section 7. |
| `test_null_parcel_id_is_rejected` | none | pytest.raises(GridProximityError, match="parcel_id") | 0 | Proves null parcel id is rejected using the exact source reproduced in section 7. |
| `test_duplicate_parcel_id_is_rejected` | none | pytest.raises(GridProximityError, match="unique") | 0 | Proves duplicate parcel id is rejected using the exact source reproduced in section 7. |
| `test_bad_parcel_geometry_is_rejected` | pytest.mark.parametrize(<br>    ("geometry", "message"),<br>    [<br>        (None, "null"),<br>        (Polygon(), "empty"),<br>        (<br>            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),<br>            "valid",<br>        ),<br>    ],<br>) | pytest.raises(GridProximityError, match=message) | 0 | Proves bad parcel geometry is rejected using the exact source reproduced in section 7. |
| `test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` | none | none | 2 | Proves inputs are not mutated and parcel order and ids are preserved using the exact source reproduced in section 7. |
| `test_distance_profile_is_threshold_free_and_tracks_ties` | none | none | 10 | Proves distance profile is threshold free and tracks ties using the exact source reproduced in section 7. |
| `test_profile_rejects_missing_voltage_cartesian_row` | none | pytest.raises(GridProximityError) | 0 | Proves profile rejects missing voltage cartesian row using the exact source reproduced in section 7. |
| `test_profile_rejects_unknown_voltage_parcel_with_same_total_count` | none | pytest.raises(GridProximityError) | 0 | Proves profile rejects unknown voltage parcel with same total count using the exact source reproduced in section 7. |
| `test_profile_rejects_duplicate_parcel_voltage_pair` | none | pytest.raises(GridProximityError, match="unique") | 0 | Proves profile rejects duplicate parcel voltage pair using the exact source reproduced in section 7. |
| `test_profile_rejects_voltage_rows_out_of_parcel_order` | none | pytest.raises(GridProximityError, match="exact parcel set") | 0 | Proves profile rejects voltage rows out of parcel order using the exact source reproduced in section 7. |
| `test_profile_rejects_inconsistent_global_exact_distance` | none | pytest.raises(GridProximityError, match="exact-line distance") | 0 | Proves profile rejects inconsistent global exact distance using the exact source reproduced in section 7. |
| `test_profile_rejects_inconsistent_global_exact_identity` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("nearest_exact_line_grid_feature_id", "OTHER-LINE"),<br>        ("nearest_exact_line_source_feature_id", "OTHER-SOURCE"),<br>        ("nearest_exact_line_voltage_kv", 275.0),<br>    ],<br>) | pytest.raises(GridProximityError, match="inconsistent") | 0 | Proves profile rejects inconsistent global exact identity using the exact source reproduced in section 7. |
| `test_profile_rejects_inconsistent_global_exact_metadata` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("nearest_exact_line_manager_name", "OTHER MANAGER"),<br>        ("nearest_exact_line_asset_status_raw", "OTHER STATUS"),<br>        ("nearest_exact_line_source_department_code", "32"),<br>        ("nearest_exact_line_source_edition", "2026-09-15"),<br>        ("nearest_exact_line_source_archive_sha256", "b" * 64),<br>    ],<br>) | pytest.raises(GridProximityError, match="inconsistent") | 0 | Proves profile rejects inconsistent global exact metadata using the exact source reproduced in section 7. |
| `test_profile_rejects_inconsistent_global_exact_tie_count` | none | pytest.raises(GridProximityError, match="tie count") | 0 | Proves profile rejects inconsistent global exact tie count using the exact source reproduced in section 7. |
| `test_profile_rejects_bad_required_match_tie_count` | pytest.mark.parametrize(<br>    "value",<br>    [<br>        0,<br>        -1,<br>        1.5,<br>        float("inf"),<br>        "2",<br>        None,<br>        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),<br>    ],<br>); pytest.mark.parametrize(<br>    "column",<br>    [<br>        "nearest_line_tie_count",<br>        "nearest_exact_line_tie_count",<br>        "nearest_post_tie_count",<br>    ],<br>) | pytest.raises(GridProximityError, match="tie_count\|match") | 0 | Proves profile rejects bad required match tie count using the exact source reproduced in section 7. |
| `test_profile_rejects_bad_long_table_tie_count` | pytest.mark.parametrize(<br>    "value",<br>    [<br>        0,<br>        -1,<br>        1.5,<br>        float("inf"),<br>        "2",<br>        None,<br>        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),<br>    ],<br>) | pytest.raises(GridProximityError, match="tie_count\|match") | 0 | Proves profile rejects bad long table tie count using the exact source reproduced in section 7. |
| `test_profile_rejects_missing_main_match_feature_id` | pytest.mark.parametrize(<br>    "column",<br>    [<br>        "nearest_line_grid_feature_id",<br>        "nearest_line_source_feature_id",<br>        "nearest_exact_line_grid_feature_id",<br>        "nearest_exact_line_source_feature_id",<br>        "nearest_post_grid_feature_id",<br>        "nearest_post_source_feature_id",<br>    ],<br>) | pytest.raises(GridProximityError, match="require") | 0 | Proves profile rejects missing main match feature id using the exact source reproduced in section 7. |
| `test_profile_rejects_bad_required_match_distance` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("nearest_line_proxy_distance_m", None),<br>        ("nearest_line_proxy_distance_m", "100"),<br>        ("nearest_exact_line_proxy_distance_m", float("inf")),<br>        ("nearest_post_proxy_distance_m", -1),<br>    ],<br>) | pytest.raises(GridProximityError) | 0 | Proves profile rejects bad required match distance using the exact source reproduced in section 7. |
| `test_profile_rejects_bad_exact_match_voltage` | pytest.mark.parametrize(<br>    "value",<br>    [None, 0, -1, float("inf"), "110", 999.0],<br>) | pytest.raises(GridProximityError, match="voltage\|match") | 0 | Proves profile rejects bad exact match voltage using the exact source reproduced in section 7. |
| `test_profile_rejects_bad_result_parcel_id` | none | pytest.raises(GridProximityError, match="parcel_id") | 0 | Proves profile rejects bad result parcel id using the exact source reproduced in section 7. |
| `test_profile_rejects_missing_required_proximity_column` | none | pytest.raises(GridProximityError, match="Missing proximity") | 0 | Proves profile rejects missing required proximity column using the exact source reproduced in section 7. |
| `test_profile_rejects_nondeterministic_or_duplicate_coverage` | pytest.mark.parametrize("mutation", ["reversed", "duplicate"]) | pytest.raises(GridProximityError, match="coverage") | 0 | Proves profile rejects nondeterministic or duplicate coverage using the exact source reproduced in section 7. |
| `test_profile_rejects_invalid_voltage_coverage_level` | pytest.mark.parametrize(<br>    "voltage_kv",<br>    [<br>        0,<br>        -1,<br>        float("inf"),<br>        "110",<br>        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),<br>    ],<br>) | pytest.raises(GridProximityError, match="coverage") | 0 | Proves profile rejects invalid voltage coverage level using the exact source reproduced in section 7. |
| `test_profile_rejects_invalid_voltage_coverage_feature_count` | pytest.mark.parametrize("feature_count", [0, -1, 1.5, float("inf"), True, "2"]) | pytest.raises(GridProximityError, match="line_feature_count") | 0 | Proves profile rejects invalid voltage coverage feature count using the exact source reproduced in section 7. |
| `test_profile_rejects_invalid_long_table_voltage` | pytest.mark.parametrize(<br>    "value",<br>    [None, 0, -1, float("inf"), "110", 220.0],<br>) | pytest.raises(GridProximityError, match="Voltage proximity") | 0 | Proves profile rejects invalid long table voltage using the exact source reproduced in section 7. |
| `test_profile_rejects_missing_long_table_match_lineage` | pytest.mark.parametrize(<br>    "column",<br>    [<br>        "nearest_line_grid_feature_id",<br>        "nearest_line_source_feature_id",<br>        "source_department_code",<br>        "source_edition",<br>        "source_archive_sha256",<br>    ],<br>) | pytest.raises(GridProximityError, match="require") | 0 | Proves profile rejects missing long table match lineage using the exact source reproduced in section 7. |
| `test_profile_rejects_bad_long_table_distance` | pytest.mark.parametrize(<br>    "value",<br>    [<br>        None,<br>        -1,<br>        float("inf"),<br>        "100",<br>        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),<br>    ],<br>) | pytest.raises(GridProximityError) | 0 | Proves profile rejects bad long table distance using the exact source reproduced in section 7. |
| `test_profile_allows_consistent_missing_manager_and_asset_status` | none | none | 5 | Proves profile allows consistent missing manager and asset status using the exact source reproduced in section 7. |
| `test_profile_rejects_nonnull_exact_field_without_exact_coverage` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("nearest_exact_line_proxy_distance_m", 1.0),<br>        ("nearest_exact_line_grid_feature_id", "LINE"),<br>        ("nearest_exact_line_source_feature_id", "SOURCE"),<br>        ("nearest_exact_line_tie_count", 1),<br>        ("nearest_exact_line_voltage_kv", 110.0),<br>    ],<br>) | pytest.raises(GridProximityError, match="unmatched\|entirely") | 0 | Proves profile rejects nonnull exact field without exact coverage using the exact source reproduced in section 7. |
| `test_no_valid_required_grid_feature_is_rejected` | pytest.mark.parametrize("kind", ["line", "post"]) | pytest.raises(GridProximityError, match="No VALID") | 0 | Proves no valid required grid feature is rejected using the exact source reproduced in section 7. |

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

import json
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

import geopandas as gpd
import numpy as np
import pandas as pd
import pyogrio
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.api.types import is_float_dtype, is_integer_dtype
from shapely.geometry import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout import stages
from landscout.sources import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    load_ign_bdtopo_source_config,
)
from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)
from landscout.stages import (
    enrich_parcel_grid_proximity as public_enrich_parcel_grid_proximity,
)
from landscout.stages.enrich_grid_proximity import (
    VOLTAGE_PROXIMITY_COLUMNS,
)
from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)
from landscout.stages.normalize_grid_ign import NormalizedIgnElectricityData

OVERFLOWING_INTEGER = 10**10000
SOURCE_CONFIG = load_ign_bdtopo_source_config()


def _geometry_status(geometry: object) -> str:
    if geometry is None:
        return "NULL"
    if geometry.is_empty:
        return "EMPTY"
    if not geometry.is_valid:
        return "INVALID"
    return "VALID"


def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    source_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs=crs,
        index=source_index,
    )


def _lines(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    voltage_statuses: list[str] | None = None,
    voltages: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [LineString([(110, -20), (110, 30)])]
    count = len(values)
    ids = identifiers or [f"LINE-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    normalized_voltage_statuses = voltage_statuses or ["EXACT"] * count
    normalized_voltages = voltages or [110.0] * count
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["ELECTRIC_LINE"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_LINE_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "voltage_raw": [
                f"{value:g} kV" if isinstance(value, (int, float)) else None
                for value in normalized_voltages
            ],
            "voltage_status": normalized_voltage_statuses,
            "voltage_kv": normalized_voltages,
            "voltage_upper_bound_kv": [np.nan] * count,
            "manager_name": ["TEST MANAGER"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )


def _posts(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
    statuses: list[str] | None = None,
    crs: str | None = "EPSG:2154",
    feature_types: list[str] | None = None,
    spatial_roles: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(110, 0), (110, 10), (120, 10), (120, 0), (110, 0)])
    ]
    count = len(values)
    ids = identifiers or [f"POST-{position + 1}" for position in range(count)]
    geometry_statuses = statuses or [_geometry_status(value) for value in values]
    return gpd.GeoDataFrame(
        {
            "grid_feature_id": ids,
            "grid_feature_type": feature_types or ["TRANSFORMATION_POST"] * count,
            "source_feature_id": [f"SOURCE-{value}" for value in ids],
            "source_department_code": ["31"] * count,
            "source_edition": ["2026-06-15"] * count,
            "source_archive_sha256": ["a" * 64] * count,
            "source_layer": ["CUSTOM_POST_LAYER"] * count,
            "spatial_role": spatial_roles or ["PROXY_GEOMETRY"] * count,
            "geometry_status": geometry_statuses,
            "name": ["Test post"] * count,
            "importance_raw": ["5"] * count,
            "asset_status_raw": ["En service"] * count,
        },
        geometry=values,
        crs=crs,
    )


def _electricity_source(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
    return IgnBdTopoElectricityData(
        extraction=cast(Any, None),
        electric_lines=lines if lines is not None else _lines(),
        transformation_posts=posts if posts is not None else _posts(),
        electric_lines_summary=cast(Any, None),
        transformation_posts_summary=cast(Any, None),
    )


def _physical_line_source(
    identifier: str,
    geometry: LineString,
) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "cleabs": [identifier],
            "voltage": ["225 kV"],
            "gestionnaire": ["Test manager"],
            "siren_gestionnaire": ["444619258"],
            "etat_de_l_objet": ["En service"],
            "sources": ["Synthetic physical source"],
            "identifiants_sources": [f"SOURCE-{identifier}"],
            "date_creation": pd.to_datetime(["2024-01-01"]),
            "date_modification": pd.to_datetime(["2025-01-01"]),
            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),
            "methode_d_acquisition_planimetrique": ["Synthetic"],
            "precision_planimetrique": [1.0],
        },
        geometry=[geometry],
        crs="EPSG:2154",
    )


def _physical_post_source(
    identifier: str,
    geometry: Polygon,
) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "cleabs": [identifier],
            "toponyme": ["Test post"],
            "statut_du_toponyme": ["Valid"],
            "importance": ["5"],
            "etat_de_l_objet": ["En service"],
            "sources": ["Synthetic physical source"],
            "identifiants_sources": [f"SOURCE-{identifier}"],
            "date_creation": pd.to_datetime(["2024-01-01"]),
            "date_modification": pd.to_datetime(["2025-01-01"]),
            "date_de_confirmation": pd.to_datetime(["2025-02-01"]),
            "methode_d_acquisition_planimetrique": ["Synthetic"],
            "precision_planimetrique": [1.0],
        },
        geometry=[geometry],
        crs="EPSG:2154",
    )


def _physical_summary(
    frame: gpd.GeoDataFrame,
    *,
    logical_name: str,
    layer_name: str,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    return IgnBdTopoLayerSummary(
        logical_name=cast(Any, logical_name),
        source_layer_name=layer_name,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=tuple(
            sorted(
                str(value) for value in geometry[~null_mask].geom_type.dropna().unique()
            )
        ),
    )


def _physical_electricity_source(
    tmp_path: Path,
    *,
    alternate_roles: bool,
) -> IgnBdTopoElectricityData:
    configured_line_layer = "LIGNE_ELECTRIQUE_CONFIGURED"
    configured_post_layer = "POSTE_DE_TRANSFORMATION_CONFIGURED"
    alternate_line_layer = "CABLE_SOURCE_ALTERNATE"
    alternate_post_layer = "INSTALLATION_SOURCE_ALTERNATE"
    frames = (
        (
            configured_line_layer,
            _physical_line_source(
                "CONFIGURED-LINE",
                LineString([(500, -20), (500, 30)]),
            ),
        ),
        (
            "TRONCON_DE_ROUTE",
            gpd.GeoDataFrame(
                {"id": ["ROAD"]},
                geometry=[LineString([(0, 0), (1, 1)])],
                crs="EPSG:2154",
            ),
        ),
        (
            "DEPARTEMENT",
            gpd.GeoDataFrame(
                {"code_insee": ["31"]},
                geometry=[Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])],
                crs="EPSG:2154",
            ),
        ),
        (
            configured_post_layer,
            _physical_post_source(
                "CONFIGURED-POST",
                Polygon([(500, 0), (500, 10), (510, 10), (510, 0), (500, 0)]),
            ),
        ),
        (
            alternate_line_layer,
            _physical_line_source(
                "ALTERNATE-LINE",
                LineString([(10, -20), (10, 30)]),
            ),
        ),
        (
            alternate_post_layer,
            _physical_post_source(
                "ALTERNATE-POST",
                Polygon([(10, 0), (10, 10), (20, 10), (20, 0), (10, 0)]),
            ),
        ),
    )
    selected_line_layer = (
        alternate_line_layer if alternate_roles else configured_line_layer
    )
    selected_post_layer = (
        alternate_post_layer if alternate_roles else configured_post_layer
    )
    extraction_path = tmp_path / (
        "alternate-electricity-extraction"
        if alternate_roles
        else "configured-electricity-extraction"
    )
    extraction_path.mkdir()
    geopackage_path = extraction_path / "electricity.gpkg"
    for position, (layer_name, frame) in enumerate(frames):
        pyogrio.write_dataframe(
            frame,
            geopackage_path,
            layer=layer_name,
            driver="GPKG",
            append=position > 0,
        )
    selected_lines = gpd.read_file(
        geopackage_path,
        layer=selected_line_layer,
        engine="pyogrio",
    )
    selected_posts = gpd.read_file(
        geopackage_path,
        layer=selected_post_layer,
        engine="pyogrio",
    )
    payload = geopackage_path.read_bytes()
    digest = sha256(payload).hexdigest()
    layer_names = tuple(
        str(record[0]) for record in pyogrio.list_layers(geopackage_path)
    )
    marker = {
        "schema_version": 3,
        "archive_sha256": "a" * 64,
        "geopackage_relative_path": geopackage_path.name,
        "geopackage_size_bytes": len(payload),
        "geopackage_sha256": digest,
        "all_layer_names": list(layer_names),
        "electric_lines_layer": selected_line_layer,
        "transformation_posts_layer": selected_post_layer,
        "road_segments_layer": "TRONCON_DE_ROUTE",
        "department_layer": "DEPARTEMENT",
        "extracted_entries": [
            {
                "relative_path": geopackage_path.name,
                "kind": "file",
                "size_bytes": len(payload),
                "sha256": digest,
            }
        ],
        "spatial_role": "PROXY_GEOMETRY",
    }
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(marker),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product=SOURCE_CONFIG.product,
        department_code=SOURCE_CONFIG.department_code,
        edition=SOURCE_CONFIG.edition,
        product_version=SOURCE_CONFIG.product_version,
        projection=SOURCE_CONFIG.projection,
        package_format=SOURCE_CONFIG.format,
        archive_format=SOURCE_CONFIG.archive_format,
        source_url=str(SOURCE_CONFIG.source_url),
        checksum_url=(
            str(SOURCE_CONFIG.checksum_url)
            if SOURCE_CONFIG.checksum_url is not None
            else None
        ),
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename=Path(str(SOURCE_CONFIG.source_url)).name,
        file_size=SOURCE_CONFIG.expected_archive_size_bytes or 1,
        sha256="a" * 64,
        official_checksum_algorithm=SOURCE_CONFIG.official_checksum_algorithm,
        official_checksum=SOURCE_CONFIG.official_checksum,
        official_checksum_validated=(SOURCE_CONFIG.official_checksum is not None),
        path=tmp_path / Path(str(SOURCE_CONFIG.source_url)).name,
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename=geopackage_path.name,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer=selected_line_layer,
        transformation_posts_layer=selected_post_layer,
        road_segments_layer="TRONCON_DE_ROUTE",
        department_layer="DEPARTEMENT",
        cache_hit=True,
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=selected_lines,
        transformation_posts=selected_posts,
        electric_lines_summary=_physical_summary(
            selected_lines,
            logical_name="electric_lines",
            layer_name=selected_line_layer,
        ),
        transformation_posts_summary=_physical_summary(
            selected_posts,
            logical_name="transformation_posts",
            layer_name=selected_post_layer,
        ),
    )


def _alternate_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
    return _physical_electricity_source(tmp_path, alternate_roles=True)


def _configured_role_electricity_source(
    tmp_path: Path,
) -> IgnBdTopoElectricityData:
    return _physical_electricity_source(tmp_path, alternate_roles=False)


def _two_parcel_two_voltage_result() -> GridProximityResult:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(40, 0), (40, 10), (50, 10), (50, 0), (40, 0)]),
        ],
        identifiers=["PARCEL-2", "PARCEL-1"],
    )
    lines = _lines(
        [
            LineString([(200, -20), (200, 30)]),
            LineString([(100, -20), (100, 30)]),
        ],
        identifiers=["LINE-275", "LINE-110"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[275.0, 110.0],
    )
    return enrich_parcel_grid_proximity(parcels, lines, _posts())


def _mutate_parcel_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    parcels = result.parcels.copy()
    parcels[column] = parcels[column].astype("object")
    parcels.at[0, column] = value
    return replace(result, parcels=parcels)


def _mutate_voltage_result(
    result: GridProximityResult,
    column: str,
    value: object,
) -> GridProximityResult:
    table = result.voltage_level_proximity.copy()
    table[column] = table[column].astype("object")
    table.at[0, column] = value
    return replace(result, voltage_level_proximity=table)


def test_clean_high_level_api_is_exported() -> None:
    assert stages.enrich_parcel_grid_proximity is public_enrich_parcel_grid_proximity
    assert stages.profile_grid_proximity is profile_grid_proximity
    assert "enrich_parcel_grid_proximity" in stages.__all__
    assert "profile_grid_proximity" in stages.__all__


def test_public_proximity_normalizes_verified_source_exactly_once() -> None:
    parcels = _parcels()
    lines = _lines()
    posts = _posts()
    source = _electricity_source(lines, posts)
    normalized = NormalizedIgnElectricityData(lines, posts)

    with patch(
        "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
        return_value=normalized,
        create=True,
    ) as normalizer:
        result = public_enrich_parcel_grid_proximity(parcels, source, SOURCE_CONFIG)

    normalizer.assert_called_once_with(source, SOURCE_CONFIG)
    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
    assert result.parcels.loc[0, "nearest_post_grid_feature_id"] == "POST-1"


@pytest.mark.parametrize("argument", ["parcels", "electricity_source", "source_config"])
def test_public_proximity_rejects_wrong_source_boundary_types(
    argument: str,
) -> None:
    kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "electricity_source": _electricity_source(),
        "source_config": SOURCE_CONFIG,
    }
    kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
            create=True,
        ) as normalizer,
        pytest.raises(GridProximityError),
    ):
        public_enrich_parcel_grid_proximity(**cast(Any, kwargs))

    normalizer.assert_not_called()


def test_caller_crafted_normalized_grid_frame_is_not_a_public_source() -> None:
    forged_lines = _lines(
        [LineString([(10, -20), (10, 30)])],
        identifiers=["IGN_BDTOPO:ELECTRIC_LINE:FORGED"],
    )
    assert forged_lines["source_department_code"].eq("31").all()
    assert forged_lines["source_edition"].eq("2026-06-15").all()
    assert forged_lines["source_archive_sha256"].eq("a" * 64).all()
    assert forged_lines["spatial_role"].eq("PROXY_GEOMETRY").all()

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
            create=True,
        ) as normalizer,
        pytest.raises(
            GridProximityError,
            match="IgnBdTopoElectricityData|electricity source",
        ),
    ):
        public_enrich_parcel_grid_proximity(
            _parcels(),
            cast(Any, forged_lines),
            SOURCE_CONFIG,
        )

    normalizer.assert_not_called()


def test_public_proximity_reproduces_configured_electricity_roles(
    tmp_path: Path,
) -> None:
    forged = _alternate_role_electricity_source(tmp_path)
    assert forged.extraction.electric_lines_layer == "CABLE_SOURCE_ALTERNATE"
    assert (
        forged.extraction.transformation_posts_layer == "INSTALLATION_SOURCE_ALTERNATE"
    )

    with pytest.raises(GridProximityError):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)


@pytest.mark.parametrize(
    "archive_changes",
    [
        pytest.param({"provider": "IGN"}, id="provider"),
        pytest.param({"product": "BDTOPO"}, id="product"),
        pytest.param({"edition": "2026-06-16"}, id="edition"),
        pytest.param({"product_version": "3.6"}, id="product-version"),
        pytest.param(
            {"projection": "urn:ogc:def:crs:EPSG::2154"},
            id="projection",
        ),
        pytest.param({"package_format": "SHP"}, id="package-format"),
        pytest.param({"archive_format": "zip"}, id="archive-format"),
        pytest.param(
            {"source_url": "https://example.test/other-package.7z"},
            id="source-url",
        ),
        pytest.param(
            {"checksum_url": "https://example.test/other-package.md5"},
            id="checksum-url",
        ),
        pytest.param(
            {
                "official_checksum_algorithm": "sha256",
                "official_checksum": "b" * 64,
                "official_checksum_validated": True,
            },
            id="official-checksum",
        ),
        pytest.param(
            {"file_size": (SOURCE_CONFIG.expected_archive_size_bytes or 1) + 1},
            id="archive-size",
        ),
    ],
)
def test_public_proximity_rejects_archive_lineage_differing_from_config(
    tmp_path: Path,
    archive_changes: dict[str, object],
) -> None:
    source = _configured_role_electricity_source(tmp_path)
    forged_archive = replace(source.extraction.archive, **archive_changes)
    forged = replace(
        source,
        extraction=replace(source.extraction, archive=forged_archive),
    )

    with (
        patch(
            "landscout.stages.enrich_grid_proximity."
            "_enrich_parcel_grid_proximity_from_normalized",
        ) as computation,
        pytest.raises(GridProximityError),
    ):
        public_enrich_parcel_grid_proximity(_parcels(), forged, SOURCE_CONFIG)

    computation.assert_not_called()


def test_source_normalization_failure_stops_grid_computation() -> None:
    source = _electricity_source()

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity",
            side_effect=ValueError("physical source changed"),
            create=True,
        ) as normalizer,
        pytest.raises(GridProximityError),
    ):
        public_enrich_parcel_grid_proximity(_parcels(), source, SOURCE_CONFIG)

    normalizer.assert_called_once_with(source, SOURCE_CONFIG)


def test_separated_distance_uses_parcel_edge_not_centroid() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0
    )
    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(
        100.0
    )


def test_touching_line_has_zero_distance() -> None:
    touching = _lines([LineString([(10, -20), (10, 30)])])

    result = enrich_parcel_grid_proximity(_parcels(), touching, _posts())

    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == 0.0


def test_post_distance_uses_parcel_and_post_polygons() -> None:
    posts = _posts([Polygon([(60, 0), (60, 10), (70, 10), (70, 0), (60, 0)])])

    result = enrich_parcel_grid_proximity(_parcels(), _lines(), posts)

    assert result.parcels.loc[0, "nearest_post_proxy_distance_m"] == pytest.approx(50.0)


def test_epsg4326_input_is_calculated_in_lambert93_and_preserved() -> None:
    projected = _parcels()
    geographic = projected.to_crs("EPSG:4326")
    before_geometry = geographic.geometry.copy()

    result = enrich_parcel_grid_proximity(geographic, _lines(), _posts())

    assert result.parcels.crs == geographic.crs
    assert result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        100.0, abs=1e-6
    )
    assert result.parcels.geometry.geom_equals_exact(
        before_geometry.reset_index(drop=True), tolerance=0
    ).all()


def test_epsg2154_parcel_input_remains_epsg2154() -> None:
    result = enrich_parcel_grid_proximity(_parcels(), _lines(), _posts())

    assert result.parcels.crs is not None
    assert result.parcels.crs.to_epsg() == 2154


def test_valid_parcel_id_is_preserved_exactly() -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(identifiers=["FR-31-VALID-ID"]), _lines(), _posts()
    )

    assert result.parcels["parcel_id"].tolist() == ["FR-31-VALID-ID"]


def test_public_proximity_rejects_generated_parcel_column_before_normalization() -> (
    None
):
    parcels = _parcels()
    parcels["nearest_line_proxy_distance_m"] = 123.0

    with (
        patch(
            "landscout.stages.enrich_grid_proximity.normalize_ign_electricity"
        ) as normalize,
        pytest.raises(GridProximityError, match="collides.*generated"),
    ):
        public_enrich_parcel_grid_proximity(
            parcels,
            _electricity_source(),
            SOURCE_CONFIG,
        )

    normalize.assert_not_called()


@pytest.mark.parametrize(
    "identifier",
    [None, "", "   ", " PARCEL-1", "PARCEL-1 ", 123],
)
def test_invalid_parcel_id_hygiene_is_rejected(identifier: object) -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(
            _parcels(identifiers=[identifier]), _lines(), _posts()
        )


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        MultiPolygon([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]),
        Polygon([(0, 0, 5), (0, 10, 5), (10, 10, 5), (10, 0, 5), (0, 0, 5)]),
    ],
)
def test_supported_parcel_polygon_geometry_is_preserved(geometry: object) -> None:
    result = enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())

    assert result.parcels.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert result.parcels.geometry.iloc[0].has_z == geometry.has_z


@pytest.mark.parametrize(
    "geometry",
    [
        Point(1, 1),
        LineString([(0, 0), (10, 10)]),
        MultiLineString([[(0, 0), (10, 10)]]),
        GeometryCollection([Point(1, 1)]),
    ],
)
def test_semantically_wrong_parcel_geometry_is_rejected(geometry: object) -> None:
    with pytest.raises(GridProximityError, match="Polygon|MultiPolygon"):
        enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())


@pytest.mark.parametrize("kind", ["parcel", "line", "post"])
def test_missing_crs_is_rejected(kind: str) -> None:
    parcels = _parcels(crs=None if kind == "parcel" else "EPSG:2154")
    lines = _lines(crs=None if kind == "line" else "EPSG:2154")
    posts = _posts(crs=None if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="CRS"):
        enrich_parcel_grid_proximity(parcels, lines, posts)


@pytest.mark.parametrize("kind", ["line", "post"])
def test_wrong_grid_crs_is_rejected(kind: str) -> None:
    lines = _lines(crs="EPSG:4326" if kind == "line" else "EPSG:2154")
    posts = _posts(crs="EPSG:4326" if kind == "post" else "EPSG:2154")

    with pytest.raises(GridProximityError, match="2154"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


def test_z_line_has_same_horizontal_distance_as_xy_line() -> None:
    xy = _lines([LineString([(110, -20), (110, 30)])])
    xyz = _lines([LineString([(110, -20, 500), (110, 30, 900)])])

    xy_result = enrich_parcel_grid_proximity(_parcels(), xy, _posts())
    xyz_result = enrich_parcel_grid_proximity(_parcels(), xyz, _posts())

    assert xyz.geometry.iloc[0].has_z
    assert xyz_result.parcels.loc[0, "nearest_line_proxy_distance_m"] == pytest.approx(
        xy_result.parcels.loc[0, "nearest_line_proxy_distance_m"]
    )


def test_line_tie_is_counted_and_lexical_feature_id_wins() -> None:
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_proxy_distance_m"] == pytest.approx(100.0)
    assert row["nearest_line_tie_count"] == 2
    assert row["nearest_line_grid_feature_id"] == "A-LINE"
    assert row["nearest_exact_line_tie_count"] == 2
    assert row["nearest_exact_line_grid_feature_id"] == "A-LINE"
    assert result.voltage_level_proximity.loc[0, "tie_count"] == 2
    assert (
        result.voltage_level_proximity.loc[0, "nearest_line_grid_feature_id"]
        == "A-LINE"
    )
    assert len(result.parcels) == 1


def test_cross_voltage_tie_uses_lexical_global_feature_id() -> None:
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE-110", "A-LINE-275"],
        voltage_statuses=["EXACT", "EXACT"],
        voltages=[110.0, 275.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())
    profile = profile_grid_proximity(result)

    row = result.parcels.iloc[0]
    assert row["nearest_exact_line_proxy_distance_m"] == pytest.approx(100.0)
    assert row["nearest_exact_line_grid_feature_id"] == "A-LINE-275"
    assert row["nearest_exact_line_voltage_kv"] == 275.0
    assert row["nearest_exact_line_tie_count"] == 2
    assert result.voltage_level_proximity[
        "nearest_line_proxy_distance_m"
    ].tolist() == pytest.approx([100.0, 100.0])
    assert result.voltage_level_proximity["tie_count"].tolist() == [1, 1]
    assert profile.nearest_exact_line.tie_count == 1


def test_nonvalid_grid_geometries_are_excluded_without_row_loss() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    lines = _lines(
        [None, LineString(), invalid, LineString([(110, -20), (110, 30)])],
        identifiers=["NULL", "EMPTY", "INVALID", "VALID"],
        voltage_statuses=["UNKNOWN", "UNKNOWN", "UNKNOWN", "EXACT"],
        voltages=[None, None, None, 110.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert len(result.parcels) == 1
    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "VALID"


@pytest.mark.parametrize("kind", ["line", "post"])
def test_wrong_grid_feature_type_is_rejected(kind: str) -> None:
    lines = _lines(feature_types=["WRONG"] if kind == "line" else None)
    posts = _posts(feature_types=["WRONG"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="grid_feature_type"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


@pytest.mark.parametrize("kind", ["line", "post"])
def test_duplicate_grid_feature_id_is_rejected(kind: str) -> None:
    if kind == "line":
        lines = _lines(
            [LineString([(100, 0), (100, 10)])] * 2,
            identifiers=["DUPLICATE", "DUPLICATE"],
        )
        posts = _posts()
    else:
        lines = _lines()
        posts = _posts(
            [
                Polygon([(50, 0), (50, 5), (55, 5), (55, 0), (50, 0)]),
                Polygon([(60, 0), (60, 5), (65, 5), (65, 0), (60, 0)]),
            ],
            identifiers=["DUPLICATE", "DUPLICATE"],
        )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


@pytest.mark.parametrize("kind", ["line", "post"])
def test_wrong_spatial_role_is_rejected(kind: str) -> None:
    lines = _lines(spatial_roles=["EXACT"] if kind == "line" else None)
    posts = _posts(spatial_roles=["EXACT"] if kind == "post" else None)

    with pytest.raises(GridProximityError, match="PROXY_GEOMETRY"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


@pytest.mark.parametrize(
    ("kind", "geometry"),
    [
        ("line", Point(100, 0)),
        ("line", Polygon([(100, 0), (100, 5), (105, 5), (105, 0), (100, 0)])),
        ("post", Point(100, 0)),
        ("post", LineString([(100, 0), (100, 10)])),
    ],
)
def test_unsupported_valid_grid_geometry_type_is_rejected(
    kind: str, geometry: object
) -> None:
    lines = _lines([geometry]) if kind == "line" else _lines()
    posts = _posts([geometry]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="geometry types"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)


def test_supported_multi_geometries_are_accepted() -> None:
    lines = _lines(
        [MultiLineString([[(110, -20), (110, 30)], [(120, -20), (120, 30)]])]
    )
    posts = _posts(
        [MultiPolygon([Polygon([(110, 0), (110, 5), (115, 5), (115, 0), (110, 0)])])]
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, posts)

    assert len(result.parcels) == 1


@pytest.mark.parametrize(
    "status", ["EXACT", "BELOW", "UNKNOWN", "DEENERGIZED", "UNPARSED"]
)
def test_nearest_any_line_preserves_every_voltage_status(status: str) -> None:
    voltage = 110.0 if status == "EXACT" else None
    lines = _lines(voltage_statuses=[status], voltages=[voltage])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_voltage_status"] == status


def test_nearest_exact_and_voltage_table_exclude_nonexact_lines() -> None:
    lines = _lines(
        [
            LineString([(20, -20), (20, 30)]),
            LineString([(110, -20), (110, 30)]),
            LineString([(210, -20), (210, 30)]),
        ],
        identifiers=["BELOW", "EXACT-110", "EXACT-275"],
        voltage_statuses=["BELOW", "EXACT", "EXACT"],
        voltages=[None, 110.0, 275.0],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    row = result.parcels.iloc[0]
    assert row["nearest_line_grid_feature_id"] == "BELOW"
    assert row["nearest_exact_line_grid_feature_id"] == "EXACT-110"
    assert row["nearest_exact_line_voltage_kv"] == 110.0
    assert result.voltage_level_proximity["voltage_kv"].tolist() == [110.0, 275.0]
    assert len(result.voltage_level_proximity) == 2
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )


def test_voltage_table_is_exact_ordered_cartesian_product() -> None:
    result = _two_parcel_two_voltage_result()

    assert tuple(item.voltage_kv for item in result.voltage_level_coverage) == (
        110.0,
        275.0,
    )
    assert len(result.voltage_level_proximity) == 4
    assert not result.voltage_level_proximity.duplicated(
        ["parcel_id", "voltage_kv"]
    ).any()
    for voltage_kv in (110.0, 275.0):
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == voltage_kv
        ]
        assert rows["parcel_id"].tolist() == ["PARCEL-2", "PARCEL-1"]


def test_invalid_exact_voltage_values_are_not_used_as_exact() -> None:
    lines = _lines(
        [LineString([(20, -20), (20, 30)])] * 4,
        identifiers=["ZERO", "NEGATIVE", "INFINITE", "TEXT"],
        voltage_statuses=["EXACT"] * 4,
        voltages=[0.0, -1.0, float("inf"), "110"],
    )

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.voltage_level_proximity.empty


def test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table() -> None:
    lines = _lines(voltage_statuses=["UNKNOWN"], voltages=[None])

    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    assert result.parcels.loc[0, "nearest_line_grid_feature_id"] == "LINE-1"
    assert result.parcels["nearest_exact_line_proxy_distance_m"].isna().all()
    assert result.parcels["nearest_exact_line_grid_feature_id"].isna().all()
    assert result.voltage_level_proximity.empty
    assert list(result.voltage_level_proximity.columns) == list(
        VOLTAGE_PROXIMITY_COLUMNS
    )
    assert is_float_dtype(result.parcels["nearest_exact_line_proxy_distance_m"].dtype)
    assert is_float_dtype(result.parcels["nearest_exact_line_voltage_kv"].dtype)
    assert is_integer_dtype(result.parcels["nearest_exact_line_tie_count"].dtype)
    assert str(result.parcels["nearest_exact_line_tie_count"].dtype) == "Int64"
    assert is_float_dtype(result.voltage_level_proximity["voltage_kv"].dtype)
    assert is_float_dtype(
        result.voltage_level_proximity["nearest_line_proxy_distance_m"].dtype
    )
    assert str(result.voltage_level_proximity["tie_count"].dtype) == "Int64"
    assert result.voltage_level_coverage == ()
    profile = profile_grid_proximity(result)
    assert profile.nearest_exact_line.count == 0
    assert profile.nearest_exact_line.missing_count == 1


@pytest.mark.parametrize("column", ["parcel_id", "geometry"])
def test_missing_parcel_column_is_rejected(column: str) -> None:
    parcels = _parcels().drop(columns=column)

    with pytest.raises(GridProximityError, match=column):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())


def test_null_parcel_id_is_rejected() -> None:
    with pytest.raises(GridProximityError, match="parcel_id"):
        enrich_parcel_grid_proximity(_parcels(identifiers=[None]), _lines(), _posts())


def test_duplicate_parcel_id_is_rejected() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(GridProximityError, match="unique"):
        enrich_parcel_grid_proximity(parcels, _lines(), _posts())


@pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null"),
        (Polygon(), "empty"),
        (
            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),
            "valid",
        ),
    ],
)
def test_bad_parcel_geometry_is_rejected(geometry: object, message: str) -> None:
    with pytest.raises(GridProximityError, match=message):
        enrich_parcel_grid_proximity(_parcels([geometry]), _lines(), _posts())


def test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved() -> None:
    parcels = _parcels(
        [
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND-SPATIAL", "FIRST-SPATIAL"],
        index=[99, 99],
    )
    lines = _lines()
    posts = _posts()
    parcels_before = deepcopy(parcels)
    lines_before = deepcopy(lines)
    posts_before = deepcopy(posts)

    result = enrich_parcel_grid_proximity(parcels, lines, posts)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(lines, lines_before)
    assert_geodataframe_equal(posts, posts_before)
    assert result.parcels["parcel_id"].tolist() == [
        "SECOND-SPATIAL",
        "FIRST-SPATIAL",
    ]
    assert isinstance(result.parcels.index, pd.RangeIndex)


def test_distance_profile_is_threshold_free_and_tracks_ties() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    lines = _lines(
        [
            LineString([(-100, -20), (-100, 30)]),
            LineString([(110, -20), (110, 30)]),
        ],
        identifiers=["Z-LINE", "A-LINE"],
    )
    result = enrich_parcel_grid_proximity(parcels, lines, _posts())

    profile = profile_grid_proximity(result)

    assert profile.parcel_count == 2
    assert profile.nearest_line.count == 2
    assert profile.nearest_line.missing_count == 0
    assert profile.nearest_line.minimum == pytest.approx(50.0)
    assert profile.nearest_line.p50 == pytest.approx(75.0)
    assert profile.nearest_line.maximum == pytest.approx(100.0)
    assert profile.nearest_line.tie_count == 1
    assert profile.voltage_levels[0].voltage_kv == 110.0
    assert profile.voltage_levels[0].line_feature_count == 2
    assert profile.voltage_levels[0].parcel_proximity_count == 2


def test_profile_rejects_missing_voltage_cartesian_row() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[:-1].copy()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))


def test_profile_rejects_unknown_voltage_parcel_with_same_total_count() -> None:
    result = _two_parcel_two_voltage_result()
    corrupted = _mutate_voltage_result(result, "parcel_id", "UNKNOWN-PARCEL")

    with pytest.raises(GridProximityError):
        profile_grid_proximity(corrupted)


def test_profile_rejects_duplicate_parcel_voltage_pair() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.copy()
    table.at[1, "parcel_id"] = table.at[0, "parcel_id"]

    with pytest.raises(GridProximityError, match="unique"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))


def test_profile_rejects_voltage_rows_out_of_parcel_order() -> None:
    result = _two_parcel_two_voltage_result()
    table = result.voltage_level_proximity.iloc[[1, 0, 2, 3]].reset_index(drop=True)

    with pytest.raises(GridProximityError, match="exact parcel set"):
        profile_grid_proximity(replace(result, voltage_level_proximity=table))


def test_profile_rejects_inconsistent_global_exact_distance() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="exact-line distance"):
        profile_grid_proximity(
            _mutate_parcel_result(
                result,
                "nearest_exact_line_proxy_distance_m",
                5000.0,
            )
        )


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_exact_line_grid_feature_id", "OTHER-LINE"),
        ("nearest_exact_line_source_feature_id", "OTHER-SOURCE"),
        ("nearest_exact_line_voltage_kv", 275.0),
    ],
)
def test_profile_rejects_inconsistent_global_exact_identity(
    column: str,
    value: object,
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_exact_line_manager_name", "OTHER MANAGER"),
        ("nearest_exact_line_asset_status_raw", "OTHER STATUS"),
        ("nearest_exact_line_source_department_code", "32"),
        ("nearest_exact_line_source_edition", "2026-09-15"),
        ("nearest_exact_line_source_archive_sha256", "b" * 64),
    ],
)
def test_profile_rejects_inconsistent_global_exact_metadata(
    column: str,
    value: object,
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="inconsistent"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


def test_profile_rejects_inconsistent_global_exact_tie_count() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie count"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_tie_count", 2)
        )


@pytest.mark.parametrize(
    "value",
    [
        0,
        -1,
        1.5,
        float("inf"),
        "2",
        None,
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
@pytest.mark.parametrize(
    "column",
    [
        "nearest_line_tie_count",
        "nearest_exact_line_tie_count",
        "nearest_post_tie_count",
    ],
)
def test_profile_rejects_bad_required_match_tie_count(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


@pytest.mark.parametrize(
    "value",
    [
        0,
        -1,
        1.5,
        float("inf"),
        "2",
        None,
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
def test_profile_rejects_bad_long_table_tie_count(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="tie_count|match"):
        profile_grid_proximity(_mutate_voltage_result(result, "tie_count", value))


@pytest.mark.parametrize(
    "column",
    [
        "nearest_line_grid_feature_id",
        "nearest_line_source_feature_id",
        "nearest_exact_line_grid_feature_id",
        "nearest_exact_line_source_feature_id",
        "nearest_post_grid_feature_id",
        "nearest_post_source_feature_id",
    ],
)
def test_profile_rejects_missing_main_match_feature_id(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_parcel_result(result, column, None))


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_line_proxy_distance_m", None),
        ("nearest_line_proxy_distance_m", "100"),
        ("nearest_exact_line_proxy_distance_m", float("inf")),
        ("nearest_post_proxy_distance_m", -1),
    ],
)
def test_profile_rejects_bad_required_match_distance(
    column: str, value: object
) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


@pytest.mark.parametrize(
    "value",
    [None, 0, -1, float("inf"), "110", 999.0],
)
def test_profile_rejects_bad_exact_match_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="voltage|match"):
        profile_grid_proximity(
            _mutate_parcel_result(result, "nearest_exact_line_voltage_kv", value)
        )


def test_profile_rejects_bad_result_parcel_id() -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="parcel_id"):
        profile_grid_proximity(_mutate_parcel_result(result, "parcel_id", " BAD "))


def test_profile_rejects_missing_required_proximity_column() -> None:
    result = _two_parcel_two_voltage_result()
    parcels = result.parcels.drop(columns="nearest_line_grid_feature_id")

    with pytest.raises(GridProximityError, match="Missing proximity"):
        profile_grid_proximity(replace(result, parcels=parcels))


@pytest.mark.parametrize("mutation", ["reversed", "duplicate"])
def test_profile_rejects_nondeterministic_or_duplicate_coverage(
    mutation: str,
) -> None:
    result = _two_parcel_two_voltage_result()
    if mutation == "reversed":
        coverage = tuple(reversed(result.voltage_level_coverage))
    else:
        coverage = (*result.voltage_level_coverage, result.voltage_level_coverage[0])

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))


@pytest.mark.parametrize(
    "voltage_kv",
    [
        0,
        -1,
        float("inf"),
        "110",
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
def test_profile_rejects_invalid_voltage_coverage_level(voltage_kv: object) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (VoltageLevelCoverage(voltage_kv=voltage_kv, line_feature_count=1),)

    with pytest.raises(GridProximityError, match="coverage"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))


@pytest.mark.parametrize("feature_count", [0, -1, 1.5, float("inf"), True, "2"])
def test_profile_rejects_invalid_voltage_coverage_feature_count(
    feature_count: object,
) -> None:
    result = _two_parcel_two_voltage_result()
    coverage = (
        VoltageLevelCoverage(voltage_kv=110.0, line_feature_count=feature_count),
    )

    with pytest.raises(GridProximityError, match="line_feature_count"):
        profile_grid_proximity(replace(result, voltage_level_coverage=coverage))


@pytest.mark.parametrize(
    "value",
    [None, 0, -1, float("inf"), "110", 220.0],
)
def test_profile_rejects_invalid_long_table_voltage(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="Voltage proximity"):
        profile_grid_proximity(_mutate_voltage_result(result, "voltage_kv", value))


@pytest.mark.parametrize(
    "column",
    [
        "nearest_line_grid_feature_id",
        "nearest_line_source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    ],
)
def test_profile_rejects_missing_long_table_match_lineage(column: str) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError, match="require"):
        profile_grid_proximity(_mutate_voltage_result(result, column, None))


@pytest.mark.parametrize(
    "value",
    [
        None,
        -1,
        float("inf"),
        "100",
        pytest.param(OVERFLOWING_INTEGER, id="overflowing-integer"),
    ],
)
def test_profile_rejects_bad_long_table_distance(value: object) -> None:
    result = _two_parcel_two_voltage_result()

    with pytest.raises(GridProximityError):
        profile_grid_proximity(
            _mutate_voltage_result(result, "nearest_line_proxy_distance_m", value)
        )


def test_profile_allows_consistent_missing_manager_and_asset_status() -> None:
    lines = _lines()
    lines["manager_name"] = None
    lines["asset_status_raw"] = None
    result = enrich_parcel_grid_proximity(_parcels(), lines, _posts())

    profile = profile_grid_proximity(result)

    assert profile.parcel_count == 1
    assert result.parcels["nearest_exact_line_manager_name"].isna().all()
    assert result.parcels["nearest_exact_line_asset_status_raw"].isna().all()
    assert result.voltage_level_proximity["manager_name"].isna().all()
    assert result.voltage_level_proximity["asset_status_raw"].isna().all()


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("nearest_exact_line_proxy_distance_m", 1.0),
        ("nearest_exact_line_grid_feature_id", "LINE"),
        ("nearest_exact_line_source_feature_id", "SOURCE"),
        ("nearest_exact_line_tie_count", 1),
        ("nearest_exact_line_voltage_kv", 110.0),
    ],
)
def test_profile_rejects_nonnull_exact_field_without_exact_coverage(
    column: str, value: object
) -> None:
    result = enrich_parcel_grid_proximity(
        _parcels(),
        _lines(voltage_statuses=["UNKNOWN"], voltages=[None]),
        _posts(),
    )

    with pytest.raises(GridProximityError, match="unmatched|entirely"):
        profile_grid_proximity(_mutate_parcel_result(result, column, value))


@pytest.mark.parametrize("kind", ["line", "post"])
def test_no_valid_required_grid_feature_is_rejected(kind: str) -> None:
    lines = _lines([None]) if kind == "line" else _lines()
    posts = _posts([None]) if kind == "post" else _posts()

    with pytest.raises(GridProximityError, match="No VALID"):
        enrich_parcel_grid_proximity(_parcels(), lines, posts)
```
