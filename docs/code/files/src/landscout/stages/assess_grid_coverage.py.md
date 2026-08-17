# `src/landscout/stages/assess_grid_coverage.py`

## File identity

- Repository path: `src/landscout/stages/assess_grid_coverage.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: grid/source
- Responsibility: Diagnoses grid proxy distances against the configured IGN source-package boundary.
- Source SHA256: `2a74a08a04563372347c42bacbf53fc124a57ee3a49686586983d81fcef41057`

## 1. Purpose

Diagnoses grid proxy distances against the configured IGN source-package boundary.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **grid/source** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

#### `CALCULATION_CRS`

```python
CALCULATION_CRS = "EPSG:2154"
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` (value argument/reference), `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_normalize_layer` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_combine_catalogs` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_metric_parcels` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_relation_base` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_project_geometries` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_normalize_zones` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_normalize_zones` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_metric_parcels` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_candidate_intersections` (value argument/reference), `src/landscout/stages/enrich_planning_zoning.py::_candidate_intersections` (value argument/reference).

#### `COVERAGE_SPATIAL_ROLE`

```python
COVERAGE_SPATIAL_ROLE = "SOURCE_COVERAGE_BOUNDARY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `COVERAGE_STATUSES`

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

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `COVERAGE_POSITIONS`

```python
COVERAGE_POSITIONS = frozenset(
    {"FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"}
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `PARCEL_DIAGNOSTIC_COLUMNS`

```python
PARCEL_DIAGNOSTIC_COLUMNS = (
    "grid_source_boundary_distance_m",
    "grid_source_coverage_position",
    "nearest_line_coverage_status",
    "nearest_exact_line_coverage_status",
    "nearest_post_coverage_status",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` (value argument/reference), `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` (value argument/reference).

#### `VOLTAGE_DIAGNOSTIC_COLUMNS`

```python
VOLTAGE_DIAGNOSTIC_COLUMNS = (
    "source_boundary_distance_m",
    "coverage_status",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` (value argument/reference), `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` (value argument/reference).

#### `COVERAGE_LINEAGE_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` (value argument/reference), `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` (value argument/reference).

#### `_SOURCE_LINEAGE_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `_IGN_PROVIDER_IDENTITIES`

```python
_IGN_PROVIDER_IDENTITIES = frozenset(
    {
        "ign",
        "institutnationaldelinformationgeographiqueetforestiereign",
    }
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_SHA256_PATTERN`

```python
_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.


### B. Type aliases and closed domains

#### `CoverageStatus`

```python
CoverageStatus = Literal[
    "NOT_BOUNDARY_LIMITED",
    "BOUNDARY_LIMITED",
    "OUTSIDE_OR_CROSSING_COVERAGE",
    "NO_MATCH",
]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. It is consumed by annotations or Pydantic validation in this module.

#### `CoveragePosition`

```python
CoveragePosition = Literal["FULLY_COVERED", "OUTSIDE_OR_CROSSING_COVERAGE"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. It is consumed by annotations or Pydantic validation in this module.


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `GridCoverageAssessmentError`

**Purpose:** Raised when coverage diagnostics cannot be calculated safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validated_lambert93` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_normalized_identity` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_strict_nonnegative_integer` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_coverage_summary` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_configured_coverage_identity` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_proximity_source_identity` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_finite_nonnegative` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_preserves_original_frame` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::assess_grid_coverage` via `GridCoverageAssessmentError`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_boundary_profile` via `GridCoverageAssessmentError`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `pytest.raises(GridCoverageAssessmentError, match='physical|configured')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `pytest.raises(GridCoverageAssessmentError)`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `pytest.raises(GridCoverageAssessmentError, match='parcels|GeoDataFrame')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` via `pytest.raises(GridCoverageAssessmentError, match=message)`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match` via `pytest.raises(GridCoverageAssessmentError, match='lineage')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity` via `pytest.raises(GridCoverageAssessmentError, match='provider|product|identity')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame` via `pytest.raises(GridCoverageAssessmentError, match='selected|count')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns` via `pytest.raises(GridCoverageAssessmentError, match='summary|column|dtype|schema')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame` via `pytest.raises(GridCoverageAssessmentError, match='CRS|2154')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated` via `pytest.raises(GridCoverageAssessmentError, match='geometry|summary')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match` via `pytest.raises(GridCoverageAssessmentError, match='department')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact` via `pytest.raises(GridCoverageAssessmentError, match='department|field')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `pytest.raises(GridCoverageAssessmentError, match='source|count')`.
- callback/function object: `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `pytest.raises(GridCoverageAssessmentError, match='layer|lineage')`.
- import/re-export: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.stages import (
    GridCoverageAssessmentError,
    profile_grid_coverage,
)`.

**Exact class source**

```python
class GridCoverageAssessmentError(ValueError):
    """Raised when coverage diagnostics cannot be calculated safely."""
```

### `GridCoverageAssessmentResult`

**Purpose:** Coverage-annotated copies of both grid-proximity representations.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `voltage_level_proximity` | `voltage_level_proximity: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `voltage_level_coverage` | `voltage_level_coverage: tuple[VoltageLevelCoverage, ...]` | Structured `voltage level coverage` collection owned by `GridCoverageAssessmentResult`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `source_coverage` | `source_coverage: IgnBdTopoDepartmentCoverage` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `GridCoverageAssessmentResult`.

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

**Purpose:** Immutable result/value envelope carrying `count`, `minimum`, `p01`, `p05`, `p10`, `p25`, `p50`, `p75`, `p90`, `p95`, `p99`, `maximum`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `count` | `count: int` | Stores `BoundaryDistanceProfile`'s `count` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `minimum` | `minimum: float` | Stores `BoundaryDistanceProfile`'s `minimum` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p01` | `p01: float` | Stores `BoundaryDistanceProfile`'s `p01` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p05` | `p05: float` | Stores `BoundaryDistanceProfile`'s `p05` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p10` | `p10: float` | Stores `BoundaryDistanceProfile`'s `p10` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p25` | `p25: float` | Stores `BoundaryDistanceProfile`'s `p25` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p50` | `p50: float` | Stores `BoundaryDistanceProfile`'s `p50` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p75` | `p75: float` | Stores `BoundaryDistanceProfile`'s `p75` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p90` | `p90: float` | Stores `BoundaryDistanceProfile`'s `p90` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p95` | `p95: float` | Stores `BoundaryDistanceProfile`'s `p95` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `p99` | `p99: float` | Stores `BoundaryDistanceProfile`'s `p99` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `maximum` | `maximum: float` | Stores `BoundaryDistanceProfile`'s `maximum` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_boundary_profile` via `BoundaryDistanceProfile`.

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

**Purpose:** Immutable result/value envelope carrying `not_boundary_limited`, `boundary_limited`, `outside_or_crossing_coverage`, `no_match`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `not_boundary_limited` | `not_boundary_limited: int` | Stores `CoverageStatusCounts`'s `not boundary limited` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `boundary_limited` | `boundary_limited: int` | Stores `CoverageStatusCounts`'s `boundary limited` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `outside_or_crossing_coverage` | `outside_or_crossing_coverage: int` | Stores `CoverageStatusCounts`'s `outside or crossing coverage` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `no_match` | `no_match: int` | Stores `CoverageStatusCounts`'s `no match` value under exact annotation `int`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_status_counts` via `CoverageStatusCounts`.

**Exact class source**

```python
class CoverageStatusCounts:
    not_boundary_limited: int
    boundary_limited: int
    outside_or_crossing_coverage: int
    no_match: int
```

### `VoltageCoverageStatusProfile`

**Purpose:** Immutable result/value envelope carrying `voltage_kv`, `parcel_count`, `statuses`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `voltage_kv` | `voltage_kv: float` | Stores `VoltageCoverageStatusProfile`'s `voltage kv` value under exact annotation `float`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `parcel_count` | `parcel_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `statuses` | `statuses: CoverageStatusCounts` | Closed or validated `statuses` classification on `VoltageCoverageStatusProfile`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::profile_grid_coverage` via `VoltageCoverageStatusProfile`.

**Exact class source**

```python
class VoltageCoverageStatusProfile:
    voltage_kv: float
    parcel_count: int
    statuses: CoverageStatusCounts
```

### `GridCoverageProfile`

**Purpose:** Immutable result/value envelope carrying `parcel_count`, `fully_covered_count`, `outside_or_crossing_count`, `boundary_distance`, `nearest_line`, `nearest_exact_line`, `nearest_post`, `voltage_levels`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcel_count` | `parcel_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `fully_covered_count` | `fully_covered_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `outside_or_crossing_count` | `outside_or_crossing_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `boundary_distance` | `boundary_distance: BoundaryDistanceProfile` | Stores `GridCoverageProfile`'s `boundary distance` value under exact annotation `BoundaryDistanceProfile`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `nearest_line` | `nearest_line: CoverageStatusCounts` | Stores `GridCoverageProfile`'s `nearest line` value under exact annotation `CoverageStatusCounts`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `nearest_exact_line` | `nearest_exact_line: CoverageStatusCounts` | Stores `GridCoverageProfile`'s `nearest exact line` value under exact annotation `CoverageStatusCounts`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `nearest_post` | `nearest_post: CoverageStatusCounts` | Stores `GridCoverageProfile`'s `nearest post` value under exact annotation `CoverageStatusCounts`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `voltage_levels` | `voltage_levels: tuple[VoltageCoverageStatusProfile, ...]` | Structured `voltage levels` collection owned by `GridCoverageProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::profile_grid_coverage` via `GridCoverageProfile`.

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


## 6. Functions and methods

### `_validated_lambert93`

**Exact signature**

```python
def _validated_lambert93(value: object, label: str) -> CRS:
```

**Purpose**

Checks and returns canonical lambert93; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
crs
```

**Validation and exceptions**

- Guard with a raise path: `value is None`.
- Guard with a raise path: `not crs.is_projected or not crs.equals(expected)`.
- Explicit raise expressions: `GridCoverageAssessmentError(f'{label} CRS is required')`, `GridCoverageAssessmentError(f'{label} CRS is unreadable')`, `GridCoverageAssessmentError(f'{label} must use EPSG:2154')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_coverage_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_layer_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_frame` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_input` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_layer_summary` via `_validated_lambert93`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `_validated_lambert93`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_normalized_identity`

**Exact signature**

```python
def _normalized_identity(value: object, label: str) -> str:
```

**Purpose**

Private `grid/source` helper for normalized identity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
''.join((character for character in decomposed.casefold() if character.isalnum()))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `GridCoverageAssessmentError(f'Department coverage {label} must be a non-empty exact string')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_configured_coverage_identity` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/normalize_access_ign.py::_validate_source_bundle` via `_normalized_identity`.
- direct call or construction: `src/landscout/stages/normalize_grid_ign.py::_validate_archive_identity` via `_normalized_identity`.

**Complete source-ordered implementation**

```python
def _normalized_identity(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise GridCoverageAssessmentError(
            f"Department coverage {label} must be a non-empty exact string"
        )
    decomposed = unicodedata.normalize("NFKD", value)
    return "".join(
        character
        for character in decomposed.casefold()
        if character.isalnum()
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_strict_nonnegative_integer`

**Exact signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Private `grid/source` helper for strict nonnegative integer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `type(value) is not int or value < 0`.
- Explicit raise expressions: `GridCoverageAssessmentError(f'Department coverage summary {label} must be a non-negative integer')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_coverage_summary` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_layer_summary` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_integer_values` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_pages` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::search_planning_regulation` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_validate_planning_regulation_search_result` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_validate_parcels` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_sections` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_zone_mapping` via `_strict_nonnegative_integer`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_topic_evidence` via `_strict_nonnegative_integer`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_coverage_summary`

**Exact signature**

```python
def _validate_coverage_summary(
    source: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent coverage summary; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(summary) is not IgnBdTopoCoverageLayerSummary`.
- Guard with a raise path: `summary.source_layer_name != source.source_layer`.
- Guard with a raise path: `not summary_crs.equals(frame_crs)`.
- Guard with a raise path: `type(summary.selected_feature_count) is not int or summary.selected_feature_count != len(frame)`.
- Guard with a raise path: `source_count < summary.selected_feature_count`.
- Guard with a raise path: `type(summary.columns) is not tuple or not summary.columns or any((not isinstance(column, str) or not column or column != column.strip() for column in summary.columns)) or (len(set(summary.columns)) != len(summary.columns))`.
- Guard with a raise path: `tuple((str(column) for column in frame.columns)) != expected_frame_columns`.
- Guard with a raise path: `type(summary.dtypes) is not tuple or summary.dtypes != observed_dtypes`.
- Guard with a raise path: `any((count > source_count for count in geometry_counts))`.
- Guard with a raise path: `type(geometry_types) is not tuple or geometry_types != tuple(sorted(set(geometry_types))) or (not set(geometry_types) <= {'Polygon', 'MultiPolygon'})`.
- Guard with a raise path: `source_count == summary.selected_feature_count and (geometry_counts != selected_counts or geometry_types != selected_types)`.
- Guard with a raise path: `any((observed > reported for observed, reported in zip(selected_counts, geometry_counts, strict=True))) or not set(selected_types) <= set(geometry_types)`.
- Guard with a raise path: `not isinstance(department_field, str) or not department_field or department_field != department_field.strip() or (department_field not in summary.columns)`.
- Guard with a raise path: `summary.selected_department_code != source.source_department_code`.
- Guard with a raise path: `not frame[department_field].eq(source.source_department_code).all()`.
- Guard with a raise path: `summary.spatial_role != source.spatial_role`.
- Explicit raise expressions: `GridCoverageAssessmentError('Department coverage selected department field is inconsistent')`, `GridCoverageAssessmentError('Department coverage selected geometry contradicts source summary')`, `GridCoverageAssessmentError('Department coverage summary CRS does not match the selected frame')`, `GridCoverageAssessmentError('Department coverage summary columns are invalid')`, `GridCoverageAssessmentError('Department coverage summary department field is invalid')`, `GridCoverageAssessmentError('Department coverage summary geometry count exceeds source count')`, `GridCoverageAssessmentError('Department coverage summary geometry facts do not match frame')`, `GridCoverageAssessmentError('Department coverage summary geometry types are invalid')`, `GridCoverageAssessmentError('Department coverage summary layer does not match source lineage')`, `GridCoverageAssessmentError('Department coverage summary ordered columns do not match frame')`, `GridCoverageAssessmentError('Department coverage summary ordered dtypes do not match frame')`, `GridCoverageAssessmentError('Department coverage summary selected department code is inconsistent')`, `GridCoverageAssessmentError('Department coverage summary selected feature count does not match frame')`, `GridCoverageAssessmentError('Department coverage summary source count is smaller than selected count')`, `GridCoverageAssessmentError('Department coverage summary spatial role is inconsistent')`, `GridCoverageAssessmentError('Department coverage summary type is invalid')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(~selected_geometry.isna() & selected_geometry.is_empty).sum`, `(~selected_geometry.isna() & ~selected_geometry.is_empty & ~selected_geometry.is_valid).sum`, `selected_geometry.geom_type.dropna`, `selected_geometry.geom_type.dropna().unique`, `selected_geometry.isna`, `selected_geometry.isna().sum`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_source_coverage` via `_validate_coverage_summary`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_source_coverage` via `_validate_coverage_summary`.

**Complete source-ordered implementation**

```python
def _validate_coverage_summary(
    source: IgnBdTopoDepartmentCoverage,
    frame: gpd.GeoDataFrame,
) -> None:
    summary = source.summary
    if type(summary) is not IgnBdTopoCoverageLayerSummary:
        raise GridCoverageAssessmentError(
            "Department coverage summary type is invalid"
        )
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
            not isinstance(column, str)
            or not column
            or column != column.strip()
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_source_coverage`

**Exact signature**

```python
def _validate_source_coverage(
    source: IgnBdTopoDepartmentCoverage,
) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent source coverage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `type(source) is not IgnBdTopoDepartmentCoverage`.
- Guard with a raise path: `source.spatial_role != COVERAGE_SPATIAL_ROLE`.
- Guard with a raise path: `provider not in _IGN_PROVIDER_IDENTITIES`.
- Guard with a raise path: `product != 'bdtopo'`.
- Guard with a raise path: `_SHA256_PATTERN.fullmatch(source.source_archive_sha256) is None`.
- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `'geometry' not in frame.columns or frame.active_geometry_name != 'geometry'`.
- Guard with a raise path: `len(frame) != 1`.
- Guard with a raise path: `geometry.isna().any()`.
- Guard with a raise path: `geometry.is_empty.any()`.
- Guard with a raise path: `not geometry.is_valid.all()`.
- Guard with a raise path: `not set(geometry.geom_type.dropna()) <= {'Polygon', 'MultiPolygon'}`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Guard with a raise path: `not both_null and actual != expected`.
- Explicit raise expressions: `GridCoverageAssessmentError('Department coverage archive SHA256 is invalid')`, `GridCoverageAssessmentError('Department coverage geometry column must exist and be active')`, `GridCoverageAssessmentError('Department coverage geometry must be Polygon or MultiPolygon')`, `GridCoverageAssessmentError('Department coverage geometry must be valid')`, `GridCoverageAssessmentError('Department coverage geometry must not be empty')`, `GridCoverageAssessmentError('Department coverage geometry must not be null')`, `GridCoverageAssessmentError('Department coverage lineage columns are missing: ' + ', '.join(sorted(missing)))`, `GridCoverageAssessmentError('Department coverage must be a GeoDataFrame')`, `GridCoverageAssessmentError('Department coverage must contain exactly one selected feature')`, `GridCoverageAssessmentError('Department coverage product is not BD TOPO')`, `GridCoverageAssessmentError('Department coverage provider is not an IGN identity')`, `GridCoverageAssessmentError('Department coverage source type is invalid')`, `GridCoverageAssessmentError('Department coverage spatial_role must be SOURCE_COVERAGE_BOUNDARY')`, `GridCoverageAssessmentError(f'Department coverage lineage is inconsistent: {column}')`, `GridCoverageAssessmentError(f'Department coverage {label} must be a non-empty exact string')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.geom_type.dropna`, `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`.
- Hashing: `_SHA256_PATTERN.fullmatch`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` via `_validate_source_coverage`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `_validate_source_coverage`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_validate_source_coverage`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_source_coverage`.

**Complete source-ordered implementation**

```python
def _validate_source_coverage(
    source: IgnBdTopoDepartmentCoverage,
) -> gpd.GeoDataFrame:
    if type(source) is not IgnBdTopoDepartmentCoverage:
        raise GridCoverageAssessmentError(
            "Department coverage source type is invalid"
        )
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
        raise GridCoverageAssessmentError(
            "Department coverage product is not BD TOPO"
        )
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
        raise GridCoverageAssessmentError("Department coverage geometry must not be null")
    if geometry.is_empty.any():
        raise GridCoverageAssessmentError("Department coverage geometry must not be empty")
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_configured_coverage_identity`

**Exact signature**

```python
def _validate_configured_coverage_identity(
    source: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent configured coverage identity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `source.source_layer != expected_layer`.
- Guard with a raise path: `source.summary.department_code_field != expected_field`.
- Guard with a raise path: `archive.department_code != config.department_code`.
- Guard with a raise path: `archive_provider not in _IGN_PROVIDER_IDENTITIES or config_provider not in _IGN_PROVIDER_IDENTITIES`.
- Guard with a raise path: `_normalized_identity(archive.product, 'archive product') != 'bdtopo' or _normalized_identity(config.product, 'config product') != 'bdtopo'`.
- Explicit raise expressions: `GridCoverageAssessmentError('Department coverage archive differs from the configured department')`, `GridCoverageAssessmentError('Department coverage archive product differs from config')`, `GridCoverageAssessmentError('Department coverage archive provider differs from config')`, `GridCoverageAssessmentError('Department coverage does not use the configured department field')`, `GridCoverageAssessmentError('Department coverage does not use the configured physical layer')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `_validate_configured_coverage_identity`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_coverage_lineage_values`

**Exact signature**

```python
def _coverage_lineage_values(
    source: IgnBdTopoDepartmentCoverage,
) -> dict[str, object]:
```

**Purpose**

Private `grid/source` helper for coverage lineage values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'grid_source_coverage_provider': source.source_provider, 'grid_source_coverage_product': source.source_product, 'grid_source_coverage_department_code': source.source_department_code, 'grid_source_coverage_edition': source.source_edition, 'grid_source_coverage_product_version': source.source_product_version, 'grid_source_coverage_archive_sha256': source.source_archive_sha256, 'grid_source_coverage_layer': source.source_layer, 'grid_source_coverage_spatial_role': source.spatial_role}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` via `_coverage_lineage_values`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `_coverage_lineage_values`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_proximity_source_identity`

**Exact signature**

```python
def _validate_proximity_source_identity(
    proximity: GridProximityResult,
    source: IgnBdTopoDepartmentCoverage,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent proximity source identity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not values.eq(expected).all()`.
- Guard with a raise path: `not proximity.voltage_level_proximity[column].eq(expected).all()`.
- Explicit raise expressions: `GridCoverageAssessmentError(f'Proximity lineage does not match department coverage: {column}')`, `GridCoverageAssessmentError(f'Voltage proximity lineage does not match coverage: {column}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `_validate_proximity_source_identity`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_finite_nonnegative`

**Exact signature**

```python
def _finite_nonnegative(values: pd.Series, label: str) -> np.ndarray:
```

**Purpose**

Private `grid/source` helper for finite nonnegative; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `np.ndarray`.
- Every observed return expression is reproduced without truncation:
```python
np.asarray(converted, dtype='float64')
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, Real) or isinstance(value, bool)`.
- Guard with a raise path: `not isfinite(numeric) or numeric < 0`.
- Explicit raise expressions: `GridCoverageAssessmentError(f'{label} must be finite and non-negative')`, `GridCoverageAssessmentError(f'{label} must be finite')`, `GridCoverageAssessmentError(f'{label} must be numeric')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` via `_finite_nonnegative`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_boundary_profile` via `_finite_nonnegative`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_match_rows` via `_finite_nonnegative`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_finite_nonnegative`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_coverage_statuses`

**Exact signature**

```python
def _coverage_statuses(
    distances: pd.Series,
    boundary_distances: np.ndarray,
    fully_covered: np.ndarray,
) -> pd.Series:
```

**Purpose**

Private `grid/source` helper for coverage statuses; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
pd.Series(statuses, index=distances.index, dtype='object')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `distances.to_numpy`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `statuses[internal & (numeric < boundary_distances)]`, `statuses[internal & (numeric >= boundary_distances)]`, `statuses[outside]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` via `_coverage_statuses`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `_coverage_statuses`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_expected_diagnostics` via `_coverage_statuses`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_preserves_original_frame`

**Exact signature**

```python
def _preserves_original_frame(
    original: pd.DataFrame,
    output: pd.DataFrame,
    added_columns: set[str],
    label: str,
) -> None:
```

**Purpose**

Private `grid/source` helper for preserves original frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `set(output.columns) != set(original_columns) | added_columns`.
- Guard with a raise path: `not original[column].equals(output[column])`.
- Explicit raise expressions: `GridCoverageAssessmentError(f'{label} changed original proximity column: {column}')`, `GridCoverageAssessmentError(f'{label} output schema is inconsistent')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `_preserves_original_frame`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_assessment_result`

**Exact signature**

```python
def _validate_assessment_result(result: GridCoverageAssessmentResult) -> None:
```

**Purpose**

Rejects malformed or inconsistent assessment result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `parcel_missing or table_missing`.
- Guard with a raise path: `position.isna().any() or not set(position.unique()) <= COVERAGE_POSITIONS`.
- Guard with a raise path: `not table['source_boundary_distance_m'].equals(table_boundary)`.
- Guard with a raise path: `not actual_table_status.equals(expected_table_status)`.
- Guard with a raise path: `not actual_status.equals(expected_status)`.
- Guard with a raise path: `not valid`.
- Explicit raise expressions: `GridCoverageAssessmentError('Coverage diagnostic columns are missing')`, `GridCoverageAssessmentError('Coverage position values are invalid')`, `GridCoverageAssessmentError('Voltage boundary distances do not match parcel diagnostics')`, `GridCoverageAssessmentError('Voltage coverage statuses are inconsistent')`, `GridCoverageAssessmentError(f'Coverage diagnostic lineage is inconsistent: {column}')`, `GridCoverageAssessmentError(f'Coverage status is inconsistent: {status_column}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `table['parcel_id'].map(boundary_by_id).astype`, `table['source_boundary_distance_m'].equals`, `table_boundary.to_numpy`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `_validate_assessment_result`.
- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::profile_grid_coverage` via `_validate_assessment_result`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_assessment_result`.

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
        set(PARCEL_DIAGNOSTIC_COLUMNS)
        | set(COVERAGE_LINEAGE_COLUMNS)
    ) - set(parcels.columns)
    table_missing = (
        set(VOLTAGE_DIAGNOSTIC_COLUMNS)
        | set(COVERAGE_LINEAGE_COLUMNS)
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
    boundary_by_id = dict(
        zip(parcels["parcel_id"], boundary_distances, strict=True)
    )
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
    actual_table_status = table["coverage_status"].astype("object").reset_index(
        drop=True
    )
    expected_table_status = expected_table_status.astype("object").reset_index(
        drop=True
    )
    if not actual_table_status.equals(expected_table_status):
        raise GridCoverageAssessmentError(
            "Voltage coverage statuses are inconsistent"
        )
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_assess_grid_coverage_from_proximity`

**Exact signature**

```python
def _assess_grid_coverage_from_proximity(
    proximity_result: GridProximityResult,
    department_coverage: IgnBdTopoDepartmentCoverage,
    config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
```

**Purpose**

Classify proximity results against one loaded department boundary. All geometry operations use planar XY copies in EPSG:2154. A parcel that touches or crosses the source boundary is handled conservatively as not fully covered. No parcel, proximity match, or source geometry is mutated.

**Return contract**

- Declared return annotation: `GridCoverageAssessmentResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `not np.isfinite(measured_boundary).all() or (measured_boundary < 0).any()`.
- Guard with a raise path: `not output_parcels.geometry.geom_equals_exact(source_parcels.geometry, tolerance=0, align=False).all()`.
- Guard with a raise path: `output_parcels.crs is None or source_parcels.crs is None`.
- Guard with a raise path: `not CRS.from_user_input(output_parcels.crs).equals(CRS.from_user_input(source_parcels.crs))`.
- Explicit raise expressions: `GridCoverageAssessmentError('Calculated coverage boundary distances must be finite and non-negative')`, `GridCoverageAssessmentError('Coverage assessment changed parcel CRS')`, `GridCoverageAssessmentError('Coverage assessment changed parcel geometry')`, `GridCoverageAssessmentError('Parcel CRS is required')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(measured_boundary < 0).any`, `boundary`, `distance`, `force_2d`, `np.isfinite(measured_boundary).all`, `output_parcels.geometry.geom_equals_exact`, `output_parcels.geometry.geom_equals_exact(source_parcels.geometry, tolerance=0, align=False).all`, `output_table['parcel_id'].map(boundary_by_id).astype`, `output_table['source_boundary_distance_m'].to_numpy`, `source_parcels.to_crs`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output_parcels['grid_source_boundary_distance_m']`, `output_parcels['grid_source_coverage_position']`, `output_parcels['nearest_exact_line_coverage_status']`, `output_parcels['nearest_line_coverage_status']`, `output_parcels['nearest_post_coverage_status']`, `output_parcels[column]`, `output_table['coverage_status']`, `output_table['source_boundary_distance_m']`, `output_table[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::assess_grid_coverage` via `_assess_grid_coverage_from_proximity`.
- import/re-export: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    _assess_grid_coverage_from_proximity as assess_grid_coverage,
)`.

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
    covered_by_id = dict(
        zip(output_parcels["parcel_id"], fully_covered, strict=True)
    )
    output_table["source_boundary_distance_m"] = (
        output_table["parcel_id"].map(boundary_by_id).astype("float64")
    )
    table_fully_covered = output_table["parcel_id"].map(covered_by_id).to_numpy(
        dtype="bool"
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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `assess_grid_coverage`

**Exact signature**

```python
def assess_grid_coverage(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridCoverageAssessmentResult:
```

**Purpose**

Diagnose source-complete grid proximity against configured coverage.

**Return contract**

- Declared return annotation: `GridCoverageAssessmentResult`.
- Every observed return expression is reproduced without truncation:
```python
_assess_grid_coverage_from_proximity(proximity, coverage, source_config)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `type(electricity_source) is not IgnBdTopoElectricityData`.
- Guard with a raise path: `type(source_config) is not IgnBdTopoSourceConfig`.
- Guard with a raise path: `coverage.extraction is not electricity_source.extraction`.
- Explicit raise expressions: `GridCoverageAssessmentError('Department coverage must retain the electricity extraction identity')`, `GridCoverageAssessmentError('Grid proximity coverage cannot be assessed safely')`, `GridCoverageAssessmentError('electricity source must be an IgnBdTopoElectricityData')`, `GridCoverageAssessmentError('parcels must be a GeoDataFrame with active geometry')`, `GridCoverageAssessmentError('source_config must be an IgnBdTopoSourceConfig')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `assess_grid_coverage`.
- property/attribute access: `tests/unit/test_assess_grid_coverage.py::test_clean_coverage_api_is_exported` via `stages.assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `assess_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `assess_grid_coverage`.
- import/re-export: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.stages import (
    assess_grid_coverage as public_assess_grid_coverage,
)`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_status_counts`

**Exact signature**

```python
def _status_counts(values: pd.Series) -> CoverageStatusCounts:
```

**Purpose**

Private `grid/source` helper for status counts; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `CoverageStatusCounts`.
- Every observed return expression is reproduced without truncation:
```python
CoverageStatusCounts(not_boundary_limited=int(counts.get('NOT_BOUNDARY_LIMITED', 0)), boundary_limited=int(counts.get('BOUNDARY_LIMITED', 0)), outside_or_crossing_coverage=int(counts.get('OUTSIDE_OR_CROSSING_COVERAGE', 0)), no_match=int(counts.get('NO_MATCH', 0)))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::profile_grid_coverage` via `_status_counts`.

**Complete source-ordered implementation**

```python
def _status_counts(values: pd.Series) -> CoverageStatusCounts:
    counts = values.value_counts()
    return CoverageStatusCounts(
        not_boundary_limited=int(counts.get("NOT_BOUNDARY_LIMITED", 0)),
        boundary_limited=int(counts.get("BOUNDARY_LIMITED", 0)),
        outside_or_crossing_coverage=int(
            counts.get("OUTSIDE_OR_CROSSING_COVERAGE", 0)
        ),
        no_match=int(counts.get("NO_MATCH", 0)),
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_boundary_profile`

**Exact signature**

```python
def _boundary_profile(values: pd.Series) -> BoundaryDistanceProfile:
```

**Purpose**

Private `grid/source` helper for boundary profile; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BoundaryDistanceProfile`.
- Every observed return expression is reproduced without truncation:
```python
BoundaryDistanceProfile(count=len(series), minimum=float(series.min()), p01=float(series.quantile(0.01)), p05=float(series.quantile(0.05)), p10=float(series.quantile(0.1)), p25=float(series.quantile(0.25)), p50=float(series.quantile(0.5)), p75=float(series.quantile(0.75)), p90=float(series.quantile(0.9)), p95=float(series.quantile(0.95)), p99=float(series.quantile(0.99)), maximum=float(series.max()))
```

**Validation and exceptions**

- Guard with a raise path: `len(numeric) == 0`.
- Explicit raise expressions: `GridCoverageAssessmentError('Cannot profile an empty parcel coverage assessment')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `BoundaryDistanceProfile`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/assess_grid_coverage.py::profile_grid_coverage` via `_boundary_profile`.

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

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `profile_grid_coverage`

**Exact signature**

```python
def profile_grid_coverage(
    result: GridCoverageAssessmentResult,
) -> GridCoverageProfile:
```

**Purpose**

Summarize boundary diagnostics without suitability thresholds.

**Return contract**

- Declared return annotation: `GridCoverageProfile`.
- Every observed return expression is reproduced without truncation:
```python
GridCoverageProfile(parcel_count=len(parcels), fully_covered_count=int(position_counts.get('FULLY_COVERED', 0)), outside_or_crossing_count=int(position_counts.get('OUTSIDE_OR_CROSSING_COVERAGE', 0)), boundary_distance=_boundary_profile(parcels['grid_source_boundary_distance_m']), nearest_line=_status_counts(parcels['nearest_line_coverage_status']), nearest_exact_line=_status_counts(parcels['nearest_exact_line_coverage_status']), nearest_post=_status_counts(parcels['nearest_post_coverage_status']), voltage_levels=tuple(voltage_profiles))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_boundary_profile`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.assess_grid_coverage import (
    BoundaryDistanceProfile,
    CoverageStatusCounts,
    GridCoverageAssessmentError,
    GridCoverageAssessmentResult,
    GridCoverageProfile,
    VoltageCoverageStatusProfile,
    assess_grid_coverage,
    profile_grid_coverage,
)`.
- property/attribute access: `tests/unit/test_assess_grid_coverage.py::test_clean_coverage_api_is_exported` via `stages.profile_grid_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `profile_grid_coverage`.
- import/re-export: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.stages import (
    GridCoverageAssessmentError,
    profile_grid_coverage,
)`.

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
        boundary_distance=_boundary_profile(
            parcels["grid_source_boundary_distance_m"]
        ),
        nearest_line=_status_counts(parcels["nearest_line_coverage_status"]),
        nearest_exact_line=_status_counts(
            parcels["nearest_exact_line_coverage_status"]
        ),
        nearest_post=_status_counts(parcels["nearest_post_coverage_status"]),
        voltage_levels=tuple(voltage_profiles),
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.


## 7. Data contracts

### Frame-preservation and semantic notes

- Coverage fields are diagnostics appended to the proximity results. The coverage boundary is the full configured department polygon boundary in EPSG:2154; it is not an electrical service territory or connection boundary.

### `PARCEL_DIAGNOSTIC_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_DIAGNOSTIC_COLUMNS = (
    "grid_source_boundary_distance_m",
    "grid_source_coverage_position",
    "nearest_line_coverage_status",
    "nearest_exact_line_coverage_status",
    "nearest_post_coverage_status",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `grid_source_boundary_distance_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 2 | `grid_source_coverage_position` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `nearest_line_coverage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `nearest_exact_line_coverage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `nearest_post_coverage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |

### `VOLTAGE_DIAGNOSTIC_COLUMNS` — canonical or derived frame-column schema

```python
VOLTAGE_DIAGNOSTIC_COLUMNS = (
    "source_boundary_distance_m",
    "coverage_status",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `source_boundary_distance_m` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `coverage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |

### `COVERAGE_LINEAGE_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `grid_source_coverage_provider` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `grid_source_coverage_product` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `grid_source_coverage_department_code` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `grid_source_coverage_edition` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `grid_source_coverage_product_version` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `grid_source_coverage_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 7 | `grid_source_coverage_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `grid_source_coverage_spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `_SOURCE_LINEAGE_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `source_provider` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `source_product` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_product_version` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 7 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


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

The module contributes to the grid/source flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
