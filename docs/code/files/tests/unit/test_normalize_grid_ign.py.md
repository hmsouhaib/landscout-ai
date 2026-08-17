# `tests/unit/test_normalize_grid_ign.py`

## File identity

- Repository path: `tests/unit/test_normalize_grid_ign.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.
- Source SHA256: `2ef2f253fa949fff73772dd7e05f6f46a0d8b1bccafb33606ad21b2be108c345`

## 1. Purpose

Provides complete unit and regression coverage for the `normalize_grid_ign` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import tempfile`
- `from copy import deepcopy`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from math import isfinite`
- `from pathlib import Path`
- `from typing import Any, Literal, cast`
- `from uuid import uuid4`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import pyogrio`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `import landscout.stages.normalize_grid_ign as grid_normalization`
- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoElectricityData,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.normalize_grid_ign import (
    LINE_OUTPUT_COLUMNS,
    TRANSFORMATION_POST_OUTPUT_COLUMNS,
    IgnGridNormalizationError,
    NormalizedIgnElectricityData,
    parse_ign_voltage,
)`
- `from landscout.stages.normalize_grid_ign import (
    _IgnGridSourceContext as IgnGridSourceContext,
)`
- `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_electric_lines as normalize_ign_electric_lines,
)`
- `from landscout.stages.normalize_grid_ign import (
    _normalize_ign_transformation_posts as normalize_ign_transformation_posts,
)`
- `from landscout.stages.normalize_grid_ign import (
    normalize_ign_electricity as _normalize_ign_electricity,
)`

## 4. Contract taxonomy

### A. Python constants

#### `LINE_LAYER`

```python
LINE_LAYER = "LIGNE_ELECTRIQUE_V2"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::test_layer_loader_retains_crs_counts_and_null_geometries` (value argument/reference), `tests/unit/test_ign_bdtopo_fr.py::test_geographic_crs_is_rejected` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_valid_line_has_stable_identity_lineage_and_range_index` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_does_not_override_source_asset_status` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_null_or_empty_line_cleabs_fails` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_unsafe_source_id_is_rejected_without_rewriting` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_duplicate_line_cleabs_fails` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_line_missing_or_wrong_crs_fails` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_z_coordinates_are_preserved` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_unusual_duplicate_source_index_is_not_preserved_as_identity` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_line_normalization_does_not_mutate_input_and_has_stable_columns` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_missing_required_line_field_fails` (value argument/reference).

#### `POST_LAYER`

```python
POST_LAYER = "POSTE_DE_TRANSFORMATION_V2"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::test_invalid_geometry_is_preserved_without_repair` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_valid_post_has_stable_lineage_and_no_voltage_inference` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_post_geometry_crs_and_input_are_preserved` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_duplicate_post_cleabs_fails` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_null_post_geometry_and_precision_are_preserved` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_invalid_post_precision_fails` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::test_valid_line_or_point_is_rejected_as_transformation_post` (value argument/reference).

#### `ARCHIVE_SHA256`

```python
ARCHIVE_SHA256 = "a" * 64
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract. Consumers include `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::_coverage` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_road_proximity_coverage.py::_archive` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_enrich_planning_zoning.py::_planning_document` (value argument/reference), `tests/unit/test_normalize_access_ign.py::_source` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_context` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference).

#### `SOURCE_URL`

```python
SOURCE_URL = "https://example.test/BDTOPO_D031.7z"
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `tests/unit/test_normalize_access_ign.py::_source` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_context` (value argument/reference), `tests/unit/test_normalize_grid_ign.py::_source_bundle` (value argument/reference).

#### `_FIXTURE_ROOT`

```python
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-grid-ign-"))
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_SOURCE_CONFIG_PAYLOAD`

```python
_SOURCE_CONFIG_PAYLOAD = load_ign_bdtopo_source_config().model_dump(mode="json")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_normalize_grid_ign.py::<module>` (value argument/reference).

#### `SOURCE_CONFIG`

```python
SOURCE_CONFIG = IgnBdTopoSourceConfig.model_validate(_SOURCE_CONFIG_PAYLOAD)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` (value argument/reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `normalize_ign_electricity`

**Exact signature**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
```

**Purpose**

Source-completely revalidates configured IGN electricity layers once and projects them into stable factual line and transformation-post catalogs.

**Return contract**

- Declared return annotation: `NormalizedIgnElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
_normalize_ign_electricity(source, SOURCE_CONFIG)
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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    IgnGridNormalizationError,
    IgnVoltageNormalization,
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
    parse_ign_voltage,
)`.
- direct call or construction: `src/landscout/stages/enrich_grid_proximity.py::enrich_parcel_grid_proximity` via `normalize_ign_electricity`.
- import/re-export: `src/landscout/stages/enrich_grid_proximity.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    NormalizedIgnElectricityData,
    normalize_ign_electricity,
)`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_supported_package_api_keeps_high_level_normalization` via `stages.normalize_ign_electricity`.
- property/attribute access: `tests/unit/test_normalize_grid_ign.py::test_supported_package_api_keeps_high_level_normalization` via `stages.normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_grid_summary_requires_strict_structural_types` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_grid_archive_sha256_requires_canonical_lowercase` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_path_uses_discovered_layer_names_and_archive_lineage` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_source_complete_grid_validation_does_not_mutate_supplied_frames` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_incompatible_archive_identity` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_row_count_mismatch` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_layer_name_mismatch` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_wrong_logical_name` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_crs_mismatch` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_forged_ordered_summary_schema` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_colliding_electricity_roles` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `normalize_ign_electricity`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_any_spatial_role_mismatch` via `normalize_ign_electricity`.
- import/re-export: `tests/unit/test_normalize_grid_ign.py::<module>` via `from landscout.stages.normalize_grid_ign import (
    normalize_ign_electricity as _normalize_ign_electricity,
)`.

**Complete source-ordered implementation**

```python
def normalize_ign_electricity(
    source: IgnBdTopoElectricityData,
) -> NormalizedIgnElectricityData:
    return _normalize_ign_electricity(source, SOURCE_CONFIG)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_line_source`

**Exact signature**

```python
def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for line source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'cleabs': source_ids, 'voltage': source_voltages, 'gestionnaire': ["Réseau de Transport d'Électricité"] * count, 'siren_gestionnaire': ['444619258'] * count, 'etat_de_l_objet': ['En service'] * count, 'sources': ['RTE 2024'] * count, 'identifiants_sources': ['source-id'] * count, 'date_creation': pd.to_datetime(['2024-01-01'] * count), 'date_modification': pd.to_datetime(['2025-01-01'] * count), 'date_de_confirmation': pd.to_datetime(['2024-12-18'] * count), 'methode_d_acquisition_planimetrique': ['Photogrammétrie'] * count, 'precision_planimetrique': source_precisions}, geometry=source_geometries, crs=crs, index=source_index)
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

- direct call or construction: `tests/unit/test_normalize_grid_ign.py::_source_bundle` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_line_has_stable_identity_lineage_and_range_index` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_does_not_override_source_asset_status` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_null_or_empty_line_cleabs_fails` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_unsafe_source_id_is_rejected_without_rewriting` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_duplicate_line_cleabs_fails` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_line_missing_or_wrong_crs_fails` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_z_coordinates_are_preserved` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_missing_required_line_field_fails` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_or_null_line_precision_is_normalized_to_float` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_invalid_line_precision_fails` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_normalized_voltage_never_emits_non_finite_numeric_values` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted` via `_line_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_polygon_or_point_is_rejected_as_electric_line` via `_line_source`.

**Complete source-ordered implementation**

```python
def _line_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    voltages: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries
        if geometries is not None
        else [LineString([(0, 0), (100, 100)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"LIGNE-{item + 1}" for item in range(count)]
    )
    source_voltages = voltages if voltages is not None else ["225 kV"] * count
    source_precisions = precisions if precisions is not None else [2.5] * count
    source_index = index if index is not None else [100 + item for item in range(count)]
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "voltage": source_voltages,
            "gestionnaire": ["Réseau de Transport d'Électricité"] * count,
            "siren_gestionnaire": ["444619258"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2024"] * count,
            "identifiants_sources": ["source-id"] * count,
            "date_creation": pd.to_datetime(["2024-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-01-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2024-12-18"] * count),
            "methode_d_acquisition_planimetrique": ["Photogrammétrie"]
            * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_post_source`

**Exact signature**

```python
def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for post source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'cleabs': source_ids, 'toponyme': ['Poste de test'] * count, 'statut_du_toponyme': ['Validé'] * count, 'importance': ['5'] * count, 'etat_de_l_objet': ['En service'] * count, 'sources': ['RTE 2021'] * count, 'identifiants_sources': ['source-post-id'] * count, 'date_creation': pd.to_datetime(['2023-01-01'] * count), 'date_modification': pd.to_datetime(['2025-02-01'] * count), 'date_de_confirmation': pd.to_datetime(['2025-01-15'] * count), 'methode_d_acquisition_planimetrique': ['Orthophotographie'] * count, 'precision_planimetrique': source_precisions}, geometry=source_geometries, crs=crs, index=source_index)
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

- direct call or construction: `tests/unit/test_normalize_grid_ign.py::_source_bundle` via `_post_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `_post_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_post_geometry_crs_and_input_are_preserved` via `_post_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_duplicate_post_cleabs_fails` via `_post_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_null_post_geometry_and_precision_are_preserved` via `_post_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_invalid_post_precision_fails` via `_post_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted` via `_post_source`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_line_or_point_is_rejected_as_transformation_post` via `_post_source`.

**Complete source-ordered implementation**

```python
def _post_source(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    precisions: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = (
        geometries
        if geometries is not None
        else [Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])]
    )
    count = len(source_geometries)
    source_ids = (
        identifiers
        if identifiers is not None
        else [f"POSTE-{item + 1}" for item in range(count)]
    )
    source_precisions = precisions if precisions is not None else [5.0] * count
    source_index = index if index is not None else [200 + item for item in range(count)]
    return gpd.GeoDataFrame(
        {
            "cleabs": source_ids,
            "toponyme": ["Poste de test"] * count,
            "statut_du_toponyme": ["Validé"] * count,
            "importance": ["5"] * count,
            "etat_de_l_objet": ["En service"] * count,
            "sources": ["RTE 2021"] * count,
            "identifiants_sources": ["source-post-id"] * count,
            "date_creation": pd.to_datetime(["2023-01-01"] * count),
            "date_modification": pd.to_datetime(["2025-02-01"] * count),
            "date_de_confirmation": pd.to_datetime(["2025-01-15"] * count),
            "methode_d_acquisition_planimetrique": ["Orthophotographie"]
            * count,
            "precision_planimetrique": source_precisions,
        },
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_context`

**Exact signature**

```python
def _context(source_layer: str) -> IgnGridSourceContext:
```

**Purpose**

Private `test` helper for context; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnGridSourceContext`.
- Every observed return expression is reproduced without truncation:
```python
IgnGridSourceContext(source_layer=source_layer, department_code='31', edition='2026-06-15', product_version='3.5', download_timestamp='2026-08-11T15:32:03+00:00', archive_sha256=ARCHIVE_SHA256, source_url=SOURCE_URL)
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

- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_accepts_supported_department_codes` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_uppercase_sha256` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_internal_source_context_rejects_invalid_lineage_values` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_line_has_stable_identity_lineage_and_range_index` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_deenergized_voltage_does_not_override_source_asset_status` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_null_or_empty_line_cleabs_fails` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_unsafe_source_id_is_rejected_without_rewriting` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_duplicate_line_cleabs_fails` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_line_missing_or_wrong_crs_fails` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_line_geometry_quality_is_preserved_without_row_loss_or_repair` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_z_coordinates_are_preserved` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_unusual_duplicate_source_index_is_not_preserved_as_identity` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_line_normalization_does_not_mutate_input_and_has_stable_columns` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_missing_required_line_field_fails` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_or_null_line_precision_is_normalized_to_float` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_invalid_line_precision_fails` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_normalized_voltage_never_emits_non_finite_numeric_values` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_post_has_stable_lineage_and_no_voltage_inference` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_post_geometry_crs_and_input_are_preserved` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_duplicate_post_cleabs_fails` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_null_post_geometry_and_precision_are_preserved` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_invalid_post_precision_fails` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_appropriate_multigeometry_types_are_accepted` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_polygon_or_point_is_rejected_as_electric_line` via `_context`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_valid_line_or_point_is_rejected_as_transformation_post` via `_context`.

**Complete source-ordered implementation**

```python
def _context(source_layer: str) -> IgnGridSourceContext:
    return IgnGridSourceContext(
        source_layer=source_layer,
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        download_timestamp="2026-08-11T15:32:03+00:00",
        archive_sha256=ARCHIVE_SHA256,
        source_url=SOURCE_URL,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_summary`

**Exact signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    logical_name: Literal["electric_lines", "transformation_posts"],
    layer_name: str,
) -> IgnBdTopoLayerSummary:
```

**Purpose**

Private `test` helper for summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoLayerSummary(logical_name=logical_name, source_layer_name=layer_name, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), invalid_geometry_count=int(invalid_mask.sum()), geometry_types=geometry_types)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `geometry.isna`, `geometry[~null_mask].geom_type.dropna`, `geometry[~null_mask].geom_type.dropna().unique`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_enrich_planning_features.py::_inspected` via `_summary`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_materialize_layer` via `_summary`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_planning_document` via `_summary`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::test_prescription_surface_uses_validated_source_ogr_fid_when_cnig_id_absent` via `_summary`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_replace_related_layer` via `_summary`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `_summary`.
- direct call or construction: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `_summary`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::_write_zoning_source` via `_summary`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::_source` via `_summary`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `_summary`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::_source_bundle` via `_summary`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `_summary`.

**Complete source-ordered implementation**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    logical_name: Literal["electric_lines", "transformation_posts"],
    layer_name: str,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    geometry_types = tuple(
        sorted(str(value) for value in geometry[~null_mask].geom_type.dropna().unique())
    )
    return IgnBdTopoLayerSummary(
        logical_name=logical_name,
        source_layer_name=layer_name,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in frame.dtypes.items()),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=geometry_types,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source_bundle`

**Exact signature**

```python
def _source_bundle(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
```

**Purpose**

Private `test` helper for source bundle; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoElectricityData(extraction=extraction, electric_lines=line_frame, transformation_posts=post_frame, electric_lines_summary=_summary(line_frame, 'electric_lines', LINE_LAYER), transformation_posts_summary=_summary(post_frame, 'transformation_posts', POST_LAYER))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: `IgnBdTopoDownload`.
- Filesystem read: `geopackage_path.read_bytes`, `gpd.read_file`.
- Filesystem write: `(extraction_path / '.landscout-extraction.json').write_text`, `extraction_path.mkdir`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_normalize_grid_ign.py::_source_bundle_with_archive` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_supported_package_api_keeps_high_level_normalization` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_grid_summary_requires_strict_structural_types` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_path_uses_discovered_layer_names_and_archive_lineage` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_coordinated_frame_and_summary_forgery` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_source_complete_grid_validation_does_not_mutate_supplied_frames` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_row_count_mismatch` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_layer_name_mismatch` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_wrong_logical_name` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_summary_crs_mismatch` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_forged_ordered_summary_schema` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_duplicate_or_missing_layer_inventory` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_colliding_electricity_roles` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_counts_after_frame_mutation` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_stale_geometry_types_after_frame_mutation` via `_source_bundle`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_any_spatial_role_mismatch` via `_source_bundle`.

**Complete source-ordered implementation**

```python
def _source_bundle(
    lines: gpd.GeoDataFrame | None = None,
    posts: gpd.GeoDataFrame | None = None,
) -> IgnBdTopoElectricityData:
    line_frame = lines if lines is not None else _line_source()
    post_frame = posts if posts is not None else _post_source()
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    pyogrio.write_dataframe(line_frame, geopackage_path, layer=LINE_LAYER, driver="GPKG")
    pyogrio.write_dataframe(
        post_frame,
        geopackage_path,
        layer=POST_LAYER,
        driver="GPKG",
        append=True,
    )
    line_frame = gpd.read_file(geopackage_path, layer=LINE_LAYER, engine="pyogrio")
    post_frame = gpd.read_file(geopackage_path, layer=POST_LAYER, engine="pyogrio")
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker = {
        "schema_version": 2,
        "archive_sha256": ARCHIVE_SHA256,
        "geopackage_relative_path": "data.gpkg",
        "geopackage_size_bytes": len(payload),
        "geopackage_sha256": digest,
        "all_layer_names": list(layer_names),
        "electric_lines_layer": LINE_LAYER,
        "transformation_posts_layer": POST_LAYER,
        "spatial_role": "PROXY_GEOMETRY",
    }
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(marker), encoding="utf-8"
    )
    archive = IgnBdTopoDownload(
        provider="Institut national de l'information géographique et forestière",
        product="BD TOPO",
        department_code="31",
        edition="2026-06-15",
        product_version="3.5",
        projection="EPSG:2154",
        package_format="GPKG",
        archive_format="7z",
        source_url=SOURCE_URL,
        checksum_url=None,
        download_timestamp="2026-08-11T15:32:03+00:00",
        filename="BDTOPO_D031.7z",
        file_size=1234,
        sha256=ARCHIVE_SHA256,
        official_checksum_algorithm=None,
        official_checksum=None,
        official_checksum_validated=False,
        path=Path("cache/BDTOPO_D031.7z"),
        cache_hit=True,
    )
    extraction = IgnBdTopoExtraction(
        archive=archive,
        extraction_path=extraction_path,
        geopackage_path=geopackage_path,
        geopackage_filename="data.gpkg",
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
        electric_lines_layer=LINE_LAYER,
        transformation_posts_layer=POST_LAYER,
        cache_hit=True,
    )
    return IgnBdTopoElectricityData(
        extraction=extraction,
        electric_lines=line_frame,
        transformation_posts=post_frame,
        electric_lines_summary=_summary(line_frame, "electric_lines", LINE_LAYER),
        transformation_posts_summary=_summary(
            post_frame, "transformation_posts", POST_LAYER
        ),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source_bundle_with_archive`

**Exact signature**

```python
def _source_bundle_with_archive(**changes: object) -> IgnBdTopoElectricityData:
```

**Purpose**

Private `test` helper for source bundle with archive; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoElectricityData`.
- Every observed return expression is reproduced without truncation:
```python
replace(source, extraction=replace(source.extraction, archive=archive))
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

- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_grid_archive_sha256_requires_canonical_lowercase` via `_source_bundle_with_archive`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_high_level_rejects_incompatible_archive_identity` via `_source_bundle_with_archive`.
- direct call or construction: `tests/unit/test_normalize_grid_ign.py::test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant` via `_source_bundle_with_archive`.

**Complete source-ordered implementation**

```python
def _source_bundle_with_archive(**changes: object) -> IgnBdTopoElectricityData:
    source = _source_bundle()
    archive = replace(source.extraction.archive, **changes)
    return replace(source, extraction=replace(source.extraction, archive=archive))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_low_level_normalization_is_not_part_of_stages_public_api`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `name`.

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
assert name not in stages.__all__
assert not hasattr(stages, name)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_low_level_normalization_is_not_part_of_stages_public_api(name: str) -> None:
    assert name not in stages.__all__
    assert not hasattr(stages, name)
```

### `test_supported_package_api_keeps_high_level_normalization`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
expected_names = {
        "IgnGridNormalizationError",
        "IgnVoltageNormalization",
        "NormalizedIgnElectricityData",
        "parse_ign_voltage",
        "normalize_ign_electricity",
    }
normalized = stages.normalize_ign_electricity(_source_bundle(), SOURCE_CONFIG)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert expected_names <= set(stages.__all__)
assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_supported_package_api_keeps_high_level_normalization() -> None:
    expected_names = {
        "IgnGridNormalizationError",
        "IgnVoltageNormalization",
        "NormalizedIgnElectricityData",
        "parse_ign_voltage",
        "normalize_ign_electricity",
    }

    assert expected_names <= set(stages.__all__)
    normalized = stages.normalize_ign_electricity(_source_bundle(), SOURCE_CONFIG)
    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
```

### `test_internal_source_context_accepts_supported_department_codes`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `department_code`.

**Setup**

```python
context = replace(_context(LINE_LAYER), department_code=department_code)
grid_normalization._validate_source_context(context)
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
def test_internal_source_context_accepts_supported_department_codes(
    department_code: str,
) -> None:
    context = replace(_context(LINE_LAYER), department_code=department_code)

    grid_normalization._validate_source_context(context)
```

### `test_internal_source_context_rejects_uppercase_sha256`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
archive_sha256 = "A" * 64
context = replace(_context(LINE_LAYER), archive_sha256=archive_sha256)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="archive_sha256"):
        normalize_ign_electric_lines(_line_source(), context)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_internal_source_context_rejects_uppercase_sha256() -> None:
    archive_sha256 = "A" * 64
    context = replace(_context(LINE_LAYER), archive_sha256=archive_sha256)

    with pytest.raises(IgnGridNormalizationError, match="archive_sha256"):
        normalize_ign_electric_lines(_line_source(), context)
```

### `test_grid_summary_requires_strict_structural_types`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
source = _source_bundle()
changed = replace(source.electric_lines_summary, **{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_grid_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
    source = _source_bundle()
    changed = replace(source.electric_lines_summary, **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(replace(source, electric_lines_summary=changed))
```

### `test_grid_archive_sha256_requires_canonical_lowercase`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
source = _source_bundle_with_archive(sha256=value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_grid_archive_sha256_requires_canonical_lowercase(value: str) -> None:
    source = _source_bundle_with_archive(sha256=value)

    with pytest.raises(IgnGridNormalizationError):
        normalize_ign_electricity(source)
```

### `test_internal_source_context_rejects_invalid_lineage_values`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
context = replace(_context(LINE_LAYER), **{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError):
        grid_normalization._validate_source_context(context)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_internal_source_context_rejects_invalid_lineage_values(
    field: str,
    value: object,
) -> None:
    context = replace(_context(LINE_LAYER), **{field: value})

    with pytest.raises(IgnGridNormalizationError):
        grid_normalization._validate_source_context(context)
```

### `test_exact_voltage_parser_is_generic_and_finite`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_kv`, `raw`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
parsed = parse_ign_voltage(raw)
```

**Expected result**

```python
assert parsed.raw == raw
assert parsed.status == "EXACT"
assert parsed.voltage_kv == expected_kv
assert parsed.voltage_kv is not None and isfinite(parsed.voltage_kv)
assert parsed.voltage_upper_bound_kv is None
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_voltage_parser_is_generic_and_finite(
    raw: str, expected_kv: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "EXACT"
    assert parsed.voltage_kv == expected_kv
    assert parsed.voltage_kv is not None and isfinite(parsed.voltage_kv)
    assert parsed.voltage_upper_bound_kv is None
```

### `test_bounded_voltage_is_generic_finite_and_not_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `expected_upper_bound`, `raw`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
parsed = parse_ign_voltage(raw)
```

**Expected result**

```python
assert parsed.raw == raw
assert parsed.status == "BELOW"
assert parsed.voltage_kv is None
assert parsed.voltage_upper_bound_kv == expected_upper_bound
assert isfinite(parsed.voltage_upper_bound_kv)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_bounded_voltage_is_generic_finite_and_not_exact(
    raw: str, expected_upper_bound: float
) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "BELOW"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv == expected_upper_bound
    assert isfinite(parsed.voltage_upper_bound_kv)
```

### `test_unknown_voltage_parser`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `raw`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
parsed = parse_ign_voltage(raw)
```

**Expected result**

```python
assert parsed.raw == raw
assert parsed.status == "UNKNOWN"
assert parsed.voltage_kv is None
assert parsed.voltage_upper_bound_kv is None
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_voltage_parser(raw: str | None) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "UNKNOWN"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

### `test_deenergized_voltage_parser`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `raw`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
parsed = parse_ign_voltage(raw)
```

**Expected result**

```python
assert parsed.raw == raw
assert parsed.status == "DEENERGIZED"
assert parsed.voltage_kv is None
assert parsed.voltage_upper_bound_kv is None
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_deenergized_voltage_parser(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.raw == raw
    assert parsed.status == "DEENERGIZED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

### `test_unexpected_or_non_scalar_voltage_is_controlled_unparsed`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
parsed = parse_ign_voltage(value)
```

**Expected result**

```python
assert parsed.status == "UNPARSED"
assert parsed.voltage_kv is None
assert parsed.voltage_upper_bound_kv is None
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unexpected_or_non_scalar_voltage_is_controlled_unparsed(
    value: object,
) -> None:
    parsed = parse_ign_voltage(value)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

### `test_invalid_or_overflowing_numeric_voltage_is_unparsed`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `raw`.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
parsed = parse_ign_voltage(raw)
```

**Expected result**

```python
assert parsed.status == "UNPARSED"
assert parsed.voltage_kv is None
assert parsed.voltage_upper_bound_kv is None
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_or_overflowing_numeric_voltage_is_unparsed(raw: str) -> None:
    parsed = parse_ign_voltage(raw)

    assert parsed.status == "UNPARSED"
    assert parsed.voltage_kv is None
    assert parsed.voltage_upper_bound_kv is None
```

### `test_valid_line_has_stable_identity_lineage_and_range_index`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _line_source()
row = normalized.iloc[0]
```

**Action**

```python
normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Expected result**

```python
assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
assert isinstance(normalized.index, pd.RangeIndex)
assert row["grid_feature_id"] == "IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1"
assert row["source_feature_id"] == "LIGNE-1"
assert row["source_provider"] == "IGN"
assert row["source_product"] == "BD_TOPO"
assert row["source_layer"] == LINE_LAYER
assert row["source_department_code"] == "31"
assert row["source_edition"] == "2026-06-15"
assert row["source_product_version"] == "3.5"
assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
assert row["source_archive_sha256"] == ARCHIVE_SHA256
assert row["source_url"] == SOURCE_URL
assert row["manager_name"] == "Réseau de Transport d'Électricité"
assert row["asset_status_raw"] == "En service"
assert row["source_identifiers_raw"] == "source-id"
assert row["planimetric_precision_m"] == 2.5
assert row["spatial_role"] == "PROXY_GEOMETRY"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_line_has_stable_identity_lineage_and_range_index() -> None:
    source = _line_source()

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:ELECTRIC_LINE:LIGNE-1"
    assert row["source_feature_id"] == "LIGNE-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == LINE_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["manager_name"] == "Réseau de Transport d'Électricité"
    assert row["asset_status_raw"] == "En service"
    assert row["source_identifiers_raw"] == "source-id"
    assert row["planimetric_precision_m"] == 2.5
    assert row["spatial_role"] == "PROXY_GEOMETRY"
```

### `test_deenergized_voltage_does_not_override_source_asset_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
normalized = normalize_ign_electric_lines(
        _line_source(voltages=["Hors tension"]), _context(LINE_LAYER)
    )
```

**Expected result**

```python
assert normalized.iloc[0]["voltage_status"] == "DEENERGIZED"
assert normalized.iloc[0]["asset_status_raw"] == "En service"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_deenergized_voltage_does_not_override_source_asset_status() -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(voltages=["Hors tension"]), _context(LINE_LAYER)
    )

    assert normalized.iloc[0]["voltage_status"] == "DEENERGIZED"
    assert normalized.iloc[0]["asset_status_raw"] == "En service"
```

### `test_null_or_empty_line_cleabs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `identifier`.

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
with pytest.raises(IgnGridNormalizationError, match="cleabs|null|empty"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_null_or_empty_line_cleabs_fails(identifier: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|null|empty"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )
```

### `test_unsafe_source_id_is_rejected_without_rewriting`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `identifier`.

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
with pytest.raises(IgnGridNormalizationError, match="cleabs|whitespace|control|:"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unsafe_source_id_is_rejected_without_rewriting(identifier: str) -> None:
    with pytest.raises(IgnGridNormalizationError, match="cleabs|whitespace|control|:"):
        normalize_ign_electric_lines(
            _line_source(identifiers=[identifier]), _context(LINE_LAYER)
        )
```

### `test_duplicate_line_cleabs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
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
with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_line_cleabs_fails() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

### `test_line_missing_or_wrong_crs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `crs`.

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
with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electric_lines(_line_source(crs=crs), _context(LINE_LAYER))
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_line_missing_or_wrong_crs_fails(crs: str | None) -> None:
    with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electric_lines(_line_source(crs=crs), _context(LINE_LAYER))
```

### `test_line_geometry_quality_is_preserved_without_row_loss_or_repair`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
source = _line_source(
        geometries=[LineString([(0, 0), (10, 10)]), None, LineString(), invalid],
        identifiers=["VALID", "NULL", "EMPTY", "INVALID"],
        voltages=["63 kV"] * 4,
    )
```

**Action**

```python
normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Expected result**

```python
assert normalized["geometry_status"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
assert normalized["source_feature_id"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
assert normalized.geometry.iloc[1] is None
assert normalized.geometry.iloc[2].is_empty
assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_line_geometry_quality_is_preserved_without_row_loss_or_repair() -> None:
    invalid = Polygon([(0, 0), (20, 20), (20, 0), (0, 20), (0, 0)])
    source = _line_source(
        geometries=[LineString([(0, 0), (10, 10)]), None, LineString(), invalid],
        identifiers=["VALID", "NULL", "EMPTY", "INVALID"],
        voltages=["63 kV"] * 4,
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert normalized["geometry_status"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert normalized["source_feature_id"].tolist() == [
        "VALID",
        "NULL",
        "EMPTY",
        "INVALID",
    ]
    assert normalized.geometry.iloc[1] is None
    assert normalized.geometry.iloc[2].is_empty
    assert normalized.geometry.iloc[3].equals_exact(invalid, tolerance=0)
```

### `test_z_coordinates_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _line_source(geometries=[LineString([(0, 0, 10), (10, 10, 20)])])
```

**Action**

```python
normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Expected result**

```python
assert source.geometry.iloc[0].has_z
assert normalized.geometry.iloc[0].has_z
assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_z_coordinates_are_preserved() -> None:
    source = _line_source(geometries=[LineString([(0, 0, 10), (10, 10, 20)])])

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert source.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].has_z
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )
```

### `test_unusual_duplicate_source_index_is_not_preserved_as_identity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["FIRST", "SECOND"],
        index=[77, 77],
    )
```

**Action**

```python
normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Expected result**

```python
assert isinstance(normalized.index, pd.RangeIndex)
assert normalized.index.tolist() == [0, 1]
assert normalized["source_feature_id"].tolist() == ["FIRST", "SECOND"]
assert normalized["grid_feature_id"].tolist() == [
        "IGN_BDTOPO:ELECTRIC_LINE:FIRST",
        "IGN_BDTOPO:ELECTRIC_LINE:SECOND",
    ]
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unusual_duplicate_source_index_is_not_preserved_as_identity() -> None:
    source = _line_source(
        geometries=[
            LineString([(0, 0), (10, 10)]),
            LineString([(20, 20), (30, 30)]),
        ],
        identifiers=["FIRST", "SECOND"],
        index=[77, 77],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert isinstance(normalized.index, pd.RangeIndex)
    assert normalized.index.tolist() == [0, 1]
    assert normalized["source_feature_id"].tolist() == ["FIRST", "SECOND"]
    assert normalized["grid_feature_id"].tolist() == [
        "IGN_BDTOPO:ELECTRIC_LINE:FIRST",
        "IGN_BDTOPO:ELECTRIC_LINE:SECOND",
    ]
```

### `test_line_normalization_does_not_mutate_input_and_has_stable_columns`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _line_source()
reordered = source.loc[:, list(reversed(source.columns))].set_geometry("geometry")
before = deepcopy(reordered)
assert_geodataframe_equal(reordered, before)
```

**Action**

```python
normalized = normalize_ign_electric_lines(reordered, _context(LINE_LAYER))
```

**Expected result**

```python
assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_line_normalization_does_not_mutate_input_and_has_stable_columns() -> None:
    source = _line_source()
    reordered = source.loc[:, list(reversed(source.columns))].set_geometry("geometry")
    before = deepcopy(reordered)

    normalized = normalize_ign_electric_lines(reordered, _context(LINE_LAYER))

    assert_geodataframe_equal(reordered, before)
    assert list(normalized.columns) == list(LINE_OUTPUT_COLUMNS)
```

### `test_missing_required_line_field_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
source = _line_source().drop(columns=column)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match=column):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_required_line_field_fails(column: str) -> None:
    source = _line_source().drop(columns=column)

    with pytest.raises(IgnGridNormalizationError, match=column):
        normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

### `test_valid_or_null_line_precision_is_normalized_to_float`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `precision`.

**Setup**

```python
if precision is None or (isinstance(precision, float) and np.isnan(precision)):
        assert pd.isna(normalized.iloc[0]["planimetric_precision_m"])
    else:
        assert normalized.iloc[0]["planimetric_precision_m"] == float(precision)
```

**Action**

```python
normalized = normalize_ign_electric_lines(
        _line_source(precisions=[precision]), _context(LINE_LAYER)
    )
```

**Expected result**

```python
assert str(normalized["planimetric_precision_m"].dtype) == "float64"
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_or_null_line_precision_is_normalized_to_float(
    precision: object,
) -> None:
    normalized = normalize_ign_electric_lines(
        _line_source(precisions=[precision]), _context(LINE_LAYER)
    )

    assert str(normalized["planimetric_precision_m"].dtype) == "float64"
    if precision is None or (isinstance(precision, float) and np.isnan(precision)):
        assert pd.isna(normalized.iloc[0]["planimetric_precision_m"])
    else:
        assert normalized.iloc[0]["planimetric_precision_m"] == float(precision)
```

### `test_invalid_line_precision_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `precision`.

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
with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_electric_lines(
            _line_source(precisions=[precision]), _context(LINE_LAYER)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_line_precision_fails(precision: object) -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_electric_lines(
            _line_source(precisions=[precision]), _context(LINE_LAYER)
        )
```

### `test_normalized_voltage_never_emits_non_finite_numeric_values`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
huge = f"{'9' * 400} kV"
source = _line_source(
        geometries=[LineString([(0, 0), (1, 1)])] * 4,
        identifiers=["EXACT", "BELOW", "OVERFLOW", "MISSING"],
        voltages=["225 kV", "<90 kV", huge, None],
    )
```

**Action**

```python
normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))
```

**Expected result**

```python
assert normalized["voltage_status"].tolist() == [
        "EXACT",
        "BELOW",
        "UNPARSED",
        "UNKNOWN",
    ]
assert np.isfinite(normalized["voltage_kv"].dropna()).all()
assert np.isfinite(normalized["voltage_upper_bound_kv"].dropna()).all()
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_normalized_voltage_never_emits_non_finite_numeric_values() -> None:
    huge = f"{'9' * 400} kV"
    source = _line_source(
        geometries=[LineString([(0, 0), (1, 1)])] * 4,
        identifiers=["EXACT", "BELOW", "OVERFLOW", "MISSING"],
        voltages=["225 kV", "<90 kV", huge, None],
    )

    normalized = normalize_ign_electric_lines(source, _context(LINE_LAYER))

    assert normalized["voltage_status"].tolist() == [
        "EXACT",
        "BELOW",
        "UNPARSED",
        "UNKNOWN",
    ]
    assert np.isfinite(normalized["voltage_kv"].dropna()).all()
    assert np.isfinite(normalized["voltage_upper_bound_kv"].dropna()).all()
```

### `test_valid_post_has_stable_lineage_and_no_voltage_inference`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _post_source()
row = normalized.iloc[0]
```

**Action**

```python
normalized = normalize_ign_transformation_posts(
        source, _context(POST_LAYER)
    )
```

**Expected result**

```python
assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)
assert isinstance(normalized.index, pd.RangeIndex)
assert row["grid_feature_id"] == "IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1"
assert row["source_layer"] == POST_LAYER
assert row["source_department_code"] == "31"
assert row["source_archive_sha256"] == ARCHIVE_SHA256
assert row["name"] == "Poste de test"
assert row["voltage_status"] == "UNKNOWN"
assert pd.isna(row["voltage_kv"])
assert row["spatial_role"] == "PROXY_GEOMETRY"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_post_has_stable_lineage_and_no_voltage_inference() -> None:
    source = _post_source()

    normalized = normalize_ign_transformation_posts(
        source, _context(POST_LAYER)
    )

    row = normalized.iloc[0]
    assert list(normalized.columns) == list(TRANSFORMATION_POST_OUTPUT_COLUMNS)
    assert isinstance(normalized.index, pd.RangeIndex)
    assert row["grid_feature_id"] == "IGN_BDTOPO:TRANSFORMATION_POST:POSTE-1"
    assert row["source_layer"] == POST_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["name"] == "Poste de test"
    assert row["voltage_status"] == "UNKNOWN"
    assert pd.isna(row["voltage_kv"])
    assert row["spatial_role"] == "PROXY_GEOMETRY"
```

### `test_post_geometry_crs_and_input_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _post_source()
before = deepcopy(source)
assert_geodataframe_equal(source, before)
```

**Action**

```python
normalized = normalize_ign_transformation_posts(
        source, _context(POST_LAYER)
    )
```

**Expected result**

```python
assert normalized.crs is not None and normalized.crs.to_epsg() == 2154
assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_post_geometry_crs_and_input_are_preserved() -> None:
    source = _post_source()
    before = deepcopy(source)

    normalized = normalize_ign_transformation_posts(
        source, _context(POST_LAYER)
    )

    assert_geodataframe_equal(source, before)
    assert normalized.crs is not None and normalized.crs.to_epsg() == 2154
    assert normalized.geometry.iloc[0].equals_exact(
        source.geometry.iloc[0], tolerance=0
    )
```

### `test_duplicate_post_cleabs_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
polygon = Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])
source = _post_source(
        geometries=[polygon, polygon], identifiers=["DUPLICATE", "DUPLICATE"]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_transformation_posts(source, _context(POST_LAYER))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_post_cleabs_fails() -> None:
    polygon = Polygon([(0, 0), (0, 20), (20, 20), (20, 0), (0, 0)])
    source = _post_source(
        geometries=[polygon, polygon], identifiers=["DUPLICATE", "DUPLICATE"]
    )

    with pytest.raises(IgnGridNormalizationError, match="unique"):
        normalize_ign_transformation_posts(source, _context(POST_LAYER))
```

### `test_null_post_geometry_and_precision_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
normalized = normalize_ign_transformation_posts(
        _post_source(geometries=[None], precisions=[None]), _context(POST_LAYER)
    )
```

**Expected result**

```python
assert normalized.iloc[0]["geometry_status"] == "NULL"
assert normalized.geometry.iloc[0] is None
assert normalized.iloc[0]["voltage_status"] == "UNKNOWN"
assert normalized["voltage_kv"].isna().all()
assert normalized["planimetric_precision_m"].isna().all()
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_post_geometry_and_precision_are_preserved() -> None:
    normalized = normalize_ign_transformation_posts(
        _post_source(geometries=[None], precisions=[None]), _context(POST_LAYER)
    )

    assert normalized.iloc[0]["geometry_status"] == "NULL"
    assert normalized.geometry.iloc[0] is None
    assert normalized.iloc[0]["voltage_status"] == "UNKNOWN"
    assert normalized["voltage_kv"].isna().all()
    assert normalized["planimetric_precision_m"].isna().all()
```

### `test_invalid_post_precision_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

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
with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_transformation_posts(
            _post_source(precisions=["5.0"]), _context(POST_LAYER)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_post_precision_fails() -> None:
    with pytest.raises(IgnGridNormalizationError, match="precision_planimetrique"):
        normalize_ign_transformation_posts(
            _post_source(precisions=["5.0"]), _context(POST_LAYER)
        )
```

### `test_appropriate_multigeometry_types_are_accepted`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
multilines = MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])
multipolygon = MultiPolygon(
        [
            Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
            Polygon([(10, 10), (10, 15), (15, 15), (15, 10), (10, 10)]),
        ]
    )
```

**Action**

```python
lines = normalize_ign_electric_lines(
        _line_source(geometries=[multilines]), _context(LINE_LAYER)
    )
posts = normalize_ign_transformation_posts(
        _post_source(geometries=[multipolygon]), _context(POST_LAYER)
    )
```

**Expected result**

```python
assert lines.iloc[0]["geometry_status"] == "VALID"
assert lines.geometry.iloc[0].geom_type == "MultiLineString"
assert posts.iloc[0]["geometry_status"] == "VALID"
assert posts.geometry.iloc[0].geom_type == "MultiPolygon"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_appropriate_multigeometry_types_are_accepted() -> None:
    multilines = MultiLineString([[(0, 0), (10, 10)], [(20, 20), (30, 30)]])
    multipolygon = MultiPolygon(
        [
            Polygon([(0, 0), (0, 5), (5, 5), (5, 0), (0, 0)]),
            Polygon([(10, 10), (10, 15), (15, 15), (15, 10), (10, 10)]),
        ]
    )

    lines = normalize_ign_electric_lines(
        _line_source(geometries=[multilines]), _context(LINE_LAYER)
    )
    posts = normalize_ign_transformation_posts(
        _post_source(geometries=[multipolygon]), _context(POST_LAYER)
    )

    assert lines.iloc[0]["geometry_status"] == "VALID"
    assert lines.geometry.iloc[0].geom_type == "MultiLineString"
    assert posts.iloc[0]["geometry_status"] == "VALID"
    assert posts.geometry.iloc[0].geom_type == "MultiPolygon"
```

### `test_valid_polygon_or_point_is_rejected_as_electric_line`

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
with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_electric_lines(
            _line_source(geometries=[geometry]), _context(LINE_LAYER)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_polygon_or_point_is_rejected_as_electric_line(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_electric_lines(
            _line_source(geometries=[geometry]), _context(LINE_LAYER)
        )
```

### `test_valid_line_or_point_is_rejected_as_transformation_post`

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
with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_transformation_posts(
            _post_source(geometries=[geometry]), _context(POST_LAYER)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_line_or_point_is_rejected_as_transformation_post(
    geometry: object,
) -> None:
    with pytest.raises(IgnGridNormalizationError, match="geometry types"):
        normalize_ign_transformation_posts(
            _post_source(geometries=[geometry]), _context(POST_LAYER)
        )
```

### `test_high_level_path_uses_discovered_layer_names_and_archive_lineage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
normalized = normalize_ign_electricity(source)
for frame in (normalized.electric_lines, normalized.transformation_posts):
        assert frame["source_department_code"].unique().tolist() == ["31"]
        assert frame["source_edition"].unique().tolist() == ["2026-06-15"]
        assert frame["source_product_version"].unique().tolist() == ["3.5"]
        assert frame["source_archive_sha256"].unique().tolist() == [ARCHIVE_SHA256]
        assert frame["source_url"].unique().tolist() == [SOURCE_URL]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_path_uses_discovered_layer_names_and_archive_lineage() -> None:
    source = _source_bundle()

    normalized = normalize_ign_electricity(source)

    assert normalized.electric_lines["source_layer"].unique().tolist() == [LINE_LAYER]
    assert normalized.transformation_posts["source_layer"].unique().tolist() == [
        POST_LAYER
    ]
    for frame in (normalized.electric_lines, normalized.transformation_posts):
        assert frame["source_department_code"].unique().tolist() == ["31"]
        assert frame["source_edition"].unique().tolist() == ["2026-06-15"]
        assert frame["source_product_version"].unique().tolist() == ["3.5"]
        assert frame["source_archive_sha256"].unique().tolist() == [ARCHIVE_SHA256]
        assert frame["source_url"].unique().tolist() == [SOURCE_URL]
```

### `test_high_level_rejects_coordinated_frame_and_summary_forgery`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
forged = source.electric_lines.copy()
forged.loc[0, "voltage"] = "400 kV"
forged_summary = _summary(forged, "electric_lines", LINE_LAYER)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="physical|fresh|source"):
        normalize_ign_electricity(
            replace(
                source,
                electric_lines=forged,
                electric_lines_summary=forged_summary,
            )
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_coordinated_frame_and_summary_forgery() -> None:
    source = _source_bundle()
    forged = source.electric_lines.copy()
    forged.loc[0, "voltage"] = "400 kV"
    forged_summary = _summary(forged, "electric_lines", LINE_LAYER)

    with pytest.raises(IgnGridNormalizationError, match="physical|fresh|source"):
        normalize_ign_electricity(
            replace(
                source,
                electric_lines=forged,
                electric_lines_summary=forged_summary,
            )
        )
```

### `test_source_complete_grid_validation_does_not_mutate_supplied_frames`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
lines_before = deepcopy(source.electric_lines)
posts_before = deepcopy(source.transformation_posts)
normalize_ign_electricity(source)
assert_geodataframe_equal(source.electric_lines, lines_before)
assert_geodataframe_equal(source.transformation_posts, posts_before)
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

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_source_complete_grid_validation_does_not_mutate_supplied_frames() -> None:
    source = _source_bundle()
    lines_before = deepcopy(source.electric_lines)
    posts_before = deepcopy(source.transformation_posts)

    normalize_ign_electricity(source)

    assert_geodataframe_equal(source.electric_lines, lines_before)
    assert_geodataframe_equal(source.transformation_posts, posts_before)
```

### `test_high_level_rejects_incompatible_archive_identity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `message`, `value`.

**Setup**

```python
source = _source_bundle_with_archive(**{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match=message):
        normalize_ign_electricity(source)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_incompatible_archive_identity(
    field: str,
    value: str,
    message: str,
) -> None:
    source = _source_bundle_with_archive(**{field: value})

    with pytest.raises(IgnGridNormalizationError, match=message):
        normalize_ign_electricity(source)
```

### `test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
provider = (
        "INSTITUT NATIONAL DE L'INFORMATION GEOGRAPHIQUE ET FORESTIERE (ign)"
    )
product = "bd-topo"
source = _source_bundle_with_archive(
        provider=provider,
        product=product,
    )
config_payload = SOURCE_CONFIG.model_dump(mode="json")
config_payload.update({"provider": provider, "product": product})
matching_config = IgnBdTopoSourceConfig.model_validate(config_payload)
```

**Action**

```python
normalized = _normalize_ign_electricity(source, matching_config)
```

**Expected result**

```python
assert len(normalized.electric_lines) == 1
assert len(normalized.transformation_posts) == 1
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_archive_identity_comparison_is_case_accent_and_punctuation_tolerant() -> None:
    provider = (
        "INSTITUT NATIONAL DE L'INFORMATION GEOGRAPHIQUE ET FORESTIERE (ign)"
    )
    product = "bd-topo"
    source = _source_bundle_with_archive(
        provider=provider,
        product=product,
    )
    config_payload = SOURCE_CONFIG.model_dump(mode="json")
    config_payload.update({"provider": provider, "product": product})
    matching_config = IgnBdTopoSourceConfig.model_validate(config_payload)

    normalized = _normalize_ign_electricity(source, matching_config)

    assert len(normalized.electric_lines) == 1
    assert len(normalized.transformation_posts) == 1
```

### `test_high_level_rejects_summary_row_count_mismatch`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
summary = replace(
        source.electric_lines_summary,
        feature_count=source.electric_lines_summary.feature_count + 1,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="row count"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_summary_row_count_mismatch() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        feature_count=source.electric_lines_summary.feature_count + 1,
    )

    with pytest.raises(IgnGridNormalizationError, match="row count"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

### `test_high_level_rejects_summary_layer_name_mismatch`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
summary = replace(source.electric_lines_summary, source_layer_name="WRONG")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="summary layer"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_summary_layer_name_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, source_layer_name="WRONG")

    with pytest.raises(IgnGridNormalizationError, match="summary layer"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

### `test_high_level_rejects_wrong_logical_name`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
summary = replace(
        source.electric_lines_summary,
        logical_name=cast(Any, "transformation_posts"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="logical name"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_wrong_logical_name() -> None:
    source = _source_bundle()
    summary = replace(
        source.electric_lines_summary,
        logical_name=cast(Any, "transformation_posts"),
    )

    with pytest.raises(IgnGridNormalizationError, match="logical name"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

### `test_high_level_rejects_summary_crs_mismatch`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
summary = replace(source.electric_lines_summary, crs="EPSG:4326")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_summary_crs_mismatch() -> None:
    source = _source_bundle()
    summary = replace(source.electric_lines_summary, crs="EPSG:4326")

    with pytest.raises(IgnGridNormalizationError, match="CRS|2154"):
        normalize_ign_electricity(replace(source, electric_lines_summary=summary))
```

### `test_high_level_rejects_forged_ordered_summary_schema`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
source = _source_bundle()
summary = source.electric_lines_summary
if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "object")
        changed = replace(summary, dtypes=tuple(dtypes))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="schema|columns|dtype"):
        normalize_ign_electricity(
            replace(source, electric_lines_summary=changed)
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_forged_ordered_summary_schema(mutation: str) -> None:
    source = _source_bundle()
    summary = source.electric_lines_summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "object")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(IgnGridNormalizationError, match="schema|columns|dtype"):
        normalize_ign_electricity(
            replace(source, electric_lines_summary=changed)
        )
```

### `test_high_level_rejects_duplicate_or_missing_layer_inventory`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
duplicate = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(LINE_LAYER, POST_LAYER, LINE_LAYER),
        ),
    )
missing = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(POST_LAYER,),
        ),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="inventory|duplicate"):
        normalize_ign_electricity(duplicate)
with pytest.raises(IgnGridNormalizationError, match="inventory|selected"):
        normalize_ign_electricity(missing)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_duplicate_or_missing_layer_inventory() -> None:
    source = _source_bundle()
    duplicate = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(LINE_LAYER, POST_LAYER, LINE_LAYER),
        ),
    )
    with pytest.raises(IgnGridNormalizationError, match="inventory|duplicate"):
        normalize_ign_electricity(duplicate)

    missing = replace(
        source,
        extraction=replace(
            source.extraction,
            all_layer_names=(POST_LAYER,),
        ),
    )
    with pytest.raises(IgnGridNormalizationError, match="inventory|selected"):
        normalize_ign_electricity(missing)
```

### `test_high_level_rejects_colliding_electricity_roles`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
extraction = replace(
        source.extraction,
        transformation_posts_layer=LINE_LAYER,
    )
post_summary = replace(
        source.transformation_posts_summary,
        source_layer_name=LINE_LAYER,
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="same layer|distinct|role"):
        normalize_ign_electricity(
            replace(
                source,
                extraction=extraction,
                transformation_posts_summary=post_summary,
            )
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_colliding_electricity_roles() -> None:
    source = _source_bundle()
    extraction = replace(
        source.extraction,
        transformation_posts_layer=LINE_LAYER,
    )
    post_summary = replace(
        source.transformation_posts_summary,
        source_layer_name=LINE_LAYER,
    )

    with pytest.raises(IgnGridNormalizationError, match="same layer|distinct|role"):
        normalize_ign_electricity(
            replace(
                source,
                extraction=extraction,
                transformation_posts_summary=post_summary,
            )
        )
```

### `test_high_level_rejects_stale_geometry_counts_after_frame_mutation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
mutated = source.electric_lines.copy()
mutated.at[mutated.index[0], "geometry"] = None
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="geometry summary"):
        normalize_ign_electricity(replace(source, electric_lines=mutated))
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_high_level_rejects_stale_geometry_counts_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = None

    with pytest.raises(IgnGridNormalizationError, match="geometry summary"):
        normalize_ign_electricity(replace(source, electric_lines=mutated))
```

### `test_high_level_rejects_stale_geometry_types_after_frame_mutation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source_bundle()
mutated = source.electric_lines.copy()
mutated.at[mutated.index[0], "geometry"] = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="geometry summary"):
        normalize_ign_electricity(replace(source, electric_lines=mutated))
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_high_level_rejects_stale_geometry_types_after_frame_mutation() -> None:
    source = _source_bundle()
    mutated = source.electric_lines.copy()
    mutated.at[mutated.index[0], "geometry"] = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )

    with pytest.raises(IgnGridNormalizationError, match="geometry summary"):
        normalize_ign_electricity(replace(source, electric_lines=mutated))
```

### `test_high_level_rejects_any_spatial_role_mismatch`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `component`.

**Setup**

```python
source = _source_bundle()
wrong_role = cast(Any, "EXACT_RTE_GEOMETRY")
if component == "source":
        inconsistent = replace(source, spatial_role=wrong_role)
    elif component == "extraction":
        inconsistent = replace(
            source, extraction=replace(source.extraction, spatial_role=wrong_role)
        )
    elif component == "archive":
        extraction = replace(
            source.extraction,
            archive=replace(source.extraction.archive, spatial_role=wrong_role),
        )
        inconsistent = replace(source, extraction=extraction)
    elif component == "line_summary":
        inconsistent = replace(
            source,
            electric_lines_summary=replace(
                source.electric_lines_summary, spatial_role=wrong_role
            ),
        )
    else:
        inconsistent = replace(
            source,
            transformation_posts_summary=replace(
                source.transformation_posts_summary, spatial_role=wrong_role
            ),
        )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnGridNormalizationError, match="PROXY_GEOMETRY"):
        normalize_ign_electricity(inconsistent)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_high_level_rejects_any_spatial_role_mismatch(component: str) -> None:
    source = _source_bundle()
    wrong_role = cast(Any, "EXACT_RTE_GEOMETRY")
    if component == "source":
        inconsistent = replace(source, spatial_role=wrong_role)
    elif component == "extraction":
        inconsistent = replace(
            source, extraction=replace(source.extraction, spatial_role=wrong_role)
        )
    elif component == "archive":
        extraction = replace(
            source.extraction,
            archive=replace(source.extraction.archive, spatial_role=wrong_role),
        )
        inconsistent = replace(source, extraction=extraction)
    elif component == "line_summary":
        inconsistent = replace(
            source,
            electric_lines_summary=replace(
                source.electric_lines_summary, spatial_role=wrong_role
            ),
        )
    else:
        inconsistent = replace(
            source,
            transformation_posts_summary=replace(
                source.transformation_posts_summary, spatial_role=wrong_role
            ),
        )

    with pytest.raises(IgnGridNormalizationError, match="PROXY_GEOMETRY"):
        normalize_ign_electricity(inconsistent)
```


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

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
