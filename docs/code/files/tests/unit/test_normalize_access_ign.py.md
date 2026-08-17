# `tests/unit/test_normalize_access_ign.py`

## File identity

- Repository path: `tests/unit/test_normalize_access_ign.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.
- Source SHA256: `ed8a0fa4513e82eef5c9192b53c9f47fc32c3fc64ba3d5b7d85f1b94ab7da15c`

## 1. Purpose

Provides complete unit and regression coverage for the `normalize_access_ign` contracts exercised in this file.

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
- `from pathlib import Path`
- `from typing import Any, cast`
- `from uuid import uuid4`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pyogrio`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import LineString, MultiLineString, Point, Polygon`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoDownload,
    IgnBdTopoExtraction,
    IgnBdTopoLayerSummary,
    IgnBdTopoRoadData,
    IgnBdTopoSourceConfig,
    load_ign_bdtopo_roads,
    load_ign_bdtopo_source_config,
)`
- `from landscout.stages.normalize_access_ign import (
    IgnRoadNormalizationError,
    NormalizedIgnRoadData,
    normalize_ign_roads,
)`

## 4. Contract taxonomy

### A. Python constants

#### `ROAD_LAYER`

```python
ROAD_LAYER = "troncon_de_route"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_ign_bdtopo_fr.py::test_road_loader_preserves_lambert93_lines_unchanged` (value argument/reference), `tests/unit/test_normalize_access_ign.py::_source` (value argument/reference), `tests/unit/test_normalize_access_ign.py::_source` (value argument/reference), `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer` (value argument/reference).

#### `ALTERNATE_ROAD_LAYER`

```python
ALTERNATE_ROAD_LAYER = "voie_secondaire"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_normalize_access_ign.py::_with_alternate_road_layer` (value argument/reference).

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
_FIXTURE_ROOT = Path(tempfile.mkdtemp(prefix="landscout-road-ign-"))
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `SOURCE_CONFIG`

```python
SOURCE_CONFIG = load_ign_bdtopo_source_config()
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_type_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_coverage_assessment_reproduces_configured_logical_layer` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_owns_proximity_and_configured_coverage_once` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_public_coverage_proximity_failure_stops_coverage_loading` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_caller_provided_proximity_and_coverage_are_not_public_inputs` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_polygonal_coverage_geometry_is_accepted` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_invalid_coverage_geometry_is_rejected` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_strict_geometric_boundary_proof` (value argument/reference), `tests/unit/test_assess_grid_coverage.py::test_outside_crossing_or_touching_parcel_is_conservative` (value argument/reference).

#### `OUTPUT_COLUMNS`

```python
OUTPUT_COLUMNS = (
    "road_feature_id",
    "road_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
    "nature_raw",
    "importance_raw",
    "fictitious_raw",
    "position_relative_to_ground_raw",
    "asset_status_raw",
    "lane_count_raw",
    "carriageway_width_raw",
    "private_raw",
    "traffic_direction_raw",
    "urban_raw",
    "mean_light_vehicle_speed_raw",
    "light_vehicle_access_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "restriction_height_raw",
    "restriction_total_weight_raw",
    "restriction_axle_weight_raw",
    "restriction_width_raw",
    "restriction_length_raw",
    "dangerous_goods_forbidden_raw",
    "administrative_classification_raw",
    "manager_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_raw",
    "spatial_role",
    "geometry_status",
    "geometry",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_normalize_access_ign.py::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` (value argument/reference).

#### `RAW_FIELD_MAPPING`

```python
RAW_FIELD_MAPPING = (
    ("nature", "nature_raw"),
    ("importance", "importance_raw"),
    ("fictif", "fictitious_raw"),
    ("position_par_rapport_au_sol", "position_relative_to_ground_raw"),
    ("etat_de_l_objet", "asset_status_raw"),
    ("nombre_de_voies", "lane_count_raw"),
    ("largeur_de_chaussee", "carriageway_width_raw"),
    ("prive", "private_raw"),
    ("sens_de_circulation", "traffic_direction_raw"),
    ("urbain", "urban_raw"),
    ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"),
    ("acces_vehicule_leger", "light_vehicle_access_raw"),
    ("periode_de_fermeture", "closure_period_raw"),
    ("nature_de_la_restriction", "restriction_nature_raw"),
    ("restriction_de_hauteur", "restriction_height_raw"),
    ("restriction_de_poids_total", "restriction_total_weight_raw"),
    ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"),
    ("restriction_de_largeur", "restriction_width_raw"),
    ("restriction_de_longueur", "restriction_length_raw"),
    ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"),
    ("cpx_classement_administratif", "administrative_classification_raw"),
    ("cpx_gestionnaire", "manager_raw"),
    ("sources", "source_name_raw"),
    ("identifiants_sources", "source_identifiers_raw"),
    ("date_creation", "source_created_at"),
    ("date_modification", "source_modified_at"),
    ("date_de_confirmation", "source_confirmed_at"),
    ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"),
    ("precision_planimetrique", "planimetric_precision_raw"),
)
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_road_frame`

**Exact signature**

```python
def _road_frame(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for road frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame(values, geometry=source_geometries, crs=crs, index=source_index)
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

- direct call or construction: `tests/unit/test_normalize_access_ign.py::_source` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::_with_alternate_road_layer` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_multilinestring_is_preserved` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_z_coordinates_are_preserved_exactly` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_row_count_order_geometry_and_range_index_are_preserved` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected` via `_road_frame`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `_road_frame`.

**Complete source-ordered implementation**

```python
def _road_frame(
    geometries: list[object] | None = None,
    *,
    identifiers: list[object] | None = None,
    crs: str | None = "EPSG:2154",
    index: list[object] | None = None,
) -> gpd.GeoDataFrame:
    source_geometries = geometries or [LineString([(0, 0), (100, 100)])]
    count = len(source_geometries)
    source_ids = identifiers or [f"ROAD-{number + 1}" for number in range(count)]
    source_index = index or [100 + number for number in range(count)]
    values: dict[str, list[object]] = {
        "cleabs": source_ids,
        "nature": ["Route à 1 chaussée"] * count,
        "importance": ["2"] * count,
        "fictif": ["Non"] * count,
        "position_par_rapport_au_sol": [-1] * count,
        "etat_de_l_objet": ["En service"] * count,
        "nombre_de_voies": [2] * count,
        "largeur_de_chaussee": [7.5] * count,
        "prive": ["Non"] * count,
        "sens_de_circulation": ["Double sens"] * count,
        "urbain": ["Non"] * count,
        "vitesse_moyenne_vl": [80] * count,
        "acces_vehicule_leger": ["Libre"] * count,
        "periode_de_fermeture": [None] * count,
        "nature_de_la_restriction": ["Poids total"] * count,
        "restriction_de_hauteur": [4.2] * count,
        "restriction_de_poids_total": [19.0] * count,
        "restriction_de_poids_par_essieu": [11.5] * count,
        "restriction_de_largeur": [3.2] * count,
        "restriction_de_longueur": [18.0] * count,
        "matieres_dangereuses_interdites": ["Oui"] * count,
        "cpx_classement_administratif": ["Départementale"] * count,
        "cpx_gestionnaire": ["CD31"] * count,
        "sources": ["IGN 2026"] * count,
        "identifiants_sources": ["source-road-id"] * count,
        "date_creation": [pd.Timestamp("2024-01-01", tz="UTC")] * count,
        "date_modification": [pd.Timestamp("2025-01-01", tz="UTC")] * count,
        "date_de_confirmation": [pd.Timestamp("2025-06-01", tz="UTC")] * count,
        "methode_d_acquisition_planimetrique": ["Photogrammétrie"] * count,
        "precision_planimetrique": [2.5] * count,
    }
    return gpd.GeoDataFrame(
        values,
        geometry=source_geometries,
        crs=crs,
        index=source_index,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_summary`

**Exact signature**

```python
def _summary(
    frame: gpd.GeoDataFrame,
    *,
    layer: str = ROAD_LAYER,
) -> IgnBdTopoLayerSummary:
```

**Purpose**

Private `test` helper for summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoLayerSummary`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoLayerSummary(logical_name='road_segments', source_layer_name=layer, crs=str(frame.crs), feature_count=len(frame), columns=tuple((str(column) for column in frame.columns)), dtypes=tuple(((str(column), str(dtype)) for column, dtype in frame.dtypes.items())), null_geometry_count=int(null_mask.sum()), empty_geometry_count=int(empty_mask.sum()), invalid_geometry_count=int(invalid_mask.sum()), geometry_types=tuple(sorted((str(value) for value in geometry[~null_mask].geom_type.dropna().unique()))))
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
    *,
    layer: str = ROAD_LAYER,
) -> IgnBdTopoLayerSummary:
    geometry = frame.geometry
    null_mask = geometry.isna()
    empty_mask = ~null_mask & geometry.is_empty
    invalid_mask = ~null_mask & ~geometry.is_empty & ~geometry.is_valid
    return IgnBdTopoLayerSummary(
        logical_name="road_segments",
        source_layer_name=layer,
        crs=str(frame.crs),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple((str(column), str(dtype)) for column, dtype in frame.dtypes.items()),
        null_geometry_count=int(null_mask.sum()),
        empty_geometry_count=int(empty_mask.sum()),
        invalid_geometry_count=int(invalid_mask.sum()),
        geometry_types=tuple(
            sorted(
                str(value)
                for value in geometry[~null_mask].geom_type.dropna().unique()
            )
        ),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_source`

**Exact signature**

```python
def _source(frame: gpd.GeoDataFrame | None = None) -> IgnBdTopoRoadData:
```

**Purpose**

Private `test` helper for source; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `IgnBdTopoRoadData`.
- Every observed return expression is reproduced without truncation:
```python
IgnBdTopoRoadData(extraction=extraction, road_segments=road_frame, road_segments_summary=_summary(road_frame))
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

- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::_apply` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_wrong_source_config_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_malformed_policy_path_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_complete_normalization_is_invoked_exactly_once` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalization_failure_stops_policy_loading` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_object_is_not_mutated` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_valid_geometry_status_with_unsupported_geometry_is_not_repaired` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` via `_source`.
- direct call or construction: `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_source_config_is_exact_pydantic_type` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::_enrich` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_parcel_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_source_config_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_policy_path_type_has_controlled_error` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_stage_is_invoked_exactly_once` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_failure_stops_proximity` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_malformed_policy_stops_before_application` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_wrong_application_result_type_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_enrich_road_proximity.py::test_application_roads_must_be_geodataframe` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_linestring_normalization_has_exact_schema_identity_and_lineage` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_multilinestring_is_preserved` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_z_coordinates_are_preserved_exactly` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_row_count_order_geometry_and_range_index_are_preserved` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_raw_access_and_restriction_values_are_copied_without_interpretation` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_every_raw_field_preserves_source_values_nulls_and_dtype` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_missing_required_source_field_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_or_empty_cleabs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_unsafe_cleabs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_duplicate_cleabs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_or_missing_road_crs_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_archive_identity_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_wrong_source_spatial_role_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_row_count_mismatch_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_summary_requires_strict_structural_types` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_archive_sha256_requires_canonical_lowercase` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_crs_mismatch_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_forged_ordered_summary_schema_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_physical_role_collision` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_source_rejects_duplicate_layer_inventory` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_geometry_facts_mismatch_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_layer_must_exist_in_extraction_inventory` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_summary_layer_and_logical_name_must_be_exact` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_valid_unsupported_geometry_type_is_rejected` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_null_empty_and_invalid_geometry_are_preserved_with_status` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_normalization_does_not_mutate_input` via `_source`.
- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_high_level_rejects_coordinated_road_frame_and_summary_forgery` via `_source`.

**Complete source-ordered implementation**

```python
def _source(frame: gpd.GeoDataFrame | None = None) -> IgnBdTopoRoadData:
    road_frame = frame if frame is not None else _road_frame()
    extraction_path = _FIXTURE_ROOT / uuid4().hex
    extraction_path.mkdir(parents=True)
    geopackage_path = extraction_path / "data.gpkg"
    crs = road_frame.crs or "EPSG:2154"
    dummy = gpd.GeoDataFrame(
        {"id": ["dummy"]},
        geometry=[LineString([(0, 0), (1, 1)])],
        crs=crs,
    )
    pyogrio.write_dataframe(
        dummy, geopackage_path, layer="ligne_electrique", driver="GPKG"
    )
    pyogrio.write_dataframe(
        dummy,
        geopackage_path,
        layer="poste_de_transformation",
        driver="GPKG",
        append=True,
    )
    pyogrio.write_dataframe(
        road_frame,
        geopackage_path,
        layer=ROAD_LAYER,
        driver="GPKG",
        append=True,
    )
    road_frame = gpd.read_file(geopackage_path, layer=ROAD_LAYER, engine="pyogrio")
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    (extraction_path / ".landscout-extraction.json").write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": ARCHIVE_SHA256,
                "geopackage_relative_path": "data.gpkg",
                "geopackage_size_bytes": len(payload),
                "geopackage_sha256": digest,
                "all_layer_names": list(layer_names),
                "electric_lines_layer": "ligne_electrique",
                "transformation_posts_layer": "poste_de_transformation",
                "spatial_role": "PROXY_GEOMETRY",
            }
        ),
        encoding="utf-8",
    )
    archive = IgnBdTopoDownload(
        provider="IGN",
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
        electric_lines_layer="ligne_electrique",
        transformation_posts_layer="poste_de_transformation",
        cache_hit=True,
    )
    return IgnBdTopoRoadData(
        extraction=extraction,
        road_segments=road_frame,
        road_segments_summary=_summary(road_frame),
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_with_alternate_road_layer`

**Exact signature**

```python
def _with_alternate_road_layer(
    source: IgnBdTopoRoadData,
) -> tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]:
```

**Purpose**

Private `test` helper for with alternate road layer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]`.
- Every observed return expression is reproduced without truncation:
```python
(configured, forged)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `geopackage_path.read_bytes`, `marker_path.read_text`.
- Filesystem write: `marker_path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: `alternate_config_payload['access']['road_segments']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_normalize_access_ign.py::test_road_normalization_reproduces_configured_logical_layer` via `_with_alternate_road_layer`.

**Complete source-ordered implementation**

```python
def _with_alternate_road_layer(
    source: IgnBdTopoRoadData,
) -> tuple[IgnBdTopoRoadData, IgnBdTopoRoadData]:
    alternate = _road_frame(
        [LineString([(500, 500), (600, 600)])],
        identifiers=["ALTERNATE-ROAD"],
    )
    geopackage_path = source.extraction.geopackage_path
    pyogrio.write_dataframe(
        alternate,
        geopackage_path,
        layer=ALTERNATE_ROAD_LAYER,
        driver="GPKG",
        append=True,
    )
    payload = geopackage_path.read_bytes()
    layer_names = tuple(str(row[0]) for row in pyogrio.list_layers(geopackage_path))
    digest = sha256(payload).hexdigest()
    marker_path = source.extraction.extraction_path / ".landscout-extraction.json"
    marker = json.loads(marker_path.read_text(encoding="utf-8"))
    marker.update(
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=list(layer_names),
    )
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    extraction = replace(
        source.extraction,
        geopackage_size_bytes=len(payload),
        geopackage_sha256=digest,
        all_layer_names=layer_names,
    )
    configured = replace(source, extraction=extraction)
    alternate_config_payload = SOURCE_CONFIG.model_dump(mode="python")
    alternate_config_payload["access"]["road_segments"] = {
        "class_label": "Voie secondaire",
        "match_tokens": ("voie", "secondaire"),
    }
    alternate_config = IgnBdTopoSourceConfig.model_validate(
        alternate_config_payload
    )
    forged = load_ign_bdtopo_roads(extraction, alternate_config)
    return configured, forged
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_road_normalization_reproduces_configured_logical_layer`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
configured, forged = _with_alternate_road_layer(_source())
```

**Action**

```python
loaded = load_ign_bdtopo_roads(configured.extraction, SOURCE_CONFIG)
normalized = normalize_ign_roads(loaded, SOURCE_CONFIG)
```

**Expected result**

```python
assert normalized.road_segments["source_layer"].eq(ROAD_LAYER).all()
with pytest.raises(IgnRoadNormalizationError, match="source|configured|physical"):
        normalize_ign_roads(forged, SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_road_normalization_reproduces_configured_logical_layer() -> None:
    configured, forged = _with_alternate_road_layer(_source())

    loaded = load_ign_bdtopo_roads(configured.extraction, SOURCE_CONFIG)
    normalized = normalize_ign_roads(loaded, SOURCE_CONFIG)
    assert normalized.road_segments["source_layer"].eq(ROAD_LAYER).all()

    with pytest.raises(IgnRoadNormalizationError, match="source|configured|physical"):
        normalize_ign_roads(forged, SOURCE_CONFIG)
```

### `test_public_api_exports_only_stable_road_normalization_symbols`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
import landscout.stages.normalize_access_ign as access_normalization
expected = {
        "IgnRoadNormalizationError",
        "NormalizedIgnRoadData",
        "normalize_ign_roads",
    }
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(access_normalization.__all__) == expected
assert expected <= set(stages.__all__)
assert all(hasattr(stages, name) for name in expected)
assert not hasattr(stages, "_validate_road_source")
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_api_exports_only_stable_road_normalization_symbols() -> None:
    import landscout.stages.normalize_access_ign as access_normalization

    expected = {
        "IgnRoadNormalizationError",
        "NormalizedIgnRoadData",
        "normalize_ign_roads",
    }
    assert set(access_normalization.__all__) == expected
    assert expected <= set(stages.__all__)
    assert all(hasattr(stages, name) for name in expected)
    assert not hasattr(stages, "_validate_road_source")
```

### `test_valid_linestring_normalization_has_exact_schema_identity_and_lineage`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
roads = normalized.road_segments
row = roads.iloc[0]
```

**Action**

```python
normalized = normalize_ign_roads(_source(), SOURCE_CONFIG)
```

**Expected result**

```python
assert type(normalized) is NormalizedIgnRoadData
assert list(roads.columns) == list(OUTPUT_COLUMNS)
assert isinstance(roads.index, pd.RangeIndex)
assert roads.index.tolist() == [0]
assert row["road_feature_id"] == "IGN_BDTOPO:ROAD_SEGMENT:ROAD-1"
assert row["road_feature_type"] == "ROAD_SEGMENT"
assert row["source_feature_id"] == "ROAD-1"
assert row["source_provider"] == "IGN"
assert row["source_product"] == "BD_TOPO"
assert row["source_layer"] == ROAD_LAYER
assert row["source_department_code"] == "31"
assert row["source_edition"] == "2026-06-15"
assert row["source_product_version"] == "3.5"
assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
assert row["source_archive_sha256"] == ARCHIVE_SHA256
assert row["source_url"] == SOURCE_URL
assert row["spatial_role"] == "PROXY_GEOMETRY"
assert row["geometry_status"] == "VALID"
assert roads.crs is not None and roads.crs.to_epsg() == 2154
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_linestring_normalization_has_exact_schema_identity_and_lineage() -> None:
    normalized = normalize_ign_roads(_source(), SOURCE_CONFIG)

    assert type(normalized) is NormalizedIgnRoadData
    roads = normalized.road_segments
    assert list(roads.columns) == list(OUTPUT_COLUMNS)
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.index.tolist() == [0]
    row = roads.iloc[0]
    assert row["road_feature_id"] == "IGN_BDTOPO:ROAD_SEGMENT:ROAD-1"
    assert row["road_feature_type"] == "ROAD_SEGMENT"
    assert row["source_feature_id"] == "ROAD-1"
    assert row["source_provider"] == "IGN"
    assert row["source_product"] == "BD_TOPO"
    assert row["source_layer"] == ROAD_LAYER
    assert row["source_department_code"] == "31"
    assert row["source_edition"] == "2026-06-15"
    assert row["source_product_version"] == "3.5"
    assert row["source_download_timestamp"] == "2026-08-11T15:32:03+00:00"
    assert row["source_archive_sha256"] == ARCHIVE_SHA256
    assert row["source_url"] == SOURCE_URL
    assert row["spatial_role"] == "PROXY_GEOMETRY"
    assert row["geometry_status"] == "VALID"
    assert roads.crs is not None and roads.crs.to_epsg() == 2154
```

### `test_valid_multilinestring_is_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
geometry = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )
```

**Action**

```python
roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments
```

**Expected result**

```python
assert roads.iloc[0]["geometry_status"] == "VALID"
assert roads.geometry.iloc[0].equals_exact(geometry, tolerance=0)
assert roads.geometry.iloc[0].geom_type == "MultiLineString"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_multilinestring_is_preserved() -> None:
    geometry = MultiLineString(
        [[(0, 0), (10, 10)], [(20, 20), (30, 30)]]
    )

    roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments

    assert roads.iloc[0]["geometry_status"] == "VALID"
    assert roads.geometry.iloc[0].equals_exact(geometry, tolerance=0)
    assert roads.geometry.iloc[0].geom_type == "MultiLineString"
```

### `test_z_coordinates_are_preserved_exactly`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
geometry = LineString([(0, 0, 12), (10, 10, 24)])
```

**Action**

```python
roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments
```

**Expected result**

```python
assert roads.geometry.iloc[0].has_z
assert roads.geometry.iloc[0].wkb == geometry.wkb
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_z_coordinates_are_preserved_exactly() -> None:
    geometry = LineString([(0, 0, 12), (10, 10, 24)])

    roads = normalize_ign_roads(
        _source(_road_frame([geometry])), SOURCE_CONFIG
    ).road_segments

    assert roads.geometry.iloc[0].has_z
    assert roads.geometry.iloc[0].wkb == geometry.wkb
```

### `test_row_count_order_geometry_and_range_index_are_preserved`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
geometries = [
        LineString([(20, 0), (20, 10)]),
        LineString([(5, 0), (5, 10)]),
    ]
source = _source(
        _road_frame(
            geometries,
            identifiers=["SECOND", "FIRST"],
            index=[91, 14],
        )
    )
```

**Action**

```python
roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments
```

**Expected result**

```python
assert len(roads) == 2
assert roads["source_feature_id"].tolist() == ["SECOND", "FIRST"]
assert roads["road_feature_id"].tolist() == [
        "IGN_BDTOPO:ROAD_SEGMENT:SECOND",
        "IGN_BDTOPO:ROAD_SEGMENT:FIRST",
    ]
assert isinstance(roads.index, pd.RangeIndex)
assert roads.geometry.to_wkb().tolist() == [value.wkb for value in geometries]
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_row_count_order_geometry_and_range_index_are_preserved() -> None:
    geometries = [
        LineString([(20, 0), (20, 10)]),
        LineString([(5, 0), (5, 10)]),
    ]
    source = _source(
        _road_frame(
            geometries,
            identifiers=["SECOND", "FIRST"],
            index=[91, 14],
        )
    )

    roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments

    assert len(roads) == 2
    assert roads["source_feature_id"].tolist() == ["SECOND", "FIRST"]
    assert roads["road_feature_id"].tolist() == [
        "IGN_BDTOPO:ROAD_SEGMENT:SECOND",
        "IGN_BDTOPO:ROAD_SEGMENT:FIRST",
    ]
    assert isinstance(roads.index, pd.RangeIndex)
    assert roads.geometry.to_wkb().tolist() == [value.wkb for value in geometries]
```

### `test_raw_access_and_restriction_values_are_copied_without_interpretation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _road_frame()
source.loc[source.index[0], "importance"] = "00"
source.loc[source.index[0], "prive"] = "Valeur IGN non interprétée"
source.loc[source.index[0], "acces_vehicule_leger"] = "Inconnu"
source.loc[source.index[0], "restriction_de_poids_total"] = 19.75
source.loc[source.index[0], "nature_de_la_restriction"] = None
```

**Action**

```python
row = normalize_ign_roads(_source(source), SOURCE_CONFIG).road_segments.iloc[0]
```

**Expected result**

```python
assert row["importance_raw"] == "00"
assert row["private_raw"] == "Valeur IGN non interprétée"
assert row["light_vehicle_access_raw"] == "Inconnu"
assert row["restriction_total_weight_raw"] == 19.75
assert pd.isna(row["restriction_nature_raw"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_raw_access_and_restriction_values_are_copied_without_interpretation() -> None:
    source = _road_frame()
    source.loc[source.index[0], "importance"] = "00"
    source.loc[source.index[0], "prive"] = "Valeur IGN non interprétée"
    source.loc[source.index[0], "acces_vehicule_leger"] = "Inconnu"
    source.loc[source.index[0], "restriction_de_poids_total"] = 19.75
    source.loc[source.index[0], "nature_de_la_restriction"] = None

    row = normalize_ign_roads(_source(source), SOURCE_CONFIG).road_segments.iloc[0]

    assert row["importance_raw"] == "00"
    assert row["private_raw"] == "Valeur IGN non interprétée"
    assert row["light_vehicle_access_raw"] == "Inconnu"
    assert row["restriction_total_weight_raw"] == 19.75
    assert pd.isna(row["restriction_nature_raw"])
```

### `test_every_raw_field_preserves_source_values_nulls_and_dtype`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
for source_column, output_column in RAW_FIELD_MAPPING:
        pd.testing.assert_series_equal(
            roads[output_column],
            source.road_segments[source_column].reset_index(drop=True),
            check_names=False,
            check_dtype=True,
        )
```

**Action**

```python
roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_every_raw_field_preserves_source_values_nulls_and_dtype() -> None:
    source = _source()

    roads = normalize_ign_roads(source, SOURCE_CONFIG).road_segments

    for source_column, output_column in RAW_FIELD_MAPPING:
        pd.testing.assert_series_equal(
            roads[output_column],
            source.road_segments[source_column].reset_index(drop=True),
            check_names=False,
            check_dtype=True,
        )
```

### `test_missing_required_source_field_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
source = _source()
frame = source.road_segments.drop(columns=column)
mutated = replace(source, road_segments=frame)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match=column):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_missing_required_source_field_is_rejected(column: str) -> None:
    source = _source()
    frame = source.road_segments.drop(columns=column)
    mutated = replace(source, road_segments=frame)

    with pytest.raises(IgnRoadNormalizationError, match=column):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

### `test_null_or_empty_cleabs_is_rejected`

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
with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_null_or_empty_cleabs_is_rejected(identifier: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )
```

### `test_unsafe_cleabs_is_rejected`

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
with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unsafe_cleabs_is_rejected(identifier: str) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="cleabs"):
        normalize_ign_roads(
            _source(_road_frame(identifiers=[identifier])), SOURCE_CONFIG
        )
```

### `test_duplicate_cleabs_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
frame = _road_frame(
        [LineString([(0, 0), (1, 1)]), LineString([(2, 2), (3, 3)])],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="unique"):
        normalize_ign_roads(_source(frame), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_cleabs_is_rejected() -> None:
    frame = _road_frame(
        [LineString([(0, 0), (1, 1)]), LineString([(2, 2), (3, 3)])],
        identifiers=["DUPLICATE", "DUPLICATE"],
    )

    with pytest.raises(IgnRoadNormalizationError, match="unique"):
        normalize_ign_roads(_source(frame), SOURCE_CONFIG)
```

### `test_wrong_or_missing_road_crs_is_rejected`

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
with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(_source(_road_frame(crs=crs)), SOURCE_CONFIG)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_or_missing_road_crs_is_rejected(crs: str | None) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(_source(_road_frame(crs=crs)), SOURCE_CONFIG)
```

### `test_wrong_archive_identity_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `message`, `value`.

**Setup**

```python
source = _source()
archive = replace(source.extraction.archive, **{field: value})
mutated = replace(source, extraction=replace(source.extraction, archive=archive))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match=message):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_wrong_archive_identity_is_rejected(
    field: str,
    value: str,
    message: str,
) -> None:
    source = _source()
    archive = replace(source.extraction.archive, **{field: value})
    mutated = replace(source, extraction=replace(source.extraction, archive=archive))

    with pytest.raises(IgnRoadNormalizationError, match=message):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

### `test_wrong_source_spatial_role_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `component`.

**Setup**

```python
source = _source()
wrong_role = cast(Any, "AUTHORITATIVE_ACCESS")
if component == "archive":
        archive = replace(source.extraction.archive, spatial_role=wrong_role)
        mutated = replace(
            source,
            extraction=replace(source.extraction, archive=archive),
        )
    elif component == "extraction":
        mutated = replace(
            source,
            extraction=replace(source.extraction, spatial_role=wrong_role),
        )
    else:
        mutated = replace(
            source,
            road_segments_summary=replace(
                source.road_segments_summary,
                spatial_role=wrong_role,
            ),
        )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="PROXY_GEOMETRY"):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_wrong_source_spatial_role_is_rejected(component: str) -> None:
    source = _source()
    wrong_role = cast(Any, "AUTHORITATIVE_ACCESS")
    if component == "archive":
        archive = replace(source.extraction.archive, spatial_role=wrong_role)
        mutated = replace(
            source,
            extraction=replace(source.extraction, archive=archive),
        )
    elif component == "extraction":
        mutated = replace(
            source,
            extraction=replace(source.extraction, spatial_role=wrong_role),
        )
    else:
        mutated = replace(
            source,
            road_segments_summary=replace(
                source.road_segments_summary,
                spatial_role=wrong_role,
            ),
        )

    with pytest.raises(IgnRoadNormalizationError, match="PROXY_GEOMETRY"):
        normalize_ign_roads(mutated, SOURCE_CONFIG)
```

### `test_summary_row_count_mismatch_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
summary = replace(source.road_segments_summary, feature_count=2)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="row count"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_summary_row_count_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, feature_count=2)

    with pytest.raises(IgnRoadNormalizationError, match="row count"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

### `test_road_summary_requires_strict_structural_types`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
source = _source()
changed = replace(source.road_segments_summary, **{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_road_summary_requires_strict_structural_types(
    field: str, value: object
) -> None:
    source = _source()
    changed = replace(source.road_segments_summary, **{field: value})

    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )
```

### `test_road_archive_sha256_requires_canonical_lowercase`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `value`.

**Setup**

```python
source = _source()
extraction = replace(
        source.extraction,
        archive=replace(source.extraction.archive, sha256=value),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_road_archive_sha256_requires_canonical_lowercase(value: str) -> None:
    source = _source()
    extraction = replace(
        source.extraction,
        archive=replace(source.extraction.archive, sha256=value),
    )

    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

### `test_summary_crs_mismatch_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
summary = replace(source.road_segments_summary, crs="EPSG:4326")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_summary_crs_mismatch_is_rejected() -> None:
    source = _source()
    summary = replace(source.road_segments_summary, crs="EPSG:4326")

    with pytest.raises(IgnRoadNormalizationError, match="CRS|2154"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

### `test_forged_ordered_summary_schema_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
source = _source()
summary = source.road_segments_summary
if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "float64")
        changed = replace(summary, dtypes=tuple(dtypes))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="schema|columns|dtype"):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_forged_ordered_summary_schema_is_rejected(mutation: str) -> None:
    source = _source()
    summary = source.road_segments_summary
    if mutation == "missing":
        changed = replace(summary, columns=summary.columns[:-1])
    elif mutation == "extra":
        changed = replace(summary, columns=(*summary.columns, "invented"))
    elif mutation == "reordered":
        changed = replace(summary, columns=tuple(reversed(summary.columns)))
    else:
        dtypes = list(summary.dtypes)
        dtypes[0] = (dtypes[0][0], "float64")
        changed = replace(summary, dtypes=tuple(dtypes))

    with pytest.raises(IgnRoadNormalizationError, match="schema|columns|dtype"):
        normalize_ign_roads(
            replace(source, road_segments_summary=changed), SOURCE_CONFIG
        )
```

### `test_road_source_rejects_physical_role_collision`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `role`.

**Setup**

```python
source = _source()
selected = (
        source.extraction.electric_lines_layer
        if role == "electric"
        else source.extraction.transformation_posts_layer
    )
summary = replace(source.road_segments_summary, source_layer_name=selected)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="same layer|distinct|role"):
        normalize_ign_roads(
            replace(
                source,
                road_segments_summary=summary,
            ),
            SOURCE_CONFIG,
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_road_source_rejects_physical_role_collision(role: str) -> None:
    source = _source()
    selected = (
        source.extraction.electric_lines_layer
        if role == "electric"
        else source.extraction.transformation_posts_layer
    )
    summary = replace(source.road_segments_summary, source_layer_name=selected)
    with pytest.raises(IgnRoadNormalizationError, match="same layer|distinct|role"):
        normalize_ign_roads(
            replace(
                source,
                road_segments_summary=summary,
            ),
            SOURCE_CONFIG,
        )
```

### `test_road_source_rejects_duplicate_layer_inventory`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
extraction = replace(
        source.extraction,
        all_layer_names=(*source.extraction.all_layer_names, ROAD_LAYER),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="inventory|duplicate"):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_road_source_rejects_duplicate_layer_inventory() -> None:
    source = _source()
    extraction = replace(
        source.extraction,
        all_layer_names=(*source.extraction.all_layer_names, ROAD_LAYER),
    )

    with pytest.raises(IgnRoadNormalizationError, match="inventory|duplicate"):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

### `test_summary_geometry_facts_mismatch_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
source = _source()
summary = replace(source.road_segments_summary, **{field: value})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="geometry summary"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_summary_geometry_facts_mismatch_is_rejected(
    field: str,
    value: object,
) -> None:
    source = _source()
    summary = replace(source.road_segments_summary, **{field: value})

    with pytest.raises(IgnRoadNormalizationError, match="geometry summary"):
        normalize_ign_roads(
            replace(source, road_segments_summary=summary), SOURCE_CONFIG
        )
```

### `test_summary_layer_must_exist_in_extraction_inventory`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
extraction = replace(source.extraction, all_layer_names=("other_layer",))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="layer inventory"):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_summary_layer_must_exist_in_extraction_inventory() -> None:
    source = _source()
    extraction = replace(source.extraction, all_layer_names=("other_layer",))

    with pytest.raises(IgnRoadNormalizationError, match="layer inventory"):
        normalize_ign_roads(replace(source, extraction=extraction), SOURCE_CONFIG)
```

### `test_summary_layer_and_logical_name_must_be_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
wrong_layer = replace(source.road_segments_summary, source_layer_name="route")
wrong_logical = replace(
        source.road_segments_summary,
        logical_name=cast(Any, "electric_lines"),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="physical layer"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_layer), SOURCE_CONFIG
        )
with pytest.raises(IgnRoadNormalizationError, match="logical name"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_logical), SOURCE_CONFIG
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_summary_layer_and_logical_name_must_be_exact() -> None:
    source = _source()
    wrong_layer = replace(source.road_segments_summary, source_layer_name="route")
    with pytest.raises(IgnRoadNormalizationError, match="physical layer"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_layer), SOURCE_CONFIG
        )

    wrong_logical = replace(
        source.road_segments_summary,
        logical_name=cast(Any, "electric_lines"),
    )
    with pytest.raises(IgnRoadNormalizationError, match="logical name"):
        normalize_ign_roads(
            replace(source, road_segments_summary=wrong_logical), SOURCE_CONFIG
        )
```

### `test_valid_unsupported_geometry_type_is_rejected`

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
with pytest.raises(IgnRoadNormalizationError, match="geometry types"):
        normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_unsupported_geometry_type_is_rejected(geometry: object) -> None:
    with pytest.raises(IgnRoadNormalizationError, match="geometry types"):
        normalize_ign_roads(_source(_road_frame([geometry])), SOURCE_CONFIG)
```

### `test_null_empty_and_invalid_geometry_are_preserved_with_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
invalid = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
frame = _road_frame(
        [None, LineString(), invalid],
        identifiers=["NULL", "EMPTY", "INVALID"],
    )
```

**Action**

```python
roads = normalize_ign_roads(_source(frame), SOURCE_CONFIG).road_segments
```

**Expected result**

```python
assert roads["geometry_status"].tolist() == ["NULL", "EMPTY", "INVALID"]
assert roads.geometry.iloc[0] is None
assert roads.geometry.iloc[1].is_empty
assert roads.geometry.iloc[2].equals_exact(invalid, tolerance=0)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_null_empty_and_invalid_geometry_are_preserved_with_status() -> None:
    invalid = Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
    frame = _road_frame(
        [None, LineString(), invalid],
        identifiers=["NULL", "EMPTY", "INVALID"],
    )

    roads = normalize_ign_roads(_source(frame), SOURCE_CONFIG).road_segments

    assert roads["geometry_status"].tolist() == ["NULL", "EMPTY", "INVALID"]
    assert roads.geometry.iloc[0] is None
    assert roads.geometry.iloc[1].is_empty
    assert roads.geometry.iloc[2].equals_exact(invalid, tolerance=0)
```

### `test_normalization_does_not_mutate_input`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
before = deepcopy(source.road_segments)
assert_geodataframe_equal(source.road_segments, before)
```

**Action**

```python
normalize_ign_roads(source, SOURCE_CONFIG)
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_normalization_does_not_mutate_input() -> None:
    source = _source()
    before = deepcopy(source.road_segments)

    normalize_ign_roads(source, SOURCE_CONFIG)

    assert_geodataframe_equal(source.road_segments, before)
```

### `test_high_level_rejects_coordinated_road_frame_and_summary_forgery`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
source = _source()
forged = source.road_segments.copy()
forged.loc[0, "nature"] = "Invented road nature"
forged_summary = _summary(forged)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(IgnRoadNormalizationError, match="physical|fresh|source"):
        normalize_ign_roads(
            replace(
                source,
                road_segments=forged,
                road_segments_summary=forged_summary,
            ),
            SOURCE_CONFIG,
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_high_level_rejects_coordinated_road_frame_and_summary_forgery() -> None:
    source = _source()
    forged = source.road_segments.copy()
    forged.loc[0, "nature"] = "Invented road nature"
    forged_summary = _summary(forged)

    with pytest.raises(IgnRoadNormalizationError, match="physical|fresh|source"):
        normalize_ign_roads(
            replace(
                source,
                road_segments=forged,
                road_segments_summary=forged_summary,
            ),
            SOURCE_CONFIG,
        )
```

### `test_malformed_public_input_has_controlled_error`

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
with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(cast(Any, object()), SOURCE_CONFIG)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_public_input_has_controlled_error() -> None:
    with pytest.raises(IgnRoadNormalizationError):
        normalize_ign_roads(cast(Any, object()), SOURCE_CONFIG)
```


## 7. Data contracts

### `OUTPUT_COLUMNS` — canonical or derived frame-column schema

```python
OUTPUT_COLUMNS = (
    "road_feature_id",
    "road_feature_type",
    "source_provider",
    "source_product",
    "source_layer",
    "source_feature_id",
    "source_department_code",
    "source_edition",
    "source_product_version",
    "source_download_timestamp",
    "source_archive_sha256",
    "source_url",
    "nature_raw",
    "importance_raw",
    "fictitious_raw",
    "position_relative_to_ground_raw",
    "asset_status_raw",
    "lane_count_raw",
    "carriageway_width_raw",
    "private_raw",
    "traffic_direction_raw",
    "urban_raw",
    "mean_light_vehicle_speed_raw",
    "light_vehicle_access_raw",
    "closure_period_raw",
    "restriction_nature_raw",
    "restriction_height_raw",
    "restriction_total_weight_raw",
    "restriction_axle_weight_raw",
    "restriction_width_raw",
    "restriction_length_raw",
    "dangerous_goods_forbidden_raw",
    "administrative_classification_raw",
    "manager_raw",
    "source_name_raw",
    "source_identifiers_raw",
    "source_created_at",
    "source_modified_at",
    "source_confirmed_at",
    "planimetric_acquisition_method",
    "planimetric_precision_raw",
    "spatial_role",
    "geometry_status",
    "geometry",
)
```

### `RAW_FIELD_MAPPING` — mapping between source/input and output keys or columns

```python
RAW_FIELD_MAPPING = (
    ("nature", "nature_raw"),
    ("importance", "importance_raw"),
    ("fictif", "fictitious_raw"),
    ("position_par_rapport_au_sol", "position_relative_to_ground_raw"),
    ("etat_de_l_objet", "asset_status_raw"),
    ("nombre_de_voies", "lane_count_raw"),
    ("largeur_de_chaussee", "carriageway_width_raw"),
    ("prive", "private_raw"),
    ("sens_de_circulation", "traffic_direction_raw"),
    ("urbain", "urban_raw"),
    ("vitesse_moyenne_vl", "mean_light_vehicle_speed_raw"),
    ("acces_vehicule_leger", "light_vehicle_access_raw"),
    ("periode_de_fermeture", "closure_period_raw"),
    ("nature_de_la_restriction", "restriction_nature_raw"),
    ("restriction_de_hauteur", "restriction_height_raw"),
    ("restriction_de_poids_total", "restriction_total_weight_raw"),
    ("restriction_de_poids_par_essieu", "restriction_axle_weight_raw"),
    ("restriction_de_largeur", "restriction_width_raw"),
    ("restriction_de_longueur", "restriction_length_raw"),
    ("matieres_dangereuses_interdites", "dangerous_goods_forbidden_raw"),
    ("cpx_classement_administratif", "administrative_classification_raw"),
    ("cpx_gestionnaire", "manager_raw"),
    ("sources", "source_name_raw"),
    ("identifiants_sources", "source_identifiers_raw"),
    ("date_creation", "source_created_at"),
    ("date_modification", "source_modified_at"),
    ("date_de_confirmation", "source_confirmed_at"),
    ("methode_d_acquisition_planimetrique", "planimetric_acquisition_method"),
    ("precision_planimetrique", "planimetric_precision_raw"),
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
