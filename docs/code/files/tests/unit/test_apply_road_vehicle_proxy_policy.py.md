# `tests/unit/test_apply_road_vehicle_proxy_policy.py`

## File identity

- Repository path: `tests/unit/test_apply_road_vehicle_proxy_policy.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.
- Source SHA256: `21a34be0292629d035c000c6bfce154e5d31c2b7573acc61ae4b5623cf0ab7ca`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for apply road vehicle proxy policy; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

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
- `import numpy as np`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import LineString, Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)`
- `import landscout.stages.apply_road_vehicle_proxy_policy as module`

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

### `POLICY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POLICY_COLUMNS = (
    "road_proxy_primary_rule",
    "road_proxy_class",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_policy_scope",
    "road_proxy_policy_evidence_checked_on",
    "road_proxy_vehicle_scope",
    "road_proxy_heavy_vehicle_access",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `road_proxy_primary_rule`
  - `road_proxy_class`
  - `road_proxy_rule_trace_json`
  - `road_proxy_unknown_fields_json`
  - `road_proxy_toll_evidence`
  - `road_proxy_policy_id`
  - `road_proxy_policy_schema_version`
  - `road_proxy_policy_config_sha256`
  - `road_proxy_policy_scope`
  - `road_proxy_policy_evidence_checked_on`
  - `road_proxy_vehicle_scope`
  - `road_proxy_heavy_vehicle_access`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `test_source_config_is_exact_pydantic_type.ConfigSubclass`

**Source purpose:** Defines `test_source_config_is_exact_pydantic_type.ConfigSubclass`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `IgnBdTopoSourceConfig`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class ConfigSubclass(IgnBdTopoSourceConfig):
        pass
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_base_row`

**Purpose:** Implements `base row` within the file role: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

**Exact signature**

```python
def _base_row(number: int = 1) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `number` | positional-or-keyword | `int` | `1` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "road_feature_id": f"IGN_BDTOPO:ROAD_SEGMENT:ROAD-{number}",<br>        "road_feature_type": "ROAD_SEGMENT",<br>        "source_provider": "IGN",<br>        "source_product": "BD_TOPO",<br>        "source_layer": "troncon_de_route",<br>        "source_feature_id": f"ROAD-{number}",<br>        "source_department_code": "31",<br>        "source_edition": "2026-06-15",<br>        "source_product_version": "3.5",<br>        "source_download_timestamp": "2026-08-11T15:32:03+00:00",<br>        "source_archive_sha256": "a" * 64,<br>        "source_url": "https://example.test/roads.7z",<br>        "nature_raw": "Route à 1 chaussée",<br>        "importance_raw": "2",<br>        "fictitious_raw": False,<br>        "position_relative_to_ground_raw": 0,<br>        "asset_status_raw": "En service",<br>        "lane_count_raw": 2.0,<br>        "carriageway_width_raw": 7.0,<br>        "private_raw": 0.0,<br>        "traffic_direction_raw": "Double sens",<br>        "urban_raw": False,<br>        "mean_light_vehicle_speed_raw": 80,<br>        "light_vehicle_access_raw": "Libre",<br>        "closure_period_raw": None,<br>        "restriction_nature_raw": None,<br>        "restriction_height_raw": None,<br>        "restriction_total_weight_raw": None,<br>        "restriction_axle_weight_raw": None,<br>        "restriction_width_raw": None,<br>        "restriction_length_raw": None,<br>        "dangerous_goods_forbidden_raw": None,<br>        "administrative_classification_raw": None,<br>        "manager_raw": None,<br>        "source_name_raw": None,<br>        "source_identifiers_raw": None,<br>        "source_created_at": None,<br>        "source_modified_at": None,<br>        "source_confirmed_at": None,<br>        "planimetric_acquisition_method": "Photogrammétrie",<br>        "planimetric_precision_raw": 1.5,<br>        "spatial_role": "PROXY_GEOMETRY",<br>        "geometry_status": "VALID",<br>        "geometry": LineString([(number, 0), (number, 10)]),<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::_roads` via `_base_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_roads` via `_base_row`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
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
def _base_row(number: int = 1) -> dict[str, object]:
    return {
        "road_feature_id": f"IGN_BDTOPO:ROAD_SEGMENT:ROAD-{number}",
        "road_feature_type": "ROAD_SEGMENT",
        "source_provider": "IGN",
        "source_product": "BD_TOPO",
        "source_layer": "troncon_de_route",
        "source_feature_id": f"ROAD-{number}",
        "source_department_code": "31",
        "source_edition": "2026-06-15",
        "source_product_version": "3.5",
        "source_download_timestamp": "2026-08-11T15:32:03+00:00",
        "source_archive_sha256": "a" * 64,
        "source_url": "https://example.test/roads.7z",
        "nature_raw": "Route à 1 chaussée",
        "importance_raw": "2",
        "fictitious_raw": False,
        "position_relative_to_ground_raw": 0,
        "asset_status_raw": "En service",
        "lane_count_raw": 2.0,
        "carriageway_width_raw": 7.0,
        "private_raw": 0.0,
        "traffic_direction_raw": "Double sens",
        "urban_raw": False,
        "mean_light_vehicle_speed_raw": 80,
        "light_vehicle_access_raw": "Libre",
        "closure_period_raw": None,
        "restriction_nature_raw": None,
        "restriction_height_raw": None,
        "restriction_total_weight_raw": None,
        "restriction_axle_weight_raw": None,
        "restriction_width_raw": None,
        "restriction_length_raw": None,
        "dangerous_goods_forbidden_raw": None,
        "administrative_classification_raw": None,
        "manager_raw": None,
        "source_name_raw": None,
        "source_identifiers_raw": None,
        "source_created_at": None,
        "source_modified_at": None,
        "source_confirmed_at": None,
        "planimetric_acquisition_method": "Photogrammétrie",
        "planimetric_precision_raw": 1.5,
        "spatial_role": "PROXY_GEOMETRY",
        "geometry_status": "VALID",
        "geometry": LineString([(number, 0), (number, 10)]),
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_roads`

**Purpose:** Implements `roads` within the file role: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

**Exact signature**

```python
def _roads(*overrides: dict[str, object]) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*overrides` | variadic positional | `dict[str, object]` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:2154")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::_source` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_source` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::_row` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_row` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_geometry_status_is_rejected` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_geometry_status_is_rejected` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_lineage_is_exact_on_every_row` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_lineage_is_exact_on_every_row` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` via `_roads`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_roads`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_roads`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `_base_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._base_row` |
| `row.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `row.update(mutation)`<br>`rows.append(row)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _roads(*overrides: dict[str, object]) -> gpd.GeoDataFrame:
    mutations = overrides or ({},)
    rows: list[dict[str, object]] = []
    for number, mutation in enumerate(mutations, start=1):
        row = _base_row(number)
        row.update(mutation)
        rows.append(row)
    return gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:2154")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_source`

**Purpose:** Implements `source` within the file role: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

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
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::_apply` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_apply` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_config_type_has_controlled_error` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_wrong_source_config_type_has_controlled_error` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_malformed_policy_path_has_controlled_error` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_complete_normalization_is_invoked_exactly_once` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalization_failure_stops_policy_loading` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalization_failure_stops_policy_loading` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_generated_policy_column_collision_fails_before_policy_loading` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_object_is_not_mutated` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_path_must_be_path_or_none` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_path_must_be_path_or_none` via `_source`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_config_is_exact_pydantic_type` via `_source`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_source_config_is_exact_pydantic_type` via `_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `IgnBdTopoRoadData` | `landscout.sources.ign_bdtopo_fr.IgnBdTopoRoadData` |
| `cast` | `typing.cast` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |

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

### `_apply`

**Purpose:** Implements `apply` within the file role: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

**Exact signature**

```python
def _apply(
    roads: gpd.GeoDataFrame,
    *,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `IgnRoadVehicleProxyApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy_path` | keyword-only | `Path \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `apply_ign_road_vehicle_proxy_policy(<br>            _source(), SOURCE_CONFIG, policy_path<br>        )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::_row` via `_apply`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::_row` via `_apply`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` via `_apply`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` via `_apply`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_geometry_status_is_rejected` via `_apply`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_geometry_status_is_rejected` via `_apply`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_lineage_is_exact_on_every_row` via `_apply`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_lineage_is_exact_on_every_row` via `_apply`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` via `_apply`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` via `_apply`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `patch` | `unittest.mock.patch` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |

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
def _apply(
    roads: gpd.GeoDataFrame,
    *,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
    normalized = NormalizedIgnRoadData(road_segments=roads)
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ):
        return apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, policy_path
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_row`

**Purpose:** Implements `row` within the file role: Provides complete unit and regression coverage for the `apply_road_vehicle_proxy_policy` contracts exercised in this file.

**Exact signature**

```python
def _row(
    overrides: dict[str, object] | None = None,
) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `overrides` | positional-or-keyword | `dict[str, object] \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `result.roads.iloc[0]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_non_valid_geometry_uses_technical_gate` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_non_valid_geometry_uses_technical_gate` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_each_policy_rule_selects_approved_outcome` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_each_policy_rule_selects_approved_outcome` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_precedence_conflicts_select_first_rule` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_policy_precedence_conflicts_select_first_rule` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_boolean_like_source_values_are_parsed_without_coercion` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_boolean_like_source_values_are_parsed_without_coercion` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_critical_vocabulary_never_uses_general_fallback` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_critical_vocabulary_never_uses_general_fallback` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_width_contract` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_width_contract` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_optional_restriction_source_contract` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_optional_restriction_source_contract` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_every_configured_known_restriction_is_applied` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_every_configured_known_restriction_is_applied` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_general_fallback_requires_complete_positive_evidence_and_tracks_toll` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_general_fallback_requires_complete_positive_evidence_and_tracks_toll` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_open_access_does_not_hide_unresolved_evidence` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_open_access_does_not_hide_unresolved_evidence` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_trace_is_complete_unique_and_in_policy_order` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_trace_is_complete_unique_and_in_policy_order` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_known_higher_rule_remains_primary_while_unknown_is_traced` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_known_higher_rule_remains_primary_while_unknown_is_traced` via `_row`
- direct call: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_fields_trace_is_fixed_and_deterministic` via `_row`
- value/type reference: `tests.unit.test_apply_road_vehicle_proxy_policy::test_unknown_fields_trace_is_fixed_and_deterministic` via `_row`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_apply` | `tests.unit.test_apply_road_vehicle_proxy_policy._apply` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |

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
def _row(
    overrides: dict[str, object] | None = None,
) -> pd.Series:
    result = _apply(_roads(overrides or {}))
    return result.roads.iloc[0]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_api_exports_only_stable_application_symbols`

**Purpose:** Regression invariant: public api exports only stable application symbols. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_api_exports_only_stable_application_symbols() -> None:
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
  - `assert not hasattr(stages, "_classify_road_frame")`

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
def test_public_api_exports_only_stable_application_symbols() -> None:
    import landscout.stages.apply_road_vehicle_proxy_policy as module

    expected = {
        "IgnRoadVehicleProxyApplicationError",
        "IgnRoadVehicleProxyApplicationResult",
        "apply_ign_road_vehicle_proxy_policy",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_classify_road_frame")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_source_type_has_controlled_error`

**Purpose:** Regression invariant: wrong source type has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_source_type_has_controlled_error() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
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
def test_wrong_source_type_has_controlled_error() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(cast(Any, object()), SOURCE_CONFIG)
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
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
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
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), cast(Any, object()))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_policy_path_has_controlled_error`

**Purpose:** Regression invariant: malformed policy path has controlled error. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_policy_path_has_controlled_error(tmp_path: Path) -> None:
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
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `patch` | `unittest.mock.patch` |
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |

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
def test_malformed_policy_path_has_controlled_error(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            return_value=NormalizedIgnRoadData(_roads()),
        ),
        pytest.raises(IgnRoadVehicleProxyApplicationError),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_complete_normalization_is_invoked_exactly_once`

**Purpose:** Regression invariant: source complete normalization is invoked exactly once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_complete_normalization_is_invoked_exactly_once() -> None:
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
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
| `patch` | `unittest.mock.patch` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
| `validator.assert_called_once` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_source_complete_normalization_is_invoked_exactly_once() -> None:
    normalized = NormalizedIgnRoadData(_roads())
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ) as validator:
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    validator.assert_called_once()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalization_failure_stops_policy_loading`

**Purpose:** Regression invariant: normalization failure stops policy loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalization_failure_stops_policy_loading() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `patch` | `unittest.mock.patch` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
| `policy_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_normalization_failure_stops_policy_loading() -> None:
    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            side_effect=IgnRoadNormalizationError("bad source"),
        ),
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy"
        ) as policy_loader,
        pytest.raises(IgnRoadVehicleProxyApplicationError),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    policy_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_generated_policy_column_collision_fails_before_policy_loading`

**Purpose:** Regression invariant: generated policy column collision fails before policy loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_generated_policy_column_collision_fails_before_policy_loading() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyApplicationError, match="collide.*generated")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
| `patch` | `unittest.mock.patch` |
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
| `policy_loader.assert_not_called` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `roads["road_proxy_class"] = "FORGED"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_generated_policy_column_collision_fails_before_policy_loading() -> None:
    roads = _roads()
    roads["road_proxy_class"] = "FORGED"

    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            return_value=NormalizedIgnRoadData(roads),
        ),
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy"
        ) as policy_loader,
        pytest.raises(IgnRoadVehicleProxyApplicationError, match="collide.*generated"),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    policy_loader.assert_not_called()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalized_facts_rows_index_crs_and_geometry_are_preserved`

**Purpose:** Regression invariant: normalized facts rows index crs and geometry are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalized_facts_rows_index_crs_and_geometry_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert list(result.columns[: len(roads.columns)]) == list(roads.columns)`
  - `assert list(result.columns[len(roads.columns) :]) == list(POLICY_COLUMNS)`
  - `assert isinstance(result.index, pd.RangeIndex)`
  - `assert result.index.equals(roads.index)`
  - `assert result.crs == roads.crs`
  - `assert result.active_geometry_name == roads.active_geometry_name`
  - `assert result.geometry.to_wkb().equals(roads.geometry.to_wkb())`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
| `deepcopy` | `copy.deepcopy` |
| `_apply` | `tests.unit.test_apply_road_vehicle_proxy_policy._apply` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.geometry.to_wkb().equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.geometry.to_wkb().equals`<br>`result.geometry.to_wkb`<br>`roads.geometry.to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_normalized_facts_rows_index_crs_and_geometry_are_preserved() -> None:
    roads = _roads(
        {"nature_raw": "Chemin"},
        {"road_feature_id": "IGN_BDTOPO:ROAD_SEGMENT:SECOND"},
    )
    before = deepcopy(roads)

    result = _apply(roads).roads

    assert list(result.columns[: len(roads.columns)]) == list(roads.columns)
    assert list(result.columns[len(roads.columns) :]) == list(POLICY_COLUMNS)
    assert isinstance(result.index, pd.RangeIndex)
    assert result.index.equals(roads.index)
    assert result.crs == roads.crs
    assert result.active_geometry_name == roads.active_geometry_name
    assert result.geometry.to_wkb().equals(roads.geometry.to_wkb())
    assert_geodataframe_equal(result.loc[:, roads.columns], roads)
    assert_geodataframe_equal(roads, before)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_object_is_not_mutated`

**Purpose:** Regression invariant: source object is not mutated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_object_is_not_mutated() -> None:
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
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
| `deepcopy` | `copy.deepcopy` |
| `NormalizedIgnRoadData` | `landscout.stages.normalize_access_ign.NormalizedIgnRoadData` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
| `patch` | `unittest.mock.patch` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
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
def test_source_object_is_not_mutated() -> None:
    source = _source()
    before = deepcopy(source.road_segments)
    normalized = NormalizedIgnRoadData(_roads())

    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ):
        apply_ign_road_vehicle_proxy_policy(source, SOURCE_CONFIG)

    assert_geodataframe_equal(source.road_segments, before)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_non_valid_geometry_uses_technical_gate`

**Purpose:** Regression invariant: non valid geometry uses technical gate. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_non_valid_geometry_uses_technical_gate(status: str, geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("status", "geometry"),
    [
        ("NULL", None),
        ("EMPTY", LineString()),
        ("INVALID", LineString([(0, 0), (1, 1), (0, 1), (1, 0)])),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `status` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.road_proxy_primary_rule == "SOURCE_GEOMETRY_NOT_VALID"`
  - `assert row.road_proxy_class == "NOT_DISTANCE_PROXY"`
  - `assert row.road_proxy_rule_trace_json == '["SOURCE_GEOMETRY_NOT_VALID"]'`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
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
def test_non_valid_geometry_uses_technical_gate(status: str, geometry: object) -> None:
    row = _row({"geometry_status": status, "geometry": geometry})

    assert row.road_proxy_primary_rule == "SOURCE_GEOMETRY_NOT_VALID"
    assert row.road_proxy_class == "NOT_DISTANCE_PROXY"
    assert row.road_proxy_rule_trace_json == '["SOURCE_GEOMETRY_NOT_VALID"]'
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_geometry_status_is_rejected`

**Purpose:** Regression invariant: unknown geometry status is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_geometry_status_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_apply` | `tests.unit.test_apply_road_vehicle_proxy_policy._apply` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |

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
def test_unknown_geometry_status_is_rejected() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        _apply(_roads({"geometry_status": "BROKEN"}))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_each_policy_rule_selects_approved_outcome`

**Purpose:** Regression invariant: each policy rule selects approved outcome. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_each_policy_rule_selects_approved_outcome(
    overrides: dict[str, object], rule: str, expected_class: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("overrides", "rule", "expected_class"),
    [
        ({"fictitious_raw": True}, "FICTITIOUS_GEOMETRY", "NOT_DISTANCE_PROXY"),
        (
            {"asset_status_raw": "En projet"},
            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
            "NOT_DISTANCE_PROXY",
        ),
        (
            {"asset_status_raw": "En construction"},
            "NOT_IN_SERVICE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"light_vehicle_access_raw": "Physiquement impossible"},
            "PHYSICALLY_IMPOSSIBLE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"nature_raw": "Escalier"},
            "NON_GENERAL_VEHICLE_NATURE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"light_vehicle_access_raw": "Restreint aux ayants droit"},
            "RIGHTS_RESTRICTED",
            "RESTRICTED_REVIEW",
        ),
        ({"private_raw": 1.0}, "PRIVATE_ROAD", "RESTRICTED_REVIEW"),
        (
            {"closure_period_raw": "Fermeture hivernale"},
            "TEMPORAL_CLOSURE",
            "RESTRICTED_REVIEW",
        ),
        (
            {"restriction_nature_raw": "Plot amovible"},
            "KNOWN_RESTRICTION",
            "RESTRICTED_REVIEW",
        ),
        (
            {"restriction_nature_raw": "Nouvelle restriction"},
            "OTHER_RECORDED_RESTRICTION",
            "RESTRICTED_REVIEW",
        ),
        (
            {"nature_raw": "Bac ou liaison maritime"},
            "SPECIAL_NATURE",
            "RESTRICTED_REVIEW",
        ),
        ({"nature_raw": "Chemin"}, "LIMITED_NATURE", "LIMITED_VEHICLE_PROXY"),
        ({"importance_raw": "6"}, "IMPORTANCE_6", "LIMITED_VEHICLE_PROXY"),
        (
            {"carriageway_width_raw": 2.8},
            "NARROW_CARRIAGEWAY",
            "LIMITED_VEHICLE_PROXY",
        ),
        ({}, "OPEN_OR_TOLL", "GENERAL_VEHICLE_PROXY"),
        ({"nature_raw": "Future"}, "UNKNOWN", "UNKNOWN_REVIEW"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `overrides` | positional-or-keyword | `dict[str, object]` | `required` |
| `rule` | positional-or-keyword | `str` | `required` |
| `expected_class` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.road_proxy_primary_rule == rule`
  - `assert row.road_proxy_class == expected_class`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
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
def test_each_policy_rule_selects_approved_outcome(
    overrides: dict[str, object], rule: str, expected_class: str
) -> None:
    row = _row(overrides)

    assert row.road_proxy_primary_rule == rule
    assert row.road_proxy_class == expected_class
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_precedence_conflicts_select_first_rule`

**Purpose:** Regression invariant: policy precedence conflicts select first rule. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_precedence_conflicts_select_first_rule(
    overrides: dict[str, object], rule: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("overrides", "rule"),
    [
        ({"fictitious_raw": True, "private_raw": 1.0}, "FICTITIOUS_GEOMETRY"),
        (
            {
                "asset_status_raw": "En projet",
                "light_vehicle_access_raw": "Physiquement impossible",
            },
            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
        ),
        (
            {
                "light_vehicle_access_raw": "Physiquement impossible",
                "private_raw": 1.0,
            },
            "PHYSICALLY_IMPOSSIBLE",
        ),
        ({"private_raw": 1.0, "carriageway_width_raw": 2.5}, "PRIVATE_ROAD"),
        (
            {"closure_period_raw": "Hiver", "nature_raw": "Chemin"},
            "TEMPORAL_CLOSURE",
        ),
        (
            {
                "restriction_nature_raw": "Plot amovible",
                "nature_raw": "Bac ou liaison maritime",
            },
            "KNOWN_RESTRICTION",
        ),
        ({"nature_raw": "Chemin", "importance_raw": "6"}, "LIMITED_NATURE"),
        (
            {"importance_raw": "6", "carriageway_width_raw": 2.5},
            "IMPORTANCE_6",
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `overrides` | positional-or-keyword | `dict[str, object]` | `required` |
| `rule` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row(overrides).road_proxy_primary_rule == rule`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
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
def test_policy_precedence_conflicts_select_first_rule(
    overrides: dict[str, object], rule: str
) -> None:
    assert _row(overrides).road_proxy_primary_rule == rule
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_boolean_like_source_values_are_parsed_without_coercion`

**Purpose:** Regression invariant: boolean like source values are parsed without coercion. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_boolean_like_source_values_are_parsed_without_coercion(
    field: str, value: object, expected_rule: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value", "expected_rule"),
    [
        ("fictitious_raw", False, "OPEN_OR_TOLL"),
        ("fictitious_raw", np.bool_(True), "FICTITIOUS_GEOMETRY"),
        ("fictitious_raw", None, "UNKNOWN"),
        ("fictitious_raw", "true", "UNKNOWN"),
        ("private_raw", False, "OPEN_OR_TOLL"),
        ("private_raw", True, "PRIVATE_ROAD"),
        ("private_raw", 0, "OPEN_OR_TOLL"),
        ("private_raw", 1, "PRIVATE_ROAD"),
        ("private_raw", 0.0, "OPEN_OR_TOLL"),
        ("private_raw", 1.0, "PRIVATE_ROAD"),
        ("private_raw", None, "UNKNOWN"),
        ("private_raw", 2, "UNKNOWN"),
        ("private_raw", "1", "UNKNOWN"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |
| `expected_rule` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row({field: value}).road_proxy_primary_rule == expected_rule`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `np.bool_` | `numpy.bool_` |

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
def test_boolean_like_source_values_are_parsed_without_coercion(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_critical_vocabulary_never_uses_general_fallback`

**Purpose:** Regression invariant: unknown critical vocabulary never uses general fallback. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_critical_vocabulary_never_uses_general_fallback(
    field: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("asset_status_raw", "Future"),
        ("nature_raw", "Future"),
        ("light_vehicle_access_raw", "Future"),
        ("importance_raw", "7"),
        ("importance_raw", 6),
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
- Exact assertions:
  - `assert row.road_proxy_primary_rule == "UNKNOWN"`
  - `assert row.road_proxy_class == "UNKNOWN_REVIEW"`
  - `assert field in row.road_proxy_unknown_fields_json`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
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
def test_unknown_critical_vocabulary_never_uses_general_fallback(
    field: str, value: object
) -> None:
    row = _row({field: value})

    assert row.road_proxy_primary_rule == "UNKNOWN"
    assert row.road_proxy_class == "UNKNOWN_REVIEW"
    assert field in row.road_proxy_unknown_fields_json
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_width_contract`

**Purpose:** Regression invariant: width contract. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_width_contract(value: object, expected_rule: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("value", "expected_rule"),
    [
        (None, "OPEN_OR_TOLL"),
        (float("nan"), "OPEN_OR_TOLL"),
        (2.9, "OPEN_OR_TOLL"),
        (2.899999, "NARROW_CARRIAGEWAY"),
        (0.0, "UNKNOWN"),
        (-1.0, "UNKNOWN"),
        (float("inf"), "UNKNOWN"),
        ("2.8", "UNKNOWN"),
        (True, "UNKNOWN"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `expected_rule` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row({"carriageway_width_raw": value}).road_proxy_primary_rule == (<br>        expected_rule<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
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
def test_width_contract(value: object, expected_rule: str) -> None:
    assert _row({"carriageway_width_raw": value}).road_proxy_primary_rule == (
        expected_rule
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_optional_restriction_source_contract`

**Purpose:** Regression invariant: optional restriction source contract. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_optional_restriction_source_contract(
    field: str, value: object, expected_rule: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value", "expected_rule"),
    [
        ("closure_period_raw", None, "OPEN_OR_TOLL"),
        ("closure_period_raw", "Hiver", "TEMPORAL_CLOSURE"),
        ("closure_period_raw", " ", "UNKNOWN"),
        ("closure_period_raw", 1, "UNKNOWN"),
        ("restriction_nature_raw", None, "OPEN_OR_TOLL"),
        ("restriction_nature_raw", "Plot amovible", "KNOWN_RESTRICTION"),
        (
            "restriction_nature_raw",
            "Restriction nouvelle",
            "OTHER_RECORDED_RESTRICTION",
        ),
        ("restriction_nature_raw", "", "UNKNOWN"),
        ("restriction_nature_raw", 1, "UNKNOWN"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |
| `expected_rule` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row({field: value}).road_proxy_primary_rule == expected_rule`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
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
def test_optional_restriction_source_contract(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_configured_known_restriction_is_applied`

**Purpose:** Regression invariant: every configured known restriction is applied. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_configured_known_restriction_is_applied() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>            _row({"restriction_nature_raw": restriction}).road_proxy_primary_rule<br>            == "KNOWN_RESTRICTION"<br>        )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |

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
def test_every_configured_known_restriction_is_applied() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    for restriction in policy.known_restriction_review:
        assert (
            _row({"restriction_nature_raw": restriction}).road_proxy_primary_rule
            == "KNOWN_RESTRICTION"
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_general_fallback_requires_complete_positive_evidence_and_tracks_toll`

**Purpose:** Regression invariant: general fallback requires complete positive evidence and tracks toll. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_general_fallback_requires_complete_positive_evidence_and_tracks_toll() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert open_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"`
  - `assert not open_row.road_proxy_toll_evidence`
  - `assert toll_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"`
  - `assert toll_row.road_proxy_toll_evidence`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |

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
def test_general_fallback_requires_complete_positive_evidence_and_tracks_toll() -> None:
    open_row = _row()
    toll_row = _row({"light_vehicle_access_raw": "A péage"})

    assert open_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert not open_row.road_proxy_toll_evidence
    assert toll_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert toll_row.road_proxy_toll_evidence
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_open_access_does_not_hide_unresolved_evidence`

**Purpose:** Regression invariant: open access does not hide unresolved evidence. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_open_access_does_not_hide_unresolved_evidence(
    overrides: dict[str, object],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "overrides",
    [
        {"nature_raw": "Future"},
        {"private_raw": None},
        {"importance_raw": "7"},
        {"carriageway_width_raw": "wide"},
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `overrides` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert _row(overrides).road_proxy_primary_rule == "UNKNOWN"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |
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
def test_open_access_does_not_hide_unresolved_evidence(
    overrides: dict[str, object],
) -> None:
    assert _row(overrides).road_proxy_primary_rule == "UNKNOWN"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_trace_is_complete_unique_and_in_policy_order`

**Purpose:** Regression invariant: trace is complete unique and in policy order. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_trace_is_complete_unique_and_in_policy_order() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.road_proxy_rule_trace_json == expected`
  - `assert row.road_proxy_primary_rule == "PRIVATE_ROAD"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |

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
def test_trace_is_complete_unique_and_in_policy_order() -> None:
    row = _row(
        {
            "private_raw": 1.0,
            "closure_period_raw": "Hiver",
            "restriction_nature_raw": "Plot amovible",
            "nature_raw": "Chemin",
            "importance_raw": "6",
            "carriageway_width_raw": 2.0,
        }
    )
    expected = (
        '["PRIVATE_ROAD","TEMPORAL_CLOSURE","KNOWN_RESTRICTION",'
        '"LIMITED_NATURE","IMPORTANCE_6","NARROW_CARRIAGEWAY"]'
    )

    assert row.road_proxy_rule_trace_json == expected
    assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_known_higher_rule_remains_primary_while_unknown_is_traced`

**Purpose:** Regression invariant: known higher rule remains primary while unknown is traced. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_known_higher_rule_remains_primary_while_unknown_is_traced() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.road_proxy_primary_rule == "PRIVATE_ROAD"`
  - `assert row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'`
  - `assert row.road_proxy_unknown_fields_json == '["importance_raw"]'`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |

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
def test_known_higher_rule_remains_primary_while_unknown_is_traced() -> None:
    row = _row({"private_raw": 1.0, "importance_raw": "7"})

    assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
    assert row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'
    assert row.road_proxy_unknown_fields_json == '["importance_raw"]'
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_fields_trace_is_fixed_and_deterministic`

**Purpose:** Regression invariant: unknown fields trace is fixed and deterministic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_fields_trace_is_fixed_and_deterministic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert row.road_proxy_unknown_fields_json == (<br>        '["fictitious_raw","asset_status_raw","nature_raw",'<br>        '"light_vehicle_access_raw","private_raw","importance_raw",'<br>        '"carriageway_width_raw","closure_period_raw",'<br>        '"restriction_nature_raw"]'<br>    )`
  - `assert _row().road_proxy_unknown_fields_json == "[]"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_row` | `tests.unit.test_apply_road_vehicle_proxy_policy._row` |

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
def test_unknown_fields_trace_is_fixed_and_deterministic() -> None:
    row = _row(
        {
            "fictitious_raw": None,
            "asset_status_raw": "Future",
            "nature_raw": "Future",
            "light_vehicle_access_raw": "Future",
            "private_raw": None,
            "importance_raw": "7",
            "carriageway_width_raw": "bad",
            "closure_period_raw": " ",
            "restriction_nature_raw": 1,
        }
    )
    assert row.road_proxy_unknown_fields_json == (
        '["fictitious_raw","asset_status_raw","nature_raw",'
        '"light_vehicle_access_raw","private_raw","importance_raw",'
        '"carriageway_width_raw","closure_period_raw",'
        '"restriction_nature_raw"]'
    )
    assert _row().road_proxy_unknown_fields_json == "[]"
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_lineage_is_exact_on_every_row`

**Purpose:** Regression invariant: policy lineage is exact on every row. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_lineage_is_exact_on_every_row() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(result.road_proxy_policy_id) == {policy.policy_id}`
  - `assert set(result.road_proxy_policy_schema_version) == {policy.schema_version}`
  - `assert set(result.road_proxy_policy_config_sha256) == {policy.config_sha256}`
  - `assert set(result.road_proxy_policy_scope) == {policy.scope}`
  - `assert set(result.road_proxy_policy_evidence_checked_on) == {<br>        policy.evidence_checked_on<br>    }`
  - `assert set(result.road_proxy_vehicle_scope) == {policy.vehicle_scope}`
  - `assert set(result.road_proxy_heavy_vehicle_access) == {"NOT_PROVEN"}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `_apply` | `tests.unit.test_apply_road_vehicle_proxy_policy._apply` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
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
def test_policy_lineage_is_exact_on_every_row() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    result = _apply(_roads({}, {})).roads

    assert set(result.road_proxy_policy_id) == {policy.policy_id}
    assert set(result.road_proxy_policy_schema_version) == {policy.schema_version}
    assert set(result.road_proxy_policy_config_sha256) == {policy.config_sha256}
    assert set(result.road_proxy_policy_scope) == {policy.scope}
    assert set(result.road_proxy_policy_evidence_checked_on) == {
        policy.evidence_checked_on
    }
    assert set(result.road_proxy_vehicle_scope) == {policy.vehicle_scope}
    assert set(result.road_proxy_heavy_vehicle_access) == {"NOT_PROVEN"}
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary`

**Purpose:** Regression invariant: result is frozen and contains no unsafe claim vocabulary. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary() -> None:
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
  - `assert all(token not in produced for token in forbidden)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_apply` | `tests.unit.test_apply_road_vehicle_proxy_policy._apply` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
| `pytest.raises` | `pytest.raises` |
| `" ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `map` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.roads.astype(str).to_numpy().ravel` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.roads.astype(str).to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.roads.astype` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `result.roads = _roads()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary() -> None:
    result = _apply(_roads())
    forbidden = (
        "TRUCK_ACCESSIBLE",
        "LEGAL_ACCESS",
        "BESS_ACCESSIBLE",
        "AUTHORIZED",
        "APPROVED",
    )

    with pytest.raises(FrozenInstanceError):
        result.roads = _roads()  # type: ignore[misc]
    produced = " ".join(
        map(
            str,
            [*result.roads.columns, *result.roads.astype(str).to_numpy().ravel()],
        )
    )
    assert all(token not in produced for token in forbidden)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_geometry_status_with_unsupported_geometry_is_not_repaired`

**Purpose:** Regression invariant: valid geometry status with unsupported geometry is not repaired. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_geometry_status_with_unsupported_geometry_is_not_repaired() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`
- Exact assertions:
  - `assert roads.geometry.iloc[0].equals_exact(polygon, tolerance=0)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_roads` | `tests.unit.test_apply_road_vehicle_proxy_policy._roads` |
| `patch` | `unittest.mock.patch` |
| `IgnRoadNormalizationError` | `landscout.stages.normalize_access_ign.IgnRoadNormalizationError` |
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
| `roads.geometry.iloc[0].equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `roads.geometry.iloc[0].equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_geometry_status_with_unsupported_geometry_is_not_repaired() -> None:
    polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])
    roads = _roads({"geometry": polygon})

    # The source-complete normalizer owns this geometry-kind rejection. The
    # application must propagate its controlled failure rather than repair it.
    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            side_effect=IgnRoadNormalizationError("unsupported geometry"),
        ),
        pytest.raises(IgnRoadVehicleProxyApplicationError),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    assert roads.geometry.iloc[0].equals_exact(polygon, tolerance=0)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_path_must_be_path_or_none`

**Purpose:** Regression invariant: policy path must be path or none. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_path_must_be_path_or_none() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
| `cast` | `typing.cast` |
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
def test_policy_path_must_be_path_or_none() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, cast(Any, str(POLICY_PATH))
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_config_is_exact_pydantic_type`

**Purpose:** Regression invariant: source config is exact pydantic type. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_config_is_exact_pydantic_type() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(IgnRoadVehicleProxyApplicationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_source` | `tests.unit.test_apply_road_vehicle_proxy_policy._source` |
| `ConfigSubclass.model_validate` | `unresolved local/third-party receiver; no ownership inferred` |
| `SOURCE_CONFIG.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_source_config_is_exact_pydantic_type() -> None:
    class ConfigSubclass(IgnBdTopoSourceConfig):
        pass

    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), ConfigSubclass.model_validate(SOURCE_CONFIG.model_dump())
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **28**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_public_api_exports_only_stable_application_symbols` | none | none | 4 | Proves public api exports only stable application symbols using the exact source reproduced in section 7. |
| `test_wrong_source_type_has_controlled_error` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 0 | Proves wrong source type has controlled error using the exact source reproduced in section 7. |
| `test_wrong_source_config_type_has_controlled_error` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 0 | Proves wrong source config type has controlled error using the exact source reproduced in section 7. |
| `test_malformed_policy_path_has_controlled_error` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 0 | Proves malformed policy path has controlled error using the exact source reproduced in section 7. |
| `test_source_complete_normalization_is_invoked_exactly_once` | none | none | 0 | Proves source complete normalization is invoked exactly once using the exact source reproduced in section 7. |
| `test_normalization_failure_stops_policy_loading` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 0 | Proves normalization failure stops policy loading using the exact source reproduced in section 7. |
| `test_generated_policy_column_collision_fails_before_policy_loading` | none | pytest.raises(IgnRoadVehicleProxyApplicationError, match="collide.*generated") | 0 | Proves generated policy column collision fails before policy loading using the exact source reproduced in section 7. |
| `test_normalized_facts_rows_index_crs_and_geometry_are_preserved` | none | none | 7 | Proves normalized facts rows index crs and geometry are preserved using the exact source reproduced in section 7. |
| `test_source_object_is_not_mutated` | none | none | 0 | Proves source object is not mutated using the exact source reproduced in section 7. |
| `test_non_valid_geometry_uses_technical_gate` | pytest.mark.parametrize(<br>    ("status", "geometry"),<br>    [<br>        ("NULL", None),<br>        ("EMPTY", LineString()),<br>        ("INVALID", LineString([(0, 0), (1, 1), (0, 1), (1, 0)])),<br>    ],<br>) | none | 3 | Proves non valid geometry uses technical gate using the exact source reproduced in section 7. |
| `test_unknown_geometry_status_is_rejected` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 0 | Proves unknown geometry status is rejected using the exact source reproduced in section 7. |
| `test_each_policy_rule_selects_approved_outcome` | pytest.mark.parametrize(<br>    ("overrides", "rule", "expected_class"),<br>    [<br>        ({"fictitious_raw": True}, "FICTITIOUS_GEOMETRY", "NOT_DISTANCE_PROXY"),<br>        (<br>            {"asset_status_raw": "En projet"},<br>            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",<br>            "NOT_DISTANCE_PROXY",<br>        ),<br>        (<br>            {"asset_status_raw": "En construction"},<br>            "NOT_IN_SERVICE",<br>            "NOT_GENERAL_VEHICLE_PROXY",<br>        ),<br>        (<br>            {"light_vehicle_access_raw": "Physiquement impossible"},<br>            "PHYSICALLY_IMPOSSIBLE",<br>            "NOT_GENERAL_VEHICLE_PROXY",<br>        ),<br>        (<br>            {"nature_raw": "Escalier"},<br>            "NON_GENERAL_VEHICLE_NATURE",<br>            "NOT_GENERAL_VEHICLE_PROXY",<br>        ),<br>        (<br>            {"light_vehicle_access_raw": "Restreint aux ayants droit"},<br>            "RIGHTS_RESTRICTED",<br>            "RESTRICTED_REVIEW",<br>        ),<br>        ({"private_raw": 1.0}, "PRIVATE_ROAD", "RESTRICTED_REVIEW"),<br>        (<br>            {"closure_period_raw": "Fermeture hivernale"},<br>            "TEMPORAL_CLOSURE",<br>            "RESTRICTED_REVIEW",<br>        ),<br>        (<br>            {"restriction_nature_raw": "Plot amovible"},<br>            "KNOWN_RESTRICTION",<br>            "RESTRICTED_REVIEW",<br>        ),<br>        (<br>            {"restriction_nature_raw": "Nouvelle restriction"},<br>            "OTHER_RECORDED_RESTRICTION",<br>            "RESTRICTED_REVIEW",<br>        ),<br>        (<br>            {"nature_raw": "Bac ou liaison maritime"},<br>            "SPECIAL_NATURE",<br>            "RESTRICTED_REVIEW",<br>        ),<br>        ({"nature_raw": "Chemin"}, "LIMITED_NATURE", "LIMITED_VEHICLE_PROXY"),<br>        ({"importance_raw": "6"}, "IMPORTANCE_6", "LIMITED_VEHICLE_PROXY"),<br>        (<br>            {"carriageway_width_raw": 2.8},<br>            "NARROW_CARRIAGEWAY",<br>            "LIMITED_VEHICLE_PROXY",<br>        ),<br>        ({}, "OPEN_OR_TOLL", "GENERAL_VEHICLE_PROXY"),<br>        ({"nature_raw": "Future"}, "UNKNOWN", "UNKNOWN_REVIEW"),<br>    ],<br>) | none | 2 | Proves each policy rule selects approved outcome using the exact source reproduced in section 7. |
| `test_policy_precedence_conflicts_select_first_rule` | pytest.mark.parametrize(<br>    ("overrides", "rule"),<br>    [<br>        ({"fictitious_raw": True, "private_raw": 1.0}, "FICTITIOUS_GEOMETRY"),<br>        (<br>            {<br>                "asset_status_raw": "En projet",<br>                "light_vehicle_access_raw": "Physiquement impossible",<br>            },<br>            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",<br>        ),<br>        (<br>            {<br>                "light_vehicle_access_raw": "Physiquement impossible",<br>                "private_raw": 1.0,<br>            },<br>            "PHYSICALLY_IMPOSSIBLE",<br>        ),<br>        ({"private_raw": 1.0, "carriageway_width_raw": 2.5}, "PRIVATE_ROAD"),<br>        (<br>            {"closure_period_raw": "Hiver", "nature_raw": "Chemin"},<br>            "TEMPORAL_CLOSURE",<br>        ),<br>        (<br>            {<br>                "restriction_nature_raw": "Plot amovible",<br>                "nature_raw": "Bac ou liaison maritime",<br>            },<br>            "KNOWN_RESTRICTION",<br>        ),<br>        ({"nature_raw": "Chemin", "importance_raw": "6"}, "LIMITED_NATURE"),<br>        (<br>            {"importance_raw": "6", "carriageway_width_raw": 2.5},<br>            "IMPORTANCE_6",<br>        ),<br>    ],<br>) | none | 1 | Proves policy precedence conflicts select first rule using the exact source reproduced in section 7. |
| `test_boolean_like_source_values_are_parsed_without_coercion` | pytest.mark.parametrize(<br>    ("field", "value", "expected_rule"),<br>    [<br>        ("fictitious_raw", False, "OPEN_OR_TOLL"),<br>        ("fictitious_raw", np.bool_(True), "FICTITIOUS_GEOMETRY"),<br>        ("fictitious_raw", None, "UNKNOWN"),<br>        ("fictitious_raw", "true", "UNKNOWN"),<br>        ("private_raw", False, "OPEN_OR_TOLL"),<br>        ("private_raw", True, "PRIVATE_ROAD"),<br>        ("private_raw", 0, "OPEN_OR_TOLL"),<br>        ("private_raw", 1, "PRIVATE_ROAD"),<br>        ("private_raw", 0.0, "OPEN_OR_TOLL"),<br>        ("private_raw", 1.0, "PRIVATE_ROAD"),<br>        ("private_raw", None, "UNKNOWN"),<br>        ("private_raw", 2, "UNKNOWN"),<br>        ("private_raw", "1", "UNKNOWN"),<br>    ],<br>) | none | 1 | Proves boolean like source values are parsed without coercion using the exact source reproduced in section 7. |
| `test_unknown_critical_vocabulary_never_uses_general_fallback` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("asset_status_raw", "Future"),<br>        ("nature_raw", "Future"),<br>        ("light_vehicle_access_raw", "Future"),<br>        ("importance_raw", "7"),<br>        ("importance_raw", 6),<br>    ],<br>) | none | 3 | Proves unknown critical vocabulary never uses general fallback using the exact source reproduced in section 7. |
| `test_width_contract` | pytest.mark.parametrize(<br>    ("value", "expected_rule"),<br>    [<br>        (None, "OPEN_OR_TOLL"),<br>        (float("nan"), "OPEN_OR_TOLL"),<br>        (2.9, "OPEN_OR_TOLL"),<br>        (2.899999, "NARROW_CARRIAGEWAY"),<br>        (0.0, "UNKNOWN"),<br>        (-1.0, "UNKNOWN"),<br>        (float("inf"), "UNKNOWN"),<br>        ("2.8", "UNKNOWN"),<br>        (True, "UNKNOWN"),<br>    ],<br>) | none | 1 | Proves width contract using the exact source reproduced in section 7. |
| `test_optional_restriction_source_contract` | pytest.mark.parametrize(<br>    ("field", "value", "expected_rule"),<br>    [<br>        ("closure_period_raw", None, "OPEN_OR_TOLL"),<br>        ("closure_period_raw", "Hiver", "TEMPORAL_CLOSURE"),<br>        ("closure_period_raw", " ", "UNKNOWN"),<br>        ("closure_period_raw", 1, "UNKNOWN"),<br>        ("restriction_nature_raw", None, "OPEN_OR_TOLL"),<br>        ("restriction_nature_raw", "Plot amovible", "KNOWN_RESTRICTION"),<br>        (<br>            "restriction_nature_raw",<br>            "Restriction nouvelle",<br>            "OTHER_RECORDED_RESTRICTION",<br>        ),<br>        ("restriction_nature_raw", "", "UNKNOWN"),<br>        ("restriction_nature_raw", 1, "UNKNOWN"),<br>    ],<br>) | none | 1 | Proves optional restriction source contract using the exact source reproduced in section 7. |
| `test_every_configured_known_restriction_is_applied` | none | none | 1 | Proves every configured known restriction is applied using the exact source reproduced in section 7. |
| `test_general_fallback_requires_complete_positive_evidence_and_tracks_toll` | none | none | 4 | Proves general fallback requires complete positive evidence and tracks toll using the exact source reproduced in section 7. |
| `test_open_access_does_not_hide_unresolved_evidence` | pytest.mark.parametrize(<br>    "overrides",<br>    [<br>        {"nature_raw": "Future"},<br>        {"private_raw": None},<br>        {"importance_raw": "7"},<br>        {"carriageway_width_raw": "wide"},<br>    ],<br>) | none | 1 | Proves open access does not hide unresolved evidence using the exact source reproduced in section 7. |
| `test_trace_is_complete_unique_and_in_policy_order` | none | none | 2 | Proves trace is complete unique and in policy order using the exact source reproduced in section 7. |
| `test_known_higher_rule_remains_primary_while_unknown_is_traced` | none | none | 3 | Proves known higher rule remains primary while unknown is traced using the exact source reproduced in section 7. |
| `test_unknown_fields_trace_is_fixed_and_deterministic` | none | none | 2 | Proves unknown fields trace is fixed and deterministic using the exact source reproduced in section 7. |
| `test_policy_lineage_is_exact_on_every_row` | none | none | 7 | Proves policy lineage is exact on every row using the exact source reproduced in section 7. |
| `test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary` | none | pytest.raises(FrozenInstanceError) | 1 | Proves result is frozen and contains no unsafe claim vocabulary using the exact source reproduced in section 7. |
| `test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 1 | Proves valid geometry status with unsupported geometry is not repaired using the exact source reproduced in section 7. |
| `test_policy_path_must_be_path_or_none` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 0 | Proves policy path must be path or none using the exact source reproduced in section 7. |
| `test_source_config_is_exact_pydantic_type` | none | pytest.raises(IgnRoadVehicleProxyApplicationError) | 0 | Proves source config is exact pydantic type using the exact source reproduced in section 7. |

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
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import LineString, Polygon

from landscout import stages
from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)
from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationError,
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)
from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
)
from landscout.stages.road_vehicle_proxy_policy import (
    load_ign_road_vehicle_proxy_policy,
)

SOURCE_CONFIG = load_ign_bdtopo_source_config()
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
POLICY_COLUMNS = (
    "road_proxy_primary_rule",
    "road_proxy_class",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_policy_scope",
    "road_proxy_policy_evidence_checked_on",
    "road_proxy_vehicle_scope",
    "road_proxy_heavy_vehicle_access",
)


def _base_row(number: int = 1) -> dict[str, object]:
    return {
        "road_feature_id": f"IGN_BDTOPO:ROAD_SEGMENT:ROAD-{number}",
        "road_feature_type": "ROAD_SEGMENT",
        "source_provider": "IGN",
        "source_product": "BD_TOPO",
        "source_layer": "troncon_de_route",
        "source_feature_id": f"ROAD-{number}",
        "source_department_code": "31",
        "source_edition": "2026-06-15",
        "source_product_version": "3.5",
        "source_download_timestamp": "2026-08-11T15:32:03+00:00",
        "source_archive_sha256": "a" * 64,
        "source_url": "https://example.test/roads.7z",
        "nature_raw": "Route à 1 chaussée",
        "importance_raw": "2",
        "fictitious_raw": False,
        "position_relative_to_ground_raw": 0,
        "asset_status_raw": "En service",
        "lane_count_raw": 2.0,
        "carriageway_width_raw": 7.0,
        "private_raw": 0.0,
        "traffic_direction_raw": "Double sens",
        "urban_raw": False,
        "mean_light_vehicle_speed_raw": 80,
        "light_vehicle_access_raw": "Libre",
        "closure_period_raw": None,
        "restriction_nature_raw": None,
        "restriction_height_raw": None,
        "restriction_total_weight_raw": None,
        "restriction_axle_weight_raw": None,
        "restriction_width_raw": None,
        "restriction_length_raw": None,
        "dangerous_goods_forbidden_raw": None,
        "administrative_classification_raw": None,
        "manager_raw": None,
        "source_name_raw": None,
        "source_identifiers_raw": None,
        "source_created_at": None,
        "source_modified_at": None,
        "source_confirmed_at": None,
        "planimetric_acquisition_method": "Photogrammétrie",
        "planimetric_precision_raw": 1.5,
        "spatial_role": "PROXY_GEOMETRY",
        "geometry_status": "VALID",
        "geometry": LineString([(number, 0), (number, 10)]),
    }


def _roads(*overrides: dict[str, object]) -> gpd.GeoDataFrame:
    mutations = overrides or ({},)
    rows: list[dict[str, object]] = []
    for number, mutation in enumerate(mutations, start=1):
        row = _base_row(number)
        row.update(mutation)
        rows.append(row)
    return gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:2154")


def _source() -> IgnBdTopoRoadData:
    return IgnBdTopoRoadData(
        extraction=cast(Any, None),
        road_segments=_roads(),
        road_segments_summary=cast(Any, None),
    )


def _apply(
    roads: gpd.GeoDataFrame,
    *,
    policy_path: Path | None = None,
) -> IgnRoadVehicleProxyApplicationResult:
    normalized = NormalizedIgnRoadData(road_segments=roads)
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ):
        return apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, policy_path
        )


def _row(
    overrides: dict[str, object] | None = None,
) -> pd.Series:
    result = _apply(_roads(overrides or {}))
    return result.roads.iloc[0]


def test_public_api_exports_only_stable_application_symbols() -> None:
    import landscout.stages.apply_road_vehicle_proxy_policy as module

    expected = {
        "IgnRoadVehicleProxyApplicationError",
        "IgnRoadVehicleProxyApplicationResult",
        "apply_ign_road_vehicle_proxy_policy",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_classify_road_frame")


def test_wrong_source_type_has_controlled_error() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(cast(Any, object()), SOURCE_CONFIG)


def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(_source(), cast(Any, object()))


def test_malformed_policy_path_has_controlled_error(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            return_value=NormalizedIgnRoadData(_roads()),
        ),
        pytest.raises(IgnRoadVehicleProxyApplicationError),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG, path)


def test_source_complete_normalization_is_invoked_exactly_once() -> None:
    normalized = NormalizedIgnRoadData(_roads())
    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ) as validator:
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    validator.assert_called_once()


def test_normalization_failure_stops_policy_loading() -> None:
    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            side_effect=IgnRoadNormalizationError("bad source"),
        ),
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy"
        ) as policy_loader,
        pytest.raises(IgnRoadVehicleProxyApplicationError),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    policy_loader.assert_not_called()


def test_generated_policy_column_collision_fails_before_policy_loading() -> None:
    roads = _roads()
    roads["road_proxy_class"] = "FORGED"

    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            return_value=NormalizedIgnRoadData(roads),
        ),
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy"
        ) as policy_loader,
        pytest.raises(IgnRoadVehicleProxyApplicationError, match="collide.*generated"),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    policy_loader.assert_not_called()


def test_normalized_facts_rows_index_crs_and_geometry_are_preserved() -> None:
    roads = _roads(
        {"nature_raw": "Chemin"},
        {"road_feature_id": "IGN_BDTOPO:ROAD_SEGMENT:SECOND"},
    )
    before = deepcopy(roads)

    result = _apply(roads).roads

    assert list(result.columns[: len(roads.columns)]) == list(roads.columns)
    assert list(result.columns[len(roads.columns) :]) == list(POLICY_COLUMNS)
    assert isinstance(result.index, pd.RangeIndex)
    assert result.index.equals(roads.index)
    assert result.crs == roads.crs
    assert result.active_geometry_name == roads.active_geometry_name
    assert result.geometry.to_wkb().equals(roads.geometry.to_wkb())
    assert_geodataframe_equal(result.loc[:, roads.columns], roads)
    assert_geodataframe_equal(roads, before)


def test_source_object_is_not_mutated() -> None:
    source = _source()
    before = deepcopy(source.road_segments)
    normalized = NormalizedIgnRoadData(_roads())

    with patch(
        "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
        return_value=normalized,
    ):
        apply_ign_road_vehicle_proxy_policy(source, SOURCE_CONFIG)

    assert_geodataframe_equal(source.road_segments, before)


@pytest.mark.parametrize(
    ("status", "geometry"),
    [
        ("NULL", None),
        ("EMPTY", LineString()),
        ("INVALID", LineString([(0, 0), (1, 1), (0, 1), (1, 0)])),
    ],
)
def test_non_valid_geometry_uses_technical_gate(status: str, geometry: object) -> None:
    row = _row({"geometry_status": status, "geometry": geometry})

    assert row.road_proxy_primary_rule == "SOURCE_GEOMETRY_NOT_VALID"
    assert row.road_proxy_class == "NOT_DISTANCE_PROXY"
    assert row.road_proxy_rule_trace_json == '["SOURCE_GEOMETRY_NOT_VALID"]'


def test_unknown_geometry_status_is_rejected() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        _apply(_roads({"geometry_status": "BROKEN"}))


@pytest.mark.parametrize(
    ("overrides", "rule", "expected_class"),
    [
        ({"fictitious_raw": True}, "FICTITIOUS_GEOMETRY", "NOT_DISTANCE_PROXY"),
        (
            {"asset_status_raw": "En projet"},
            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
            "NOT_DISTANCE_PROXY",
        ),
        (
            {"asset_status_raw": "En construction"},
            "NOT_IN_SERVICE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"light_vehicle_access_raw": "Physiquement impossible"},
            "PHYSICALLY_IMPOSSIBLE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"nature_raw": "Escalier"},
            "NON_GENERAL_VEHICLE_NATURE",
            "NOT_GENERAL_VEHICLE_PROXY",
        ),
        (
            {"light_vehicle_access_raw": "Restreint aux ayants droit"},
            "RIGHTS_RESTRICTED",
            "RESTRICTED_REVIEW",
        ),
        ({"private_raw": 1.0}, "PRIVATE_ROAD", "RESTRICTED_REVIEW"),
        (
            {"closure_period_raw": "Fermeture hivernale"},
            "TEMPORAL_CLOSURE",
            "RESTRICTED_REVIEW",
        ),
        (
            {"restriction_nature_raw": "Plot amovible"},
            "KNOWN_RESTRICTION",
            "RESTRICTED_REVIEW",
        ),
        (
            {"restriction_nature_raw": "Nouvelle restriction"},
            "OTHER_RECORDED_RESTRICTION",
            "RESTRICTED_REVIEW",
        ),
        (
            {"nature_raw": "Bac ou liaison maritime"},
            "SPECIAL_NATURE",
            "RESTRICTED_REVIEW",
        ),
        ({"nature_raw": "Chemin"}, "LIMITED_NATURE", "LIMITED_VEHICLE_PROXY"),
        ({"importance_raw": "6"}, "IMPORTANCE_6", "LIMITED_VEHICLE_PROXY"),
        (
            {"carriageway_width_raw": 2.8},
            "NARROW_CARRIAGEWAY",
            "LIMITED_VEHICLE_PROXY",
        ),
        ({}, "OPEN_OR_TOLL", "GENERAL_VEHICLE_PROXY"),
        ({"nature_raw": "Future"}, "UNKNOWN", "UNKNOWN_REVIEW"),
    ],
)
def test_each_policy_rule_selects_approved_outcome(
    overrides: dict[str, object], rule: str, expected_class: str
) -> None:
    row = _row(overrides)

    assert row.road_proxy_primary_rule == rule
    assert row.road_proxy_class == expected_class


@pytest.mark.parametrize(
    ("overrides", "rule"),
    [
        ({"fictitious_raw": True, "private_raw": 1.0}, "FICTITIOUS_GEOMETRY"),
        (
            {
                "asset_status_raw": "En projet",
                "light_vehicle_access_raw": "Physiquement impossible",
            },
            "PROJECT_GEOMETRY_NOT_SIGNIFICANT",
        ),
        (
            {
                "light_vehicle_access_raw": "Physiquement impossible",
                "private_raw": 1.0,
            },
            "PHYSICALLY_IMPOSSIBLE",
        ),
        ({"private_raw": 1.0, "carriageway_width_raw": 2.5}, "PRIVATE_ROAD"),
        (
            {"closure_period_raw": "Hiver", "nature_raw": "Chemin"},
            "TEMPORAL_CLOSURE",
        ),
        (
            {
                "restriction_nature_raw": "Plot amovible",
                "nature_raw": "Bac ou liaison maritime",
            },
            "KNOWN_RESTRICTION",
        ),
        ({"nature_raw": "Chemin", "importance_raw": "6"}, "LIMITED_NATURE"),
        (
            {"importance_raw": "6", "carriageway_width_raw": 2.5},
            "IMPORTANCE_6",
        ),
    ],
)
def test_policy_precedence_conflicts_select_first_rule(
    overrides: dict[str, object], rule: str
) -> None:
    assert _row(overrides).road_proxy_primary_rule == rule


@pytest.mark.parametrize(
    ("field", "value", "expected_rule"),
    [
        ("fictitious_raw", False, "OPEN_OR_TOLL"),
        ("fictitious_raw", np.bool_(True), "FICTITIOUS_GEOMETRY"),
        ("fictitious_raw", None, "UNKNOWN"),
        ("fictitious_raw", "true", "UNKNOWN"),
        ("private_raw", False, "OPEN_OR_TOLL"),
        ("private_raw", True, "PRIVATE_ROAD"),
        ("private_raw", 0, "OPEN_OR_TOLL"),
        ("private_raw", 1, "PRIVATE_ROAD"),
        ("private_raw", 0.0, "OPEN_OR_TOLL"),
        ("private_raw", 1.0, "PRIVATE_ROAD"),
        ("private_raw", None, "UNKNOWN"),
        ("private_raw", 2, "UNKNOWN"),
        ("private_raw", "1", "UNKNOWN"),
    ],
)
def test_boolean_like_source_values_are_parsed_without_coercion(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("asset_status_raw", "Future"),
        ("nature_raw", "Future"),
        ("light_vehicle_access_raw", "Future"),
        ("importance_raw", "7"),
        ("importance_raw", 6),
    ],
)
def test_unknown_critical_vocabulary_never_uses_general_fallback(
    field: str, value: object
) -> None:
    row = _row({field: value})

    assert row.road_proxy_primary_rule == "UNKNOWN"
    assert row.road_proxy_class == "UNKNOWN_REVIEW"
    assert field in row.road_proxy_unknown_fields_json


@pytest.mark.parametrize(
    ("value", "expected_rule"),
    [
        (None, "OPEN_OR_TOLL"),
        (float("nan"), "OPEN_OR_TOLL"),
        (2.9, "OPEN_OR_TOLL"),
        (2.899999, "NARROW_CARRIAGEWAY"),
        (0.0, "UNKNOWN"),
        (-1.0, "UNKNOWN"),
        (float("inf"), "UNKNOWN"),
        ("2.8", "UNKNOWN"),
        (True, "UNKNOWN"),
    ],
)
def test_width_contract(value: object, expected_rule: str) -> None:
    assert _row({"carriageway_width_raw": value}).road_proxy_primary_rule == (
        expected_rule
    )


@pytest.mark.parametrize(
    ("field", "value", "expected_rule"),
    [
        ("closure_period_raw", None, "OPEN_OR_TOLL"),
        ("closure_period_raw", "Hiver", "TEMPORAL_CLOSURE"),
        ("closure_period_raw", " ", "UNKNOWN"),
        ("closure_period_raw", 1, "UNKNOWN"),
        ("restriction_nature_raw", None, "OPEN_OR_TOLL"),
        ("restriction_nature_raw", "Plot amovible", "KNOWN_RESTRICTION"),
        (
            "restriction_nature_raw",
            "Restriction nouvelle",
            "OTHER_RECORDED_RESTRICTION",
        ),
        ("restriction_nature_raw", "", "UNKNOWN"),
        ("restriction_nature_raw", 1, "UNKNOWN"),
    ],
)
def test_optional_restriction_source_contract(
    field: str, value: object, expected_rule: str
) -> None:
    assert _row({field: value}).road_proxy_primary_rule == expected_rule


def test_every_configured_known_restriction_is_applied() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    for restriction in policy.known_restriction_review:
        assert (
            _row({"restriction_nature_raw": restriction}).road_proxy_primary_rule
            == "KNOWN_RESTRICTION"
        )


def test_general_fallback_requires_complete_positive_evidence_and_tracks_toll() -> None:
    open_row = _row()
    toll_row = _row({"light_vehicle_access_raw": "A péage"})

    assert open_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert not open_row.road_proxy_toll_evidence
    assert toll_row.road_proxy_class == "GENERAL_VEHICLE_PROXY"
    assert toll_row.road_proxy_toll_evidence


@pytest.mark.parametrize(
    "overrides",
    [
        {"nature_raw": "Future"},
        {"private_raw": None},
        {"importance_raw": "7"},
        {"carriageway_width_raw": "wide"},
    ],
)
def test_open_access_does_not_hide_unresolved_evidence(
    overrides: dict[str, object],
) -> None:
    assert _row(overrides).road_proxy_primary_rule == "UNKNOWN"


def test_trace_is_complete_unique_and_in_policy_order() -> None:
    row = _row(
        {
            "private_raw": 1.0,
            "closure_period_raw": "Hiver",
            "restriction_nature_raw": "Plot amovible",
            "nature_raw": "Chemin",
            "importance_raw": "6",
            "carriageway_width_raw": 2.0,
        }
    )
    expected = (
        '["PRIVATE_ROAD","TEMPORAL_CLOSURE","KNOWN_RESTRICTION",'
        '"LIMITED_NATURE","IMPORTANCE_6","NARROW_CARRIAGEWAY"]'
    )

    assert row.road_proxy_rule_trace_json == expected
    assert row.road_proxy_primary_rule == "PRIVATE_ROAD"


def test_known_higher_rule_remains_primary_while_unknown_is_traced() -> None:
    row = _row({"private_raw": 1.0, "importance_raw": "7"})

    assert row.road_proxy_primary_rule == "PRIVATE_ROAD"
    assert row.road_proxy_rule_trace_json == '["PRIVATE_ROAD","UNKNOWN"]'
    assert row.road_proxy_unknown_fields_json == '["importance_raw"]'


def test_unknown_fields_trace_is_fixed_and_deterministic() -> None:
    row = _row(
        {
            "fictitious_raw": None,
            "asset_status_raw": "Future",
            "nature_raw": "Future",
            "light_vehicle_access_raw": "Future",
            "private_raw": None,
            "importance_raw": "7",
            "carriageway_width_raw": "bad",
            "closure_period_raw": " ",
            "restriction_nature_raw": 1,
        }
    )
    assert row.road_proxy_unknown_fields_json == (
        '["fictitious_raw","asset_status_raw","nature_raw",'
        '"light_vehicle_access_raw","private_raw","importance_raw",'
        '"carriageway_width_raw","closure_period_raw",'
        '"restriction_nature_raw"]'
    )
    assert _row().road_proxy_unknown_fields_json == "[]"


def test_policy_lineage_is_exact_on_every_row() -> None:
    policy = load_ign_road_vehicle_proxy_policy()
    result = _apply(_roads({}, {})).roads

    assert set(result.road_proxy_policy_id) == {policy.policy_id}
    assert set(result.road_proxy_policy_schema_version) == {policy.schema_version}
    assert set(result.road_proxy_policy_config_sha256) == {policy.config_sha256}
    assert set(result.road_proxy_policy_scope) == {policy.scope}
    assert set(result.road_proxy_policy_evidence_checked_on) == {
        policy.evidence_checked_on
    }
    assert set(result.road_proxy_vehicle_scope) == {policy.vehicle_scope}
    assert set(result.road_proxy_heavy_vehicle_access) == {"NOT_PROVEN"}


def test_result_is_frozen_and_contains_no_unsafe_claim_vocabulary() -> None:
    result = _apply(_roads())
    forbidden = (
        "TRUCK_ACCESSIBLE",
        "LEGAL_ACCESS",
        "BESS_ACCESSIBLE",
        "AUTHORIZED",
        "APPROVED",
    )

    with pytest.raises(FrozenInstanceError):
        result.roads = _roads()  # type: ignore[misc]
    produced = " ".join(
        map(
            str,
            [*result.roads.columns, *result.roads.astype(str).to_numpy().ravel()],
        )
    )
    assert all(token not in produced for token in forbidden)


def test_valid_geometry_status_with_unsupported_geometry_is_not_repaired() -> None:
    polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])
    roads = _roads({"geometry": polygon})

    # The source-complete normalizer owns this geometry-kind rejection. The
    # application must propagate its controlled failure rather than repair it.
    with (
        patch(
            "landscout.stages.apply_road_vehicle_proxy_policy.normalize_ign_roads",
            side_effect=IgnRoadNormalizationError("unsupported geometry"),
        ),
        pytest.raises(IgnRoadVehicleProxyApplicationError),
    ):
        apply_ign_road_vehicle_proxy_policy(_source(), SOURCE_CONFIG)

    assert roads.geometry.iloc[0].equals_exact(polygon, tolerance=0)


def test_policy_path_must_be_path_or_none() -> None:
    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), SOURCE_CONFIG, cast(Any, str(POLICY_PATH))
        )


def test_source_config_is_exact_pydantic_type() -> None:
    class ConfigSubclass(IgnBdTopoSourceConfig):
        pass

    with pytest.raises(IgnRoadVehicleProxyApplicationError):
        apply_ign_road_vehicle_proxy_policy(
            _source(), ConfigSubclass.model_validate(SOURCE_CONFIG.model_dump())
        )
```
