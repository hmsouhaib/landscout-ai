# `src/landscout/stages/assess_grid_coverage.py`

## File identity

- Repository path: `src/landscout/stages/assess_grid_coverage.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Diagnoses grid proxy distances against the configured IGN source-package boundary.
- Source SHA256: `303571815dbdc314a0800b72ce782958e2603b3c93119d7e15ae96c620121abb`

## 1. STEP 7F.1A.4 contract delta

- Revalidates the immutable IGN config and derives coverage only from the fresh config-selected department object.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Diagnoses grid proxy distances against the configured IGN source-package boundary.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import re`
- `import unicodedata`
- `from dataclasses import dataclass`
- `from math import isfinite`
- `from numbers import Real`
- `from typing import Literal`

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
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)`
- `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `CALCULATION_CRS`

- Category: module constant or closed domain.
- Exact declaration:

```python
CALCULATION_CRS = "EPSG:2154"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `COVERAGE_SPATIAL_ROLE`

- Category: module constant or closed domain.
- Exact declaration:

```python
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CoverageStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
CoverageStatus = Literal[
    "NOT_BOUNDARY_LIMITED",
    "BOUNDARY_LIMITED",
    "OUTSIDE_OR_CROSSING_COVERAGE",
    "NO_MATCH",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CoveragePosition`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
CoveragePosition = Literal["FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `COVERAGE_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
COVERAGE_STATUSES = frozenset(
    {
        "NOT_BOUNDARY_LIMITED",
        "BOUNDARY_LIMITED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
        "NO_MATCH",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `COVERAGE_POSITIONS`

- Category: module constant or closed domain.
- Exact declaration:

```python
COVERAGE_POSITIONS = frozenset({"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PARCEL_DIAGNOSTIC_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
PARCEL_DIAGNOSTIC_COLUMNS = (
    "grid_source_boundary_distance_m",
    "grid_source_coverage_position",
    "nearest_line_coverage_status",
    "nearest_exact_line_coverage_status",
    "nearest_post_coverage_status",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `grid_source_boundary_distance_m`
  - `grid_source_coverage_position`
  - `nearest_line_coverage_status`
  - `nearest_exact_line_coverage_status`
  - `nearest_post_coverage_status`

### `VOLTAGE_DIAGNOSTIC_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
VOLTAGE_DIAGNOSTIC_COLUMNS = (
    "source_boundary_distance_m",
    "coverage_status",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `source_boundary_distance_m`
  - `coverage_status`

### `COVERAGE_LINEAGE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
COVERAGE_LINEAGE_COLUMNS = (
    "grid_source_coverage_provider",
    "grid_source_coverage_product",
    "grid_source_coverage_department_code",
    "grid_source_coverage_edition",
    "grid_source_coverage_product_version",
    "grid_source_coverage_archive_sha256",
    "grid_source_coverage_layer",
    "grid_source_coverage_spatial_role",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `grid_source_coverage_provider`
  - `grid_source_coverage_product`
  - `grid_source_coverage_department_code`
  - `grid_source_coverage_edition`
  - `grid_source_coverage_product_version`
  - `grid_source_coverage_archive_sha256`
  - `grid_source_coverage_layer`
  - `grid_source_coverage_spatial_role`

### `_SOURCE_LINEAGE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_SOURCE_LINEAGE_COLUMNS = (
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

### `_SHA256_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_PARCEL_GENERATED_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_PARCEL_GENERATED_COLUMNS = frozenset(
    {*PARCEL_DIAGNOSTIC_COLUMNS, *COVERAGE_LINEAGE_COLUMNS}
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `GridCoverageAssessmentError`

**Source purpose:** Raised when coverage diagnostics cannot be calculated safely.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`
- constructor call: `landscout.stages.assess_grid_coverage::_reject_parcel_output_collisions` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_reject_parcel_output_collisions` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_validated_lambert93` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_validated_lambert93` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_normalized_identity` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_normalized_identity` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_strict_nonnegative_integer` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_strict_nonnegative_integer` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_validate_proximity_source_identity` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_proximity_source_identity` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_finite_nonnegative` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_finite_nonnegative` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_preserves_original_frame` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_preserves_original_frame` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `GridCoverageAssessmentError`
- constructor call: `landscout.stages.assess_grid_coverage::_boundary_profile` via `GridCoverageAssessmentError`
- value/type reference: `landscout.stages.assess_grid_coverage::_boundary_profile` via `GridCoverageAssessmentError`

**Exact class source**

```python
class GridCoverageAssessmentError(ValueError):
    """Raised when coverage diagnostics cannot be calculated safely."""
```

### `GridCoverageAssessmentResult`

**Source purpose:** Coverage-annotated copies of both grid-proximity representations.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |
| `voltage_level_proximity` | `pd.DataFrame` | `required` | `voltage_level_proximity: pd.DataFrame` |
| `voltage_level_coverage` | `tuple[VoltageLevelCoverage, ...]` | `required` | `voltage_level_coverage: tuple[VoltageLevelCoverage, ...]` |
| `source_coverage` | `IgnBdTopoDepartmentCoverage` | `required` | `source_coverage: IgnBdTopoDepartmentCoverage` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `GridCoverageAssessmentResult`
- constructor call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `GridCoverageAssessmentResult`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `GridCoverageAssessmentResult`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `GridCoverageAssessmentResult`
- value/type reference: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `GridCoverageAssessmentResult`

**Exact class source**

```python
class GridCoverageAssessmentResult:
    """Coverage-annotated copies of both grid-proximity representations."""

    parcels: gpd.GeoDataFrame
    voltage_level_proximity: pd.DataFrame
    voltage_level_coverage: tuple[VoltageLevelCoverage, ...]
    source_coverage: IgnBdTopoDepartmentCoverage
```

### `BoundaryDistanceProfile`

**Source purpose:** Defines `BoundaryDistanceProfile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `count` | `int` | `required` | `count: int` |
| `minimum` | `float` | `required` | `minimum: float` |
| `p01` | `float` | `required` | `p01: float` |
| `p05` | `float` | `required` | `p05: float` |
| `p10` | `float` | `required` | `p10: float` |
| `p25` | `float` | `required` | `p25: float` |
| `p50` | `float` | `required` | `p50: float` |
| `p75` | `float` | `required` | `p75: float` |
| `p90` | `float` | `required` | `p90: float` |
| `p95` | `float` | `required` | `p95: float` |
| `p99` | `float` | `required` | `p99: float` |
| `maximum` | `float` | `required` | `maximum: float` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`
- constructor call: `landscout.stages.assess_grid_coverage::_boundary_profile` via `BoundaryDistanceProfile`
- value/type reference: `landscout.stages.assess_grid_coverage::_boundary_profile` via `BoundaryDistanceProfile`

**Exact class source**

```python
class BoundaryDistanceProfile:
    count: int
    minimum: float
    p01: float
    p05: float
    p10: float
    p25: float
    p50: float
    p75: float
    p90: float
    p95: float
    p99: float
    maximum: float
```

### `CoverageStatusCounts`

**Source purpose:** Defines `CoverageStatusCounts`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `not_boundary_limited` | `int` | `required` | `not_boundary_limited: int` |
| `boundary_limited` | `int` | `required` | `boundary_limited: int` |
| `outside_or_crossing_coverage` | `int` | `required` | `outside_or_crossing_coverage: int` |
| `no_match` | `int` | `required` | `no_match: int` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`
- constructor call: `landscout.stages.assess_grid_coverage::_status_counts` via `CoverageStatusCounts`
- value/type reference: `landscout.stages.assess_grid_coverage::_status_counts` via `CoverageStatusCounts`

**Exact class source**

```python
class CoverageStatusCounts:
    not_boundary_limited: int
    boundary_limited: int
    outside_or_crossing_coverage: int
    no_match: int
```

### `VoltageCoverageStatusProfile`

**Source purpose:** Defines `VoltageCoverageStatusProfile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `voltage_kv` | `float` | `required` | `voltage_kv: float` |
| `parcel_count` | `int` | `required` | `parcel_count: int` |
| `statuses` | `CoverageStatusCounts` | `required` | `statuses: CoverageStatusCounts` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`
- constructor call: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `VoltageCoverageStatusProfile`
- value/type reference: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `VoltageCoverageStatusProfile`

**Exact class source**

```python
class VoltageCoverageStatusProfile:
    voltage_kv: float
    parcel_count: int
    statuses: CoverageStatusCounts
```

### `GridCoverageProfile`

**Source purpose:** Defines `GridCoverageProfile`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `parcel_count` | `int` | `required` | `parcel_count: int` |
| `fully_covered_count` | `int` | `required` | `fully_covered_count: int` |
| `outside_or_crossing_count` | `int` | `required` | `outside_or_crossing_count: int` |
| `boundary_distance` | `BoundaryDistanceProfile` | `required` | `boundary_distance: BoundaryDistanceProfile` |
| `nearest_line` | `CoverageStatusCounts` | `required` | `nearest_line: CoverageStatusCounts` |
| `nearest_exact_line` | `CoverageStatusCounts` | `required` | `nearest_exact_line: CoverageStatusCounts` |
| `nearest_post` | `CoverageStatusCounts` | `required` | `nearest_post: CoverageStatusCounts` |
| `voltage_levels` | `tuple[VoltageCoverageStatusProfile, ...]` | `required` | `voltage_levels: tuple[VoltageCoverageStatusProfile, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`
- constructor call: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `GridCoverageProfile`
- value/type reference: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `GridCoverageProfile`

**Exact class source**

```python
class GridCoverageProfile:
    parcel_count: int
    fully_covered_count: int
    outside_or_crossing_count: int
    boundary_distance: BoundaryDistanceProfile
    nearest_line: CoverageStatusCounts
    nearest_exact_line: CoverageStatusCounts
    nearest_post: CoverageStatusCounts
    voltage_levels: tuple[VoltageCoverageStatusProfile, ...]
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_reject_parcel_output_collisions`

**Purpose:** Implements `reject parcel output collisions` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _reject_parcel_output_collisions(parcels: gpd.GeoDataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridCoverageAssessmentError(<br>            "Parcel input collides with generated grid-coverage columns: "<br>            + ", ".join(sorted(collisions))<br>        )` under lexical guard `collisions`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_reject_parcel_output_collisions`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_reject_parcel_output_collisions`
- direct call: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `_reject_parcel_output_collisions`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `_reject_parcel_output_collisions`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _reject_parcel_output_collisions(parcels: gpd.GeoDataFrame) -> None:
    collisions = _PARCEL_GENERATED_COLUMNS & set(parcels.columns)
    if collisions:
        raise GridCoverageAssessmentError(
            "Parcel input collides with generated grid-coverage columns: "
            + ", ".join(sorted(collisions))
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_lambert93`

**Purpose:** Implements `validated lambert93` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _validated_lambert93(value: object, label: str) -> CRS:
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
  - `crs`
- Explicit raise paths:
  - `GridCoverageAssessmentError(f"{label} CRS is required")` under lexical guard `value is None`.
  - `GridCoverageAssessmentError(f"{label} CRS is unreadable")`.
  - `GridCoverageAssessmentError(f"{label} must use EPSG:2154")` under lexical guard `not crs.is_projected or not crs.equals(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `_validated_lambert93`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `_validated_lambert93`
- direct call: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `_validated_lambert93`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `_validated_lambert93`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validated_lambert93(value: object, label: str) -> CRS:
    if value is None:
        raise GridCoverageAssessmentError(f"{label} CRS is required")
    try:
        crs = CRS.from_user_input(value)
    except Exception as error:
        raise GridCoverageAssessmentError(f"{label} CRS is unreadable") from error
    expected = CRS.from_epsg(2154)
    if not crs.is_projected or not crs.equals(expected):
        raise GridCoverageAssessmentError(f"{label} must use EPSG:2154")
    return crs
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalized_identity`

**Purpose:** Implements `normalized identity` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

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
  - `GridCoverageAssessmentError(<br>            f"Department coverage {label} must be a non-empty exact string"<br>        )` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `_normalized_identity`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `_normalized_identity`
- direct call: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `_normalized_identity`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_configured_coverage_identity` via `_normalized_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
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
        raise GridCoverageAssessmentError(
            f"Department coverage {label} must be a non-empty exact string"
        )
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(
        character for character in decomposed.casefold() if character.isalnum()
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_nonnegative_integer`

**Purpose:** Implements `strict nonnegative integer` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `GridCoverageAssessmentError(<br>            f"Department coverage summary {label} must be a non-negative integer"<br>        )` under lexical guard `type(value) is not int or value < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_coverage_summary` via `_strict_nonnegative_integer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |

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
def _strict_nonnegative_integer(value: object, label: str) -> int:
    if type(value) is not int or value < 0:
        raise GridCoverageAssessmentError(
            f"Department coverage summary {label} must be a non-negative integer"
        )
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_coverage_summary`

**Purpose:** Implements `validate coverage summary` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _validate_coverage_summary(
    source: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridCoverageAssessmentError("Department coverage summary type is invalid")` under lexical guard `type(summary) is not IgnBdTopoCoverageLayerSummary`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary layer does not match source lineage"<br>        )` under lexical guard `summary.source_layer_name != source.source_layer`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary CRS does not match the selected frame"<br>        )` under lexical guard `not summary_crs.equals(frame_crs)`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary selected feature count does not match frame"<br>        )` under lexical guard `type(summary.selected_feature_count) is not int or (<br>        summary.selected_feature_count != len(frame)<br>    )`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary source count is smaller than selected count"<br>        )` under lexical guard `source_count < summary.selected_feature_count`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary columns are invalid"<br>        )` under lexical guard `type(summary.columns) is not tuple<br>        or not summary.columns<br>        or any(<br>            not isinstance(column, str) or not column or column != column.strip()<br>            for column in summary.columns<br>        )<br>        or len(set(summary.columns)) != len(summary.columns)`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary ordered columns do not match frame"<br>        )` under lexical guard `tuple(str(column) for column in frame.columns) != expected_frame_columns`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary ordered dtypes do not match frame"<br>        )` under lexical guard `type(summary.dtypes) is not tuple or summary.dtypes != observed_dtypes`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary geometry count exceeds source count"<br>        )` under lexical guard `any(count > source_count for count in geometry_counts)`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary geometry types are invalid"<br>        )` under lexical guard `type(geometry_types) is not tuple<br>        or geometry_types != tuple(sorted(set(geometry_types)))<br>        or not set(geometry_types) <= {"Polygon", "MultiPolygon"}`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary geometry facts do not match frame"<br>        )` under lexical guard `source_count == summary.selected_feature_count and (<br>        geometry_counts != selected_counts or geometry_types != selected_types<br>    )`.
  - `GridCoverageAssessmentError(<br>            "Department coverage selected geometry contradicts source summary"<br>        )` under lexical guard `any(<br>        observed > reported<br>        for observed, reported in zip(selected_counts, geometry_counts, strict=True)<br>    ) or not set(selected_types) <= set(geometry_types)`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary department field is invalid"<br>        )` under lexical guard `not isinstance(department_field, str)<br>        or not department_field<br>        or department_field != department_field.strip()<br>        or department_field not in summary.columns`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary selected department code is inconsistent"<br>        )` under lexical guard `summary.selected_department_code != source.source_department_code`.
  - `GridCoverageAssessmentError(<br>            "Department coverage selected department field is inconsistent"<br>        )` under lexical guard `not frame[department_field].eq(source.source_department_code).all()`.
  - `GridCoverageAssessmentError(<br>            "Department coverage summary spatial role is inconsistent"<br>        )` under lexical guard `summary.spatial_role != source.spatial_role`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `_validate_coverage_summary`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_source_coverage` via `_validate_coverage_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `_validated_lambert93` | `landscout.stages.assess_grid_coverage._validated_lambert93` |
| `summary_crs.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonnegative_integer` | `landscout.stages.assess_grid_coverage._strict_nonnegative_integer` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `column.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~selected_geometry.isna() & selected_geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(<br>                ~selected_geometry.isna()<br>                & ~selected_geometry.is_empty<br>                & ~selected_geometry.is_valid<br>            ).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.geom_type.dropna().unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `selected_geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `department_field.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[department_field].eq(source.source_department_code).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[department_field].eq` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `selected_geometry.isna().sum`<br>`selected_geometry.isna`<br>`(~selected_geometry.isna() & selected_geometry.is_empty).sum`<br>`(<br>                ~selected_geometry.isna()<br>                & ~selected_geometry.is_empty<br>                & ~selected_geometry.is_valid<br>            ).sum`<br>`selected_geometry.geom_type.dropna().unique`<br>`selected_geometry.geom_type.dropna` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_coverage_summary(
    source: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
) -> None:
    summary = source.summary
    if type(summary) is not IgnBdTopoCoverageLayerSummary:
        raise GridCoverageAssessmentError("Department coverage summary type is invalid")
    if summary.source_layer_name != source.source_layer:
        raise GridCoverageAssessmentError(
            "Department coverage summary layer does not match source lineage"
        )
    summary_crs = _validated_lambert93(summary.crs, "Department coverage summary")
    frame_crs = _validated_lambert93(frame.crs, "Department coverage")
    if not summary_crs.equals(frame_crs):
        raise GridCoverageAssessmentError(
            "Department coverage summary CRS does not match the selected frame"
        )
    if type(summary.selected_feature_count) is not int or (
        summary.selected_feature_count != len(frame)
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary selected feature count does not match frame"
        )
    source_count = _strict_nonnegative_integer(
        summary.source_feature_count,
        "source_feature_count",
    )
    if source_count < summary.selected_feature_count:
        raise GridCoverageAssessmentError(
            "Department coverage summary source count is smaller than selected count"
        )
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or any(
            not isinstance(column, str) or not column or column != column.strip()
            for column in summary.columns
        )
        or len(set(summary.columns)) != len(summary.columns)
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary columns are invalid"
        )
    expected_frame_columns = (*summary.columns, *_SOURCE_LINEAGE_COLUMNS)
    if tuple(str(column) for column in frame.columns) != expected_frame_columns:
        raise GridCoverageAssessmentError(
            "Department coverage summary ordered columns do not match frame"
        )
    observed_dtypes = tuple(
        (column, str(frame[column].dtype)) for column in summary.columns
    )
    if type(summary.dtypes) is not tuple or summary.dtypes != observed_dtypes:
        raise GridCoverageAssessmentError(
            "Department coverage summary ordered dtypes do not match frame"
        )
    geometry_counts = (
        _strict_nonnegative_integer(
            summary.null_geometry_count,
            "null_geometry_count",
        ),
        _strict_nonnegative_integer(
            summary.empty_geometry_count,
            "empty_geometry_count",
        ),
        _strict_nonnegative_integer(
            summary.invalid_geometry_count,
            "invalid_geometry_count",
        ),
    )
    if any(count > source_count for count in geometry_counts):
        raise GridCoverageAssessmentError(
            "Department coverage summary geometry count exceeds source count"
        )
    geometry_types = summary.geometry_types
    if (
        type(geometry_types) is not tuple
        or geometry_types != tuple(sorted(set(geometry_types)))
        or not set(geometry_types) <= {"Polygon", "MultiPolygon"}
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary geometry types are invalid"
        )
    selected_geometry = frame.geometry
    selected_counts = (
        int(selected_geometry.isna().sum()),
        int((~selected_geometry.isna() & selected_geometry.is_empty).sum()),
        int(
            (
                ~selected_geometry.isna()
                & ~selected_geometry.is_empty
                & ~selected_geometry.is_valid
            ).sum()
        ),
    )
    selected_types = tuple(
        sorted(str(value) for value in selected_geometry.geom_type.dropna().unique())
    )
    if source_count == summary.selected_feature_count and (
        geometry_counts != selected_counts or geometry_types != selected_types
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary geometry facts do not match frame"
        )
    if any(
        observed > reported
        for observed, reported in zip(selected_counts, geometry_counts, strict=True)
    ) or not set(selected_types) <= set(geometry_types):
        raise GridCoverageAssessmentError(
            "Department coverage selected geometry contradicts source summary"
        )
    department_field = summary.department_code_field
    if (
        not isinstance(department_field, str)
        or not department_field
        or department_field != department_field.strip()
        or department_field not in summary.columns
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary department field is invalid"
        )
    if summary.selected_department_code != source.source_department_code:
        raise GridCoverageAssessmentError(
            "Department coverage summary selected department code is inconsistent"
        )
    if not frame[department_field].eq(source.source_department_code).all():
        raise GridCoverageAssessmentError(
            "Department coverage selected department field is inconsistent"
        )
    if summary.spatial_role != source.spatial_role:
        raise GridCoverageAssessmentError(
            "Department coverage summary spatial role is inconsistent"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_coverage`

**Purpose:** Implements `validate source coverage` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _validate_source_coverage(
    source: IgnBdTopoDepartmentCoverage,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `GridCoverageAssessmentError("Department coverage source type is invalid")` under lexical guard `type(source) is not IgnBdTopoDepartmentCoverage`.
  - `GridCoverageAssessmentError(<br>            "Department coverage spatial_role must be SOURCE_COVERAGE_BOUNDARY"<br>        )` under lexical guard `source.spatial_role != COVERAGE_SPATIAL_ROLE`.
  - `GridCoverageAssessmentError(<br>                f"Department coverage {label} must be a non-empty exact string"<br>            )` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.
  - `GridCoverageAssessmentError(<br>            "Department coverage provider is not an IGN identity"<br>        )` under lexical guard `provider not in _IGN_PROVIDER_IDENTITIES`.
  - `GridCoverageAssessmentError("Department coverage product is not BD TOPO")` under lexical guard `product != "bdtopo"`.
  - `GridCoverageAssessmentError(<br>            "Department coverage archive SHA256 is invalid"<br>        )` under lexical guard `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None`.
  - `GridCoverageAssessmentError("Department coverage must be a GeoDataFrame")` under lexical guard `not isinstance(frame, gpd.GeoDataFrame)`.
  - `GridCoverageAssessmentError(<br>            "Department coverage geometry column must exist and be active"<br>        )` under lexical guard `"geometry" not in frame.columns or frame.active_geometry_name != "geometry"`.
  - `GridCoverageAssessmentError(<br>            "Department coverage must contain exactly one selected feature"<br>        )` under lexical guard `len(frame) != 1`.
  - `GridCoverageAssessmentError(<br>            "Department coverage geometry must not be null"<br>        )` under lexical guard `geometry.isna().any()`.
  - `GridCoverageAssessmentError(<br>            "Department coverage geometry must not be empty"<br>        )` under lexical guard `geometry.is_empty.any()`.
  - `GridCoverageAssessmentError("Department coverage geometry must be valid")` under lexical guard `not geometry.is_valid.all()`.
  - `GridCoverageAssessmentError(<br>            "Department coverage geometry must be Polygon or MultiPolygon"<br>        )` under lexical guard `not set(geometry.geom_type.dropna()) <= {"Polygon", "MultiPolygon"}`.
  - `GridCoverageAssessmentError(<br>            "Department coverage lineage columns are missing: "<br>            + ", ".join(sorted(missing))<br>        )` under lexical guard `missing`.
  - `GridCoverageAssessmentError(<br>                f"Department coverage lineage is inconsistent: {column}"<br>            )` under lexical guard `not both_null and actual != expected`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_validate_source_coverage`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_validate_source_coverage`
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_source_coverage`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_source_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_normalized_identity` | `landscout.stages.assess_grid_coverage._normalized_identity` |
| `_SHA256_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_lambert93` | `landscout.stages.assess_grid_coverage._validated_lambert93` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_valid.all` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_coverage_summary` | `landscout.stages.assess_grid_coverage._validate_coverage_summary` |
| `", ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_lineage.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |

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
    source: IgnBdTopoDepartmentCoverage,
) -> gpd.GeoDataFrame:
    if type(source) is not IgnBdTopoDepartmentCoverage:
        raise GridCoverageAssessmentError("Department coverage source type is invalid")
    if source.spatial_role != COVERAGE_SPATIAL_ROLE:
        raise GridCoverageAssessmentError(
            "Department coverage spatial_role must be SOURCE_COVERAGE_BOUNDARY"
        )
    for label, value in (
        ("source_provider", source.source_provider),
        ("source_product", source.source_product),
        ("source_department_code", source.source_department_code),
        ("source_edition", source.source_edition),
        ("source_archive_sha256", source.source_archive_sha256),
        ("source_layer", source.source_layer),
    ):
        if not isinstance(value, str) or not value or value != value.strip():
            raise GridCoverageAssessmentError(
                f"Department coverage {label} must be a non-empty exact string"
            )
    provider = _normalized_identity(source.source_provider, "source_provider")
    product = _normalized_identity(source.source_product, "source_product")
    if provider not in _IGN_PROVIDER_IDENTITIES:
        raise GridCoverageAssessmentError(
            "Department coverage provider is not an IGN identity"
        )
    if product != "bdtopo":
        raise GridCoverageAssessmentError("Department coverage product is not BD TOPO")
    if _SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None:
        raise GridCoverageAssessmentError(
            "Department coverage archive SHA256 is invalid"
        )
    frame = source.coverage
    if not isinstance(frame, gpd.GeoDataFrame):
        raise GridCoverageAssessmentError("Department coverage must be a GeoDataFrame")
    if "geometry" not in frame.columns or frame.active_geometry_name != "geometry":
        raise GridCoverageAssessmentError(
            "Department coverage geometry column must exist and be active"
        )
    _validated_lambert93(frame.crs, "Department coverage")
    if len(frame) != 1:
        raise GridCoverageAssessmentError(
            "Department coverage must contain exactly one selected feature"
        )
    geometry = frame.geometry
    if geometry.isna().any():
        raise GridCoverageAssessmentError(
            "Department coverage geometry must not be null"
        )
    if geometry.is_empty.any():
        raise GridCoverageAssessmentError(
            "Department coverage geometry must not be empty"
        )
    if not geometry.is_valid.all():
        raise GridCoverageAssessmentError("Department coverage geometry must be valid")
    if not set(geometry.geom_type.dropna()) <= {"Polygon", "MultiPolygon"}:
        raise GridCoverageAssessmentError(
            "Department coverage geometry must be Polygon or MultiPolygon"
        )
    _validate_coverage_summary(source, frame)
    expected_lineage: dict[str, object] = {
        "source_provider": source.source_provider,
        "source_product": source.source_product,
        "source_department_code": source.source_department_code,
        "source_edition": source.source_edition,
        "source_product_version": source.source_product_version,
        "source_archive_sha256": source.source_archive_sha256,
        "source_layer": source.source_layer,
        "spatial_role": source.spatial_role,
    }
    missing = set(expected_lineage) - set(frame.columns)
    if missing:
        raise GridCoverageAssessmentError(
            "Department coverage lineage columns are missing: "
            + ", ".join(sorted(missing))
        )
    for column, expected in expected_lineage.items():
        actual = frame.iloc[0][column]
        both_null = pd.isna(actual) and expected is None
        if not both_null and actual != expected:
            raise GridCoverageAssessmentError(
                f"Department coverage lineage is inconsistent: {column}"
            )
    return frame
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_configured_coverage_identity`

**Purpose:** Implements `validate configured coverage identity` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _validate_configured_coverage_identity(
    source: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridCoverageAssessmentError(<br>            "Department coverage does not use the configured physical layer"<br>        )` under lexical guard `source.source_layer != expected_layer`.
  - `GridCoverageAssessmentError(<br>            "Department coverage does not use the configured department field"<br>        )` under lexical guard `source.summary.department_code_field != expected_field`.
  - `GridCoverageAssessmentError(<br>            "Department coverage archive differs from the configured department"<br>        )` under lexical guard `archive.department_code != config.department_code`.
  - `GridCoverageAssessmentError(<br>            "Department coverage archive provider differs from config"<br>        )` under lexical guard `archive_provider not in _IGN_PROVIDER_IDENTITIES<br>        or config_provider not in _IGN_PROVIDER_IDENTITIES`.
  - `GridCoverageAssessmentError(<br>            "Department coverage archive product differs from config"<br>        )` under lexical guard `_normalized_identity(archive.product, "archive product") != "bdtopo"<br>        or _normalized_identity(config.product, "config product") != "bdtopo"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_configured_coverage_identity`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_configured_coverage_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_discover_department_coverage_layer` | `landscout.sources.ign_bdtopo_fr._discover_department_coverage_layer` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `_normalized_identity` | `landscout.stages.assess_grid_coverage._normalized_identity` |

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
def _validate_configured_coverage_identity(
    source: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> None:
    archive = source.extraction.archive
    expected_layer = _discover_department_coverage_layer(
        source.extraction.all_layer_names,
        config,
    )
    if source.source_layer != expected_layer:
        raise GridCoverageAssessmentError(
            "Department coverage does not use the configured physical layer"
        )
    expected_field = config.coverage.department_layer.department_code_field
    if source.summary.department_code_field != expected_field:
        raise GridCoverageAssessmentError(
            "Department coverage does not use the configured department field"
        )
    if archive.department_code != config.department_code:
        raise GridCoverageAssessmentError(
            "Department coverage archive differs from the configured department"
        )
    archive_provider = _normalized_identity(archive.provider, "archive provider")
    config_provider = _normalized_identity(config.provider, "config provider")
    if (
        archive_provider not in _IGN_PROVIDER_IDENTITIES
        or config_provider not in _IGN_PROVIDER_IDENTITIES
    ):
        raise GridCoverageAssessmentError(
            "Department coverage archive provider differs from config"
        )
    if (
        _normalized_identity(archive.product, "archive product") != "bdtopo"
        or _normalized_identity(config.product, "config product") != "bdtopo"
    ):
        raise GridCoverageAssessmentError(
            "Department coverage archive product differs from config"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_coverage_lineage_values`

**Purpose:** Implements `coverage lineage values` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _coverage_lineage_values(
    source: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "grid_source_coverage_provider": source.source_provider,<br>        "grid_source_coverage_product": source.source_product,<br>        "grid_source_coverage_department_code": source.source_department_code,<br>        "grid_source_coverage_edition": source.source_edition,<br>        "grid_source_coverage_product_version": source.source_product_version,<br>        "grid_source_coverage_archive_sha256": source.source_archive_sha256,<br>        "grid_source_coverage_layer": source.source_layer,<br>        "grid_source_coverage_spatial_role": source.spatial_role,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_coverage_lineage_values`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_coverage_lineage_values`
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_coverage_lineage_values`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_coverage_lineage_values`

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
def _coverage_lineage_values(
    source: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
    return {
        "grid_source_coverage_provider": source.source_provider,
        "grid_source_coverage_product": source.source_product,
        "grid_source_coverage_department_code": source.source_department_code,
        "grid_source_coverage_edition": source.source_edition,
        "grid_source_coverage_product_version": source.source_product_version,
        "grid_source_coverage_archive_sha256": source.source_archive_sha256,
        "grid_source_coverage_layer": source.source_layer,
        "grid_source_coverage_spatial_role": source.spatial_role,
    }
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_proximity_source_identity`

**Purpose:** Implements `validate proximity source identity` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _validate_proximity_source_identity(
    proximity: GridProximityResult,
    source: IgnBdTopoDepartmentCoverage,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `proximity` | positional-or-keyword | `GridProximityResult` | `required` |
| `source` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridCoverageAssessmentError(<br>                f"Proximity lineage does not match department coverage: {column}"<br>            )` under lexical guard `not values.eq(expected).all()`.
  - `GridCoverageAssessmentError(<br>                f"Voltage proximity lineage does not match coverage: {column}"<br>            )` under lexical guard `not proximity.voltage_level_proximity[column].eq(expected).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_proximity_source_identity`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_proximity_source_identity`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `proximity.parcels[column].dropna` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.eq(expected).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `proximity.voltage_level_proximity[column].eq(expected).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `proximity.voltage_level_proximity[column].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_proximity_source_identity(
    proximity: GridProximityResult,
    source: IgnBdTopoDepartmentCoverage,
) -> None:
    parcel_mappings = (
        (
            "nearest_line_source_department_code",
            source.source_department_code,
        ),
        ("nearest_line_source_edition", source.source_edition),
        ("nearest_line_source_archive_sha256", source.source_archive_sha256),
        (
            "nearest_exact_line_source_department_code",
            source.source_department_code,
        ),
        ("nearest_exact_line_source_edition", source.source_edition),
        (
            "nearest_exact_line_source_archive_sha256",
            source.source_archive_sha256,
        ),
        (
            "nearest_post_source_department_code",
            source.source_department_code,
        ),
        ("nearest_post_source_edition", source.source_edition),
        ("nearest_post_source_archive_sha256", source.source_archive_sha256),
    )
    for column, expected in parcel_mappings:
        values = proximity.parcels[column].dropna()
        if not values.eq(expected).all():
            raise GridCoverageAssessmentError(
                f"Proximity lineage does not match department coverage: {column}"
            )
    table_mappings = (
        ("source_department_code", source.source_department_code),
        ("source_edition", source.source_edition),
        ("source_archive_sha256", source.source_archive_sha256),
    )
    for column, expected in table_mappings:
        if not proximity.voltage_level_proximity[column].eq(expected).all():
            raise GridCoverageAssessmentError(
                f"Voltage proximity lineage does not match coverage: {column}"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_finite_nonnegative`

**Purpose:** Implements `finite nonnegative` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

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
  - `GridCoverageAssessmentError(f"{label} must be numeric")` under lexical guard `not isinstance(value, Real) or isinstance(value, bool)`.
  - `GridCoverageAssessmentError(f"{label} must be finite")`.
  - `GridCoverageAssessmentError(<br>                f"{label} must be finite and non-negative"<br>            )` under lexical guard `not isfinite(numeric) or numeric < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_finite_nonnegative`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_finite_nonnegative`
- direct call: `landscout.stages.assess_grid_coverage::_boundary_profile` via `_finite_nonnegative`
- value/type reference: `landscout.stages.assess_grid_coverage::_boundary_profile` via `_finite_nonnegative`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
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
        if not isinstance(value, Real) or isinstance(value, bool):
            raise GridCoverageAssessmentError(f"{label} must be numeric")
        try:
            numeric = float(value)
        except (OverflowError, TypeError, ValueError) as error:
            raise GridCoverageAssessmentError(f"{label} must be finite") from error
        if not isfinite(numeric) or numeric < 0:
            raise GridCoverageAssessmentError(
                f"{label} must be finite and non-negative"
            )
        converted.append(numeric)
    return np.asarray(converted, dtype="float64")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_coverage_statuses`

**Purpose:** Implements `coverage statuses` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    fully_covered: np.ndarray,
) -> pd.Series:
```

- Exact decorators: none.
- Declared return annotation: `pd.Series`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `distances` | positional-or-keyword | `pd.Series` | `required` |
| `boundary_distances` | positional-or-keyword | `np.ndarray` | `required` |
| `fully_covered` | positional-or-keyword | `np.ndarray` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.Series(statuses, index=distances.index, dtype="object")`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_coverage_statuses`
- value/type reference: `landscout.stages.assess_grid_coverage::_validate_assessment_result` via `_coverage_statuses`
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_coverage_statuses`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_coverage_statuses`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `distances.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isnan` | `numpy.isnan` |
| `np.full` | `numpy.full` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |

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
    fully_covered: np.ndarray,
) -> pd.Series:
    numeric = distances.to_numpy(dtype="float64", na_value=np.nan)
    matched = ~np.isnan(numeric)
    statuses = np.full(len(distances), "NO_MATCH", dtype=object)
    outside = matched & ~fully_covered
    statuses[outside] = "OUTSIDE_OR_CROSSING_COVERAGE"
    internal = matched & fully_covered
    statuses[internal & (numeric < boundary_distances)] = "NOT_BOUNDARY_LIMITED"
    statuses[internal & (numeric >= boundary_distances)] = "BOUNDARY_LIMITED"
    return pd.Series(statuses, index=distances.index, dtype="object")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_preserves_original_frame`

**Purpose:** Implements `preserves original frame` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _preserves_original_frame(
    original: pd.DataFrame,
    output: pd.DataFrame,
    added_columns: set[str],
    label: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `original` | positional-or-keyword | `pd.DataFrame` | `required` |
| `output` | positional-or-keyword | `pd.DataFrame` | `required` |
| `added_columns` | positional-or-keyword | `set[str]` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridCoverageAssessmentError(f"{label} output schema is inconsistent")` under lexical guard `set(output.columns) != set(original_columns) \| added_columns`.
  - `GridCoverageAssessmentError(<br>                f"{label} changed original proximity column: {column}"<br>            )` under lexical guard `not original[column].equals(output[column])`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_preserves_original_frame`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_preserves_original_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `original[column].equals` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _preserves_original_frame(
    original: pd.DataFrame,
    output: pd.DataFrame,
    added_columns: set[str],
    label: str,
) -> None:
    original_columns = tuple(str(column) for column in original.columns)
    if set(output.columns) != set(original_columns) | added_columns:
        raise GridCoverageAssessmentError(f"{label} output schema is inconsistent")
    for column in original_columns:
        if column == "geometry":
            continue
        if not original[column].equals(output[column]):
            raise GridCoverageAssessmentError(
                f"{label} changed original proximity column: {column}"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_assessment_result`

**Purpose:** Implements `validate assessment result` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _validate_assessment_result(result: GridCoverageAssessmentResult) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `GridCoverageAssessmentResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `GridCoverageAssessmentError("Coverage diagnostic columns are missing")` under lexical guard `parcel_missing or table_missing`.
  - `GridCoverageAssessmentError("Coverage position values are invalid")` under lexical guard `position.isna().any() or not set(position.unique()) <= COVERAGE_POSITIONS`.
  - `GridCoverageAssessmentError(<br>                f"Coverage status is inconsistent: {status_column}"<br>            )` under lexical guard `not actual_status.equals(expected_status)`.
  - `GridCoverageAssessmentError(<br>            "Voltage boundary distances do not match parcel diagnostics"<br>        )` under lexical guard `not table["source_boundary_distance_m"].equals(table_boundary)`.
  - `GridCoverageAssessmentError("Voltage coverage statuses are inconsistent")` under lexical guard `not actual_table_status.equals(expected_table_status)`.
  - `GridCoverageAssessmentError(<br>                    f"Coverage diagnostic lineage is inconsistent: {column}"<br>                )` under lexical guard `not valid`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_assessment_result`
- value/type reference: `landscout.stages.assess_grid_coverage::_assess_grid_coverage_from_proximity` via `_validate_assessment_result`
- direct call: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `_validate_assessment_result`
- value/type reference: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `_validate_assessment_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `profile_grid_proximity` | `landscout.stages.enrich_grid_proximity.profile_grid_proximity` |
| `GridProximityResult` | `landscout.stages.enrich_grid_proximity.GridProximityResult` |
| `_validate_source_coverage` | `landscout.stages.assess_grid_coverage._validate_source_coverage` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `_finite_nonnegative` | `landscout.stages.assess_grid_coverage._finite_nonnegative` |
| `position.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `position.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `position.unique` | `unresolved local/third-party receiver; no ownership inferred` |
| `position.eq("FULLY_COVERED").to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `position.eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coverage_statuses` | `landscout.stages.assess_grid_coverage._coverage_statuses` |
| `parcels[status_column].astype("object").reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[status_column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.astype("object").reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_status.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["parcel_id"].map(boundary_by_id).astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["parcel_id"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["source_boundary_distance_m"].equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["parcel_id"].map(fully_by_id).to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table_boundary.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["coverage_status"].astype("object").reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["coverage_status"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_table_status.astype("object").reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_table_status.astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `actual_table_status.equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coverage_lineage_values` | `landscout.stages.assess_grid_coverage._coverage_lineage_values` |
| `lineage.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.isna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.eq(expected).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.eq` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `table["source_boundary_distance_m"].equals` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_assessment_result(result: GridCoverageAssessmentResult) -> None:
    profile_grid_proximity(
        GridProximityResult(
            parcels=result.parcels,
            voltage_level_proximity=result.voltage_level_proximity,
            voltage_level_coverage=result.voltage_level_coverage,
        )
    )
    _validate_source_coverage(result.source_coverage)
    parcels = result.parcels
    table = result.voltage_level_proximity
    parcel_missing = (
        set(PARCEL_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS)
    ) - set(parcels.columns)
    table_missing = (
        set(VOLTAGE_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS)
    ) - set(table.columns)
    if parcel_missing or table_missing:
        raise GridCoverageAssessmentError("Coverage diagnostic columns are missing")
    boundary_distances = _finite_nonnegative(
        parcels["grid_source_boundary_distance_m"],
        "Grid source boundary distance",
    )
    position = parcels["grid_source_coverage_position"]
    if position.isna().any() or not set(position.unique()) <= COVERAGE_POSITIONS:
        raise GridCoverageAssessmentError("Coverage position values are invalid")
    fully_covered = position.eq("FULLY_COVERED").to_numpy(dtype="bool")
    for distance_column, status_column in (
        ("nearest_line_proxy_distance_m", "nearest_line_coverage_status"),
        (
            "nearest_exact_line_proxy_distance_m",
            "nearest_exact_line_coverage_status",
        ),
        ("nearest_post_proxy_distance_m", "nearest_post_coverage_status"),
    ):
        expected = _coverage_statuses(
            parcels[distance_column], boundary_distances, fully_covered
        )
        actual_status = parcels[status_column].astype("object").reset_index(drop=True)
        expected_status = expected.astype("object").reset_index(drop=True)
        if not actual_status.equals(expected_status):
            raise GridCoverageAssessmentError(
                f"Coverage status is inconsistent: {status_column}"
            )
    boundary_by_id = dict(zip(parcels["parcel_id"], boundary_distances, strict=True))
    fully_by_id = dict(zip(parcels["parcel_id"], fully_covered, strict=True))
    table_boundary = table["parcel_id"].map(boundary_by_id).astype("float64")
    if not table["source_boundary_distance_m"].equals(table_boundary):
        raise GridCoverageAssessmentError(
            "Voltage boundary distances do not match parcel diagnostics"
        )
    table_fully = table["parcel_id"].map(fully_by_id).to_numpy(dtype="bool")
    expected_table_status = _coverage_statuses(
        table["nearest_line_proxy_distance_m"],
        table_boundary.to_numpy(dtype="float64"),
        table_fully,
    )
    actual_table_status = (
        table["coverage_status"].astype("object").reset_index(drop=True)
    )
    expected_table_status = expected_table_status.astype("object").reset_index(
        drop=True
    )
    if not actual_table_status.equals(expected_table_status):
        raise GridCoverageAssessmentError("Voltage coverage statuses are inconsistent")
    lineage = _coverage_lineage_values(result.source_coverage)
    for column, expected in lineage.items():
        for frame in (parcels, table):
            values = frame[column]
            if expected is None:
                valid = values.isna().all()
            else:
                valid = values.eq(expected).all()
            if not valid:
                raise GridCoverageAssessmentError(
                    f"Coverage diagnostic lineage is inconsistent: {column}"
                )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_assess_grid_coverage_from_proximity`

**Purpose:** Classify proximity results against one loaded department boundary.

    All geometry operations use planar XY copies in EPSG:2154. A parcel that
    touches or crosses the source boundary is handled conservatively as not
    fully covered. No parcel, proximity match, or source geometry is mutated.

**Exact signature**

```python
def _assess_grid_coverage_from_proximity(
    proximity_result: GridProximityResult,
    department_coverage: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
```

- Exact decorators: none.
- Declared return annotation: `GridCoverageAssessmentResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `proximity_result` | positional-or-keyword | `GridProximityResult` | `required` |
| `department_coverage` | positional-or-keyword | `IgnBdTopoDepartmentCoverage` | `required` |
| `config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `GridCoverageAssessmentError(<br>            "Calculated coverage boundary distances must be finite and non-negative"<br>        )` under lexical guard `not np.isfinite(measured_boundary).all() or (measured_boundary < 0).any()`.
  - `GridCoverageAssessmentError("Coverage assessment changed parcel geometry")` under lexical guard `not output_parcels.geometry.geom_equals_exact(<br>        source_parcels.geometry, tolerance=0, align=False<br>    ).all()`.
  - `GridCoverageAssessmentError("Parcel CRS is required")` under lexical guard `output_parcels.crs is None or source_parcels.crs is None`.
  - `GridCoverageAssessmentError("Coverage assessment changed parcel CRS")` under lexical guard `not CRS.from_user_input(output_parcels.crs).equals(<br>        CRS.from_user_input(source_parcels.crs)<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `_assess_grid_coverage_from_proximity`
- value/type reference: `landscout.stages.assess_grid_coverage::assess_grid_coverage` via `_assess_grid_coverage_from_proximity`
- import: `tests.unit.test_assess_grid_coverage::<module>` via `from landscout.stages.assess_grid_coverage import (
    _assess_grid_coverage_from_proximity as assess_grid_coverage,
)`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_assessment_reproduces_configured_logical_layer` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_polygonal_coverage_geometry_is_accepted` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_polygonal_coverage_geometry_is_accepted` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_invalid_coverage_geometry_is_rejected` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_invalid_coverage_geometry_is_rejected` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_strict_geometric_boundary_proof` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_strict_geometric_boundary_proof` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_outside_crossing_or_touching_parcel_is_conservative` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_outside_crossing_or_touching_parcel_is_conservative` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_no_exact_match_uses_explicit_no_match_status` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_no_exact_match_uses_explicit_no_match_status` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_proximity_and_coverage_package_lineage_must_match` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_proximity_and_coverage_package_lineage_must_match` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_rejects_arbitrary_source_identity` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_rejects_arbitrary_source_identity` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_count_must_match_frame` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_count_must_match_frame` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_schema_must_match_selected_source_columns` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_schema_must_match_selected_source_columns` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_crs_must_match_frame` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_crs_must_match_frame` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_geometry_facts_are_validated` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_geometry_facts_are_validated` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_department_must_match` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_selected_department_must_match` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_department_field_must_be_exact` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_department_field_must_be_exact` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `assess_grid_coverage`
- direct call: `tests.unit.test_assess_grid_coverage::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `assess_grid_coverage`
- value/type reference: `tests.unit.test_assess_grid_coverage::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `assess_grid_coverage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_reject_parcel_output_collisions` | `landscout.stages.assess_grid_coverage._reject_parcel_output_collisions` |
| `profile_grid_proximity` | `landscout.stages.enrich_grid_proximity.profile_grid_proximity` |
| `_validate_source_coverage` | `landscout.stages.assess_grid_coverage._validate_source_coverage` |
| `_validate_configured_coverage_identity` | `landscout.stages.assess_grid_coverage._validate_configured_coverage_identity` |
| `_validate_proximity_source_identity` | `landscout.stages.assess_grid_coverage._validate_proximity_source_identity` |
| `source_parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.asarray` | `numpy.asarray` |
| `force_2d` | `shapely.force_2d` |
| `boundary` | `shapely.boundary` |
| `covers` | `shapely.covers` |
| `intersects` | `shapely.intersects` |
| `distance` | `shapely.distance` |
| `np.isfinite(measured_boundary).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(measured_boundary < 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `np.where` | `numpy.where` |
| `_coverage_statuses` | `landscout.stages.assess_grid_coverage._coverage_statuses` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `output_table["parcel_id"].map(boundary_by_id).astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `output_table["parcel_id"].map` | `unresolved local/third-party receiver; no ownership inferred` |
| `output_table["parcel_id"].map(covered_by_id).to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `output_table["source_boundary_distance_m"].to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coverage_lineage_values` | `landscout.stages.assess_grid_coverage._coverage_lineage_values` |
| `lineage.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_preserves_original_frame` | `landscout.stages.assess_grid_coverage._preserves_original_frame` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `output_parcels.geometry.geom_equals_exact(<br>        source_parcels.geometry, tolerance=0, align=False<br>    ).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `output_parcels.geometry.geom_equals_exact` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input(output_parcels.crs).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `GridCoverageAssessmentResult` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentResult` |
| `_validate_assessment_result` | `landscout.stages.assess_grid_coverage._validate_assessment_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `source_parcels.to_crs`<br>`distance`<br>`output_table["source_boundary_distance_m"].to_numpy`<br>`output_parcels.geometry.geom_equals_exact(<br>        source_parcels.geometry, tolerance=0, align=False<br>    ).all`<br>`output_parcels.geometry.geom_equals_exact` |
| External process/environment | None directly present. |
| In-memory mutation | `output_parcels["grid_source_boundary_distance_m"] = boundary_distances`<br>`output_parcels["grid_source_coverage_position"] = np.where(<br>        fully_covered,<br>        "FULLY_COVERED",<br>        "OUTSIDE_OR_CROSSING_COVERAGE",<br>    )`<br>`output_parcels["nearest_line_coverage_status"] = _coverage_statuses(<br>        output_parcels["nearest_line_proxy_distance_m"],<br>        boundary_distances,<br>        fully_covered,<br>    )`<br>`output_parcels["nearest_exact_line_coverage_status"] = _coverage_statuses(<br>        output_parcels["nearest_exact_line_proxy_distance_m"],<br>        boundary_distances,<br>        fully_covered,<br>    )`<br>`output_parcels["nearest_post_coverage_status"] = _coverage_statuses(<br>        output_parcels["nearest_post_proxy_distance_m"],<br>        boundary_distances,<br>        fully_covered,<br>    )`<br>`output_table["source_boundary_distance_m"] = (<br>        output_table["parcel_id"].map(boundary_by_id).astype("float64")<br>    )`<br>`output_table["coverage_status"] = _coverage_statuses(<br>        output_table["nearest_line_proxy_distance_m"],<br>        output_table["source_boundary_distance_m"].to_numpy(dtype="float64"),<br>        table_fully_covered,<br>    )`<br>`output_parcels[column] = value`<br>`output_table[column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _assess_grid_coverage_from_proximity(
    proximity_result: GridProximityResult,
    department_coverage: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
    """Classify proximity results against one loaded department boundary.

    All geometry operations use planar XY copies in EPSG:2154. A parcel that
    touches or crosses the source boundary is handled conservatively as not
    fully covered. No parcel, proximity match, or source geometry is mutated.
    """

    _reject_parcel_output_collisions(proximity_result.parcels)
    profile_grid_proximity(proximity_result)
    coverage_frame = _validate_source_coverage(department_coverage)
    _validate_configured_coverage_identity(department_coverage, config)
    _validate_proximity_source_identity(proximity_result, department_coverage)

    source_parcels = proximity_result.parcels
    source_table = proximity_result.voltage_level_proximity
    output_parcels = source_parcels.copy()
    output_table = source_table.copy()

    calculation_parcels = source_parcels.to_crs(CALCULATION_CRS)
    parcel_geometries = np.asarray(
        force_2d(np.asarray(calculation_parcels.geometry.array, dtype=object)),
        dtype=object,
    )
    coverage_geometry = force_2d(coverage_frame.geometry.iloc[0])
    coverage_boundary = boundary(coverage_geometry)
    covered = np.asarray(covers(coverage_geometry, parcel_geometries), dtype="bool")
    touches_boundary = np.asarray(
        intersects(parcel_geometries, coverage_boundary), dtype="bool"
    )
    fully_covered = covered & ~touches_boundary
    measured_boundary = np.asarray(
        distance(parcel_geometries, coverage_boundary), dtype="float64"
    )
    if not np.isfinite(measured_boundary).all() or (measured_boundary < 0).any():
        raise GridCoverageAssessmentError(
            "Calculated coverage boundary distances must be finite and non-negative"
        )
    boundary_distances = np.where(fully_covered, measured_boundary, 0.0)

    output_parcels["grid_source_boundary_distance_m"] = boundary_distances
    output_parcels["grid_source_coverage_position"] = np.where(
        fully_covered,
        "FULLY_COVERED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    )
    output_parcels["nearest_line_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_line_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )
    output_parcels["nearest_exact_line_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_exact_line_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )
    output_parcels["nearest_post_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_post_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )

    boundary_by_id = dict(
        zip(output_parcels["parcel_id"], boundary_distances, strict=True)
    )
    covered_by_id = dict(zip(output_parcels["parcel_id"], fully_covered, strict=True))
    output_table["source_boundary_distance_m"] = (
        output_table["parcel_id"].map(boundary_by_id).astype("float64")
    )
    table_fully_covered = (
        output_table["parcel_id"].map(covered_by_id).to_numpy(dtype="bool")
    )
    output_table["coverage_status"] = _coverage_statuses(
        output_table["nearest_line_proxy_distance_m"],
        output_table["source_boundary_distance_m"].to_numpy(dtype="float64"),
        table_fully_covered,
    )
    lineage = _coverage_lineage_values(department_coverage)
    for column, value in lineage.items():
        output_parcels[column] = value
        output_table[column] = value

    _preserves_original_frame(
        source_parcels,
        output_parcels,
        set(PARCEL_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS),
        "Parcel proximity",
    )
    _preserves_original_frame(
        source_table,
        output_table,
        set(VOLTAGE_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS),
        "Voltage proximity",
    )
    if not output_parcels.geometry.geom_equals_exact(
        source_parcels.geometry, tolerance=0, align=False
    ).all():
        raise GridCoverageAssessmentError("Coverage assessment changed parcel geometry")
    if output_parcels.crs is None or source_parcels.crs is None:
        raise GridCoverageAssessmentError("Parcel CRS is required")
    if not CRS.from_user_input(output_parcels.crs).equals(
        CRS.from_user_input(source_parcels.crs)
    ):
        raise GridCoverageAssessmentError("Coverage assessment changed parcel CRS")

    result = GridCoverageAssessmentResult(
        parcels=output_parcels,
        voltage_level_proximity=output_table,
        voltage_level_coverage=proximity_result.voltage_level_coverage,
        source_coverage=department_coverage,
    )
    _validate_assessment_result(result)
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `assess_grid_coverage`

**Purpose:** Diagnose source-complete grid proximity against configured coverage.

**Exact signature**

```python
def assess_grid_coverage(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
```

- Exact decorators: none.
- Declared return annotation: `GridCoverageAssessmentResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `electricity_source` | positional-or-keyword | `IgnBdTopoElectricityData` | `required` |
| `source_config` | positional-or-keyword | `IgnBdTopoSourceConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_assess_grid_coverage_from_proximity(<br>            proximity,<br>            coverage,<br>            source_config,<br>        )`
- Explicit raise paths:
  - `GridCoverageAssessmentError(<br>                "parcels must be a GeoDataFrame with active geometry"<br>            )` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `GridCoverageAssessmentError(<br>                "electricity source must be an IgnBdTopoElectricityData"<br>            )` under lexical guard `type(electricity_source) is not IgnBdTopoElectricityData`.
  - `GridCoverageAssessmentError(<br>                "source_config must be an IgnBdTopoSourceConfig"<br>            )` under lexical guard `type(source_config) is not IgnBdTopoSourceConfig`.
  - `GridCoverageAssessmentError(<br>                "Department coverage must retain the electricity extraction identity"<br>            )` under lexical guard `coverage.extraction is not electricity_source.extraction`.
  - `re-raise`.
  - `GridCoverageAssessmentError(<br>            "Grid proximity coverage cannot be assessed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `_reject_parcel_output_collisions` | `landscout.stages.assess_grid_coverage._reject_parcel_output_collisions` |
| `enrich_parcel_grid_proximity` | `landscout.stages.enrich_grid_proximity.enrich_parcel_grid_proximity` |
| `load_ign_bdtopo_department_coverage` | `landscout.sources.ign_bdtopo_fr.load_ign_bdtopo_department_coverage` |
| `_assess_grid_coverage_from_proximity` | `landscout.stages.assess_grid_coverage._assess_grid_coverage_from_proximity` |

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
def assess_grid_coverage(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
    """Diagnose source-complete grid proximity against configured coverage."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise GridCoverageAssessmentError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(electricity_source) is not IgnBdTopoElectricityData:
            raise GridCoverageAssessmentError(
                "electricity source must be an IgnBdTopoElectricityData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise GridCoverageAssessmentError(
                "source_config must be an IgnBdTopoSourceConfig"
            )
        _reject_parcel_output_collisions(parcels)
        proximity = enrich_parcel_grid_proximity(
            parcels,
            electricity_source,
            source_config,
        )
        coverage = load_ign_bdtopo_department_coverage(
            electricity_source.extraction,
            source_config,
        )
        if coverage.extraction is not electricity_source.extraction:
            raise GridCoverageAssessmentError(
                "Department coverage must retain the electricity extraction identity"
            )
        return _assess_grid_coverage_from_proximity(
            proximity,
            coverage,
            source_config,
        )
    except GridCoverageAssessmentError:
        raise
    except Exception as error:
        raise GridCoverageAssessmentError(
            "Grid proximity coverage cannot be assessed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_status_counts`

**Purpose:** Implements `status counts` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _status_counts(values: pd.Series) -> CoverageStatusCounts:
```

- Exact decorators: none.
- Declared return annotation: `CoverageStatusCounts`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `CoverageStatusCounts(<br>        not_boundary_limited=int(counts.get("NOT_BOUNDARY_LIMITED", 0)),<br>        boundary_limited=int(counts.get("BOUNDARY_LIMITED", 0)),<br>        outside_or_crossing_coverage=int(counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)),<br>        no_match=int(counts.get("NO_MATCH", 0)),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `_status_counts`
- value/type reference: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `_status_counts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `values.value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `CoverageStatusCounts` | `landscout.stages.assess_grid_coverage.CoverageStatusCounts` |
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
def _status_counts(values: pd.Series) -> CoverageStatusCounts:
    counts = values.value_counts()
    return CoverageStatusCounts(
        not_boundary_limited=int(counts.get("NOT_BOUNDARY_LIMITED", 0)),
        boundary_limited=int(counts.get("BOUNDARY_LIMITED", 0)),
        outside_or_crossing_coverage=int(counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)),
        no_match=int(counts.get("NO_MATCH", 0)),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_boundary_profile`

**Purpose:** Implements `boundary profile` within the file role: Diagnoses grid proxy distances against the configured IGN source-package boundary.

**Exact signature**

```python
def _boundary_profile(values: pd.Series) -> BoundaryDistanceProfile:
```

- Exact decorators: none.
- Declared return annotation: `BoundaryDistanceProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `pd.Series` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BoundaryDistanceProfile(<br>        count=len(series),<br>        minimum=float(series.min()),<br>        p01=float(series.quantile(0.01)),<br>        p05=float(series.quantile(0.05)),<br>        p10=float(series.quantile(0.10)),<br>        p25=float(series.quantile(0.25)),<br>        p50=float(series.quantile(0.50)),<br>        p75=float(series.quantile(0.75)),<br>        p90=float(series.quantile(0.90)),<br>        p95=float(series.quantile(0.95)),<br>        p99=float(series.quantile(0.99)),<br>        maximum=float(series.max()),<br>    )`
- Explicit raise paths:
  - `GridCoverageAssessmentError(<br>            "Cannot profile an empty parcel coverage assessment"<br>        )` under lexical guard `len(numeric) == 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `_boundary_profile`
- value/type reference: `landscout.stages.assess_grid_coverage::profile_grid_coverage` via `_boundary_profile`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_finite_nonnegative` | `landscout.stages.assess_grid_coverage._finite_nonnegative` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `GridCoverageAssessmentError` | `landscout.stages.assess_grid_coverage.GridCoverageAssessmentError` |
| `pd.Series` | `pandas.Series` |
| `BoundaryDistanceProfile` | `landscout.stages.assess_grid_coverage.BoundaryDistanceProfile` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.min` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.quantile` | `unresolved local/third-party receiver; no ownership inferred` |
| `series.max` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `BoundaryDistanceProfile` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _boundary_profile(values: pd.Series) -> BoundaryDistanceProfile:
    numeric = _finite_nonnegative(values, "Grid source boundary distance")
    if len(numeric) == 0:
        raise GridCoverageAssessmentError(
            "Cannot profile an empty parcel coverage assessment"
        )
    series = pd.Series(numeric, dtype="float64")
    return BoundaryDistanceProfile(
        count=len(series),
        minimum=float(series.min()),
        p01=float(series.quantile(0.01)),
        p05=float(series.quantile(0.05)),
        p10=float(series.quantile(0.10)),
        p25=float(series.quantile(0.25)),
        p50=float(series.quantile(0.50)),
        p75=float(series.quantile(0.75)),
        p90=float(series.quantile(0.90)),
        p95=float(series.quantile(0.95)),
        p99=float(series.quantile(0.99)),
        maximum=float(series.max()),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `profile_grid_coverage`

**Purpose:** Summarize boundary diagnostics without suitability thresholds.

**Exact signature**

```python
def profile_grid_coverage(
    result: GridCoverageAssessmentResult,
) -> GridCoverageProfile:
```

- Exact decorators: none.
- Declared return annotation: `GridCoverageProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `GridCoverageAssessmentResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GridCoverageProfile(<br>        parcel_count=len(parcels),<br>        fully_covered_count=int(position_counts.get("FULLY_COVERED", 0)),<br>        outside_or_crossing_count=int(<br>            position_counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)<br>        ),<br>        boundary_distance=_boundary_profile(parcels["grid_source_boundary_distance_m"]),<br>        nearest_line=_status_counts(parcels["nearest_line_coverage_status"]),<br>        nearest_exact_line=_status_counts(<br>            parcels["nearest_exact_line_coverage_status"]<br>        ),<br>        nearest_post=_status_counts(parcels["nearest_post_coverage_status"]),<br>        voltage_levels=tuple(voltage_profiles),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_assessment_result` | `landscout.stages.assess_grid_coverage._validate_assessment_result` |
| `parcels["grid_source_coverage_position"].value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `voltage_profiles.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `VoltageCoverageStatusProfile` | `landscout.stages.assess_grid_coverage.VoltageCoverageStatusProfile` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_status_counts` | `landscout.stages.assess_grid_coverage._status_counts` |
| `GridCoverageProfile` | `landscout.stages.assess_grid_coverage.GridCoverageProfile` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `position_counts.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_boundary_profile` | `landscout.stages.assess_grid_coverage._boundary_profile` |
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
| In-memory mutation | `voltage_profiles.append(<br>            VoltageCoverageStatusProfile(<br>                voltage_kv=float(item.voltage_kv),<br>                parcel_count=len(rows),<br>                statuses=_status_counts(rows["coverage_status"]),<br>            )<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def profile_grid_coverage(
    result: GridCoverageAssessmentResult,
) -> GridCoverageProfile:
    """Summarize boundary diagnostics without suitability thresholds."""

    _validate_assessment_result(result)
    parcels = result.parcels
    position_counts = parcels["grid_source_coverage_position"].value_counts()
    voltage_profiles: list[VoltageCoverageStatusProfile] = []
    for item in result.voltage_level_coverage:
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == item.voltage_kv
        ]
        voltage_profiles.append(
            VoltageCoverageStatusProfile(
                voltage_kv=float(item.voltage_kv),
                parcel_count=len(rows),
                statuses=_status_counts(rows["coverage_status"]),
            )
        )
    return GridCoverageProfile(
        parcel_count=len(parcels),
        fully_covered_count=int(position_counts.get("FULLY_COVERED", 0)),
        outside_or_crossing_count=int(
            position_counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)
        ),
        boundary_distance=_boundary_profile(parcels["grid_source_boundary_distance_m"]),
        nearest_line=_status_counts(parcels["nearest_line_coverage_status"]),
        nearest_exact_line=_status_counts(
            parcels["nearest_exact_line_coverage_status"]
        ),
        nearest_post=_status_counts(parcels["nearest_post_coverage_status"]),
        voltage_levels=tuple(voltage_profiles),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `PARCEL_DIAGNOSTIC_COLUMNS`, `VOLTAGE_DIAGNOSTIC_COLUMNS`, `COVERAGE_LINEAGE_COLUMNS`, `_SOURCE_LINEAGE_COLUMNS`, `_PARCEL_GENERATED_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Diagnose IGN grid-proxy results against loaded package coverage boundaries."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from math import isfinite
from numbers import Real
from typing import Literal

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
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
    _discover_department_coverage_layer,
    load_ign_bdtopo_department_coverage,
)
from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)

CALCULATION_CRS = "EPSG:2154"
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"

CoverageStatus = Literal[
    "NOT_BOUNDARY_LIMITED",
    "BOUNDARY_LIMITED",
    "OUTSIDE_OR_CROSSING_COVERAGE",
    "NO_MATCH",
]
CoveragePosition = Literal["FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"]

COVERAGE_STATUSES = frozenset(
    {
        "NOT_BOUNDARY_LIMITED",
        "BOUNDARY_LIMITED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
        "NO_MATCH",
    }
)
COVERAGE_POSITIONS = frozenset({"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"})
PARCEL_DIAGNOSTIC_COLUMNS = (
    "grid_source_boundary_distance_m",
    "grid_source_coverage_position",
    "nearest_line_coverage_status",
    "nearest_exact_line_coverage_status",
    "nearest_post_coverage_status",
)
VOLTAGE_DIAGNOSTIC_COLUMNS = (
    "source_boundary_distance_m",
    "coverage_status",
)
COVERAGE_LINEAGE_COLUMNS = (
    "grid_source_coverage_provider",
    "grid_source_coverage_product",
    "grid_source_coverage_department_code",
    "grid_source_coverage_edition",
    "grid_source_coverage_product_version",
    "grid_source_coverage_archive_sha256",
    "grid_source_coverage_layer",
    "grid_source_coverage_spatial_role",
)
_SOURCE_LINEAGE_COLUMNS = (
    "source_provider",
    "source_product",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_archive_sha256",
    "source_layer",
    "spatial_role",
)
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institutnationaldelinformationgeographiqueetforestiereign",
    }
)
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
_PARCEL_GENERATED_COLUMNS = frozenset(
    {*PARCEL_DIAGNOSTIC_COLUMNS, *COVERAGE_LINEAGE_COLUMNS}
)


class GridCoverageAssessmentError(ValueError):
    """Raised when coverage diagnostics cannot be calculated safely."""


def _reject_parcel_output_collisions(parcels: gpd.GeoDataFrame) -> None:
    collisions = _PARCEL_GENERATED_COLUMNS & set(parcels.columns)
    if collisions:
        raise GridCoverageAssessmentError(
            "Parcel input collides with generated grid-coverage columns: "
            + ", ".join(sorted(collisions))
        )


@dataclass(frozen=True)
class GridCoverageAssessmentResult:
    """Coverage-annotated copies of both grid-proximity representations."""

    parcels: gpd.GeoDataFrame
    voltage_level_proximity: pd.DataFrame
    voltage_level_coverage: tuple[VoltageLevelCoverage, ...]
    source_coverage: IgnBdTopoDepartmentCoverage


@dataclass(frozen=True)
class BoundaryDistanceProfile:
    count: int
    minimum: float
    p01: float
    p05: float
    p10: float
    p25: float
    p50: float
    p75: float
    p90: float
    p95: float
    p99: float
    maximum: float


@dataclass(frozen=True)
class CoverageStatusCounts:
    not_boundary_limited: int
    boundary_limited: int
    outside_or_crossing_coverage: int
    no_match: int


@dataclass(frozen=True)
class VoltageCoverageStatusProfile:
    voltage_kv: float
    parcel_count: int
    statuses: CoverageStatusCounts


@dataclass(frozen=True)
class GridCoverageProfile:
    parcel_count: int
    fully_covered_count: int
    outside_or_crossing_count: int
    boundary_distance: BoundaryDistanceProfile
    nearest_line: CoverageStatusCounts
    nearest_exact_line: CoverageStatusCounts
    nearest_post: CoverageStatusCounts
    voltage_levels: tuple[VoltageCoverageStatusProfile, ...]


def _validated_lambert93(value: object, label: str) -> CRS:
    if value is None:
        raise GridCoverageAssessmentError(f"{label} CRS is required")
    try:
        crs = CRS.from_user_input(value)
    except Exception as error:
        raise GridCoverageAssessmentError(f"{label} CRS is unreadable") from error
    expected = CRS.from_epsg(2154)
    if not crs.is_projected or not crs.equals(expected):
        raise GridCoverageAssessmentError(f"{label} must use EPSG:2154")
    return crs


def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise GridCoverageAssessmentError(
            f"Department coverage {label} must be a non-empty exact string"
        )
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(
        character for character in decomposed.casefold() if character.isalnum()
    )


def _strict_nonnegative_integer(value: object, label: str) -> int:
    if type(value) is not int or value < 0:
        raise GridCoverageAssessmentError(
            f"Department coverage summary {label} must be a non-negative integer"
        )
    return value


def _validate_coverage_summary(
    source: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
) -> None:
    summary = source.summary
    if type(summary) is not IgnBdTopoCoverageLayerSummary:
        raise GridCoverageAssessmentError("Department coverage summary type is invalid")
    if summary.source_layer_name != source.source_layer:
        raise GridCoverageAssessmentError(
            "Department coverage summary layer does not match source lineage"
        )
    summary_crs = _validated_lambert93(summary.crs, "Department coverage summary")
    frame_crs = _validated_lambert93(frame.crs, "Department coverage")
    if not summary_crs.equals(frame_crs):
        raise GridCoverageAssessmentError(
            "Department coverage summary CRS does not match the selected frame"
        )
    if type(summary.selected_feature_count) is not int or (
        summary.selected_feature_count != len(frame)
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary selected feature count does not match frame"
        )
    source_count = _strict_nonnegative_integer(
        summary.source_feature_count,
        "source_feature_count",
    )
    if source_count < summary.selected_feature_count:
        raise GridCoverageAssessmentError(
            "Department coverage summary source count is smaller than selected count"
        )
    if (
        type(summary.columns) is not tuple
        or not summary.columns
        or any(
            not isinstance(column, str) or not column or column != column.strip()
            for column in summary.columns
        )
        or len(set(summary.columns)) != len(summary.columns)
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary columns are invalid"
        )
    expected_frame_columns = (*summary.columns, *_SOURCE_LINEAGE_COLUMNS)
    if tuple(str(column) for column in frame.columns) != expected_frame_columns:
        raise GridCoverageAssessmentError(
            "Department coverage summary ordered columns do not match frame"
        )
    observed_dtypes = tuple(
        (column, str(frame[column].dtype)) for column in summary.columns
    )
    if type(summary.dtypes) is not tuple or summary.dtypes != observed_dtypes:
        raise GridCoverageAssessmentError(
            "Department coverage summary ordered dtypes do not match frame"
        )
    geometry_counts = (
        _strict_nonnegative_integer(
            summary.null_geometry_count,
            "null_geometry_count",
        ),
        _strict_nonnegative_integer(
            summary.empty_geometry_count,
            "empty_geometry_count",
        ),
        _strict_nonnegative_integer(
            summary.invalid_geometry_count,
            "invalid_geometry_count",
        ),
    )
    if any(count > source_count for count in geometry_counts):
        raise GridCoverageAssessmentError(
            "Department coverage summary geometry count exceeds source count"
        )
    geometry_types = summary.geometry_types
    if (
        type(geometry_types) is not tuple
        or geometry_types != tuple(sorted(set(geometry_types)))
        or not set(geometry_types) <= {"Polygon", "MultiPolygon"}
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary geometry types are invalid"
        )
    selected_geometry = frame.geometry
    selected_counts = (
        int(selected_geometry.isna().sum()),
        int((~selected_geometry.isna() & selected_geometry.is_empty).sum()),
        int(
            (
                ~selected_geometry.isna()
                & ~selected_geometry.is_empty
                & ~selected_geometry.is_valid
            ).sum()
        ),
    )
    selected_types = tuple(
        sorted(str(value) for value in selected_geometry.geom_type.dropna().unique())
    )
    if source_count == summary.selected_feature_count and (
        geometry_counts != selected_counts or geometry_types != selected_types
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary geometry facts do not match frame"
        )
    if any(
        observed > reported
        for observed, reported in zip(selected_counts, geometry_counts, strict=True)
    ) or not set(selected_types) <= set(geometry_types):
        raise GridCoverageAssessmentError(
            "Department coverage selected geometry contradicts source summary"
        )
    department_field = summary.department_code_field
    if (
        not isinstance(department_field, str)
        or not department_field
        or department_field != department_field.strip()
        or department_field not in summary.columns
    ):
        raise GridCoverageAssessmentError(
            "Department coverage summary department field is invalid"
        )
    if summary.selected_department_code != source.source_department_code:
        raise GridCoverageAssessmentError(
            "Department coverage summary selected department code is inconsistent"
        )
    if not frame[department_field].eq(source.source_department_code).all():
        raise GridCoverageAssessmentError(
            "Department coverage selected department field is inconsistent"
        )
    if summary.spatial_role != source.spatial_role:
        raise GridCoverageAssessmentError(
            "Department coverage summary spatial role is inconsistent"
        )


def _validate_source_coverage(
    source: IgnBdTopoDepartmentCoverage,
) -> gpd.GeoDataFrame:
    if type(source) is not IgnBdTopoDepartmentCoverage:
        raise GridCoverageAssessmentError("Department coverage source type is invalid")
    if source.spatial_role != COVERAGE_SPATIAL_ROLE:
        raise GridCoverageAssessmentError(
            "Department coverage spatial_role must be SOURCE_COVERAGE_BOUNDARY"
        )
    for label, value in (
        ("source_provider", source.source_provider),
        ("source_product", source.source_product),
        ("source_department_code", source.source_department_code),
        ("source_edition", source.source_edition),
        ("source_archive_sha256", source.source_archive_sha256),
        ("source_layer", source.source_layer),
    ):
        if not isinstance(value, str) or not value or value != value.strip():
            raise GridCoverageAssessmentError(
                f"Department coverage {label} must be a non-empty exact string"
            )
    provider = _normalized_identity(source.source_provider, "source_provider")
    product = _normalized_identity(source.source_product, "source_product")
    if provider not in _IGN_PROVIDER_IDENTITIES:
        raise GridCoverageAssessmentError(
            "Department coverage provider is not an IGN identity"
        )
    if product != "bdtopo":
        raise GridCoverageAssessmentError("Department coverage product is not BD TOPO")
    if _SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None:
        raise GridCoverageAssessmentError(
            "Department coverage archive SHA256 is invalid"
        )
    frame = source.coverage
    if not isinstance(frame, gpd.GeoDataFrame):
        raise GridCoverageAssessmentError("Department coverage must be a GeoDataFrame")
    if "geometry" not in frame.columns or frame.active_geometry_name != "geometry":
        raise GridCoverageAssessmentError(
            "Department coverage geometry column must exist and be active"
        )
    _validated_lambert93(frame.crs, "Department coverage")
    if len(frame) != 1:
        raise GridCoverageAssessmentError(
            "Department coverage must contain exactly one selected feature"
        )
    geometry = frame.geometry
    if geometry.isna().any():
        raise GridCoverageAssessmentError(
            "Department coverage geometry must not be null"
        )
    if geometry.is_empty.any():
        raise GridCoverageAssessmentError(
            "Department coverage geometry must not be empty"
        )
    if not geometry.is_valid.all():
        raise GridCoverageAssessmentError("Department coverage geometry must be valid")
    if not set(geometry.geom_type.dropna()) <= {"Polygon", "MultiPolygon"}:
        raise GridCoverageAssessmentError(
            "Department coverage geometry must be Polygon or MultiPolygon"
        )
    _validate_coverage_summary(source, frame)
    expected_lineage: dict[str, object] = {
        "source_provider": source.source_provider,
        "source_product": source.source_product,
        "source_department_code": source.source_department_code,
        "source_edition": source.source_edition,
        "source_product_version": source.source_product_version,
        "source_archive_sha256": source.source_archive_sha256,
        "source_layer": source.source_layer,
        "spatial_role": source.spatial_role,
    }
    missing = set(expected_lineage) - set(frame.columns)
    if missing:
        raise GridCoverageAssessmentError(
            "Department coverage lineage columns are missing: "
            + ", ".join(sorted(missing))
        )
    for column, expected in expected_lineage.items():
        actual = frame.iloc[0][column]
        both_null = pd.isna(actual) and expected is None
        if not both_null and actual != expected:
            raise GridCoverageAssessmentError(
                f"Department coverage lineage is inconsistent: {column}"
            )
    return frame


def _validate_configured_coverage_identity(
    source: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> None:
    archive = source.extraction.archive
    expected_layer = _discover_department_coverage_layer(
        source.extraction.all_layer_names,
        config,
    )
    if source.source_layer != expected_layer:
        raise GridCoverageAssessmentError(
            "Department coverage does not use the configured physical layer"
        )
    expected_field = config.coverage.department_layer.department_code_field
    if source.summary.department_code_field != expected_field:
        raise GridCoverageAssessmentError(
            "Department coverage does not use the configured department field"
        )
    if archive.department_code != config.department_code:
        raise GridCoverageAssessmentError(
            "Department coverage archive differs from the configured department"
        )
    archive_provider = _normalized_identity(archive.provider, "archive provider")
    config_provider = _normalized_identity(config.provider, "config provider")
    if (
        archive_provider not in _IGN_PROVIDER_IDENTITIES
        or config_provider not in _IGN_PROVIDER_IDENTITIES
    ):
        raise GridCoverageAssessmentError(
            "Department coverage archive provider differs from config"
        )
    if (
        _normalized_identity(archive.product, "archive product") != "bdtopo"
        or _normalized_identity(config.product, "config product") != "bdtopo"
    ):
        raise GridCoverageAssessmentError(
            "Department coverage archive product differs from config"
        )


def _coverage_lineage_values(
    source: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
    return {
        "grid_source_coverage_provider": source.source_provider,
        "grid_source_coverage_product": source.source_product,
        "grid_source_coverage_department_code": source.source_department_code,
        "grid_source_coverage_edition": source.source_edition,
        "grid_source_coverage_product_version": source.source_product_version,
        "grid_source_coverage_archive_sha256": source.source_archive_sha256,
        "grid_source_coverage_layer": source.source_layer,
        "grid_source_coverage_spatial_role": source.spatial_role,
    }


def _validate_proximity_source_identity(
    proximity: GridProximityResult,
    source: IgnBdTopoDepartmentCoverage,
) -> None:
    parcel_mappings = (
        (
            "nearest_line_source_department_code",
            source.source_department_code,
        ),
        ("nearest_line_source_edition", source.source_edition),
        ("nearest_line_source_archive_sha256", source.source_archive_sha256),
        (
            "nearest_exact_line_source_department_code",
            source.source_department_code,
        ),
        ("nearest_exact_line_source_edition", source.source_edition),
        (
            "nearest_exact_line_source_archive_sha256",
            source.source_archive_sha256,
        ),
        (
            "nearest_post_source_department_code",
            source.source_department_code,
        ),
        ("nearest_post_source_edition", source.source_edition),
        ("nearest_post_source_archive_sha256", source.source_archive_sha256),
    )
    for column, expected in parcel_mappings:
        values = proximity.parcels[column].dropna()
        if not values.eq(expected).all():
            raise GridCoverageAssessmentError(
                f"Proximity lineage does not match department coverage: {column}"
            )
    table_mappings = (
        ("source_department_code", source.source_department_code),
        ("source_edition", source.source_edition),
        ("source_archive_sha256", source.source_archive_sha256),
    )
    for column, expected in table_mappings:
        if not proximity.voltage_level_proximity[column].eq(expected).all():
            raise GridCoverageAssessmentError(
                f"Voltage proximity lineage does not match coverage: {column}"
            )


def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
    converted: list[float] = []
    for value in values.tolist():
        if not isinstance(value, Real) or isinstance(value, bool):
            raise GridCoverageAssessmentError(f"{label} must be numeric")
        try:
            numeric = float(value)
        except (OverflowError, TypeError, ValueError) as error:
            raise GridCoverageAssessmentError(f"{label} must be finite") from error
        if not isfinite(numeric) or numeric < 0:
            raise GridCoverageAssessmentError(
                f"{label} must be finite and non-negative"
            )
        converted.append(numeric)
    return np.asarray(converted, dtype="float64")


def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    fully_covered: np.ndarray,
) -> pd.Series:
    numeric = distances.to_numpy(dtype="float64", na_value=np.nan)
    matched = ~np.isnan(numeric)
    statuses = np.full(len(distances), "NO_MATCH", dtype=object)
    outside = matched & ~fully_covered
    statuses[outside] = "OUTSIDE_OR_CROSSING_COVERAGE"
    internal = matched & fully_covered
    statuses[internal & (numeric < boundary_distances)] = "NOT_BOUNDARY_LIMITED"
    statuses[internal & (numeric >= boundary_distances)] = "BOUNDARY_LIMITED"
    return pd.Series(statuses, index=distances.index, dtype="object")


def _preserves_original_frame(
    original: pd.DataFrame,
    output: pd.DataFrame,
    added_columns: set[str],
    label: str,
) -> None:
    original_columns = tuple(str(column) for column in original.columns)
    if set(output.columns) != set(original_columns) | added_columns:
        raise GridCoverageAssessmentError(f"{label} output schema is inconsistent")
    for column in original_columns:
        if column == "geometry":
            continue
        if not original[column].equals(output[column]):
            raise GridCoverageAssessmentError(
                f"{label} changed original proximity column: {column}"
            )


def _validate_assessment_result(result: GridCoverageAssessmentResult) -> None:
    profile_grid_proximity(
        GridProximityResult(
            parcels=result.parcels,
            voltage_level_proximity=result.voltage_level_proximity,
            voltage_level_coverage=result.voltage_level_coverage,
        )
    )
    _validate_source_coverage(result.source_coverage)
    parcels = result.parcels
    table = result.voltage_level_proximity
    parcel_missing = (
        set(PARCEL_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS)
    ) - set(parcels.columns)
    table_missing = (
        set(VOLTAGE_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS)
    ) - set(table.columns)
    if parcel_missing or table_missing:
        raise GridCoverageAssessmentError("Coverage diagnostic columns are missing")
    boundary_distances = _finite_nonnegative(
        parcels["grid_source_boundary_distance_m"],
        "Grid source boundary distance",
    )
    position = parcels["grid_source_coverage_position"]
    if position.isna().any() or not set(position.unique()) <= COVERAGE_POSITIONS:
        raise GridCoverageAssessmentError("Coverage position values are invalid")
    fully_covered = position.eq("FULLY_COVERED").to_numpy(dtype="bool")
    for distance_column, status_column in (
        ("nearest_line_proxy_distance_m", "nearest_line_coverage_status"),
        (
            "nearest_exact_line_proxy_distance_m",
            "nearest_exact_line_coverage_status",
        ),
        ("nearest_post_proxy_distance_m", "nearest_post_coverage_status"),
    ):
        expected = _coverage_statuses(
            parcels[distance_column], boundary_distances, fully_covered
        )
        actual_status = parcels[status_column].astype("object").reset_index(drop=True)
        expected_status = expected.astype("object").reset_index(drop=True)
        if not actual_status.equals(expected_status):
            raise GridCoverageAssessmentError(
                f"Coverage status is inconsistent: {status_column}"
            )
    boundary_by_id = dict(zip(parcels["parcel_id"], boundary_distances, strict=True))
    fully_by_id = dict(zip(parcels["parcel_id"], fully_covered, strict=True))
    table_boundary = table["parcel_id"].map(boundary_by_id).astype("float64")
    if not table["source_boundary_distance_m"].equals(table_boundary):
        raise GridCoverageAssessmentError(
            "Voltage boundary distances do not match parcel diagnostics"
        )
    table_fully = table["parcel_id"].map(fully_by_id).to_numpy(dtype="bool")
    expected_table_status = _coverage_statuses(
        table["nearest_line_proxy_distance_m"],
        table_boundary.to_numpy(dtype="float64"),
        table_fully,
    )
    actual_table_status = (
        table["coverage_status"].astype("object").reset_index(drop=True)
    )
    expected_table_status = expected_table_status.astype("object").reset_index(
        drop=True
    )
    if not actual_table_status.equals(expected_table_status):
        raise GridCoverageAssessmentError("Voltage coverage statuses are inconsistent")
    lineage = _coverage_lineage_values(result.source_coverage)
    for column, expected in lineage.items():
        for frame in (parcels, table):
            values = frame[column]
            if expected is None:
                valid = values.isna().all()
            else:
                valid = values.eq(expected).all()
            if not valid:
                raise GridCoverageAssessmentError(
                    f"Coverage diagnostic lineage is inconsistent: {column}"
                )


def _assess_grid_coverage_from_proximity(
    proximity_result: GridProximityResult,
    department_coverage: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
    """Classify proximity results against one loaded department boundary.

    All geometry operations use planar XY copies in EPSG:2154. A parcel that
    touches or crosses the source boundary is handled conservatively as not
    fully covered. No parcel, proximity match, or source geometry is mutated.
    """

    _reject_parcel_output_collisions(proximity_result.parcels)
    profile_grid_proximity(proximity_result)
    coverage_frame = _validate_source_coverage(department_coverage)
    _validate_configured_coverage_identity(department_coverage, config)
    _validate_proximity_source_identity(proximity_result, department_coverage)

    source_parcels = proximity_result.parcels
    source_table = proximity_result.voltage_level_proximity
    output_parcels = source_parcels.copy()
    output_table = source_table.copy()

    calculation_parcels = source_parcels.to_crs(CALCULATION_CRS)
    parcel_geometries = np.asarray(
        force_2d(np.asarray(calculation_parcels.geometry.array, dtype=object)),
        dtype=object,
    )
    coverage_geometry = force_2d(coverage_frame.geometry.iloc[0])
    coverage_boundary = boundary(coverage_geometry)
    covered = np.asarray(covers(coverage_geometry, parcel_geometries), dtype="bool")
    touches_boundary = np.asarray(
        intersects(parcel_geometries, coverage_boundary), dtype="bool"
    )
    fully_covered = covered & ~touches_boundary
    measured_boundary = np.asarray(
        distance(parcel_geometries, coverage_boundary), dtype="float64"
    )
    if not np.isfinite(measured_boundary).all() or (measured_boundary < 0).any():
        raise GridCoverageAssessmentError(
            "Calculated coverage boundary distances must be finite and non-negative"
        )
    boundary_distances = np.where(fully_covered, measured_boundary, 0.0)

    output_parcels["grid_source_boundary_distance_m"] = boundary_distances
    output_parcels["grid_source_coverage_position"] = np.where(
        fully_covered,
        "FULLY_COVERED",
        "OUTSIDE_OR_CROSSING_COVERAGE",
    )
    output_parcels["nearest_line_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_line_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )
    output_parcels["nearest_exact_line_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_exact_line_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )
    output_parcels["nearest_post_coverage_status"] = _coverage_statuses(
        output_parcels["nearest_post_proxy_distance_m"],
        boundary_distances,
        fully_covered,
    )

    boundary_by_id = dict(
        zip(output_parcels["parcel_id"], boundary_distances, strict=True)
    )
    covered_by_id = dict(zip(output_parcels["parcel_id"], fully_covered, strict=True))
    output_table["source_boundary_distance_m"] = (
        output_table["parcel_id"].map(boundary_by_id).astype("float64")
    )
    table_fully_covered = (
        output_table["parcel_id"].map(covered_by_id).to_numpy(dtype="bool")
    )
    output_table["coverage_status"] = _coverage_statuses(
        output_table["nearest_line_proxy_distance_m"],
        output_table["source_boundary_distance_m"].to_numpy(dtype="float64"),
        table_fully_covered,
    )
    lineage = _coverage_lineage_values(department_coverage)
    for column, value in lineage.items():
        output_parcels[column] = value
        output_table[column] = value

    _preserves_original_frame(
        source_parcels,
        output_parcels,
        set(PARCEL_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS),
        "Parcel proximity",
    )
    _preserves_original_frame(
        source_table,
        output_table,
        set(VOLTAGE_DIAGNOSTIC_COLUMNS) | set(COVERAGE_LINEAGE_COLUMNS),
        "Voltage proximity",
    )
    if not output_parcels.geometry.geom_equals_exact(
        source_parcels.geometry, tolerance=0, align=False
    ).all():
        raise GridCoverageAssessmentError("Coverage assessment changed parcel geometry")
    if output_parcels.crs is None or source_parcels.crs is None:
        raise GridCoverageAssessmentError("Parcel CRS is required")
    if not CRS.from_user_input(output_parcels.crs).equals(
        CRS.from_user_input(source_parcels.crs)
    ):
        raise GridCoverageAssessmentError("Coverage assessment changed parcel CRS")

    result = GridCoverageAssessmentResult(
        parcels=output_parcels,
        voltage_level_proximity=output_table,
        voltage_level_coverage=proximity_result.voltage_level_coverage,
        source_coverage=department_coverage,
    )
    _validate_assessment_result(result)
    return result


def assess_grid_coverage(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
    """Diagnose source-complete grid proximity against configured coverage."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise GridCoverageAssessmentError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(electricity_source) is not IgnBdTopoElectricityData:
            raise GridCoverageAssessmentError(
                "electricity source must be an IgnBdTopoElectricityData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise GridCoverageAssessmentError(
                "source_config must be an IgnBdTopoSourceConfig"
            )
        _reject_parcel_output_collisions(parcels)
        proximity = enrich_parcel_grid_proximity(
            parcels,
            electricity_source,
            source_config,
        )
        coverage = load_ign_bdtopo_department_coverage(
            electricity_source.extraction,
            source_config,
        )
        if coverage.extraction is not electricity_source.extraction:
            raise GridCoverageAssessmentError(
                "Department coverage must retain the electricity extraction identity"
            )
        return _assess_grid_coverage_from_proximity(
            proximity,
            coverage,
            source_config,
        )
    except GridCoverageAssessmentError:
        raise
    except Exception as error:
        raise GridCoverageAssessmentError(
            "Grid proximity coverage cannot be assessed safely"
        ) from error


def _status_counts(values: pd.Series) -> CoverageStatusCounts:
    counts = values.value_counts()
    return CoverageStatusCounts(
        not_boundary_limited=int(counts.get("NOT_BOUNDARY_LIMITED", 0)),
        boundary_limited=int(counts.get("BOUNDARY_LIMITED", 0)),
        outside_or_crossing_coverage=int(counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)),
        no_match=int(counts.get("NO_MATCH", 0)),
    )


def _boundary_profile(values: pd.Series) -> BoundaryDistanceProfile:
    numeric = _finite_nonnegative(values, "Grid source boundary distance")
    if len(numeric) == 0:
        raise GridCoverageAssessmentError(
            "Cannot profile an empty parcel coverage assessment"
        )
    series = pd.Series(numeric, dtype="float64")
    return BoundaryDistanceProfile(
        count=len(series),
        minimum=float(series.min()),
        p01=float(series.quantile(0.01)),
        p05=float(series.quantile(0.05)),
        p10=float(series.quantile(0.10)),
        p25=float(series.quantile(0.25)),
        p50=float(series.quantile(0.50)),
        p75=float(series.quantile(0.75)),
        p90=float(series.quantile(0.90)),
        p95=float(series.quantile(0.95)),
        p99=float(series.quantile(0.99)),
        maximum=float(series.max()),
    )


def profile_grid_coverage(
    result: GridCoverageAssessmentResult,
) -> GridCoverageProfile:
    """Summarize boundary diagnostics without suitability thresholds."""

    _validate_assessment_result(result)
    parcels = result.parcels
    position_counts = parcels["grid_source_coverage_position"].value_counts()
    voltage_profiles: list[VoltageCoverageStatusProfile] = []
    for item in result.voltage_level_coverage:
        rows = result.voltage_level_proximity.loc[
            result.voltage_level_proximity["voltage_kv"] == item.voltage_kv
        ]
        voltage_profiles.append(
            VoltageCoverageStatusProfile(
                voltage_kv=float(item.voltage_kv),
                parcel_count=len(rows),
                statuses=_status_counts(rows["coverage_status"]),
            )
        )
    return GridCoverageProfile(
        parcel_count=len(parcels),
        fully_covered_count=int(position_counts.get("FULLY_COVERED", 0)),
        outside_or_crossing_count=int(
            position_counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)
        ),
        boundary_distance=_boundary_profile(parcels["grid_source_boundary_distance_m"]),
        nearest_line=_status_counts(parcels["nearest_line_coverage_status"]),
        nearest_exact_line=_status_counts(
            parcels["nearest_exact_line_coverage_status"]
        ),
        nearest_post=_status_counts(parcels["nearest_post_coverage_status"]),
        voltage_levels=tuple(voltage_profiles),
    )
```
