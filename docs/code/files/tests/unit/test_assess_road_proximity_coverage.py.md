# `tests/unit/test_assess_road_proximity_coverage.py`

## File identity

- Repository path: `tests/unit/test_assess_road_proximity_coverage.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.
- Source SHA256: `aa04754f7dc742918b0efd586c6c3011ea3a3df7b8bd888a5b804931d84951fa`

## 1. Purpose

Provides complete unit and regression coverage for the `assess_road_proximity_coverage` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from copy import deepcopy`
- `from dataclasses import FrozenInstanceError, replace`
- `from importlib import import_module`
- `from pathlib import Path`
- `from typing import Any, cast`
- `from unittest.mock import patch`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoCoverageLayerSummary,
    IgnBdTopoDepartmentCoverage,
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.assess_road_proximity_coverage import (
    RoadProximityCoverageAssessmentResult,
    RoadProximityCoverageError,
    assess_road_proximity_coverage,
)`
- `from landscout.stages.enrich_road_proximity import (
    CLASS_PROXIMITY_COLUMNS,
    ParcelRoadProximityResult,
    RoadProxyClassCoverage,
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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` (value argument/reference).

#### `ARCHIVE_SHA256`

```python
ARCHIVE_SHA256 = "a" * 64
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract. Consumers include `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_road_proximity_coverage.py::_archive` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_normalize_access_ign.py::_source` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_context` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference).

#### `GEOPACKAGE_SHA256`

```python
GEOPACKAGE_SHA256 = "b" * 64
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract. Consumers include `tests/unit/test_assess_road_proximity_coverage.py::_extraction` (value argument/reference).

#### `EDITION`

```python
EDITION = "2026-06-15"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_road_proximity_coverage.py::_archive` (value argument/reference).

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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_assess_road_proximity_coverage.py::_proximity` (value argument/reference), `tests/unit/test_enrich_road_proximity.py::test_output_shape_columns_and_order_are_deterministic` (value argument/reference).

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

Module-level technical/source/policy constant consumed by the exact references below.

#### `DIAGNOSTIC_COLUMNS`

```python
DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_enrich_road_proximity.py::test_empty_eligible_class_emits_null_row_per_parcel` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_archive`

**Exact signature**

```python
def _archive() -> IgnBdTopoDownload:
```

**Purpose**

Private `test` helper for archive; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoDownload`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoDownload(provider=SOURCE_CONFIG.provider, product=SOURCE_CONFIG.product, department_code='31', edition=EDITION, product_version='3.5', projection='EPSG:2154', package_format='GPKG', archive_format='7z', source_url=str(SOURCE_CONFIG.source_url), checksum_url=None, download_timestamp='2026-08-11T15:32:03+00:00', filename='BDTOPO.7z', file_size=123, sha256=ARCHIVE_SHA256, official_checksum_algorithm=None, official_checksum=None, official_checksum_validated=False, path=Path('synthetic/BDTOPO.7z'), cache_hit=True)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `IgnBdTopoDownload`.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_extraction` via `_archive`.

**Complete source-ordered implementation**

```python
def _archive() -> IgnBdTopoDownload:
    return IgnBdTopoDownload(
        provider=SOURCE_CONFIG.provider,
        product=SOURCE_CONFIG.product,
        department_code="31",
        edition=EDITION,
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=str(SOURCE_CONFIG.source_url),
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO.7z",
        file_size=123,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("synthetic/BDTOPO.7z"),
        cache_hit=True,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_extraction`

**Exact signature**

```python
def _extraction() -> IgnBdTopoExtraction:
```

**Purpose**

Private `test` helper for extraction; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoExtraction`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoExtraction(archive=_archive(), extraction_path=Path('synthetic/extracted'), geopackage_path=Path('synthetic/extracted/data.gpkg'), geopackage_filename='data.gpkg', geopackage_size_bytes=456, geopackage_sha256=GEOPACKAGE_SHA256, all_layer_names=('ligne_electrique', 'poste_de_transformation', 'troncon_de_route', 'departement', 'zone_administrative'), electric_lines_layer='ligne_electrique', transformation_posts_layer='poste_de_transformation', cache_hit=True)
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

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_road_source` via `_extraction`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_coverage` via `_extraction`.

**Complete source-ordered implementation**

```python
def _extraction() -> IgnBdTopoExtraction:
    return IgnBdTopoExtraction(
        archive=_archive(),
        extraction_path=Path("synthetic/extracted"),
        geopackage_path=Path("synthetic/extracted/data.gpkg"),
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=456,
        geopackage_sha256=GEOPACKAGE_SHA256,
        all_layer_names=(
            "ligne_electrique",
            "poste_de_transformation",
            "troncon_de_route",
            "departement",
            "zone_administrative",
        ),
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        cache_hit=True,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_road_source`

**Exact signature**

```python
def _road_source(
    extraction: IgnBdTopoExtraction | None = None,
) -> IgnBdTopoRoadData:
```

**Purpose**

Private `test` helper for road source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoRoadData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoRoadData(package, roads, summary)
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

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object` via `_road_source`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_road_source`.

**Complete source-ordered implementation**

```python
def _road_source(
    extraction: IgnBdTopoExtraction | None = None,
) -> IgnBdTopoRoadData:
    package = extraction or _extraction()
    roads = gpd.GeoDataFrame(
        {"cleabs": ["ROAD-1"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs="EPSG:2154",
    )
    summary = IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name="troncon_de_route",
        crs="EPSG:2154",
        feature_count=1,
        columns=tuple(str(column) for column in roads.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in roads.dtypes.items()
        ),
        null_geometry_count=0,
        empty_geometry_count=0,
        invalid_geometry_count=0,
        geometry_types=("LineString",),
    )
    return IgnBdTopoRoadData(package, roads, summary)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coverage`

**Exact signature**

```python
def _coverage(
    extraction: IgnBdTopoExtraction | None = None,
    *,
    geometries: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    layer: str = "departement",
    department_code: str = "31",
    provider: str | None = None,
    product: str | None = None,
    edition: str = EDITION,
    product_version: str | None = "3.5",
    archive_sha256: str = ARCHIVE_SHA256,
) -> IgnBdTopoDepartmentCoverage:
```

**Purpose**

Private `test` helper for coverage; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoDepartmentCoverage`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoDepartmentCoverage(extraction=package, coverage=selected, summary=summary, source_provider=cast(str, lineage['source_provider']), source_product=cast(str, lineage['source_product']), source_department_code=department_code, source_edition=edition, source_product_version=product_version, source_archive_sha256=archive_sha256, source_layer=layer)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `geometry.geom_type.dropna`, `geometry.geom_type.dropna().unique`, `geometry.isna`, `geometry.isna().sum`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `selected[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_enrich_parcel_road_proximity` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_selected_department_identity_is_exact` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_invalid_coverage_geometry_is_rejected` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_exact_coverage_lineage_is_appended_to_every_row` via `_coverage`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_coverage`.

**Complete source-ordered implementation**

```python
def _coverage(
    extraction: IgnBdTopoExtraction | None = None,
    *,
    geometries: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    layer: str = "departement",
    department_code: str = "31",
    provider: str | None = None,
    product: str | None = None,
    edition: str = EDITION,
    product_version: str | None = "3.5",
    archive_sha256: str = ARCHIVE_SHA256,
) -> IgnBdTopoDepartmentCoverage:
    package = extraction or _extraction()
    values = geometries
    if values is None:
        values = [
            Polygon([(0, 0), (0, 1000), (1000, 1000), (1000, 0), (0, 0)])
        ]
    raw = gpd.GeoDataFrame(
        {
            "code_insee": [department_code] * len(values),
            "nom_officiel": [f"Department {position}" for position in range(len(values))],
        },
        geometry=values,
        crs=crs,
    )
    lineage = {
        "source_provider": provider or package.archive.provider,
        "source_product": product or package.archive.product,
        "source_department_code": department_code,
        "source_edition": edition,
        "source_product_version": product_version,
        "source_archive_sha256": archive_sha256,
        "source_layer": layer,
        "spatial_role": "SOURCE_COVERAGE_BOUNDARY",
    }
    selected = raw.copy()
    for column, value in lineage.items():
        selected[column] = value
    geometry = raw.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = IgnBdTopoCoverageLayerSummary(
        source_layer_name=layer,
        crs="" if crs is None else str(raw.crs),
        source_feature_count=len(raw),
        selected_feature_count=len(raw),
        columns=tuple(str(column) for column in raw.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in raw.dtypes.items()
        ),
        null_geometry_count=int(geometry.isna().sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
        geometry_types=tuple(
            sorted(str(value) for value in geometry.geom_type.dropna().unique())
        ),
        department_code_field="code_insee",
        selected_department_code=department_code,
    )
    return IgnBdTopoDepartmentCoverage(
        extraction=package,
        coverage=selected,
        summary=summary,
        source_provider=cast(str, lineage["source_provider"]),
        source_product=cast(str, lineage["source_product"]),
        source_department_code=department_code,
        source_edition=edition,
        source_product_version=product_version,
        source_archive_sha256=archive_sha256,
        source_layer=layer,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_metric_parcels`

**Exact signature**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for metric parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'parcel_id': ids, 'preserved_value': list(range(len(values)))}, geometry=values, crs='EPSG:2154', index=[20 + position for position in range(len(values))])
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

- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_metric_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `_metric_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_metric_parcels`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_metric_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_parcels` via `_metric_parcels`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_parcels` via `_metric_parcels`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_missing_or_wrong_storage_crs_is_rejected` via `_metric_parcels`.

**Complete source-ordered implementation**

```python
def _metric_parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    values = geometries or [
        Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)])
    ]
    ids = identifiers or [f"PARCEL-{position + 1}" for position in range(len(values))]
    return gpd.GeoDataFrame(
        {"parcel_id": ids, "preserved_value": list(range(len(values)))},
        geometry=values,
        crs="EPSG:2154",
        index=[20 + position for position in range(len(values))],
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
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_metric_parcels(geometries, identifiers=identifiers).to_crs('EPSG:4326')
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_metric_parcels(geometries, identifiers=identifiers).to_crs`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::_proximity` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_geographic_parcel_storage_crs_and_geometry_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_proximity` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_wrong_public_input_type_is_controlled_and_fast` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_proximity_failure_stops_coverage_loading` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_is_frozen_and_has_no_business_decision_fields` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::_two_parcel_two_voltage_result` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_normalizes_verified_source_exactly_once` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_wrong_source_boundary_types` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_caller_crafted_normalized_grid_frame_is_not_a_public_source` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_reproduces_configured_electricity_roles` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_public_proximity_rejects_archive_lineage_differing_from_config` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_source_normalization_failure_stops_grid_computation` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_separated_distance_uses_parcel_edge_not_centroid` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_touching_line_has_zero_distance` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_post_distance_uses_parcel_and_post_polygons` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg4326_input_is_calculated_in_lambert93_and_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_epsg2154_parcel_input_remains_epsg2154` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_valid_parcel_id_is_preserved_exactly` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_parcel_id_hygiene_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_parcel_polygon_geometry_is_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_semantically_wrong_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_z_line_has_same_horizontal_distance_as_xy_line` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_line_tie_is_counted_and_lexical_feature_id_wins` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_cross_voltage_tie_uses_lexical_global_feature_id` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nonvalid_grid_geometries_are_excluded_without_row_loss` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_grid_feature_type_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_grid_feature_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_wrong_spatial_role_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_unsupported_valid_grid_geometry_type_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_supported_multi_geometries_are_accepted` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_any_line_preserves_every_voltage_status` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_nearest_exact_and_voltage_table_exclude_nonexact_lines` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_invalid_exact_voltage_values_are_not_used_as_exact` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_exact_voltage_preserves_parcels_and_returns_empty_long_table` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_missing_parcel_column_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_null_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_duplicate_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_bad_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_inputs_are_not_mutated_and_parcel_order_and_ids_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_distance_profile_is_threshold_free_and_tracks_ties` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_allows_consistent_missing_manager_and_asset_status` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_profile_rejects_nonnull_exact_field_without_exact_coverage` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_grid_proximity.py::test_no_valid_required_grid_feature_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_run` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_epsg4326_parcels_are_measured_in_lambert93_but_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_invalid_parcel_ids_are_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_reserved_output_column_collision_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_relations_are_unique_deterministic_and_summaries_agree` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_result_frames_are_independent_from_mutable_inputs` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_contract_result` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_two_parcel_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::_run` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_one_parcel_fully_inside_one_zone` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_split_across_two_zones` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_dominant_zone_tie_is_deterministic` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_touch_only_relation_is_preserved_but_never_dominant` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_positive_area_zone_is_preserved` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_with_no_intersecting_zone_has_zero_coverage` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_overlapping_source_zones_expose_raw_sum_union_and_excess` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_parcels_are_supported` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_polygon_and_multipolygon_zones_are_supported` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_parcel_crs_is_preserved_while_metric_calculation_uses_lambert93` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_ignf_lamb93_source_zoning_is_normalized_to_epsg2154` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_or_unusable_crs_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_parcel_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_or_non_polygonal_zone_geometry_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_invalid_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_duplicate_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_missing_parcel_id_is_rejected` via `_parcels`.
- direct call or construction: `tests/unit/test_enrich_planning_zoning.py::test_geometry_must_be_the_active_parcel_geometry_column` via `_parcels`.

**Complete source-ordered implementation**

```python
def _parcels(
    geometries: list[object] | None = None,
    *,
    identifiers: list[str] | None = None,
) -> gpd.GeoDataFrame:
    return _metric_parcels(geometries, identifiers=identifiers).to_crs("EPSG:4326")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_proximity`

**Exact signature**

```python
def _proximity(
    parcels: gpd.GeoDataFrame | None = None,
    *,
    distances: dict[str, float] | None = None,
) -> ParcelRoadProximityResult:
```

**Purpose**

Private `test` helper for proximity; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `ParcelRoadProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
ParcelRoadProximityResult(source_parcels.copy(), table, coverage)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `configured_distances.get`, `table['nearest_road_proxy_distance_m'].astype`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `table['nearest_road_proxy_distance_m']`, `table['nearest_road_tie_count']`, `table['nearest_road_toll_evidence']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_no_exact_match_uses_explicit_no_match_status` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_assessment_preserves_proximity_values_and_does_not_mutate_input` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_profile_reports_dynamic_voltage_and_boundary_distributions` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_proximity_and_coverage_package_lineage_must_match` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_rejects_arbitrary_source_identity` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_count_must_match_frame` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_schema_must_match_selected_source_columns` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_crs_must_match_frame` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_geometry_facts_are_validated` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_selected_department_must_match` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_department_field_must_be_exact` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_summary_source_count_cannot_be_smaller_than_selection` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_coverage_source_layer_lineage_must_match_summary_and_frame` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_grid_coverage.py::test_public_assessment_loads_coverage_from_the_physical_source` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_assess` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_source_chain_calls_proximity_then_coverage_exactly_once` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_loader_failure_is_controlled` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_upstream_result_fails_before_coverage_load` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_road_lineage_must_match_coverage` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `_proximity`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `_proximity`.

**Complete source-ordered implementation**

```python
def _proximity(
    parcels: gpd.GeoDataFrame | None = None,
    *,
    distances: dict[str, float] | None = None,
) -> ParcelRoadProximityResult:
    source_parcels = parcels if parcels is not None else _parcels()
    policy = load_ign_road_vehicle_proxy_policy()
    configured_distances = distances or {}
    primary_rules = {
        "GENERAL_VEHICLE_PROXY": "OPEN_OR_TOLL",
        "LIMITED_VEHICLE_PROXY": "LIMITED_NATURE",
        "RESTRICTED_REVIEW": "PRIVATE_ROAD",
        "NOT_GENERAL_VEHICLE_PROXY": "PHYSICALLY_IMPOSSIBLE",
        "UNKNOWN_REVIEW": "UNKNOWN",
    }
    rows: list[dict[str, object]] = []
    for parcel_id in source_parcels["parcel_id"]:
        for position, road_class in enumerate(ELIGIBLE_CLASSES):
            distance_m = configured_distances.get(road_class, 50.0 + position)
            primary_rule = primary_rules[road_class]
            rows.append(
                {
                    "parcel_id": parcel_id,
                    "road_proxy_class": road_class,
                    "nearest_road_proxy_distance_m": distance_m,
                    "nearest_road_feature_id": f"ROAD-{road_class}",
                    "nearest_source_feature_id": f"SOURCE-{road_class}",
                    "nearest_road_tie_count": 1,
                    "nearest_road_primary_rule": primary_rule,
                    "nearest_road_rule_trace_json": f'["{primary_rule}"]',
                    "nearest_road_unknown_fields_json": "[]",
                    "nearest_road_toll_evidence": False,
                    "nearest_nature_raw": "Route à 1 chaussée",
                    "nearest_importance_raw": "2",
                    "nearest_asset_status_raw": "En service",
                    "nearest_private_raw": 0.0,
                    "nearest_light_vehicle_access_raw": "Libre",
                    "nearest_carriageway_width_raw": 7.0,
                    "nearest_closure_period_raw": None,
                    "nearest_restriction_nature_raw": None,
                    "nearest_source_layer": "troncon_de_route",
                    "nearest_source_department_code": "31",
                    "nearest_source_edition": EDITION,
                    "nearest_source_archive_sha256": ARCHIVE_SHA256,
                    "road_proxy_policy_id": policy.policy_id,
                    "road_proxy_policy_schema_version": policy.schema_version,
                    "road_proxy_policy_config_sha256": policy.config_sha256,
                    "road_proxy_heavy_vehicle_access": policy.heavy_vehicle_access,
                    "proximity_scope": "WITHIN_VERIFIED_SOURCE_PACKAGE",
                }
            )
    table = pd.DataFrame(rows, columns=CLASS_PROXIMITY_COLUMNS)
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype(
        "Int64"
    )
    table["nearest_road_toll_evidence"] = table[
        "nearest_road_toll_evidence"
    ].astype("boolean")
    coverage = tuple(
        RoadProxyClassCoverage(
            road_proxy_class=road_class,
            feature_count=1,
            distance_eligible=road_class != "NOT_DISTANCE_PROXY",
        )
        for road_class in ALL_CLASSES
    )
    return ParcelRoadProximityResult(source_parcels.copy(), table, coverage)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_without_match`

**Exact signature**

```python
def _without_match(
    proximity: ParcelRoadProximityResult,
    road_class: str = "UNKNOWN_REVIEW",
) -> ParcelRoadProximityResult:
```

**Purpose**

Private `test` helper for without match; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `ParcelRoadProximityResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(proximity, class_proximity=table, class_coverage=coverage)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `table['nearest_road_proxy_distance_m'].astype`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `table.loc[mask, column]`, `table['nearest_road_proxy_distance_m']`, `table['nearest_road_tie_count']`, `table['nearest_road_toll_evidence']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_without_match`.

**Complete source-ordered implementation**

```python
def _without_match(
    proximity: ParcelRoadProximityResult,
    road_class: str = "UNKNOWN_REVIEW",
) -> ParcelRoadProximityResult:
    table = proximity.class_proximity.copy()
    mask = table["road_proxy_class"].eq(road_class)
    for column in SELECTED_COLUMNS:
        table.loc[mask, column] = pd.NA
    table["nearest_road_proxy_distance_m"] = table[
        "nearest_road_proxy_distance_m"
    ].astype("float64")
    table["nearest_road_tie_count"] = table["nearest_road_tie_count"].astype(
        "Int64"
    )
    table["nearest_road_toll_evidence"] = table[
        "nearest_road_toll_evidence"
    ].astype("boolean")
    coverage = tuple(
        replace(item, feature_count=0)
        if item.road_proxy_class == road_class
        else item
        for item in proximity.class_coverage
    )
    return replace(proximity, class_proximity=table, class_coverage=coverage)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_measured_boundary_distance`

**Exact signature**

```python
def _measured_boundary_distance(
    parcels: gpd.GeoDataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> float:
```

**Purpose**

Private `test` helper for measured boundary distance; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.distance`, `parcels.to_crs`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_measured_boundary_distance`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_measured_boundary_distance`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_measured_boundary_distance`.

**Complete source-ordered implementation**

```python
def _measured_boundary_distance(
    parcels: gpd.GeoDataFrame,
    coverage: IgnBdTopoDepartmentCoverage,
) -> float:
    geometry = parcels.to_crs("EPSG:2154").geometry.iloc[0]
    return float(geometry.distance(coverage.coverage.geometry.iloc[0].boundary))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_assess`

**Exact signature**

```python
def _assess(
    *,
    parcels: gpd.GeoDataFrame | None = None,
    proximity: object | None = None,
    coverage: IgnBdTopoDepartmentCoverage | None = None,
    road_source: IgnBdTopoRoadData | None = None,
    source_config: IgnBdTopoSourceConfig = SOURCE_CONFIG,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
```

**Purpose**

Derives diagnostic evidence for assess; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RoadProximityCoverageAssessmentResult`.
- Every observed return expression is reproduced without truncation:
```python
assess_road_proximity_coverage(selected_parcels, selected_source, source_config, policy_path)
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

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_stage_does_not_construct_a_road_spatial_index` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_package_lineage_must_match_road_archive` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_selected_department_identity_is_exact` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_spatial_role_and_source_type_are_controlled` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_coverage_must_retain_same_extraction_object` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_invalid_coverage_geometry_is_rejected` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_polygonal_coverage_geometry_is_accepted` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_strict_boundary_status_logic` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_outside_or_crossing_status` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_exact_coverage_lineage_is_appended_to_every_row` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_matched_road_lineage_must_match_coverage` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_preserves_every_upstream_fact_and_input_object` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `_assess`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_result_is_frozen_and_has_no_business_decision_fields` via `_assess`.

**Complete source-ordered implementation**

```python
def _assess(
    *,
    parcels: gpd.GeoDataFrame | None = None,
    proximity: object | None = None,
    coverage: IgnBdTopoDepartmentCoverage | None = None,
    road_source: IgnBdTopoRoadData | None = None,
    source_config: IgnBdTopoSourceConfig = SOURCE_CONFIG,
    policy_path: Path | None = None,
) -> RoadProximityCoverageAssessmentResult:
    selected_parcels = parcels if parcels is not None else _parcels()
    selected_proximity = (
        proximity if proximity is not None else _proximity(selected_parcels)
    )
    selected_coverage = coverage or _coverage()
    selected_source = road_source or _road_source(selected_coverage.extraction)
    with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=selected_proximity,
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
        return_value=selected_coverage,
    ):
        return assess_road_proximity_coverage(
            selected_parcels,
            selected_source,
            source_config,
            policy_path,
        )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_first_row`

**Exact signature**

```python
def _first_row(
    result: RoadProximityCoverageAssessmentResult,
    road_class: str = "GENERAL_VEHICLE_PROXY",
) -> pd.Series:
```

**Purpose**

Private `test` helper for first row; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_full_parcel_coverage_position_is_conservative` via `_first_row`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_position_uses_full_geometry_not_centroid` via `_first_row`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_no_match_takes_precedence_over_coverage_position` via `_first_row`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_classes_are_diagnosed_independently` via `_first_row`.

**Complete source-ordered implementation**

```python
def _first_row(
    result: RoadProximityCoverageAssessmentResult,
    road_class: str = "GENERAL_VEHICLE_PROXY",
) -> pd.Series:
    return result.class_proximity.loc[
        result.class_proximity["road_proxy_class"].eq(road_class)
    ].iloc[0]
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_api_exports_only_stable_symbols`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = import_module("landscout.stages.assess_road_proximity_coverage")
expected = {
        "RoadProximityCoverageError",
        "RoadProximityCoverageAssessmentResult",
        "assess_road_proximity_coverage",
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
assert not hasattr(stages, "_coverage_positions")
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_api_exports_only_stable_symbols() -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    expected = {
        "RoadProximityCoverageError",
        "RoadProximityCoverageAssessmentResult",
        "assess_road_proximity_coverage",
    }
    assert set(module.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, symbol) for symbol in expected)
    assert not hasattr(stages, "_coverage_positions")
```

### `test_wrong_public_input_type_is_controlled_and_fast`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `argument`.

**Setup**

```python
kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "road_source": _road_source(),
        "source_config": SOURCE_CONFIG,
        "policy_path": None,
    }
kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()
proximity_stage.assert_not_called()
coverage_loader.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity"
    ) as proximity_stage, patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(**cast(Any, kwargs))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_wrong_public_input_type_is_controlled_and_fast(argument: str) -> None:
    kwargs: dict[str, object] = {
        "parcels": _parcels(),
        "road_source": _road_source(),
        "source_config": SOURCE_CONFIG,
        "policy_path": None,
    }
    kwargs[argument] = pd.DataFrame() if argument == "parcels" else object()
    with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity"
    ) as proximity_stage, patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(**cast(Any, kwargs))
    proximity_stage.assert_not_called()
    coverage_loader.assert_not_called()
```

### `test_source_chain_calls_proximity_then_coverage_exactly_once`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
road_source = _road_source(coverage.extraction)
parcels = _parcels()
proximity = _proximity(parcels)
policy_path = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
proximity_stage.assert_called_once_with(
        parcels, road_source, SOURCE_CONFIG, policy_path
    )
coverage_loader.assert_called_once_with(road_source.extraction, SOURCE_CONFIG)
```

**Action**

```python
with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=proximity,
    ) as proximity_stage, patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
        return_value=coverage,
    ) as coverage_loader:
        assess_road_proximity_coverage(
            parcels, road_source, SOURCE_CONFIG, policy_path
        )
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_source_chain_calls_proximity_then_coverage_exactly_once() -> None:
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels = _parcels()
    proximity = _proximity(parcels)
    policy_path = Path("configs/access/ign_bdtopo_vehicle_proxy_policy.yaml")
    with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=proximity,
    ) as proximity_stage, patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
        return_value=coverage,
    ) as coverage_loader:
        assess_road_proximity_coverage(
            parcels, road_source, SOURCE_CONFIG, policy_path
        )
    proximity_stage.assert_called_once_with(
        parcels, road_source, SOURCE_CONFIG, policy_path
    )
    coverage_loader.assert_called_once_with(road_source.extraction, SOURCE_CONFIG)
```

### `test_proximity_failure_stops_coverage_loading`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage_loader.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        side_effect=ValueError("bad proximity"),
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(_parcels(), _road_source(), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_proximity_failure_stops_coverage_loading() -> None:
    with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        side_effect=ValueError("bad proximity"),
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(_parcels(), _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()
```

### `test_coverage_loader_failure_is_controlled`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
coverage_loader.assert_called_once()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=_proximity(parcels),
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
        side_effect=ValueError("bad coverage"),
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_coverage_loader_failure_is_controlled() -> None:
    parcels = _parcels()
    with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=_proximity(parcels),
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
        side_effect=ValueError("bad coverage"),
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_called_once()
```

### `test_stage_does_not_construct_a_road_spatial_index`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
with patch("shapely.STRtree", side_effect=AssertionError("forbidden")):
        _assess()
source = Path(
        "src/landscout/stages/assess_road_proximity_coverage.py"
    ).read_text(encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert "STRtree(" not in source
assert "query_nearest(" not in source
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_stage_does_not_construct_a_road_spatial_index() -> None:
    with patch("shapely.STRtree", side_effect=AssertionError("forbidden")):
        _assess()
    source = Path(
        "src/landscout/stages/assess_road_proximity_coverage.py"
    ).read_text(encoding="utf-8")
    assert "STRtree(" not in source
    assert "query_nearest(" not in source
```

### `test_malformed_upstream_result_fails_before_coverage_load`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
parcels = _parcels()
malformed = mutation(_proximity(parcels))
coverage_loader.assert_not_called()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=malformed,
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_malformed_upstream_result_fails_before_coverage_load(mutation: Any) -> None:
    parcels = _parcels()
    malformed = mutation(_proximity(parcels))
    with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=malformed,
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage"
    ) as coverage_loader, pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
    coverage_loader.assert_not_called()
```

### `test_coverage_package_lineage_must_match_road_archive`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
coverage = _coverage()
frame = coverage.coverage.copy()
frame[field] = value
if field == "source_department_code":
        frame[coverage.summary.department_code_field] = value
        summary = replace(coverage.summary, selected_department_code=cast(str, value))
    else:
        summary = coverage.summary
forged = replace(coverage, coverage=frame, summary=summary, **{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityCoverageError, match="package|lineage|provider|product"):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_package_lineage_must_match_road_archive(
    field: str, value: object
) -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[field] = value
    if field == "source_department_code":
        frame[coverage.summary.department_code_field] = value
        summary = replace(coverage.summary, selected_department_code=cast(str, value))
    else:
        summary = coverage.summary
    forged = replace(coverage, coverage=frame, summary=summary, **{field: value})
    with pytest.raises(RoadProximityCoverageError, match="package|lineage|provider|product"):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))
```

### `test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage(layer="zone_administrative")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityCoverageError, match="configured|layer"):
        _assess(coverage=coverage, road_source=_road_source(coverage.extraction))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_configured_coverage_layer_cannot_be_replaced_by_real_alternate_layer() -> None:
    coverage = _coverage(layer="zone_administrative")
    with pytest.raises(RoadProximityCoverageError, match="configured|layer"):
        _assess(coverage=coverage, road_source=_road_source(coverage.extraction))
```

### `test_selected_department_identity_is_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
frame = coverage.coverage.copy()
frame[coverage.summary.department_code_field] = "32"
forged = replace(
        coverage,
        coverage=frame,
        summary=replace(coverage.summary, selected_department_code="32"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityCoverageError, match="department"):
        _assess(coverage=forged)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_selected_department_identity_is_exact() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame[coverage.summary.department_code_field] = "32"
    forged = replace(
        coverage,
        coverage=frame,
        summary=replace(coverage.summary, selected_department_code="32"),
    )
    with pytest.raises(RoadProximityCoverageError, match="department"):
        _assess(coverage=forged)
```

### `test_coverage_spatial_role_and_source_type_are_controlled`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
frame = coverage.coverage.copy()
frame["spatial_role"] = "PROXY_GEOMETRY"
wrong_role = replace(
        coverage,
        coverage=frame,
        summary=replace(
            coverage.summary,
            spatial_role=cast(Any, "PROXY_GEOMETRY"),
        ),
        spatial_role=cast(Any, "PROXY_GEOMETRY"),
    )
parcels = _parcels()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityCoverageError, match="spatial|lineage"):
        _assess(coverage=wrong_role)
with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=_proximity(parcels),
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
        return_value=object(),
    ), pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_coverage_spatial_role_and_source_type_are_controlled() -> None:
    coverage = _coverage()
    frame = coverage.coverage.copy()
    frame["spatial_role"] = "PROXY_GEOMETRY"
    wrong_role = replace(
        coverage,
        coverage=frame,
        summary=replace(
            coverage.summary,
            spatial_role=cast(Any, "PROXY_GEOMETRY"),
        ),
        spatial_role=cast(Any, "PROXY_GEOMETRY"),
    )
    with pytest.raises(RoadProximityCoverageError, match="spatial|lineage"):
        _assess(coverage=wrong_role)

    parcels = _parcels()
    with patch(
        "landscout.stages.assess_road_proximity_coverage.enrich_parcel_road_proximity",
        return_value=_proximity(parcels),
    ), patch(
        "landscout.stages.assess_road_proximity_coverage.load_ign_bdtopo_department_coverage",
        return_value=object(),
    ), pytest.raises(RoadProximityCoverageError):
        assess_road_proximity_coverage(parcels, _road_source(), SOURCE_CONFIG)
```

### `test_coverage_must_retain_same_extraction_object`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
forged = replace(coverage, extraction=replace(coverage.extraction))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityCoverageError, match="extraction"):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coverage_must_retain_same_extraction_object() -> None:
    coverage = _coverage()
    forged = replace(coverage, extraction=replace(coverage.extraction))
    with pytest.raises(RoadProximityCoverageError, match="extraction"):
        _assess(coverage=forged, road_source=_road_source(coverage.extraction))
```

### `test_invalid_coverage_geometry_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `crs`, `geometries`, `message`.

**Setup**

```python
coverage = _coverage(geometries=geometries, crs=crs)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityCoverageError, match=message):
        _assess(coverage=coverage)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_coverage_geometry_is_rejected(
    geometries: list[object], crs: str | None, message: str
) -> None:
    coverage = _coverage(geometries=geometries, crs=crs)
    with pytest.raises(RoadProximityCoverageError, match=message):
        _assess(coverage=coverage)
```

### `test_polygonal_coverage_geometry_is_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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
assert len(_assess(coverage=_coverage(geometries=[geometry])).parcels) == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_polygonal_coverage_geometry_is_accepted(geometry: object) -> None:
    assert len(_assess(coverage=_coverage(geometries=[geometry])).parcels) == 1
```

### `test_full_parcel_coverage_position_is_conservative`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`, `position`.

**Setup**

```python
parcels = _parcels([geometry])
row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
if position != "FULLY_COVERED":
        assert row.road_source_boundary_distance_m == 0.0
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_source_coverage_position == position
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_full_parcel_coverage_position_is_conservative(
    geometry: Polygon, position: str
) -> None:
    parcels = _parcels([geometry])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == position
    if position != "FULLY_COVERED":
        assert row.road_source_boundary_distance_m == 0.0
```

### `test_position_uses_full_geometry_not_centroid`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
crossing_with_inside_centroid = Polygon(
        [(-10, 100), (-10, 200), (300, 200), (300, 100), (-10, 100)]
    )
parcels = _parcels([crossing_with_inside_centroid])
row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert row.road_source_coverage_position == "OUTSIDE_OR_CROSSING_COVERAGE"
assert row.road_source_boundary_distance_m == 0.0
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_position_uses_full_geometry_not_centroid() -> None:
    crossing_with_inside_centroid = Polygon(
        [(-10, 100), (-10, 200), (300, 200), (300, 100), (-10, 100)]
    )
    parcels = _parcels([crossing_with_inside_centroid])
    row = _first_row(_assess(parcels=parcels, proximity=_proximity(parcels)))
    assert row.road_source_coverage_position == "OUTSIDE_OR_CROSSING_COVERAGE"
    assert row.road_source_boundary_distance_m == 0.0
```

### `test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
coverage = _coverage()
expected = _measured_boundary_distance(parcels, coverage)
result = _assess(parcels=parcels, proximity=_proximity(parcels), coverage=coverage)
values = result.class_proximity["road_source_boundary_distance_m"]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert values.eq(expected).all()
assert np.isfinite(values).all()
assert values.ge(0).all()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_internal_boundary_distance_is_full_geometry_finite_and_nonnegative() -> None:
    parcels = _parcels()
    coverage = _coverage()
    expected = _measured_boundary_distance(parcels, coverage)
    result = _assess(parcels=parcels, proximity=_proximity(parcels), coverage=coverage)
    values = result.class_proximity["road_source_boundary_distance_m"]
    assert values.eq(expected).all()
    assert np.isfinite(values).all()
    assert values.ge(0).all()
```

### `test_strict_boundary_status_logic`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected`, `offset`.

**Setup**

```python
parcels = _parcels()
coverage = _coverage()
margin = _measured_boundary_distance(parcels, coverage)
proximity = _proximity(
        parcels, distances={road_class: margin + offset for road_class in ELIGIBLE_CLASSES}
    )
result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.class_proximity["road_proximity_coverage_status"].eq(expected).all()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_strict_boundary_status_logic(offset: float, expected: str) -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels, distances={road_class: margin + offset for road_class in ELIGIBLE_CLASSES}
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert result.class_proximity["road_proximity_coverage_status"].eq(expected).all()
```

### `test_matched_outside_or_crossing_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
parcels = _parcels([geometry])
result = _assess(parcels=parcels, proximity=_proximity(parcels))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.class_proximity["road_proximity_coverage_status"].eq(
        "OUTSIDE_OR_CROSSING_COVERAGE"
    ).all()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_matched_outside_or_crossing_status(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    result = _assess(parcels=parcels, proximity=_proximity(parcels))
    assert result.class_proximity["road_proximity_coverage_status"].eq(
        "OUTSIDE_OR_CROSSING_COVERAGE"
    ).all()
```

### `test_no_match_takes_precedence_over_coverage_position`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry`.

**Setup**

```python
parcels = _parcels([geometry])
proximity = _without_match(_proximity(parcels))
result = _assess(parcels=parcels, proximity=proximity)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _first_row(result, "UNKNOWN_REVIEW").road_proximity_coverage_status == "NO_MATCH"
```

**Regression protected**

Pins the configured policy-rule ordering so a lower-priority observation cannot replace the controlling evidence.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_no_match_takes_precedence_over_coverage_position(geometry: Polygon) -> None:
    parcels = _parcels([geometry])
    proximity = _without_match(_proximity(parcels))
    result = _assess(parcels=parcels, proximity=proximity)
    assert _first_row(result, "UNKNOWN_REVIEW").road_proximity_coverage_status == "NO_MATCH"
```

### `test_classes_are_diagnosed_independently`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels()
coverage = _coverage()
margin = _measured_boundary_distance(parcels, coverage)
proximity = _proximity(
        parcels,
        distances={
            "GENERAL_VEHICLE_PROXY": margin - 1,
            "RESTRICTED_REVIEW": margin + 1,
        },
    )
result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert _first_row(result, "GENERAL_VEHICLE_PROXY").road_proximity_coverage_status == "NOT_BOUNDARY_LIMITED"
assert _first_row(result, "RESTRICTED_REVIEW").road_proximity_coverage_status == "BOUNDARY_LIMITED"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_classes_are_diagnosed_independently() -> None:
    parcels = _parcels()
    coverage = _coverage()
    margin = _measured_boundary_distance(parcels, coverage)
    proximity = _proximity(
        parcels,
        distances={
            "GENERAL_VEHICLE_PROXY": margin - 1,
            "RESTRICTED_REVIEW": margin + 1,
        },
    )
    result = _assess(parcels=parcels, proximity=proximity, coverage=coverage)
    assert _first_row(result, "GENERAL_VEHICLE_PROXY").road_proximity_coverage_status == "NOT_BOUNDARY_LIMITED"
    assert _first_row(result, "RESTRICTED_REVIEW").road_proximity_coverage_status == "BOUNDARY_LIMITED"
```

### `test_exact_coverage_lineage_is_appended_to_every_row`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
coverage = _coverage()
result = _assess(coverage=coverage)
expected = {
        "road_source_coverage_provider": coverage.source_provider,
        "road_source_coverage_product": coverage.source_product,
        "road_source_coverage_department_code": coverage.source_department_code,
        "road_source_coverage_edition": coverage.source_edition,
        "road_source_coverage_product_version": coverage.source_product_version,
        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,
        "road_source_coverage_layer": coverage.source_layer,
        "road_source_coverage_spatial_role": coverage.spatial_role,
    }
for column, value in expected.items():
        assert result.class_proximity[column].eq(value).all()
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

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_coverage_lineage_is_appended_to_every_row() -> None:
    coverage = _coverage()
    result = _assess(coverage=coverage)
    expected = {
        "road_source_coverage_provider": coverage.source_provider,
        "road_source_coverage_product": coverage.source_product,
        "road_source_coverage_department_code": coverage.source_department_code,
        "road_source_coverage_edition": coverage.source_edition,
        "road_source_coverage_product_version": coverage.source_product_version,
        "road_source_coverage_archive_sha256": coverage.source_archive_sha256,
        "road_source_coverage_layer": coverage.source_layer,
        "road_source_coverage_spatial_role": coverage.spatial_role,
    }
    for column, value in expected.items():
        assert result.class_proximity[column].eq(value).all()
```

### `test_matched_road_lineage_must_match_coverage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
proximity = _proximity()
table = proximity.class_proximity.copy()
table[column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(RoadProximityCoverageError, match="lineage|package"):
        _assess(proximity=replace(proximity, class_proximity=table))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_matched_road_lineage_must_match_coverage(
    column: str, value: str
) -> None:
    proximity = _proximity()
    table = proximity.class_proximity.copy()
    table[column] = value
    with pytest.raises(RoadProximityCoverageError, match="lineage|package"):
        _assess(proximity=replace(proximity, class_proximity=table))
```

### `test_result_preserves_every_upstream_fact_and_input_object`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
parcels = _parcels(
        [
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            Polygon([(300, 300), (300, 400), (400, 400), (400, 300), (300, 300)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
proximity = _proximity(parcels)
coverage = _coverage()
road_source = _road_source(coverage.extraction)
parcels_before = deepcopy(parcels)
proximity_parcels_before = deepcopy(proximity.parcels)
table_before = deepcopy(proximity.class_proximity)
coverage_before = deepcopy(coverage.coverage)
roads_before = deepcopy(road_source.road_segments)
road_summary_before = road_source.road_segments_summary
extraction_before = road_source.extraction
config_before = SOURCE_CONFIG.model_dump(mode="python")
result = _assess(
        parcels=parcels,
        proximity=proximity,
        coverage=coverage,
        road_source=road_source,
    )
assert_geodataframe_equal(parcels, parcels_before)
assert_geodataframe_equal(proximity.parcels, proximity_parcels_before)
assert_frame_equal(proximity.class_proximity, table_before)
assert_geodataframe_equal(coverage.coverage, coverage_before)
assert_geodataframe_equal(road_source.road_segments, roads_before)
assert_geodataframe_equal(result.parcels, proximity_parcels_before)
assert_frame_equal(
        result.class_proximity.loc[:, list(CLASS_PROXIMITY_COLUMNS)],
        table_before,
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
assert road_source.road_segments_summary == road_summary_before
assert road_source.extraction is extraction_before
assert SOURCE_CONFIG.model_dump(mode="python") == config_before
assert tuple(result.class_proximity.columns[: len(CLASS_PROXIMITY_COLUMNS)]) == CLASS_PROXIMITY_COLUMNS
assert tuple(result.class_proximity.columns[len(CLASS_PROXIMITY_COLUMNS) :]) == DIAGNOSTIC_COLUMNS
assert result.class_coverage is proximity.class_coverage
assert result.source_coverage is coverage
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_result_preserves_every_upstream_fact_and_input_object() -> None:
    parcels = _parcels(
        [
            Polygon([(100, 100), (100, 200), (200, 200), (200, 100), (100, 100)]),
            Polygon([(300, 300), (300, 400), (400, 400), (400, 300), (300, 300)]),
        ],
        identifiers=["SECOND", "FIRST"],
    )
    proximity = _proximity(parcels)
    coverage = _coverage()
    road_source = _road_source(coverage.extraction)
    parcels_before = deepcopy(parcels)
    proximity_parcels_before = deepcopy(proximity.parcels)
    table_before = deepcopy(proximity.class_proximity)
    coverage_before = deepcopy(coverage.coverage)
    roads_before = deepcopy(road_source.road_segments)
    road_summary_before = road_source.road_segments_summary
    extraction_before = road_source.extraction
    config_before = SOURCE_CONFIG.model_dump(mode="python")
    result = _assess(
        parcels=parcels,
        proximity=proximity,
        coverage=coverage,
        road_source=road_source,
    )

    assert_geodataframe_equal(parcels, parcels_before)
    assert_geodataframe_equal(proximity.parcels, proximity_parcels_before)
    assert_frame_equal(proximity.class_proximity, table_before)
    assert_geodataframe_equal(coverage.coverage, coverage_before)
    assert_geodataframe_equal(road_source.road_segments, roads_before)
    assert road_source.road_segments_summary == road_summary_before
    assert road_source.extraction is extraction_before
    assert SOURCE_CONFIG.model_dump(mode="python") == config_before
    assert_geodataframe_equal(result.parcels, proximity_parcels_before)
    assert_frame_equal(
        result.class_proximity.loc[:, list(CLASS_PROXIMITY_COLUMNS)],
        table_before,
        check_dtype=True,
        check_index_type=True,
    )
    assert tuple(result.class_proximity.columns[: len(CLASS_PROXIMITY_COLUMNS)]) == CLASS_PROXIMITY_COLUMNS
    assert tuple(result.class_proximity.columns[len(CLASS_PROXIMITY_COLUMNS) :]) == DIAGNOSTIC_COLUMNS
    assert result.class_coverage is proximity.class_coverage
    assert result.source_coverage is coverage
```

### `_corrupt_generated`

**Exact signature**

```python
def _corrupt_generated(column: str, value: object, *, outside: bool = False) -> None:
```

**Purpose**

Private `test` helper for corrupt generated; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output.at[0, column]`, `output[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_malformed_generated_value_is_rejected` via `_corrupt_generated`.
- direct call or construction: `tests/unit/test_assess_road_proximity_coverage.py::test_outside_position_requires_zero_boundary_distance` via `_corrupt_generated`.

**Complete source-ordered implementation**

```python
def _corrupt_generated(column: str, value: object, *, outside: bool = False) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    geometry = (
        Polygon([(-200, 100), (-200, 200), (-100, 200), (-100, 100), (-200, 100)])
        if outside
        else None
    )
    parcels = _parcels([geometry]) if geometry is not None else _parcels()
    proximity = _proximity(parcels)
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output[column] = output[column].astype("object")
        output.at[0, column] = value
        return output

    with patch.object(
        module, "_diagnosed_class_proximity", side_effect=corrupt
    ), pytest.raises(RoadProximityCoverageError):
        _assess(parcels=parcels, proximity=proximity)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_corrupt_generated.corrupt`

**Exact signature**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for corrupt; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output.at[0, column]`, `output[column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `patch.object(module, '_diagnosed_class_proximity', side_effect=corrupt)`.
- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `patch.object(module, '_diagnosed_class_proximity', side_effect=corrupt)`.

**Complete source-ordered implementation**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output[column] = output[column].astype("object")
        output.at[0, column] = value
        return output
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_generated_value_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
_corrupt_generated(column, value)
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

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_generated_value_is_rejected(column: str, value: object) -> None:
    _corrupt_generated(column, value)
```

### `test_inconsistent_generated_status_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `distance`, `wrong_status`.

**Setup**

```python
module = import_module("landscout.stages.assess_road_proximity_coverage")
parcels = _parcels()
proximity = _proximity(
        parcels, distances={road_class: distance for road_class in ELIGIBLE_CLASSES}
    )
original = module._diagnosed_class_proximity
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output.at[0, "road_proximity_coverage_status"] = wrong_status
        return output
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with patch.object(
        module, "_diagnosed_class_proximity", side_effect=corrupt
    ), pytest.raises(RoadProximityCoverageError):
        _assess(parcels=parcels, proximity=proximity)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_inconsistent_generated_status_is_rejected(
    distance: float, wrong_status: str
) -> None:
    module = import_module("landscout.stages.assess_road_proximity_coverage")

    parcels = _parcels()
    proximity = _proximity(
        parcels, distances={road_class: distance for road_class in ELIGIBLE_CLASSES}
    )
    original = module._diagnosed_class_proximity

    def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output.at[0, "road_proximity_coverage_status"] = wrong_status
        return output

    with patch.object(
        module, "_diagnosed_class_proximity", side_effect=corrupt
    ), pytest.raises(RoadProximityCoverageError):
        _assess(parcels=parcels, proximity=proximity)
```

### `test_inconsistent_generated_status_is_rejected.corrupt`

**Exact signature**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Private `test` helper for corrupt; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output.at[0, 'road_proximity_coverage_status']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::_corrupt_generated` via `patch.object(module, '_diagnosed_class_proximity', side_effect=corrupt)`.
- callback/function object: `tests/unit/test_assess_road_proximity_coverage.py::test_inconsistent_generated_status_is_rejected` via `patch.object(module, '_diagnosed_class_proximity', side_effect=corrupt)`.

**Complete source-ordered implementation**

```python
def corrupt(*args: object, **kwargs: object) -> pd.DataFrame:
        output = original(*args, **kwargs)
        output.at[0, "road_proximity_coverage_status"] = wrong_status
        return output
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_outside_position_requires_zero_boundary_distance`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_corrupt_generated("road_source_boundary_distance_m", 1.0, outside=True)
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

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_outside_position_requires_zero_boundary_distance() -> None:
    _corrupt_generated("road_source_boundary_distance_m", 1.0, outside=True)
```

### `test_result_is_frozen_and_has_no_business_decision_fields`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _assess()
forbidden = {
        "accessible",
        "road_access_ok",
        "legal_access",
        "truck_access",
        "bess_access",
        "score",
        "retained",
        "rejected",
    }
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()
assert forbidden.isdisjoint(result.parcels.columns)
assert forbidden.isdisjoint(result.class_proximity.columns)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_result_is_frozen_and_has_no_business_decision_fields() -> None:
    result = _assess()
    with pytest.raises(FrozenInstanceError):
        result.parcels = _parcels()  # type: ignore[misc]
    forbidden = {
        "accessible",
        "road_access_ok",
        "legal_access",
        "truck_access",
        "bess_access",
        "score",
        "retained",
        "rejected",
    }
    assert forbidden.isdisjoint(result.parcels.columns)
    assert forbidden.isdisjoint(result.class_proximity.columns)
```


## 7. Data contracts

### `DIAGNOSTIC_COLUMNS` — canonical or derived frame-column schema

```python
DIAGNOSTIC_COLUMNS = (
    "road_source_boundary_distance_m",
    "road_source_coverage_position",
    "road_proximity_coverage_status",
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
