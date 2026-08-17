# `src/landscout/stages/enrich_road_proximity.py`

## File identity

- Repository path: `src/landscout/stages/enrich_road_proximity.py`
- File type: Python source
- Layer: spatial proxy enrichment stage
- Domain: road
- Responsibility: Computes per-class parcel-to-road proxy proximity using source-bound policy application results.
- Source SHA256: `01bc54d789f3f3dca1d3e62c93aee4c686233b079025d1d96e01169523e56dfa`

## 1. Purpose

Computes per-class parcel-to-road proxy proximity using source-bound policy application results.

## 2. Position in LandScout architecture

This file belongs to the **spatial proxy enrichment stage** layer and the **road** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

#### `_PARCEL_STORAGE_CRS`

```python
_PARCEL_STORAGE_CRS = "EPSG:4326"
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary.

#### `_CALCULATION_CRS`

```python
_CALCULATION_CRS = "EPSG:2154"
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` (value reference).

#### `_PROXIMITY_SCOPE`

```python
_PROXIMITY_SCOPE = "WITHIN_VERIFIED_SOURCE_PACKAGE"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_road_proximity.py::_class_proximity_table` (value reference), `src/landscout/stages/enrich_road_proximity.py::_validate_result` (value reference).

#### `_PARCEL_GEOMETRY_TYPES`

```python
_PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_road_proximity.py::_validate_parcels` (value reference).

#### `_ROAD_GEOMETRY_TYPES`

```python
_ROAD_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` (value reference).

#### `_ROAD_GEOMETRY_STATUSES`

```python
_ROAD_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` (value reference).

#### `_ROAD_MATCH_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_road_proximity.py::<module>` (value reference), `src/landscout/stages/enrich_road_proximity.py::_empty_nearest_rows` (value reference), `src/landscout/stages/enrich_road_proximity.py::_nearest_class_rows` (value reference).

#### `_ROAD_REQUIRED_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` (value reference).

#### `_MATCH_OUTPUT_MAPPING`

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

Explicit mapping between source/input and target/output fields; keys and values are documented separately. Consumers include `src/landscout/stages/enrich_road_proximity.py::_class_proximity_table` (value reference), `src/landscout/stages/enrich_road_proximity.py::_validate_selected_evidence` (value reference), `src/landscout/stages/enrich_road_proximity.py::_validate_result` (value reference).

#### `CLASS_PROXIMITY_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::<module>` (import), `tests/unit/test_assess_road_proximity_coverage.py::<module>` (import), `tests/unit/test_enrich_road_proximity.py::<module>` (import), `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` (value reference), `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` (value reference), `src/landscout/stages/enrich_road_proximity.py::_class_proximity_table` (value reference), `src/landscout/stages/enrich_road_proximity.py::_validate_result` (value reference), `tests/unit/test_assess_road_proximity_coverage.py::_proximity` (value reference), `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` (value reference), `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "ParcelRoadProximityResult",
    "RoadProximityError",
    "RoadProxyClassCoverage",
    "enrich_parcel_road_proximity",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `RoadProximityError`

**Purpose:** Raised when parcel-to-road proximity cannot be proven safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`.
- import: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validated_crs` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_require_crs` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_exact_ids` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_parcels` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_policy_classes` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_require_row_lineage` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_nearest_class_rows` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_distance_and_ties` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_selected_evidence` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_coverage` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_parcel_preservation` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `RoadProximityError`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::enrich_parcel_road_proximity` via `RoadProximityError`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_wrong_road_source_type_has_controlled_error` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_independent_policy_sha_mismatch_is_rejected` via `pytest.raises(RoadProximityError, match='policy|SHA|lineage')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_invalid_parcel_identity_is_rejected` via `pytest.raises(RoadProximityError, match=message)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_id_is_rejected` via `pytest.raises(RoadProximityError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_duplicate_parcel_columns_are_rejected` via `pytest.raises(RoadProximityError, match='duplicate')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_missing_or_inactive_geometry_is_rejected` via `pytest.raises(RoadProximityError, match='geometry')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_missing_or_inactive_geometry_is_rejected` via `pytest.raises(RoadProximityError, match='active')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `pytest.raises(RoadProximityError, match='CRS')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `pytest.raises(RoadProximityError, match='4326')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_geometry_kind_is_rejected` via `pytest.raises(RoadProximityError, match='Polygon|MultiPolygon')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_bad_parcel_geometry_is_rejected` via `pytest.raises(RoadProximityError, match=message)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_duplicate_road_feature_id_is_rejected` via `pytest.raises(RoadProximityError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_unknown_road_proxy_class_is_rejected` via `pytest.raises(RoadProximityError, match='class')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_missing_road_policy_lineage_is_rejected` via `pytest.raises(RoadProximityError, match='column|lineage')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_requires_valid_geometry_status` via `pytest.raises(RoadProximityError, match='VALID')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_eligible_class_rejects_unsupported_geometry` via `pytest.raises(RoadProximityError, match='LineString|geometry')`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::_corrupt_nearest_output` via `pytest.raises(RoadProximityError)`.
- expected exception type: `tests/unit/test_enrich_road_proximity.py::test_policy_sha_mismatch_does_not_construct_spatial_index` via `pytest.raises(RoadProximityError)`.

**Exact class source**

```python
class RoadProximityError(ValueError):
    """Raised when parcel-to-road proximity cannot be proven safely."""
```

### `RoadProxyClassCoverage`

**Purpose:** Source coverage and distance eligibility for one policy class.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `road_proxy_class` | `road_proxy_class: str` | `RoadProxyClassCoverage.road_proxy_class` represents the `road_proxy_class` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `feature_count` | `feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `distance_eligible` | `distance_eligible: bool` | Boolean `distance eligible` flag on `RoadProxyClassCoverage`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::RoadProximityCoverageAssessmentResult` via `RoadProxyClassCoverage`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_match_rows` via `RoadProxyClassCoverage`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::ParcelRoadProximityResult` via `RoadProxyClassCoverage`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_coverage` via `RoadProxyClassCoverage`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_coverage` via `RoadProxyClassCoverage`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_validate_coverage` via `RoadProxyClassCoverage`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `RoadProxyClassCoverage`.

**Exact class source**

```python
class RoadProxyClassCoverage:
    """Source coverage and distance eligibility for one policy class."""

    road_proxy_class: str
    feature_count: int
    distance_eligible: bool
```

### `ParcelRoadProximityResult`

**Purpose:** Unchanged parcels plus class-specific factual road proximity.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `class_proximity` | `class_proximity: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `class_coverage` | `class_coverage: tuple[RoadProxyClassCoverage, ...]` | `ParcelRoadProximityResult.class_coverage` represents the `class_coverage` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
)`.
- import: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `ParcelRoadProximityResult`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `ParcelRoadProximityResult`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `ParcelRoadProximityResult`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `ParcelRoadProximityResult`.
- constructor call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `ParcelRoadProximityResult`.
- type annotation: `src/landscout/stages/enrich_road_proximity.py::enrich_parcel_road_proximity` via `ParcelRoadProximityResult`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `ParcelRoadProximityResult`.
- constructor call: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `ParcelRoadProximityResult`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_without_match` via `ParcelRoadProximityResult`.
- type annotation: `tests/unit/test_enrich_road_proximity.py::_enrich` via `ParcelRoadProximityResult`.
- type annotation: `tests/unit/test_enrich_road_proximity.py::_row` via `ParcelRoadProximityResult`.

**Exact class source**

```python
class ParcelRoadProximityResult:
    """Unchanged parcels plus class-specific factual road proximity."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]
```


## 6. Functions and methods

### `_validated_crs`

**Exact signature**

```python
def _validated_crs(value: object, label: str) -> CRS:
```

**Purpose**

Checks and returns canonical crs; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
CRS.from_user_input(value)
```

**Validation and exceptions**

- Guard with a raise path: `value is None`.
- Explicit raise expressions: `RoadProximityError(f'{label} CRS is required')`, `RoadProximityError(f'{label} CRS is unreadable')`.

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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_require_crs` via `_validated_crs`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_parcel_preservation` via `_validated_crs`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_crs`

**Exact signature**

```python
def _require_crs(value: object, expected_epsg: int, label: str) -> None:
```

**Purpose**

Private `road` helper for require crs; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not actual.equals(expected)`.
- Explicit raise expressions: `RoadProximityError(f'{label} must use EPSG:{expected_epsg}')`.

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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_parcels` via `_require_crs`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` via `_require_crs`.

**Complete source-ordered implementation**

```python
def _require_crs(value: object, expected_epsg: int, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityError(f"{label} must use EPSG:{expected_epsg}")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_exact_ids`

**Exact signature**

```python
def _validate_exact_ids(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent exact ids; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `values.isna().any()`.
- Guard with a raise path: `any((not isinstance(value, str) for value in raw))`.
- Guard with a raise path: `any((not value.strip() for value in raw))`.
- Guard with a raise path: `any((value != value.strip() for value in raw))`.
- Guard with a raise path: `require_unique and values.duplicated().any()`.
- Explicit raise expressions: `RoadProximityError(f'{label} values must be exact strings')`, `RoadProximityError(f'{label} values must be unique')`, `RoadProximityError(f'{label} values must not be empty')`, `RoadProximityError(f'{label} values must not be null')`, `RoadProximityError(f'{label} values must not have edge whitespace')`.

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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_parcels` via `_validate_exact_ids`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` via `_validate_exact_ids`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_parcels`

**Exact signature**

```python
def _validate_parcels(parcels: object) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent parcels; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
parcels
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `parcels.columns.duplicated().any()`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `parcels.active_geometry_name != 'geometry'`.
- Guard with a raise path: `parcels.geometry.isna().any()`.
- Guard with a raise path: `parcels.geometry.is_empty.any()`.
- Guard with a raise path: `not parcels.geometry.is_valid.all()`.
- Guard with a raise path: `unsupported`.
- Explicit raise expressions: `RoadProximityError('Missing required parcel columns: ' + ', '.join(sorted(missing)))`, `RoadProximityError('Parcel columns must not contain duplicates')`, `RoadProximityError('Parcel geometries must be Polygon or MultiPolygon; found: ' + ', '.join((str(value) for value in unsupported)))`, `RoadProximityError('Parcel geometries must be valid')`, `RoadProximityError('Parcel geometries must not be empty')`, `RoadProximityError('Parcel geometries must not be null')`, `RoadProximityError('Parcel geometry column must be active')`, `RoadProximityError('parcels must be a GeoDataFrame')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `parcels.geometry.geom_type.dropna`, `parcels.geometry.is_empty.any`, `parcels.geometry.is_valid.all`, `parcels.geometry.isna`, `parcels.geometry.isna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_validate_parcels`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_policy_classes`

**Exact signature**

```python
def _policy_classes(
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
```

**Purpose**

Private `road` helper for policy classes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[tuple[str, ...], tuple[str, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(all_classes, eligible)
```

**Validation and exceptions**

- Guard with a raise path: `len(all_classes) != 6 or len(set(all_classes)) != 6`.
- Guard with a raise path: `len(eligible) != 5 or non_distance not in all_classes`.
- Explicit raise expressions: `RoadProximityError('Compiled road distance eligibility is invalid')`, `RoadProximityError('Compiled road policy class domain is invalid')`.

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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` via `_policy_classes`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_coverage` via `_policy_classes`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_class_proximity_table` via `_policy_classes`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_coverage` via `_policy_classes`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_row_lineage`

**Exact signature**

```python
def _require_row_lineage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> None:
```

**Purpose**

Private `road` helper for require row lineage; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `roads[column].isna().any() or not roads[column].eq(value).all()`.
- Explicit raise expressions: `RoadProximityError(f'Road application policy lineage differs in {column}')`.

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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_application_roads` via `_require_row_lineage`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_application_roads`

**Exact signature**

```python
def _validate_application_roads(
    application: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent application roads; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
roads
```

**Validation and exceptions**

- Guard with a raise path: `type(application) is not IgnRoadVehicleProxyApplicationResult`.
- Guard with a raise path: `not isinstance(roads, gpd.GeoDataFrame)`.
- Guard with a raise path: `roads.columns.duplicated().any()`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `roads.active_geometry_name != 'geometry'`.
- Guard with a raise path: `classes.isna().any() or not classes.isin(all_classes).all()`.
- Guard with a raise path: `statuses.isna().any() or not statuses.isin(_ROAD_GEOMETRY_STATUSES).all()`.
- Guard with a raise path: `not statuses.loc[eligible].eq('VALID').all()`.
- Guard with a raise path: `eligible_geometry.isna().any()`.
- Guard with a raise path: `eligible_geometry.is_empty.any()`.
- Guard with a raise path: `not eligible_geometry.is_valid.all()`.
- Guard with a raise path: `unsupported`.
- Explicit raise expressions: `RoadProximityError('Distance-eligible geometry must be LineString or MultiLineString; found: ' + ', '.join((str(value) for value in unsupported)))`, `RoadProximityError('Distance-eligible road geometry must be valid')`, `RoadProximityError('Distance-eligible road geometry must not be empty')`, `RoadProximityError('Distance-eligible road geometry must not be null')`, `RoadProximityError('Distance-eligible roads must have VALID geometry status')`, `RoadProximityError('Missing road application column or lineage: ' + ', '.join(sorted(missing)))`, `RoadProximityError('Road application columns must not be duplicated')`, `RoadProximityError('Road application geometry must be active')`, `RoadProximityError('Road application geometry status is invalid')`, `RoadProximityError('Road application has an unknown proxy class')`, `RoadProximityError('Road application result type is invalid')`, `RoadProximityError('Road application roads must be a GeoDataFrame')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `eligible_geometry.geom_type.dropna`, `eligible_geometry.is_empty.any`, `eligible_geometry.is_valid.all`, `eligible_geometry.isna`, `eligible_geometry.isna().any`, `statuses.isin(_ROAD_GEOMETRY_STATUSES).all`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_validate_application_roads`.

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
            "Missing road application column or lineage: "
            + ", ".join(sorted(missing))
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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_calculation_geometries`

**Exact signature**

```python
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
```

**Purpose**

Private `road` helper for calculation geometries; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `np.ndarray`.
- Every observed return expression is reproduced without truncation:
```python
np.asarray(force_2d(values), dtype=object)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `force_2d`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_nearest_class_rows` via `_calculation_geometries`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_calculation_geometries`.

**Complete source-ordered implementation**

```python
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_empty_nearest_rows`

**Exact signature**

```python
def _empty_nearest_rows(parcel_count: int) -> pd.DataFrame:
```

**Purpose**

Private `road` helper for empty nearest rows; its complete implementation below is the authoritative behavioral contract.

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
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output['distance_m']`, `output['tie_count']`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_nearest_class_rows` via `_empty_nearest_rows`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_nearest_class_rows`

**Exact signature**

```python
def _nearest_class_rows(
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Private `road` helper for nearest class rows; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output

_empty_nearest_rows(parcel_count)
```

**Validation and exceptions**

- Guard with a raise path: `selected['parcel_position'].tolist() != list(range(parcel_count))`.
- Explicit raise expressions: `RoadProximityError('Nearest-road matching did not cover every parcel')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `STRtree`, `selected['distance_m'].to_numpy`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `matches['road_feature_id']`, `output`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_class_proximity_table` via `_nearest_class_rows`.

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
    matches["road_feature_id"] = roads.iloc[
        matches["road_position"].to_numpy()
    ]["road_feature_id"].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "road_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position", kind="mergesort"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise RoadProximityError(
            "Nearest-road matching did not cover every parcel"
        )

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_coverage`

**Exact signature**

```python
def _coverage(
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[RoadProxyClassCoverage, ...]:
```

**Purpose**

Private `road` helper for coverage; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[RoadProxyClassCoverage, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple((RoadProxyClassCoverage(road_proxy_class=road_class, feature_count=int(counts.get(road_class, 0)), distance_eligible=road_class in eligible_classes) for road_class in all_classes))
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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_coverage`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_class_proximity_table`

**Exact signature**

```python
def _class_proximity_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> pd.DataFrame:
```

**Purpose**

Private `road` helper for class proximity table; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_validate_distance_and_ties`, `output['nearest_road_proxy_distance_m'].astype`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output['nearest_road_proxy_distance_m']`, `output['nearest_road_tie_count']`, `output['nearest_road_toll_evidence']`, `table['proximity_scope']`, `table['road_proxy_heavy_vehicle_access']`, `table['road_proxy_policy_config_sha256']`, `table['road_proxy_policy_id']`, `table['road_proxy_policy_schema_version']`, `table[output_column]`, `tables`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_class_proximity_table`.

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
        class_roads = roads.loc[
            roads["road_proxy_class"].eq(road_class)
        ].reset_index(drop=True)
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
    output["nearest_road_tie_count"] = output["nearest_road_tie_count"].astype(
        "Int64"
    )
    output["nearest_road_toll_evidence"] = output[
        "nearest_road_toll_evidence"
    ].astype("boolean")
    return output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_is_missing_scalar`

**Exact signature**

```python
def _is_missing_scalar(value: object) -> bool:
```

**Purpose**

Tests whether missing scalar; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
True

bool(pd.isna(value))

False
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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_distance_and_ties` via `_is_missing_scalar`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_distance_and_ties`

**Exact signature**

```python
def _validate_distance_and_ties(
    rows: pd.DataFrame,
    *,
    expect_matches: bool,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent distance and ties; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `expect_matches and (not matched.all())`.
- Guard with a raise path: `not expect_matches and matched.any()`.
- Guard with a raise path: `matched.any()`.
- Guard with a raise path: `not is_numeric_dtype(distances.dtype) or is_bool_dtype(distances.dtype)`.
- Guard with a raise path: `not np.isfinite(numeric).all() or (numeric < 0).any()`.
- Guard with a raise path: `not row_matched`.
- Guard with a raise path: `missing or not isinstance(value, Integral) or isinstance(value, (bool, np.bool_)) or (int(value) < 1)`.
- Guard with a raise path: `not missing`.
- Explicit raise expressions: `RoadProximityError('Empty road classes must not contain matches')`, `RoadProximityError('Matched nearest_road_tie_count must be an integer >= 1')`, `RoadProximityError('Matched road distances must be finite and >= 0')`, `RoadProximityError('Matched road distances must be numeric')`, `RoadProximityError('Non-empty road classes require parcel matches')`, `RoadProximityError('Unmatched rows require null tie_count')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `distances.loc[matched].to_numpy`, `distances.notna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_class_proximity_table` via `_validate_distance_and_ties`.
- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `_validate_distance_and_ties`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_null_safe_equal`

**Exact signature**

```python
def _null_safe_equal(actual: pd.Series, expected: pd.Series) -> bool:
```

**Purpose**

Private `road` helper for null safe equal; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
bool((both_null | equal).all())

False

False
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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_selected_evidence` via `_null_safe_equal`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_selected_evidence`

**Exact signature**

```python
def _validate_selected_evidence(
    table: pd.DataFrame,
    roads: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent selected evidence; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
None
```

**Validation and exceptions**

- Guard with a raise path: `(positions < 0).any()`.
- Guard with a raise path: `not selected['road_proxy_class'].reset_index(drop=True).eq(expected['road_proxy_class']).all()`.
- Guard with a raise path: `not _null_safe_equal(selected[output_column], expected[source_column])`.
- Explicit raise expressions: `RoadProximityError('Selected nearest road ID is absent from source')`, `RoadProximityError('Selected nearest road has the wrong proxy class')`, `RoadProximityError(f'Selected nearest road evidence differs for {output_column}')`.

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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `_validate_selected_evidence`.

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
    if not selected["road_proxy_class"].reset_index(drop=True).eq(
        expected["road_proxy_class"]
    ).all():
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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_coverage`

**Exact signature**

```python
def _validate_coverage(
    coverage: tuple[RoadProxyClassCoverage, ...],
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
```

**Purpose**

Rejects malformed or inconsistent coverage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
eligible_classes
```

**Validation and exceptions**

- Guard with a raise path: `type(coverage) is not tuple or len(coverage) != len(all_classes)`.
- Guard with a raise path: `total != len(roads)`.
- Guard with a raise path: `type(item) is not RoadProxyClassCoverage`.
- Guard with a raise path: `item.road_proxy_class != road_class`.
- Guard with a raise path: `type(item.feature_count) is not int or item.feature_count < 0`.
- Guard with a raise path: `type(item.distance_eligible) is not bool`.
- Guard with a raise path: `item.distance_eligible != (road_class in eligible_classes)`.
- Guard with a raise path: `item.feature_count != int(counts.get(road_class, 0))`.
- Explicit raise expressions: `RoadProximityError('Road class coverage does not sum to source rows')`, `RoadProximityError('Road class coverage entry type is invalid')`, `RoadProximityError('Road class coverage is incomplete')`, `RoadProximityError('Road class coverage order is invalid')`, `RoadProximityError('Road class distance eligibility is invalid')`, `RoadProximityError('Road class distance_eligible must be Boolean')`, `RoadProximityError('Road class feature_count differs from source')`, `RoadProximityError('Road class feature_count must be an integer >= 0')`.

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

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `_validate_coverage`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_parcel_preservation`

**Exact signature**

```python
def _validate_parcel_preservation(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent parcel preservation; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `len(output) != len(source)`.
- Guard with a raise path: `list(output.columns) != list(source.columns)`.
- Guard with a raise path: `not output.dtypes.equals(source.dtypes)`.
- Guard with a raise path: `type(output.index) is not type(source.index) or output.index.names != source.index.names or str(output.index.dtype) != str(source.index.dtype) or (not output.index.equals(source.index))`.
- Guard with a raise path: `not _validated_crs(output.crs, 'Output parcel').equals(_validated_crs(source.crs, 'Source parcel'))`.
- Guard with a raise path: `not output.geometry.to_wkb().equals(source.geometry.to_wkb())`.
- Guard with a raise path: `geometry_column is None or not output.drop(columns=geometry_column).equals(source.drop(columns=geometry_column))`.
- Explicit raise expressions: `RoadProximityError('Road proximity changed parcel CRS')`, `RoadProximityError('Road proximity changed parcel columns')`, `RoadProximityError('Road proximity changed parcel count')`, `RoadProximityError('Road proximity changed parcel dtypes')`, `RoadProximityError('Road proximity changed parcel facts')`, `RoadProximityError('Road proximity changed parcel geometry WKB')`, `RoadProximityError('Road proximity changed parcel index metadata')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `output.drop(columns=geometry_column).equals`, `output.geometry.to_wkb`, `output.geometry.to_wkb().equals`, `source.geometry.to_wkb`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_validate_result` via `_validate_parcel_preservation`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_result`

**Exact signature**

```python
def _validate_result(
    source_parcels: gpd.GeoDataFrame,
    roads: gpd.GeoDataFrame,
    policy: IgnRoadVehicleProxyPolicy,
    result: ParcelRoadProximityResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(result) is not ParcelRoadProximityResult`.
- Guard with a raise path: `not isinstance(result.parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `type(result.class_proximity) is not pd.DataFrame`.
- Guard with a raise path: `table.columns.duplicated().any() or list(table.columns) != list(CLASS_PROXIMITY_COLUMNS)`.
- Guard with a raise path: `len(table) != len(source_parcels) * len(eligible_classes)`.
- Guard with a raise path: `table['parcel_id'].tolist() != expected_ids`.
- Guard with a raise path: `table['road_proxy_class'].tolist() != expected_classes`.
- Guard with a raise path: `policy.classes.not_distance_proxy in set(table['road_proxy_class'])`.
- Guard with a raise path: `table.duplicated(['parcel_id', 'road_proxy_class']).any()`.
- Guard with a raise path: `expect_matches`.
- Guard with a raise path: `table[column].isna().any() or not table[column].eq(value).all()`.
- Guard with a raise path: `rows.loc[:, list(_MATCH_OUTPUT_MAPPING.values())].notna().any().any()`.
- Guard with a raise path: `rows[column].isna().any()`.
- Explicit raise expressions: `RoadProximityError('Class proximity class order is invalid')`, `RoadProximityError('Class proximity must be a plain DataFrame')`, `RoadProximityError('Class proximity parcel order is invalid')`, `RoadProximityError('Class proximity parcel/class pairs must be unique')`, `RoadProximityError('Class proximity row count is invalid')`, `RoadProximityError('Class proximity schema is invalid')`, `RoadProximityError('Empty-class selected road evidence must be entirely null')`, `RoadProximityError('NOT_DISTANCE_PROXY cannot have distance rows')`, `RoadProximityError('Road proximity parcels must be a GeoDataFrame')`, `RoadProximityError('Road proximity result type is invalid')`, `RoadProximityError(f'Class proximity lineage differs in {column}')`, `RoadProximityError(f'Matched class rows require {column}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_validate_distance_and_ties`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_validate_result`.

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
    eligible_classes = _validate_coverage(
        result.class_coverage, roads, policy
    )
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
                    raise RoadProximityError(
                        f"Matched class rows require {column}"
                    )
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
            raise RoadProximityError(
                f"Class proximity lineage differs in {column}"
            )
    _validate_selected_evidence(table, roads)
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_enrich_parcel_road_proximity`

**Exact signature**

```python
def _enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Copies input evidence and adds parcel road proximity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `ParcelRoadProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `source_parcels.to_crs`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_road_proximity.py::enrich_parcel_road_proximity` via `_enrich_parcel_road_proximity`.

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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `enrich_parcel_road_proximity`

**Exact signature**

```python
def enrich_parcel_road_proximity(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Compute exact class-specific distance within the verified source package.

**Return contract**

- Declared return annotation: `ParcelRoadProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
_enrich_parcel_road_proximity(parcels, road_source, source_config, policy_path)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `type(road_source) is not IgnBdTopoRoadData`.
- Guard with a raise path: `type(source_config) is not IgnBdTopoSourceConfig`.
- Guard with a raise path: `policy_path is not None and (not isinstance(policy_path, Path))`.
- Explicit raise expressions: `RoadProximityError('Parcel-to-road proximity cannot be computed safely')`, `RoadProximityError('parcels must be a GeoDataFrame with active geometry')`, `RoadProximityError('policy_path must be a pathlib.Path or None')`, `RoadProximityError('road_source must be an IgnBdTopoRoadData')`, `RoadProximityError('source_config must be an IgnBdTopoSourceConfig')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    ParcelRoadProximityResult,
    RoadProximityError,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`.
- import: `src/landscout/stages/assess_road_proximity_coverage.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`.
- import: `tests/unit/test_enrich_road_proximity.py::<module>` via `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProximityError,
    enrich_parcel_road_proximity,
)`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::_enrich` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_road_source_type_has_controlled_error` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected` via `enrich_parcel_road_proximity`.
- direct call: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `enrich_parcel_road_proximity`.

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
            raise RoadProximityError(
                "road_source must be an IgnBdTopoRoadData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise RoadProximityError(
                "source_config must be an IgnBdTopoSourceConfig"
            )
        if policy_path is not None and not isinstance(policy_path, Path):
            raise RoadProximityError(
                "policy_path must be a pathlib.Path or None"
            )
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

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.


## 7. Data contracts

### Frame-preservation and semantic notes

- `CLASS_PROXIMITY_COLUMNS` is the exact parcel-by-eligible-road-class table. `_MATCH_OUTPUT_MAPPING` defines source-match fields renamed to nearest-road output columns. Proxy class values remain row values, not schema fields.

### `_ROAD_MATCH_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `road_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `road_proxy_primary_rule` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `road_proxy_rule_trace_json` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `road_proxy_unknown_fields_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `road_proxy_toll_evidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `private_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `light_vehicle_access_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `carriageway_width_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `closure_period_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `restriction_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `_ROAD_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `carriageway_width_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `closure_period_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 5 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 6 | `importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `light_vehicle_access_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `private_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `restriction_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `road_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 12 | `road_proxy_class` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 13 | `road_proxy_heavy_vehicle_access` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `road_proxy_policy_config_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 15 | `road_proxy_policy_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 16 | `road_proxy_policy_schema_version` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `road_proxy_policy_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `road_proxy_primary_rule` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 19 | `road_proxy_rule_trace_json` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 20 | `road_proxy_toll_evidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 21 | `road_proxy_unknown_fields_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 22 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 24 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 25 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 26 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `_MATCH_OUTPUT_MAPPING` — mapping between source/input and output keys or columns

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

| Source/input key or column | Target/output key or column | Contract |
|---|---|---|
| `distance_m` | `nearest_road_proxy_distance_m` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `road_feature_id` | `nearest_road_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_feature_id` | `nearest_source_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `tie_count` | `nearest_road_tie_count` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `road_proxy_primary_rule` | `nearest_road_primary_rule` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `road_proxy_rule_trace_json` | `nearest_road_rule_trace_json` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `road_proxy_unknown_fields_json` | `nearest_road_unknown_fields_json` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `road_proxy_toll_evidence` | `nearest_road_toll_evidence` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `nature_raw` | `nearest_nature_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `importance_raw` | `nearest_importance_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `asset_status_raw` | `nearest_asset_status_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `private_raw` | `nearest_private_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `light_vehicle_access_raw` | `nearest_light_vehicle_access_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `carriageway_width_raw` | `nearest_carriageway_width_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `closure_period_raw` | `nearest_closure_period_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `restriction_nature_raw` | `nearest_restriction_nature_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_layer` | `nearest_source_layer` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_department_code` | `nearest_source_department_code` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_edition` | `nearest_source_edition` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_archive_sha256` | `nearest_source_archive_sha256` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |

### `CLASS_PROXIMITY_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `road_proxy_class` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `nearest_road_proxy_distance_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 4 | `nearest_road_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 5 | `nearest_source_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 6 | `nearest_road_tie_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 7 | `nearest_road_primary_rule` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 8 | `nearest_road_rule_trace_json` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 9 | `nearest_road_unknown_fields_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `nearest_road_toll_evidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `nearest_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `nearest_importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `nearest_asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `nearest_private_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `nearest_light_vehicle_access_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `nearest_carriageway_width_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `nearest_closure_period_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 18 | `nearest_restriction_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `nearest_source_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 20 | `nearest_source_department_code` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 21 | `nearest_source_edition` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 22 | `nearest_source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `road_proxy_policy_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 24 | `road_proxy_policy_schema_version` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 25 | `road_proxy_policy_config_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 26 | `road_proxy_heavy_vehicle_access` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 27 | `proximity_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `ParcelRoadProximityResult` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_road_proximity.py`` | yes |
| `RoadProximityError` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_road_proximity.py`` | yes |
| `RoadProxyClassCoverage` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_road_proximity.py`` | yes |
| `enrich_parcel_road_proximity` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_road_proximity.py`` | yes |

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

The module contributes to the road flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
