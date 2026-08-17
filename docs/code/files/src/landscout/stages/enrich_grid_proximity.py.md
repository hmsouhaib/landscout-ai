# `src/landscout/stages/enrich_grid_proximity.py`

## File identity

- Repository path: `src/landscout/stages/enrich_grid_proximity.py`
- File type: Python source
- Layer: spatial proxy enrichment stage
- Domain: grid/source
- Responsibility: Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.
- Source SHA256: `b6b2f3c296b3fc933a542a33157b42f4260a7356a0da8e59710c2d482cf2d8c3`

## 1. Purpose

Computes parcel-to-grid proxy distances and exact-voltage views from verified IGN electricity source data.

## 2. Position in LandScout architecture

This file belongs to the **spatial proxy enrichment stage** layer and the **grid/source** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from dataclasses import dataclass`
- `from math import isfinite`
- `from numbers import Integral, Real`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pandas.api.types import is_scalar`
- `from pyproj import CRS`
- `from shapely import STRtree, force_2d`

### Internal LandScout imports

- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoElectricityData,
    IgnBdTopoSourceConfig,
)`
- `from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)`

## 4. Contract taxonomy

### A. Python constants

#### `CALCULATION_CRS`

```python
CALCULATION_CRS = "EPSG:2154"
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `SPATIAL_ROLE`

```python
SPATIAL_ROLE = "PROXY_GEOMETRY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_grid` (value reference).

#### `PARCEL_REQUIRED_COLUMNS`

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_parcels` (value reference).

#### `LINE_REQUIRED_COLUMNS`

```python
LINE_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "voltage_raw",
        "voltage_status",
        "voltage_kv",
        "voltage_upper_bound_kv",
        "manager_name",
        "asset_status_raw",
        "geometry",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `POST_REQUIRED_COLUMNS`

```python
POST_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "name",
        "importance_raw",
        "asset_status_raw",
        "geometry",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `GRID_GEOMETRY_STATUSES`

```python
GRID_GEOMETRY_STATUSES = frozenset({"VALID", "NULL", "EMPTY", "INVALID"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_grid` (value reference).

#### `LINE_GEOMETRY_TYPES`

```python
LINE_GEOMETRY_TYPES = frozenset({"LineString", "MultiLineString"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `POST_GEOMETRY_TYPES`

```python
POST_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `PARCEL_GEOMETRY_TYPES`

```python
PARCEL_GEOMETRY_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_parcels` (value reference).

#### `VOLTAGE_PROXIMITY_COLUMNS`

```python
VOLTAGE_PROXIMITY_COLUMNS = (
    "parcel_id",
    "voltage_kv",
    "nearest_line_proxy_distance_m",
    "nearest_line_grid_feature_id",
    "nearest_line_source_feature_id",
    "tie_count",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_enrich_grid_proximity.py::<module>` (import), `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_table` (value reference), `src/landscout/stages/enrich_grid_proximity.py::_voltage_level_table` (value reference), `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` (value reference), `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` (value reference).

#### `_LINE_MATCH_COLUMNS`

```python
_LINE_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `_POST_MATCH_COLUMNS`

```python
_POST_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "name",
    "importance_raw",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `_LINE_OUTPUT_MAPPING`

```python
_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_line_proxy_distance_m",
    "grid_feature_id": "nearest_line_grid_feature_id",
    "source_feature_id": "nearest_line_source_feature_id",
    "tie_count": "nearest_line_tie_count",
    "voltage_raw": "nearest_line_voltage_raw",
    "voltage_status": "nearest_line_voltage_status",
    "voltage_kv": "nearest_line_voltage_kv",
    "voltage_upper_bound_kv": "nearest_line_voltage_upper_bound_kv",
    "manager_name": "nearest_line_manager_name",
    "asset_status_raw": "nearest_line_asset_status_raw",
    "source_department_code": "nearest_line_source_department_code",
    "source_edition": "nearest_line_source_edition",
    "source_archive_sha256": "nearest_line_source_archive_sha256",
}
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` (value reference), `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `_EXACT_LINE_OUTPUT_MAPPING`

```python
_EXACT_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_exact_line_proxy_distance_m",
    "grid_feature_id": "nearest_exact_line_grid_feature_id",
    "source_feature_id": "nearest_exact_line_source_feature_id",
    "tie_count": "nearest_exact_line_tie_count",
    "voltage_kv": "nearest_exact_line_voltage_kv",
    "manager_name": "nearest_exact_line_manager_name",
    "asset_status_raw": "nearest_exact_line_asset_status_raw",
    "source_department_code": "nearest_exact_line_source_department_code",
    "source_edition": "nearest_exact_line_source_edition",
    "source_archive_sha256": "nearest_exact_line_source_archive_sha256",
}
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` (value reference), `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).

#### `_POST_OUTPUT_MAPPING`

```python
_POST_OUTPUT_MAPPING = {
    "distance_m": "nearest_post_proxy_distance_m",
    "grid_feature_id": "nearest_post_grid_feature_id",
    "source_feature_id": "nearest_post_source_feature_id",
    "tie_count": "nearest_post_tie_count",
    "name": "nearest_post_name",
    "importance_raw": "nearest_post_importance_raw",
    "asset_status_raw": "nearest_post_asset_status_raw",
    "source_department_code": "nearest_post_source_department_code",
    "source_edition": "nearest_post_source_edition",
    "source_archive_sha256": "nearest_post_source_archive_sha256",
}
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately. Consumers include `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` (value reference), `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `GridProximityError`

**Purpose:** Raised when grid-proximity inputs or results are unsafe.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validated_crs` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_require_lambert93` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_active_geometry` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_id_values` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_parcels` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_grid` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_nearest_feature_rows` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_distance_values` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_tie_counts` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_match_integrity` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_coverage` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_table` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_exact_representation_consistency` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_validate_output_integrity` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `GridProximityError`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_distance_profile` via `GridProximityError`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `pytest.raises(GridProximityError, match='IgnBdTopoElectricityData|electricity source')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `pytest.raises(GridProximityError, match='parcel_id')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `pytest.raises(GridProximityError, match='Polygon|MultiPolygon')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `pytest.raises(GridProximityError, match='CRS')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `pytest.raises(GridProximityError, match='2154')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `pytest.raises(GridProximityError, match='grid_feature_type')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `pytest.raises(GridProximityError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `pytest.raises(GridProximityError, match='PROXY_GEOMETRY')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `pytest.raises(GridProximityError, match='geometry types')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `pytest.raises(GridProximityError, match=column)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `pytest.raises(GridProximityError, match='parcel_id')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `pytest.raises(GridProximityError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `pytest.raises(GridProximityError, match=message)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_voltage_cartesian_row` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_duplicate_parcel_voltage_pair` via `pytest.raises(GridProximityError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_voltage_rows_out_of_parcel_order` via `pytest.raises(GridProximityError, match='exact parcel set')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_distance` via `pytest.raises(GridProximityError, match='exact-line distance')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_identity` via `pytest.raises(GridProximityError, match='inconsistent')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_metadata` via `pytest.raises(GridProximityError, match='inconsistent')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_tie_count` via `pytest.raises(GridProximityError, match='tie count')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_tie_count` via `pytest.raises(GridProximityError, match='tie_count|match')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_tie_count` via `pytest.raises(GridProximityError, match='tie_count|match')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_main_match_feature_id` via `pytest.raises(GridProximityError, match='require')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_distance` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_exact_match_voltage` via `pytest.raises(GridProximityError, match='voltage|match')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_result_parcel_id` via `pytest.raises(GridProximityError, match='parcel_id')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_required_proximity_column` via `pytest.raises(GridProximityError, match='Missing proximity')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nondeterministic_or_duplicate_coverage` via `pytest.raises(GridProximityError, match='coverage')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_level` via `pytest.raises(GridProximityError, match='coverage')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_feature_count` via `pytest.raises(GridProximityError, match='line_feature_count')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_long_table_voltage` via `pytest.raises(GridProximityError, match='Voltage proximity')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_long_table_match_lineage` via `pytest.raises(GridProximityError, match='require')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_distance` via `pytest.raises(GridProximityError)`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `pytest.raises(GridProximityError, match='unmatched|entirely')`.
- expected exception type: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `pytest.raises(GridProximityError, match='No VALID')`.

**Exact class source**

```python
class GridProximityError(ValueError):
    """Raised when grid-proximity inputs or results are unsafe."""
```

### `VoltageLevelCoverage`

**Purpose:** Source-line coverage for one dynamically observed exact voltage.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `voltage_kv` | `voltage_kv: float` | Parsed or profiled voltage level in kilovolts. |
| `line_feature_count` | `line_feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::GridCoverageAssessmentResult` via `VoltageLevelCoverage`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::GridProximityResult` via `VoltageLevelCoverage`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_coverage` via `VoltageLevelCoverage`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_table` via `VoltageLevelCoverage`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::_voltage_level_table` via `VoltageLevelCoverage`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_voltage_level_table` via `VoltageLevelCoverage`.
- constructor call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_level` via `VoltageLevelCoverage`.
- constructor call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_feature_count` via `VoltageLevelCoverage`.

**Exact class source**

```python
class VoltageLevelCoverage:
    """Source-line coverage for one dynamically observed exact voltage."""

    voltage_kv: float
    line_feature_count: int
```

### `GridProximityResult`

**Purpose:** Parcel enrichment and dynamic exact-voltage proximity output.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `voltage_level_proximity` | `voltage_level_proximity: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `voltage_level_coverage` | `voltage_level_coverage: tuple[VoltageLevelCoverage, ...]` | Structured `voltage level coverage` collection owned by `GridProximityResult`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_validate_proximity_source_identity` via `GridProximityResult`.
- constructor call: `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` via `GridProximityResult`.
- type annotation: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `GridProximityResult`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `GridProximityResult`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::_validate_output_integrity` via `GridProximityResult`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `GridProximityResult`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `GridProximityResult`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `GridProximityResult`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::profile_grid_proximity` via `GridProximityResult`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `GridProximityResult`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_mutate_parcel_result` via `GridProximityResult`.
- type annotation: `tests/unit/test_enrich_grid_proximity.py::_mutate_voltage_result` via `GridProximityResult`.

**Exact class source**

```python
class GridProximityResult:
    """Parcel enrichment and dynamic exact-voltage proximity output."""

    parcels: gpd.GeoDataFrame
    voltage_level_proximity: pd.DataFrame
    voltage_level_coverage: tuple[VoltageLevelCoverage, ...]
```

### `DistanceProfile`

**Purpose:** Threshold-free distribution summary for one distance field.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `count` | `count: int` | Number of observations included in this deterministic diagnostic profile. |
| `missing_count` | `missing_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `minimum` | `minimum: float \| None` | Minimum finite observed distance/metric in this diagnostic profile. |
| `p01` | `p01: float \| None` | First percentile of the finite diagnostic distance distribution. |
| `p05` | `p05: float \| None` | Fifth percentile of the finite diagnostic distance distribution. |
| `p10` | `p10: float \| None` | Tenth percentile of the finite diagnostic distance distribution. |
| `p25` | `p25: float \| None` | Twenty-fifth percentile of the finite diagnostic distance distribution. |
| `p50` | `p50: float \| None` | Median of the finite diagnostic distance distribution. |
| `p75` | `p75: float \| None` | Seventy-fifth percentile of the finite diagnostic distance distribution. |
| `p90` | `p90: float \| None` | Ninetieth percentile of the finite diagnostic distance distribution. |
| `p95` | `p95: float \| None` | Ninety-fifth percentile of the finite diagnostic distance distribution. |
| `p99` | `p99: float \| None` | Ninety-ninth percentile of the finite diagnostic distance distribution. |
| `maximum` | `maximum: float \| None` | Maximum finite observed distance/metric in this diagnostic profile. |
| `zero_distance_count` | `zero_distance_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `tie_count` | `tie_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::VoltageLevelDistanceProfile` via `DistanceProfile`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::GridProximityProfile` via `DistanceProfile`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::_distance_profile` via `DistanceProfile`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::_distance_profile` via `DistanceProfile`.

**Exact class source**

```python
class DistanceProfile:
    """Threshold-free distribution summary for one distance field."""

    count: int
    missing_count: int
    minimum: float | None
    p01: float | None
    p05: float | None
    p10: float | None
    p25: float | None
    p50: float | None
    p75: float | None
    p90: float | None
    p95: float | None
    p99: float | None
    maximum: float | None
    zero_distance_count: int
    tie_count: int
```

### `VoltageLevelDistanceProfile`

**Purpose:** Distance distribution and source coverage for one exact voltage.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `voltage_kv` | `voltage_kv: float` | Parsed or profiled voltage level in kilovolts. |
| `line_feature_count` | `line_feature_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `parcel_proximity_count` | `parcel_proximity_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `distance` | `distance: DistanceProfile` | Distance-profile statistics for the owning voltage level or proximity category. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::GridProximityProfile` via `VoltageLevelDistanceProfile`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::profile_grid_proximity` via `VoltageLevelDistanceProfile`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::profile_grid_proximity` via `VoltageLevelDistanceProfile`.

**Exact class source**

```python
class VoltageLevelDistanceProfile:
    """Distance distribution and source coverage for one exact voltage."""

    voltage_kv: float
    line_feature_count: int
    parcel_proximity_count: int
    distance: DistanceProfile
```

### `GridProximityProfile`

**Purpose:** Threshold-free parcel and voltage-level proximity profiles.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcel_count` | `parcel_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `nearest_line` | `nearest_line: DistanceProfile` | Diagnostic profile for nearest eligible electricity-line proxy distances. |
| `nearest_exact_line` | `nearest_exact_line: DistanceProfile` | Diagnostic profile for nearest exact-voltage electricity-line proxy distances. |
| `nearest_post` | `nearest_post: DistanceProfile` | Diagnostic profile for nearest transformation-post proxy distances. |
| `voltage_levels` | `voltage_levels: tuple[VoltageLevelDistanceProfile, ...]` | Structured `voltage levels` collection owned by `GridProximityProfile`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- type annotation: `src/landscout/stages/enrich_grid_proximity.py::profile_grid_proximity` via `GridProximityProfile`.
- constructor call: `src/landscout/stages/enrich_grid_proximity.py::profile_grid_proximity` via `GridProximityProfile`.

**Exact class source**

```python
class GridProximityProfile:
    """Threshold-free parcel and voltage-level proximity profiles."""

    parcel_count: int
    nearest_line: DistanceProfile
    nearest_exact_line: DistanceProfile
    nearest_post: DistanceProfile
    voltage_levels: tuple[VoltageLevelDistanceProfile, ...]
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
- Explicit raise expressions: `GridProximityError(f'{label} CRS is required')`, `GridProximityError(f'{label} CRS is unreadable')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_require_lambert93` via `_validated_crs`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_parcels` via `_validated_crs`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_output_integrity` via `_validated_crs`.

**Complete source-ordered implementation**

```python
def _validated_crs(value: object, label: str) -> CRS:
    if value is None:
        raise GridProximityError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise GridProximityError(f"{label} CRS is unreadable") from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_require_lambert93`

**Exact signature**

```python
def _require_lambert93(value: object, label: str) -> None:
```

**Purpose**

Private `grid/source` helper for require lambert93; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not actual.is_projected or not actual.equals(expected)`.
- Explicit raise expressions: `GridProximityError(f'{label} must use EPSG:2154')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_grid` via `_require_lambert93`.

**Complete source-ordered implementation**

```python
def _require_lambert93(value: object, label: str) -> None:
    actual = _validated_crs(value, label)
    expected = CRS.from_epsg(2154)
    if not actual.is_projected or not actual.equals(expected):
        raise GridProximityError(f"{label} must use EPSG:2154")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_active_geometry`

**Exact signature**

```python
def _validate_active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent active geometry; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `'geometry' not in frame.columns`.
- Guard with a raise path: `frame.active_geometry_name != 'geometry'`.
- Explicit raise expressions: `GridProximityError(f'{label} geometry column is required')`, `GridProximityError(f'{label} geometry column must be active')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_parcels` via `_validate_active_geometry`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_grid` via `_validate_active_geometry`.

**Complete source-ordered implementation**

```python
def _validate_active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise GridProximityError(f"{label} geometry column is required")
    if frame.active_geometry_name != "geometry":
        raise GridProximityError(f"{label} geometry column must be active")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_id_values`

**Exact signature**

```python
def _validate_id_values(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent id values; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `values.isna().any()`.
- Guard with a raise path: `any((not isinstance(value, str) for value in raw_values))`.
- Guard with a raise path: `any((not value.strip() for value in raw_values))`.
- Guard with a raise path: `any((value != value.strip() for value in raw_values))`.
- Guard with a raise path: `require_unique and values.duplicated().any()`.
- Explicit raise expressions: `GridProximityError(f'{label} values must be strings')`, `GridProximityError(f'{label} values must be unique')`, `GridProximityError(f'{label} values must not be empty')`, `GridProximityError(f'{label} values must not be null')`, `GridProximityError(f'{label} values must not contain leading or trailing whitespace')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_parcels` via `_validate_id_values`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_table` via `_validate_id_values`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_exact_representation_consistency` via `_validate_id_values`.

**Complete source-ordered implementation**

```python
def _validate_id_values(
    values: pd.Series,
    label: str,
    *,
    require_unique: bool,
) -> None:
    if values.isna().any():
        raise GridProximityError(f"{label} values must not be null")
    raw_values = values.tolist()
    if any(not isinstance(value, str) for value in raw_values):
        raise GridProximityError(f"{label} values must be strings")
    if any(not value.strip() for value in raw_values):
        raise GridProximityError(f"{label} values must not be empty")
    if any(value != value.strip() for value in raw_values):
        raise GridProximityError(
            f"{label} values must not contain leading or trailing whitespace"
        )
    if require_unique and values.duplicated().any():
        raise GridProximityError(f"{label} values must be unique")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_parcels`

**Exact signature**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
```

**Purpose**

Rejects malformed or inconsistent parcels; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
source_crs
```

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `parcels.geometry.isna().any()`.
- Guard with a raise path: `parcels.geometry.is_empty.any()`.
- Guard with a raise path: `not parcels.geometry.is_valid.all()`.
- Guard with a raise path: `unsupported`.
- Explicit raise expressions: `GridProximityError('Missing required parcel columns: ' + ', '.join(sorted(missing)))`, `GridProximityError('Parcel geometries must be Polygon or MultiPolygon; found: ' + ', '.join(unsupported))`, `GridProximityError('Parcel geometries must be valid')`, `GridProximityError('Parcel geometries must not be empty')`, `GridProximityError('Parcel geometries must not be null')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_validate_active_geometry`, `parcels.geometry.geom_type.dropna`, `parcels.geometry.is_empty.any`, `parcels.geometry.is_valid.all`, `parcels.geometry.isna`, `parcels.geometry.isna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_validate_parcels`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_validate_parcels`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `_validate_parcels`.

**Complete source-ordered implementation**

```python
def _validate_parcels(parcels: gpd.GeoDataFrame) -> CRS:
    missing = PARCEL_REQUIRED_COLUMNS - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing required parcel columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(parcels, "Parcel")
    source_crs = _validated_crs(parcels.crs, "Parcel")
    _validate_id_values(parcels["parcel_id"], "parcel_id", require_unique=True)
    if parcels.geometry.isna().any():
        raise GridProximityError("Parcel geometries must not be null")
    if parcels.geometry.is_empty.any():
        raise GridProximityError("Parcel geometries must not be empty")
    if not parcels.geometry.is_valid.all():
        raise GridProximityError("Parcel geometries must be valid")
    geometry_types = set(parcels.geometry.geom_type.dropna())
    unsupported = sorted(
        str(value) for value in geometry_types - PARCEL_GEOMETRY_TYPES
    )
    if unsupported:
        raise GridProximityError(
            "Parcel geometries must be Polygon or MultiPolygon; found: "
            + ", ".join(unsupported)
        )
    return source_crs
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_observed_geometry_status`

**Exact signature**

```python
def _observed_geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
```

**Purpose**

Private `grid/source` helper for observed geometry status; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.Series`.
- Every observed return expression is reproduced without truncation:
```python
status
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `geometry.isna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `status.loc[empty_mask]`, `status.loc[invalid_mask]`, `status.loc[null_mask]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_grid` via `_observed_geometry_status`.

**Complete source-ordered implementation**

```python
def _observed_geometry_status(geometry: gpd.GeoSeries) -> pd.Series:
    status = pd.Series("VALID", index=geometry.index, dtype="object")
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    status.loc[null_mask] = "NULL"
    status.loc[empty_mask] = "EMPTY"
    status.loc[invalid_mask] = "INVALID"
    return status
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_grid`

**Exact signature**

```python
def _validate_grid(
    frame: gpd.GeoDataFrame,
    *,
    label: str,
    required_columns: frozenset[str],
    feature_type: str,
    allowed_geometry_types: frozenset[str],
) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent grid; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame.loc[valid_mask].reset_index(drop=True).copy()
```

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `identifiers.isna().any()`.
- Guard with a raise path: `any((not isinstance(value, str) or not value for value in identifiers.tolist()))`.
- Guard with a raise path: `identifiers.duplicated().any()`.
- Guard with a raise path: `frame['grid_feature_type'].isna().any() or not frame['grid_feature_type'].eq(feature_type).all()`.
- Guard with a raise path: `frame['spatial_role'].isna().any() or not frame['spatial_role'].eq(SPATIAL_ROLE).all()`.
- Guard with a raise path: `declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES`.
- Guard with a raise path: `not declared_status.astype('object').equals(observed_status)`.
- Guard with a raise path: `unsupported`.
- Explicit raise expressions: `GridProximityError(f'Missing required {label} columns: ' + ', '.join(sorted(missing)))`, `GridProximityError(f'{label} geometry_status does not match the source geometry')`, `GridProximityError(f'{label} grid_feature_id values must be non-empty strings')`, `GridProximityError(f'{label} grid_feature_id values must be unique')`, `GridProximityError(f'{label} grid_feature_id values must not be null')`, `GridProximityError(f'{label} grid_feature_type must be {feature_type}')`, `GridProximityError(f'{label} has unexpected geometry_status values')`, `GridProximityError(f'{label} has unsupported VALID geometry types: ' + ', '.join(unsupported))`, `GridProximityError(f'{label} spatial_role must be PROXY_GEOMETRY')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_observed_geometry_status`, `_validate_active_geometry`, `frame.loc[valid_mask, 'geometry'].geom_type.dropna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_validate_grid`.

**Complete source-ordered implementation**

```python
def _validate_grid(
    frame: gpd.GeoDataFrame,
    *,
    label: str,
    required_columns: frozenset[str],
    feature_type: str,
    allowed_geometry_types: frozenset[str],
) -> gpd.GeoDataFrame:
    missing = required_columns - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing required {label} columns: " + ", ".join(sorted(missing))
        )
    _validate_active_geometry(frame, label)
    _require_lambert93(frame.crs, label)

    identifiers = frame["grid_feature_id"]
    if identifiers.isna().any():
        raise GridProximityError(f"{label} grid_feature_id values must not be null")
    if any(not isinstance(value, str) or not value for value in identifiers.tolist()):
        raise GridProximityError(
            f"{label} grid_feature_id values must be non-empty strings"
        )
    if identifiers.duplicated().any():
        raise GridProximityError(f"{label} grid_feature_id values must be unique")
    if frame["grid_feature_type"].isna().any() or not frame[
        "grid_feature_type"
    ].eq(feature_type).all():
        raise GridProximityError(
            f"{label} grid_feature_type must be {feature_type}"
        )
    if frame["spatial_role"].isna().any() or not frame["spatial_role"].eq(
        SPATIAL_ROLE
    ).all():
        raise GridProximityError(f"{label} spatial_role must be PROXY_GEOMETRY")

    declared_status = frame["geometry_status"]
    observed_status = _observed_geometry_status(frame.geometry)
    declared_values = set(declared_status.dropna().unique())
    if declared_status.isna().any() or not declared_values <= GRID_GEOMETRY_STATUSES:
        raise GridProximityError(f"{label} has unexpected geometry_status values")
    if not declared_status.astype("object").equals(observed_status):
        raise GridProximityError(
            f"{label} geometry_status does not match the source geometry"
        )

    valid_mask = declared_status == "VALID"
    valid_types = set(frame.loc[valid_mask, "geometry"].geom_type.dropna())
    unsupported = sorted(str(value) for value in valid_types - allowed_geometry_types)
    if unsupported:
        raise GridProximityError(
            f"{label} has unsupported VALID geometry types: "
            + ", ".join(unsupported)
        )
    return frame.loc[valid_mask].reset_index(drop=True).copy()
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_finite_real_as_float`

**Exact signature**

```python
def _finite_real_as_float(value: object) -> float | None:
```

**Purpose**

Private `grid/source` helper for finite real as float; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float | None`.
- Every observed return expression is reproduced without truncation:
```python
numeric if isfinite(numeric) else None

None

None
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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_is_positive_finite_number` via `_finite_real_as_float`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_distance_values` via `_finite_real_as_float`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_tie_counts` via `_finite_real_as_float`.

**Complete source-ordered implementation**

```python
def _finite_real_as_float(value: object) -> float | None:
    if not isinstance(value, Real) or isinstance(value, bool):
        return None
    try:
        numeric = float(value)
    except (OverflowError, TypeError, ValueError):
        return None
    return numeric if isfinite(numeric) else None
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_is_positive_finite_number`

**Exact signature**

```python
def _is_positive_finite_number(value: object) -> bool:
```

**Purpose**

Tests whether positive finite number; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
numeric is not None and numeric > 0
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

- function object argument: `src/landscout/stages/enrich_grid_proximity.py::_validate_match_integrity` via `frame[voltage_column].map(_is_positive_finite_number)`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_coverage` via `_is_positive_finite_number`.
- function object argument: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_table` via `raw_voltage_values.map(_is_positive_finite_number)`.
- function object argument: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `valid_lines['voltage_kv'].map(_is_positive_finite_number)`.

**Complete source-ordered implementation**

```python
def _is_positive_finite_number(value: object) -> bool:
    numeric = _finite_real_as_float(value)
    return numeric is not None and numeric > 0
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_calculation_geometries`

**Exact signature**

```python
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
```

**Purpose**

Private `grid/source` helper for calculation geometries; its complete implementation below is the authoritative behavioral contract.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_nearest_feature_rows` via `_calculation_geometries`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_calculation_geometries`.

**Complete source-ordered implementation**

```python
def _calculation_geometries(frame: gpd.GeoDataFrame) -> np.ndarray:
    values = np.asarray(frame.geometry.array, dtype=object)
    return np.asarray(force_2d(values), dtype=object)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_empty_nearest_result`

**Exact signature**

```python
def _empty_nearest_result(
    parcel_count: int,
    attribute_columns: tuple[str, ...],
) -> pd.DataFrame:
```

**Purpose**

Private `grid/source` helper for empty nearest result; its complete implementation below is the authoritative behavioral contract.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_nearest_feature_rows` via `_empty_nearest_result`.

**Complete source-ordered implementation**

```python
def _empty_nearest_result(
    parcel_count: int,
    attribute_columns: tuple[str, ...],
) -> pd.DataFrame:
    output = pd.DataFrame(index=pd.RangeIndex(parcel_count))
    output["distance_m"] = pd.Series(np.nan, index=output.index, dtype="float64")
    output["tie_count"] = pd.Series(pd.NA, index=output.index, dtype="Int64")
    for column in attribute_columns:
        if column in {"voltage_kv", "voltage_upper_bound_kv"}:
            output[column] = pd.Series(np.nan, index=output.index, dtype="float64")
        else:
            output[column] = pd.Series(pd.NA, index=output.index, dtype="object")
    return output
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_nearest_feature_rows`

**Exact signature**

```python
def _nearest_feature_rows(
    parcel_geometries: np.ndarray,
    features: gpd.GeoDataFrame,
    attribute_columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> pd.DataFrame:
```

**Purpose**

Private `grid/source` helper for nearest feature rows; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output

_empty_nearest_result(parcel_count, attribute_columns)
```

**Validation and exceptions**

- Guard with a raise path: `features.empty`.
- Guard with a raise path: `selected['parcel_position'].tolist() != list(range(parcel_count))`.
- Explicit raise expressions: `GridProximityError('Nearest-neighbour matching did not cover every parcel')`, `GridProximityError('No VALID grid proxy feature is available')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `STRtree`, `selected['distance_m'].to_numpy`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `matches['grid_feature_id']`, `output`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_voltage_level_table` via `_nearest_feature_rows`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_nearest_feature_rows`.

**Complete source-ordered implementation**

```python
def _nearest_feature_rows(
    parcel_geometries: np.ndarray,
    features: gpd.GeoDataFrame,
    attribute_columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> pd.DataFrame:
    parcel_count = len(parcel_geometries)
    if features.empty:
        if allow_empty:
            return _empty_nearest_result(parcel_count, attribute_columns)
        raise GridProximityError("No VALID grid proxy feature is available")

    feature_geometries = _calculation_geometries(features)
    tree = STRtree(feature_geometries)
    indices, distances = tree.query_nearest(
        parcel_geometries,
        all_matches=True,
        return_distance=True,
    )
    matches = pd.DataFrame(
        {
            "parcel_position": indices[0],
            "feature_position": indices[1],
            "distance_m": distances,
        }
    )
    matches["grid_feature_id"] = features.iloc[
        matches["feature_position"].to_numpy()
    ]["grid_feature_id"].to_numpy()
    matches = matches.sort_values(
        ["parcel_position", "distance_m", "grid_feature_id"],
        kind="mergesort",
    )
    ties = matches.groupby("parcel_position", sort=False).size()
    selected = matches.drop_duplicates("parcel_position", keep="first").sort_values(
        "parcel_position"
    )
    if selected["parcel_position"].tolist() != list(range(parcel_count)):
        raise GridProximityError("Nearest-neighbour matching did not cover every parcel")

    feature_positions = selected["feature_position"].to_numpy()
    output = features.iloc[feature_positions].loc[:, list(attribute_columns)].copy()
    output = output.reset_index(drop=True)
    output.insert(0, "tie_count", ties.reindex(range(parcel_count)).to_numpy())
    output.insert(0, "distance_m", selected["distance_m"].to_numpy(dtype="float64"))
    return output
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_attach_matches`

**Exact signature**

```python
def _attach_matches(
    parcels: gpd.GeoDataFrame,
    matches: pd.DataFrame,
    mapping: dict[str, str],
) -> None:
```

**Purpose**

Private `grid/source` helper for attach matches; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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
- In-memory mutation: `parcels[output_column]`.
- Input mutation: `parcels[output_column]`.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_attach_matches`.

**Complete source-ordered implementation**

```python
def _attach_matches(
    parcels: gpd.GeoDataFrame,
    matches: pd.DataFrame,
    mapping: dict[str, str],
) -> None:
    for source_column, output_column in mapping.items():
        parcels[output_column] = matches[source_column].reset_index(drop=True)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_distance_values`

**Exact signature**

```python
def _validate_distance_values(values: pd.Series, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent distance values; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((value is None for value in numeric_values))`.
- Guard with a raise path: `(numeric < 0).any()`.
- Explicit raise expressions: `GridProximityError(f'{label} distances must be finite and >= 0')`, `GridProximityError(f'{label} distances must be numeric and finite')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_match_integrity` via `_validate_distance_values`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_distance_profile` via `_validate_distance_values`.

**Complete source-ordered implementation**

```python
def _validate_distance_values(values: pd.Series, label: str) -> None:
    non_null = values.dropna()
    numeric_values = [
        _finite_real_as_float(value) for value in non_null.tolist()
    ]
    if any(value is None for value in numeric_values):
        raise GridProximityError(f"{label} distances must be numeric and finite")
    numeric = np.asarray(numeric_values, dtype="float64")
    if (numeric < 0).any():
        raise GridProximityError(f"{label} distances must be finite and >= 0")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

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
bool(pd.isna(value))

True

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_tie_counts` via `_is_missing_scalar`.

**Complete source-ordered implementation**

```python
def _is_missing_scalar(value: object) -> bool:
    if value is None:
        return True
    if not is_scalar(value):
        return False
    return bool(pd.isna(value))
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_tie_counts`

**Exact signature**

```python
def _validate_tie_counts(
    values: pd.Series,
    matched: pd.Series,
    label: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent tie counts; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `len(values) != len(matched)`.
- Guard with a raise path: `not row_is_matched`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `numeric is None or not numeric.is_integer() or numeric < 1`.
- Guard with a raise path: `not missing`.
- Explicit raise expressions: `GridProximityError(f'{label} matched rows require tie_count')`, `GridProximityError(f'{label} tie-count state is inconsistent')`, `GridProximityError(f'{label} tie_count must be a finite integer >= 1')`, `GridProximityError(f'{label} unmatched rows must have null tie_count')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_match_integrity` via `_validate_tie_counts`.

**Complete source-ordered implementation**

```python
def _validate_tie_counts(
    values: pd.Series,
    matched: pd.Series,
    label: str,
) -> None:
    if len(values) != len(matched):
        raise GridProximityError(f"{label} tie-count state is inconsistent")
    for value, row_is_matched in zip(
        values.tolist(), matched.to_numpy(dtype="bool"), strict=True
    ):
        missing = _is_missing_scalar(value)
        if not row_is_matched:
            if not missing:
                raise GridProximityError(
                    f"{label} unmatched rows must have null tie_count"
                )
            continue
        if missing:
            raise GridProximityError(f"{label} matched rows require tie_count")
        numeric = _finite_real_as_float(value)
        if numeric is None or not numeric.is_integer() or numeric < 1:
            raise GridProximityError(
                f"{label} tie_count must be a finite integer >= 1"
            )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_match_integrity`

**Exact signature**

```python
def _validate_match_integrity(
    frame: pd.DataFrame,
    *,
    label: str,
    distance_column: str,
    grid_id_column: str,
    source_id_column: str,
    tie_column: str,
    expect_matches: bool,
    voltage_column: str | None = None,
    unmatched_null_columns: tuple[str, ...] = (),
) -> None:
```

**Purpose**

Rejects malformed or inconsistent match integrity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
None
```

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `expect_matches and (not matched.all())`.
- Guard with a raise path: `not expect_matches and matched.any()`.
- Guard with a raise path: `expect_matches`.
- Guard with a raise path: `voltage_column is not None and (not frame[voltage_column].map(_is_positive_finite_number).all())`.
- Guard with a raise path: `column not in frame.columns`.
- Guard with a raise path: `frame[column].notna().any()`.
- Guard with a raise path: `frame[column].isna().any()`.
- Explicit raise expressions: `GridProximityError(f'Missing {label} match column: {column}')`, `GridProximityError(f'Missing {label} match columns: ' + ', '.join(sorted(missing)))`, `GridProximityError(f'{label} matched rows require {column}')`, `GridProximityError(f'{label} must be entirely unmatched')`, `GridProximityError(f'{label} requires a match for every parcel')`, `GridProximityError(f'{label} unmatched rows must have null {column}')`, `GridProximityError(f'{label} voltage must be numeric, finite, and > 0')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_validate_distance_values`, `distance.notna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `null_columns`, `required`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_table` via `_validate_match_integrity`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_validate_match_integrity`.

**Complete source-ordered implementation**

```python
def _validate_match_integrity(
    frame: pd.DataFrame,
    *,
    label: str,
    distance_column: str,
    grid_id_column: str,
    source_id_column: str,
    tie_column: str,
    expect_matches: bool,
    voltage_column: str | None = None,
    unmatched_null_columns: tuple[str, ...] = (),
) -> None:
    required = {distance_column, grid_id_column, source_id_column, tie_column}
    if voltage_column is not None:
        required.add(voltage_column)
    missing = required - set(frame.columns)
    if missing:
        raise GridProximityError(
            f"Missing {label} match columns: " + ", ".join(sorted(missing))
        )

    distance = frame[distance_column]
    matched = distance.notna()
    if expect_matches and not matched.all():
        raise GridProximityError(f"{label} requires a match for every parcel")
    if not expect_matches and matched.any():
        raise GridProximityError(f"{label} must be entirely unmatched")
    _validate_distance_values(distance, label)
    _validate_tie_counts(frame[tie_column], matched, label)

    id_columns = (grid_id_column, source_id_column)
    if expect_matches:
        for column in id_columns:
            if frame[column].isna().any():
                raise GridProximityError(f"{label} matched rows require {column}")
        if voltage_column is not None and not frame[voltage_column].map(
            _is_positive_finite_number
        ).all():
            raise GridProximityError(
                f"{label} voltage must be numeric, finite, and > 0"
            )
        return

    null_columns = set(unmatched_null_columns) | set(id_columns)
    if voltage_column is not None:
        null_columns.add(voltage_column)
    for column in null_columns:
        if column not in frame.columns:
            raise GridProximityError(f"Missing {label} match column: {column}")
        if frame[column].notna().any():
            raise GridProximityError(
                f"{label} unmatched rows must have null {column}"
            )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_voltage_coverage`

**Exact signature**

```python
def _validate_voltage_coverage(
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
```

**Purpose**

Rejects malformed or inconsistent voltage coverage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[float, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(levels)
```

**Validation and exceptions**

- Guard with a raise path: `len(set(levels)) != len(levels)`.
- Guard with a raise path: `levels != sorted(levels)`.
- Guard with a raise path: `not isinstance(item, VoltageLevelCoverage)`.
- Guard with a raise path: `not _is_positive_finite_number(item.voltage_kv)`.
- Guard with a raise path: `not isinstance(item.line_feature_count, Integral) or isinstance(item.line_feature_count, bool) or item.line_feature_count <= 0`.
- Explicit raise expressions: `GridProximityError('Voltage coverage entries are invalid')`, `GridProximityError('Voltage coverage levels must be ascending')`, `GridProximityError('Voltage coverage levels must be numeric, finite, and > 0')`, `GridProximityError('Voltage coverage levels must be unique')`, `GridProximityError('Voltage coverage line_feature_count must be an integer > 0')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `levels`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_voltage_table` via `_validate_voltage_coverage`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_validate_voltage_coverage`.

**Complete source-ordered implementation**

```python
def _validate_voltage_coverage(
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    levels: list[float] = []
    for item in coverage:
        if not isinstance(item, VoltageLevelCoverage):
            raise GridProximityError("Voltage coverage entries are invalid")
        if not _is_positive_finite_number(item.voltage_kv):
            raise GridProximityError(
                "Voltage coverage levels must be numeric, finite, and > 0"
            )
        if (
            not isinstance(item.line_feature_count, Integral)
            or isinstance(item.line_feature_count, bool)
            or item.line_feature_count <= 0
        ):
            raise GridProximityError(
                "Voltage coverage line_feature_count must be an integer > 0"
            )
        levels.append(float(item.voltage_kv))
    if len(set(levels)) != len(levels):
        raise GridProximityError("Voltage coverage levels must be unique")
    if levels != sorted(levels):
        raise GridProximityError("Voltage coverage levels must be ascending")
    return tuple(levels)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_voltage_table`

**Exact signature**

```python
def _validate_voltage_table(
    table: pd.DataFrame,
    parcel_ids: pd.Series,
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
```

**Purpose**

Rejects malformed or inconsistent voltage table; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[float, ...]`.
- Every observed return expression is reproduced without truncation:
```python
levels

levels
```

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `len(table) != expected_rows`.
- Guard with a raise path: `not raw_voltage_values.map(_is_positive_finite_number).all()`.
- Guard with a raise path: `table.duplicated(['parcel_id', 'voltage_kv']).any()`.
- Guard with a raise path: `table_levels != levels`.
- Guard with a raise path: `len(rows) != len(expected_ids) or rows['parcel_id'].tolist() != expected_ids`.
- Guard with a raise path: `table[column].isna().any()`.
- Explicit raise expressions: `GridProximityError('Missing voltage proximity columns: ' + ', '.join(sorted(missing)))`, `GridProximityError('Voltage proximity levels do not match source coverage')`, `GridProximityError('Voltage proximity levels must be numeric, finite, and > 0')`, `GridProximityError('Voltage proximity parcel/voltage pairs must be unique')`, `GridProximityError('Voltage proximity row count is inconsistent')`, `GridProximityError(f'Voltage proximity does not contain the exact parcel set for {voltage_kv:g} kV')`, `GridProximityError(f'Voltage-level matched rows require {column}')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_validate_voltage_table`.

**Complete source-ordered implementation**

```python
def _validate_voltage_table(
    table: pd.DataFrame,
    parcel_ids: pd.Series,
    coverage: tuple[VoltageLevelCoverage, ...],
) -> tuple[float, ...]:
    missing = set(VOLTAGE_PROXIMITY_COLUMNS) - set(table.columns)
    if missing:
        raise GridProximityError(
            "Missing voltage proximity columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(coverage)
    expected_rows = len(parcel_ids) * len(levels)
    if len(table) != expected_rows:
        raise GridProximityError("Voltage proximity row count is inconsistent")
    if table.empty:
        return levels

    _validate_id_values(table["parcel_id"], "parcel_id", require_unique=False)
    raw_voltage_values = table["voltage_kv"]
    if not raw_voltage_values.map(_is_positive_finite_number).all():
        raise GridProximityError(
            "Voltage proximity levels must be numeric, finite, and > 0"
        )
    if table.duplicated(["parcel_id", "voltage_kv"]).any():
        raise GridProximityError("Voltage proximity parcel/voltage pairs must be unique")
    table_levels = tuple(
        sorted({float(value) for value in raw_voltage_values.tolist()})
    )
    if table_levels != levels:
        raise GridProximityError(
            "Voltage proximity levels do not match source coverage"
        )

    expected_ids = parcel_ids.tolist()
    for voltage_kv in levels:
        rows = table.loc[raw_voltage_values.map(float) == voltage_kv]
        if len(rows) != len(expected_ids) or rows["parcel_id"].tolist() != expected_ids:
            raise GridProximityError(
                f"Voltage proximity does not contain the exact parcel set for {voltage_kv:g} kV"
            )

    _validate_match_integrity(
        table,
        label="Voltage-level line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="tie_count",
        expect_matches=True,
    )
    for column in (
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    ):
        if table[column].isna().any():
            raise GridProximityError(
                f"Voltage-level matched rows require {column}"
            )
    return levels
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_null_safe_series_equal`

**Exact signature**

```python
def _null_safe_series_equal(actual: pd.Series, expected: pd.Series) -> bool:
```

**Purpose**

Private `grid/source` helper for null safe series equal; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
bool((both_null | equal_values).all())

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_exact_representation_consistency` via `_null_safe_series_equal`.

**Complete source-ordered implementation**

```python
def _null_safe_series_equal(actual: pd.Series, expected: pd.Series) -> bool:
    actual_values = actual.reset_index(drop=True)
    expected_values = expected.reset_index(drop=True)
    if len(actual_values) != len(expected_values):
        return False
    both_null = actual_values.isna() & expected_values.isna()
    try:
        equal_values = actual_values.eq(expected_values).fillna(False)
    except (TypeError, ValueError):
        return False
    return bool((both_null | equal_values).all())
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_exact_representation_consistency`

**Exact signature**

```python
def _validate_exact_representation_consistency(
    parcels: gpd.GeoDataFrame,
    voltage_table: pd.DataFrame,
    levels: tuple[float, ...],
) -> None:
```

**Purpose**

Rejects malformed or inconsistent exact representation consistency; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
None
```

**Validation and exceptions**

- Guard with a raise path: `candidates['_parcel_position'].isna().any()`.
- Guard with a raise path: `expected['parcel_id'].isna().any()`.
- Guard with a raise path: `not actual_distance.eq(expected['_distance'].reset_index(drop=True)).all()`.
- Guard with a raise path: `not actual_ties.eq(expected_ties.reset_index(drop=True)).all()`.
- Guard with a raise path: `not _null_safe_series_equal(actual[parcel_column], expected[table_column])`.
- Explicit raise expressions: `GridProximityError('Global exact-line distance is inconsistent with voltage-level proximity')`, `GridProximityError('Global exact-line tie count is inconsistent with voltage-level proximity')`, `GridProximityError('Voltage-level proximity contains an unexpected parcel ID')`, `GridProximityError('Voltage-level proximity does not cover every parcel')`, `GridProximityError(f'Global exact-line {parcel_column} is inconsistent with voltage-level proximity')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `actual['nearest_exact_line_proxy_distance_m'].map`, `actual_distance.eq`, `actual_distance.eq(expected['_distance'].reset_index(drop=True)).all`, `candidates.groupby('_parcel_position', sort=False)['_distance'].transform`, `candidates['_distance'].eq`, `candidates[distance_column].map`, `expected['_distance'].reset_index`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `candidates['_distance']`, `candidates['_parcel_position']`, `candidates['_tie_count']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_result_contract` via `_validate_exact_representation_consistency`.

**Complete source-ordered implementation**

```python
def _validate_exact_representation_consistency(
    parcels: gpd.GeoDataFrame,
    voltage_table: pd.DataFrame,
    levels: tuple[float, ...],
) -> None:
    if not levels:
        return

    distance_column = "nearest_line_proxy_distance_m"
    grid_id_column = "nearest_line_grid_feature_id"
    selected_columns = (
        "parcel_id",
        distance_column,
        grid_id_column,
        "nearest_line_source_feature_id",
        "voltage_kv",
        "tie_count",
        "manager_name",
        "asset_status_raw",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
    )
    candidates = voltage_table.loc[:, list(selected_columns)].copy()
    _validate_id_values(
        candidates[grid_id_column],
        "Voltage-level nearest grid_feature_id",
        require_unique=False,
    )
    parcel_positions = {
        parcel_id: position
        for position, parcel_id in enumerate(parcels["parcel_id"].tolist())
    }
    candidates["_parcel_position"] = candidates["parcel_id"].map(parcel_positions)
    if candidates["_parcel_position"].isna().any():
        raise GridProximityError(
            "Voltage-level proximity contains an unexpected parcel ID"
        )
    candidates["_distance"] = candidates[distance_column].map(float)
    candidates["_tie_count"] = candidates["tie_count"].map(int).astype("object")

    ordered = candidates.sort_values(
        ["_parcel_position", "_distance", grid_id_column],
        kind="mergesort",
    )
    expected = ordered.drop_duplicates("_parcel_position", keep="first")
    expected = expected.set_index("_parcel_position").reindex(range(len(parcels)))
    if expected["parcel_id"].isna().any():
        raise GridProximityError(
            "Voltage-level proximity does not cover every parcel"
        )

    minimum_distance = candidates.groupby("_parcel_position", sort=False)[
        "_distance"
    ].transform("min")
    tied_level_winners = candidates.loc[
        candidates["_distance"].eq(minimum_distance)
    ]
    expected_ties = tied_level_winners.groupby("_parcel_position", sort=False)[
        "_tie_count"
    ].agg(lambda values: sum(values.tolist()))
    expected_ties = expected_ties.reindex(range(len(parcels)))

    actual = parcels.reset_index(drop=True)
    actual_distance = actual["nearest_exact_line_proxy_distance_m"].map(float)
    if not actual_distance.eq(expected["_distance"].reset_index(drop=True)).all():
        raise GridProximityError(
            "Global exact-line distance is inconsistent with voltage-level proximity"
        )

    field_mapping = (
        ("nearest_exact_line_grid_feature_id", grid_id_column),
        ("nearest_exact_line_source_feature_id", "nearest_line_source_feature_id"),
        ("nearest_exact_line_voltage_kv", "voltage_kv"),
        ("nearest_exact_line_manager_name", "manager_name"),
        ("nearest_exact_line_asset_status_raw", "asset_status_raw"),
        ("nearest_exact_line_source_department_code", "source_department_code"),
        ("nearest_exact_line_source_edition", "source_edition"),
        ("nearest_exact_line_source_archive_sha256", "source_archive_sha256"),
    )
    for parcel_column, table_column in field_mapping:
        if not _null_safe_series_equal(
            actual[parcel_column], expected[table_column]
        ):
            raise GridProximityError(
                f"Global exact-line {parcel_column} is inconsistent with "
                "voltage-level proximity"
            )

    actual_ties = actual["nearest_exact_line_tie_count"].map(int)
    if not actual_ties.eq(expected_ties.reset_index(drop=True)).all():
        raise GridProximityError(
            "Global exact-line tie count is inconsistent with voltage-level proximity"
        )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_result_contract`

**Exact signature**

```python
def _validate_result_contract(result: GridProximityResult) -> tuple[float, ...]:
```

**Purpose**

Rejects malformed or inconsistent result contract; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[float, ...]`.
- Every observed return expression is reproduced without truncation:
```python
levels
```

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `levels and (not parcels['nearest_exact_line_voltage_kv'].map(float).isin(levels).all())`.
- Explicit raise expressions: `GridProximityError('Missing proximity result columns: ' + ', '.join(sorted(missing)))`, `GridProximityError('Nearest exact-line voltage does not match source coverage')`.

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

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_validate_output_integrity` via `_validate_result_contract`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::profile_grid_proximity` via `_validate_result_contract`.

**Complete source-ordered implementation**

```python
def _validate_result_contract(result: GridProximityResult) -> tuple[float, ...]:
    parcels = result.parcels
    _validate_parcels(parcels)
    required_proximity_columns = (
        set(_LINE_OUTPUT_MAPPING.values())
        | set(_EXACT_LINE_OUTPUT_MAPPING.values())
        | set(_POST_OUTPUT_MAPPING.values())
    )
    missing = required_proximity_columns - set(parcels.columns)
    if missing:
        raise GridProximityError(
            "Missing proximity result columns: " + ", ".join(sorted(missing))
        )
    levels = _validate_voltage_coverage(result.voltage_level_coverage)
    _validate_match_integrity(
        parcels,
        label="Nearest line proximity",
        distance_column="nearest_line_proxy_distance_m",
        grid_id_column="nearest_line_grid_feature_id",
        source_id_column="nearest_line_source_feature_id",
        tie_column="nearest_line_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest post proximity",
        distance_column="nearest_post_proxy_distance_m",
        grid_id_column="nearest_post_grid_feature_id",
        source_id_column="nearest_post_source_feature_id",
        tie_column="nearest_post_tie_count",
        expect_matches=True,
    )
    _validate_match_integrity(
        parcels,
        label="Nearest exact-line proximity",
        distance_column="nearest_exact_line_proxy_distance_m",
        grid_id_column="nearest_exact_line_grid_feature_id",
        source_id_column="nearest_exact_line_source_feature_id",
        tie_column="nearest_exact_line_tie_count",
        expect_matches=bool(levels),
        voltage_column="nearest_exact_line_voltage_kv",
        unmatched_null_columns=tuple(_EXACT_LINE_OUTPUT_MAPPING.values()),
    )
    if levels and not parcels["nearest_exact_line_voltage_kv"].map(float).isin(
        levels
    ).all():
        raise GridProximityError(
            "Nearest exact-line voltage does not match source coverage"
        )
    _validate_voltage_table(
        result.voltage_level_proximity,
        parcels["parcel_id"],
        result.voltage_level_coverage,
    )
    _validate_exact_representation_consistency(
        parcels,
        result.voltage_level_proximity,
        levels,
    )
    return levels
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_validate_output_integrity`

**Exact signature**

```python
def _validate_output_integrity(
    source_parcels: gpd.GeoDataFrame,
    result: GridProximityResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent output integrity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `len(output) != len(source_parcels)`.
- Guard with a raise path: `not source_ids.equals(output_ids)`.
- Guard with a raise path: `not source_crs.equals(output_crs)`.
- Guard with a raise path: `not output.geometry.geom_equals_exact(source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False).all()`.
- Explicit raise expressions: `GridProximityError('Enriched parcel CRS changed')`, `GridProximityError('Enriched parcel geometry changed')`, `GridProximityError('Grid proximity enrichment changed parcel IDs or order')`, `GridProximityError('Grid proximity enrichment changed parcel count')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `output.geometry.geom_equals_exact`, `output.geometry.geom_equals_exact(source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False).all`, `source_parcels.geometry.reset_index`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_validate_output_integrity`.

**Complete source-ordered implementation**

```python
def _validate_output_integrity(
    source_parcels: gpd.GeoDataFrame,
    result: GridProximityResult,
) -> None:
    _validate_result_contract(result)
    output = result.parcels
    if len(output) != len(source_parcels):
        raise GridProximityError("Grid proximity enrichment changed parcel count")
    source_ids = source_parcels["parcel_id"].reset_index(drop=True)
    output_ids = output["parcel_id"].reset_index(drop=True)
    if not source_ids.equals(output_ids):
        raise GridProximityError("Grid proximity enrichment changed parcel IDs or order")
    source_crs = _validated_crs(source_parcels.crs, "Input parcel")
    output_crs = _validated_crs(output.crs, "Output parcel")
    if not source_crs.equals(output_crs):
        raise GridProximityError("Enriched parcel CRS changed")
    if not output.geometry.geom_equals_exact(
        source_parcels.geometry.reset_index(drop=True), tolerance=0, align=False
    ).all():
        raise GridProximityError("Enriched parcel geometry changed")
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_voltage_level_table`

**Exact signature**

```python
def _voltage_level_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    exact_lines: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]:
```

**Purpose**

Private `grid/source` helper for voltage level table; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(pd.concat(tables, ignore_index=True), tuple(coverage))

(empty, ())
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `empty['nearest_line_proxy_distance_m'].astype`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `coverage`, `empty['nearest_line_proxy_distance_m']`, `empty['tie_count']`, `empty['voltage_kv']`, `tables`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::_enrich_parcel_grid_proximity_from_normalized` via `_voltage_level_table`.

**Complete source-ordered implementation**

```python
def _voltage_level_table(
    parcel_ids: pd.Series,
    parcel_geometries: np.ndarray,
    exact_lines: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, tuple[VoltageLevelCoverage, ...]]:
    levels = tuple(sorted(float(value) for value in exact_lines["voltage_kv"].unique()))
    tables: list[pd.DataFrame] = []
    coverage: list[VoltageLevelCoverage] = []
    for voltage_kv in levels:
        level_lines = exact_lines.loc[exact_lines["voltage_kv"] == voltage_kv].copy()
        coverage.append(
            VoltageLevelCoverage(
                voltage_kv=voltage_kv,
                line_feature_count=len(level_lines),
            )
        )
        nearest = _nearest_feature_rows(
            parcel_geometries,
            level_lines,
            (
                "grid_feature_id",
                "source_feature_id",
                "manager_name",
                "asset_status_raw",
                "source_department_code",
                "source_edition",
                "source_archive_sha256",
            ),
        )
        table = pd.DataFrame(
            {
                "parcel_id": parcel_ids.reset_index(drop=True),
                "voltage_kv": voltage_kv,
                "nearest_line_proxy_distance_m": nearest["distance_m"],
                "nearest_line_grid_feature_id": nearest["grid_feature_id"],
                "nearest_line_source_feature_id": nearest["source_feature_id"],
                "tie_count": nearest["tie_count"],
                "manager_name": nearest["manager_name"],
                "asset_status_raw": nearest["asset_status_raw"],
                "source_department_code": nearest["source_department_code"],
                "source_edition": nearest["source_edition"],
                "source_archive_sha256": nearest["source_archive_sha256"],
            }
        )
        tables.append(table.loc[:, list(VOLTAGE_PROXIMITY_COLUMNS)])

    if not tables:
        empty = pd.DataFrame(columns=list(VOLTAGE_PROXIMITY_COLUMNS))
        empty["voltage_kv"] = empty["voltage_kv"].astype("float64")
        empty["nearest_line_proxy_distance_m"] = empty[
            "nearest_line_proxy_distance_m"
        ].astype("float64")
        empty["tie_count"] = empty["tie_count"].astype("Int64")
        return empty, ()
    return pd.concat(tables, ignore_index=True), tuple(coverage)
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_enrich_parcel_grid_proximity_from_normalized`

**Exact signature**

```python
def _enrich_parcel_grid_proximity_from_normalized(
    parcels: gpd.GeoDataFrame,
    electric_lines: gpd.GeoDataFrame,
    transformation_posts: gpd.GeoDataFrame,
) -> GridProximityResult:
```

**Purpose**

Attach nearest IGN proxy matches using planar XY distance in EPSG:2154. IGN Z values are removed from calculation-only copies and do not affect horizontal proximity. Source parcel and normalized IGN geometries are not mutated. Distances describe only the nearest feature inside loaded proxy coverage and do not establish connection feasibility.

**Return contract**

- Declared return annotation: `GridProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `valid_lines.empty`.
- Guard with a raise path: `valid_posts.empty`.
- Explicit raise expressions: `GridProximityError('No VALID electric-line proxy is available')`, `GridProximityError('No VALID transformation-post proxy is available')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `output.to_crs`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `exact_lines['voltage_kv']`.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_assess_grid_coverage.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    _enrich_parcel_grid_proximity_from_normalized as enrich_parcel_grid_proximity,
)`.
- direct call: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `_enrich_parcel_grid_proximity_from_normalized`.
- direct call: `tests/unit/test_assess_grid_coverage.py::_proximity` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `enrich_parcel_grid_proximity`.

**Complete source-ordered implementation**

```python
def _enrich_parcel_grid_proximity_from_normalized(
    parcels: gpd.GeoDataFrame,
    electric_lines: gpd.GeoDataFrame,
    transformation_posts: gpd.GeoDataFrame,
) -> GridProximityResult:
    """Attach nearest IGN proxy matches using planar XY distance in EPSG:2154.

    IGN Z values are removed from calculation-only copies and do not affect
    horizontal proximity. Source parcel and normalized IGN geometries are not
    mutated. Distances describe only the nearest feature inside loaded proxy
    coverage and do not establish connection feasibility.
    """

    _validate_parcels(parcels)
    valid_lines = _validate_grid(
        electric_lines,
        label="Electric-line grid",
        required_columns=LINE_REQUIRED_COLUMNS,
        feature_type="ELECTRIC_LINE",
        allowed_geometry_types=LINE_GEOMETRY_TYPES,
    )
    valid_posts = _validate_grid(
        transformation_posts,
        label="Transformation-post grid",
        required_columns=POST_REQUIRED_COLUMNS,
        feature_type="TRANSFORMATION_POST",
        allowed_geometry_types=POST_GEOMETRY_TYPES,
    )
    if valid_lines.empty:
        raise GridProximityError("No VALID electric-line proxy is available")
    if valid_posts.empty:
        raise GridProximityError("No VALID transformation-post proxy is available")

    output = parcels.reset_index(drop=True).copy()
    calculation_parcels = output.to_crs(CALCULATION_CRS)
    parcel_geometries = _calculation_geometries(calculation_parcels)

    nearest_line = _nearest_feature_rows(
        parcel_geometries,
        valid_lines,
        _LINE_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_line, _LINE_OUTPUT_MAPPING)

    exact_mask = (valid_lines["voltage_status"] == "EXACT") & valid_lines[
        "voltage_kv"
    ].map(_is_positive_finite_number)
    exact_lines = valid_lines.loc[exact_mask].reset_index(drop=True).copy()
    exact_lines["voltage_kv"] = exact_lines["voltage_kv"].map(float).astype("float64")
    nearest_exact = _nearest_feature_rows(
        parcel_geometries,
        exact_lines,
        _LINE_MATCH_COLUMNS,
        allow_empty=True,
    )
    _attach_matches(output, nearest_exact, _EXACT_LINE_OUTPUT_MAPPING)

    nearest_post = _nearest_feature_rows(
        parcel_geometries,
        valid_posts,
        _POST_MATCH_COLUMNS,
    )
    _attach_matches(output, nearest_post, _POST_OUTPUT_MAPPING)

    voltage_table, voltage_coverage = _voltage_level_table(
        output["parcel_id"], parcel_geometries, exact_lines
    )
    result = GridProximityResult(
        parcels=output,
        voltage_level_proximity=voltage_table,
        voltage_level_coverage=voltage_coverage,
    )
    _validate_output_integrity(parcels, result)
    return result
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `enrich_parcel_grid_proximity`

**Exact signature**

```python
def enrich_parcel_grid_proximity(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridProximityResult:
```

**Purpose**

Compute proximity from one physically revalidated IGN source bundle.

**Return contract**

- Declared return annotation: `GridProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
_enrich_parcel_grid_proximity_from_normalized(parcels, normalized.electric_lines, normalized.transformation_posts)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `type(electricity_source) is not IgnBdTopoElectricityData`.
- Guard with a raise path: `type(source_config) is not IgnBdTopoSourceConfig`.
- Guard with a raise path: `type(normalized) is not NormalizedIgnElectricityData`.
- Explicit raise expressions: `GridProximityError('IGN electricity normalization returned an invalid result')`, `GridProximityError('Parcel-to-grid proximity cannot be computed safely')`, `GridProximityError('electricity source must be an IgnBdTopoElectricityData')`, `GridProximityError('parcels must be a GeoDataFrame with active geometry')`, `GridProximityError('source_config must be an IgnBdTopoSourceConfig')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.stages import (
    enrich_parcel_grid_proximity as public_enrich_parcel_grid_proximity,
)`.
- direct call: `src/landscout/stages/assess_grid_coverage.py::assess_grid_coverage` via `enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `public_enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types` via `public_enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `public_enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles` via `public_enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config` via `public_enrich_parcel_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation` via `public_enrich_parcel_grid_proximity`.

**Complete source-ordered implementation**

```python
def enrich_parcel_grid_proximity(
    parcels: gpd.GeoDataFrame,
    electricity_source: IgnBdTopoElectricityData,
    source_config: IgnBdTopoSourceConfig,
) -> GridProximityResult:
    """Compute proximity from one physically revalidated IGN source bundle."""

    try:
        if not isinstance(parcels, gpd.GeoDataFrame):
            raise GridProximityError(
                "parcels must be a GeoDataFrame with active geometry"
            )
        if type(electricity_source) is not IgnBdTopoElectricityData:
            raise GridProximityError(
                "electricity source must be an IgnBdTopoElectricityData"
            )
        if type(source_config) is not IgnBdTopoSourceConfig:
            raise GridProximityError(
                "source_config must be an IgnBdTopoSourceConfig"
            )
        _validate_parcels(parcels)
        normalized = normalize_ign_electricity(electricity_source, source_config)
        if type(normalized) is not NormalizedIgnElectricityData:
            raise GridProximityError(
                "IGN electricity normalization returned an invalid result"
            )
        return _enrich_parcel_grid_proximity_from_normalized(
            parcels,
            normalized.electric_lines,
            normalized.transformation_posts,
        )
    except GridProximityError:
        raise
    except Exception as error:
        raise GridProximityError(
            "Parcel-to-grid proximity cannot be computed safely"
        ) from error
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `_distance_profile`

**Exact signature**

```python
def _distance_profile(distances: pd.Series, ties: pd.Series) -> DistanceProfile:
```

**Purpose**

Private `grid/source` helper for distance profile; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `DistanceProfile`.
- Every observed return expression is reproduced without truncation:
```python
DistanceProfile(count=len(values), missing_count=missing_count, minimum=float(values.min()), p01=float(values.quantile(0.01)), p05=float(values.quantile(0.05)), p10=float(values.quantile(0.1)), p25=float(values.quantile(0.25)), p50=float(values.quantile(0.5)), p75=float(values.quantile(0.75)), p90=float(values.quantile(0.9)), p95=float(values.quantile(0.95)), p99=float(values.quantile(0.99)), maximum=float(values.max()), zero_distance_count=int(values.eq(0).sum()), tie_count=sum((value > 1 for value in matched_ties.tolist())))

DistanceProfile(count=0, missing_count=missing_count, minimum=None, p01=None, p05=None, p10=None, p25=None, p50=None, p75=None, p90=None, p95=None, p99=None, maximum=None, zero_distance_count=0, tie_count=0)
```

**Validation and exceptions**

- Guard with a raise path: `matched_ties.isna().any()`.
- Explicit raise expressions: `GridProximityError('Matched distance rows require tie counts')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `DistanceProfile`, `_validate_distance_values`, `distances.dropna`, `distances.dropna().astype`, `distances.isna`, `distances.isna().sum`, `distances.notna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_grid_proximity.py::profile_grid_proximity` via `_distance_profile`.

**Complete source-ordered implementation**

```python
def _distance_profile(distances: pd.Series, ties: pd.Series) -> DistanceProfile:
    _validate_distance_values(distances, "Profile")
    values = distances.dropna().astype("float64")
    missing_count = int(distances.isna().sum())
    if values.empty:
        return DistanceProfile(
            count=0,
            missing_count=missing_count,
            minimum=None,
            p01=None,
            p05=None,
            p10=None,
            p25=None,
            p50=None,
            p75=None,
            p90=None,
            p95=None,
            p99=None,
            maximum=None,
            zero_distance_count=0,
            tie_count=0,
        )
    matched_ties = ties.loc[distances.notna()]
    if matched_ties.isna().any():
        raise GridProximityError("Matched distance rows require tie counts")
    return DistanceProfile(
        count=len(values),
        missing_count=missing_count,
        minimum=float(values.min()),
        p01=float(values.quantile(0.01)),
        p05=float(values.quantile(0.05)),
        p10=float(values.quantile(0.10)),
        p25=float(values.quantile(0.25)),
        p50=float(values.quantile(0.50)),
        p75=float(values.quantile(0.75)),
        p90=float(values.quantile(0.90)),
        p95=float(values.quantile(0.95)),
        p99=float(values.quantile(0.99)),
        maximum=float(values.max()),
        zero_distance_count=int(values.eq(0).sum()),
        tie_count=sum(value > 1 for value in matched_ties.tolist()),
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.

### `profile_grid_proximity`

**Exact signature**

```python
def profile_grid_proximity(result: GridProximityResult) -> GridProximityProfile:
```

**Purpose**

Profile proximity distances without thresholds or suitability labels.

**Return contract**

- Declared return annotation: `GridProximityProfile`.
- Every observed return expression is reproduced without truncation:
```python
GridProximityProfile(parcel_count=len(parcels), nearest_line=_distance_profile(parcels['nearest_line_proxy_distance_m'], parcels['nearest_line_tie_count']), nearest_exact_line=_distance_profile(parcels['nearest_exact_line_proxy_distance_m'], parcels['nearest_exact_line_tie_count']), nearest_post=_distance_profile(parcels['nearest_post_proxy_distance_m'], parcels['nearest_post_tie_count']), voltage_levels=tuple(voltage_profiles))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `VoltageLevelDistanceProfile`, `_distance_profile`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `voltage_profiles`.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    DistanceProfile,
    GridProximityError,
    GridProximityProfile,
    GridProximityResult,
    VoltageLevelCoverage,
    VoltageLevelDistanceProfile,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `src/landscout/stages/assess_grid_coverage.py::<module>` via `from landscout.stages.enrich_grid_proximity import (
    GridProximityResult,
    VoltageLevelCoverage,
    enrich_parcel_grid_proximity,
    profile_grid_proximity,
)`.
- import: `tests/unit/test_enrich_grid_proximity.py::<module>` via `from landscout.stages import (
    GridProximityError,
    GridProximityResult,
    VoltageLevelCoverage,
    profile_grid_proximity,
)`.
- direct call: `src/landscout/stages/assess_grid_coverage.py::_validate_assessment_result` via `profile_grid_proximity`.
- direct call: `src/landscout/stages/assess_grid_coverage.py::_assess_grid_coverage_from_proximity` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_voltage_cartesian_row` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_unknown_voltage_parcel_with_same_total_count` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_duplicate_parcel_voltage_pair` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_voltage_rows_out_of_parcel_order` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_distance` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_identity` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_metadata` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_inconsistent_global_exact_tie_count` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_tie_count` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_tie_count` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_main_match_feature_id` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_required_match_distance` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_exact_match_voltage` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_result_parcel_id` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_required_proximity_column` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nondeterministic_or_duplicate_coverage` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_level` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_voltage_coverage_feature_count` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_invalid_long_table_voltage` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_missing_long_table_match_lineage` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_bad_long_table_distance` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `profile_grid_proximity`.
- direct call: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `profile_grid_proximity`.

**Complete source-ordered implementation**

```python
def profile_grid_proximity(result: GridProximityResult) -> GridProximityProfile:
    """Profile proximity distances without thresholds or suitability labels."""

    _validate_result_contract(result)
    parcels = result.parcels
    coverage = {
        float(item.voltage_kv): item.line_feature_count
        for item in result.voltage_level_coverage
    }
    voltage_profiles: list[VoltageLevelDistanceProfile] = []
    table = result.voltage_level_proximity
    observed_levels = tuple(coverage)
    for voltage_kv in observed_levels:
        rows = table.loc[table["voltage_kv"] == voltage_kv]
        distance = _distance_profile(
            rows["nearest_line_proxy_distance_m"], rows["tie_count"]
        )
        voltage_profiles.append(
            VoltageLevelDistanceProfile(
                voltage_kv=voltage_kv,
                line_feature_count=coverage[voltage_kv],
                parcel_proximity_count=len(rows),
                distance=distance,
            )
        )

    return GridProximityProfile(
        parcel_count=len(parcels),
        nearest_line=_distance_profile(
            parcels["nearest_line_proxy_distance_m"],
            parcels["nearest_line_tie_count"],
        ),
        nearest_exact_line=_distance_profile(
            parcels["nearest_exact_line_proxy_distance_m"],
            parcels["nearest_exact_line_tie_count"],
        ),
        nearest_post=_distance_profile(
            parcels["nearest_post_proxy_distance_m"],
            parcels["nearest_post_tie_count"],
        ),
        voltage_levels=tuple(voltage_profiles),
    )
```

**Business boundary**

- Grid proximity is proxy evidence; it does not prove capacity, connection feasibility, cost, or authorization.


## 7. Data contracts

### Frame-preservation and semantic notes

- The parcel output preserves the complete input parcel frame and appends nearest-line, nearest-exact-line, nearest-transformation-post proxy, tie, voltage-representation, policy-lineage, and scope fields. Distance values are geometry-derived proxy facts in metres; they do not establish capacity or connection feasibility.
- The voltage-level table is a separate parcel-by-voltage result. Null nearest-feature fields are required where a class has no eligible geometry; tie counts and match flags distinguish absence from a measured match.

### `PARCEL_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 2 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |

### `LINE_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
LINE_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "voltage_raw",
        "voltage_status",
        "voltage_kv",
        "voltage_upper_bound_kv",
        "manager_name",
        "asset_status_raw",
        "geometry",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 3 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `grid_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 5 | `grid_feature_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `manager_name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 8 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `voltage_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 14 | `voltage_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `voltage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 16 | `voltage_upper_bound_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |

### `POST_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
POST_REQUIRED_COLUMNS = frozenset(
    {
        "grid_feature_id",
        "grid_feature_type",
        "source_feature_id",
        "source_department_code",
        "source_edition",
        "source_archive_sha256",
        "source_layer",
        "spatial_role",
        "geometry_status",
        "name",
        "importance_raw",
        "asset_status_raw",
        "geometry",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 3 | `geometry_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `grid_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 5 | `grid_feature_type` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 9 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `spatial_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `VOLTAGE_PROXIMITY_COLUMNS` — canonical or derived frame-column schema

```python
VOLTAGE_PROXIMITY_COLUMNS = (
    "parcel_id",
    "voltage_kv",
    "nearest_line_proxy_distance_m",
    "nearest_line_grid_feature_id",
    "nearest_line_source_feature_id",
    "tie_count",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `voltage_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 3 | `nearest_line_proxy_distance_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 4 | `nearest_line_grid_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 5 | `nearest_line_source_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 6 | `tie_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 7 | `manager_name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `_LINE_MATCH_COLUMNS` — canonical or derived frame-column schema

```python
_LINE_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "voltage_raw",
    "voltage_status",
    "voltage_kv",
    "voltage_upper_bound_kv",
    "manager_name",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `grid_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `voltage_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `voltage_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | derived factual classification | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `voltage_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 6 | `voltage_upper_bound_kv` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 7 | `manager_name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `_POST_MATCH_COLUMNS` — canonical or derived frame-column schema

```python
_POST_MATCH_COLUMNS = (
    "grid_feature_id",
    "source_feature_id",
    "name",
    "importance_raw",
    "asset_status_raw",
    "source_department_code",
    "source_edition",
    "source_archive_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `grid_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `name` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `importance_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `asset_status_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `source_department_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 7 | `source_edition` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `_LINE_OUTPUT_MAPPING` — mapping between source/input and output keys or columns

```python
_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_line_proxy_distance_m",
    "grid_feature_id": "nearest_line_grid_feature_id",
    "source_feature_id": "nearest_line_source_feature_id",
    "tie_count": "nearest_line_tie_count",
    "voltage_raw": "nearest_line_voltage_raw",
    "voltage_status": "nearest_line_voltage_status",
    "voltage_kv": "nearest_line_voltage_kv",
    "voltage_upper_bound_kv": "nearest_line_voltage_upper_bound_kv",
    "manager_name": "nearest_line_manager_name",
    "asset_status_raw": "nearest_line_asset_status_raw",
    "source_department_code": "nearest_line_source_department_code",
    "source_edition": "nearest_line_source_edition",
    "source_archive_sha256": "nearest_line_source_archive_sha256",
}
```

| Source/input key or column | Target/output key or column | Contract |
|---|---|---|
| `distance_m` | `nearest_line_proxy_distance_m` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `grid_feature_id` | `nearest_line_grid_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_feature_id` | `nearest_line_source_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `tie_count` | `nearest_line_tie_count` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `voltage_raw` | `nearest_line_voltage_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `voltage_status` | `nearest_line_voltage_status` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `voltage_kv` | `nearest_line_voltage_kv` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `voltage_upper_bound_kv` | `nearest_line_voltage_upper_bound_kv` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `manager_name` | `nearest_line_manager_name` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `asset_status_raw` | `nearest_line_asset_status_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_department_code` | `nearest_line_source_department_code` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_edition` | `nearest_line_source_edition` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_archive_sha256` | `nearest_line_source_archive_sha256` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |

### `_EXACT_LINE_OUTPUT_MAPPING` — mapping between source/input and output keys or columns

```python
_EXACT_LINE_OUTPUT_MAPPING = {
    "distance_m": "nearest_exact_line_proxy_distance_m",
    "grid_feature_id": "nearest_exact_line_grid_feature_id",
    "source_feature_id": "nearest_exact_line_source_feature_id",
    "tie_count": "nearest_exact_line_tie_count",
    "voltage_kv": "nearest_exact_line_voltage_kv",
    "manager_name": "nearest_exact_line_manager_name",
    "asset_status_raw": "nearest_exact_line_asset_status_raw",
    "source_department_code": "nearest_exact_line_source_department_code",
    "source_edition": "nearest_exact_line_source_edition",
    "source_archive_sha256": "nearest_exact_line_source_archive_sha256",
}
```

| Source/input key or column | Target/output key or column | Contract |
|---|---|---|
| `distance_m` | `nearest_exact_line_proxy_distance_m` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `grid_feature_id` | `nearest_exact_line_grid_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_feature_id` | `nearest_exact_line_source_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `tie_count` | `nearest_exact_line_tie_count` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `voltage_kv` | `nearest_exact_line_voltage_kv` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `manager_name` | `nearest_exact_line_manager_name` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `asset_status_raw` | `nearest_exact_line_asset_status_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_department_code` | `nearest_exact_line_source_department_code` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_edition` | `nearest_exact_line_source_edition` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_archive_sha256` | `nearest_exact_line_source_archive_sha256` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |

### `_POST_OUTPUT_MAPPING` — mapping between source/input and output keys or columns

```python
_POST_OUTPUT_MAPPING = {
    "distance_m": "nearest_post_proxy_distance_m",
    "grid_feature_id": "nearest_post_grid_feature_id",
    "source_feature_id": "nearest_post_source_feature_id",
    "tie_count": "nearest_post_tie_count",
    "name": "nearest_post_name",
    "importance_raw": "nearest_post_importance_raw",
    "asset_status_raw": "nearest_post_asset_status_raw",
    "source_department_code": "nearest_post_source_department_code",
    "source_edition": "nearest_post_source_edition",
    "source_archive_sha256": "nearest_post_source_archive_sha256",
}
```

| Source/input key or column | Target/output key or column | Contract |
|---|---|---|
| `distance_m` | `nearest_post_proxy_distance_m` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `grid_feature_id` | `nearest_post_grid_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_feature_id` | `nearest_post_source_feature_id` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `tie_count` | `nearest_post_tie_count` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `name` | `nearest_post_name` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `importance_raw` | `nearest_post_importance_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `asset_status_raw` | `nearest_post_asset_status_raw` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_department_code` | `nearest_post_source_department_code` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_edition` | `nearest_post_source_edition` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |
| `source_archive_sha256` | `nearest_post_source_archive_sha256` | Explicit mapping; the implementation determines whether values are copied, renamed, or transformed. |


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
