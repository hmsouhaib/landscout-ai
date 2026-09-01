# `src/landscout/stages/assess_road_proximity_coverage.py`

## File identity

- Repository path: `src/landscout/stages/assess_road_proximity_coverage.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Diagnoses road proxy proximity against the verified IGN department coverage boundary.
- Source SHA256: `d9e4b36d0f211906e74489a22dbf51455ac8ac8b86be9416a255740a783217c6`

## 1. STEP 7F.1A.4 contract delta

- Ruff formatting only in STEP 7F.1A.4; executable contract, values, schemas, and test intent are unchanged. The companion is refreshed because its raw bytes and SHA changed.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Diagnoses road proxy proximity against the verified IGN department coverage boundary.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "RoadProximityCoverageAssessmentResult",
    "RoadProximityCoverageError",
    "assess_road_proximity_coverage",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `RoadProximityCoverageAssessmentResult`
  - `RoadProximityCoverageError`
  - `assess_road_proximity_coverage`

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

### `_COVERAGE_SPATIAL_ROLE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SOURCE_SPATIAL_ROLE`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SOURCE_SPATIAL_ROLE = "PROXY_GEOMETRY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_POSITIONS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_POSITIONS = frozenset({"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

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

### `_COVERAGE_GEOMETRY_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_COVERAGE_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SHA256_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_IGN_PROVIDER_IDENTITIES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institutnationaldelinformationgeographiqueetforestiereign",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_COVERAGE_LINEAGE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `road_source_coverage_provider`
  - `road_source_coverage_product`
  - `road_source_coverage_department_code`
  - `road_source_coverage_edition`
  - `road_source_coverage_product_version`
  - `road_source_coverage_archive_sha256`
  - `road_source_coverage_layer`
  - `road_source_coverage_spatial_role`

### `_DIAGNOSTIC_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    *_COVERAGE_LINEAGE_COLUMNS,
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_COVERAGE_FRAME_LINEAGE`

- Category: module constant or closed domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `source_provider`
  - `source_product`
  - `source_department_code`
  - `source_edition`
  - `source_product_version`
  - `source_archive_sha256`
  - `source_layer`
  - `spatial_role`

### `_SELECTED_ROAD_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
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

### `RoadProximityCoverageError`

**Source purpose:** Raised when road source-boundary diagnostics cannot be proven safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validated_crs` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validated_crs` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_normalized_identity` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_normalized_identity` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_exact_string` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_exact_string` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_exact_ids` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_exact_ids` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_parcel_frame` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_parcel_frame` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_require_same_parcels` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_require_same_parcels` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_finite_nonnegative` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_finite_nonnegative` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_class_coverage` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_class_coverage` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_match_rows` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_match_rows` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_parcel_coverage_diagnostics` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_parcel_coverage_diagnostics` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_selected_road_package` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_selected_road_package` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `RoadProximityCoverageError`
- constructor call: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `RoadProximityCoverageError`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `RoadProximityCoverageError`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_wrong_public_input_type_is_controlled_and_fast` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_proximity_failure_stops_coverage_loading` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_package_lineage_must_match_road_archive` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_selected_department_identity_is_exact` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_must_retain_same_extraction_object` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_invalid_coverage_geometry_is_rejected` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_matched_road_lineage_must_match_coverage` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_corrupt_generated` via `RoadProximityCoverageError`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_inconsistent_generated_status_is_rejected` via `RoadProximityCoverageError`

**Exact class source**

```python
class RoadProximityCoverageError(ValueError):
    """Raised when road source-boundary diagnostics cannot be proven safely."""
```

### `RoadProximityCoverageAssessmentResult`

**Source purpose:** Unchanged road proximity plus its source-package boundary diagnosis.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |
| `class_proximity` | `pd.DataFrame` | `required` | `class_proximity: pd.DataFrame` |
| `class_coverage` | `tuple[RoadProxyClassCoverage, ...]` | `required` | `class_coverage: tuple[RoadProxyClassCoverage, ...]` |
| `source_coverage` | `IgnBdTopoDepartmentCoverage` | `required` | `source_coverage: IgnBdTopoDepartmentCoverage` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `RoadProximityCoverageAssessmentResult`
- constructor call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `RoadProximityCoverageAssessmentResult`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `RoadProximityCoverageAssessmentResult`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `RoadProximityCoverageAssessmentResult`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `RoadProximityCoverageAssessmentResult`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_first_row` via `RoadProximityCoverageAssessmentResult`

**Exact class source**

```python
class RoadProximityCoverageAssessmentResult:
    """Unchanged road proximity plus its source-package boundary diagnosis."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]
    source_coverage: IgnBdTopoDepartmentCoverage
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_validated_crs`

**Purpose:** Implements `validated crs` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validated_crs(value: object, expected_epsg: int, label: str) -> CRS:
```

- Exact decorators: none.
- Declared return annotation: `CRS`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `expected_epsg` | positional-or-keyword | `int` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `actual`
- Explicit raise paths:
  - `RoadProximityCoverageError(f"{label} CRS is required")` under lexical guard `value is None`.
  - `RoadProximityCoverageError(f"{label} CRS is unreadable")`.
  - `RoadProximityCoverageError(f"{label} must use EPSG:{expected_epsg}")` under lexical guard `not actual.equals(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_parcel_frame` via `_validated_crs`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_parcel_frame` via `_validated_crs`
- direct call: `landscout.stages.assess_road_proximity_coverage::_require_same_parcels` via `_validated_crs`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_require_same_parcels` via `_validated_crs`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `_validated_crs`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_coverage_summary` via `_validated_crs`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_validated_crs`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_validated_crs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `actual.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validated_crs(value: object, expected_epsg: int, label: str) -> CRS:
    if value is None:
        raise RoadProximityCoverageError(f"{label} CRS is required")
    try:
        actual = CRS.from_user_input(value)
    except Exception as error:
        raise RoadProximityCoverageError(f"{label} CRS is unreadable") from error
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityCoverageError(f"{label} must use EPSG:{expected_epsg}")
    return actual
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalized_identity`

**Purpose:** Implements `normalized identity` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"".join(<br>        character for character in decomposed.casefold() if character.isalnum()<br>    )`
- Explicit raise paths:
  - `RoadProximityCoverageError(f"{label} must be a non-empty exact string")` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_normalized_identity`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_normalized_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `unicodedata.normalize` | `unicodedata.normalize` |
| `"".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `decomposed.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `character.isalnum` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(f"{label} must be a non-empty exact string")
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(
        character for character in decomposed.casefold() if character.isalnum()
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_exact_string`

**Purpose:** Implements `exact string` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _exact_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `RoadProximityCoverageError(f"{label} must be a non-empty exact string")` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |

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
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_safe_scalar_equal`

**Purpose:** Implements `null safe scalar equal` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _null_safe_scalar_equal(actual: object, expected: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `actual` | positional-or-keyword | `object` | `required` |
| `expected` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `bool(pd.isna(actual))`
  - `bool(actual == expected)`
  - `False`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_null_safe_scalar_equal`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_null_safe_scalar_equal`

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
def _null_safe_scalar_equal(actual: object, expected: object) -> bool:
    if expected is None:
        return bool(pd.isna(actual))
    try:
        return bool(actual == expected)
    except (TypeError, ValueError):
        return False
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_exact_ids`

**Purpose:** Implements `exact ids` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _exact_ids(values: pd.Series, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityCoverageError(f"{label} values must not be null")` under lexical guard `values.isna().any()`.
  - `RoadProximityCoverageError(f"{label} values must be exact strings")` under lexical guard `any(not isinstance(item, str) for item in items)`.
  - `RoadProximityCoverageError(<br>            f"{label} values must be non-empty without edge whitespace"<br>        )` under lexical guard `any(not item or item != item.strip() for item in items)`.
  - `RoadProximityCoverageError(f"{label} values must be unique")` under lexical guard `values.duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_parcel_frame` via `_exact_ids`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_parcel_frame` via `_exact_ids`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.strip` | `unresolved local/third-party receiver; no ownership inferred` |
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_parcel_frame`

**Purpose:** Implements `validate parcel frame` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `RoadProximityCoverageError(f"{label} must be a GeoDataFrame")` under lexical guard `not isinstance(frame, gpd.GeoDataFrame)`.
  - `RoadProximityCoverageError(f"{label} columns must be unique")` under lexical guard `frame.columns.duplicated().any()`.
  - `RoadProximityCoverageError(<br>            f"{label} is missing: " + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `RoadProximityCoverageError(f"{label} geometry must be active")` under lexical guard `frame.active_geometry_name != "geometry"`.
  - `RoadProximityCoverageError(f"{label} geometry must not be null")` under lexical guard `geometry.isna().any()`.
  - `RoadProximityCoverageError(f"{label} geometry must not be empty")` under lexical guard `geometry.is_empty.any()`.
  - `RoadProximityCoverageError(f"{label} geometry must be valid")` under lexical guard `not geometry.is_valid.all()`.
  - `RoadProximityCoverageError(<br>            f"{label} geometry must be Polygon or MultiPolygon"<br>        )` under lexical guard `not set(geometry.geom_type.dropna()) <= _PARCEL_GEOMETRY_TYPES`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_validate_parcel_frame`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_validate_parcel_frame`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_validate_parcel_frame`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_validate_parcel_frame`
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_parcel_frame`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_parcel_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_crs` | `landscout.stages.assess_road_proximity_coverage._validated_crs` |
| `_exact_ids` | `landscout.stages.assess_road_proximity_coverage._exact_ids` |
| `geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna().any`<br>`geometry.isna`<br>`geometry.is_empty.any`<br>`geometry.is_valid.all`<br>`geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_same_index`

**Purpose:** Implements `same index` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _same_index(left: pd.Index, right: pd.Index) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `left` | positional-or-keyword | `pd.Index` | `required` |
| `right` | positional-or-keyword | `pd.Index` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `bool(<br>        type(left) is type(right)<br>        and left.names == right.names<br>        and str(left.dtype) == str(right.dtype)<br>        and left.equals(right)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_require_same_parcels` via `_same_index`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_require_same_parcels` via `_same_index`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_same_index`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_same_index`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `left.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _same_index(left: pd.Index, right: pd.Index) -> bool:
    return bool(
        type(left) is type(right)
        and left.names == right.names
        and str(left.dtype) == str(right.dtype)
        and left.equals(right)
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_require_same_parcels`

**Purpose:** Implements `require same parcels` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _require_same_parcels(
    expected: gpd.GeoDataFrame,
    actual: gpd.GeoDataFrame,
    label: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `expected` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `actual` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityCoverageError(f"{label} parcel columns changed")` under lexical guard `list(actual.columns) != list(expected.columns)`.
  - `RoadProximityCoverageError(f"{label} parcel dtypes changed")` under lexical guard `not actual.dtypes.equals(expected.dtypes)`.
  - `RoadProximityCoverageError(f"{label} parcel index changed")` under lexical guard `not _same_index(actual.index, expected.index)`.
  - `RoadProximityCoverageError(f"{label} parcel CRS changed")` under lexical guard `not _validated_crs(actual.crs, 4326, label).equals(<br>        _validated_crs(expected.crs, 4326, label)<br>    )`.
  - `RoadProximityCoverageError(f"{label} parcel geometry changed")` under lexical guard `not actual.geometry.to_wkb().equals(expected.geometry.to_wkb())`.
  - `RoadProximityCoverageError(f"{label} parcel facts changed")` under lexical guard `not actual.drop(columns="geometry").equals(expected.drop(columns="geometry"))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_require_same_parcels`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_require_same_parcels`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_require_same_parcels`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_require_same_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `actual.dtypes.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_same_index` | `landscout.stages.assess_road_proximity_coverage._same_index` |
| `_validated_crs(actual.crs, 4326, label).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_crs` | `landscout.stages.assess_road_proximity_coverage._validated_crs` |
| `actual.geometry.to_wkb().equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.geometry.to_wkb` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual.drop(columns="geometry").equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.drop` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `actual.geometry.to_wkb().equals`<br>`actual.geometry.to_wkb`<br>`expected.geometry.to_wkb`<br>`actual.drop(columns="geometry").equals` |
| External process/environment | None directly present. |
| In-memory mutation | `actual.drop(columns="geometry")`<br>`expected.drop(columns="geometry")` |
| Direct parameter mutation | `actual.drop(columns="geometry")`<br>`expected.drop(columns="geometry")` |

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
    if not actual.drop(columns="geometry").equals(expected.drop(columns="geometry")):
        raise RoadProximityCoverageError(f"{label} parcel facts changed")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_finite_nonnegative`

**Purpose:** Implements `finite nonnegative` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
```

- Exact decorators: none.
- Declared return annotation: `np.ndarray`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `np.asarray(converted, dtype="float64")`
- Explicit raise paths:
  - `RoadProximityCoverageError(f"{label} must be numeric")` under lexical guard `not isinstance(value, Real) or isinstance(value, (bool, np.bool_))`.
  - `RoadProximityCoverageError(f"{label} must be finite and non-negative")` under lexical guard `not isfinite(numeric) or numeric < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_match_rows` via `_finite_nonnegative`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_match_rows` via `_finite_nonnegative`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_finite_nonnegative`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_finite_nonnegative`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `isfinite` | `math.isfinite` |
| `converted.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.asarray` | `numpy.asarray` |

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
| In-memory mutation | `converted.append(numeric)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
    converted: list[float] = []
    for value in values.tolist():
        if not isinstance(value, Real) or isinstance(value, (bool, np.bool_)):
            raise RoadProximityCoverageError(f"{label} must be numeric")
        numeric = float(value)
        if not isfinite(numeric) or numeric < 0:
            raise RoadProximityCoverageError(f"{label} must be finite and non-negative")
        converted.append(numeric)
    return np.asarray(converted, dtype="float64")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_class_coverage`

**Purpose:** Implements `validate class coverage` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validate_class_coverage(
    coverage: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coverage` | positional-or-keyword | `object` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `eligible`
- Explicit raise paths:
  - `RoadProximityCoverageError("Road class coverage is invalid")` under lexical guard `type(coverage) is not tuple or len(coverage) != len(classes)`.
  - `RoadProximityCoverageError("Road class coverage type is invalid")` under lexical guard `type(item) is not RoadProxyClassCoverage`.
  - `RoadProximityCoverageError("Road class coverage order is invalid")` under lexical guard `item.road_proxy_class != classes[position]`.
  - `RoadProximityCoverageError(<br>                "Road class coverage feature_count is invalid"<br>            )` under lexical guard `type(item.feature_count) is not int or item.feature_count < 0`.
  - `RoadProximityCoverageError(<br>                "Road class coverage distance eligibility is invalid"<br>            )` under lexical guard `type(item.distance_eligible) is not bool or (<br>            item.distance_eligible != (item.road_proxy_class in eligible)<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_validate_class_coverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_validate_class_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_match_rows`

**Purpose:** Implements `validate match rows` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validate_match_rows(
    table: pd.DataFrame,
    coverage: tuple[RoadProxyClassCoverage, ...],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `table` | positional-or-keyword | `pd.DataFrame` | `required` |
| `coverage` | positional-or-keyword | `tuple[RoadProxyClassCoverage, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityCoverageError(<br>                    "Empty road class contains selected road evidence"<br>                )` under lexical guard `item.feature_count == 0`.
  - `RoadProximityCoverageError(<br>                "Non-empty road class is missing a parcel match"<br>            )` under lexical guard `not matched.all()`.
  - `RoadProximityCoverageError("Matched road evidence is incomplete")` under lexical guard `rows.loc[:, list(required)].isna().any().any()`.
  - `RoadProximityCoverageError(<br>                    "Nearest road tie count must be an integer >= 1"<br>                )` under lexical guard `not isinstance(value, Integral)<br>                or isinstance(value, (bool, np.bool_))<br>                or int(value) < 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_validate_match_rows`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_upstream_result` via `_validate_match_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `by_class.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["road_proxy_class"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows["nearest_road_proxy_distance_m"].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `matched.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `matched.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `_finite_nonnegative` | `landscout.stages.assess_road_proximity_coverage._finite_nonnegative` |
| `rows.loc[:, list(required)].isna().any().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(required)].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.loc[:, list(required)].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows["nearest_road_tie_count"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
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
| CRS/geometry/spatial calculation | `rows["nearest_road_proxy_distance_m"].notna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
            if (
                matched.any()
                or rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any()
            ):
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
            raise RoadProximityCoverageError("Matched road evidence is incomplete")
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_upstream_result`

**Purpose:** Implements `validate upstream result` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validate_upstream_result(
    input_parcels: gpd.GeoDataFrame,
    result: object,
    policy: IgnRoadVehicleProxyPolicy,
) -> ParcelRoadProximityResult:
```

- Exact decorators: none.
- Declared return annotation: `ParcelRoadProximityResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `input_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `result` | positional-or-keyword | `object` | `required` |
| `policy` | positional-or-keyword | `IgnRoadVehicleProxyPolicy` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `RoadProximityCoverageError("Road proximity result type is invalid")` under lexical guard `type(result) is not ParcelRoadProximityResult`.
  - `RoadProximityCoverageError("Class proximity must be a plain DataFrame")` under lexical guard `type(table) is not pd.DataFrame`.
  - `RoadProximityCoverageError("Class proximity schema is invalid")` under lexical guard `table.columns.duplicated().any()<br>        or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS`.
  - `RoadProximityCoverageError("Class proximity index is invalid")` under lexical guard `not isinstance(table.index, pd.RangeIndex) or (<br>        table.index.start != 0 or table.index.step != 1 or table.index.name is not None<br>    )`.
  - `RoadProximityCoverageError("Class proximity row count is invalid")` under lexical guard `len(table) != len(parcels) * len(eligible)`.
  - `RoadProximityCoverageError("Class proximity parcel order is invalid")` under lexical guard `table["parcel_id"].tolist() != expected_ids`.
  - `RoadProximityCoverageError("Class proximity class order is invalid")` under lexical guard `table["road_proxy_class"].tolist() != expected_classes`.
  - `RoadProximityCoverageError("Class proximity pairs are duplicated")` under lexical guard `table.duplicated(["parcel_id", "road_proxy_class"]).any()`.
  - `RoadProximityCoverageError(<br>                f"Class proximity policy lineage is invalid: {column}"<br>            )` under lexical guard `table[column].isna().any() or not table[column].eq(expected).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_upstream_result`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_upstream_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `_validate_parcel_frame` | `landscout.stages.assess_road_proximity_coverage._validate_parcel_frame` |
| `_require_same_parcels` | `landscout.stages.assess_road_proximity_coverage._require_same_parcels` |
| `_validate_class_coverage` | `landscout.stages.assess_road_proximity_coverage._validate_class_coverage` |
| `table.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["road_proxy_class"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.duplicated(["parcel_id", "road_proxy_class"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_lineage.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].eq(expected).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `table[column].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_match_rows` | `landscout.stages.assess_road_proximity_coverage._validate_match_rows` |

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
    if (
        table.columns.duplicated().any()
        or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS
    ):
        raise RoadProximityCoverageError("Class proximity schema is invalid")
    if not isinstance(table.index, pd.RangeIndex) or (
        table.index.start != 0 or table.index.step != 1 or table.index.name is not None
    ):
        raise RoadProximityCoverageError("Class proximity index is invalid")
    if len(table) != len(parcels) * len(eligible):
        raise RoadProximityCoverageError("Class proximity row count is invalid")
    expected_ids = [
        parcel_id for parcel_id in parcels["parcel_id"].tolist() for _ in eligible
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_coverage_summary`

**Purpose:** Implements `validate coverage summary` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validate_coverage_summary(
    coverage: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
    config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityCoverageError("Coverage summary type is invalid")` under lexical guard `type(summary) is not IgnBdTopoCoverageLayerSummary`.
  - `RoadProximityCoverageError("Coverage summary layer is invalid")` under lexical guard `summary.source_layer_name != coverage.source_layer`.
  - `RoadProximityCoverageError("Coverage selected feature count is invalid")` under lexical guard `type(summary.selected_feature_count) is not int or (<br>        summary.selected_feature_count != len(frame)<br>    )`.
  - `RoadProximityCoverageError("Coverage source feature count is invalid")` under lexical guard `type(summary.source_feature_count) is not int<br>        or summary.source_feature_count < summary.selected_feature_count`.
  - `RoadProximityCoverageError("Coverage summary columns are invalid")` under lexical guard `type(summary.columns) is not tuple<br>        or not summary.columns<br>        or len(set(summary.columns)) != len(summary.columns)<br>        or any(<br>            not isinstance(column, str) or not column or column != column.strip()<br>            for column in summary.columns<br>        )`.
  - `RoadProximityCoverageError("Coverage frame schema is invalid")` under lexical guard `tuple(frame.columns) != (*summary.columns, *_COVERAGE_FRAME_LINEAGE)`.
  - `RoadProximityCoverageError("Coverage summary dtypes are invalid")` under lexical guard `type(summary.dtypes) is not tuple or summary.dtypes != expected_dtypes`.
  - `RoadProximityCoverageError(<br>            "Coverage configured department field is invalid"<br>        )` under lexical guard `summary.department_code_field != expected_field`.
  - `RoadProximityCoverageError("Coverage selected department is invalid")` under lexical guard `summary.selected_department_code != coverage.source_department_code`.
  - `RoadProximityCoverageError("Coverage department identity is invalid")` under lexical guard `not frame[expected_field].eq(coverage.source_department_code).all()`.
  - `RoadProximityCoverageError("Coverage summary spatial role is invalid")` under lexical guard `summary.spatial_role != _COVERAGE_SPATIAL_ROLE`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_validate_coverage_summary`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_source_coverage` via `_validate_coverage_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `_validated_crs` | `landscout.stages.assess_road_proximity_coverage._validated_crs` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `column.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[expected_field].eq(coverage.source_department_code).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[expected_field].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
            not isinstance(column, str) or not column or column != column.strip()
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_coverage`

**Purpose:** Implements `validate source coverage` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validate_source_coverage(
    source: object,
    road_source: IgnBdTopoRoadData,
    config: IgnBdTopoSourceConfig,
) -> tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[IgnBdTopoDepartmentCoverage, gpd.GeoDataFrame]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `object` | `required` |
| `road_source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `source, frame`
- Explicit raise paths:
  - `RoadProximityCoverageError("Coverage source type is invalid")` under lexical guard `type(source) is not IgnBdTopoDepartmentCoverage`.
  - `RoadProximityCoverageError(<br>            "Coverage must retain the exact road extraction identity"<br>        )` under lexical guard `source.extraction is not road_source.extraction`.
  - `RoadProximityCoverageError("Road package spatial role is invalid")` under lexical guard `road_source.extraction.spatial_role != _SOURCE_SPATIAL_ROLE or (<br>        archive.spatial_role != _SOURCE_SPATIAL_ROLE<br>    )`.
  - `RoadProximityCoverageError("Road package provider is not IGN")` under lexical guard `provider_identity not in _IGN_PROVIDER_IDENTITIES`.
  - `RoadProximityCoverageError("Road package product is not BD TOPO")` under lexical guard `product_identity != "bdtopo"`.
  - `RoadProximityCoverageError("Road package provider differs from config")` under lexical guard `provider_identity != _normalized_identity(config.provider, "Config provider")`.
  - `RoadProximityCoverageError("Road package product differs from config")` under lexical guard `product_identity != _normalized_identity(config.product, "Config product")`.
  - `RoadProximityCoverageError("Road package department differs from config")` under lexical guard `archive.department_code != config.department_code`.
  - `RoadProximityCoverageError("Road package archive SHA256 is invalid")` under lexical guard `_SHA256_PATTERN.fullmatch(archive.sha256) is None`.
  - `RoadProximityCoverageError(<br>            "Coverage does not use the configured physical layer"<br>        )` under lexical guard `source.source_layer != expected_layer`.
  - `RoadProximityCoverageError(<br>                f"Coverage package lineage is invalid: {name}"<br>            )` under lexical guard `not _null_safe_scalar_equal(getattr(source, name), expected)`.
  - `RoadProximityCoverageError("Coverage provider is not IGN")` under lexical guard `_normalized_identity(source.source_provider, "Coverage provider") not in (<br>        _IGN_PROVIDER_IDENTITIES<br>    )`.
  - `RoadProximityCoverageError("Coverage product is not BD TOPO")` under lexical guard `_normalized_identity(source.source_product, "Coverage product") != "bdtopo"`.
  - `RoadProximityCoverageError("Coverage archive SHA256 is invalid")` under lexical guard `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None`.
  - `RoadProximityCoverageError("Coverage must be a GeoDataFrame")` under lexical guard `not isinstance(frame, gpd.GeoDataFrame)`.
  - `RoadProximityCoverageError("Coverage columns must be unique")` under lexical guard `frame.columns.duplicated().any()`.
  - `RoadProximityCoverageError("Coverage geometry must exist and be active")` under lexical guard `"geometry" not in frame.columns or frame.active_geometry_name != "geometry"`.
  - `RoadProximityCoverageError(<br>            "Coverage must contain exactly one selected feature"<br>        )` under lexical guard `len(frame) != 1`.
  - `RoadProximityCoverageError("Coverage geometry must not be null")` under lexical guard `geometry.isna().any()`.
  - `RoadProximityCoverageError("Coverage geometry must not be empty")` under lexical guard `geometry.is_empty.any()`.
  - `RoadProximityCoverageError("Coverage geometry must be valid")` under lexical guard `not geometry.is_valid.all()`.
  - `RoadProximityCoverageError(<br>            "Coverage geometry must be Polygon or MultiPolygon"<br>        )` under lexical guard `not set(geometry.geom_type.dropna()) <= _COVERAGE_GEOMETRY_TYPES`.
  - `RoadProximityCoverageError(<br>                f"Coverage row lineage is invalid: {column}"<br>            )` under lexical guard `not _null_safe_scalar_equal(actual, expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_validate_source_coverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_validate_source_coverage`
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_source_coverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_source_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `_validated_crs` | `landscout.stages.assess_road_proximity_coverage._validated_crs` |
| `_normalized_identity` | `landscout.stages.assess_road_proximity_coverage._normalized_identity` |
| `_SHA256_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_discover_department_coverage_layer` | `landscout.sources.ign_bdtopo_fr._discover_department_coverage_layer` |
| `expected_scalars.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_scalar_equal` | `landscout.stages.assess_road_proximity_coverage._null_safe_scalar_equal` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_coverage_summary` | `landscout.stages.assess_road_proximity_coverage._validate_coverage_summary` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_SHA256_PATTERN.fullmatch` |
| CRS/geometry/spatial calculation | `geometry.isna().any`<br>`geometry.isna`<br>`geometry.is_empty.any`<br>`geometry.is_valid.all`<br>`geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_coverage_lineage`

**Purpose:** Implements `coverage lineage` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _coverage_lineage(
    coverage: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "road_source_coverage_provider": coverage.source_provider,<br>        "road_source_coverage_product": coverage.source_product,<br>        "road_source_coverage_department_code": coverage.source_department_code,<br>        "road_source_coverage_edition": coverage.source_edition,<br>        "road_source_coverage_product_version": coverage.source_product_version,<br>        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,<br>        "road_source_coverage_layer": coverage.source_layer,<br>        "road_source_coverage_spatial_role": coverage.spatial_role,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_expected_diagnostics` via `_coverage_lineage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_expected_diagnostics` via `_coverage_lineage`

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_parcel_coverage_diagnostics`

**Purpose:** Implements `parcel coverage diagnostics` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _parcel_coverage_diagnostics(
    parcels: gpd.GeoDataFrame,
    coverage_frame: gpd.GeoDataFrame,
) -> tuple[np.ndarray, np.ndarray]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[np.ndarray, np.ndarray]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `coverage_frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `boundary_distances, positions`
- Explicit raise paths:
  - `RoadProximityCoverageError(<br>            "Calculated boundary distances must be finite and non-negative"<br>        )` under lexical guard `not np.isfinite(measured).all() or (measured < 0).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_parcel_coverage_diagnostics`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_parcel_coverage_diagnostics`
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_parcel_coverage_diagnostics`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_parcel_coverage_diagnostics`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.asarray` | `numpy.asarray` |
| `force_2d` | `shapely.force_2d` |
| `boundary` | `shapely.boundary` |
| `covers` | `shapely.covers` |
| `intersects` | `shapely.intersects` |
| `distance` | `shapely.distance` |
| `np.isfinite(measured).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(measured < 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `np.where` | `numpy.where` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.to_crs`<br>`distance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_coverage_statuses`

**Purpose:** Implements `coverage statuses` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
) -> np.ndarray:
```

- Exact decorators: none.
- Declared return annotation: `np.ndarray`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `distances` | positional-or-keyword | `pd.Series` | `required` |
| `boundary_distances` | positional-or-keyword | `np.ndarray` | `required` |
| `positions` | positional-or-keyword | `np.ndarray` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `statuses`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_expected_diagnostics` via `_coverage_statuses`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_expected_diagnostics` via `_coverage_statuses`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `distances.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isnan` | `numpy.isnan` |
| `np.full` | `numpy.full` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `distances.to_numpy` |
| External process/environment | None directly present. |
| In-memory mutation | `statuses[outside] = "OUTSIDE_OR_CROSSING_COVERAGE"`<br>`statuses[internal & (numeric < boundary_distances)] = "NOT_BOUNDARY_LIMITED"`<br>`statuses[internal & (numeric >= boundary_distances)] = "BOUNDARY_LIMITED"` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_expected_diagnostics`

**Purpose:** Implements `expected diagnostics` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

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

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `table` | positional-or-keyword | `pd.DataFrame` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `boundary_distances` | positional-or-keyword | `np.ndarray` | `required` |
| `positions` | positional-or-keyword | `np.ndarray` | `required` |
| `coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output.loc[:, list(_DIAGNOSTIC_COLUMNS)]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_diagnosed_class_proximity` via `_expected_diagnostics`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_diagnosed_class_proximity` via `_expected_diagnostics`
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_expected_diagnostics`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_expected_diagnostics`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["parcel_id"].map(boundary_by_id).astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["parcel_id"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `table.index.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coverage_statuses` | `landscout.stages.assess_road_proximity_coverage._coverage_statuses` |
| `row_boundary.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `row_positions.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coverage_lineage(coverage).items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coverage_lineage` | `landscout.stages.assess_road_proximity_coverage._coverage_lineage` |
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
| In-memory mutation | `output["road_source_boundary_distance_m"] = row_boundary`<br>`output["road_source_coverage_position"] = row_positions`<br>`output["road_proximity_coverage_status"] = _coverage_statuses(<br>        table["nearest_road_proxy_distance_m"],<br>        row_boundary.to_numpy(dtype="float64"),<br>        row_positions.to_numpy(dtype=object),<br>    )`<br>`output[column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _expected_diagnostics(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
    boundary_by_id = dict(zip(parcels["parcel_id"], boundary_distances, strict=True))
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_diagnosed_class_proximity`

**Purpose:** Implements `diagnosed class proximity` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

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

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `table` | positional-or-keyword | `pd.DataFrame` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `boundary_distances` | positional-or-keyword | `np.ndarray` | `required` |
| `positions` | positional-or-keyword | `np.ndarray` | `required` |
| `coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_diagnosed_class_proximity`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_diagnosed_class_proximity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_expected_diagnostics` | `landscout.stages.assess_road_proximity_coverage._expected_diagnostics` |

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
| In-memory mutation | `output[column] = diagnostics[column]` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_selected_road_package`

**Purpose:** Implements `validate selected road package` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _validate_selected_road_package(
    table: pd.DataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `table` | positional-or-keyword | `pd.DataFrame` | `required` |
| `coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityCoverageError(<br>                f"Selected road package lineage differs from coverage: {column}"<br>            )` under lexical guard `selected.isna().any() or not selected.eq(value).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_validate_selected_road_package`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_validate_assessment_result` via `_validate_selected_road_package`
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_selected_road_package`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_selected_road_package`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `table["nearest_road_proxy_distance_m"].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected.eq(value).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `table["nearest_road_proxy_distance_m"].notna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_assessment_result`

**Purpose:** Implements `validate assessment result` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `input_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `proximity` | positional-or-keyword | `ParcelRoadProximityResult` | `required` |
| `road_source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `loaded_coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |
| `result` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `RoadProximityCoverageError("Coverage assessment result type is invalid")` under lexical guard `type(result) is not RoadProximityCoverageAssessmentResult`.
  - `RoadProximityCoverageError("Coverage assessment source was not preserved")` under lexical guard `result.source_coverage is not loaded_coverage`.
  - `RoadProximityCoverageError("Road class coverage was not preserved")` under lexical guard `result.class_coverage is not proximity.class_coverage`.
  - `RoadProximityCoverageError("Coverage class proximity is invalid")` under lexical guard `type(output) is not pd.DataFrame`.
  - `RoadProximityCoverageError("Coverage class proximity schema is invalid")` under lexical guard `output.columns.duplicated().any() or tuple(output.columns) != expected_columns`.
  - `RoadProximityCoverageError("Coverage class proximity index changed")` under lexical guard `not _same_index(output.index, source.index)`.
  - `RoadProximityCoverageError(<br>            "Coverage assessment changed original class proximity facts"<br>        )` under lexical guard `not prefix.dtypes.equals(source.dtypes) or not prefix.equals(source)`.
  - `RoadProximityCoverageError(<br>            "Coverage diagnostics differ from geometric reconstruction"<br>        )` under lexical guard `not actual.dtypes.equals(expected.dtypes) or not actual.equals(expected)`.
  - `RoadProximityCoverageError("Coverage position is invalid")` under lexical guard `position_values.isna().any() or not set(position_values.unique()) <= _POSITIONS`.
  - `RoadProximityCoverageError(<br>            "Outside or crossing rows require zero boundary distance"<br>        )` under lexical guard `(numeric[outside] != 0.0).any()`.
  - `RoadProximityCoverageError("Coverage status is invalid")` under lexical guard `statuses.isna().any() or not set(statuses.unique()) <= _STATUSES`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_assessment_result`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::_assess_road_proximity_coverage` via `_validate_assessment_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `_validate_source_coverage` | `landscout.stages.assess_road_proximity_coverage._validate_source_coverage` |
| `_validate_parcel_frame` | `landscout.stages.assess_road_proximity_coverage._validate_parcel_frame` |
| `_require_same_parcels` | `landscout.stages.assess_road_proximity_coverage._require_same_parcels` |
| `output.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `output.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_same_index` | `landscout.stages.assess_road_proximity_coverage._same_index` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `prefix.dtypes.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `prefix.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcel_coverage_diagnostics` | `landscout.stages.assess_road_proximity_coverage._parcel_coverage_diagnostics` |
| `_expected_diagnostics` | `landscout.stages.assess_road_proximity_coverage._expected_diagnostics` |
| `actual.dtypes.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_finite_nonnegative` | `landscout.stages.assess_road_proximity_coverage._finite_nonnegative` |
| `position_values.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `position_values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `position_values.unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `position_values.eq("OUTSIDE_OR_CROSSING_COVERAGE").to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `position_values.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `(numeric[outside] != 0.0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_selected_road_package` | `landscout.stages.assess_road_proximity_coverage._validate_selected_road_package` |

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
        raise RoadProximityCoverageError("Coverage class proximity schema is invalid")
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
    outside = position_values.eq("OUTSIDE_OR_CROSSING_COVERAGE").to_numpy(dtype="bool")
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_assess_road_proximity_coverage`

**Purpose:** Implements `assess road proximity coverage` within the file role: Diagnoses road proxy proximity against the verified IGN department coverage boundary.

**Exact signature**

```python
def _assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None,
) -> RoadProximityCoverageAssessmentResult:
```

- Exact decorators: none.
- Declared return annotation: `RoadProximityCoverageAssessmentResult`.

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
- direct call: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `_assess_road_proximity_coverage`
- value/type reference: `landscout.stages.assess_road_proximity_coverage::assess_road_proximity_coverage` via `_assess_road_proximity_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_parcel_frame` | `landscout.stages.assess_road_proximity_coverage._validate_parcel_frame` |
| `enrich_parcel_road_proximity` | `landscout.stages.enrich_road_proximity.enrich_parcel_road_proximity` |
| `load_ign_road_vehicle_proxy_policy` | `landscout.stages.road_vehicle_proxy_policy.load_ign_road_vehicle_proxy_policy` |
| `_validate_upstream_result` | `landscout.stages.assess_road_proximity_coverage._validate_upstream_result` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `_validate_source_coverage` | `landscout.stages.assess_road_proximity_coverage._validate_source_coverage` |
| `_validate_selected_road_package` | `landscout.stages.assess_road_proximity_coverage._validate_selected_road_package` |
| `_parcel_coverage_diagnostics` | `landscout.stages.assess_road_proximity_coverage._parcel_coverage_diagnostics` |
| `_diagnosed_class_proximity` | `landscout.stages.assess_road_proximity_coverage._diagnosed_class_proximity` |
| `RoadProximityCoverageAssessmentResult` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageAssessmentResult` |
| `validated_proximity.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_assessment_result` | `landscout.stages.assess_road_proximity_coverage._validate_assessment_result` |

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
    validated_proximity = _validate_upstream_result(input_parcels, proximity, policy)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `assess_road_proximity_coverage`

**Purpose:** Diagnose source-bound road proximity using the verified package boundary.

**Exact signature**

```python
def assess_road_proximity_coverage(
    parcels: gpd.GeoDataFrame,
    road_source: IgnBdTopoRoadData,
    source_config: IgnBdTopoSourceConfig,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
```

- Exact decorators: none.
- Declared return annotation: `RoadProximityCoverageAssessmentResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `road_source` | positional-or-keyword | `IgnBdTopoRoadData` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |
| `policy_path` | positional-or-keyword | `Path \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_assess_road_proximity_coverage(<br>            parcels, road_source, source_config, policy_path<br>        )`
- Explicit raise paths:
  - `RoadProximityCoverageError("parcels must be a GeoDataFrame")` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `RoadProximityCoverageError("road_source must be an IgnBdTopoRoadData")` under lexical guard `type(road_source) is not IgnBdTopoRoadData`.
  - `RoadProximityCoverageError(<br>                "source_config must be an IgnBdTopoSourceConfig"<br>            )` under lexical guard `type(source_config) is not IgnBdTopoSourceConfig`.
  - `RoadProximityCoverageError(<br>                "policy_path must be a pathlib.Path or None"<br>            )` under lexical guard `policy_path is not None and not isinstance(policy_path, Path)`.
  - `re-raise`.
  - `RoadProximityCoverageError(<br>            "Road proximity coverage cannot be assessed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- import: `tests.unit.test_assess_road_proximity_coverage::<module>` via `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- direct call: `tests.unit.test_assess_road_proximity_coverage::_assess` via `assess_road_proximity_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::_assess` via `assess_road_proximity_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_wrong_public_input_type_is_controlled_and_fast` via `assess_road_proximity_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_wrong_public_input_type_is_controlled_and_fast` via `assess_road_proximity_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `assess_road_proximity_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_source_chain_calls_proximity_then_coverage_exactly_once` via `assess_road_proximity_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_proximity_failure_stops_coverage_loading` via `assess_road_proximity_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_proximity_failure_stops_coverage_loading` via `assess_road_proximity_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `assess_road_proximity_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_loader_failure_is_controlled` via `assess_road_proximity_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `assess_road_proximity_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_malformed_upstream_result_fails_before_coverage_load` via `assess_road_proximity_coverage`
- direct call: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `assess_road_proximity_coverage`
- value/type reference: `tests.unit.test_assess_road_proximity_coverage::test_coverage_spatial_role_and_source_type_are_controlled` via `assess_road_proximity_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `_assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage._assess_road_proximity_coverage` |

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
            raise RoadProximityCoverageError("road_source must be an IgnBdTopoRoadData")
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `_COVERAGE_LINEAGE_COLUMNS`, `_DIAGNOSTIC_COLUMNS`, `_SELECTED_ROAD_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `RoadProximityCoverageAssessmentResult` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageAssessmentResult` |
| `RoadProximityCoverageError` | `landscout.stages.assess_road_proximity_coverage.RoadProximityCoverageError` |
| `assess_road_proximity_coverage` | `landscout.stages.assess_road_proximity_coverage.assess_road_proximity_coverage` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Diagnose road proximity against one verified IGN package boundary."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from math import isfinite
from numbers import Integral, Real
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS
from shapely import (  # type: ignore[import-untyped]
    boundary,
    covers,
    distance,
    force_2d,
    intersects,
)

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)
from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
    enrich_parcel_road_proximity,
)
from landscout.stages.road_vehicle_proxy_policy import (
    IgnRoadVehicleProxyPolicy,
    load_ign_road_vehicle_proxy_policy,
)

__all__ = [
    "RoadProximityCoverageAssessmentResult",
    "RoadProximityCoverageError",
    "assess_road_proximity_coverage",
]

_CALCULATION_CRS = "EPSG:2154"
_PROXIMITY_SCOPE = "WITHIN_VERIFIED_SOURCE_PACKAGE"
_COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
_SOURCE_SPATIAL_ROLE = "PROXY_GEOMETRY"
_POSITIONS = frozenset({"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"})
_STATUSES = frozenset(
    {
        "NO_MATCH",
        "NOT_BOUNDARY_LIMITED",
        "BOUNDARY_LIMITED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    }
)
_PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
_COVERAGE_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institutnationaldelinformationgeographiqueetforestiereign",
    }
)
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
_DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
    *_COVERAGE_LINEAGE_COLUMNS,
)
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


class RoadProximityCoverageError(ValueError):
    """Raised when road source-boundary diagnostics cannot be proven safely."""


@dataclass(frozen=True)
class RoadProximityCoverageAssessmentResult:
    """Unchanged road proximity plus its source-package boundary diagnosis."""

    parcels: gpd.GeoDataFrame
    class_proximity: pd.DataFrame
    class_coverage: tuple[RoadProxyClassCoverage, ...]
    source_coverage: IgnBdTopoDepartmentCoverage


def _validated_crs(value: object, expected_epsg: int, label: str) -> CRS:
    if value is None:
        raise RoadProximityCoverageError(f"{label} CRS is required")
    try:
        actual = CRS.from_user_input(value)
    except Exception as error:
        raise RoadProximityCoverageError(f"{label} CRS is unreadable") from error
    expected = CRS.from_epsg(expected_epsg)
    if not actual.equals(expected):
        raise RoadProximityCoverageError(f"{label} must use EPSG:{expected_epsg}")
    return actual


def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(f"{label} must be a non-empty exact string")
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(
        character for character in decomposed.casefold() if character.isalnum()
    )


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise RoadProximityCoverageError(f"{label} must be a non-empty exact string")
    return value


def _null_safe_scalar_equal(actual: object, expected: object) -> bool:
    if expected is None:
        return bool(pd.isna(actual))
    try:
        return bool(actual == expected)
    except (TypeError, ValueError):
        return False


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


def _same_index(left: pd.Index, right: pd.Index) -> bool:
    return bool(
        type(left) is type(right)
        and left.names == right.names
        and str(left.dtype) == str(right.dtype)
        and left.equals(right)
    )


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
    if not actual.drop(columns="geometry").equals(expected.drop(columns="geometry")):
        raise RoadProximityCoverageError(f"{label} parcel facts changed")


def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
    converted: list[float] = []
    for value in values.tolist():
        if not isinstance(value, Real) or isinstance(value, (bool, np.bool_)):
            raise RoadProximityCoverageError(f"{label} must be numeric")
        numeric = float(value)
        if not isfinite(numeric) or numeric < 0:
            raise RoadProximityCoverageError(f"{label} must be finite and non-negative")
        converted.append(numeric)
    return np.asarray(converted, dtype="float64")


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
            if (
                matched.any()
                or rows.loc[:, list(_SELECTED_ROAD_COLUMNS)].notna().any().any()
            ):
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
            raise RoadProximityCoverageError("Matched road evidence is incomplete")
        for value in rows["nearest_road_tie_count"].tolist():
            if (
                not isinstance(value, Integral)
                or isinstance(value, (bool, np.bool_))
                or int(value) < 1
            ):
                raise RoadProximityCoverageError(
                    "Nearest road tie count must be an integer >= 1"
                )


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
    if (
        table.columns.duplicated().any()
        or tuple(table.columns) != CLASS_PROXIMITY_COLUMNS
    ):
        raise RoadProximityCoverageError("Class proximity schema is invalid")
    if not isinstance(table.index, pd.RangeIndex) or (
        table.index.start != 0 or table.index.step != 1 or table.index.name is not None
    ):
        raise RoadProximityCoverageError("Class proximity index is invalid")
    if len(table) != len(parcels) * len(eligible):
        raise RoadProximityCoverageError("Class proximity row count is invalid")
    expected_ids = [
        parcel_id for parcel_id in parcels["parcel_id"].tolist() for _ in eligible
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
            not isinstance(column, str) or not column or column != column.strip()
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


def _expected_diagnostics(
    table: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    boundary_distances: np.ndarray,
    positions: np.ndarray,
    coverage: IgnBdTopoDepartmentCoverage,
) -> pd.DataFrame:
    boundary_by_id = dict(zip(parcels["parcel_id"], boundary_distances, strict=True))
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
        raise RoadProximityCoverageError("Coverage class proximity schema is invalid")
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
    outside = position_values.eq("OUTSIDE_OR_CROSSING_COVERAGE").to_numpy(dtype="bool")
    if (numeric[outside] != 0.0).any():
        raise RoadProximityCoverageError(
            "Outside or crossing rows require zero boundary distance"
        )
    statuses = output["road_proximity_coverage_status"]
    if statuses.isna().any() or not set(statuses.unique()) <= _STATUSES:
        raise RoadProximityCoverageError("Coverage status is invalid")
    _validate_selected_road_package(output, coverage)


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
    validated_proximity = _validate_upstream_result(input_parcels, proximity, policy)
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
            raise RoadProximityCoverageError("road_source must be an IgnBdTopoRoadData")
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
