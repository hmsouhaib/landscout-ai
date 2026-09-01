# `src/landscout/stages/enrich_road_proximity.py`

## File identity

- Repository path: `src/landscout/stages/enrich_road_proximity.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.
- Source SHA256: `8ebf75667fe539cb121ad0e9e1475abf442be82f61847771e91de2b5f1850439`

## 1. STEP 7F.1A.4 contract delta

- Ruff formatting only in STEP 7F.1A.4; executable contract, values, schemas, and test intent are unchanged. The companion is refreshed because its raw bytes and SHA changed.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import dataclass`
- `from numbers import Integral`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pandas.api.types import (  # type: ignore[import-untyped]
    is_bool_dtype,
    is_numeric_dtype,
)`
- `from pyproj import CRS`
- `from shapely import STRtree, force_2d`

### Internal LandScout imports

- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)`
- `from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "ParcelRoadProximityResult",
    "RoadProximityError",
    "RoadProxyClassCoverage",
    "enrich_parcel_road_proximity",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `ParcelRoadProximityResult`
  - `RoadProximityError`
  - `RoadProxyClassCoverage`
  - `enrich_parcel_road_proximity`

### `_PARCEL_STORAGE_CRS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_PARCEL_STORAGE_CRS = "EPSG:4326"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_CALCULATION_CRS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_CALCULATION_CRS = "EPSG:2154"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_PROXIMITY_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_PROXIMITY_SCOPE = "WITHIN_VERIFIED_SOURCE_PACKAGE"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_PARCEL_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_ROAD_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_ROAD_GEOMETRY_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_ROAD_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_ROAD_MATCH_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_ROAD_MATCH_COLUMNS = (
    "road_feature_id",
    "source_feature_id",
    "road_proxy_primary_rule",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "nature_raw",
    "importance_raw",
    "asset_status_raw",
    "private_raw",
    "light_vehicle_access_raw",
    "carriageway_width_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "source_layer",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `road_feature_id`
  - `source_feature_id`
  - `road_proxy_primary_rule`
  - `road_proxy_rule_trace_json`
  - `road_proxy_unknown_fields_json`
  - `road_proxy_toll_evidence`
  - `nature_raw`
  - `importance_raw`
  - `asset_status_raw`
  - `private_raw`
  - `light_vehicle_access_raw`
  - `carriageway_width_raw`
  - `closure_period_raw`
  - `restriction_nature_raw`
  - `source_layer`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `_ROAD_REQUIRED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_ROAD_REQUIRED_COLUMNS = frozenset(
    {
        *_ROAD_MATCH_COLUMNS,
        "geometry_status",
        "road_proxy_class",
        "road_proxy_policy_id",
        "road_proxy_policy_schema_version",
        "road_proxy_policy_config_sha256",
        "road_proxy_policy_scope",
        "road_proxy_heavy_vehicle_access",
        "geometry",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_MATCH_OUTPUT_MAPPING`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_MATCH_OUTPUT_MAPPING = {
    "distance_m": "nearest_road_proxy_distance_m",
    "road_feature_id": "nearest_road_feature_id",
    "source_feature_id": "nearest_source_feature_id",
    "tie_count": "nearest_road_tie_count",
    "road_proxy_primary_rule": "nearest_road_primary_rule",
    "road_proxy_rule_trace_json": "nearest_road_rule_trace_json",
    "road_proxy_unknown_fields_json": "nearest_road_unknown_fields_json",
    "road_proxy_toll_evidence": "nearest_road_toll_evidence",
    "nature_raw": "nearest_nature_raw",
    "importance_raw": "nearest_importance_raw",
    "asset_status_raw": "nearest_asset_status_raw",
    "private_raw": "nearest_private_raw",
    "light_vehicle_access_raw": "nearest_light_vehicle_access_raw",
    "carriageway_width_raw": "nearest_carriageway_width_raw",
    "closure_period_raw": "nearest_closure_period_raw",
    "restriction_nature_raw": "nearest_restriction_nature_raw",
    "source_layer": "nearest_source_layer",
    "source_department_code": "nearest_source_department_code",
    "source_edition": "nearest_source_edition",
    "source_archive_sha256": "nearest_source_archive_sha256",
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `distance_m`
  - `road_feature_id`
  - `source_feature_id`
  - `tie_count`
  - `road_proxy_primary_rule`
  - `road_proxy_rule_trace_json`
  - `road_proxy_unknown_fields_json`
  - `road_proxy_toll_evidence`
  - `nature_raw`
  - `importance_raw`
  - `asset_status_raw`
  - `private_raw`
  - `light_vehicle_access_raw`
  - `carriageway_width_raw`
  - `closure_period_raw`
  - `restriction_nature_raw`
  - `source_layer`
  - `source_department_code`
  - `source_edition`
  - `source_archive_sha256`

### `CLASS_PROXIMITY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
CLASS_PROXIMITY_COLUMNS = (
    "parcel_id",
    "road_proxy_class",
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
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_heavy_vehicle_access",
    "proximity_scope",
)
```

- Qualified consumers:
  - import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
  - value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `CLASS_PROXIMITY_COLUMNS`
  - value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `CLASS_PROXIMITY_COLUMNS`
  - import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)`
  - value/type reference: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `CLASS_PROXIMITY_COLUMNS`
  - value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_result_preserves_every_upstream_fact_and_input_object` via `CLASS_PROXIMITY_COLUMNS`
  - import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`
  - value/type reference: `tests.unit.test_enrich_road_proximity::test_output_shape_columns_and_order_are_deterministic` via `CLASS_PROXIMITY_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `road_proxy_class`
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
  - `road_proxy_policy_id`
  - `road_proxy_policy_schema_version`
  - `road_proxy_policy_config_sha256`
  - `road_proxy_heavy_vehicle_access`
  - `proximity_scope`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `RoadProximityError`

**Source purpose:** Raised when parcel-to-road proximity cannot be proven safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- constructor call: `landscout.stages.enrich_road_proximity::_validated_crs` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validated_crs` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_require_crs` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_require_crs` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_exact_ids` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_exact_ids` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_parcels` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_parcels` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_policy_classes` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_policy_classes` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_require_row_lineage` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_require_row_lineage` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_nearest_class_rows` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_nearest_class_rows` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_distance_and_ties` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_distance_and_ties` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_selected_evidence` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_selected_evidence` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_coverage` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_coverage` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_parcel_preservation` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_parcel_preservation` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::_validate_result` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_result` via `RoadProximityError`
- constructor call: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `RoadProximityError`
- value/type reference: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `RoadProximityError`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_type_has_controlled_error` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_road_source_type_has_controlled_error` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_source_config_type_has_controlled_error` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_policy_path_type_has_controlled_error` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_malformed_policy_stops_before_application` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_independent_policy_sha_mismatch_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_invalid_parcel_identity_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_id_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_parcel_columns_are_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_or_inactive_geometry_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_or_wrong_storage_crs_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_geometry_kind_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_bad_parcel_geometry_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_application_result_type_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_duplicate_road_feature_id_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_unknown_road_proxy_class_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_missing_road_policy_lineage_is_rejected` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_eligible_class_requires_valid_geometry_status` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_eligible_class_rejects_unsupported_geometry` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::_corrupt_nearest_output` via `RoadProximityError`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_policy_sha_mismatch_does_not_construct_spatial_index` via `RoadProximityError`

**Exact class source**

```python
class RoadProximityError(ValueError):
    """Raised when parcel-to-road proximity cannot be proven safely."""
```

### `RoadProxyClassCoverage`

**Source purpose:** Source coverage and distance eligibility for one policy class.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `road_proxy_class` | `str` | `required` | `road_proxy_class: str` |
| `feature_count` | `int` | `required` | `feature_count: int` |
| `distance_eligible` | `bool` | `required` | `distance_eligible: bool` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_class_coverage` via `RoadProxyClassCoverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_match_rows` via `RoadProxyClassCoverage`
- constructor call: `landscout.stages.enrich_road_proximity::_coverage` via `RoadProxyClassCoverage`
- value/type reference: `landscout.stages.enrich_road_proximity::_coverage` via `RoadProxyClassCoverage`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_coverage` via `RoadProxyClassCoverage`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `RoadProxyClassCoverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `RoadProxyClassCoverage`

**Exact class source**

```python
class RoadProxyClassCoverage:
    """Source coverage and distance eligibility for one policy class."""

    road_proxy_class: str
    feature_count: int
    distance_eligible: bool
```

### `ParcelRoadProximityResult`

**Source purpose:** Unchanged parcels plus class-specific factual road proximity.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |
| `class_proximity` | `pd.DataFrame` | `required` | `class_proximity: pd.DataFrame` |
| `class_coverage` | `tuple[RoadProxyClassCoverage, ...]` | `required` | `class_coverage: tuple[RoadProxyClassCoverage, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `ParcelRoadProximityResult`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `ParcelRoadProximityResult`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_result` via `ParcelRoadProximityResult`
- constructor call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `ParcelRoadProximityResult`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `ParcelRoadProximityResult`
- value/type reference: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `ParcelRoadProximityResult`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)`
- constructor call: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `ParcelRoadProximityResult`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_proximity` via `ParcelRoadProximityResult`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_without_match` via `ParcelRoadProximityResult`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`
- value/type reference: `tests.unit.test_enrich_road_proximity::_enrich` via `ParcelRoadProximityResult`
- value/type reference: `tests.unit.test_enrich_road_proximity::_row` via `ParcelRoadProximityResult`

**Exact class source**

```python
class ParcelRoadProximityResult:
    """Unchanged parcels plus class-specific factual road proximity."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_validated_crs`

**Purpose:** Implements `validated crs` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validated_crs(value: object, label: str) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `CRS.from_user_input(value)`
- Explicit raise paths:
  - `RoadProximityError(f"{label} CRS is required")` under lexical guard `value is None`.
  - `RoadProximityError(f"{label} CRS is unreadable")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_require_crs` via `_validated_crs`
- value/type reference: `landscout.stages.enrich_road_proximity::_require_crs` via `_validated_crs`
- direct call: `landscout.stages.enrich_road_proximity::_validate_parcel_preservation` via `_validated_crs`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_parcel_preservation` via `_validated_crs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |

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
def _validated_crs(value: object, label: str) -> CRS:
    if value is None:
        raise RoadProximityError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise RoadProximityError(f"{label} CRS is unreadable") from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_require_crs`

**Purpose:** Implements `require crs` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _require_crs(value: object, expected_epsg: int, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `expected_epsg` | positional-or-keyword | `int` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityError(f"{label} must use EPSG:{expected_epsg}")` under lexical guard `not actual.equals(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_parcels` via `_require_crs`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_parcels` via `_require_crs`
- direct call: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_require_crs`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_require_crs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_crs` | `landscout.stages.enrich_road_proximity._validated_crs` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `actual.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |

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
def _require_crs(value: object, expected_epsg: int, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityError(f"{label} must use EPSG:{expected_epsg}")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_exact_ids`

**Purpose:** Implements `validate exact ids` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_exact_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |
| `require_unique` | keyword-only | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityError(f"{label} values must not be null")` under lexical guard `values.isna().any()`.
  - `RoadProximityError(f"{label} values must be exact strings")` under lexical guard `any(not isinstance(value, str) for value in raw)`.
  - `RoadProximityError(f"{label} values must not be empty")` under lexical guard `any(not value.strip() for value in raw)`.
  - `RoadProximityError(f"{label} values must not have edge whitespace")` under lexical guard `any(value != value.strip() for value in raw)`.
  - `RoadProximityError(f"{label} values must be unique")` under lexical guard `require_unique and values.duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_parcels` via `_validate_exact_ids`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_parcels` via `_validate_exact_ids`
- direct call: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_validate_exact_ids`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_validate_exact_ids`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_exact_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise RoadProximityError(f"{label} values must not be null")
    raw = values.tolist()
    if any(not isinstance(value, str) for value in raw):
        raise RoadProximityError(f"{label} values must be exact strings")
    if any(not value.strip() for value in raw):
        raise RoadProximityError(f"{label} values must not be empty")
    if any(value != value.strip() for value in raw):
        raise RoadProximityError(f"{label} values must not have edge whitespace")
    if require_unique and values.duplicated().any():
        raise RoadProximityError(f"{label} values must be unique")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_parcels`

**Purpose:** Implements `validate parcels` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_parcels(parcels: object) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parcels`
- Explicit raise paths:
  - `RoadProximityError("parcels must be a GeoDataFrame")` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `RoadProximityError("Parcel columns must not contain duplicates")` under lexical guard `parcels.columns.duplicated().any()`.
  - `RoadProximityError(<br>            "Missing required parcel columns: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `RoadProximityError("Parcel geometry column must be active")` under lexical guard `parcels.active_geometry_name != "geometry"`.
  - `RoadProximityError("Parcel geometries must not be null")` under lexical guard `parcels.geometry.isna().any()`.
  - `RoadProximityError("Parcel geometries must not be empty")` under lexical guard `parcels.geometry.is_empty.any()`.
  - `RoadProximityError("Parcel geometries must be valid")` under lexical guard `not parcels.geometry.is_valid.all()`.
  - `RoadProximityError(<br>            "Parcel geometries must be Polygon or MultiPolygon; found: "<br>            + ", ".join(str(value) for value in unsupported)<br>        )` under lexical guard `unsupported`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_validate_parcels`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_validate_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `parcels.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_crs` | `landscout.stages.enrich_road_proximity._require_crs` |
| `_validate_exact_ids` | `landscout.stages.enrich_road_proximity._validate_exact_ids` |
| `parcels.geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.geometry.isna().any`<br>`parcels.geometry.isna`<br>`parcels.geometry.is_empty.any`<br>`parcels.geometry.is_valid.all`<br>`parcels.geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_parcels(parcels: object) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise RoadProximityError("parcels must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise RoadProximityError("Parcel columns must not contain duplicates")
    missing = {"parcel_id", "geometry"} - set(parcels.columns)
    if missing:
        raise RoadProximityError(
            "Missing required parcel columns: " + ", ".join(sorted(missing))
        )
    if parcels.active_geometry_name != "geometry":
        raise RoadProximityError("Parcel geometry column must be active")
    _require_crs(parcels.crs, 4326, "Parcel storage")
    _validate_exact_ids(parcels["parcel_id"], "parcel_id", require_unique=True)
    if parcels.geometry.isna().any():
        raise RoadProximityError("Parcel geometries must not be null")
    if parcels.geometry.is_empty.any():
        raise RoadProximityError("Parcel geometries must not be empty")
    if not parcels.geometry.is_valid.all():
        raise RoadProximityError("Parcel geometries must be valid")
    unsupported = sorted(
        set(parcels.geometry.geom_type.dropna()) - _PARCEL_GEOMETRY_TYPES
    )
    if unsupported:
        raise RoadProximityError(
            "Parcel geometries must be Polygon or MultiPolygon; found: "
            + ", ".join(str(value) for value in unsupported)
        )
    return parcels
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_classes`

**Purpose:** Implements `policy classes` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _policy_classes(
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[str, ...], tuple[str, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `all_classes, eligible`
- Explicit raise paths:
  - `RoadProximityError("Compiled road policy class domain is invalid")` under lexical guard `len(all_classes) != 6 or len(set(all_classes)) != 6`.
  - `RoadProximityError("Compiled road distance eligibility is invalid")` under lexical guard `len(eligible) != 5 or non_distance not in all_classes`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_policy_classes`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_policy_classes`
- direct call: `landscout.stages.enrich_road_proximity::_coverage` via `_policy_classes`
- value/type reference: `landscout.stages.enrich_road_proximity::_coverage` via `_policy_classes`
- direct call: `landscout.stages.enrich_road_proximity::_class_proximity_table` via `_policy_classes`
- value/type reference: `landscout.stages.enrich_road_proximity::_class_proximity_table` via `_policy_classes`
- direct call: `landscout.stages.enrich_road_proximity::_validate_coverage` via `_policy_classes`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_coverage` via `_policy_classes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _policy_classes(
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    all_classes = policy.classes.values
    if len(all_classes) != 6 or len(set(all_classes)) != 6:
        raise RoadProximityError("Compiled road policy class domain is invalid")
    non_distance = policy.classes.not_distance_proxy
    eligible = tuple(value for value in all_classes if value != non_distance)
    if len(eligible) != 5 or non_distance not in all_classes:
        raise RoadProximityError("Compiled road distance eligibility is invalid")
    return all_classes, eligible
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_require_row_lineage`

**Purpose:** Implements `require row lineage` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _require_row_lineage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityError(<br>                f"Road application policy lineage differs in {column}"<br>            )` under lexical guard `roads[column].isna().any() or not roads[column].eq(value).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_require_row_lineage`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_application_roads` via `_require_row_lineage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `expected.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads[column].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads[column].eq(value).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads[column].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |

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
def _require_row_lineage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> None:
    expected = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_policy_scope": policy.scope,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
    }
    for column, value in expected.items():
        if roads[column].isna().any() or not roads[column].eq(value).all():
            raise RoadProximityError(
                f"Road application policy lineage differs in {column}"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_application_roads`

**Purpose:** Implements `validate application roads` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_application_roads(
    application: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `application` | positional-or-keyword | `object` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `roads`
- Explicit raise paths:
  - `RoadProximityError("Road application result type is invalid")` under lexical guard `type(application) is not IgnRoadVehicleProxyApplicationResult`.
  - `RoadProximityError("Road application roads must be a GeoDataFrame")` under lexical guard `not isinstance(roads, gpd.GeoDataFrame)`.
  - `RoadProximityError("Road application columns must not be duplicated")` under lexical guard `roads.columns.duplicated().any()`.
  - `RoadProximityError(<br>            "Missing road application column or lineage: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `RoadProximityError("Road application geometry must be active")` under lexical guard `roads.active_geometry_name != "geometry"`.
  - `RoadProximityError("Road application has an unknown proxy class")` under lexical guard `classes.isna().any() or not classes.isin(all_classes).all()`.
  - `RoadProximityError("Road application geometry status is invalid")` under lexical guard `statuses.isna().any() or not statuses.isin(_ROAD_GEOMETRY_STATUSES).all()`.
  - `RoadProximityError(<br>            "Distance-eligible roads must have VALID geometry status"<br>        )` under lexical guard `not statuses.loc[eligible].eq("VALID").all()`.
  - `RoadProximityError("Distance-eligible road geometry must not be null")` under lexical guard `eligible_geometry.isna().any()`.
  - `RoadProximityError("Distance-eligible road geometry must not be empty")` under lexical guard `eligible_geometry.is_empty.any()`.
  - `RoadProximityError("Distance-eligible road geometry must be valid")` under lexical guard `not eligible_geometry.is_valid.all()`.
  - `RoadProximityError(<br>            "Distance-eligible geometry must be LineString or MultiLineString; found: "<br>            + ", ".join(str(value) for value in unsupported)<br>        )` under lexical guard `unsupported`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_validate_application_roads`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_validate_application_roads`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_crs` | `landscout.stages.enrich_road_proximity._require_crs` |
| `_validate_exact_ids` | `landscout.stages.enrich_road_proximity._validate_exact_ids` |
| `_policy_classes` | `landscout.stages.enrich_road_proximity._policy_classes` |
| `classes.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `classes.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `classes.isin(all_classes).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `classes.isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `_require_row_lineage` | `landscout.stages.enrich_road_proximity._require_row_lineage` |
| `statuses.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isin(_ROAD_GEOMETRY_STATUSES).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.loc[eligible].eq("VALID").all` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.loc[eligible].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `eligible_geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `eligible_geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `eligible_geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `eligible_geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `eligible_geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `statuses.isin(_ROAD_GEOMETRY_STATUSES).all`<br>`eligible_geometry.isna().any`<br>`eligible_geometry.isna`<br>`eligible_geometry.is_empty.any`<br>`eligible_geometry.is_valid.all`<br>`eligible_geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_application_roads(
    application: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
    if type(application) is not IgnRoadVehicleProxyApplicationResult:
        raise RoadProximityError("Road application result type is invalid")
    roads = application.roads
    if not isinstance(roads, gpd.GeoDataFrame):
        raise RoadProximityError("Road application roads must be a GeoDataFrame")
    if roads.columns.duplicated().any():
        raise RoadProximityError("Road application columns must not be duplicated")
    missing = _ROAD_REQUIRED_COLUMNS - set(roads.columns)
    if missing:
        raise RoadProximityError(
            "Missing road application column or lineage: " + ", ".join(sorted(missing))
        )
    if roads.active_geometry_name != "geometry":
        raise RoadProximityError("Road application geometry must be active")
    _require_crs(roads.crs, 2154, "Road application")
    _validate_exact_ids(
        roads["road_feature_id"], "road_feature_id", require_unique=True
    )
    _validate_exact_ids(
        roads["source_feature_id"], "source_feature_id", require_unique=False
    )

    all_classes, eligible_classes = _policy_classes(policy)
    classes = roads["road_proxy_class"]
    if classes.isna().any() or not classes.isin(all_classes).all():
        raise RoadProximityError("Road application has an unknown proxy class")
    _require_row_lineage(roads, policy)

    statuses = roads["geometry_status"]
    if statuses.isna().any() or not statuses.isin(_ROAD_GEOMETRY_STATUSES).all():
        raise RoadProximityError("Road application geometry status is invalid")
    eligible = classes.isin(eligible_classes)
    if not statuses.loc[eligible].eq("VALID").all():
        raise RoadProximityError(
            "Distance-eligible roads must have VALID geometry status"
        )
    eligible_geometry = roads.loc[eligible, "geometry"]
    if eligible_geometry.isna().any():
        raise RoadProximityError("Distance-eligible road geometry must not be null")
    if eligible_geometry.is_empty.any():
        raise RoadProximityError("Distance-eligible road geometry must not be empty")
    if not eligible_geometry.is_valid.all():
        raise RoadProximityError("Distance-eligible road geometry must be valid")
    unsupported = sorted(
        set(eligible_geometry.geom_type.dropna()) - _ROAD_GEOMETRY_TYPES
    )
    if unsupported:
        raise RoadProximityError(
            "Distance-eligible geometry must be LineString or MultiLineString; found: "
            + ", ".join(str(value) for value in unsupported)
        )
    return roads
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_calculation_geometries`

**Purpose:** Implements `calculation geometries` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
```

- Exact decorators: none.
- Declared return annotation: `np.ndarray`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `np.asarray(force_2d(values), dtype=object)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_nearest_class_rows` via `_calculation_geometries`
- value/type reference: `landscout.stages.enrich_road_proximity::_nearest_class_rows` via `_calculation_geometries`
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_calculation_geometries`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_calculation_geometries`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `np.asarray` | `numpy.asarray` |
| `force_2d` | `shapely.force_2d` |

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
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_empty_nearest_rows`

**Purpose:** Implements `empty nearest rows` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _empty_nearest_rows(parcel_count: int) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_count` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_nearest_class_rows` via `_empty_nearest_rows`
- value/type reference: `landscout.stages.enrich_road_proximity::_nearest_class_rows` via `_empty_nearest_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `pd.RangeIndex` | `pandas.RangeIndex` |
| `pd.Series` | `pandas.Series` |

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
| In-memory mutation | `output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")`<br>`output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")`<br>`output[column] = pd.Series(pd.NA, index=output.index, dtype="boolean")`<br>`output[column] = pd.Series(pd.NA, index=output.index, dtype="object")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _empty_nearest_rows(parcel_count: int) -> pd.DataFrame:
    output = pd.DataFrame(index=pd.RangeIndex(parcel_count))
    output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")
    output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")
    for column in _ROAD_MATCH_COLUMNS:
        if column == "road_proxy_toll_evidence":
            output[column] = pd.Series(pd.NA, index=output.index, dtype="boolean")
        else:
            output[column] = pd.Series(pd.NA, index=output.index, dtype="object")
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_nearest_class_rows`

**Purpose:** Implements `nearest class rows` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _nearest_class_rows(
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_geometries` | positional-or-keyword | `np.ndarray` | `required` |
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_empty_nearest_rows(parcel_count)`
  - `output`
- Explicit raise paths:
  - `RoadProximityError("Nearest-road matching did not cover every parcel")` under lexical guard `selected["parcel_position"].tolist() != list(range(parcel_count))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_class_proximity_table` via `_nearest_class_rows`
- value/type reference: `landscout.stages.enrich_road_proximity::_class_proximity_table` via `_nearest_class_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_empty_nearest_rows` | `landscout.stages.enrich_road_proximity._empty_nearest_rows` |
| `STRtree` | `shapely.STRtree` |
| `_calculation_geometries` | `landscout.stages.enrich_road_proximity._calculation_geometries` |
| `tree.query_nearest` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `roads.iloc[matches["road_position"].to_numpy()][<br>        "road_feature_id"<br>    ].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches["road_position"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.groupby("parcel_position", sort=False).size` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.drop_duplicates("parcel_position", keep="first").sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `matches.drop_duplicates` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["parcel_position"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `selected["road_position"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_rows.loc[:, list(_ROAD_MATCH_COLUMNS)].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.insert` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `ties.reindex(range(parcel_count)).to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `ties.reindex` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["distance_m"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `selected["distance_m"].to_numpy` |
| External process/environment | None directly present. |
| In-memory mutation | `matches["road_feature_id"] = roads.iloc[matches["road_position"].to_numpy()][<br>        "road_feature_id"<br>    ].to_numpy()`<br>`output.insert(<br>        0,<br>        "tie_count",<br>        pd.Series(ties.reindex(range(parcel_count)).to_numpy(), dtype="Int64"),<br>    )`<br>`output.insert(<br>        0,<br>        "distance_m",<br>        selected["distance_m"].to_numpy(dtype="float64"),<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _nearest_class_rows(
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
) -> pd.DataFrame:
    parcel_count = len(parcel_geometries)
    if roads.empty:
        return _empty_nearest_rows(parcel_count)

    tree = STRtree(_calculation_geometries(roads))
    indices, distances = tree.query_nearest(
        parcel_geometries,
        all_matches=True,
        return_distance=True,
    )
    matches = pd.DataFrame(
        {
            "parcel_position": indices[0],
            "road_position": indices[1],
            "distance_m": distances,
        }
    )
    matches["road_feature_id"] = roads.iloc[matches["road_position"].to_numpy()][
        "road_feature_id"
    ].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "road_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position", kind="mergesort"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise RoadProximityError("Nearest-road matching did not cover every parcel")

    source_rows = roads.iloc[selected["road_position"].to_numpy()]
    output = source_rows.loc[:, list(_ROAD_MATCH_COLUMNS)].reset_index(drop=True)
    output.insert(
        0,
        "tie_count",
        pd.Series(ties.reindex(range(parcel_count)).to_numpy(), dtype="Int64"),
    )
    output.insert(
        0,
        "distance_m",
        selected["distance_m"].to_numpy(dtype="float64"),
    )
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_coverage`

**Purpose:** Implements `coverage` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _coverage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[RoadProxyClassCoverage, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[RoadProxyClassCoverage, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        RoadProxyClassCoverage(<br>            road_proxy_class=road_class,<br>            feature_count=int(counts.get(road_class, 0)),<br>            distance_eligible=road_class in eligible_classes,<br>        )<br>        for road_class in all_classes<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_coverage`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_policy_classes` | `landscout.stages.enrich_road_proximity._policy_classes` |
| `roads["road_proxy_class"].value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProxyClassCoverage` | `landscout.stages.enrich_road_proximity.RoadProxyClassCoverage` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `counts.get` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _coverage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[RoadProxyClassCoverage, ...]:
    all_classes, eligible_classes = _policy_classes(policy)
    counts = roads["road_proxy_class"].value_counts()
    return tuple(
        RoadProxyClassCoverage(
            road_proxy_class=road_class,
            feature_count=int(counts.get(road_class, 0)),
            distance_eligible=road_class in eligible_classes,
        )
        for road_class in all_classes
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_class_proximity_table`

**Purpose:** Implements `class proximity table` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _class_proximity_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_ids` | positional-or-keyword | `pd.Series` | `required` |
| `parcel_geometries` | positional-or-keyword | `np.ndarray` | `required` |
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_class_proximity_table`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_class_proximity_table`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_policy_classes` | `landscout.stages.enrich_road_proximity._policy_classes` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.loc[roads["road_proxy_class"].eq(road_class)].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads["road_proxy_class"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_nearest_class_rows` | `landscout.stages.enrich_road_proximity._nearest_class_rows` |
| `_validate_distance_and_ties` | `landscout.stages.enrich_road_proximity._validate_distance_and_ties` |
| `nearest.rename` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `np.arange` | `numpy.arange` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_ids.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_MATCH_OUTPUT_MAPPING.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `nearest[source_column].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `tables.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `output.sort_values(<br>        ["_parcel_position", "_class_position"], kind="mergesort"<br>    ).reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `output[<br>        "nearest_road_proxy_distance_m"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["nearest_road_tie_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["nearest_road_toll_evidence"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_validate_distance_and_ties`<br>`output[<br>        "nearest_road_proxy_distance_m"<br>    ].astype` |
| External process/environment | None directly present. |
| In-memory mutation | `nearest.rename(<br>                columns={<br>                    "distance_m": "nearest_road_proxy_distance_m",<br>                    "tie_count": "nearest_road_tie_count",<br>                }<br>            )`<br>`table[output_column] = nearest[source_column].reset_index(drop=True)`<br>`table["road_proxy_policy_id"] = policy.policy_id`<br>`table["road_proxy_policy_schema_version"] = policy.schema_version`<br>`table["road_proxy_policy_config_sha256"] = policy.config_sha256`<br>`table["road_proxy_heavy_vehicle_access"] = policy.heavy_vehicle_access`<br>`table["proximity_scope"] = _PROXIMITY_SCOPE`<br>`tables.append(table)`<br>`output.drop(columns=["_parcel_position", "_class_position"])`<br>`output["nearest_road_proxy_distance_m"] = output[<br>        "nearest_road_proxy_distance_m"<br>    ].astype("float64")`<br>`output["nearest_road_tie_count"] = output["nearest_road_tie_count"].astype("Int64")`<br>`output["nearest_road_toll_evidence"] = output["nearest_road_toll_evidence"].astype(<br>        "boolean"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _class_proximity_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> pd.DataFrame:
    _, eligible_classes = _policy_classes(policy)
    tables: list[pd.DataFrame] = []
    for class_position, road_class in enumerate(eligible_classes):
        class_roads = roads.loc[roads["road_proxy_class"].eq(road_class)].reset_index(
            drop=True
        )
        nearest = _nearest_class_rows(parcel_geometries, class_roads)
        _validate_distance_and_ties(
            nearest.rename(
                columns={
                    "distance_m": "nearest_road_proxy_distance_m",
                    "tie_count": "nearest_road_tie_count",
                }
            ),
            expect_matches=not class_roads.empty,
        )
        table = pd.DataFrame(
            {
                "_parcel_position": np.arange(len(parcel_ids), dtype="int64"),
                "_class_position": class_position,
                "parcel_id": parcel_ids.reset_index(drop=True),
                "road_proxy_class": road_class,
            }
        )
        for source_column, output_column in _MATCH_OUTPUT_MAPPING.items():
            table[output_column] = nearest[source_column].reset_index(drop=True)
        table["road_proxy_policy_id"] = policy.policy_id
        table["road_proxy_policy_schema_version"] = policy.schema_version
        table["road_proxy_policy_config_sha256"] = policy.config_sha256
        table["road_proxy_heavy_vehicle_access"] = policy.heavy_vehicle_access
        table["proximity_scope"] = _PROXIMITY_SCOPE
        tables.append(table)

    output = pd.concat(tables, ignore_index=True)
    output = output.sort_values(
        ["_parcel_position", "_class_position"], kind="mergesort"
    ).reset_index(drop=True)
    output = output.drop(columns=["_parcel_position", "_class_position"])
    output["nearest_road_proxy_distance_m"] = output[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    output["nearest_road_tie_count"] = output["nearest_road_tie_count"].astype("Int64")
    output["nearest_road_toll_evidence"] = output["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    return output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_missing_scalar`

**Purpose:** Implements `is missing scalar` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _is_missing_scalar(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `True`
  - `bool(pd.isna(value))`
  - `False`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_distance_and_ties` via `_is_missing_scalar`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_distance_and_ties` via `_is_missing_scalar`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |

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
def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_distance_and_ties`

**Purpose:** Implements `validate distance and ties` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_distance_and_ties(
    rows: pd.DataFrame,
    *,
    expect_matches: bool,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `rows` | positional-or-keyword | `pd.DataFrame` | `required` |
| `expect_matches` | keyword-only | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityError("Non-empty road classes require parcel matches")` under lexical guard `expect_matches and not matched.all()`.
  - `RoadProximityError("Empty road classes must not contain matches")` under lexical guard `not expect_matches and matched.any()`.
  - `RoadProximityError("Matched road distances must be numeric")` under lexical guard `matched.any()`.
  - `RoadProximityError("Matched road distances must be finite and >= 0")` under lexical guard `matched.any()`.
  - `RoadProximityError("Unmatched rows require null tie_count")` under lexical guard `not row_matched`.
  - `RoadProximityError(<br>                "Matched nearest_road_tie_count must be an integer >= 1"<br>            )` under lexical guard `missing<br>            or not isinstance(value, Integral)<br>            or isinstance(value, (bool, np.bool_))<br>            or int(value) < 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_class_proximity_table` via `_validate_distance_and_ties`
- value/type reference: `landscout.stages.enrich_road_proximity::_class_proximity_table` via `_validate_distance_and_ties`
- direct call: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_distance_and_ties`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_distance_and_ties`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `distances.notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `matched.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `is_numeric_dtype` | `pandas.api.types.is_numeric_dtype` |
| `is_bool_dtype` | `pandas.api.types.is_bool_dtype` |
| `distances.loc[matched].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite(numeric).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(numeric < 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `ties.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_missing_scalar` | `landscout.stages.enrich_road_proximity._is_missing_scalar` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `distances.notna`<br>`distances.loc[matched].to_numpy` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_distance_and_ties(
    rows: pd.DataFrame,
    *,
    expect_matches: bool,
) -> None:
    distances = rows["nearest_road_proxy_distance_m"]
    matched = distances.notna()
    if expect_matches and not matched.all():
        raise RoadProximityError("Non-empty road classes require parcel matches")
    if not expect_matches and matched.any():
        raise RoadProximityError("Empty road classes must not contain matches")
    if matched.any():
        if not is_numeric_dtype(distances.dtype) or is_bool_dtype(distances.dtype):
            raise RoadProximityError("Matched road distances must be numeric")
        numeric = distances.loc[matched].to_numpy(dtype="float64")
        if not np.isfinite(numeric).all() or (numeric < 0).any():
            raise RoadProximityError("Matched road distances must be finite and >= 0")

    ties = rows["nearest_road_tie_count"]
    for value, row_matched in zip(
        ties.tolist(), matched.to_numpy(dtype=bool), strict=True
    ):
        missing = _is_missing_scalar(value)
        if not row_matched:
            if not missing:
                raise RoadProximityError("Unmatched rows require null tie_count")
            continue
        if (
            missing
            or not isinstance(value, Integral)
            or isinstance(value, (bool, np.bool_))
            or int(value) < 1
        ):
            raise RoadProximityError(
                "Matched nearest_road_tie_count must be an integer >= 1"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_safe_equal`

**Purpose:** Implements `null safe equal` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _null_safe_equal(actual: pd.Series, expected: pd.Series) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `actual` | positional-or-keyword | `pd.Series` | `required` |
| `expected` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `False`
  - `bool((both_null \| equal).all())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_selected_evidence` via `_null_safe_equal`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_selected_evidence` via `_null_safe_equal`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `left.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `right.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `left.eq(right).fillna` | `unresolved local/third-party receiver; no ownership inferred` |
| `left.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `(both_null \| equal).all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _null_safe_equal(actual: pd.Series, expected: pd.Series) -> bool:
    left = actual.reset_index(drop=True)
    right = expected.reset_index(drop=True)
    if len(left) != len(right):
        return False
    both_null = left.isna() & right.isna()
    try:
        equal = left.eq(right).fillna(False)
    except (TypeError, ValueError):
        return False
    return bool((both_null | equal).all())
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_selected_evidence`

**Purpose:** Implements `validate selected evidence` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_selected_evidence(
    table: pd.DataFrame,
    roads: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `table` | positional-or-keyword | `pd.DataFrame` | `required` |
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- Explicit raise paths:
  - `RoadProximityError("Selected nearest road ID is absent from source")` under lexical guard `(positions < 0).any()`.
  - `RoadProximityError("Selected nearest road has the wrong proxy class")` under lexical guard `not selected["road_proxy_class"]<br>        .reset_index(drop=True)<br>        .eq(expected["road_proxy_class"])<br>        .all()`.
  - `RoadProximityError(<br>                f"Selected nearest road evidence differs for {output_column}"<br>            )` under lexical guard `not _null_safe_equal(selected[output_column], expected[source_column])`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_selected_evidence`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_selected_evidence`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `table["nearest_road_feature_id"].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.loc[matched].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `roads.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `lookup.index.get_indexer` | `unresolved local/third-party receiver; no ownership inferred` |
| `(positions < 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `lookup.iloc[positions].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["road_proxy_class"]<br>        .reset_index(drop=True)<br>        .eq(expected["road_proxy_class"])<br>        .all` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["road_proxy_class"]<br>        .reset_index(drop=True)<br>        .eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected["road_proxy_class"]<br>        .reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_MATCH_OUTPUT_MAPPING.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_equal` | `landscout.stages.enrich_road_proximity._null_safe_equal` |

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
def _validate_selected_evidence(
    table: pd.DataFrame,
    roads: gpd.GeoDataFrame,
) -> None:
    matched = table["nearest_road_feature_id"].notna()
    selected = table.loc[matched].reset_index(drop=True)
    if selected.empty:
        return
    lookup = roads.set_index("road_feature_id", drop=False)
    positions = lookup.index.get_indexer(selected["nearest_road_feature_id"])
    if (positions < 0).any():
        raise RoadProximityError("Selected nearest road ID is absent from source")
    expected = lookup.iloc[positions].reset_index(drop=True)
    if (
        not selected["road_proxy_class"]
        .reset_index(drop=True)
        .eq(expected["road_proxy_class"])
        .all()
    ):
        raise RoadProximityError("Selected nearest road has the wrong proxy class")

    for source_column, output_column in _MATCH_OUTPUT_MAPPING.items():
        if source_column in {"distance_m", "tie_count"}:
            continue
        if not _null_safe_equal(selected[output_column], expected[source_column]):
            raise RoadProximityError(
                f"Selected nearest road evidence differs for {output_column}"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_coverage`

**Purpose:** Implements `validate coverage` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_coverage(
    coverage: tuple[RoadProxyClassCoverage, ...],
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coverage` | positional-or-keyword | `tuple[RoadProxyClassCoverage, ...]` | `required` |
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `eligible_classes`
- Explicit raise paths:
  - `RoadProximityError("Road class coverage is incomplete")` under lexical guard `type(coverage) is not tuple or len(coverage) != len(all_classes)`.
  - `RoadProximityError("Road class coverage entry type is invalid")` under lexical guard `type(item) is not RoadProxyClassCoverage`.
  - `RoadProximityError("Road class coverage order is invalid")` under lexical guard `item.road_proxy_class != road_class`.
  - `RoadProximityError("Road class feature_count must be an integer >= 0")` under lexical guard `type(item.feature_count) is not int or item.feature_count < 0`.
  - `RoadProximityError("Road class distance_eligible must be Boolean")` under lexical guard `type(item.distance_eligible) is not bool`.
  - `RoadProximityError("Road class distance eligibility is invalid")` under lexical guard `item.distance_eligible != (road_class in eligible_classes)`.
  - `RoadProximityError("Road class feature_count differs from source")` under lexical guard `item.feature_count != int(counts.get(road_class, 0))`.
  - `RoadProximityError("Road class coverage does not sum to source rows")` under lexical guard `total != len(roads)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_coverage`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_policy_classes` | `landscout.stages.enrich_road_proximity._policy_classes` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `roads["road_proxy_class"].value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `counts.get` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_coverage(
    coverage: tuple[RoadProxyClassCoverage, ...],
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
    all_classes, eligible_classes = _policy_classes(policy)
    if type(coverage) is not tuple or len(coverage) != len(all_classes):
        raise RoadProximityError("Road class coverage is incomplete")
    counts = roads["road_proxy_class"].value_counts()
    total = 0
    for position, item in enumerate(coverage):
        if type(item) is not RoadProxyClassCoverage:
            raise RoadProximityError("Road class coverage entry type is invalid")
        road_class = all_classes[position]
        if item.road_proxy_class != road_class:
            raise RoadProximityError("Road class coverage order is invalid")
        if type(item.feature_count) is not int or item.feature_count < 0:
            raise RoadProximityError("Road class feature_count must be an integer >= 0")
        if type(item.distance_eligible) is not bool:
            raise RoadProximityError("Road class distance_eligible must be Boolean")
        if item.distance_eligible != (road_class in eligible_classes):
            raise RoadProximityError("Road class distance eligibility is invalid")
        if item.feature_count != int(counts.get(road_class, 0)):
            raise RoadProximityError("Road class feature_count differs from source")
        total += item.feature_count
    if total != len(roads):
        raise RoadProximityError("Road class coverage does not sum to source rows")
    return eligible_classes
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_parcel_preservation`

**Purpose:** Implements `validate parcel preservation` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_parcel_preservation(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `output` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityError("Road proximity changed parcel count")` under lexical guard `len(output) != len(source)`.
  - `RoadProximityError("Road proximity changed parcel columns")` under lexical guard `list(output.columns) != list(source.columns)`.
  - `RoadProximityError("Road proximity changed parcel dtypes")` under lexical guard `not output.dtypes.equals(source.dtypes)`.
  - `RoadProximityError("Road proximity changed parcel index metadata")` under lexical guard `type(output.index) is not type(source.index)<br>        or output.index.names != source.index.names<br>        or str(output.index.dtype) != str(source.index.dtype)<br>        or not output.index.equals(source.index)`.
  - `RoadProximityError("Road proximity changed parcel CRS")` under lexical guard `not _validated_crs(output.crs, "Output parcel").equals(<br>        _validated_crs(source.crs, "Source parcel")<br>    )`.
  - `RoadProximityError("Road proximity changed parcel geometry WKB")` under lexical guard `not output.geometry.to_wkb().equals(source.geometry.to_wkb())`.
  - `RoadProximityError("Road proximity changed parcel facts")` under lexical guard `geometry_column is None or not output.drop(columns=geometry_column).equals(<br>        source.drop(columns=geometry_column)<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_parcel_preservation`
- value/type reference: `landscout.stages.enrich_road_proximity::_validate_result` via `_validate_parcel_preservation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.dtypes.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_crs(output.crs, "Output parcel").equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_crs` | `landscout.stages.enrich_road_proximity._validated_crs` |
| `output.geometry.to_wkb().equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `source.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.drop(columns=geometry_column).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `source.drop` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `output.geometry.to_wkb().equals`<br>`output.geometry.to_wkb`<br>`source.geometry.to_wkb`<br>`output.drop(columns=geometry_column).equals` |
| External process/environment | None directly present. |
| In-memory mutation | `output.drop(columns=geometry_column)`<br>`source.drop(columns=geometry_column)` |
| Direct parameter mutation | `output.drop(columns=geometry_column)`<br>`source.drop(columns=geometry_column)` |

**Complete source-ordered implementation**

```python
def _validate_parcel_preservation(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
) -> None:
    if len(output) != len(source):
        raise RoadProximityError("Road proximity changed parcel count")
    if list(output.columns) != list(source.columns):
        raise RoadProximityError("Road proximity changed parcel columns")
    if not output.dtypes.equals(source.dtypes):
        raise RoadProximityError("Road proximity changed parcel dtypes")
    if (
        type(output.index) is not type(source.index)
        or output.index.names != source.index.names
        or str(output.index.dtype) != str(source.index.dtype)
        or not output.index.equals(source.index)
    ):
        raise RoadProximityError("Road proximity changed parcel index metadata")
    if not _validated_crs(output.crs, "Output parcel").equals(
        _validated_crs(source.crs, "Source parcel")
    ):
        raise RoadProximityError("Road proximity changed parcel CRS")
    if not output.geometry.to_wkb().equals(source.geometry.to_wkb()):
        raise RoadProximityError("Road proximity changed parcel geometry WKB")
    geometry_column = source.active_geometry_name
    if geometry_column is None or not output.drop(columns=geometry_column).equals(
        source.drop(columns=geometry_column)
    ):
        raise RoadProximityError("Road proximity changed parcel facts")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result`

**Purpose:** Implements `validate result` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _validate_result(
    source_parcels: gpd.GeoDataFrame,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
    result: ParcelRoadProximityResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `roads` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |
| `result` | positional-or-keyword | `ParcelRoadProximityResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityError("Road proximity result type is invalid")` under lexical guard `type(result) is not ParcelRoadProximityResult`.
  - `RoadProximityError("Road proximity parcels must be a GeoDataFrame")` under lexical guard `not isinstance(result.parcels, gpd.GeoDataFrame)`.
  - `RoadProximityError("Class proximity must be a plain DataFrame")` under lexical guard `type(result.class_proximity) is not pd.DataFrame`.
  - `RoadProximityError("Class proximity schema is invalid")` under lexical guard `table.columns.duplicated().any() or list(table.columns) != list(<br>        CLASS_PROXIMITY_COLUMNS<br>    )`.
  - `RoadProximityError("Class proximity row count is invalid")` under lexical guard `len(table) != len(source_parcels) * len(eligible_classes)`.
  - `RoadProximityError("Class proximity parcel order is invalid")` under lexical guard `table["parcel_id"].tolist() != expected_ids`.
  - `RoadProximityError("Class proximity class order is invalid")` under lexical guard `table["road_proxy_class"].tolist() != expected_classes`.
  - `RoadProximityError("NOT_DISTANCE_PROXY cannot have distance rows")` under lexical guard `policy.classes.not_distance_proxy in set(table["road_proxy_class"])`.
  - `RoadProximityError("Class proximity parcel/class pairs must be unique")` under lexical guard `table.duplicated(["parcel_id", "road_proxy_class"]).any()`.
  - `RoadProximityError(f"Matched class rows require {column}")` under lexical guard `expect_matches`.
  - `RoadProximityError(<br>                "Empty-class selected road evidence must be entirely null"<br>            )` under lexical guard `expect_matches`.
  - `RoadProximityError(f"Class proximity lineage differs in {column}")` under lexical guard `table[column].isna().any() or not table[column].eq(value).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_validate_result`
- value/type reference: `landscout.stages.enrich_road_proximity::_enrich_parcel_road_proximity` via `_validate_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_parcel_preservation` | `landscout.stages.enrich_road_proximity._validate_parcel_preservation` |
| `_validate_coverage` | `landscout.stages.enrich_road_proximity._validate_coverage` |
| `table.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["road_proxy_class"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.duplicated(["parcel_id", "road_proxy_class"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["road_proxy_class"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_distance_and_ties` | `landscout.stages.enrich_road_proximity._validate_distance_and_ties` |
| `rows[column].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `_MATCH_OUTPUT_MAPPING.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_lineage.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].eq(value).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_selected_evidence` | `landscout.stages.enrich_road_proximity._validate_selected_evidence` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_validate_distance_and_ties` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_result(
    source_parcels: gpd.GeoDataFrame,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
    result: ParcelRoadProximityResult,
) -> None:
    if type(result) is not ParcelRoadProximityResult:
        raise RoadProximityError("Road proximity result type is invalid")
    if not isinstance(result.parcels, gpd.GeoDataFrame):
        raise RoadProximityError("Road proximity parcels must be a GeoDataFrame")
    if type(result.class_proximity) is not pd.DataFrame:
        raise RoadProximityError("Class proximity must be a plain DataFrame")
    _validate_parcel_preservation(source_parcels, result.parcels)
    eligible_classes = _validate_coverage(result.class_coverage, roads, policy)
    table = result.class_proximity
    if table.columns.duplicated().any() or list(table.columns) != list(
        CLASS_PROXIMITY_COLUMNS
    ):
        raise RoadProximityError("Class proximity schema is invalid")
    if len(table) != len(source_parcels) * len(eligible_classes):
        raise RoadProximityError("Class proximity row count is invalid")
    expected_ids = [
        parcel_id
        for parcel_id in source_parcels["parcel_id"].tolist()
        for _ in eligible_classes
    ]
    expected_classes = list(eligible_classes) * len(source_parcels)
    if table["parcel_id"].tolist() != expected_ids:
        raise RoadProximityError("Class proximity parcel order is invalid")
    if table["road_proxy_class"].tolist() != expected_classes:
        raise RoadProximityError("Class proximity class order is invalid")
    if policy.classes.not_distance_proxy in set(table["road_proxy_class"]):
        raise RoadProximityError("NOT_DISTANCE_PROXY cannot have distance rows")
    if table.duplicated(["parcel_id", "road_proxy_class"]).any():
        raise RoadProximityError("Class proximity parcel/class pairs must be unique")

    coverage = {item.road_proxy_class: item for item in result.class_coverage}
    required_match_values = (
        "nearest_road_feature_id",
        "nearest_source_feature_id",
        "nearest_road_primary_rule",
        "nearest_road_rule_trace_json",
        "nearest_road_unknown_fields_json",
        "nearest_road_toll_evidence",
        "nearest_source_layer",
        "nearest_source_department_code",
        "nearest_source_edition",
        "nearest_source_archive_sha256",
    )
    for road_class in eligible_classes:
        rows = table.loc[table["road_proxy_class"].eq(road_class)]
        expect_matches = coverage[road_class].feature_count > 0
        _validate_distance_and_ties(rows, expect_matches=expect_matches)
        if expect_matches:
            for column in required_match_values:
                if rows[column].isna().any():
                    raise RoadProximityError(f"Matched class rows require {column}")
        elif rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any().any():
            raise RoadProximityError(
                "Empty-class selected road evidence must be entirely null"
            )

    expected_lineage = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "proximity_scope": _PROXIMITY_SCOPE,
    }
    for column, value in expected_lineage.items():
        if table[column].isna().any() or not table[column].eq(value).all():
            raise RoadProximityError(f"Class proximity lineage differs in {column}")
    _validate_selected_evidence(table, roads)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_enrich_parcel_road_proximity`

**Purpose:** Implements `enrich parcel road proximity` within the file role: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

**Exact signature**

```python
def _enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> ParcelRoadProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelRoadProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `road_source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `policy_path` | positional-or-keyword | `Path \| None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `_enrich_parcel_road_proximity`
- value/type reference: `landscout.stages.enrich_road_proximity::enrich_parcel_road_proximity` via `_enrich_parcel_road_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_parcels` | `landscout.stages.enrich_road_proximity._validate_parcels` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `apply_ign_road_vehicle_proxy_policy` | `landscout.stages.apply_road_vehicle_proxy_policy.apply_ign_road_vehicle_proxy_policy` |
| `_validate_application_roads` | `landscout.stages.enrich_road_proximity._validate_application_roads` |
| `source_parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_calculation_geometries` | `landscout.stages.enrich_road_proximity._calculation_geometries` |
| `_class_proximity_table` | `landscout.stages.enrich_road_proximity._class_proximity_table` |
| `ParcelRoadProximityResult` | `landscout.stages.enrich_road_proximity.ParcelRoadProximityResult` |
| `_coverage` | `landscout.stages.enrich_road_proximity._coverage` |
| `_validate_result` | `landscout.stages.enrich_road_proximity._validate_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `source_parcels.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> ParcelRoadProximityResult:
    source_parcels = _validate_parcels(parcels)
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    application = apply_ign_road_vehicle_proxy_policy(
        road_source, source_config, policy_path
    )
    roads = _validate_application_roads(application, policy)

    output_parcels = source_parcels.copy(deep=True)
    calculation_parcels = source_parcels.to_crs(_CALCULATION_CRS)
    parcel_geometries = _calculation_geometries(calculation_parcels)
    class_proximity = _class_proximity_table(
        source_parcels["parcel_id"], parcel_geometries, roads, policy
    )
    result = ParcelRoadProximityResult(
        parcels=output_parcels,
        class_proximity=class_proximity,
        class_coverage=_coverage(roads, policy),
    )
    _validate_result(source_parcels, roads, policy, result)
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `enrich_parcel_road_proximity`

**Purpose:** Compute exact class-specific distance within the verified source package.

**Exact signature**

```python
def enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelRoadProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `road_source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `policy_path` | positional-or-keyword | `Path \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_enrich_parcel_road_proximity(<br>            parcels, road_source, source_config, policy_path<br>        )`
- Explicit raise paths:
  - `RoadProximityError(<br>                "parcels must be a GeoDataFrame with active geometry"<br>            )` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `RoadProximityError("road_source must be an IgnBdTopoRoadData")` under lexical guard `type(road_source) is not IgnBdTopoRoadData`.
  - `RoadProximityError("source_config must be an IgnBdTopoSourceConfig")` under lexical guard `type(source_config) is not IgnBdTopoSourceConfig`.
  - `RoadProximityError("policy_path must be a pathlib.Path or None")` under lexical guard `policy_path is not None and not isinstance(policy_path, Path)`.
  - `re-raise`.
  - `RoadProximityError(<br>            "Parcel-to-road proximity cannot be computed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- import: `landscout.stages.assess_road_proximity_coverage::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `enrich_parcel_road_proximity`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `enrich_parcel_road_proximity`
- import: `tests.unit.test_enrich_road_proximity::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`
- direct call: `tests.unit.test_enrich_road_proximity::_enrich` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::_enrich` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_type_has_controlled_error` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_parcel_type_has_controlled_error` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_road_source_type_has_controlled_error` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_road_source_type_has_controlled_error` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_source_config_type_has_controlled_error` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_source_config_type_has_controlled_error` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_policy_path_type_has_controlled_error` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_policy_path_type_has_controlled_error` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_stage_is_invoked_exactly_once` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_failure_stops_proximity` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_malformed_policy_stops_before_application` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_malformed_policy_stops_before_application` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_wrong_application_result_type_is_rejected` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_wrong_application_result_type_is_rejected` via `enrich_parcel_road_proximity`
- direct call: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `enrich_parcel_road_proximity`
- value/type reference: `tests.unit.test_enrich_road_proximity::test_application_roads_must_be_geodataframe` via `enrich_parcel_road_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `_enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity._enrich_parcel_road_proximity` |

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
def enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
    """Compute exact class-specific distance within the verified source package."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise RoadProximityError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(road_source) is not IgnBdTopoRoadData:
            raise RoadProximityError("road_source must be an IgnBdTopoRoadData")
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise RoadProximityError("source_config must be an IgnBdTopoSourceConfig")
        if policy_path is not None and not isinstance(policy_path, Path):
            raise RoadProximityError("policy_path must be a pathlib.Path or None")
        return _enrich_parcel_road_proximity(
            parcels, road_source, source_config, policy_path
        )
    except RoadProximityError:
        raise
    except Exception as error:
        raise RoadProximityError(
            "Parcel-to-road proximity cannot be computed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `_ROAD_MATCH_COLUMNS`, `_ROAD_REQUIRED_COLUMNS`, `_MATCH_OUTPUT_MAPPING`, `CLASS_PROXIMITY_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `ParcelRoadProximityResult` | `landscout.stages.enrich_road_proximity.ParcelRoadProximityResult` |
| `RoadProximityError` | `landscout.stages.enrich_road_proximity.RoadProximityError` |
| `RoadProxyClassCoverage` | `landscout.stages.enrich_road_proximity.RoadProxyClassCoverage` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Compute threshold-free parcel proximity by IGN road proxy class."""

from __future__ import annotations

from dataclasses import dataclass
from numbers import Integral
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pandas.api.types import (  # type: ignore[import-untyped]
    is_bool_dtype,
    is_numeric_dtype,
)
from pyproj import CRS
from shapely import STRtree, force_2d  # type: ignore[import-untyped]

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
)
from landscout.stages.apply_road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyApplicationResult,
    apply_ign_road_vehicle_proxy_policy,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)

__all__ = [
    "ParcelRoadProximityResult",
    "RoadProximityError",
    "RoadProxyClassCoverage",
    "enrich_parcel_road_proximity",
]

_PARCEL_STORAGE_CRS = "EPSG:4326"
_CALCULATION_CRS = "EPSG:2154"
_PROXIMITY_SCOPE = "WITHIN_VERIFIED_SOURCE_PACKAGE"
_PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
_ROAD_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})

_ROAD_MATCH_COLUMNS = (
    "road_feature_id",
    "source_feature_id",
    "road_proxy_primary_rule",
    "road_proxy_rule_trace_json",
    "road_proxy_unknown_fields_json",
    "road_proxy_toll_evidence",
    "nature_raw",
    "importance_raw",
    "asset_status_raw",
    "private_raw",
    "light_vehicle_access_raw",
    "carriageway_width_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "source_layer",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
_ROAD_REQUIRED_COLUMNS = frozenset(
    {
        *_ROAD_MATCH_COLUMNS,
        "geometry_status",
        "road_proxy_class",
        "road_proxy_policy_id",
        "road_proxy_policy_schema_version",
        "road_proxy_policy_config_sha256",
        "road_proxy_policy_scope",
        "road_proxy_heavy_vehicle_access",
        "geometry",
    }
)
_MATCH_OUTPUT_MAPPING = {
    "distance_m": "nearest_road_proxy_distance_m",
    "road_feature_id": "nearest_road_feature_id",
    "source_feature_id": "nearest_source_feature_id",
    "tie_count": "nearest_road_tie_count",
    "road_proxy_primary_rule": "nearest_road_primary_rule",
    "road_proxy_rule_trace_json": "nearest_road_rule_trace_json",
    "road_proxy_unknown_fields_json": "nearest_road_unknown_fields_json",
    "road_proxy_toll_evidence": "nearest_road_toll_evidence",
    "nature_raw": "nearest_nature_raw",
    "importance_raw": "nearest_importance_raw",
    "asset_status_raw": "nearest_asset_status_raw",
    "private_raw": "nearest_private_raw",
    "light_vehicle_access_raw": "nearest_light_vehicle_access_raw",
    "carriageway_width_raw": "nearest_carriageway_width_raw",
    "closure_period_raw": "nearest_closure_period_raw",
    "restriction_nature_raw": "nearest_restriction_nature_raw",
    "source_layer": "nearest_source_layer",
    "source_department_code": "nearest_source_department_code",
    "source_edition": "nearest_source_edition",
    "source_archive_sha256": "nearest_source_archive_sha256",
}

CLASS_PROXIMITY_COLUMNS = (
    "parcel_id",
    "road_proxy_class",
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
    "road_proxy_policy_id",
    "road_proxy_policy_schema_version",
    "road_proxy_policy_config_sha256",
    "road_proxy_heavy_vehicle_access",
    "proximity_scope",
)


class RoadProximityError(ValueError):
    """Raised when parcel-to-road proximity cannot be proven safely."""


@dataclass(frozen=True)
class RoadProxyClassCoverage:
    """Source coverage and distance eligibility for one policy class."""

    road_proxy_class: str
    feature_count: int
    distance_eligible: bool


@dataclass(frozen=True)
class ParcelRoadProximityResult:
    """Unchanged parcels plus class-specific factual road proximity."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]


def _validated_crs(value: object, label: str) -> CRS:
    if value is None:
        raise RoadProximityError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise RoadProximityError(f"{label} CRS is unreadable") from error


def _require_crs(value: object, expected_epsg: int, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityError(f"{label} must use EPSG:{expected_epsg}")


def _validate_exact_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise RoadProximityError(f"{label} values must not be null")
    raw = values.tolist()
    if any(not isinstance(value, str) for value in raw):
        raise RoadProximityError(f"{label} values must be exact strings")
    if any(not value.strip() for value in raw):
        raise RoadProximityError(f"{label} values must not be empty")
    if any(value != value.strip() for value in raw):
        raise RoadProximityError(f"{label} values must not have edge whitespace")
    if require_unique and values.duplicated().any():
        raise RoadProximityError(f"{label} values must be unique")


def _validate_parcels(parcels: object) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise RoadProximityError("parcels must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise RoadProximityError("Parcel columns must not contain duplicates")
    missing = {"parcel_id", "geometry"} - set(parcels.columns)
    if missing:
        raise RoadProximityError(
            "Missing required parcel columns: " + ", ".join(sorted(missing))
        )
    if parcels.active_geometry_name != "geometry":
        raise RoadProximityError("Parcel geometry column must be active")
    _require_crs(parcels.crs, 4326, "Parcel storage")
    _validate_exact_ids(parcels["parcel_id"], "parcel_id", require_unique=True)
    if parcels.geometry.isna().any():
        raise RoadProximityError("Parcel geometries must not be null")
    if parcels.geometry.is_empty.any():
        raise RoadProximityError("Parcel geometries must not be empty")
    if not parcels.geometry.is_valid.all():
        raise RoadProximityError("Parcel geometries must be valid")
    unsupported = sorted(
        set(parcels.geometry.geom_type.dropna()) - _PARCEL_GEOMETRY_TYPES
    )
    if unsupported:
        raise RoadProximityError(
            "Parcel geometries must be Polygon or MultiPolygon; found: "
            + ", ".join(str(value) for value in unsupported)
        )
    return parcels


def _policy_classes(
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    all_classes = policy.classes.values
    if len(all_classes) != 6 or len(set(all_classes)) != 6:
        raise RoadProximityError("Compiled road policy class domain is invalid")
    non_distance = policy.classes.not_distance_proxy
    eligible = tuple(value for value in all_classes if value != non_distance)
    if len(eligible) != 5 or non_distance not in all_classes:
        raise RoadProximityError("Compiled road distance eligibility is invalid")
    return all_classes, eligible


def _require_row_lineage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> None:
    expected = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_policy_scope": policy.scope,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
    }
    for column, value in expected.items():
        if roads[column].isna().any() or not roads[column].eq(value).all():
            raise RoadProximityError(
                f"Road application policy lineage differs in {column}"
            )


def _validate_application_roads(
    application: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
    if type(application) is not IgnRoadVehicleProxyApplicationResult:
        raise RoadProximityError("Road application result type is invalid")
    roads = application.roads
    if not isinstance(roads, gpd.GeoDataFrame):
        raise RoadProximityError("Road application roads must be a GeoDataFrame")
    if roads.columns.duplicated().any():
        raise RoadProximityError("Road application columns must not be duplicated")
    missing = _ROAD_REQUIRED_COLUMNS - set(roads.columns)
    if missing:
        raise RoadProximityError(
            "Missing road application column or lineage: " + ", ".join(sorted(missing))
        )
    if roads.active_geometry_name != "geometry":
        raise RoadProximityError("Road application geometry must be active")
    _require_crs(roads.crs, 2154, "Road application")
    _validate_exact_ids(
        roads["road_feature_id"], "road_feature_id", require_unique=True
    )
    _validate_exact_ids(
        roads["source_feature_id"], "source_feature_id", require_unique=False
    )

    all_classes, eligible_classes = _policy_classes(policy)
    classes = roads["road_proxy_class"]
    if classes.isna().any() or not classes.isin(all_classes).all():
        raise RoadProximityError("Road application has an unknown proxy class")
    _require_row_lineage(roads, policy)

    statuses = roads["geometry_status"]
    if statuses.isna().any() or not statuses.isin(_ROAD_GEOMETRY_STATUSES).all():
        raise RoadProximityError("Road application geometry status is invalid")
    eligible = classes.isin(eligible_classes)
    if not statuses.loc[eligible].eq("VALID").all():
        raise RoadProximityError(
            "Distance-eligible roads must have VALID geometry status"
        )
    eligible_geometry = roads.loc[eligible, "geometry"]
    if eligible_geometry.isna().any():
        raise RoadProximityError("Distance-eligible road geometry must not be null")
    if eligible_geometry.is_empty.any():
        raise RoadProximityError("Distance-eligible road geometry must not be empty")
    if not eligible_geometry.is_valid.all():
        raise RoadProximityError("Distance-eligible road geometry must be valid")
    unsupported = sorted(
        set(eligible_geometry.geom_type.dropna()) - _ROAD_GEOMETRY_TYPES
    )
    if unsupported:
        raise RoadProximityError(
            "Distance-eligible geometry must be LineString or MultiLineString; found: "
            + ", ".join(str(value) for value in unsupported)
        )
    return roads


def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)


def _empty_nearest_rows(parcel_count: int) -> pd.DataFrame:
    output = pd.DataFrame(index=pd.RangeIndex(parcel_count))
    output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")
    output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")
    for column in _ROAD_MATCH_COLUMNS:
        if column == "road_proxy_toll_evidence":
            output[column] = pd.Series(pd.NA, index=output.index, dtype="boolean")
        else:
            output[column] = pd.Series(pd.NA, index=output.index, dtype="object")
    return output


def _nearest_class_rows(
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
) -> pd.DataFrame:
    parcel_count = len(parcel_geometries)
    if roads.empty:
        return _empty_nearest_rows(parcel_count)

    tree = STRtree(_calculation_geometries(roads))
    indices, distances = tree.query_nearest(
        parcel_geometries,
        all_matches=True,
        return_distance=True,
    )
    matches = pd.DataFrame(
        {
            "parcel_position": indices[0],
            "road_position": indices[1],
            "distance_m": distances,
        }
    )
    matches["road_feature_id"] = roads.iloc[matches["road_position"].to_numpy()][
        "road_feature_id"
    ].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "road_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position", kind="mergesort"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise RoadProximityError("Nearest-road matching did not cover every parcel")

    source_rows = roads.iloc[selected["road_position"].to_numpy()]
    output = source_rows.loc[:, list(_ROAD_MATCH_COLUMNS)].reset_index(drop=True)
    output.insert(
        0,
        "tie_count",
        pd.Series(ties.reindex(range(parcel_count)).to_numpy(), dtype="Int64"),
    )
    output.insert(
        0,
        "distance_m",
        selected["distance_m"].to_numpy(dtype="float64"),
    )
    return output


def _coverage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[RoadProxyClassCoverage, ...]:
    all_classes, eligible_classes = _policy_classes(policy)
    counts = roads["road_proxy_class"].value_counts()
    return tuple(
        RoadProxyClassCoverage(
            road_proxy_class=road_class,
            feature_count=int(counts.get(road_class, 0)),
            distance_eligible=road_class in eligible_classes,
        )
        for road_class in all_classes
    )


def _class_proximity_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> pd.DataFrame:
    _, eligible_classes = _policy_classes(policy)
    tables: list[pd.DataFrame] = []
    for class_position, road_class in enumerate(eligible_classes):
        class_roads = roads.loc[roads["road_proxy_class"].eq(road_class)].reset_index(
            drop=True
        )
        nearest = _nearest_class_rows(parcel_geometries, class_roads)
        _validate_distance_and_ties(
            nearest.rename(
                columns={
                    "distance_m": "nearest_road_proxy_distance_m",
                    "tie_count": "nearest_road_tie_count",
                }
            ),
            expect_matches=not class_roads.empty,
        )
        table = pd.DataFrame(
            {
                "_parcel_position": np.arange(len(parcel_ids), dtype="int64"),
                "_class_position": class_position,
                "parcel_id": parcel_ids.reset_index(drop=True),
                "road_proxy_class": road_class,
            }
        )
        for source_column, output_column in _MATCH_OUTPUT_MAPPING.items():
            table[output_column] = nearest[source_column].reset_index(drop=True)
        table["road_proxy_policy_id"] = policy.policy_id
        table["road_proxy_policy_schema_version"] = policy.schema_version
        table["road_proxy_policy_config_sha256"] = policy.config_sha256
        table["road_proxy_heavy_vehicle_access"] = policy.heavy_vehicle_access
        table["proximity_scope"] = _PROXIMITY_SCOPE
        tables.append(table)

    output = pd.concat(tables, ignore_index=True)
    output = output.sort_values(
        ["_parcel_position", "_class_position"], kind="mergesort"
    ).reset_index(drop=True)
    output = output.drop(columns=["_parcel_position", "_class_position"])
    output["nearest_road_proxy_distance_m"] = output[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    output["nearest_road_tie_count"] = output["nearest_road_tie_count"].astype("Int64")
    output["nearest_road_toll_evidence"] = output["nearest_road_toll_evidence"].astype(
        "boolean"
    )
    return output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]


def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False


def _validate_distance_and_ties(
    rows: pd.DataFrame,
    *,
    expect_matches: bool,
) -> None:
    distances = rows["nearest_road_proxy_distance_m"]
    matched = distances.notna()
    if expect_matches and not matched.all():
        raise RoadProximityError("Non-empty road classes require parcel matches")
    if not expect_matches and matched.any():
        raise RoadProximityError("Empty road classes must not contain matches")
    if matched.any():
        if not is_numeric_dtype(distances.dtype) or is_bool_dtype(distances.dtype):
            raise RoadProximityError("Matched road distances must be numeric")
        numeric = distances.loc[matched].to_numpy(dtype="float64")
        if not np.isfinite(numeric).all() or (numeric < 0).any():
            raise RoadProximityError("Matched road distances must be finite and >= 0")

    ties = rows["nearest_road_tie_count"]
    for value, row_matched in zip(
        ties.tolist(), matched.to_numpy(dtype=bool), strict=True
    ):
        missing = _is_missing_scalar(value)
        if not row_matched:
            if not missing:
                raise RoadProximityError("Unmatched rows require null tie_count")
            continue
        if (
            missing
            or not isinstance(value, Integral)
            or isinstance(value, (bool, np.bool_))
            or int(value) < 1
        ):
            raise RoadProximityError(
                "Matched nearest_road_tie_count must be an integer >= 1"
            )


def _null_safe_equal(actual: pd.Series, expected: pd.Series) -> bool:
    left = actual.reset_index(drop=True)
    right = expected.reset_index(drop=True)
    if len(left) != len(right):
        return False
    both_null = left.isna() & right.isna()
    try:
        equal = left.eq(right).fillna(False)
    except (TypeError, ValueError):
        return False
    return bool((both_null | equal).all())


def _validate_selected_evidence(
    table: pd.DataFrame,
    roads: gpd.GeoDataFrame,
) -> None:
    matched = table["nearest_road_feature_id"].notna()
    selected = table.loc[matched].reset_index(drop=True)
    if selected.empty:
        return
    lookup = roads.set_index("road_feature_id", drop=False)
    positions = lookup.index.get_indexer(selected["nearest_road_feature_id"])
    if (positions < 0).any():
        raise RoadProximityError("Selected nearest road ID is absent from source")
    expected = lookup.iloc[positions].reset_index(drop=True)
    if (
        not selected["road_proxy_class"]
        .reset_index(drop=True)
        .eq(expected["road_proxy_class"])
        .all()
    ):
        raise RoadProximityError("Selected nearest road has the wrong proxy class")

    for source_column, output_column in _MATCH_OUTPUT_MAPPING.items():
        if source_column in {"distance_m", "tie_count"}:
            continue
        if not _null_safe_equal(selected[output_column], expected[source_column]):
            raise RoadProximityError(
                f"Selected nearest road evidence differs for {output_column}"
            )


def _validate_coverage(
    coverage: tuple[RoadProxyClassCoverage, ...],
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
    all_classes, eligible_classes = _policy_classes(policy)
    if type(coverage) is not tuple or len(coverage) != len(all_classes):
        raise RoadProximityError("Road class coverage is incomplete")
    counts = roads["road_proxy_class"].value_counts()
    total = 0
    for position, item in enumerate(coverage):
        if type(item) is not RoadProxyClassCoverage:
            raise RoadProximityError("Road class coverage entry type is invalid")
        road_class = all_classes[position]
        if item.road_proxy_class != road_class:
            raise RoadProximityError("Road class coverage order is invalid")
        if type(item.feature_count) is not int or item.feature_count < 0:
            raise RoadProximityError("Road class feature_count must be an integer >= 0")
        if type(item.distance_eligible) is not bool:
            raise RoadProximityError("Road class distance_eligible must be Boolean")
        if item.distance_eligible != (road_class in eligible_classes):
            raise RoadProximityError("Road class distance eligibility is invalid")
        if item.feature_count != int(counts.get(road_class, 0)):
            raise RoadProximityError("Road class feature_count differs from source")
        total += item.feature_count
    if total != len(roads):
        raise RoadProximityError("Road class coverage does not sum to source rows")
    return eligible_classes


def _validate_parcel_preservation(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
) -> None:
    if len(output) != len(source):
        raise RoadProximityError("Road proximity changed parcel count")
    if list(output.columns) != list(source.columns):
        raise RoadProximityError("Road proximity changed parcel columns")
    if not output.dtypes.equals(source.dtypes):
        raise RoadProximityError("Road proximity changed parcel dtypes")
    if (
        type(output.index) is not type(source.index)
        or output.index.names != source.index.names
        or str(output.index.dtype) != str(source.index.dtype)
        or not output.index.equals(source.index)
    ):
        raise RoadProximityError("Road proximity changed parcel index metadata")
    if not _validated_crs(output.crs, "Output parcel").equals(
        _validated_crs(source.crs, "Source parcel")
    ):
        raise RoadProximityError("Road proximity changed parcel CRS")
    if not output.geometry.to_wkb().equals(source.geometry.to_wkb()):
        raise RoadProximityError("Road proximity changed parcel geometry WKB")
    geometry_column = source.active_geometry_name
    if geometry_column is None or not output.drop(columns=geometry_column).equals(
        source.drop(columns=geometry_column)
    ):
        raise RoadProximityError("Road proximity changed parcel facts")


def _validate_result(
    source_parcels: gpd.GeoDataFrame,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
    result: ParcelRoadProximityResult,
) -> None:
    if type(result) is not ParcelRoadProximityResult:
        raise RoadProximityError("Road proximity result type is invalid")
    if not isinstance(result.parcels, gpd.GeoDataFrame):
        raise RoadProximityError("Road proximity parcels must be a GeoDataFrame")
    if type(result.class_proximity) is not pd.DataFrame:
        raise RoadProximityError("Class proximity must be a plain DataFrame")
    _validate_parcel_preservation(source_parcels, result.parcels)
    eligible_classes = _validate_coverage(result.class_coverage, roads, policy)
    table = result.class_proximity
    if table.columns.duplicated().any() or list(table.columns) != list(
        CLASS_PROXIMITY_COLUMNS
    ):
        raise RoadProximityError("Class proximity schema is invalid")
    if len(table) != len(source_parcels) * len(eligible_classes):
        raise RoadProximityError("Class proximity row count is invalid")
    expected_ids = [
        parcel_id
        for parcel_id in source_parcels["parcel_id"].tolist()
        for _ in eligible_classes
    ]
    expected_classes = list(eligible_classes) * len(source_parcels)
    if table["parcel_id"].tolist() != expected_ids:
        raise RoadProximityError("Class proximity parcel order is invalid")
    if table["road_proxy_class"].tolist() != expected_classes:
        raise RoadProximityError("Class proximity class order is invalid")
    if policy.classes.not_distance_proxy in set(table["road_proxy_class"]):
        raise RoadProximityError("NOT_DISTANCE_PROXY cannot have distance rows")
    if table.duplicated(["parcel_id", "road_proxy_class"]).any():
        raise RoadProximityError("Class proximity parcel/class pairs must be unique")

    coverage = {item.road_proxy_class: item for item in result.class_coverage}
    required_match_values = (
        "nearest_road_feature_id",
        "nearest_source_feature_id",
        "nearest_road_primary_rule",
        "nearest_road_rule_trace_json",
        "nearest_road_unknown_fields_json",
        "nearest_road_toll_evidence",
        "nearest_source_layer",
        "nearest_source_department_code",
        "nearest_source_edition",
        "nearest_source_archive_sha256",
    )
    for road_class in eligible_classes:
        rows = table.loc[table["road_proxy_class"].eq(road_class)]
        expect_matches = coverage[road_class].feature_count > 0
        _validate_distance_and_ties(rows, expect_matches=expect_matches)
        if expect_matches:
            for column in required_match_values:
                if rows[column].isna().any():
                    raise RoadProximityError(f"Matched class rows require {column}")
        elif rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any().any():
            raise RoadProximityError(
                "Empty-class selected road evidence must be entirely null"
            )

    expected_lineage = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "proximity_scope": _PROXIMITY_SCOPE,
    }
    for column, value in expected_lineage.items():
        if table[column].isna().any() or not table[column].eq(value).all():
            raise RoadProximityError(f"Class proximity lineage differs in {column}")
    _validate_selected_evidence(table, roads)


def _enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> ParcelRoadProximityResult:
    source_parcels = _validate_parcels(parcels)
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    application = apply_ign_road_vehicle_proxy_policy(
        road_source, source_config, policy_path
    )
    roads = _validate_application_roads(application, policy)

    output_parcels = source_parcels.copy(deep=True)
    calculation_parcels = source_parcels.to_crs(_CALCULATION_CRS)
    parcel_geometries = _calculation_geometries(calculation_parcels)
    class_proximity = _class_proximity_table(
        source_parcels["parcel_id"], parcel_geometries, roads, policy
    )
    result = ParcelRoadProximityResult(
        parcels=output_parcels,
        class_proximity=class_proximity,
        class_coverage=_coverage(roads, policy),
    )
    _validate_result(source_parcels, roads, policy, result)
    return result


def enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
    """Compute exact class-specific distance within the verified source package."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise RoadProximityError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(road_source) is not IgnBdTopoRoadData:
            raise RoadProximityError("road_source must be an IgnBdTopoRoadData")
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise RoadProximityError("source_config must be an IgnBdTopoSourceConfig")
        if policy_path is not None and not isinstance(policy_path, Path):
            raise RoadProximityError("policy_path must be a pathlib.Path or None")
        return _enrich_parcel_road_proximity(
            parcels, road_source, source_config, policy_path
        )
    except RoadProximityError:
        raise
    except Exception as error:
        raise RoadProximityError(
            "Parcel-to-road proximity cannot be computed safely"
        ) from error
```
