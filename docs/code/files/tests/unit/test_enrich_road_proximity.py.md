# `tests/unit/test_enrich_road_proximity.py`

## File identity

- Repository path: `tests/unit/test_enrich_road_proximity.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.
- Source SHA256: `153e2611e0d1ddc8ae4f28389e5311cca7b4c14668efbb809cc88f2645831367`

## 1. STEP 7F.1A.4 contract delta

- Ruff formatting only in STEP 7F.1A.4; executable contract, values, schemas, and test intent are unchanged. The companion is refreshed because its raw bytes and SHA changed.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)`
- `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`
- `import landscout.stages.enrich_road_proximity as module`

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

### `POLICY_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
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

### `_metric_parcels`

**Purpose:** Implements `metric parcels` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
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
| `index` | keyword-only | `list[object] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {"parcel_id": ids, "source_value": list(range(count))},<br>        geometry=values,<br>        crs="EPSG:2154",<br>        index=frame_index,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::_parcels` via `_metric_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::_parcels` via `_metric_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_missing_or_wrong_storage_crs_is_rejected` via `_metric_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_or_wrong_storage_crs_is_rejected` via `_metric_parcels`

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
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    frame_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs="EPSG:2154",
        index=frame_index,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_parcels`

**Purpose:** Implements `parcels` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
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
| `index` | keyword-only | `list[object] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs(<br>        "EPSG:4326"<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::_enrich` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::_enrich` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_road_source_type_has_controlled_error` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_road_source_type_has_controlled_error` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_source_config_type_has_controlled_error` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_source_config_type_has_controlled_error` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_policy_path_type_has_controlled_error` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_policy_path_type_has_controlled_error` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_malformed_policy_stops_before_application` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_malformed_policy_stops_before_application` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_invalid_parcel_identity_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_invalid_parcel_identity_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_id_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_id_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_columns_are_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_columns_are_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_missing_or_inactive_geometry_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_or_inactive_geometry_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_missing_or_wrong_storage_crs_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_or_wrong_storage_crs_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_geometry_kind_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_geometry_kind_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_bad_parcel_geometry_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_bad_parcel_geometry_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_polygon_and_multipolygon_are_accepted` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_polygon_and_multipolygon_are_accepted` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_application_result_type_is_rejected` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_application_result_type_is_rejected` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_empty_eligible_class_emits_null_row_per_parcel` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_empty_eligible_class_emits_null_row_per_parcel` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_output_shape_columns_and_order_are_deterministic` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_output_shape_columns_and_order_are_deterministic` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_parcels_and_road_application_are_not_mutated` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_parcels_and_road_application_are_not_mutated` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_result_dataclasses_are_frozen` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_result_dataclasses_are_frozen` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_result_parcel_frame_is_an_independent_copy` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_result_parcel_frame_is_an_independent_copy` via `_parcels`
- direct call: `tests.unit.test_enrich_road_proximity::test_parcel_preservation_uses_exact_non_geometry_values` via `_parcels`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_parcel_preservation_uses_exact_non_geometry_values` via `_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_metric_parcels` | `tests.unit.test_enrich_road_proximity._metric_parcels` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(geometries, identifiers=identifiers, index=index).to_crs(
        "EPSG:4326"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_road_row`

**Purpose:** Implements `road row` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _road_row(
    road_class: str,
    x: float,
    *,
    identifier: str,
    geometry: object | None = None,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `road_class` | positional-or-keyword | `str` | `required` |
| `x` | positional-or-keyword | `float` | `required` |
| `identifier` | keyword-only | `str` | `required` |
| `geometry` | keyword-only | `object \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "road_feature_id": identifier,<br>        "source_feature_id": f"SOURCE-{identifier}",<br>        "geometry_status": "VALID",<br>        "nature_raw": "Route à 1 chaussée",<br>        "importance_raw": "2",<br>        "asset_status_raw": "En service",<br>        "private_raw": 0.0,<br>        "light_vehicle_access_raw": "Libre",<br>        "carriageway_width_raw": 7.0,<br>        "closure_period_raw": None,<br>        "restriction_nature_raw": None,<br>        "source_layer": "troncon_de_route",<br>        "source_department_code": "31",<br>        "source_edition": "2026-06-15",<br>        "source_archive_sha256": "a" * 64,<br>        "road_proxy_primary_rule": primary_rule,<br>        "road_proxy_class": road_class,<br>        "road_proxy_rule_trace_json": f'["{primary_rule}"]',<br>        "road_proxy_unknown_fields_json": "[]",<br>        "road_proxy_toll_evidence": False,<br>        "road_proxy_policy_id": policy.policy_id,<br>        "road_proxy_policy_schema_version": policy.schema_version,<br>        "road_proxy_policy_config_sha256": policy.config_sha256,<br>        "road_proxy_policy_scope": policy.scope,<br>        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,<br>        "geometry": geometry or LineString([(x, -20), (x, 30)]),<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::_roads` via `_road_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::_roads` via `_road_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_road_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_road_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_road_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_road_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_road_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_road_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_road_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_road_row`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
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
def _road_row(
    road_class: str,
    x: float,
    *,
    identifier: str,
    geometry: object | None = None,
) -> dict[str, object]:
    policy = load_ign_road_vehicle_proxy_policy()
    primary_rule = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "NOT_DISTANCE_PROXY": "FICTITIOUS_GEOMETRY",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }[road_class]
    return {
        "road_feature_id": identifier,
        "source_feature_id": f"SOURCE-{identifier}",
        "geometry_status": "VALID",
        "nature_raw": "Route à 1 chaussée",
        "importance_raw": "2",
        "asset_status_raw": "En service",
        "private_raw": 0.0,
        "light_vehicle_access_raw": "Libre",
        "carriageway_width_raw": 7.0,
        "closure_period_raw": None,
        "restriction_nature_raw": None,
        "source_layer": "troncon_de_route",
        "source_department_code": "31",
        "source_edition": "2026-06-15",
        "source_archive_sha256": "a" * 64,
        "road_proxy_primary_rule": primary_rule,
        "road_proxy_class": road_class,
        "road_proxy_rule_trace_json": f'["{primary_rule}"]',
        "road_proxy_unknown_fields_json": "[]",
        "road_proxy_toll_evidence": False,
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_policy_scope": policy.scope,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "geometry": geometry or LineString([(x, -20), (x, 30)]),
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_roads`

**Purpose:** Implements `roads` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `rows` | positional-or-keyword | `list[dict[str, object]] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(values, geometry="geometry", crs="EPSG:2154")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::_source` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::_source` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::_enrich` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::_enrich` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_independent_policy_sha_mismatch_is_rejected` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_independent_policy_sha_mismatch_is_rejected` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_duplicate_road_feature_id_is_rejected` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_road_feature_id_is_rejected` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_unknown_road_proxy_class_is_rejected` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_unknown_road_proxy_class_is_rejected` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_missing_road_policy_lineage_is_rejected` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_road_policy_lineage_is_rejected` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_eligible_class_requires_valid_geometry_status` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_eligible_class_requires_valid_geometry_status` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_eligible_class_rejects_unsupported_geometry` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_eligible_class_rejects_unsupported_geometry` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_not_distance_road_is_counted_but_never_indexed` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_not_distance_road_is_counted_but_never_indexed` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_empty_eligible_class_emits_null_row_per_parcel` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_empty_eligible_class_emits_null_row_per_parcel` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_parcels_and_road_application_are_not_mutated` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_parcels_and_road_application_are_not_mutated` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_selected_rows_belong_to_requested_class` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_selected_rows_belong_to_requested_class` via `_roads`
- direct call: `tests.unit.test_enrich_road_proximity::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_roads`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_roads`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_road_row` | `tests.unit.test_enrich_road_proximity._road_row` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |

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
def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
    values = rows or [
        _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="ROAD-GENERAL"),
        _road_row("LIMITED_VEHICLE_PROXY", 30, identifier="ROAD-LIMITED"),
        _road_row("RESTRICTED_REVIEW", 15, identifier="ROAD-RESTRICTED"),
        _road_row("NOT_GENERAL_VEHICLE_PROXY", 40, identifier="ROAD-NOT-GENERAL"),
        _road_row("NOT_DISTANCE_PROXY", 11, identifier="ROAD-NOT-DISTANCE"),
        _road_row("UNKNOWN_REVIEW", 50, identifier="ROAD-UNKNOWN"),
    ]
    return gpd.GeoDataFrame(values, geometry="geometry", crs="EPSG:2154")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source`

**Purpose:** Implements `source` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _source() -> IgnBdTopoRoadData:
```

- Exact decorators: none.
- Declared return annotation: `IgnBdTopoRoadData`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `IgnBdTopoRoadData(<br>        extraction=cast(Any, None),<br>        road_segments=_roads(),<br>        road_segments_summary=cast(Any, None),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::_enrich` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::_enrich` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_type_has_controlled_error` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_type_has_controlled_error` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_source_config_type_has_controlled_error` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_source_config_type_has_controlled_error` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_policy_path_type_has_controlled_error` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_policy_path_type_has_controlled_error` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_malformed_policy_stops_before_application` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_malformed_policy_stops_before_application` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_application_result_type_is_rejected` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_application_result_type_is_rejected` via `_source`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `_source`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoRoadData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` |
| `cast` | `typing.cast` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |

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
def _source() -> IgnBdTopoRoadData:
    return IgnBdTopoRoadData(
        extraction=cast(Any, None),
        road_segments=_roads(),
        road_segments_summary=cast(Any, None),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_enrich`

**Purpose:** Implements `enrich` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelRoadProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `roads` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `policy_path` | keyword-only | `Path \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `enrich_parcel_road_proximity(<br>            parcels if parcels is not None else _parcels(),<br>            _source(),<br>            SOURCE_CONFIG,<br>            policy_path,<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::test_independent_policy_sha_mismatch_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_independent_policy_sha_mismatch_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_invalid_parcel_identity_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_invalid_parcel_identity_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_id_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_id_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_columns_are_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_columns_are_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_missing_or_inactive_geometry_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_or_inactive_geometry_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_missing_or_wrong_storage_crs_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_or_wrong_storage_crs_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_geometry_kind_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_geometry_kind_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_bad_parcel_geometry_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_bad_parcel_geometry_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_polygon_and_multipolygon_are_accepted` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_polygon_and_multipolygon_are_accepted` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_duplicate_road_feature_id_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_road_feature_id_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_unknown_road_proxy_class_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_unknown_road_proxy_class_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_missing_road_policy_lineage_is_rejected` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_road_policy_lineage_is_rejected` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_eligible_class_requires_valid_geometry_status` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_eligible_class_requires_valid_geometry_status` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_eligible_class_rejects_unsupported_geometry` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_eligible_class_rejects_unsupported_geometry` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_not_distance_road_is_counted_but_never_indexed` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_not_distance_road_is_counted_but_never_indexed` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_known_polygon_to_line_distance_is_ten_metres` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_known_polygon_to_line_distance_is_ten_metres` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_distance_uses_full_polygon_not_centroid` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_distance_uses_full_polygon_not_centroid` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_each_eligible_class_has_independent_distance` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_each_eligible_class_has_independent_distance` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_near_not_distance_road_cannot_change_general_distance` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_near_not_distance_road_cannot_change_general_distance` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_single_nearest_road_has_tie_count_one` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_single_nearest_road_has_tie_count_one` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_empty_eligible_class_emits_null_row_per_parcel` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_empty_eligible_class_emits_null_row_per_parcel` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_output_shape_columns_and_order_are_deterministic` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_output_shape_columns_and_order_are_deterministic` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_class_coverage_is_complete_and_strict` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_class_coverage_is_complete_and_strict` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_selected_road_evidence_and_lineage_are_exact` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_selected_road_evidence_and_lineage_are_exact` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_parcels_and_road_application_are_not_mutated` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_parcels_and_road_application_are_not_mutated` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::_corrupt_nearest_output` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::_corrupt_nearest_output` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_result_dataclasses_are_frozen` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_result_dataclasses_are_frozen` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_no_business_decision_columns_or_implementation_exist` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_no_business_decision_columns_or_implementation_exist` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_result_parcel_frame_is_an_independent_copy` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_result_parcel_frame_is_an_independent_copy` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_class_proximity_is_plain_dataframe` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_class_proximity_is_plain_dataframe` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_selected_rows_belong_to_requested_class` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_selected_rows_belong_to_requested_class` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_matched_output_dtypes_are_stable` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_matched_output_dtypes_are_stable` via `_enrich`
- direct call: `tests.unit.test_enrich_road_proximity::test_parcel_preservation_uses_exact_non_geometry_values` via `_enrich`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_parcel_preservation_uses_exact_non_geometry_values` via `_enrich`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnRoadVehicleProxyApplicationResult` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationResult` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `patch` | `unittest.mock.patch` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |

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
def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
    application = IgnRoadVehicleProxyApplicationResult(
        roads if roads is not None else _roads()
    )
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ):
        return enrich_parcel_road_proximity(
            parcels if parcels is not None else _parcels(),
            _source(),
            SOURCE_CONFIG,
            policy_path,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_row`

**Purpose:** Implements `row` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `ParcelRoadProximityResult` | `required` |
| `road_class` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result.class_proximity.loc[<br>        result.class_proximity["road_proxy_class"].eq(road_class)<br>    ].iloc[0]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::test_known_polygon_to_line_distance_is_ten_metres` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_known_polygon_to_line_distance_is_ten_metres` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_intersecting_or_touching_road_has_zero_distance` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_distance_uses_full_polygon_not_centroid` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_distance_uses_full_polygon_not_centroid` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_each_eligible_class_has_independent_distance` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_each_eligible_class_has_independent_distance` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_near_not_distance_road_cannot_change_general_distance` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_near_not_distance_road_cannot_change_general_distance` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_single_nearest_road_has_tie_count_one` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_single_nearest_road_has_tie_count_one` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_exact_tie_counts_two_and_lexical_id_wins` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_tie_winner_is_independent_of_source_order` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_unequal_distance_wins_regardless_of_identifier` via `_row`
- direct call: `tests.unit.test_enrich_road_proximity::test_selected_road_evidence_and_lineage_are_exact` via `_row`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_selected_road_evidence_and_lineage_are_exact` via `_row`

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
def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
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
  - `assert not hasattr(stages, "_nearest_class_rows")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
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
    import landscout.stages.enrich_road_proximity as module

    expected = {
        "RoadProximityError",
        "RoadProxyClassCoverage",
        "ParcelRoadProximityResult",
        "enrich_parcel_road_proximity",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_nearest_class_rows")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_parcel_type_has_controlled_error`

**Purpose:** Regression invariant: wrong parcel type has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_parcel_type_has_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `cast` | `typing.cast` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |

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
def test_wrong_parcel_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_road_source_type_has_controlled_error`

**Purpose:** Regression invariant: wrong road source type has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_road_source_type_has_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `cast` | `typing.cast` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_wrong_road_source_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), cast(Any, object()), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_source_config_type_has_controlled_error`

**Purpose:** Regression invariant: wrong source config type has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_source_config_type_has_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |
| `cast` | `typing.cast` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), cast(Any, object()))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_policy_path_type_has_controlled_error`

**Purpose:** Regression invariant: wrong policy path type has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_policy_path_type_has_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |
| `cast` | `typing.cast` |

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
def test_wrong_policy_path_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), SOURCE_CONFIG, cast(Any, "policy.yaml")
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_stage_is_invoked_exactly_once`

**Purpose:** Regression invariant: application stage is invoked exactly once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_stage_is_invoked_exactly_once() -> None:
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
| `IgnRoadVehicleProxyApplicationResult` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationResult` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `patch` | `unittest.mock.patch` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |
| `source_application.assert_called_once` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_application_stage_is_invoked_exactly_once() -> None:
    application = IgnRoadVehicleProxyApplicationResult(_roads())
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ) as source_application:
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    source_application.assert_called_once()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_failure_stops_proximity`

**Purpose:** Regression invariant: application failure stops proximity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_failure_stops_proximity() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `IgnRoadVehicleProxyApplicationError` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationError` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |
| `spatial_index.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_application_failure_stops_proximity() -> None:
    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
            side_effect=IgnRoadVehicleProxyApplicationError("bad source"),
        ),
        patch("landscout.stages.enrich_road_proximity.STRtree") as spatial_index,
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    spatial_index.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_policy_stops_before_application`

**Purpose:** Regression invariant: malformed policy stops before application. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_policy_stops_before_application(tmp_path: Path) -> None:
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
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |
| `source_application.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_malformed_policy_stops_before_application(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy"
        ) as source_application,
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)

    source_application.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_independent_policy_sha_mismatch_is_rejected`

**Purpose:** Regression invariant: independent policy sha mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_independent_policy_sha_mismatch_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="policy\|SHA\|lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
| In-memory mutation | `roads["road_proxy_policy_config_sha256"] = "b" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_independent_policy_sha_mismatch_is_rejected() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with pytest.raises(RoadProximityError, match="policy|SHA|lineage"):
        _enrich(roads=roads)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_parcel_identity_is_rejected`

**Purpose:** Regression invariant: invalid parcel identity is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_parcel_identity_is_rejected(mutation: Any, message: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda frame: frame.drop(columns="parcel_id"), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=None), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=123), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=""), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=" BAD "), "parcel_id"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `Any` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `mutation` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
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
def test_invalid_parcel_identity_is_rejected(mutation: Any, message: str) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=mutation(_parcels()))
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
  - `pytest.raises(RoadProximityError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(parcels=parcels)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_columns_are_rejected`

**Purpose:** Regression invariant: duplicate parcel columns are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_columns_are_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.concat` | `pandas.concat` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
def test_duplicate_parcel_columns_are_rejected() -> None:
    parcels = _parcels()
    duplicated = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(RoadProximityError, match="duplicate"):
        _enrich(parcels=duplicated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_or_inactive_geometry_is_rejected`

**Purpose:** Regression invariant: missing or inactive geometry is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_or_inactive_geometry_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="geometry")`
  - `pytest.raises(RoadProximityError, match="active")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.assign(other_geometry=parcels.geometry).set_geometry` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.assign` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.assign(other_geometry=parcels.geometry).set_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | `parcels.drop(columns="geometry")`<br>`parcels.assign(other_geometry=parcels.geometry).set_geometry(<br>        "other_geometry"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_or_inactive_geometry_is_rejected() -> None:
    parcels = _parcels()
    missing = parcels.drop(columns="geometry")
    inactive = parcels.assign(other_geometry=parcels.geometry).set_geometry(
        "other_geometry"
    )

    with pytest.raises(RoadProximityError, match="geometry"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="active"):
        _enrich(parcels=inactive)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_or_wrong_storage_crs_is_rejected`

**Purpose:** Regression invariant: missing or wrong storage crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_or_wrong_storage_crs_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="CRS")`
  - `pytest.raises(RoadProximityError, match="4326")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels().set_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_metric_parcels` | `tests.unit.test_enrich_road_proximity._metric_parcels` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_parcels().set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `_parcels().set_crs(None, allow_override=True)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_or_wrong_storage_crs_is_rejected() -> None:
    missing = _parcels().set_crs(None, allow_override=True)
    wrong = _metric_parcels()

    with pytest.raises(RoadProximityError, match="CRS"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="4326"):
        _enrich(parcels=wrong)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_parcel_geometry_kind_is_rejected`

**Purpose:** Regression invariant: wrong parcel geometry kind is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_parcel_geometry_kind_is_rejected(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [Point(0, 0), LineString([(0, 0), (10, 10)])],
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
  - `pytest.raises(RoadProximityError, match="Polygon\|MultiPolygon")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
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
def test_wrong_parcel_geometry_kind_is_rejected(geometry: object) -> None:
    with pytest.raises(RoadProximityError, match="Polygon|MultiPolygon"):
        _enrich(parcels=_parcels([geometry]))
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
  - `pytest.raises(RoadProximityError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
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
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=_parcels([geometry]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_polygon_and_multipolygon_are_accepted`

**Purpose:** Regression invariant: polygon and multipolygon are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_polygon_and_multipolygon_are_accepted(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        MultiPolygon([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]),
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
  - `assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
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
def test_polygon_and_multipolygon_are_accepted(geometry: object) -> None:
    assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_application_result_type_is_rejected`

**Purpose:** Regression invariant: wrong application result type is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_application_result_type_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |

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
def test_wrong_application_result_type_is_rejected() -> None:
    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
            return_value=object(),
        ),
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_roads_must_be_geodataframe`

**Purpose:** Regression invariant: application roads must be geodataframe. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_roads_must_be_geodataframe() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnRoadVehicleProxyApplicationResult` | `landscout.stages.apply_road_vehicle_proxy_policy.IgnRoadVehicleProxyApplicationResult` |
| `cast` | `typing.cast` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_roads().drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_source` | `tests.unit.test_enrich_road_proximity._source` |

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
| In-memory mutation | `_roads().drop(columns="geometry")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_application_roads_must_be_geodataframe() -> None:
    application = IgnRoadVehicleProxyApplicationResult(
        cast(Any, pd.DataFrame(_roads().drop(columns="geometry")))
    )
    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
            return_value=application,
        ),
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_road_feature_id_is_rejected`

**Purpose:** Regression invariant: duplicate road feature id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_road_feature_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
| In-memory mutation | `roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_road_feature_id_is_rejected() -> None:
    roads = _roads()
    roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(roads=roads)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_road_proxy_class_is_rejected`

**Purpose:** Regression invariant: unknown road proxy class is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_road_proxy_class_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="class")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
| In-memory mutation | `roads.loc[0, "road_proxy_class"] = "INVENTED"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_road_proxy_class_is_rejected() -> None:
    roads = _roads()
    roads.loc[0, "road_proxy_class"] = "INVENTED"

    with pytest.raises(RoadProximityError, match="class"):
        _enrich(roads=roads)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_road_policy_lineage_is_rejected`

**Purpose:** Regression invariant: missing road policy lineage is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_road_policy_lineage_is_rejected(column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    [
        "road_proxy_policy_id",
        "road_proxy_policy_schema_version",
        "road_proxy_policy_config_sha256",
        "road_proxy_heavy_vehicle_access",
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
  - `pytest.raises(RoadProximityError, match="column\|lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_roads().drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
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
| In-memory mutation | `_roads().drop(columns=column)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_road_policy_lineage_is_rejected(column: str) -> None:
    with pytest.raises(RoadProximityError, match="column|lineage"):
        _enrich(roads=_roads().drop(columns=column))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_eligible_class_requires_valid_geometry_status`

**Purpose:** Regression invariant: eligible class requires valid geometry status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_eligible_class_requires_valid_geometry_status(status: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("status", ["NULL", "EMPTY", "INVALID"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="VALID")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
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
| In-memory mutation | `roads.loc[0, "geometry_status"] = status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_eligible_class_requires_valid_geometry_status(status: str) -> None:
    roads = _roads()
    roads.loc[0, "geometry_status"] = status

    with pytest.raises(RoadProximityError, match="VALID"):
        _enrich(roads=roads)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_eligible_class_rejects_unsupported_geometry`

**Purpose:** Regression invariant: eligible class rejects unsupported geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_eligible_class_rejects_unsupported_geometry() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError, match="LineString\|geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `Point` | `shapely.geometry.Point` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
| In-memory mutation | `roads.at[0, "geometry"] = Point(20, 0)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_eligible_class_rejects_unsupported_geometry() -> None:
    roads = _roads()
    roads.at[0, "geometry"] = Point(20, 0)

    with pytest.raises(RoadProximityError, match="LineString|geometry"):
        _enrich(roads=roads)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_not_distance_road_is_counted_but_never_indexed`

**Purpose:** Regression invariant: not distance road is counted but never indexed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_not_distance_road_is_counted_but_never_indexed() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1`
  - `assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible`
  - `assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `roads["road_proxy_class"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
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
| In-memory mutation | `roads.loc[roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"] = (<br>        "INVALID"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_not_distance_road_is_counted_but_never_indexed() -> None:
    roads = _roads()
    roads.loc[roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"] = (
        "INVALID"
    )
    result = _enrich(roads=roads)
    coverage = {item.road_proxy_class: item for item in result.class_coverage}

    assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1
    assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible
    assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_known_polygon_to_line_distance_is_ten_metres`

**Purpose:** Regression invariant: known polygon to line distance is ten metres. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_known_polygon_to_line_distance_is_ten_metres() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row(<br>        result, "GENERAL_VEHICLE_PROXY"<br>    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
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
def test_known_polygon_to_line_distance_is_ten_metres() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_intersecting_or_touching_road_has_zero_distance`

**Purpose:** Regression invariant: intersecting or touching road has zero distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_intersecting_or_touching_road_has_zero_distance(x: float) -> None:
```

- Exact decorators: `pytest.mark.parametrize("x", [5.0, 10.0])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `x` | positional-or-keyword | `float` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row(<br>        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"<br>    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `_road_row` | `tests.unit.test_enrich_road_proximity._road_row` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `pytest.approx` | `pytest.approx` |
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
def test_intersecting_or_touching_road_has_zero_distance(x: float) -> None:
    roads = _roads([_road_row("GENERAL_VEHICLE_PROXY", x, identifier="ROAD-GENERAL")])

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_distance_uses_full_polygon_not_centroid`

**Purpose:** Regression invariant: distance uses full polygon not centroid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_distance_uses_full_polygon_not_centroid() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert distance == pytest.approx(10.0, abs=1e-5)`
  - `assert distance != pytest.approx(15.0, abs=1e-5)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
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
def test_distance_uses_full_polygon_not_centroid() -> None:
    distance = _row(_enrich(), "GENERAL_VEHICLE_PROXY").nearest_road_proxy_distance_m

    assert distance == pytest.approx(10.0, abs=1e-5)
    assert distance != pytest.approx(15.0, abs=1e-5)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_storage_geometry_stays_epsg4326_while_distance_is_metric`

**Purpose:** Regression invariant: storage geometry stays epsg4326 while distance is metric. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_storage_geometry_stays_epsg4326_while_distance_is_metric() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.crs == parcels.crs`
  - `assert result.parcels.crs.to_epsg() == 4326`
  - `assert _row(<br>        result, "GENERAL_VEHICLE_PROXY"<br>    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `deepcopy` | `copy.deepcopy` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `result.parcels.crs.to_epsg` | `unresolved local/third-party receiver; no ownership inferred` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `pytest.approx` | `pytest.approx` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

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
def test_storage_geometry_stays_epsg4326_while_distance_is_metric() -> None:
    parcels = _parcels()
    before = deepcopy(parcels)
    result = _enrich(parcels=parcels)

    assert result.parcels.crs == parcels.crs
    assert result.parcels.crs.to_epsg() == 4326
    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert_geodataframe_equal(result.parcels, before)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_each_eligible_class_has_independent_distance`

**Purpose:** Regression invariant: each eligible class has independent distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_each_eligible_class_has_independent_distance() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert distances == pytest.approx(<br>        {<br>            "GENERAL_VEHICLE_PROXY": 10.0,<br>            "LIMITED_VEHICLE_PROXY": 20.0,<br>            "RESTRICTED_REVIEW": 5.0,<br>            "NOT_GENERAL_VEHICLE_PROXY": 30.0,<br>            "UNKNOWN_REVIEW": 40.0,<br>        },<br>        abs=1e-5,<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
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
def test_each_eligible_class_has_independent_distance() -> None:
    result = _enrich()
    distances = {
        road_class: _row(result, road_class).nearest_road_proxy_distance_m
        for road_class in ELIGIBLE_CLASSES
    }

    assert distances == pytest.approx(
        {
            "GENERAL_VEHICLE_PROXY": 10.0,
            "LIMITED_VEHICLE_PROXY": 20.0,
            "RESTRICTED_REVIEW": 5.0,
            "NOT_GENERAL_VEHICLE_PROXY": 30.0,
            "UNKNOWN_REVIEW": 40.0,
        },
        abs=1e-5,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_near_not_distance_road_cannot_change_general_distance`

**Purpose:** Regression invariant: near not distance road cannot change general distance. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_near_not_distance_road_cannot_change_general_distance() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row(<br>        result, "GENERAL_VEHICLE_PROXY"<br>    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)`
  - `assert "ROAD-NOT-DISTANCE" not in set(<br>        result.class_proximity.nearest_road_feature_id.dropna()<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `pytest.approx` | `pytest.approx` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.class_proximity.nearest_road_feature_id.dropna` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_near_not_distance_road_cannot_change_general_distance() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert "ROAD-NOT-DISTANCE" not in set(
        result.class_proximity.nearest_road_feature_id.dropna()
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_single_nearest_road_has_tie_count_one`

**Purpose:** Regression invariant: single nearest road has tie count one. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_single_nearest_road_has_tie_count_one() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row(_enrich(), "GENERAL_VEHICLE_PROXY").nearest_road_tie_count == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
def test_single_nearest_road_has_tie_count_one() -> None:
    assert _row(_enrich(), "GENERAL_VEHICLE_PROXY").nearest_road_tie_count == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_tie_counts_two_and_lexical_id_wins`

**Purpose:** Regression invariant: exact tie counts two and lexical id wins. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_tie_counts_two_and_lexical_id_wins() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)`
  - `assert row.nearest_road_tie_count == 2`
  - `assert row.nearest_road_feature_id == "A-ROAD"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `_road_row` | `tests.unit.test_enrich_road_proximity._road_row` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
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
def test_exact_tie_counts_two_and_lexical_id_wins() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    row = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert row.nearest_road_tie_count == 2
    assert row.nearest_road_feature_id == "A-ROAD"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_tie_winner_is_independent_of_source_order`

**Purpose:** Regression invariant: tie winner is independent of source order. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_tie_winner_is_independent_of_source_order() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert forward.nearest_road_feature_id == "A-ROAD"`
  - `assert reverse.nearest_road_feature_id == "A-ROAD"`
  - `assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `_road_row` | `tests.unit.test_enrich_road_proximity._road_row` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `roads.iloc[::-1].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_tie_winner_is_independent_of_source_order() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    forward = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")
    reverse = _row(
        _enrich(roads=roads.iloc[::-1].reset_index(drop=True)),
        "GENERAL_VEHICLE_PROXY",
    )

    assert forward.nearest_road_feature_id == "A-ROAD"
    assert reverse.nearest_road_feature_id == "A-ROAD"
    assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unequal_distance_wins_regardless_of_identifier`

**Purpose:** Regression invariant: unequal distance wins regardless of identifier. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unequal_distance_wins_regardless_of_identifier() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY").nearest_road_feature_id<br>        == "Z-NEAR"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `_road_row` | `tests.unit.test_enrich_road_proximity._road_row` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
def test_unequal_distance_wins_regardless_of_identifier() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="Z-NEAR"),
            _road_row("GENERAL_VEHICLE_PROXY", 30, identifier="A-FAR"),
        ]
    )

    assert (
        _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY").nearest_road_feature_id
        == "Z-NEAR"
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_empty_eligible_class_emits_null_row_per_parcel`

**Purpose:** Regression invariant: empty eligible class emits null row per parcel. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_empty_eligible_class_emits_null_row_per_parcel() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(rows) == 2`
  - `assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()`
  - `assert coverage["UNKNOWN_REVIEW"].feature_count == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads()<br>        .loc[~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")]<br>        .reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `_roads()["road_proxy_class"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `result.class_proximity.road_proxy_class.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(SELECTED_COLUMNS)].isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(SELECTED_COLUMNS)].isna` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_empty_eligible_class_emits_null_row_per_parcel() -> None:
    roads = (
        _roads()
        .loc[~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")]
        .reset_index(drop=True)
    )
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    result = _enrich(parcels=parcels, roads=roads)
    rows = result.class_proximity.loc[
        result.class_proximity.road_proxy_class.eq("UNKNOWN_REVIEW")
    ]

    assert len(rows) == 2
    assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()
    coverage = {item.road_proxy_class: item for item in result.class_coverage}
    assert coverage["UNKNOWN_REVIEW"].feature_count == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_output_shape_columns_and_order_are_deterministic`

**Purpose:** Regression invariant: output shape columns and order are deterministic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_output_shape_columns_and_order_are_deterministic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.class_proximity) == len(parcels) * 5`
  - `assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)`
  - `assert result.class_proximity.parcel_id.tolist() == [<br>        value for parcel_id in ("SECOND", "FIRST") for value in [parcel_id] * 5<br>    ]`
  - `assert (<br>        result.class_proximity.road_proxy_class.tolist() == list(ELIGIBLE_CLASSES) * 2<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `Polygon` | `shapely.geometry.Polygon` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.class_proximity.parcel_id.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.class_proximity.road_proxy_class.tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_output_shape_columns_and_order_are_deterministic() -> None:
    parcels = _parcels(
        [
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    result = _enrich(parcels=parcels)

    assert len(result.class_proximity) == len(parcels) * 5
    assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)
    assert result.class_proximity.parcel_id.tolist() == [
        value for parcel_id in ("SECOND", "FIRST") for value in [parcel_id] * 5
    ]
    assert (
        result.class_proximity.road_proxy_class.tolist() == list(ELIGIBLE_CLASSES) * 2
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_class_coverage_is_complete_and_strict`

**Purpose:** Regression invariant: class coverage is complete and strict. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_class_coverage_is_complete_and_strict() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(item.road_proxy_class for item in result.class_coverage) == (<br>        ALL_CLASSES<br>    )`
  - `assert sum(item.feature_count for item in result.class_coverage) == 6`
  - `assert all(<br>        item.distance_eligible == (item.road_proxy_class != "NOT_DISTANCE_PROXY")<br>        for item in result.class_coverage<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_class_coverage_is_complete_and_strict() -> None:
    result = _enrich()

    assert tuple(item.road_proxy_class for item in result.class_coverage) == (
        ALL_CLASSES
    )
    assert sum(item.feature_count for item in result.class_coverage) == 6
    assert all(
        item.distance_eligible == (item.road_proxy_class != "NOT_DISTANCE_PROXY")
        for item in result.class_coverage
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_selected_road_evidence_and_lineage_are_exact`

**Purpose:** Regression invariant: selected road evidence and lineage are exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_selected_road_evidence_and_lineage_are_exact() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.nearest_road_feature_id == "ROAD-GENERAL"`
  - `assert row.nearest_source_feature_id == "SOURCE-ROAD-GENERAL"`
  - `assert row.nearest_road_primary_rule == "OPEN_OR_TOLL"`
  - `assert row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'`
  - `assert row.nearest_road_unknown_fields_json == "[]"`
  - `assert not row.nearest_road_toll_evidence`
  - `assert row.nearest_source_archive_sha256 == "a" * 64`
  - `assert row.road_proxy_policy_id == policy.policy_id`
  - `assert row.road_proxy_policy_schema_version == policy.schema_version`
  - `assert row.road_proxy_policy_config_sha256 == policy.config_sha256`
  - `assert row.road_proxy_heavy_vehicle_access == "NOT_PROVEN"`
  - `assert row.proximity_scope == "WITHIN_VERIFIED_SOURCE_PACKAGE"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `_row` | `tests.unit.test_enrich_road_proximity._row` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
def test_selected_road_evidence_and_lineage_are_exact() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    row = _row(_enrich(), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_feature_id == "ROAD-GENERAL"
    assert row.nearest_source_feature_id == "SOURCE-ROAD-GENERAL"
    assert row.nearest_road_primary_rule == "OPEN_OR_TOLL"
    assert row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'
    assert row.nearest_road_unknown_fields_json == "[]"
    assert not row.nearest_road_toll_evidence
    assert row.nearest_source_archive_sha256 == "a" * 64
    assert row.road_proxy_policy_id == policy.policy_id
    assert row.road_proxy_policy_schema_version == policy.schema_version
    assert row.road_proxy_policy_config_sha256 == policy.config_sha256
    assert row.road_proxy_heavy_vehicle_access == "NOT_PROVEN"
    assert row.proximity_scope == "WITHIN_VERIFIED_SOURCE_PACKAGE"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcels_and_road_application_are_not_mutated`

**Purpose:** Regression invariant: parcels and road application are not mutated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcels_and_road_application_are_not_mutated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.index.equals(parcels.index)`
  - `assert list(result.parcels.columns) == list(parcels.columns)`
  - `assert result.parcels.dtypes.equals(parcels.dtypes)`
  - `assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `deepcopy` | `copy.deepcopy` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `result.parcels.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.dtypes.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.geometry.to_wkb().equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels.geometry.to_wkb().equals`<br>`result.parcels.geometry.to_wkb`<br>`parcels.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_parcels_and_road_application_are_not_mutated() -> None:
    parcels = _parcels(index=[777])
    roads = _roads()
    parcels_before = deepcopy(parcels)
    roads_before = deepcopy(roads)
    result = _enrich(parcels=parcels, roads=roads)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(roads, roads_before)
    assert_geodataframe_equal(result.parcels, parcels_before)
    assert result.parcels.index.equals(parcels.index)
    assert list(result.parcels.columns) == list(parcels.columns)
    assert result.parcels.dtypes.equals(parcels.dtypes)
    assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_corrupt_nearest_output`

**Purpose:** Implements `corrupt nearest output` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def _corrupt_nearest_output(column: str, value: object) -> None:
```

- Exact decorators: none.
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
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_enrich_road_proximity::test_malformed_produced_distance_is_rejected` via `_corrupt_nearest_output`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_malformed_produced_distance_is_rejected` via `_corrupt_nearest_output`
- direct call: `tests.unit.test_enrich_road_proximity::test_malformed_produced_tie_count_is_rejected` via `_corrupt_nearest_output`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_malformed_produced_tie_count_is_rejected` via `_corrupt_nearest_output`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch.object` | `unittest.mock.patch.object` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
def _corrupt_nearest_output(column: str, value: object) -> None:
    import landscout.stages.enrich_road_proximity as module

    original = module._nearest_class_rows

    def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        if output["distance_m"].notna().any():
            output[column] = output[column].astype("object")
            output.at[0, column] = value
        return output

    with (
        patch.object(module, "_nearest_class_rows", side_effect=corrupted),
        pytest.raises(RoadProximityError),
    ):
        _enrich()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_corrupt_nearest_output.corrupted`

**Purpose:** Implements `corrupted` within the file role: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

**Exact signature**

```python
def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
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
| `output["distance_m"].notna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["distance_m"].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `output[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `output["distance_m"].notna().any`<br>`output["distance_m"].notna` |
| External process/environment | None directly present. |
| In-memory mutation | `output[column] = output[column].astype("object")`<br>`output.at[0, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        if output["distance_m"].notna().any():
            output[column] = output[column].astype("object")
            output.at[0, column] = value
        return output
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_produced_distance_is_rejected`

**Purpose:** Regression invariant: malformed produced distance is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_produced_distance_is_rejected(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [-1.0, float("nan"), float("inf")])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
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
| `_corrupt_nearest_output` | `tests.unit.test_enrich_road_proximity._corrupt_nearest_output` |
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
def test_malformed_produced_distance_is_rejected(value: object) -> None:
    _corrupt_nearest_output("distance_m", value)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_produced_tie_count_is_rejected`

**Purpose:** Regression invariant: malformed produced tie count is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_produced_tie_count_is_rejected(value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("value", [0, -1, True, 1.5])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
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
| `_corrupt_nearest_output` | `tests.unit.test_enrich_road_proximity._corrupt_nearest_output` |
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
def test_malformed_produced_tie_count_is_rejected(value: object) -> None:
    _corrupt_nearest_output("tie_count", value)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_dataclasses_are_frozen`

**Purpose:** Regression invariant: result dataclasses are frozen. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_dataclasses_are_frozen() -> None:
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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `pytest.raises` | `pytest.raises` |
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |

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
| In-memory mutation | `result.parcels = _parcels()`<br>`coverage.feature_count = 99` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_result_dataclasses_are_frozen() -> None:
    result = _enrich()
    coverage = result.class_coverage[0]

    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        coverage.feature_count = 99
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_business_decision_columns_or_implementation_exist`

**Purpose:** Regression invariant: no business decision columns or implementation exist. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_business_decision_columns_or_implementation_exist() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert forbidden.isdisjoint(result.parcels.columns)`
  - `assert forbidden.isdisjoint(result.class_proximity.columns)`
  - `assert ".iterrows(" not in source`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `forbidden.isdisjoint` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path("src/landscout/stages/enrich_road_proximity.py").read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path("src/landscout/stages/enrich_road_proximity.py").read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `forbidden.isdisjoint` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_no_business_decision_columns_or_implementation_exist() -> None:
    result = _enrich()
    forbidden = {
        "access_score",
        "bess_score",
        "accessible",
        "legal_access",
        "parcel_status",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)

    source = Path("src/landscout/stages/enrich_road_proximity.py").read_text(
        encoding="utf-8"
    )
    assert ".iterrows(" not in source
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_parcel_frame_is_an_independent_copy`

**Purpose:** Regression invariant: result parcel frame is an independent copy. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_parcel_frame_is_an_independent_copy() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcels.iloc[0].source_value == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |

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
| In-memory mutation | `result.parcels.loc[result.parcels.index[0], "source_value"] = 999` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_result_parcel_frame_is_an_independent_copy() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)
    result.parcels.loc[result.parcels.index[0], "source_value"] = 999

    assert parcels.iloc[0].source_value == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_class_proximity_is_plain_dataframe`

**Purpose:** Regression invariant: class proximity is plain dataframe. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_class_proximity_is_plain_dataframe() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert type(result.class_proximity) is pd.DataFrame`
  - `assert not isinstance(result.class_proximity, gpd.GeoDataFrame)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_class_proximity_is_plain_dataframe() -> None:
    result = _enrich()

    assert type(result.class_proximity) is pd.DataFrame
    assert not isinstance(result.class_proximity, gpd.GeoDataFrame)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_selected_rows_belong_to_requested_class`

**Purpose:** Regression invariant: selected rows belong to requested class. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_selected_rows_belong_to_requested_class() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert all(<br>        road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class<br>        for row in selected.itertuples(index=False)<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `_roads().set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `result.class_proximity.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected.itertuples` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_selected_rows_belong_to_requested_class() -> None:
    result = _enrich()
    road_classes = _roads().set_index("road_feature_id")["road_proxy_class"]
    selected = result.class_proximity.dropna(subset=["nearest_road_feature_id"])

    assert all(
        road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class
        for row in selected.itertuples(index=False)
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_sha_mismatch_does_not_construct_spatial_index`

**Purpose:** Regression invariant: policy sha mismatch does not construct spatial index. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_sha_mismatch_does_not_construct_spatial_index() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(RoadProximityError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_enrich_road_proximity._roads` |
| `patch` | `unittest.mock.patch` |
| `pytest.raises` | `pytest.raises` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `spatial_index.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `roads["road_proxy_policy_config_sha256"] = "b" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_sha_mismatch_does_not_construct_spatial_index() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with (
        patch("landscout.stages.enrich_road_proximity.STRtree") as spatial_index,
        pytest.raises(RoadProximityError),
    ):
        _enrich(roads=roads)

    spatial_index.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_matched_output_dtypes_are_stable`

**Purpose:** Regression invariant: matched output dtypes are stable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_matched_output_dtypes_are_stable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"`
  - `assert str(table.nearest_road_tie_count.dtype) == "Int64"`
  - `assert str(table.nearest_road_toll_evidence.dtype) == "boolean"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_matched_output_dtypes_are_stable() -> None:
    result = _enrich()
    table = result.class_proximity

    assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"
    assert str(table.nearest_road_tie_count.dtype) == "Int64"
    assert str(table.nearest_road_toll_evidence.dtype) == "boolean"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_preservation_uses_exact_non_geometry_values`

**Purpose:** Regression invariant: parcel preservation uses exact non geometry values. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_preservation_uses_exact_non_geometry_values() -> None:
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
| `_parcels` | `tests.unit.test_enrich_road_proximity._parcels` |
| `_enrich` | `tests.unit.test_enrich_road_proximity._enrich` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `result.parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `result.parcels.drop(columns="geometry")`<br>`parcels.drop(columns="geometry")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_parcel_preservation_uses_exact_non_geometry_values() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)

    assert_frame_equal(
        pd.DataFrame(result.parcels.drop(columns="geometry")),
        pd.DataFrame(parcels.drop(columns="geometry")),
        check_dtype=True,
        check_index_type=True,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **50**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_public_api_exports_only_stable_symbols` | none | none | 4 | Proves public api exports only stable symbols using the exact source reproduced in section 7. |
| `test_wrong_parcel_type_has_controlled_error` | none | pytest.raises(RoadProximityError) | 0 | Proves wrong parcel type has controlled error using the exact source reproduced in section 7. |
| `test_wrong_road_source_type_has_controlled_error` | none | pytest.raises(RoadProximityError) | 0 | Proves wrong road source type has controlled error using the exact source reproduced in section 7. |
| `test_wrong_source_config_type_has_controlled_error` | none | pytest.raises(RoadProximityError) | 0 | Proves wrong source config type has controlled error using the exact source reproduced in section 7. |
| `test_wrong_policy_path_type_has_controlled_error` | none | pytest.raises(RoadProximityError) | 0 | Proves wrong policy path type has controlled error using the exact source reproduced in section 7. |
| `test_application_stage_is_invoked_exactly_once` | none | none | 0 | Proves application stage is invoked exactly once using the exact source reproduced in section 7. |
| `test_application_failure_stops_proximity` | none | pytest.raises(RoadProximityError) | 0 | Proves application failure stops proximity using the exact source reproduced in section 7. |
| `test_malformed_policy_stops_before_application` | none | pytest.raises(RoadProximityError) | 0 | Proves malformed policy stops before application using the exact source reproduced in section 7. |
| `test_independent_policy_sha_mismatch_is_rejected` | none | pytest.raises(RoadProximityError, match="policy\|SHA\|lineage") | 0 | Proves independent policy sha mismatch is rejected using the exact source reproduced in section 7. |
| `test_invalid_parcel_identity_is_rejected` | pytest.mark.parametrize(<br>    ("mutation", "message"),<br>    [<br>        (lambda frame: frame.drop(columns="parcel_id"), "parcel_id"),<br>        (lambda frame: frame.assign(parcel_id=None), "parcel_id"),<br>        (lambda frame: frame.assign(parcel_id=123), "parcel_id"),<br>        (lambda frame: frame.assign(parcel_id=""), "parcel_id"),<br>        (lambda frame: frame.assign(parcel_id=" BAD "), "parcel_id"),<br>    ],<br>) | pytest.raises(RoadProximityError, match=message) | 0 | Proves invalid parcel identity is rejected using the exact source reproduced in section 7. |
| `test_duplicate_parcel_id_is_rejected` | none | pytest.raises(RoadProximityError, match="unique") | 0 | Proves duplicate parcel id is rejected using the exact source reproduced in section 7. |
| `test_duplicate_parcel_columns_are_rejected` | none | pytest.raises(RoadProximityError, match="duplicate") | 0 | Proves duplicate parcel columns are rejected using the exact source reproduced in section 7. |
| `test_missing_or_inactive_geometry_is_rejected` | none | pytest.raises(RoadProximityError, match="geometry"); pytest.raises(RoadProximityError, match="active") | 0 | Proves missing or inactive geometry is rejected using the exact source reproduced in section 7. |
| `test_missing_or_wrong_storage_crs_is_rejected` | none | pytest.raises(RoadProximityError, match="CRS"); pytest.raises(RoadProximityError, match="4326") | 0 | Proves missing or wrong storage crs is rejected using the exact source reproduced in section 7. |
| `test_wrong_parcel_geometry_kind_is_rejected` | pytest.mark.parametrize(<br>    "geometry",<br>    [Point(0, 0), LineString([(0, 0), (10, 10)])],<br>) | pytest.raises(RoadProximityError, match="Polygon\|MultiPolygon") | 0 | Proves wrong parcel geometry kind is rejected using the exact source reproduced in section 7. |
| `test_bad_parcel_geometry_is_rejected` | pytest.mark.parametrize(<br>    ("geometry", "message"),<br>    [<br>        (None, "null"),<br>        (Polygon(), "empty"),<br>        (<br>            Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)]),<br>            "valid",<br>        ),<br>    ],<br>) | pytest.raises(RoadProximityError, match=message) | 0 | Proves bad parcel geometry is rejected using the exact source reproduced in section 7. |
| `test_polygon_and_multipolygon_are_accepted` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),<br>        MultiPolygon([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]),<br>    ],<br>) | none | 1 | Proves polygon and multipolygon are accepted using the exact source reproduced in section 7. |
| `test_wrong_application_result_type_is_rejected` | none | pytest.raises(RoadProximityError) | 0 | Proves wrong application result type is rejected using the exact source reproduced in section 7. |
| `test_application_roads_must_be_geodataframe` | none | pytest.raises(RoadProximityError) | 0 | Proves application roads must be geodataframe using the exact source reproduced in section 7. |
| `test_duplicate_road_feature_id_is_rejected` | none | pytest.raises(RoadProximityError, match="unique") | 0 | Proves duplicate road feature id is rejected using the exact source reproduced in section 7. |
| `test_unknown_road_proxy_class_is_rejected` | none | pytest.raises(RoadProximityError, match="class") | 0 | Proves unknown road proxy class is rejected using the exact source reproduced in section 7. |
| `test_missing_road_policy_lineage_is_rejected` | pytest.mark.parametrize(<br>    "column",<br>    [<br>        "road_proxy_policy_id",<br>        "road_proxy_policy_schema_version",<br>        "road_proxy_policy_config_sha256",<br>        "road_proxy_heavy_vehicle_access",<br>    ],<br>) | pytest.raises(RoadProximityError, match="column\|lineage") | 0 | Proves missing road policy lineage is rejected using the exact source reproduced in section 7. |
| `test_eligible_class_requires_valid_geometry_status` | pytest.mark.parametrize("status", ["NULL", "EMPTY", "INVALID"]) | pytest.raises(RoadProximityError, match="VALID") | 0 | Proves eligible class requires valid geometry status using the exact source reproduced in section 7. |
| `test_eligible_class_rejects_unsupported_geometry` | none | pytest.raises(RoadProximityError, match="LineString\|geometry") | 0 | Proves eligible class rejects unsupported geometry using the exact source reproduced in section 7. |
| `test_not_distance_road_is_counted_but_never_indexed` | none | none | 3 | Proves not distance road is counted but never indexed using the exact source reproduced in section 7. |
| `test_known_polygon_to_line_distance_is_ten_metres` | none | none | 1 | Proves known polygon to line distance is ten metres using the exact source reproduced in section 7. |
| `test_intersecting_or_touching_road_has_zero_distance` | pytest.mark.parametrize("x", [5.0, 10.0]) | none | 1 | Proves intersecting or touching road has zero distance using the exact source reproduced in section 7. |
| `test_distance_uses_full_polygon_not_centroid` | none | none | 2 | Proves distance uses full polygon not centroid using the exact source reproduced in section 7. |
| `test_storage_geometry_stays_epsg4326_while_distance_is_metric` | none | none | 3 | Proves storage geometry stays epsg4326 while distance is metric using the exact source reproduced in section 7. |
| `test_each_eligible_class_has_independent_distance` | none | none | 1 | Proves each eligible class has independent distance using the exact source reproduced in section 7. |
| `test_near_not_distance_road_cannot_change_general_distance` | none | none | 2 | Proves near not distance road cannot change general distance using the exact source reproduced in section 7. |
| `test_single_nearest_road_has_tie_count_one` | none | none | 1 | Proves single nearest road has tie count one using the exact source reproduced in section 7. |
| `test_exact_tie_counts_two_and_lexical_id_wins` | none | none | 3 | Proves exact tie counts two and lexical id wins using the exact source reproduced in section 7. |
| `test_tie_winner_is_independent_of_source_order` | none | none | 3 | Proves tie winner is independent of source order using the exact source reproduced in section 7. |
| `test_unequal_distance_wins_regardless_of_identifier` | none | none | 1 | Proves unequal distance wins regardless of identifier using the exact source reproduced in section 7. |
| `test_empty_eligible_class_emits_null_row_per_parcel` | none | none | 3 | Proves empty eligible class emits null row per parcel using the exact source reproduced in section 7. |
| `test_output_shape_columns_and_order_are_deterministic` | none | none | 4 | Proves output shape columns and order are deterministic using the exact source reproduced in section 7. |
| `test_class_coverage_is_complete_and_strict` | none | none | 3 | Proves class coverage is complete and strict using the exact source reproduced in section 7. |
| `test_selected_road_evidence_and_lineage_are_exact` | none | none | 12 | Proves selected road evidence and lineage are exact using the exact source reproduced in section 7. |
| `test_parcels_and_road_application_are_not_mutated` | none | none | 4 | Proves parcels and road application are not mutated using the exact source reproduced in section 7. |
| `test_malformed_produced_distance_is_rejected` | pytest.mark.parametrize("value", [-1.0, float("nan"), float("inf")]) | none | 0 | Proves malformed produced distance is rejected using the exact source reproduced in section 7. |
| `test_malformed_produced_tie_count_is_rejected` | pytest.mark.parametrize("value", [0, -1, True, 1.5]) | none | 0 | Proves malformed produced tie count is rejected using the exact source reproduced in section 7. |
| `test_result_dataclasses_are_frozen` | none | pytest.raises(FrozenInstanceError); pytest.raises(FrozenInstanceError) | 0 | Proves result dataclasses are frozen using the exact source reproduced in section 7. |
| `test_no_business_decision_columns_or_implementation_exist` | none | none | 3 | Proves no business decision columns or implementation exist using the exact source reproduced in section 7. |
| `test_result_parcel_frame_is_an_independent_copy` | none | none | 1 | Proves result parcel frame is an independent copy using the exact source reproduced in section 7. |
| `test_class_proximity_is_plain_dataframe` | none | none | 2 | Proves class proximity is plain dataframe using the exact source reproduced in section 7. |
| `test_selected_rows_belong_to_requested_class` | none | none | 1 | Proves selected rows belong to requested class using the exact source reproduced in section 7. |
| `test_policy_sha_mismatch_does_not_construct_spatial_index` | none | pytest.raises(RoadProximityError) | 0 | Proves policy sha mismatch does not construct spatial index using the exact source reproduced in section 7. |
| `test_matched_output_dtypes_are_stable` | none | none | 3 | Proves matched output dtypes are stable using the exact source reproduced in section 7. |
| `test_parcel_preservation_uses_exact_non_geometry_values` | none | none | 0 | Proves parcel preservation uses exact non geometry values using the exact source reproduced in section 7. |

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
from dataclasses import FrozenInstanceError
from pathlib import Path
from typing import Any, cast
from unittest.mock import patch

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely.geometry import LineString, MultiPolygon, Point, Polygon

from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    load_ign_bdtopo_source_config,
)
from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
)
from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)
from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)

SOURCE_CONFIG = load_ign_bdtopo_source_config()
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
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


def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]
    count = len(values)
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(count)]
    frame_index = index or [100 + position for position in range(count)]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "source_value": list(range(count))},
        geometry=values,
        crs="EPSG:2154",
        index=frame_index,
    )


def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(geometries, identifiers=identifiers, index=index).to_crs(
        "EPSG:4326"
    )


def _road_row(
    road_class: str,
    x: float,
    *,
    identifier: str,
    geometry: object | None = None,
) -> dict[str, object]:
    policy = load_ign_road_vehicle_proxy_policy()
    primary_rule = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "NOT_DISTANCE_PROXY": "FICTITIOUS_GEOMETRY",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }[road_class]
    return {
        "road_feature_id": identifier,
        "source_feature_id": f"SOURCE-{identifier}",
        "geometry_status": "VALID",
        "nature_raw": "Route à 1 chaussée",
        "importance_raw": "2",
        "asset_status_raw": "En service",
        "private_raw": 0.0,
        "light_vehicle_access_raw": "Libre",
        "carriageway_width_raw": 7.0,
        "closure_period_raw": None,
        "restriction_nature_raw": None,
        "source_layer": "troncon_de_route",
        "source_department_code": "31",
        "source_edition": "2026-06-15",
        "source_archive_sha256": "a" * 64,
        "road_proxy_primary_rule": primary_rule,
        "road_proxy_class": road_class,
        "road_proxy_rule_trace_json": f'["{primary_rule}"]',
        "road_proxy_unknown_fields_json": "[]",
        "road_proxy_toll_evidence": False,
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_policy_scope": policy.scope,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "geometry": geometry or LineString([(x, -20), (x, 30)]),
    }


def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
    values = rows or [
        _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="ROAD-GENERAL"),
        _road_row("LIMITED_VEHICLE_PROXY", 30, identifier="ROAD-LIMITED"),
        _road_row("RESTRICTED_REVIEW", 15, identifier="ROAD-RESTRICTED"),
        _road_row("NOT_GENERAL_VEHICLE_PROXY", 40, identifier="ROAD-NOT-GENERAL"),
        _road_row("NOT_DISTANCE_PROXY", 11, identifier="ROAD-NOT-DISTANCE"),
        _road_row("UNKNOWN_REVIEW", 50, identifier="ROAD-UNKNOWN"),
    ]
    return gpd.GeoDataFrame(values, geometry="geometry", crs="EPSG:2154")


def _source() -> IgnBdTopoRoadData:
    return IgnBdTopoRoadData(
        extraction=cast(Any, None),
        road_segments=_roads(),
        road_segments_summary=cast(Any, None),
    )


def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
    application = IgnRoadVehicleProxyApplicationResult(
        roads if roads is not None else _roads()
    )
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ):
        return enrich_parcel_road_proximity(
            parcels if parcels is not None else _parcels(),
            _source(),
            SOURCE_CONFIG,
            policy_path,
        )


def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]


def test_public_api_exports_only_stable_symbols() -> None:
    import landscout.stages.enrich_road_proximity as module

    expected = {
        "RoadProximityError",
        "RoadProxyClassCoverage",
        "ParcelRoadProximityResult",
        "enrich_parcel_road_proximity",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_nearest_class_rows")


def test_wrong_parcel_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG
        )


def test_wrong_road_source_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), cast(Any, object()), SOURCE_CONFIG)


def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), cast(Any, object()))


def test_wrong_policy_path_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), SOURCE_CONFIG, cast(Any, "policy.yaml")
        )


def test_application_stage_is_invoked_exactly_once() -> None:
    application = IgnRoadVehicleProxyApplicationResult(_roads())
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ) as source_application:
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    source_application.assert_called_once()


def test_application_failure_stops_proximity() -> None:
    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
            side_effect=IgnRoadVehicleProxyApplicationError("bad source"),
        ),
        patch("landscout.stages.enrich_road_proximity.STRtree") as spatial_index,
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    spatial_index.assert_not_called()


def test_malformed_policy_stops_before_application(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy"
        ) as source_application,
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)

    source_application.assert_not_called()


def test_independent_policy_sha_mismatch_is_rejected() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with pytest.raises(RoadProximityError, match="policy|SHA|lineage"):
        _enrich(roads=roads)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda frame: frame.drop(columns="parcel_id"), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=None), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=123), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=""), "parcel_id"),
        (lambda frame: frame.assign(parcel_id=" BAD "), "parcel_id"),
    ],
)
def test_invalid_parcel_identity_is_rejected(mutation: Any, message: str) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=mutation(_parcels()))


def test_duplicate_parcel_id_is_rejected() -> None:
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(parcels=parcels)


def test_duplicate_parcel_columns_are_rejected() -> None:
    parcels = _parcels()
    duplicated = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )

    with pytest.raises(RoadProximityError, match="duplicate"):
        _enrich(parcels=duplicated)


def test_missing_or_inactive_geometry_is_rejected() -> None:
    parcels = _parcels()
    missing = parcels.drop(columns="geometry")
    inactive = parcels.assign(other_geometry=parcels.geometry).set_geometry(
        "other_geometry"
    )

    with pytest.raises(RoadProximityError, match="geometry"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="active"):
        _enrich(parcels=inactive)


def test_missing_or_wrong_storage_crs_is_rejected() -> None:
    missing = _parcels().set_crs(None, allow_override=True)
    wrong = _metric_parcels()

    with pytest.raises(RoadProximityError, match="CRS"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="4326"):
        _enrich(parcels=wrong)


@pytest.mark.parametrize(
    "geometry",
    [Point(0, 0), LineString([(0, 0), (10, 10)])],
)
def test_wrong_parcel_geometry_kind_is_rejected(geometry: object) -> None:
    with pytest.raises(RoadProximityError, match="Polygon|MultiPolygon"):
        _enrich(parcels=_parcels([geometry]))


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
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=_parcels([geometry]))


@pytest.mark.parametrize(
    "geometry",
    [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        MultiPolygon([Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])]),
    ],
)
def test_polygon_and_multipolygon_are_accepted(geometry: object) -> None:
    assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1


def test_wrong_application_result_type_is_rejected() -> None:
    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
            return_value=object(),
        ),
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)


def test_application_roads_must_be_geodataframe() -> None:
    application = IgnRoadVehicleProxyApplicationResult(
        cast(Any, pd.DataFrame(_roads().drop(columns="geometry")))
    )
    with (
        patch(
            "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
            return_value=application,
        ),
        pytest.raises(RoadProximityError),
    ):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)


def test_duplicate_road_feature_id_is_rejected() -> None:
    roads = _roads()
    roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(roads=roads)


def test_unknown_road_proxy_class_is_rejected() -> None:
    roads = _roads()
    roads.loc[0, "road_proxy_class"] = "INVENTED"

    with pytest.raises(RoadProximityError, match="class"):
        _enrich(roads=roads)


@pytest.mark.parametrize(
    "column",
    [
        "road_proxy_policy_id",
        "road_proxy_policy_schema_version",
        "road_proxy_policy_config_sha256",
        "road_proxy_heavy_vehicle_access",
    ],
)
def test_missing_road_policy_lineage_is_rejected(column: str) -> None:
    with pytest.raises(RoadProximityError, match="column|lineage"):
        _enrich(roads=_roads().drop(columns=column))


@pytest.mark.parametrize("status", ["NULL", "EMPTY", "INVALID"])
def test_eligible_class_requires_valid_geometry_status(status: str) -> None:
    roads = _roads()
    roads.loc[0, "geometry_status"] = status

    with pytest.raises(RoadProximityError, match="VALID"):
        _enrich(roads=roads)


def test_eligible_class_rejects_unsupported_geometry() -> None:
    roads = _roads()
    roads.at[0, "geometry"] = Point(20, 0)

    with pytest.raises(RoadProximityError, match="LineString|geometry"):
        _enrich(roads=roads)


def test_not_distance_road_is_counted_but_never_indexed() -> None:
    roads = _roads()
    roads.loc[roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"] = (
        "INVALID"
    )
    result = _enrich(roads=roads)
    coverage = {item.road_proxy_class: item for item in result.class_coverage}

    assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1
    assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible
    assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)


def test_known_polygon_to_line_distance_is_ten_metres() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)


@pytest.mark.parametrize("x", [5.0, 10.0])
def test_intersecting_or_touching_road_has_zero_distance(x: float) -> None:
    roads = _roads([_road_row("GENERAL_VEHICLE_PROXY", x, identifier="ROAD-GENERAL")])

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)


def test_distance_uses_full_polygon_not_centroid() -> None:
    distance = _row(_enrich(), "GENERAL_VEHICLE_PROXY").nearest_road_proxy_distance_m

    assert distance == pytest.approx(10.0, abs=1e-5)
    assert distance != pytest.approx(15.0, abs=1e-5)


def test_storage_geometry_stays_epsg4326_while_distance_is_metric() -> None:
    parcels = _parcels()
    before = deepcopy(parcels)
    result = _enrich(parcels=parcels)

    assert result.parcels.crs == parcels.crs
    assert result.parcels.crs.to_epsg() == 4326
    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert_geodataframe_equal(result.parcels, before)


def test_each_eligible_class_has_independent_distance() -> None:
    result = _enrich()
    distances = {
        road_class: _row(result, road_class).nearest_road_proxy_distance_m
        for road_class in ELIGIBLE_CLASSES
    }

    assert distances == pytest.approx(
        {
            "GENERAL_VEHICLE_PROXY": 10.0,
            "LIMITED_VEHICLE_PROXY": 20.0,
            "RESTRICTED_REVIEW": 5.0,
            "NOT_GENERAL_VEHICLE_PROXY": 30.0,
            "UNKNOWN_REVIEW": 40.0,
        },
        abs=1e-5,
    )


def test_near_not_distance_road_cannot_change_general_distance() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert "ROAD-NOT-DISTANCE" not in set(
        result.class_proximity.nearest_road_feature_id.dropna()
    )


def test_single_nearest_road_has_tie_count_one() -> None:
    assert _row(_enrich(), "GENERAL_VEHICLE_PROXY").nearest_road_tie_count == 1


def test_exact_tie_counts_two_and_lexical_id_wins() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    row = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
    assert row.nearest_road_tie_count == 2
    assert row.nearest_road_feature_id == "A-ROAD"


def test_tie_winner_is_independent_of_source_order() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
    forward = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")
    reverse = _row(
        _enrich(roads=roads.iloc[::-1].reset_index(drop=True)),
        "GENERAL_VEHICLE_PROXY",
    )

    assert forward.nearest_road_feature_id == "A-ROAD"
    assert reverse.nearest_road_feature_id == "A-ROAD"
    assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2


def test_unequal_distance_wins_regardless_of_identifier() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="Z-NEAR"),
            _road_row("GENERAL_VEHICLE_PROXY", 30, identifier="A-FAR"),
        ]
    )

    assert (
        _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY").nearest_road_feature_id
        == "Z-NEAR"
    )


def test_empty_eligible_class_emits_null_row_per_parcel() -> None:
    roads = (
        _roads()
        .loc[~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")]
        .reset_index(drop=True)
    )
    parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
        ]
    )
    result = _enrich(parcels=parcels, roads=roads)
    rows = result.class_proximity.loc[
        result.class_proximity.road_proxy_class.eq("UNKNOWN_REVIEW")
    ]

    assert len(rows) == 2
    assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()
    coverage = {item.road_proxy_class: item for item in result.class_coverage}
    assert coverage["UNKNOWN_REVIEW"].feature_count == 0


def test_output_shape_columns_and_order_are_deterministic() -> None:
    parcels = _parcels(
        [
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    result = _enrich(parcels=parcels)

    assert len(result.class_proximity) == len(parcels) * 5
    assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)
    assert result.class_proximity.parcel_id.tolist() == [
        value for parcel_id in ("SECOND", "FIRST") for value in [parcel_id] * 5
    ]
    assert (
        result.class_proximity.road_proxy_class.tolist() == list(ELIGIBLE_CLASSES) * 2
    )


def test_class_coverage_is_complete_and_strict() -> None:
    result = _enrich()

    assert tuple(item.road_proxy_class for item in result.class_coverage) == (
        ALL_CLASSES
    )
    assert sum(item.feature_count for item in result.class_coverage) == 6
    assert all(
        item.distance_eligible == (item.road_proxy_class != "NOT_DISTANCE_PROXY")
        for item in result.class_coverage
    )


def test_selected_road_evidence_and_lineage_are_exact() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    row = _row(_enrich(), "GENERAL_VEHICLE_PROXY")

    assert row.nearest_road_feature_id == "ROAD-GENERAL"
    assert row.nearest_source_feature_id == "SOURCE-ROAD-GENERAL"
    assert row.nearest_road_primary_rule == "OPEN_OR_TOLL"
    assert row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'
    assert row.nearest_road_unknown_fields_json == "[]"
    assert not row.nearest_road_toll_evidence
    assert row.nearest_source_archive_sha256 == "a" * 64
    assert row.road_proxy_policy_id == policy.policy_id
    assert row.road_proxy_policy_schema_version == policy.schema_version
    assert row.road_proxy_policy_config_sha256 == policy.config_sha256
    assert row.road_proxy_heavy_vehicle_access == "NOT_PROVEN"
    assert row.proximity_scope == "WITHIN_VERIFIED_SOURCE_PACKAGE"


def test_parcels_and_road_application_are_not_mutated() -> None:
    parcels = _parcels(index=[777])
    roads = _roads()
    parcels_before = deepcopy(parcels)
    roads_before = deepcopy(roads)
    result = _enrich(parcels=parcels, roads=roads)

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(roads, roads_before)
    assert_geodataframe_equal(result.parcels, parcels_before)
    assert result.parcels.index.equals(parcels.index)
    assert list(result.parcels.columns) == list(parcels.columns)
    assert result.parcels.dtypes.equals(parcels.dtypes)
    assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())


def _corrupt_nearest_output(column: str, value: object) -> None:
    import landscout.stages.enrich_road_proximity as module

    original = module._nearest_class_rows

    def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        if output["distance_m"].notna().any():
            output[column] = output[column].astype("object")
            output.at[0, column] = value
        return output

    with (
        patch.object(module, "_nearest_class_rows", side_effect=corrupted),
        pytest.raises(RoadProximityError),
    ):
        _enrich()


@pytest.mark.parametrize("value", [-1.0, float("nan"), float("inf")])
def test_malformed_produced_distance_is_rejected(value: object) -> None:
    _corrupt_nearest_output("distance_m", value)


@pytest.mark.parametrize("value", [0, -1, True, 1.5])
def test_malformed_produced_tie_count_is_rejected(value: object) -> None:
    _corrupt_nearest_output("tie_count", value)


def test_result_dataclasses_are_frozen() -> None:
    result = _enrich()
    coverage = result.class_coverage[0]

    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        coverage.feature_count = 99  # type: ignore[misc]


def test_no_business_decision_columns_or_implementation_exist() -> None:
    result = _enrich()
    forbidden = {
        "access_score",
        "bess_score",
        "accessible",
        "legal_access",
        "parcel_status",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)

    source = Path("src/landscout/stages/enrich_road_proximity.py").read_text(
        encoding="utf-8"
    )
    assert ".iterrows(" not in source


def test_result_parcel_frame_is_an_independent_copy() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)
    result.parcels.loc[result.parcels.index[0], "source_value"] = 999

    assert parcels.iloc[0].source_value == 0


def test_class_proximity_is_plain_dataframe() -> None:
    result = _enrich()

    assert type(result.class_proximity) is pd.DataFrame
    assert not isinstance(result.class_proximity, gpd.GeoDataFrame)


def test_selected_rows_belong_to_requested_class() -> None:
    result = _enrich()
    road_classes = _roads().set_index("road_feature_id")["road_proxy_class"]
    selected = result.class_proximity.dropna(subset=["nearest_road_feature_id"])

    assert all(
        road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class
        for row in selected.itertuples(index=False)
    )


def test_policy_sha_mismatch_does_not_construct_spatial_index() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with (
        patch("landscout.stages.enrich_road_proximity.STRtree") as spatial_index,
        pytest.raises(RoadProximityError),
    ):
        _enrich(roads=roads)

    spatial_index.assert_not_called()


def test_matched_output_dtypes_are_stable() -> None:
    result = _enrich()
    table = result.class_proximity

    assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"
    assert str(table.nearest_road_tie_count.dtype) == "Int64"
    assert str(table.nearest_road_toll_evidence.dtype) == "boolean"


def test_parcel_preservation_uses_exact_non_geometry_values() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)

    assert_frame_equal(
        pd.DataFrame(result.parcels.drop(columns="geometry")),
        pd.DataFrame(parcels.drop(columns="geometry")),
        check_dtype=True,
        check_index_type=True,
    )
```
