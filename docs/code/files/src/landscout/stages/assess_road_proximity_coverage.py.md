# `src/landscout/stages/assess_road_proximity_coverage.py`

## File identity

- Repository path: `src/landscout/stages/assess_road_proximity_coverage.py`
- File type: Python source
- Layer: diagnostic/profile stage
- Domain: road
- Responsibility: Diagnoses road proxy proximity against the verified IGN department coverage boundary.
- Source SHA256: `ff3fda58bfc1086082d8222ed099f1fae529ec45b05476c90d3177c42c114d2d`

## 1. Purpose

Diagnoses road proxy proximity against the verified IGN department coverage boundary.

## 2. Position in LandScout architecture

This file belongs to the **diagnostic/profile stage** layer and the **road** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import re`
- `import unicodedata`
- `from dataclasses import dataclass`
- `from math import isfinite`
- `from numbers import Integral, Real`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pyproj import CRS`
- `from shapely import (  # type: ignore[import-untyped]
    boundary,
    covers,
    distance,
    force_2d,
    intersects,
)`

### Internal LandScout imports

- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)`
- `from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)`

## 4. Contract taxonomy

### A. Python constants

#### `_CALCULATION_CRS`

```python
_CALCULATION_CRS = "EPSG:2154"
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_parcel_coverage_diagnostics` (value reference).

#### `_PROXIMITY_SCOPE`

```python
_PROXIMITY_SCOPE = "WITHIN_VERIFIED_SOURCE_PACKAGE"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` (value reference).

#### `_COVERAGE_SPATIAL_ROLE`

```python
_COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_coverage_summary` (value reference), `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` (value reference).

#### `_SOURCE_SPATIAL_ROLE`

```python
_SOURCE_SPATIAL_ROLE = "PROXY_GEOMETRY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` (value reference).

#### `_POSITIONS`

```python
_POSITIONS = frozenset(
    {"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"}
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` (value reference).

#### `_STATUSES`

```python
_STATUSES = frozenset(
    {
        "NO_MATCH",
        "NOT_BOUNDARY_LIMITED",
        "BOUNDARY_LIMITED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    }
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` (value reference).

#### `_PARCEL_GEOMETRY_TYPES`

```python
_PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_parcel_frame` (value reference).

#### `_COVERAGE_GEOMETRY_TYPES`

```python
_COVERAGE_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` (value reference).

#### `_SHA256_PATTERN`

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` (value reference).

#### `_IGN_PROVIDER_IDENTITIES`

```python
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institutnationaldelinformationgeographiqueetforestiereign",
    }
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` (value reference).

#### `_COVERAGE_LINEAGE_COLUMNS`

```python
_COVERAGE_LINEAGE_COLUMNS = (
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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::<module>` (value reference).

#### `_DIAGNOSTIC_COLUMNS`

```python
_DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    *_COVERAGE_LINEAGE_COLUMNS,
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_expected_diagnostics` (value reference), `src/landscout/stages/assess_road_proximity_coverage.py::_diagnosed_class_proximity` (value reference), `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` (value reference).

#### `_COVERAGE_FRAME_LINEAGE`

```python
_COVERAGE_FRAME_LINEAGE = (
    "source_provider",
    "source_product",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_archive_sha256",
    "source_layer",
    "spatial_role",
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_coverage_summary` (value reference).

#### `_SELECTED_ROAD_COLUMNS`

```python
_SELECTED_ROAD_COLUMNS = (
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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/assess_road_proximity_coverage.py::_validate_match_rows` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "RoadProximityCoverageAssessmentResult",
    "RoadProximityCoverageError",
    "assess_road_proximity_coverage",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `RoadProximityCoverageError`

**Purpose:** Raised when road source-boundary diagnostics cannot be proven safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validated_crs` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_normalized_identity` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_exact_string` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_exact_ids` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_parcel_frame` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_require_same_parcels` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_finite_nonnegative` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_class_coverage` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_match_rows` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_coverage_summary` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_parcel_coverage_diagnostics` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_selected_road_package` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `RoadProximityCoverageError`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::assess_road_proximity_coverage` via `RoadProximityCoverageError`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast` via `pytest.raises(RoadProximityCoverageError)`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading` via `pytest.raises(RoadProximityCoverageError)`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `pytest.raises(RoadProximityCoverageError)`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `pytest.raises(RoadProximityCoverageError)`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive` via `pytest.raises(RoadProximityCoverageError, match='package|lineage|provider|product')`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `pytest.raises(RoadProximityCoverageError, match='configured|layer')`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_selected_department_identity_is_exact` via `pytest.raises(RoadProximityCoverageError, match='department')`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `pytest.raises(RoadProximityCoverageError, match='spatial|lineage')`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `pytest.raises(RoadProximityCoverageError)`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object` via `pytest.raises(RoadProximityCoverageError, match='extraction')`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_invalid_coverage_geometry_is_rejected` via `pytest.raises(RoadProximityCoverageError, match=message)`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_road_lineage_must_match_coverage` via `pytest.raises(RoadProximityCoverageError, match='lineage|package')`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `pytest.raises(RoadProximityCoverageError)`.
- expected exception type: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `pytest.raises(RoadProximityCoverageError)`.

**Exact class source**

```python
class RoadProximityCoverageError(ValueError):
    """Raised when road source-boundary diagnostics cannot be proven safely."""
```

### `RoadProximityCoverageAssessmentResult`

**Purpose:** Unchanged road proximity plus its source-package boundary diagnosis.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `class_proximity` | `class_proximity: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `class_coverage` | `class_coverage: tuple[RoadProxyClassCoverage, ...]` | `RoadProximityCoverageAssessmentResult.class_coverage` represents the `class_coverage` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `source_coverage` | `source_coverage: IgnBdTopoDepartmentCoverage` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `RoadProximityCoverageAssessmentResult`.
- constructor call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `RoadProximityCoverageAssessmentResult`.
- type annotation: `src/landscout/stages/assess_road_proximity_coverage.py::assess_road_proximity_coverage` via `RoadProximityCoverageAssessmentResult`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `RoadProximityCoverageAssessmentResult`.
- type annotation: `tests/unit/test_assess_road_proximity_coverage.py::_first_row` via `RoadProximityCoverageAssessmentResult`.

**Exact class source**

```python
class RoadProximityCoverageAssessmentResult:
    """Unchanged road proximity plus its source-package boundary diagnosis."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]
    source_coverage: IgnBdTopoDepartmentCoverage
```


## 6. Functions and methods

### `_validated_crs`

**Exact signature**

```python
def _validated_crs(value: object, expected_epsg: int, label: str) -> CRS:
```

**Purpose**

Checks and returns canonical crs; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
actual
```

**Validation and exceptions**

- Guard with a raise path: `value is None`.
- Guard with a raise path: `not actual.equals(expected)`.
- Explicit raise expressions: `RoadProximityCoverageError(f'{label} CRS is required')`, `RoadProximityCoverageError(f'{label} CRS is unreadable')`, `RoadProximityCoverageError(f'{label} must use EPSG:{expected_epsg}')`.

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_parcel_frame` via `_validated_crs`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_require_same_parcels` via `_validated_crs`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_coverage_summary` via `_validated_crs`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_validated_crs`.

**Complete source-ordered implementation**

```python
def _validated_crs(value: object, expected_epsg: int, label: str) -> CRS:
    if value is None:
        raise RoadProximityCoverageError(f"{label} CRS is required")
    try:
        actual = CRS.from_user_input(value)
    except Exception as error:
        raise RoadProximityCoverageError(f"{label} CRS is unreadable") from error
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityCoverageError(
            f"{label} must use EPSG:{expected_epsg}"
        )
    return actual
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_normalized_identity`

**Exact signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

**Purpose**

Private `road` helper for normalized identity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
''.join((character for character in decomposed.casefold() if character.isalnum()))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `RoadProximityCoverageError(f'{label} must be a non-empty exact string')`.

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_normalized_identity`.

**Complete source-ordered implementation**

```python
def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(
            f"{label} must be a non-empty exact string"
        )
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(
        character
        for character in decomposed.casefold()
        if character.isalnum()
    )
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_exact_string`

**Exact signature**

```python
def _exact_string(value: object, label: str) -> str:
```

**Purpose**

Private `road` helper for exact string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `RoadProximityCoverageError(f'{label} must be a non-empty exact string')`.

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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(
            f"{label} must be a non-empty exact string"
        )
    return value
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_null_safe_scalar_equal`

**Exact signature**

```python
def _null_safe_scalar_equal(actual: object, expected: object) -> bool:
```

**Purpose**

Private `road` helper for null safe scalar equal; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
bool(pd.isna(actual))

bool(actual == expected)

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_null_safe_scalar_equal`.

**Complete source-ordered implementation**

```python
def _null_safe_scalar_equal(actual: object, expected: object) -> bool:
    if expected is None:
        return bool(pd.isna(actual))
    try:
        return bool(actual == expected)
    except (TypeError, ValueError):
        return False
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_exact_ids`

**Exact signature**

```python
def _exact_ids(values: pd.Series, label: str) -> None:
```

**Purpose**

Private `road` helper for exact ids; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `values.isna().any()`.
- Guard with a raise path: `any((not isinstance(item, str) for item in items))`.
- Guard with a raise path: `any((not item or item != item.strip() for item in items))`.
- Guard with a raise path: `values.duplicated().any()`.
- Explicit raise expressions: `RoadProximityCoverageError(f'{label} values must be exact strings')`, `RoadProximityCoverageError(f'{label} values must be non-empty without edge whitespace')`, `RoadProximityCoverageError(f'{label} values must be unique')`, `RoadProximityCoverageError(f'{label} values must not be null')`.

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_parcel_frame` via `_exact_ids`.

**Complete source-ordered implementation**

```python
def _exact_ids(values: pd.Series, label: str) -> None:
    if values.isna().any():
        raise RoadProximityCoverageError(f"{label} values must not be null")
    items = values.tolist()
    if any(not isinstance(item, str) for item in items):
        raise RoadProximityCoverageError(f"{label} values must be exact strings")
    if any(not item or item != item.strip() for item in items):
        raise RoadProximityCoverageError(
            f"{label} values must be non-empty without edge whitespace"
        )
    if values.duplicated().any():
        raise RoadProximityCoverageError(f"{label} values must be unique")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_parcel_frame`

**Exact signature**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent parcel frame; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `frame.active_geometry_name != 'geometry'`.
- Guard with a raise path: `geometry.isna().any()`.
- Guard with a raise path: `geometry.is_empty.any()`.
- Guard with a raise path: `not geometry.is_valid.all()`.
- Guard with a raise path: `not set(geometry.geom_type.dropna()) <= _PARCEL_GEOMETRY_TYPES`.
- Explicit raise expressions: `RoadProximityCoverageError(f'{label} columns must be unique')`, `RoadProximityCoverageError(f'{label} geometry must be Polygon or MultiPolygon')`, `RoadProximityCoverageError(f'{label} geometry must be active')`, `RoadProximityCoverageError(f'{label} geometry must be valid')`, `RoadProximityCoverageError(f'{label} geometry must not be empty')`, `RoadProximityCoverageError(f'{label} geometry must not be null')`, `RoadProximityCoverageError(f'{label} is missing: ' + ', '.join(sorted(missing)))`, `RoadProximityCoverageError(f'{label} must be a GeoDataFrame')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `geometry.geom_type.dropna`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `_validate_parcel_frame`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_validate_parcel_frame`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_parcel_frame`.

**Complete source-ordered implementation**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise RoadProximityCoverageError(f"{label} must be a GeoDataFrame")
    if frame.columns.duplicated().any():
        raise RoadProximityCoverageError(f"{label} columns must be unique")
    missing = {"parcel_id", "geometry"} - set(frame.columns)
    if missing:
        raise RoadProximityCoverageError(
            f"{label} is missing: " + ", ".join(sorted(missing))
        )
    if frame.active_geometry_name != "geometry":
        raise RoadProximityCoverageError(f"{label} geometry must be active")
    _validated_crs(frame.crs, 4326, label)
    _exact_ids(frame["parcel_id"], f"{label} parcel_id")
    geometry = frame.geometry
    if geometry.isna().any():
        raise RoadProximityCoverageError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise RoadProximityCoverageError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise RoadProximityCoverageError(f"{label} geometry must be valid")
    if not set(geometry.geom_type.dropna()) <= _PARCEL_GEOMETRY_TYPES:
        raise RoadProximityCoverageError(
            f"{label} geometry must be Polygon or MultiPolygon"
        )
    return frame
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_same_index`

**Exact signature**

```python
def _same_index(left: pd.Index, right: pd.Index) -> bool:
```

**Purpose**

Compares index; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
bool(type(left) is type(right) and left.names == right.names and (str(left.dtype) == str(right.dtype)) and left.equals(right))
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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_require_same_parcels` via `_same_index`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_same_index`.

**Complete source-ordered implementation**

```python
def _same_index(left: pd.Index, right: pd.Index) -> bool:
    return bool(
        type(left) is type(right)
        and left.names == right.names
        and str(left.dtype) == str(right.dtype)
        and left.equals(right)
    )
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_require_same_parcels`

**Exact signature**

```python
def _require_same_parcels(
    expected: gpd.GeoDataFrame,
    actual: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Private `road` helper for require same parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `list(actual.columns) != list(expected.columns)`.
- Guard with a raise path: `not actual.dtypes.equals(expected.dtypes)`.
- Guard with a raise path: `not _same_index(actual.index, expected.index)`.
- Guard with a raise path: `not _validated_crs(actual.crs, 4326, label).equals(_validated_crs(expected.crs, 4326, label))`.
- Guard with a raise path: `not actual.geometry.to_wkb().equals(expected.geometry.to_wkb())`.
- Guard with a raise path: `not actual.drop(columns='geometry').equals(expected.drop(columns='geometry'))`.
- Explicit raise expressions: `RoadProximityCoverageError(f'{label} parcel CRS changed')`, `RoadProximityCoverageError(f'{label} parcel columns changed')`, `RoadProximityCoverageError(f'{label} parcel dtypes changed')`, `RoadProximityCoverageError(f'{label} parcel facts changed')`, `RoadProximityCoverageError(f'{label} parcel geometry changed')`, `RoadProximityCoverageError(f'{label} parcel index changed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `actual.drop(columns='geometry').equals`, `actual.geometry.to_wkb`, `actual.geometry.to_wkb().equals`, `expected.geometry.to_wkb`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `_require_same_parcels`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_require_same_parcels`.

**Complete source-ordered implementation**

```python
def _require_same_parcels(
    expected: gpd.GeoDataFrame,
    actual: gpd.GeoDataFrame,
    label: str,
) -> None:
    if list(actual.columns) != list(expected.columns):
        raise RoadProximityCoverageError(f"{label} parcel columns changed")
    if not actual.dtypes.equals(expected.dtypes):
        raise RoadProximityCoverageError(f"{label} parcel dtypes changed")
    if not _same_index(actual.index, expected.index):
        raise RoadProximityCoverageError(f"{label} parcel index changed")
    if not _validated_crs(actual.crs, 4326, label).equals(
        _validated_crs(expected.crs, 4326, label)
    ):
        raise RoadProximityCoverageError(f"{label} parcel CRS changed")
    if not actual.geometry.to_wkb().equals(expected.geometry.to_wkb()):
        raise RoadProximityCoverageError(f"{label} parcel geometry changed")
    if not actual.drop(columns="geometry").equals(
        expected.drop(columns="geometry")
    ):
        raise RoadProximityCoverageError(f"{label} parcel facts changed")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_finite_nonnegative`

**Exact signature**

```python
def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
```

**Purpose**

Private `road` helper for finite nonnegative; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `np.ndarray`.
- Every observed return expression is reproduced without truncation:
```python
np.asarray(converted, dtype='float64')
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, Real) or isinstance(value, (bool, np.bool_))`.
- Guard with a raise path: `not isfinite(numeric) or numeric < 0`.
- Explicit raise expressions: `RoadProximityCoverageError(f'{label} must be finite and non-negative')`, `RoadProximityCoverageError(f'{label} must be numeric')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `converted`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_match_rows` via `_finite_nonnegative`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_finite_nonnegative`.

**Complete source-ordered implementation**

```python
def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
    converted: list[float] = []
    for value in values.tolist():
        if not isinstance(value, Real) or isinstance(value, (bool, np.bool_)):
            raise RoadProximityCoverageError(f"{label} must be numeric")
        numeric = float(value)
        if not isfinite(numeric) or numeric < 0:
            raise RoadProximityCoverageError(
                f"{label} must be finite and non-negative"
            )
        converted.append(numeric)
    return np.asarray(converted, dtype="float64")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_class_coverage`

**Exact signature**

```python
def _validate_class_coverage(
    coverage: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
```

**Purpose**

Rejects malformed or inconsistent class coverage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
eligible
```

**Validation and exceptions**

- Guard with a raise path: `type(coverage) is not tuple or len(coverage) != len(classes)`.
- Guard with a raise path: `type(item) is not RoadProxyClassCoverage`.
- Guard with a raise path: `item.road_proxy_class != classes[position]`.
- Guard with a raise path: `type(item.feature_count) is not int or item.feature_count < 0`.
- Guard with a raise path: `type(item.distance_eligible) is not bool or item.distance_eligible != (item.road_proxy_class in eligible)`.
- Explicit raise expressions: `RoadProximityCoverageError('Road class coverage distance eligibility is invalid')`, `RoadProximityCoverageError('Road class coverage feature_count is invalid')`, `RoadProximityCoverageError('Road class coverage is invalid')`, `RoadProximityCoverageError('Road class coverage order is invalid')`, `RoadProximityCoverageError('Road class coverage type is invalid')`.

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `_validate_class_coverage`.

**Complete source-ordered implementation**

```python
def _validate_class_coverage(
    coverage: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
    classes = policy.classes.values
    eligible = tuple(
        road_class
        for road_class in classes
        if road_class != policy.classes.not_distance_proxy
    )
    if type(coverage) is not tuple or len(coverage) != len(classes):
        raise RoadProximityCoverageError("Road class coverage is invalid")
    for position, item in enumerate(coverage):
        if type(item) is not RoadProxyClassCoverage:
            raise RoadProximityCoverageError("Road class coverage type is invalid")
        if item.road_proxy_class != classes[position]:
            raise RoadProximityCoverageError("Road class coverage order is invalid")
        if type(item.feature_count) is not int or item.feature_count < 0:
            raise RoadProximityCoverageError(
                "Road class coverage feature_count is invalid"
            )
        if type(item.distance_eligible) is not bool or (
            item.distance_eligible != (item.road_proxy_class in eligible)
        ):
            raise RoadProximityCoverageError(
                "Road class coverage distance eligibility is invalid"
            )
    return eligible
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_match_rows`

**Exact signature**

```python
def _validate_match_rows(
    table: pd.DataFrame,
    coverage: tuple[RoadProxyClassCoverage, ...],
) -> None:
```

**Purpose**

Rejects malformed or inconsistent match rows; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `item.feature_count == 0`.
- Guard with a raise path: `not matched.all()`.
- Guard with a raise path: `rows.loc[:, list(required)].isna().any().any()`.
- Guard with a raise path: `matched.any() or rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any()`.
- Guard with a raise path: `not isinstance(value, Integral) or isinstance(value, (bool, np.bool_)) or int(value) < 1`.
- Explicit raise expressions: `RoadProximityCoverageError('Empty road class contains selected road evidence')`, `RoadProximityCoverageError('Matched road evidence is incomplete')`, `RoadProximityCoverageError('Nearest road tie count must be an integer >= 1')`, `RoadProximityCoverageError('Non-empty road class is missing a parcel match')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `rows['nearest_road_proxy_distance_m'].notna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `_validate_match_rows`.

**Complete source-ordered implementation**

```python
def _validate_match_rows(
    table: pd.DataFrame,
    coverage: tuple[RoadProxyClassCoverage, ...],
) -> None:
    by_class = {item.road_proxy_class: item for item in coverage}
    for road_class, item in by_class.items():
        if not item.distance_eligible:
            continue
        rows = table.loc[table["road_proxy_class"].eq(road_class)]
        matched = rows["nearest_road_proxy_distance_m"].notna()
        if item.feature_count == 0:
            if matched.any() or rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any():
                raise RoadProximityCoverageError(
                    "Empty road class contains selected road evidence"
                )
            continue
        if not matched.all():
            raise RoadProximityCoverageError(
                "Non-empty road class is missing a parcel match"
            )
        _finite_nonnegative(
            rows["nearest_road_proxy_distance_m"], "Nearest road distance"
        )
        required = (
            "nearest_road_feature_id",
            "nearest_source_feature_id",
            "nearest_road_tie_count",
            "nearest_road_primary_rule",
            "nearest_road_rule_trace_json",
            "nearest_road_unknown_fields_json",
            "nearest_road_toll_evidence",
            "nearest_source_layer",
            "nearest_source_department_code",
            "nearest_source_edition",
            "nearest_source_archive_sha256",
        )
        if rows.loc[:, list(required)].isna().any().any():
            raise RoadProximityCoverageError(
                "Matched road evidence is incomplete"
            )
        for value in rows["nearest_road_tie_count"].tolist():
            if (
                not isinstance(value, Integral)
                or isinstance(value, (bool, np.bool_))
                or int(value) < 1
            ):
                raise RoadProximityCoverageError(
                    "Nearest road tie count must be an integer >= 1"
                )
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_upstream_result`

**Exact signature**

```python
def _validate_upstream_result(
    input_parcels: gpd.GeoDataFrame,
    result: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> ParcelRoadProximityResult:
```

**Purpose**

Rejects malformed or inconsistent upstream result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `ParcelRoadProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `type(result) is not ParcelRoadProximityResult`.
- Guard with a raise path: `type(table) is not pd.DataFrame`.
- Guard with a raise path: `table.columns.duplicated().any() or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS`.
- Guard with a raise path: `not isinstance(table.index, pd.RangeIndex) or (table.index.start != 0 or table.index.step != 1 or table.index.name is not None)`.
- Guard with a raise path: `len(table) != len(parcels) * len(eligible)`.
- Guard with a raise path: `table['parcel_id'].tolist() != expected_ids`.
- Guard with a raise path: `table['road_proxy_class'].tolist() != expected_classes`.
- Guard with a raise path: `table.duplicated(['parcel_id', 'road_proxy_class']).any()`.
- Guard with a raise path: `table[column].isna().any() or not table[column].eq(expected).all()`.
- Explicit raise expressions: `RoadProximityCoverageError('Class proximity class order is invalid')`, `RoadProximityCoverageError('Class proximity index is invalid')`, `RoadProximityCoverageError('Class proximity must be a plain DataFrame')`, `RoadProximityCoverageError('Class proximity pairs are duplicated')`, `RoadProximityCoverageError('Class proximity parcel order is invalid')`, `RoadProximityCoverageError('Class proximity row count is invalid')`, `RoadProximityCoverageError('Class proximity schema is invalid')`, `RoadProximityCoverageError('Road proximity result type is invalid')`, `RoadProximityCoverageError(f'Class proximity policy lineage is invalid: {column}')`.

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_upstream_result`.

**Complete source-ordered implementation**

```python
def _validate_upstream_result(
    input_parcels: gpd.GeoDataFrame,
    result: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> ParcelRoadProximityResult:
    if type(result) is not ParcelRoadProximityResult:
        raise RoadProximityCoverageError("Road proximity result type is invalid")
    parcels = _validate_parcel_frame(result.parcels, "Road proximity parcels")
    _require_same_parcels(input_parcels, parcels, "Road proximity")
    eligible = _validate_class_coverage(result.class_coverage, policy)
    table = result.class_proximity
    if type(table) is not pd.DataFrame:
        raise RoadProximityCoverageError("Class proximity must be a plain DataFrame")
    if table.columns.duplicated().any() or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS:
        raise RoadProximityCoverageError("Class proximity schema is invalid")
    if not isinstance(table.index, pd.RangeIndex) or (
        table.index.start != 0
        or table.index.step != 1
        or table.index.name is not None
    ):
        raise RoadProximityCoverageError("Class proximity index is invalid")
    if len(table) != len(parcels) * len(eligible):
        raise RoadProximityCoverageError("Class proximity row count is invalid")
    expected_ids = [
        parcel_id
        for parcel_id in parcels["parcel_id"].tolist()
        for _ in eligible
    ]
    expected_classes = list(eligible) * len(parcels)
    if table["parcel_id"].tolist() != expected_ids:
        raise RoadProximityCoverageError("Class proximity parcel order is invalid")
    if table["road_proxy_class"].tolist() != expected_classes:
        raise RoadProximityCoverageError("Class proximity class order is invalid")
    if table.duplicated(["parcel_id", "road_proxy_class"]).any():
        raise RoadProximityCoverageError("Class proximity pairs are duplicated")
    expected_lineage = {
        "road_proxy_policy_id": policy.policy_id,
        "road_proxy_policy_schema_version": policy.schema_version,
        "road_proxy_policy_config_sha256": policy.config_sha256,
        "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
        "proximity_scope": _PROXIMITY_SCOPE,
    }
    for column, expected in expected_lineage.items():
        if table[column].isna().any() or not table[column].eq(expected).all():
            raise RoadProximityCoverageError(
                f"Class proximity policy lineage is invalid: {column}"
            )
    _validate_match_rows(table, result.class_coverage)
    return result
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_coverage_summary`

**Exact signature**

```python
def _validate_coverage_summary(
    coverage: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
    config: IgnBdTopoSourceConfig,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent coverage summary; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(summary) is not IgnBdTopoCoverageLayerSummary`.
- Guard with a raise path: `summary.source_layer_name != coverage.source_layer`.
- Guard with a raise path: `type(summary.selected_feature_count) is not int or summary.selected_feature_count != len(frame)`.
- Guard with a raise path: `type(summary.source_feature_count) is not int or summary.source_feature_count < summary.selected_feature_count`.
- Guard with a raise path: `type(summary.columns) is not tuple or not summary.columns or len(set(summary.columns)) != len(summary.columns) or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns))`.
- Guard with a raise path: `tuple(frame.columns) != (*summary.columns, *_COVERAGE_FRAME_LINEAGE)`.
- Guard with a raise path: `type(summary.dtypes) is not tuple or summary.dtypes != expected_dtypes`.
- Guard with a raise path: `summary.department_code_field != expected_field`.
- Guard with a raise path: `summary.selected_department_code != coverage.source_department_code`.
- Guard with a raise path: `not frame[expected_field].eq(coverage.source_department_code).all()`.
- Guard with a raise path: `summary.spatial_role != _COVERAGE_SPATIAL_ROLE`.
- Explicit raise expressions: `RoadProximityCoverageError('Coverage configured department field is invalid')`, `RoadProximityCoverageError('Coverage department identity is invalid')`, `RoadProximityCoverageError('Coverage frame schema is invalid')`, `RoadProximityCoverageError('Coverage selected department is invalid')`, `RoadProximityCoverageError('Coverage selected feature count is invalid')`, `RoadProximityCoverageError('Coverage source feature count is invalid')`, `RoadProximityCoverageError('Coverage summary columns are invalid')`, `RoadProximityCoverageError('Coverage summary dtypes are invalid')`, `RoadProximityCoverageError('Coverage summary layer is invalid')`, `RoadProximityCoverageError('Coverage summary spatial role is invalid')`, `RoadProximityCoverageError('Coverage summary type is invalid')`.

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_validate_coverage_summary`.

**Complete source-ordered implementation**

```python
def _validate_coverage_summary(
    coverage: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
    config: IgnBdTopoSourceConfig,
) -> None:
    summary = coverage.summary
    if type(summary) is not IgnBdTopoCoverageLayerSummary:
        raise RoadProximityCoverageError("Coverage summary type is invalid")
    if summary.source_layer_name != coverage.source_layer:
        raise RoadProximityCoverageError("Coverage summary layer is invalid")
    _validated_crs(summary.crs, 2154, "Coverage summary")
    if type(summary.selected_feature_count) is not int or (
        summary.selected_feature_count != len(frame)
    ):
        raise RoadProximityCoverageError("Coverage selected feature count is invalid")
    if (
        type(summary.source_feature_count) is not int
        or summary.source_feature_count < summary.selected_feature_count
    ):
        raise RoadProximityCoverageError("Coverage source feature count is invalid")
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or len(set(summary.columns)) != len(summary.columns)
        or any(
            not isinstance(column, str)
            or not column
            or column != column.strip()
            for column in summary.columns
        )
    ):
        raise RoadProximityCoverageError("Coverage summary columns are invalid")
    if tuple(frame.columns) != (*summary.columns, *_COVERAGE_FRAME_LINEAGE):
        raise RoadProximityCoverageError("Coverage frame schema is invalid")
    expected_dtypes = tuple(
        (column, str(frame[column].dtype)) for column in summary.columns
    )
    if type(summary.dtypes) is not tuple or summary.dtypes != expected_dtypes:
        raise RoadProximityCoverageError("Coverage summary dtypes are invalid")
    expected_field = config.coverage.department_layer.department_code_field
    if summary.department_code_field != expected_field:
        raise RoadProximityCoverageError(
            "Coverage configured department field is invalid"
        )
    if summary.selected_department_code != coverage.source_department_code:
        raise RoadProximityCoverageError("Coverage selected department is invalid")
    if not frame[expected_field].eq(coverage.source_department_code).all():
        raise RoadProximityCoverageError("Coverage department identity is invalid")
    if summary.spatial_role != _COVERAGE_SPATIAL_ROLE:
        raise RoadProximityCoverageError("Coverage summary spatial role is invalid")
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_source_coverage`

**Exact signature**

```python
def _validate_source_coverage(
    source: object,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]:
```

**Purpose**

Rejects malformed or inconsistent source coverage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(source, frame)
```

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoDepartmentCoverage`.
- Guard with a raise path: `source.extraction is not road_source.extraction`.
- Guard with a raise path: `road_source.extraction.spatial_role != _SOURCE_SPATIAL_ROLE or archive.spatial_role != _SOURCE_SPATIAL_ROLE`.
- Guard with a raise path: `provider_identity not in _IGN_PROVIDER_IDENTITIES`.
- Guard with a raise path: `product_identity != 'bdtopo'`.
- Guard with a raise path: `provider_identity != _normalized_identity(config.provider, 'Config provider')`.
- Guard with a raise path: `product_identity != _normalized_identity(config.product, 'Config product')`.
- Guard with a raise path: `archive.department_code != config.department_code`.
- Guard with a raise path: `_SHA256_PATTERN.fullmatch(archive.sha256) is None`.
- Guard with a raise path: `source.source_layer != expected_layer`.
- Guard with a raise path: `_normalized_identity(source.source_provider, 'Coverage provider') not in _IGN_PROVIDER_IDENTITIES`.
- Guard with a raise path: `_normalized_identity(source.source_product, 'Coverage product') != 'bdtopo'`.
- Guard with a raise path: `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None`.
- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `'geometry' not in frame.columns or frame.active_geometry_name != 'geometry'`.
- Guard with a raise path: `len(frame) != 1`.
- Guard with a raise path: `geometry.isna().any()`.
- Guard with a raise path: `geometry.is_empty.any()`.
- Guard with a raise path: `not geometry.is_valid.all()`.
- Guard with a raise path: `not set(geometry.geom_type.dropna()) <= _COVERAGE_GEOMETRY_TYPES`.
- Guard with a raise path: `not _null_safe_scalar_equal(getattr(source, name), expected)`.
- Guard with a raise path: `not _null_safe_scalar_equal(actual, expected)`.
- Explicit raise expressions: `RoadProximityCoverageError('Coverage archive SHA256 is invalid')`, `RoadProximityCoverageError('Coverage columns must be unique')`, `RoadProximityCoverageError('Coverage does not use the configured physical layer')`, `RoadProximityCoverageError('Coverage geometry must be Polygon or MultiPolygon')`, `RoadProximityCoverageError('Coverage geometry must be valid')`, `RoadProximityCoverageError('Coverage geometry must exist and be active')`, `RoadProximityCoverageError('Coverage geometry must not be empty')`, `RoadProximityCoverageError('Coverage geometry must not be null')`, `RoadProximityCoverageError('Coverage must be a GeoDataFrame')`, `RoadProximityCoverageError('Coverage must contain exactly one selected feature')`, `RoadProximityCoverageError('Coverage must retain the exact road extraction identity')`, `RoadProximityCoverageError('Coverage product is not BD TOPO')`, `RoadProximityCoverageError('Coverage provider is not IGN')`, `RoadProximityCoverageError('Coverage source type is invalid')`, `RoadProximityCoverageError('Road package archive SHA256 is invalid')`, `RoadProximityCoverageError('Road package department differs from config')`, `RoadProximityCoverageError('Road package product differs from config')`, `RoadProximityCoverageError('Road package product is not BD TOPO')`, `RoadProximityCoverageError('Road package provider differs from config')`, `RoadProximityCoverageError('Road package provider is not IGN')`, `RoadProximityCoverageError('Road package spatial role is invalid')`, `RoadProximityCoverageError(f'Coverage package lineage is invalid: {name}')`, `RoadProximityCoverageError(f'Coverage row lineage is invalid: {column}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `geometry.geom_type.dropna`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_validate_source_coverage`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_source_coverage`.

**Complete source-ordered implementation**

```python
def _validate_source_coverage(
    source: object,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]:
    if type(source) is not IgnBdTopoDepartmentCoverage:
        raise RoadProximityCoverageError("Coverage source type is invalid")
    if source.extraction is not road_source.extraction:
        raise RoadProximityCoverageError(
            "Coverage must retain the exact road extraction identity"
        )
    archive = road_source.extraction.archive
    if road_source.extraction.spatial_role != _SOURCE_SPATIAL_ROLE or (
        archive.spatial_role != _SOURCE_SPATIAL_ROLE
    ):
        raise RoadProximityCoverageError("Road package spatial role is invalid")
    _validated_crs(archive.projection, 2154, "Road package")
    provider_identity = _normalized_identity(archive.provider, "Road provider")
    product_identity = _normalized_identity(archive.product, "Road product")
    if provider_identity not in _IGN_PROVIDER_IDENTITIES:
        raise RoadProximityCoverageError("Road package provider is not IGN")
    if product_identity != "bdtopo":
        raise RoadProximityCoverageError("Road package product is not BD TOPO")
    if provider_identity != _normalized_identity(config.provider, "Config provider"):
        raise RoadProximityCoverageError("Road package provider differs from config")
    if product_identity != _normalized_identity(config.product, "Config product"):
        raise RoadProximityCoverageError("Road package product differs from config")
    if archive.department_code != config.department_code:
        raise RoadProximityCoverageError("Road package department differs from config")
    if _SHA256_PATTERN.fullmatch(archive.sha256) is None:
        raise RoadProximityCoverageError("Road package archive SHA256 is invalid")
    expected_layer = _discover_department_coverage_layer(
        road_source.extraction.all_layer_names, config
    )
    if source.source_layer != expected_layer:
        raise RoadProximityCoverageError(
            "Coverage does not use the configured physical layer"
        )
    expected_scalars = {
        "source_provider": archive.provider,
        "source_product": archive.product,
        "source_department_code": archive.department_code,
        "source_edition": archive.edition,
        "source_product_version": archive.product_version,
        "source_archive_sha256": archive.sha256,
        "source_layer": expected_layer,
        "spatial_role": _COVERAGE_SPATIAL_ROLE,
    }
    for name, expected in expected_scalars.items():
        if not _null_safe_scalar_equal(getattr(source, name), expected):
            raise RoadProximityCoverageError(
                f"Coverage package lineage is invalid: {name}"
            )
    if _normalized_identity(source.source_provider, "Coverage provider") not in (
        _IGN_PROVIDER_IDENTITIES
    ):
        raise RoadProximityCoverageError("Coverage provider is not IGN")
    if _normalized_identity(source.source_product, "Coverage product") != "bdtopo":
        raise RoadProximityCoverageError("Coverage product is not BD TOPO")
    if _SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None:
        raise RoadProximityCoverageError("Coverage archive SHA256 is invalid")

    frame = source.coverage
    if not isinstance(frame, gpd.GeoDataFrame):
        raise RoadProximityCoverageError("Coverage must be a GeoDataFrame")
    if frame.columns.duplicated().any():
        raise RoadProximityCoverageError("Coverage columns must be unique")
    if "geometry" not in frame.columns or frame.active_geometry_name != "geometry":
        raise RoadProximityCoverageError("Coverage geometry must exist and be active")
    _validated_crs(frame.crs, 2154, "Coverage")
    if len(frame) != 1:
        raise RoadProximityCoverageError(
            "Coverage must contain exactly one selected feature"
        )
    geometry = frame.geometry
    if geometry.isna().any():
        raise RoadProximityCoverageError("Coverage geometry must not be null")
    if geometry.is_empty.any():
        raise RoadProximityCoverageError("Coverage geometry must not be empty")
    if not geometry.is_valid.all():
        raise RoadProximityCoverageError("Coverage geometry must be valid")
    if not set(geometry.geom_type.dropna()) <= _COVERAGE_GEOMETRY_TYPES:
        raise RoadProximityCoverageError(
            "Coverage geometry must be Polygon or MultiPolygon"
        )
    _validate_coverage_summary(source, frame, config)
    for column, expected in expected_scalars.items():
        actual = frame.iloc[0][column]
        if not _null_safe_scalar_equal(actual, expected):
            raise RoadProximityCoverageError(
                f"Coverage row lineage is invalid: {column}"
            )
    return source, frame
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_coverage_lineage`

**Exact signature**

```python
def _coverage_lineage(
    coverage: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
```

**Purpose**

Private `road` helper for coverage lineage; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'road_source_coverage_provider': coverage.source_provider, 'road_source_coverage_product': coverage.source_product, 'road_source_coverage_department_code': coverage.source_department_code, 'road_source_coverage_edition': coverage.source_edition, 'road_source_coverage_product_version': coverage.source_product_version, 'road_source_coverage_archive_sha256': coverage.source_archive_sha256, 'road_source_coverage_layer': coverage.source_layer, 'road_source_coverage_spatial_role': coverage.spatial_role}
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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_expected_diagnostics` via `_coverage_lineage`.

**Complete source-ordered implementation**

```python
def _coverage_lineage(
    coverage: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
    return {
        "road_source_coverage_provider": coverage.source_provider,
        "road_source_coverage_product": coverage.source_product,
        "road_source_coverage_department_code": coverage.source_department_code,
        "road_source_coverage_edition": coverage.source_edition,
        "road_source_coverage_product_version": coverage.source_product_version,
        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,
        "road_source_coverage_layer": coverage.source_layer,
        "road_source_coverage_spatial_role": coverage.spatial_role,
    }
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_parcel_coverage_diagnostics`

**Exact signature**

```python
def _parcel_coverage_diagnostics(
    parcels: gpd.GeoDataFrame,
    coverage_frame: gpd.GeoDataFrame,
) -> tuple[np.ndarray, np.ndarray]:
```

**Purpose**

Private `road` helper for parcel coverage diagnostics; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[np.ndarray, np.ndarray]`.
- Every observed return expression is reproduced without truncation:
```python
(boundary_distances, positions)
```

**Validation and exceptions**

- Guard with a raise path: `not np.isfinite(measured).all() or (measured < 0).any()`.
- Explicit raise expressions: `RoadProximityCoverageError('Calculated boundary distances must be finite and non-negative')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `boundary`, `distance`, `force_2d`, `parcels.to_crs`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_parcel_coverage_diagnostics`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_parcel_coverage_diagnostics`.

**Complete source-ordered implementation**

```python
def _parcel_coverage_diagnostics(
    parcels: gpd.GeoDataFrame,
    coverage_frame: gpd.GeoDataFrame,
) -> tuple[np.ndarray, np.ndarray]:
    calculation = parcels.to_crs(_CALCULATION_CRS)
    parcel_geometries = np.asarray(
        force_2d(np.asarray(calculation.geometry.array, dtype=object)),
        dtype=object,
    )
    coverage_geometry = force_2d(coverage_frame.geometry.iloc[0])
    coverage_boundary = boundary(coverage_geometry)
    covered = np.asarray(covers(coverage_geometry, parcel_geometries), dtype="bool")
    boundary_contact = np.asarray(
        intersects(parcel_geometries, coverage_boundary), dtype="bool"
    )
    fully_covered = covered & ~boundary_contact
    measured = np.asarray(
        distance(parcel_geometries, coverage_boundary), dtype="float64"
    )
    if not np.isfinite(measured).all() or (measured < 0).any():
        raise RoadProximityCoverageError(
            "Calculated boundary distances must be finite and non-negative"
        )
    boundary_distances = np.where(fully_covered, measured, 0.0)
    positions = np.where(
        fully_covered,
        "FULLY_COVERED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    )
    return boundary_distances, positions
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_coverage_statuses`

**Exact signature**

```python
def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
) -> np.ndarray:
```

**Purpose**

Private `road` helper for coverage statuses; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `np.ndarray`.
- Every observed return expression is reproduced without truncation:
```python
statuses
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `distances.to_numpy`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `statuses[internal & (numeric < boundary_distances)]`, `statuses[internal & (numeric >= boundary_distances)]`, `statuses[outside]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_expected_diagnostics` via `_coverage_statuses`.

**Complete source-ordered implementation**

```python
def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
) -> np.ndarray:
    numeric = distances.to_numpy(dtype="float64", na_value=np.nan)
    matched = ~np.isnan(numeric)
    fully_covered = positions == "FULLY_COVERED"
    statuses = np.full(len(distances), "NO_MATCH", dtype=object)
    outside = matched & ~fully_covered
    statuses[outside] = "OUTSIDE_OR_CROSSING_COVERAGE"
    internal = matched & fully_covered
    statuses[internal & (numeric < boundary_distances)] = "NOT_BOUNDARY_LIMITED"
    statuses[internal & (numeric >= boundary_distances)] = "BOUNDARY_LIMITED"
    return statuses
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_expected_diagnostics`

**Exact signature**

```python
def _expected_diagnostics(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
```

**Purpose**

Private `road` helper for expected diagnostics; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output.loc[:, list(_DIAGNOSTIC_COLUMNS)]
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `row_boundary.to_numpy`, `table['parcel_id'].map(boundary_by_id).astype`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output['road_proximity_coverage_status']`, `output['road_source_boundary_distance_m']`, `output['road_source_coverage_position']`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_diagnosed_class_proximity` via `_expected_diagnostics`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_expected_diagnostics`.

**Complete source-ordered implementation**

```python
def _expected_diagnostics(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
    boundary_by_id = dict(
        zip(parcels["parcel_id"], boundary_distances, strict=True)
    )
    position_by_id = dict(zip(parcels["parcel_id"], positions, strict=True))
    row_boundary = table["parcel_id"].map(boundary_by_id).astype("float64")
    row_positions = table["parcel_id"].map(position_by_id)
    output = pd.DataFrame(index=table.index.copy())
    output["road_source_boundary_distance_m"] = row_boundary
    output["road_source_coverage_position"] = row_positions
    output["road_proximity_coverage_status"] = _coverage_statuses(
        table["nearest_road_proxy_distance_m"],
        row_boundary.to_numpy(dtype="float64"),
        row_positions.to_numpy(dtype=object),
    )
    for column, value in _coverage_lineage(coverage).items():
        output[column] = value
    return output.loc[:, list(_DIAGNOSTIC_COLUMNS)]
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_diagnosed_class_proximity`

**Exact signature**

```python
def _diagnosed_class_proximity(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
```

**Purpose**

Private `road` helper for diagnosed class proximity; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_diagnosed_class_proximity`.

**Complete source-ordered implementation**

```python
def _diagnosed_class_proximity(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
    output = table.copy(deep=True)
    diagnostics = _expected_diagnostics(
        table, parcels, boundary_distances, positions, coverage
    )
    for column in _DIAGNOSTIC_COLUMNS:
        output[column] = diagnostics[column]
    return output
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_selected_road_package`

**Exact signature**

```python
def _validate_selected_road_package(
    table: pd.DataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent selected road package; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `selected.isna().any() or not selected.eq(value).all()`.
- Explicit raise expressions: `RoadProximityCoverageError(f'Selected road package lineage differs from coverage: {column}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `table['nearest_road_proxy_distance_m'].notna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_validate_selected_road_package`.
- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_selected_road_package`.

**Complete source-ordered implementation**

```python
def _validate_selected_road_package(
    table: pd.DataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> None:
    matched = table["nearest_road_proxy_distance_m"].notna()
    expected = {
        "nearest_source_department_code": coverage.source_department_code,
        "nearest_source_edition": coverage.source_edition,
        "nearest_source_archive_sha256": coverage.source_archive_sha256,
    }
    for column, value in expected.items():
        selected = table.loc[matched, column]
        if selected.isna().any() or not selected.eq(value).all():
            raise RoadProximityCoverageError(
                f"Selected road package lineage differs from coverage: {column}"
            )
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_validate_assessment_result`

**Exact signature**

```python
def _validate_assessment_result(
    input_parcels: gpd.GeoDataFrame,
    proximity: ParcelRoadProximityResult,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
    loaded_coverage: IgnBdTopoDepartmentCoverage,
    result: object,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent assessment result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(result) is not RoadProximityCoverageAssessmentResult`.
- Guard with a raise path: `result.source_coverage is not loaded_coverage`.
- Guard with a raise path: `result.class_coverage is not proximity.class_coverage`.
- Guard with a raise path: `type(output) is not pd.DataFrame`.
- Guard with a raise path: `output.columns.duplicated().any() or tuple(output.columns) != expected_columns`.
- Guard with a raise path: `not _same_index(output.index, source.index)`.
- Guard with a raise path: `not prefix.dtypes.equals(source.dtypes) or not prefix.equals(source)`.
- Guard with a raise path: `not actual.dtypes.equals(expected.dtypes) or not actual.equals(expected)`.
- Guard with a raise path: `position_values.isna().any() or not set(position_values.unique()) <= _POSITIONS`.
- Guard with a raise path: `(numeric[outside] != 0.0).any()`.
- Guard with a raise path: `statuses.isna().any() or not set(statuses.unique()) <= _STATUSES`.
- Explicit raise expressions: `RoadProximityCoverageError('Coverage assessment changed original class proximity facts')`, `RoadProximityCoverageError('Coverage assessment result type is invalid')`, `RoadProximityCoverageError('Coverage assessment source was not preserved')`, `RoadProximityCoverageError('Coverage class proximity index changed')`, `RoadProximityCoverageError('Coverage class proximity is invalid')`, `RoadProximityCoverageError('Coverage class proximity schema is invalid')`, `RoadProximityCoverageError('Coverage diagnostics differ from geometric reconstruction')`, `RoadProximityCoverageError('Coverage position is invalid')`, `RoadProximityCoverageError('Coverage status is invalid')`, `RoadProximityCoverageError('Outside or crossing rows require zero boundary distance')`, `RoadProximityCoverageError('Road class coverage was not preserved')`.

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

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_assessment_result`.

**Complete source-ordered implementation**

```python
def _validate_assessment_result(
    input_parcels: gpd.GeoDataFrame,
    proximity: ParcelRoadProximityResult,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
    loaded_coverage: IgnBdTopoDepartmentCoverage,
    result: object,
) -> None:
    if type(result) is not RoadProximityCoverageAssessmentResult:
        raise RoadProximityCoverageError("Coverage assessment result type is invalid")
    if result.source_coverage is not loaded_coverage:
        raise RoadProximityCoverageError("Coverage assessment source was not preserved")
    coverage, coverage_frame = _validate_source_coverage(
        result.source_coverage, road_source, config
    )
    _validate_parcel_frame(result.parcels, "Coverage result parcels")
    _require_same_parcels(input_parcels, result.parcels, "Coverage result")
    _require_same_parcels(proximity.parcels, result.parcels, "Coverage result")
    if result.class_coverage is not proximity.class_coverage:
        raise RoadProximityCoverageError("Road class coverage was not preserved")
    output = result.class_proximity
    source = proximity.class_proximity
    if type(output) is not pd.DataFrame:
        raise RoadProximityCoverageError("Coverage class proximity is invalid")
    expected_columns = (*CLASS_PROXIMITY_COLUMNS, *_DIAGNOSTIC_COLUMNS)
    if output.columns.duplicated().any() or tuple(output.columns) != expected_columns:
        raise RoadProximityCoverageError(
            "Coverage class proximity schema is invalid"
        )
    if not _same_index(output.index, source.index):
        raise RoadProximityCoverageError("Coverage class proximity index changed")
    prefix = output.loc[:, list(CLASS_PROXIMITY_COLUMNS)]
    if not prefix.dtypes.equals(source.dtypes) or not prefix.equals(source):
        raise RoadProximityCoverageError(
            "Coverage assessment changed original class proximity facts"
        )
    boundary_distances, positions = _parcel_coverage_diagnostics(
        proximity.parcels, coverage_frame
    )
    expected = _expected_diagnostics(
        source, proximity.parcels, boundary_distances, positions, coverage
    )
    actual = output.loc[:, list(_DIAGNOSTIC_COLUMNS)]
    if not actual.dtypes.equals(expected.dtypes) or not actual.equals(expected):
        raise RoadProximityCoverageError(
            "Coverage diagnostics differ from geometric reconstruction"
        )
    numeric = _finite_nonnegative(
        output["road_source_boundary_distance_m"],
        "Road source boundary distance",
    )
    position_values = output["road_source_coverage_position"]
    if position_values.isna().any() or not set(position_values.unique()) <= _POSITIONS:
        raise RoadProximityCoverageError("Coverage position is invalid")
    outside = position_values.eq("OUTSIDE_OR_CROSSING_COVERAGE").to_numpy(
        dtype="bool"
    )
    if (numeric[outside] != 0.0).any():
        raise RoadProximityCoverageError(
            "Outside or crossing rows require zero boundary distance"
        )
    statuses = output["road_proximity_coverage_status"]
    if statuses.isna().any() or not set(statuses.unique()) <= _STATUSES:
        raise RoadProximityCoverageError("Coverage status is invalid")
    _validate_selected_road_package(output, coverage)
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `_assess_road_proximity_coverage`

**Exact signature**

```python
def _assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> RoadProximityCoverageAssessmentResult:
```

**Purpose**

Derives diagnostic evidence for road proximity coverage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RoadProximityCoverageAssessmentResult`.
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
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/assess_road_proximity_coverage.py::assess_road_proximity_coverage` via `_assess_road_proximity_coverage`.

**Complete source-ordered implementation**

```python
def _assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> RoadProximityCoverageAssessmentResult:
    input_parcels = _validate_parcel_frame(parcels, "Input parcels")
    proximity = enrich_parcel_road_proximity(
        parcels, road_source, source_config, policy_path
    )
    policy = (
        load_ign_road_vehicle_proxy_policy()
        if policy_path is None
        else load_ign_road_vehicle_proxy_policy(policy_path)
    )
    validated_proximity = _validate_upstream_result(
        input_parcels, proximity, policy
    )
    coverage = load_ign_bdtopo_department_coverage(
        road_source.extraction, source_config
    )
    validated_coverage, coverage_frame = _validate_source_coverage(
        coverage, road_source, source_config
    )
    _validate_selected_road_package(
        validated_proximity.class_proximity, validated_coverage
    )
    boundary_distances, positions = _parcel_coverage_diagnostics(
        validated_proximity.parcels, coverage_frame
    )
    output_table = _diagnosed_class_proximity(
        validated_proximity.class_proximity,
        validated_proximity.parcels,
        boundary_distances,
        positions,
        validated_coverage,
    )
    result = RoadProximityCoverageAssessmentResult(
        parcels=validated_proximity.parcels.copy(deep=True),
        class_proximity=output_table,
        class_coverage=validated_proximity.class_coverage,
        source_coverage=validated_coverage,
    )
    _validate_assessment_result(
        input_parcels,
        validated_proximity,
        road_source,
        source_config,
        validated_coverage,
        result,
    )
    return result
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.

### `assess_road_proximity_coverage`

**Exact signature**

```python
def assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
```

**Purpose**

Diagnose source-bound road proximity using the verified package boundary.

**Return contract**

- Declared return annotation: `RoadProximityCoverageAssessmentResult`.
- Every observed return expression is reproduced without truncation:
```python
_assess_road_proximity_coverage(parcels, road_source, source_config, policy_path)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `type(road_source) is not IgnBdTopoRoadData`.
- Guard with a raise path: `type(source_config) is not IgnBdTopoSourceConfig`.
- Guard with a raise path: `policy_path is not None and (not isinstance(policy_path, Path))`.
- Explicit raise expressions: `RoadProximityCoverageError('Road proximity coverage cannot be assessed safely')`, `RoadProximityCoverageError('parcels must be a GeoDataFrame')`, `RoadProximityCoverageError('policy_path must be a pathlib.Path or None')`, `RoadProximityCoverageError('road_source must be an IgnBdTopoRoadData')`, `RoadProximityCoverageError('source_config must be an IgnBdTopoSourceConfig')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`.
- import: `tests/unit/test_assess_road_proximity_coverage.py::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `assess_road_proximity_coverage`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast` via `assess_road_proximity_coverage`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `assess_road_proximity_coverage`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading` via `assess_road_proximity_coverage`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `assess_road_proximity_coverage`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `assess_road_proximity_coverage`.
- direct call: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `assess_road_proximity_coverage`.

**Complete source-ordered implementation**

```python
def assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
    """Diagnose source-bound road proximity using the verified package boundary."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise RoadProximityCoverageError("parcels must be a GeoDataFrame")
        if type(road_source) is not IgnBdTopoRoadData:
            raise RoadProximityCoverageError(
                "road_source must be an IgnBdTopoRoadData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise RoadProximityCoverageError(
                "source_config must be an IgnBdTopoSourceConfig"
            )
        if policy_path is not None and not isinstance(policy_path, Path):
            raise RoadProximityCoverageError(
                "policy_path must be a pathlib.Path or None"
            )
        return _assess_road_proximity_coverage(
            parcels, road_source, source_config, policy_path
        )
    except RoadProximityCoverageError:
        raise
    except Exception as error:
        raise RoadProximityCoverageError(
            "Road proximity coverage cannot be assessed safely"
        ) from error
```

**Business boundary**

- Road geometry and general-car evidence do not prove legal parcel access or heavy/construction-vehicle access.


## 7. Data contracts

### Frame-preservation and semantic notes

- Coverage position/status fields are diagnostics repeated per parcel/class row. They qualify whether a distance is bounded by the verified source package, not whether a parcel has legal road access.

### `_COVERAGE_LINEAGE_COLUMNS` — canonical or derived frame-column schema

```python
_COVERAGE_LINEAGE_COLUMNS = (
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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `road_source_coverage_provider` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `road_source_coverage_product` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `road_source_coverage_department_code` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `road_source_coverage_edition` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `road_source_coverage_product_version` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `road_source_coverage_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 7 | `road_source_coverage_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `road_source_coverage_spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `_DIAGNOSTIC_COLUMNS` — canonical or derived frame-column schema

```python
_DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    *_COVERAGE_LINEAGE_COLUMNS,
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `road_source_boundary_distance_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 2 | `road_source_coverage_position` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `road_proximity_coverage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `road_source_coverage_provider` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `road_source_coverage_product` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `road_source_coverage_department_code` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `road_source_coverage_edition` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `road_source_coverage_product_version` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `road_source_coverage_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 10 | `road_source_coverage_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `road_source_coverage_spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `_SELECTED_ROAD_COLUMNS` — canonical or derived frame-column schema

```python
_SELECTED_ROAD_COLUMNS = (
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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `nearest_road_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `nearest_source_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `nearest_road_tie_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 4 | `nearest_road_primary_rule` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `nearest_road_rule_trace_json` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 6 | `nearest_road_unknown_fields_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `nearest_road_toll_evidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `nearest_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `nearest_importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `nearest_asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `nearest_private_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `nearest_light_vehicle_access_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `nearest_carriageway_width_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `nearest_closure_period_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `nearest_restriction_nature_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `nearest_source_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `nearest_source_department_code` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `nearest_source_edition` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 19 | `nearest_source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `RoadProximityCoverageAssessmentResult` | public symbol defined in this module | `defined in `src/landscout/stages/assess_road_proximity_coverage.py`` | yes |
| `RoadProximityCoverageError` | public symbol defined in this module | `defined in `src/landscout/stages/assess_road_proximity_coverage.py`` | yes |
| `assess_road_proximity_coverage` | public symbol defined in this module | `defined in `src/landscout/stages/assess_road_proximity_coverage.py`` | yes |

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
