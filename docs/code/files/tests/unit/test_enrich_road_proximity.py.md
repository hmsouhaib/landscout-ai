# `tests/unit/test_enrich_road_proximity.py`

## File identity

- Repository path: `tests/unit/test_enrich_road_proximity.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.
- Source SHA256: `c05463733323609f0b4b5d32e7ee0269b8f951bd12d924cc155b0f6c7c2548ff`

## 1. Purpose

Provides complete unit and regression coverage for the `enrich_road_proximity` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

## 4. Contract taxonomy

### A. Python constants

#### `SOURCE_CONFIG`

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_road_proximity.py::_enrich` (value reference), `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error` (value reference), `tests/unit/test_enrich_road_proximity.py::test_wrong_road_source_type_has_controlled_error` (value reference), `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error` (value reference), `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` (value reference), `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` (value reference), `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application` (value reference), `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected` (value reference), `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` (value reference).

#### `POLICY_PATH`

```python
POLICY_PATH = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `ELIGIBLE_CLASSES`

```python
ELIGIBLE_CLASSES = (
    "GENERAL_VEHICLE_PROXY",
    "LIMITED_VEHICLE_PROXY",
    "RESTRICTED_REVIEW",
    "NOT_GENERAL_VEHICLE_PROXY",
    "UNKNOWN_REVIEW",
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_road_proximity.py::test_each_eligible_class_has_independent_distance` (value reference), `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic` (value reference).

#### `ALL_CLASSES`

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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_enrich_road_proximity.py::test_class_coverage_is_complete_and_strict` (value reference).

#### `SELECTED_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_metric_parcels`

**Exact signature**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for metric parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'parcel_id': ids, 'source_value': list(range(count))}, geometry=values, crs='EPSG:2154', index=frame_index)
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

- direct call: `tests/unit/test_enrich_road_proximity.py::_parcels` via `_metric_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `_metric_parcels`.

**Complete source-ordered implementation**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    ]
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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_parcels`

**Exact signature**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs('EPSG:4326')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_metric_parcels(geometries, identifiers=identifiers, index=index).to_crs`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_enrich_road_proximity.py::_enrich` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_road_source_type_has_controlled_error` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_invalid_parcel_identity_is_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_id_is_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_columns_are_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_missing_or_inactive_geometry_is_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_geometry_kind_is_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_bad_parcel_geometry_is_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_polygon_and_multipolygon_are_accepted` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_result_dataclasses_are_frozen` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_result_parcel_frame_is_an_independent_copy` via `_parcels`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_parcel_preservation_uses_exact_non_geometry_values` via `_parcels`.

**Complete source-ordered implementation**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(
        geometries, identifiers=identifiers, index=index
    ).to_crs("EPSG:4326")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_road_row`

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

**Purpose**

Private `test` helper for road row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'road_feature_id': identifier, 'source_feature_id': f'SOURCE-{identifier}', 'geometry_status': 'VALID', 'nature_raw': 'Route à 1 chaussée', 'importance_raw': '2', 'asset_status_raw': 'En service', 'private_raw': 0.0, 'light_vehicle_access_raw': 'Libre', 'carriageway_width_raw': 7.0, 'closure_period_raw': None, 'restriction_nature_raw': None, 'source_layer': 'troncon_de_route', 'source_department_code': '31', 'source_edition': '2026-06-15', 'source_archive_sha256': 'a' * 64, 'road_proxy_primary_rule': primary_rule, 'road_proxy_class': road_class, 'road_proxy_rule_trace_json': f'["{primary_rule}"]', 'road_proxy_unknown_fields_json': '[]', 'road_proxy_toll_evidence': False, 'road_proxy_policy_id': policy.policy_id, 'road_proxy_policy_schema_version': policy.schema_version, 'road_proxy_policy_config_sha256': policy.config_sha256, 'road_proxy_policy_scope': policy.scope, 'road_proxy_heavy_vehicle_access': policy.heavy_vehicle_access, 'geometry': geometry or LineString([(x, -20), (x, 30)])}
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

- direct call: `tests/unit/test_enrich_road_proximity.py::_roads` via `_road_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_road_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_road_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_road_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_road_row`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_roads`

**Exact signature**

```python
def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for roads; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame(values, geometry='geometry', crs='EPSG:2154')
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

- direct call: `tests/unit/test_enrich_road_proximity.py::_source` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::_enrich` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_independent_policy_sha_mismatch_is_rejected` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_duplicate_road_feature_id_is_rejected` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_unknown_road_proxy_class_is_rejected` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_missing_road_policy_lineage_is_rejected` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_requires_valid_geometry_status` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_rejects_unsupported_geometry` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_not_distance_road_is_counted_but_never_indexed` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_selected_rows_belong_to_requested_class` via `_roads`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_roads`.

**Complete source-ordered implementation**

```python
def _roads(
    rows: list[dict[str, object]] | None = None,
) -> gpd.GeoDataFrame:
    values = rows or [
        _road_row(
            "GENERAL_VEHICLE_PROXY", 20, identifier="ROAD-GENERAL"
        ),
        _road_row(
            "LIMITED_VEHICLE_PROXY", 30, identifier="ROAD-LIMITED"
        ),
        _road_row("RESTRICTED_REVIEW", 15, identifier="ROAD-RESTRICTED"),
        _road_row(
            "NOT_GENERAL_VEHICLE_PROXY", 40, identifier="ROAD-NOT-GENERAL"
        ),
        _road_row("NOT_DISTANCE_PROXY", 11, identifier="ROAD-NOT-DISTANCE"),
        _road_row("UNKNOWN_REVIEW", 50, identifier="ROAD-UNKNOWN"),
    ]
    return gpd.GeoDataFrame(values, geometry="geometry", crs="EPSG:2154")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source`

**Exact signature**

```python
def _source() -> IgnBdTopoRoadData:
```

**Purpose**

Private `test` helper for source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoRoadData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoRoadData(extraction=cast(Any, None), road_segments=_roads(), road_segments_summary=cast(Any, None))
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

- direct call: `tests/unit/test_enrich_road_proximity.py::_enrich` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected` via `_source`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `_source`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_enrich`

**Exact signature**

```python
def _enrich(
    parcels: gpd.GeoDataFrame | None = None,
    roads: gpd.GeoDataFrame | None = None,
    *,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Copies input evidence and adds enrich; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `ParcelRoadProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
enrich_parcel_road_proximity(parcels if parcels is not None else _parcels(), _source(), SOURCE_CONFIG, policy_path)
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

- direct call: `tests/unit/test_enrich_road_proximity.py::test_independent_policy_sha_mismatch_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_invalid_parcel_identity_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_id_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_columns_are_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_missing_or_inactive_geometry_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_geometry_kind_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_bad_parcel_geometry_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_polygon_and_multipolygon_are_accepted` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_duplicate_road_feature_id_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_unknown_road_proxy_class_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_missing_road_policy_lineage_is_rejected` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_requires_valid_geometry_status` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_rejects_unsupported_geometry` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_not_distance_road_is_counted_but_never_indexed` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_known_polygon_to_line_distance_is_ten_metres` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_distance_uses_full_polygon_not_centroid` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_each_eligible_class_has_independent_distance` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_near_not_distance_road_cannot_change_general_distance` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_single_nearest_road_has_tie_count_one` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_class_coverage_is_complete_and_strict` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_parcels_and_road_application_are_not_mutated` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::_corrupt_nearest_output` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_result_dataclasses_are_frozen` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_no_business_decision_columns_or_implementation_exist` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_result_parcel_frame_is_an_independent_copy` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_class_proximity_is_plain_dataframe` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_selected_rows_belong_to_requested_class` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_policy_sha_mismatch_does_not_construct_spatial_index` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_matched_output_dtypes_are_stable` via `_enrich`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_parcel_preservation_uses_exact_non_geometry_values` via `_enrich`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_row`

**Exact signature**

```python
def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
```

**Purpose**

Private `test` helper for row; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
result.class_proximity.loc[result.class_proximity['road_proxy_class'].eq(road_class)].iloc[0]
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

- direct call: `tests/unit/test_enrich_road_proximity.py::test_known_polygon_to_line_distance_is_ten_metres` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_intersecting_or_touching_road_has_zero_distance` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_distance_uses_full_polygon_not_centroid` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_storage_geometry_stays_epsg4326_while_distance_is_metric` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_each_eligible_class_has_independent_distance` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_near_not_distance_road_cannot_change_general_distance` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_single_nearest_road_has_tie_count_one` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_exact_tie_counts_two_and_lexical_id_wins` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_tie_winner_is_independent_of_source_order` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_unequal_distance_wins_regardless_of_identifier` via `_row`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_selected_road_evidence_and_lineage_are_exact` via `_row`.

**Complete source-ordered implementation**

```python
def _row(result: ParcelRoadProximityResult, road_class: str) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_symbols`

**Purpose**

Exercises `public api exports only stable symbols`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
import landscout.stages.enrich_road_proximity as module
expected = {
        "RoadProximityError",
        "RoadProxyClassCoverage",
        "ParcelRoadProximityResult",
        "enrich_parcel_road_proximity",
    }
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(module.__all__) == expected
assert expected <= set(stages.__all__)
assert all(hasattr(stages, symbol) for symbol in expected)
assert not hasattr(stages, "_nearest_class_rows")
```

**Regression protected**

Locks `public api exports only stable symbols` through the exact asserted conditions: `set(module.__all__) == expected`; `expected <= set(stages.__all__)`; `all((hasattr(stages, symbol) for symbol in expected))`; `not hasattr(stages, '_nearest_class_rows')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_wrong_parcel_type_has_controlled_error`

**Purpose**

Exercises `wrong parcel type has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG
        )
```

**Regression protected**

Locks `wrong parcel type has controlled error`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_parcel_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            cast(Any, pd.DataFrame()), _source(), SOURCE_CONFIG
        )
```

### `test_wrong_road_source_type_has_controlled_error`

**Purpose**

Exercises `wrong road source type has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), cast(Any, object()), SOURCE_CONFIG
        )
```

**Regression protected**

Locks `wrong road source type has controlled error`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_road_source_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), cast(Any, object()), SOURCE_CONFIG
        )
```

### `test_wrong_source_config_type_has_controlled_error`

**Purpose**

Exercises `wrong source config type has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), cast(Any, object())
        )
```

**Regression protected**

Locks `wrong source config type has controlled error`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_source_config_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), cast(Any, object())
        )
```

### `test_wrong_policy_path_type_has_controlled_error`

**Purpose**

Exercises `wrong policy path type has controlled error`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), SOURCE_CONFIG, cast(Any, "policy.yaml")
        )
```

**Regression protected**

Locks `wrong policy path type has controlled error`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_policy_path_type_has_controlled_error() -> None:
    with pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(
            _parcels(), _source(), SOURCE_CONFIG, cast(Any, "policy.yaml")
        )
```

### `test_application_stage_is_invoked_exactly_once`

**Purpose**

Exercises `application stage is invoked exactly once`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source_application.assert_called_once()
```

**Action**

```python
application = IgnRoadVehicleProxyApplicationResult(_roads())
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ) as source_application:
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `application stage is invoked exactly once` by requiring the reproduced call path `IgnRoadVehicleProxyApplicationResult`, `source_application.assert_called_once`, `_roads`, `patch` without an unasserted exception.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_application_failure_stops_proximity`

**Purpose**

Exercises `application failure stops proximity`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
spatial_index.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        side_effect=IgnRoadVehicleProxyApplicationError("bad source"),
    ), patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Regression protected**

Locks `application failure stops proximity`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_application_failure_stops_proximity() -> None:
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        side_effect=IgnRoadVehicleProxyApplicationError("bad source"),
    ), patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)

    spatial_index.assert_not_called()
```

### `test_malformed_policy_stops_before_application`

**Purpose**

Exercises `malformed policy stops before application`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "policy.yaml"
path.write_text("policy_id: [", encoding="utf-8")
source_application.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy"
    ) as source_application, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)
```

**Regression protected**

Locks `malformed policy stops before application`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_malformed_policy_stops_before_application(tmp_path: Path) -> None:
    path = tmp_path / "policy.yaml"
    path.write_text("policy_id: [", encoding="utf-8")

    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy"
    ) as source_application, pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG, path)

    source_application.assert_not_called()
```

### `test_independent_policy_sha_mismatch_is_rejected`

**Purpose**

Exercises `independent policy sha mismatch is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads["road_proxy_policy_config_sha256"] = "b" * 64
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="policy|SHA|lineage"):
        _enrich(roads=roads)
```

**Regression protected**

Locks `independent policy sha mismatch is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_independent_policy_sha_mismatch_is_rejected() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with pytest.raises(RoadProximityError, match="policy|SHA|lineage"):
        _enrich(roads=roads)
```

### `test_invalid_parcel_identity_is_rejected`

**Purpose**

Exercises `invalid parcel identity is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `message`, `mutation`.

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
with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=mutation(_parcels()))
```

**Regression protected**

Locks `invalid parcel identity is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_parcel_identity_is_rejected(
    mutation: Any, message: str
) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=mutation(_parcels()))
```

### `test_duplicate_parcel_id_is_rejected`

**Purpose**

Exercises `duplicate parcel id is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
            Polygon([(20, 0), (20, 10), (30, 10), (30, 0), (20, 0)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="unique"):
        _enrich(parcels=parcels)
```

**Regression protected**

Locks `duplicate parcel id is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `test_duplicate_parcel_columns_are_rejected`

**Purpose**

Exercises `duplicate parcel columns are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
duplicated = gpd.GeoDataFrame(
        pd.concat([parcels, parcels[["parcel_id"]]], axis=1),
        geometry="geometry",
        crs=parcels.crs,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="duplicate"):
        _enrich(parcels=duplicated)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `test_missing_or_inactive_geometry_is_rejected`

**Purpose**

Exercises `missing or inactive geometry is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
missing = parcels.drop(columns="geometry")
inactive = parcels.assign(other_geometry=parcels.geometry).set_geometry(
        "other_geometry"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="geometry"):
        _enrich(parcels=missing)
with pytest.raises(RoadProximityError, match="active"):
        _enrich(parcels=inactive)
```

**Regression protected**

Locks `missing or inactive geometry is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `test_missing_or_wrong_storage_crs_is_rejected`

**Purpose**

Exercises `missing or wrong storage crs is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
missing = _parcels().set_crs(None, allow_override=True)
wrong = _metric_parcels()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="CRS"):
        _enrich(parcels=missing)
with pytest.raises(RoadProximityError, match="4326"):
        _enrich(parcels=wrong)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_or_wrong_storage_crs_is_rejected() -> None:
    missing = _parcels().set_crs(None, allow_override=True)
    wrong = _metric_parcels()

    with pytest.raises(RoadProximityError, match="CRS"):
        _enrich(parcels=missing)
    with pytest.raises(RoadProximityError, match="4326"):
        _enrich(parcels=wrong)
```

### `test_wrong_parcel_geometry_kind_is_rejected`

**Purpose**

Exercises `wrong parcel geometry kind is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

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
with pytest.raises(RoadProximityError, match="Polygon|MultiPolygon"):
        _enrich(parcels=_parcels([geometry]))
```

**Regression protected**

Locks `wrong parcel geometry kind is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_wrong_parcel_geometry_kind_is_rejected(geometry: object) -> None:
    with pytest.raises(RoadProximityError, match="Polygon|MultiPolygon"):
        _enrich(parcels=_parcels([geometry]))
```

### `test_bad_parcel_geometry_is_rejected`

**Purpose**

Exercises `bad parcel geometry is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`, `message`.

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
with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=_parcels([geometry]))
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_bad_parcel_geometry_is_rejected(
    geometry: object, message: str
) -> None:
    with pytest.raises(RoadProximityError, match=message):
        _enrich(parcels=_parcels([geometry]))
```

### `test_polygon_and_multipolygon_are_accepted`

**Purpose**

Exercises `polygon and multipolygon are accepted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

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
assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1
```

**Regression protected**

Locks `polygon and multipolygon are accepted` through the exact asserted conditions: `len(_enrich(parcels=_parcels([geometry])).parcels) == 1`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_polygon_and_multipolygon_are_accepted(geometry: object) -> None:
    assert len(_enrich(parcels=_parcels([geometry])).parcels) == 1
```

### `test_wrong_application_result_type_is_rejected`

**Purpose**

Exercises `wrong application result type is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=object(),
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Regression protected**

Locks `wrong application result type is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_wrong_application_result_type_is_rejected() -> None:
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=object(),
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

### `test_application_roads_must_be_geodataframe`

**Purpose**

Exercises `application roads must be geodataframe`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
application = IgnRoadVehicleProxyApplicationResult(
        cast(Any, pd.DataFrame(_roads().drop(columns="geometry")))
    )
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

**Regression protected**

Locks `application roads must be geodataframe`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_application_roads_must_be_geodataframe() -> None:
    application = IgnRoadVehicleProxyApplicationResult(
        cast(Any, pd.DataFrame(_roads().drop(columns="geometry")))
    )
    with patch(
        "landscout.stages.enrich_road_proximity.apply_ign_road_vehicle_proxy_policy",
        return_value=application,
    ), pytest.raises(RoadProximityError):
        enrich_parcel_road_proximity(_parcels(), _source(), SOURCE_CONFIG)
```

### `test_duplicate_road_feature_id_is_rejected`

**Purpose**

Exercises `duplicate road feature id is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="unique"):
        _enrich(roads=roads)
```

**Regression protected**

Locks `duplicate road feature id is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_road_feature_id_is_rejected() -> None:
    roads = _roads()
    roads.loc[1, "road_feature_id"] = roads.loc[0, "road_feature_id"]

    with pytest.raises(RoadProximityError, match="unique"):
        _enrich(roads=roads)
```

### `test_unknown_road_proxy_class_is_rejected`

**Purpose**

Exercises `unknown road proxy class is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.loc[0, "road_proxy_class"] = "INVENTED"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="class"):
        _enrich(roads=roads)
```

**Regression protected**

Locks `unknown road proxy class is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_road_proxy_class_is_rejected() -> None:
    roads = _roads()
    roads.loc[0, "road_proxy_class"] = "INVENTED"

    with pytest.raises(RoadProximityError, match="class"):
        _enrich(roads=roads)
```

### `test_missing_road_policy_lineage_is_rejected`

**Purpose**

Exercises `missing road policy lineage is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

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
with pytest.raises(RoadProximityError, match="column|lineage"):
        _enrich(roads=_roads().drop(columns=column))
```

**Regression protected**

Locks `missing road policy lineage is rejected`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_missing_road_policy_lineage_is_rejected(column: str) -> None:
    with pytest.raises(RoadProximityError, match="column|lineage"):
        _enrich(roads=_roads().drop(columns=column))
```

### `test_eligible_class_requires_valid_geometry_status`

**Purpose**

Exercises `eligible class requires valid geometry status`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
roads = _roads()
roads.loc[0, "geometry_status"] = status
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="VALID"):
        _enrich(roads=roads)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_eligible_class_requires_valid_geometry_status(status: str) -> None:
    roads = _roads()
    roads.loc[0, "geometry_status"] = status

    with pytest.raises(RoadProximityError, match="VALID"):
        _enrich(roads=roads)
```

### `test_eligible_class_rejects_unsupported_geometry`

**Purpose**

Exercises `eligible class rejects unsupported geometry`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.at[0, "geometry"] = Point(20, 0)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityError, match="LineString|geometry"):
        _enrich(roads=roads)
```

**Regression protected**

Locks `eligible class rejects unsupported geometry`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_eligible_class_rejects_unsupported_geometry() -> None:
    roads = _roads()
    roads.at[0, "geometry"] = Point(20, 0)

    with pytest.raises(RoadProximityError, match="LineString|geometry"):
        _enrich(roads=roads)
```

### `test_not_distance_road_is_counted_but_never_indexed`

**Purpose**

Exercises `not distance road is counted but never indexed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads.loc[
        roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"
    ] = "INVALID"
result = _enrich(roads=roads)
coverage = {item.road_proxy_class: item for item in result.class_coverage}
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1
assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible
assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)
```

**Regression protected**

Locks `not distance road is counted but never indexed` through the exact asserted conditions: `coverage['NOT_DISTANCE_PROXY'].feature_count == 1`; `not coverage['NOT_DISTANCE_PROXY'].distance_eligible`; `'NOT_DISTANCE_PROXY' not in set(result.class_proximity.road_proxy_class)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_not_distance_road_is_counted_but_never_indexed() -> None:
    roads = _roads()
    roads.loc[
        roads["road_proxy_class"].eq("NOT_DISTANCE_PROXY"), "geometry_status"
    ] = "INVALID"
    result = _enrich(roads=roads)
    coverage = {item.road_proxy_class: item for item in result.class_coverage}

    assert coverage["NOT_DISTANCE_PROXY"].feature_count == 1
    assert not coverage["NOT_DISTANCE_PROXY"].distance_eligible
    assert "NOT_DISTANCE_PROXY" not in set(result.class_proximity.road_proxy_class)
```

### `test_known_polygon_to_line_distance_is_ten_metres`

**Purpose**

Exercises `known polygon to line distance is ten metres`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
```

**Regression protected**

Locks `known polygon to line distance is ten metres` through the exact asserted conditions: `_row(result, 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-05)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_known_polygon_to_line_distance_is_ten_metres() -> None:
    result = _enrich()

    assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
```

### `test_intersecting_or_touching_road_has_zero_distance`

**Purpose**

Exercises `intersecting or touching road has zero distance`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `x`.

**Setup**

```python
roads = _roads(
        [_road_row("GENERAL_VEHICLE_PROXY", x, identifier="ROAD-GENERAL")]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)
```

**Regression protected**

Locks `intersecting or touching road has zero distance` through the exact asserted conditions: `_row(_enrich(roads=roads), 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-05)`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_intersecting_or_touching_road_has_zero_distance(x: float) -> None:
    roads = _roads(
        [_road_row("GENERAL_VEHICLE_PROXY", x, identifier="ROAD-GENERAL")]
    )

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(0.0, abs=1e-5)
```

### `test_distance_uses_full_polygon_not_centroid`

**Purpose**

Exercises `distance uses full polygon not centroid`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
distance = _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert distance == pytest.approx(10.0, abs=1e-5)
assert distance != pytest.approx(15.0, abs=1e-5)
```

**Regression protected**

Locks `distance uses full polygon not centroid` through the exact asserted conditions: `distance == pytest.approx(10.0, abs=1e-05)`; `distance != pytest.approx(15.0, abs=1e-05)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_distance_uses_full_polygon_not_centroid() -> None:
    distance = _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m

    assert distance == pytest.approx(10.0, abs=1e-5)
    assert distance != pytest.approx(15.0, abs=1e-5)
```

### `test_storage_geometry_stays_epsg4326_while_distance_is_metric`

**Purpose**

Exercises `storage geometry stays epsg4326 while distance is metric`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
before = deepcopy(parcels)
result = _enrich(parcels=parcels)
assert_geodataframe_equal(result.parcels, before)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.crs == parcels.crs
assert result.parcels.crs.to_epsg() == 4326
assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `test_each_eligible_class_has_independent_distance`

**Purpose**

Exercises `each eligible class has independent distance`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
distances = {
        road_class: _row(result, road_class).nearest_road_proxy_distance_m
        for road_class in ELIGIBLE_CLASSES
    }
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
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

**Regression protected**

Locks `each eligible class has independent distance` through the exact asserted conditions: `distances == pytest.approx({'GENERAL_VEHICLE_PROXY': 10.0, 'LIMITED_VEHICLE_PROXY': 20.0, 'RESTRICTED_REVIEW': 5.0, 'NOT_GENERAL_VEHICLE_PROXY': 30.0, 'UNKNOWN_REVIEW': 40.0}, abs=1e-05)`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_near_not_distance_road_cannot_change_general_distance`

**Purpose**

Exercises `near not distance road cannot change general distance`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        result, "GENERAL_VEHICLE_PROXY"
    ).nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
assert "ROAD-NOT-DISTANCE" not in set(
        result.class_proximity.nearest_road_feature_id.dropna()
    )
```

**Regression protected**

Locks `near not distance road cannot change general distance` through the exact asserted conditions: `_row(result, 'GENERAL_VEHICLE_PROXY').nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-05)`; `'ROAD-NOT-DISTANCE' not in set(result.class_proximity.nearest_road_feature_id.dropna())`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_single_nearest_road_has_tie_count_one`

**Purpose**

Exercises `single nearest road has tie count one`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
assert _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_tie_count == 1
```

**Regression protected**

Locks `single nearest road has tie count one` through the exact asserted conditions: `_row(_enrich(), 'GENERAL_VEHICLE_PROXY').nearest_road_tie_count == 1`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_single_nearest_road_has_tie_count_one() -> None:
    assert _row(
        _enrich(), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_tie_count == 1
```

### `test_exact_tie_counts_two_and_lexical_id_wins`

**Purpose**

Exercises `exact tie counts two and lexical id wins`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", -10, identifier="Z-ROAD"),
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="A-ROAD"),
        ]
    )
row = _row(_enrich(roads=roads), "GENERAL_VEHICLE_PROXY")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-5)
assert row.nearest_road_tie_count == 2
assert row.nearest_road_feature_id == "A-ROAD"
```

**Regression protected**

Locks `exact tie counts two and lexical id wins` through the exact asserted conditions: `row.nearest_road_proxy_distance_m == pytest.approx(10.0, abs=1e-05)`; `row.nearest_road_tie_count == 2`; `row.nearest_road_feature_id == 'A-ROAD'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_tie_winner_is_independent_of_source_order`

**Purpose**

Exercises `tie winner is independent of source order`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert forward.nearest_road_feature_id == "A-ROAD"
assert reverse.nearest_road_feature_id == "A-ROAD"
assert forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2
```

**Regression protected**

Locks `tie winner is independent of source order` through the exact asserted conditions: `forward.nearest_road_feature_id == 'A-ROAD'`; `reverse.nearest_road_feature_id == 'A-ROAD'`; `forward.nearest_road_tie_count == reverse.nearest_road_tie_count == 2`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_unequal_distance_wins_regardless_of_identifier`

**Purpose**

Exercises `unequal distance wins regardless of identifier`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="Z-NEAR"),
            _road_row("GENERAL_VEHICLE_PROXY", 30, identifier="A-FAR"),
        ]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_feature_id == "Z-NEAR"
```

**Regression protected**

Locks `unequal distance wins regardless of identifier` through the exact asserted conditions: `_row(_enrich(roads=roads), 'GENERAL_VEHICLE_PROXY').nearest_road_feature_id == 'Z-NEAR'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unequal_distance_wins_regardless_of_identifier() -> None:
    roads = _roads(
        [
            _road_row("GENERAL_VEHICLE_PROXY", 20, identifier="Z-NEAR"),
            _road_row("GENERAL_VEHICLE_PROXY", 30, identifier="A-FAR"),
        ]
    )

    assert _row(
        _enrich(roads=roads), "GENERAL_VEHICLE_PROXY"
    ).nearest_road_feature_id == "Z-NEAR"
```

### `test_empty_eligible_class_emits_null_row_per_parcel`

**Purpose**

Exercises `empty eligible class emits null row per parcel`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads().loc[
        ~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")
    ].reset_index(drop=True)
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
coverage = {item.road_proxy_class: item for item in result.class_coverage}
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(rows) == 2
assert rows.loc[:, list(SELECTED_COLUMNS)].isna().all().all()
assert coverage["UNKNOWN_REVIEW"].feature_count == 0
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_empty_eligible_class_emits_null_row_per_parcel() -> None:
    roads = _roads().loc[
        ~_roads()["road_proxy_class"].eq("UNKNOWN_REVIEW")
    ].reset_index(drop=True)
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

### `test_output_shape_columns_and_order_are_deterministic`

**Purpose**

Exercises `output shape columns and order are deterministic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [
            Polygon([(50, 0), (50, 10), (60, 10), (60, 0), (50, 0)]),
            Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
result = _enrich(parcels=parcels)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.class_proximity) == len(parcels) * 5
assert list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)
assert result.class_proximity.parcel_id.tolist() == [
        value for parcel_id in ("SECOND", "FIRST") for value in [parcel_id] * 5
    ]
assert result.class_proximity.road_proxy_class.tolist() == list(
        ELIGIBLE_CLASSES
    ) * 2
```

**Regression protected**

Locks `output shape columns and order are deterministic` through the exact asserted conditions: `len(result.class_proximity) == len(parcels) * 5`; `list(result.class_proximity.columns) == list(CLASS_PROXIMITY_COLUMNS)`; `result.class_proximity.parcel_id.tolist() == [value for parcel_id in ('SECOND', 'FIRST') for value in [parcel_id] * 5]`; `result.class_proximity.road_proxy_class.tolist() == list(ELIGIBLE_CLASSES) * 2`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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
    assert result.class_proximity.road_proxy_class.tolist() == list(
        ELIGIBLE_CLASSES
    ) * 2
```

### `test_class_coverage_is_complete_and_strict`

**Purpose**

Exercises `class coverage is complete and strict`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(item.road_proxy_class for item in result.class_coverage) == (
        ALL_CLASSES
    )
assert sum(item.feature_count for item in result.class_coverage) == 6
assert all(
        item.distance_eligible == (item.road_proxy_class != "NOT_DISTANCE_PROXY")
        for item in result.class_coverage
    )
```

**Regression protected**

Locks `class coverage is complete and strict` through the exact asserted conditions: `tuple((item.road_proxy_class for item in result.class_coverage)) == ALL_CLASSES`; `sum((item.feature_count for item in result.class_coverage)) == 6`; `all((item.distance_eligible == (item.road_proxy_class != 'NOT_DISTANCE_PROXY') for item in result.class_coverage))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_selected_road_evidence_and_lineage_are_exact`

**Purpose**

Exercises `selected road evidence and lineage are exact`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
row = _row(_enrich(), "GENERAL_VEHICLE_PROXY")
```

**Action**

```python
policy = load_ign_road_vehicle_proxy_policy()
```

**Expected result**

```python
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

**Regression protected**

Locks `selected road evidence and lineage are exact` through the exact asserted conditions: `row.nearest_road_feature_id == 'ROAD-GENERAL'`; `row.nearest_source_feature_id == 'SOURCE-ROAD-GENERAL'`; `row.nearest_road_primary_rule == 'OPEN_OR_TOLL'`; `row.nearest_road_rule_trace_json == '["OPEN_OR_TOLL"]'`; plus 8 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_parcels_and_road_application_are_not_mutated`

**Purpose**

Exercises `parcels and road application are not mutated`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(index=[777])
roads = _roads()
parcels_before = deepcopy(parcels)
roads_before = deepcopy(roads)
result = _enrich(parcels=parcels, roads=roads)
assert_geodataframe_equal(parcels, parcels_before)
assert_geodataframe_equal(roads, roads_before)
assert_geodataframe_equal(result.parcels, parcels_before)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.index.equals(parcels.index)
assert list(result.parcels.columns) == list(parcels.columns)
assert result.parcels.dtypes.equals(parcels.dtypes)
assert result.parcels.geometry.to_wkb().equals(parcels.geometry.to_wkb())
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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

### `_corrupt_nearest_output`

**Exact signature**

```python
def _corrupt_nearest_output(column: str, value: object) -> None:
```

**Purpose**

Private `test` helper for corrupt nearest output; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `output['distance_m'].notna`, `output['distance_m'].notna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output.at[0, column]`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_enrich_road_proximity.py::test_malformed_produced_distance_is_rejected` via `_corrupt_nearest_output`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_malformed_produced_tie_count_is_rejected` via `_corrupt_nearest_output`.

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

    with patch.object(module, "_nearest_class_rows", side_effect=corrupted), pytest.raises(
        RoadProximityError
    ):
        _enrich()
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_corrupt_nearest_output.corrupted`

**Exact signature**

```python
def corrupted(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for corrupted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `output['distance_m'].notna`, `output['distance_m'].notna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output.at[0, column]`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_enrich_road_proximity.py::_corrupt_nearest_output` via `patch.object(module, '_nearest_class_rows', side_effect=corrupted)`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_produced_distance_is_rejected`

**Purpose**

Exercises `malformed produced distance is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
_corrupt_nearest_output("distance_m", value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `malformed produced distance is rejected` by requiring the reproduced call path `pytest.mark.parametrize`, `_corrupt_nearest_output`, `float`, `float` without an unasserted exception.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_produced_distance_is_rejected(value: object) -> None:
    _corrupt_nearest_output("distance_m", value)
```

### `test_malformed_produced_tie_count_is_rejected`

**Purpose**

Exercises `malformed produced tie count is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
_corrupt_nearest_output("tie_count", value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `malformed produced tie count is rejected` by requiring the reproduced call path `pytest.mark.parametrize`, `_corrupt_nearest_output` without an unasserted exception.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_produced_tie_count_is_rejected(value: object) -> None:
    _corrupt_nearest_output("tie_count", value)
```

### `test_result_dataclasses_are_frozen`

**Purpose**

Exercises `result dataclasses are frozen`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
coverage = result.class_coverage[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()
with pytest.raises(FrozenInstanceError):
        coverage.feature_count = 99
```

**Regression protected**

Locks `result dataclasses are frozen`: the reproduced adversarial input must raise `FrozenInstanceError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_dataclasses_are_frozen() -> None:
    result = _enrich()
    coverage = result.class_coverage[0]

    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        coverage.feature_count = 99
```

### `test_no_business_decision_columns_or_implementation_exist`

**Purpose**

Exercises `no business decision columns or implementation exist`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
source = Path("src/landscout/stages/enrich_road_proximity.py").read_text(
        encoding="utf-8"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert forbidden.isdisjoint(result.parcels.columns)
assert forbidden.isdisjoint(result.class_proximity.columns)
assert ".iterrows(" not in source
```

**Regression protected**

Locks `no business decision columns or implementation exist` through the exact asserted conditions: `forbidden.isdisjoint(result.parcels.columns)`; `forbidden.isdisjoint(result.class_proximity.columns)`; `'.iterrows(' not in source`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_result_parcel_frame_is_an_independent_copy`

**Purpose**

Exercises `result parcel frame is an independent copy`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
result = _enrich(parcels=parcels)
result.parcels.loc[result.parcels.index[0], "source_value"] = 999
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parcels.iloc[0].source_value == 0
```

**Regression protected**

Locks `result parcel frame is an independent copy` through the exact asserted conditions: `parcels.iloc[0].source_value == 0`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_parcel_frame_is_an_independent_copy() -> None:
    parcels = _parcels()
    result = _enrich(parcels=parcels)
    result.parcels.loc[result.parcels.index[0], "source_value"] = 999

    assert parcels.iloc[0].source_value == 0
```

### `test_class_proximity_is_plain_dataframe`

**Purpose**

Exercises `class proximity is plain dataframe`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert type(result.class_proximity) is pd.DataFrame
assert not isinstance(result.class_proximity, gpd.GeoDataFrame)
```

**Regression protected**

Locks `class proximity is plain dataframe` through the exact asserted conditions: `type(result.class_proximity) is pd.DataFrame`; `not isinstance(result.class_proximity, gpd.GeoDataFrame)`.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_class_proximity_is_plain_dataframe() -> None:
    result = _enrich()

    assert type(result.class_proximity) is pd.DataFrame
    assert not isinstance(result.class_proximity, gpd.GeoDataFrame)
```

### `test_selected_rows_belong_to_requested_class`

**Purpose**

Exercises `selected rows belong to requested class`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
road_classes = _roads().set_index("road_feature_id")["road_proxy_class"]
selected = result.class_proximity.dropna(subset=["nearest_road_feature_id"])
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert all(
        road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class
        for row in selected.itertuples(index=False)
    )
```

**Regression protected**

Locks `selected rows belong to requested class` through the exact asserted conditions: `all((road_classes.loc[row.nearest_road_feature_id] == row.road_proxy_class for row in selected.itertuples(index=False)))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_sha_mismatch_does_not_construct_spatial_index`

**Purpose**

Exercises `policy sha mismatch does not construct spatial index`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = _roads()
roads["road_proxy_policy_config_sha256"] = "b" * 64
spatial_index.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        _enrich(roads=roads)
```

**Regression protected**

Locks `policy sha mismatch does not construct spatial index`: the reproduced adversarial input must raise `RoadProximityError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_policy_sha_mismatch_does_not_construct_spatial_index() -> None:
    roads = _roads()
    roads["road_proxy_policy_config_sha256"] = "b" * 64

    with patch(
        "landscout.stages.enrich_road_proximity.STRtree"
    ) as spatial_index, pytest.raises(RoadProximityError):
        _enrich(roads=roads)

    spatial_index.assert_not_called()
```

### `test_matched_output_dtypes_are_stable`

**Purpose**

Exercises `matched output dtypes are stable`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _enrich()
table = result.class_proximity
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"
assert str(table.nearest_road_tie_count.dtype) == "Int64"
assert str(table.nearest_road_toll_evidence.dtype) == "boolean"
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_matched_output_dtypes_are_stable() -> None:
    result = _enrich()
    table = result.class_proximity

    assert str(table.nearest_road_proxy_distance_m.dtype) == "float64"
    assert str(table.nearest_road_tie_count.dtype) == "Int64"
    assert str(table.nearest_road_toll_evidence.dtype) == "boolean"
```

### `test_parcel_preservation_uses_exact_non_geometry_values`

**Purpose**

Exercises `parcel preservation uses exact non geometry values`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
result = _enrich(parcels=parcels)
assert_frame_equal(
        pd.DataFrame(result.parcels.drop(columns="geometry")),
        pd.DataFrame(parcels.drop(columns="geometry")),
        check_dtype=True,
        check_index_type=True,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

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


## 7. Data contracts

### `SELECTED_COLUMNS` — canonical or derived frame-column schema

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
