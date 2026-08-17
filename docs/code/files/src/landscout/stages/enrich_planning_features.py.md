# `src/landscout/stages/enrich_planning_features.py`

## File identity

- Repository path: `src/landscout/stages/enrich_planning_features.py`
- File type: Python source
- Layer: spatial proxy enrichment stage
- Domain: planning
- Responsibility: Normalizes GPU planning feature catalogs and constructs validated factual parcel-feature relations.
- Source SHA256: `01a56b482a3c956d1f8a7069b94c69518758ea3937c3d98ef8ae5d74615d6148`

## 1. Purpose

Normalizes GPU planning feature catalogs and constructs validated factual parcel-feature relations.

## 2. Position in LandScout architecture

This file belongs to the **spatial proxy enrichment stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `from dataclasses import dataclass, replace`
- `from datetime import date, datetime`
- `from hashlib import sha256`
- `from math import isfinite`
- `from numbers import Integral, Real`
- `from typing import Literal, NamedTuple`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pyproj import CRS`
- `from shapely import (  # type: ignore[import-untyped]
    area as shapely_area,
)`
- `from shapely import (
    contains,
    covers,
    force_2d,
    get_coordinate_dimension,
    get_parts,
    intersection,
    union_all,
)`
- `from shapely import (
    length as shapely_length,
)`

### Internal LandScout imports

- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)`
- `from landscout.common.planning_feature_schema import (
    NORMALIZED_FEATURE_COLUMNS,
    NORMALIZED_FEATURE_DTYPES,
    NORMALIZED_RELATION_DTYPES,
    RELATION_COLUMNS,
    RELATION_COUNT_COLUMNS,
    RELATION_FLOAT_COLUMNS,
    RELATION_STRING_COLUMNS,
    normalized_feature_dtypes,
    validate_canonical_frame_schema,
)`
- `from landscout.common.planning_overlay import technical_overlay_tolerance`
- `from landscout.sources.gpu_fr import (
    GpuInspectedLayer,
    GpuPlanningDocument,
    GpuSpatialInspectionError,
    GpuValidatedSpatialLayerSource,
    revalidate_gpu_spatial_layer_sources,
)`

## 4. Contract taxonomy

### A. Python constants

#### `CALCULATION_CRS`

```python
CALCULATION_CRS = "EPSG:2154"
```

Coordinate-reference-system identity used for an explicit storage, validation, or calculation boundary. Consumers include `src/landscout/stages/enrich_planning_features.py::_normalize_layer` (value reference), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (value reference), `src/landscout/stages/enrich_planning_features.py::_combine_catalogs` (value reference), `src/landscout/stages/enrich_planning_features.py::_metric_parcels` (value reference), `src/landscout/stages/enrich_planning_features.py::_relation_base` (value reference).

#### `PARCEL_REQUIRED_COLUMNS`

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::_validate_parcels` (value reference).

#### `SOURCE_IDENTITY_KINDS`

```python
SOURCE_IDENTITY_KINDS = frozenset({"CNIG_ATTRIBUTE", "ARCHIVE_SCOPED_OGR_FID"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` (value reference).

#### `SURFACE_TYPES`

```python
SURFACE_TYPES = frozenset({"Polygon", "MultiPolygon"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_parcels` (value reference).

#### `LINE_TYPES`

```python
LINE_TYPES = frozenset({"LineString", "MultiLineString"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (value reference).

#### `POINT_TYPES`

```python
POINT_TYPES = frozenset({"Point", "MultiPoint"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (value reference).

#### `LAYER_SPECS`

```python
LAYER_SPECS = {
    "prescription_surface": _LayerSpec(
        "prescription_surface",
        "PRESCRIPTION",
        "SURFACE",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        SURFACE_TYPES,
    ),
    "prescription_line": _LayerSpec(
        "prescription_line",
        "PRESCRIPTION",
        "LINE",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        LINE_TYPES,
    ),
    "prescription_point": _LayerSpec(
        "prescription_point",
        "PRESCRIPTION",
        "POINT",
        "LIB_IDPSC",
        "TYPEPSC",
        "STYPEPSC",
        POINT_TYPES,
    ),
    "information_surface": _LayerSpec(
        "information_surface",
        "INFORMATION",
        "SURFACE",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        SURFACE_TYPES,
    ),
    "information_line": _LayerSpec(
        "information_line",
        "INFORMATION",
        "LINE",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        LINE_TYPES,
    ),
    "information_point": _LayerSpec(
        "information_point",
        "INFORMATION",
        "POINT",
        "LIB_IDINFO",
        "TYPEINF",
        "STYPEINF",
        POINT_TYPES,
    ),
}
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs` (value reference), `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs.combined` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` (value reference).

#### `COMMON_SOURCE_FIELDS`

```python
COMMON_SOURCE_FIELDS = {
    "label_raw": "LIBELLE",
    "text_raw": "TXT",
    "regulation_filename_raw": "NOMFIC",
    "regulation_url_raw": "URLFIC",
    "source_document_reference_raw": "IDURBA",
    "source_validity_date_raw": "DATVALID",
}
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::_normalize_layer` (value reference).

#### `OPTIONAL_SOURCE_FIELDS`

```python
OPTIONAL_SOURCE_FIELDS = frozenset(
    {
        "LIBELLE",
        "TXT",
        "NOMFIC",
        "URLFIC",
        "DATVALID",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `_CATALOG_GEOMETRY_TYPES`

```python
_CATALOG_GEOMETRY_TYPES = {
    "SURFACE": SURFACE_TYPES,
    "LINE": LINE_TYPES,
    "POINT": POINT_TYPES,
}
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` (value reference).

#### `_CATALOG_REQUIRED_EXACT_STRING_COLUMNS`

```python
_CATALOG_REQUIRED_EXACT_STRING_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "source_document_reference_raw",
    "source_provider",
    "source_portal",
    "source_commune_code",
    "source_document_id",
    "source_document_type",
    "source_archive_name",
    "source_archive_sha256",
    "source_layer",
    "source_crs",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` (value reference).

#### `_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS`

```python
_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS = (
    "label_raw",
    "text_raw",
    "regulation_filename_raw",
    "regulation_url_raw",
    "source_validity_date_raw",
    "source_standard_model",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` (value reference).

#### `PARCEL_OUTPUT_COLUMNS`

```python
PARCEL_OUTPUT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "planning_surface_intersection_area_sum_m2",
        "planning_surface_covered_union_area_m2",
        "planning_surface_covered_pct",
        "prescription_surface_relation_count",
        "prescription_surface_covered_union_area_m2",
        "prescription_surface_covered_pct",
        "information_surface_relation_count",
        "information_surface_covered_union_area_m2",
        "information_surface_covered_pct",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_line_intersection_length_sum_m",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::_validate_parcels` (value reference), `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_parcel_output` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_result` (value reference).

#### `PARCEL_COUNT_COLUMNS`

```python
PARCEL_COUNT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
    }
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_parcel_output` (value reference), `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` (value reference).

#### `_RELATION_CATALOG_FIELDS`

```python
_RELATION_CATALOG_FIELDS = (
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "label_raw",
    "text_raw",
    "source_document_id",
    "source_archive_sha256",
    "source_layer",
    "source_validity_date_raw",
    "regulation_filename_raw",
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/enrich_planning_features.py::_validate_relation_catalog_consistency` (value reference).


### B. Type aliases and closed domains

#### `FeatureFamily`

```python
FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
```

Official planning-feature family domain: PRESCRIPTION or INFORMATION. Enforced/consumed by `src/landscout/stages/enrich_planning_features.py::_LayerSpec` (type annotation).

#### `GeometryKind`

```python
GeometryKind = Literal["SURFACE", "LINE", "POINT"]
```

Closed planning-feature geometry-family domain: SURFACE, LINE, or POINT. Enforced/consumed by `src/landscout/stages/enrich_planning_features.py::_LayerSpec` (type annotation), `src/landscout/stages/enrich_planning_features.py::_canonical_catalog_dtypes` (type annotation), `src/landscout/stages/enrich_planning_features.py::_empty_catalog` (type annotation), `src/landscout/stages/enrich_planning_features.py::_combine_catalogs` (type annotation), `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs.combined` (type annotation), `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` (type annotation).

#### `SourceIdentityKind`

```python
SourceIdentityKind = Literal["CNIG_ATTRIBUTE", "ARCHIVE_SCOPED_OGR_FID"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/stages/enrich_planning_features.py::_source_feature_ids` (type annotation).


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "ParcelPlanningFeaturesResult",
    "PlanningFeatureInputValidation",
    "PlanningFeaturesError",
    "intersect_parcels_with_gpu_planning_features",
    "validate_normalized_planning_feature_inputs",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `_LayerSpec`

**Purpose:** Immutable named tuple defining one GPU planning-feature logical layer's family, geometry kind, source fields, identity field, and allowed geometry types.

**Kind:** immutable named tuple.

**Inheritance:** `NamedTuple`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `logical_layer` | `logical_layer: str` | LandScout logical GPU feature-layer name represented by this normalization specification. |
| `feature_family` | `feature_family: FeatureFamily` | `_LayerSpec.feature_family` represents the `feature_family` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `geometry_kind` | `geometry_kind: GeometryKind` | `_LayerSpec.geometry_kind` represents the `geometry_kind` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `identity_field` | `identity_field: str` | Source attribute selected as the stable feature identity for this layer specification. |
| `type_field` | `type_field: str` | `_LayerSpec.type_field` represents the `type_field` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `subtype_field` | `subtype_field: str` | `_LayerSpec.subtype_field` represents the `subtype_field` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `allowed_geometry_types` | `allowed_geometry_types: frozenset[str]` | `_LayerSpec.allowed_geometry_types` represents the `allowed_geometry_types` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- constructor call: `src/landscout/stages/enrich_planning_features.py::<module>` via `_LayerSpec`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::_source_feature_ids` via `_LayerSpec`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_LayerSpec`.

**Exact class source**

```python
class _LayerSpec(NamedTuple):
    logical_layer: str
    feature_family: FeatureFamily
    geometry_kind: GeometryKind
    identity_field: str
    type_field: str
    subtype_field: str
    allowed_geometry_types: frozenset[str]
```

### `PlanningFeaturesError`

**Purpose:** Raised when factual GPU feature measurement cannot be completed safely.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- import: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_strict_string` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_strict_nonnegative_integer` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_ids` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_exact_strings` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_crs` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_active_geometry` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_geometries` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_two_dimensional_geometry` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_parcels` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_standard_model` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_layer_summary` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_project_geometry` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_source_feature_ids` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_metric_parcels` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_relation_base` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_surface_relations` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_line_relations` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_point_relations` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_canonical_integrity_value` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_canonical_integrity_sha256` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_surface_union_summary` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_numeric_values` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_integer_values` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_require_close` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_compare_normalized_catalog` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_relation_catalog_consistency` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_relation_semantics` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_relations` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_parcel_output` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::validate_normalized_planning_feature_inputs` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `PlanningFeaturesError`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_result` via `PlanningFeaturesError`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_invalid_parcel_ids_are_rejected` via `pytest.raises(PlanningFeaturesError, match='parcel_id')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_duplicate_parcel_ids_are_rejected` via `pytest.raises(PlanningFeaturesError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_duplicate_source_ids_are_rejected` via `pytest.raises(PlanningFeaturesError, match='unique')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_idurba_mismatch_is_rejected` via `pytest.raises(PlanningFeaturesError, match='IDURBA')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_missing_required_source_fields_fail` via `pytest.raises(PlanningFeaturesError, match=missing)`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_wrong_geometry_kind_is_rejected` via `pytest.raises(PlanningFeaturesError, match='geometry')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_invalid_surface_geometry_is_rejected_without_repair` via `pytest.raises(PlanningFeaturesError, match='valid')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_null_or_empty_source_geometry_is_rejected` via `pytest.raises(PlanningFeaturesError, match='geometry')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_missing_crs_is_rejected` via `pytest.raises(PlanningFeaturesError, match='CRS|physical revalidation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_unusable_source_crs_is_rejected` via `pytest.raises(PlanningFeaturesError, match='CRS')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected` via `pytest.raises(PlanningFeaturesError, match='summary|physical revalidation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers` via `pytest.raises(PlanningFeaturesError, match='integer count|non-negative|summary|physical revalidation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_reserved_output_column_collision_is_rejected` via `pytest.raises(PlanningFeaturesError, match='output columns')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_wraps_malformed_document_context` via `pytest.raises(PlanningFeaturesError)`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_binds_inspected_spatial_inventory` via `pytest.raises(PlanningFeaturesError, match='inventory|reference')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_rejects_stripped_catalog` via `pytest.raises(PlanningFeaturesError, match='schema|label_raw')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_strict_relation_integer_counts_are_enforced` via `pytest.raises(PlanningFeaturesError, match='integer count|non-negative|dtype|schema')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_strict_parcel_summary_integer_counts_are_enforced` via `pytest.raises(PlanningFeaturesError, match='integer count|non-negative')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_corrupted_relation_semantics_are_rejected` via `pytest.raises(PlanningFeaturesError)`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_point_member_relation_semantics_are_exact` via `pytest.raises(PlanningFeaturesError, match='relation type')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_relation_must_match_feature_catalog` via `pytest.raises(PlanningFeaturesError, match='catalog|geometry kind|LINE relation|unrelated metric')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_feature_ids_are_globally_unique_across_catalogs` via `pytest.raises(PlanningFeaturesError, match='globally unique|deterministic')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_corrupted_parcel_summary_is_rejected` via `pytest.raises(PlanningFeaturesError, match='inconsistent with relations')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_corrupted_surface_union_contract_is_rejected` via `pytest.raises(PlanningFeaturesError, match='union')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_geospatial_operation_failure_is_controlled_and_chained` via `pytest.raises(PlanningFeaturesError, match='spatial join')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_unknown_relation_parcel` via `pytest.raises(PlanningFeaturesError, match='parcel|source')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_parcel_metric_mutation` via `pytest.raises(PlanningFeaturesError, match='parcel|metric|source')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_same_area_wrong_parcel_relation` via `pytest.raises(PlanningFeaturesError, match='relation|parcel|rebuilt|source')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_missing_expected_relation` via `pytest.raises(PlanningFeaturesError, match='relation|rebuilt|source')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_extra_geometrically_false_relation` via `pytest.raises(PlanningFeaturesError, match='relation|rebuilt|source')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_relations` via `pytest.raises(PlanningFeaturesError, match='relation|order|rebuilt')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_noncanonical_relation_dtype` via `pytest.raises(PlanningFeaturesError, match='schema|dtype|relation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_name_change` via `pytest.raises(PlanningFeaturesError, match='schema|index|relation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_dtype_change` via `pytest.raises(PlanningFeaturesError, match='schema|index|relation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_class_change` via `pytest.raises(PlanningFeaturesError, match='schema|index|relation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_coherent_but_wrong_line_metric` via `pytest.raises(PlanningFeaturesError, match='relation|metric|rebuilt')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_partial_parcel_output_columns` via `pytest.raises(PlanningFeaturesError, match='[Pp]arcel|output|summary|columns')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_corrupted_complete_parcel_summaries` via `pytest.raises(PlanningFeaturesError, match='parcel|summary|relation')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_noncanonical_parcel_summary_dtype` via `pytest.raises(PlanningFeaturesError, match='parcel|schema|dtype|summary')`.
- expected exception type: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_each_corrupted_parcel_summary_fact` via `pytest.raises(PlanningFeaturesError, match='parcel|summary|relation|lineage|document|archive|union|percentage')`.

**Exact class source**

```python
class PlanningFeaturesError(ValueError):
    """Raised when factual GPU feature measurement cannot be completed safely."""
```

### `ParcelPlanningFeaturesResult`

**Purpose:** Normalized feature catalogs, parcel enrichment, and factual relations.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `surface_features` | `surface_features: gpd.GeoDataFrame` | Canonical surface planning-feature catalog in this result envelope. |
| `line_features` | `line_features: gpd.GeoDataFrame` | Canonical line planning-feature catalog in this result envelope. |
| `point_features` | `point_features: gpd.GeoDataFrame` | Canonical point planning-feature catalog in this result envelope. |
| `relations` | `relations: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- import: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::_validate_result` via `ParcelPlanningFeaturesResult`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `ParcelPlanningFeaturesResult`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `ParcelPlanningFeaturesResult`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_run` via `ParcelPlanningFeaturesResult`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_contract_result` via `ParcelPlanningFeaturesResult`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_source_complete_contract` via `ParcelPlanningFeaturesResult`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_two_parcel_source_complete_contract` via `ParcelPlanningFeaturesResult`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_validate_source_complete` via `ParcelPlanningFeaturesResult`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `ParcelPlanningFeaturesResult`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `ParcelPlanningFeaturesResult`.

**Exact class source**

```python
class ParcelPlanningFeaturesResult:
    """Normalized feature catalogs, parcel enrichment, and factual relations."""

    parcels: gpd.GeoDataFrame
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame
```

### `PlanningFeatureInputValidation`

**Purpose:** Immutable source-completeness evidence for normalized planning facts.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `gpu_related_source_files_sha256` | `gpu_related_source_files_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `expected_relations_content_sha256` | `expected_relations_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `related_source_layer_count` | `related_source_layer_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `related_source_file_count` | `related_source_file_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `expected_relation_count` | `expected_relation_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- import: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.stages.enrich_planning_features import (
    PlanningFeatureInputValidation,
    validate_normalized_planning_feature_inputs,
)`.
- import: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `PlanningFeatureInputValidation`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `PlanningFeatureInputValidation`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::validate_normalized_planning_feature_inputs` via `PlanningFeatureInputValidation`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `PlanningFeatureInputValidation`.
- type annotation: `tests/unit/test_enrich_planning_features.py::_validate_source_complete` via `PlanningFeatureInputValidation`.

**Exact class source**

```python
class PlanningFeatureInputValidation:
    """Immutable source-completeness evidence for normalized planning facts."""

    gpu_related_source_files_sha256: str
    expected_relations_content_sha256: str
    related_source_layer_count: int
    related_source_file_count: int
    expected_relation_count: int
```

### `_PlanningContext`

**Purpose:** Immutable result/value envelope carrying `provider`, `portal`, `commune_code`, `document_id`, `document_type`, `archive_name`, `archive_sha256`, `standard_model`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `provider` | `provider: str` | Source-provider identity carried by this configuration/result and checked against its owning source contract. |
| `portal` | `portal: str` | Source-portal identity carried by this configuration/result; it is provenance rather than physical proof by itself. |
| `commune_code` | `commune_code: str` | Canonical five-character French commune identity attached to this source/configuration context. |
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `document_type` | `document_type: str` | `_PlanningContext.document_type` represents the `document_type` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `archive_name` | `archive_name: str` | Portable physical source-archive basename retained in lineage. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `standard_model` | `standard_model: str \| None` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |

**Interface consumers**

- type annotation: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `_PlanningContext`.
- constructor call: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `_PlanningContext`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::_validate_layer_summary` via `_PlanningContext`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_PlanningContext`.
- type annotation: `src/landscout/stages/enrich_planning_features.py::_attach_parcel_summaries` via `_PlanningContext`.

**Exact class source**

```python
class _PlanningContext:
    provider: str
    portal: str
    commune_code: str
    document_id: str
    document_type: str
    archive_name: str
    archive_sha256: str
    standard_model: str | None
```


## 6. Functions and methods

### `_strict_string`

**Exact signature**

```python
def _strict_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for strict string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} must be a non-empty exact string')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_exact_strings` via `_strict_string`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_optional_exact_strings` via `_strict_string`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_standard_model` via `_strict_string`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `_strict_string`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_strict_string`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` via `_strict_string`.

**Complete source-ordered implementation**

```python
def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise PlanningFeaturesError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_nonnegative_integer`

**Exact signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Private `planning` helper for strict nonnegative integer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
int(value)
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Integral)`.
- Guard with a raise path: `value < 0`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} must be an integer count')`, `PlanningFeaturesError(f'{label} must be non-negative')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_layer_summary` via `_strict_nonnegative_integer`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_integer_values` via `_strict_nonnegative_integer`.

**Complete source-ordered implementation**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise PlanningFeaturesError(f"{label} must be an integer count")
    if value < 0:
        raise PlanningFeaturesError(f"{label} must be non-negative")
    return int(value)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_ids`

**Exact signature**

```python
def _validate_ids(values: pd.Series, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent ids; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `values.duplicated().any()`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} values must be unique')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcels` via `_validate_ids`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_source_feature_ids` via `_validate_ids`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_combine_catalogs` via `_validate_ids`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` via `_validate_ids`.

**Complete source-ordered implementation**

```python
def _validate_ids(values: pd.Series, label: str) -> None:
    _validate_exact_strings(values, label)
    if values.duplicated().any():
        raise PlanningFeaturesError(f"{label} values must be unique")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_exact_strings`

**Exact signature**

```python
def _validate_exact_strings(values: pd.Series, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent exact strings; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `values.isna().any()`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} values must not be null')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_ids` via `_validate_exact_strings`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` via `_validate_exact_strings`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_validate_exact_strings`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_result` via `_validate_exact_strings`.

**Complete source-ordered implementation**

```python
def _validate_exact_strings(values: pd.Series, label: str) -> None:
    if values.isna().any():
        raise PlanningFeaturesError(f"{label} values must not be null")
    for value in values.tolist():
        _strict_string(value, label)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_optional_exact_strings`

**Exact signature**

```python
def _validate_optional_exact_strings(values: pd.Series, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent optional exact strings; exact branches, calls, and return construction are reproduced below.

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
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_identity` via `_validate_optional_exact_strings`.

**Complete source-ordered implementation**

```python
def _validate_optional_exact_strings(values: pd.Series, label: str) -> None:
    for value in values.tolist():
        if pd.isna(value):
            continue
        _strict_string(value, label)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_crs`

**Exact signature**

```python
def _crs(value: object, label: str) -> CRS:
```

**Purpose**

Private `planning` helper for crs; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `CRS`.
- Every observed return expression is reproduced without truncation:
```python
CRS.from_user_input(value)
```

**Validation and exceptions**

- Guard with a raise path: `value is None`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} CRS is required')`, `PlanningFeaturesError(f'{label} CRS is unreadable')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcels` via `_crs`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_layer_summary` via `_crs`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_project_geometry` via `_crs`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_compare_normalized_catalog` via `_crs`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_parcel_output` via `_crs`.

**Complete source-ordered implementation**

```python
def _crs(value: object, label: str) -> CRS:
    if value is None:
        raise PlanningFeaturesError(f"{label} CRS is required")
    try:
        return CRS.from_user_input(value)
    except Exception as error:
        raise PlanningFeaturesError(f"{label} CRS is unreadable") from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_active_geometry`

**Exact signature**

```python
def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Private `planning` helper for active geometry; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `'geometry' not in frame.columns`.
- Guard with a raise path: `active != 'geometry'`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} geometry column is required')`, `PlanningFeaturesError(f'{label} geometry must be active')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcels` via `_active_geometry`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_active_geometry`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_active_geometry`.

**Complete source-ordered implementation**

```python
def _active_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    if "geometry" not in frame.columns:
        raise PlanningFeaturesError(f"{label} geometry column is required")
    try:
        active = frame.active_geometry_name
    except AttributeError as error:
        raise PlanningFeaturesError(f"{label} geometry must be active") from error
    if active != "geometry":
        raise PlanningFeaturesError(f"{label} geometry must be active")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_geometries`

**Exact signature**

```python
def _validate_geometries(
    frame: gpd.GeoDataFrame,
    allowed: frozenset[str],
    label: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent geometries; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `geometry.isna().any()`.
- Guard with a raise path: `geometry.is_empty.any()`.
- Guard with a raise path: `not geometry.is_valid.all()`.
- Guard with a raise path: `not found.issubset(allowed)`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} geometry must be valid')`, `PlanningFeaturesError(f'{label} geometry must not be empty')`, `PlanningFeaturesError(f'{label} geometry must not be null')`, `PlanningFeaturesError(f'{label} has unsupported geometry types: ' + ', '.join(sorted(found - allowed)))`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `geometry.is_empty.any`, `geometry.is_valid.all`, `geometry.isna`, `geometry.isna().any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcels` via `_validate_geometries`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_validate_geometries`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_validate_geometries`.

**Complete source-ordered implementation**

```python
def _validate_geometries(
    frame: gpd.GeoDataFrame,
    allowed: frozenset[str],
    label: str,
) -> None:
    geometry = frame.geometry
    if geometry.isna().any():
        raise PlanningFeaturesError(f"{label} geometry must not be null")
    if geometry.is_empty.any():
        raise PlanningFeaturesError(f"{label} geometry must not be empty")
    if not geometry.is_valid.all():
        raise PlanningFeaturesError(f"{label} geometry must be valid")
    found = set(geometry.geom_type)
    if not found.issubset(allowed):
        raise PlanningFeaturesError(
            f"{label} has unsupported geometry types: "
            + ", ".join(sorted(found - allowed))
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_two_dimensional_geometry`

**Exact signature**

```python
def _validate_two_dimensional_geometry(
    frame: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent two dimensional geometry; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `(dimensions != 2).any()`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} geometry dimensionality cannot be validated')`, `PlanningFeaturesError(f'{label} geometry must be canonical 2D')`, `re-raise`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_validate_two_dimensional_geometry`.

**Complete source-ordered implementation**

```python
def _validate_two_dimensional_geometry(
    frame: gpd.GeoDataFrame,
    label: str,
) -> None:
    try:
        dimensions = np.asarray(
            get_coordinate_dimension(frame.geometry.array), dtype="int64"
        )
        if (dimensions != 2).any():
            raise PlanningFeaturesError(f"{label} geometry must be canonical 2D")
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} geometry dimensionality cannot be validated"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcels`

**Exact signature**

```python
def _validate_parcels(
    parcels: gpd.GeoDataFrame,
    *,
    allow_output_columns: bool = False,
) -> CRS:
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

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `parcels.columns.duplicated().any()`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `collisions and (not allow_output_columns)`.
- Explicit raise expressions: `PlanningFeaturesError('Parcels already contain planning-feature output columns: ' + ', '.join(collisions))`, `PlanningFeaturesError('Parcels are missing required columns: ' + ', '.join(missing))`, `PlanningFeaturesError('Parcels contain duplicate columns')`, `PlanningFeaturesError('Parcels must be a GeoDataFrame')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_active_geometry`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_validate_parcels`.
- direct call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_validate_parcels`.

**Complete source-ordered implementation**

```python
def _validate_parcels(
    parcels: gpd.GeoDataFrame,
    *,
    allow_output_columns: bool = False,
) -> CRS:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise PlanningFeaturesError("Parcels must be a GeoDataFrame")
    if parcels.columns.duplicated().any():
        raise PlanningFeaturesError("Parcels contain duplicate columns")
    missing = sorted(PARCEL_REQUIRED_COLUMNS - set(parcels.columns))
    if missing:
        raise PlanningFeaturesError(
            "Parcels are missing required columns: " + ", ".join(missing)
        )
    collisions = sorted(PARCEL_OUTPUT_COLUMNS & set(parcels.columns))
    if collisions and not allow_output_columns:
        raise PlanningFeaturesError(
            "Parcels already contain planning-feature output columns: "
            + ", ".join(collisions)
        )
    _active_geometry(parcels, "Parcel")
    source_crs = _crs(parcels.crs, "Parcel")
    _validate_ids(parcels["parcel_id"], "parcel_id")
    _validate_geometries(parcels, SURFACE_TYPES, "Parcel")
    return source_crs
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_standard_model`

**Exact signature**

```python
def _standard_model(document: GpuPlanningDocument) -> str | None:
```

**Purpose**

Private `planning` helper for standard model; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
values[0] if values else None
```

**Validation and exceptions**

- Guard with a raise path: `len(values) > 1`.
- Explicit raise expressions: `PlanningFeaturesError('GPU standard-model lineage is ambiguous')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `values`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_planning_context` via `_standard_model`.

**Complete source-ordered implementation**

```python
def _standard_model(document: GpuPlanningDocument) -> str | None:
    values: list[str] = []
    model = document.extraction.archive.document.standard_model
    if model is not None:
        values.append(_strict_string(model, "GPU standard model"))
    for value in document.extraction.standard_models:
        validated = _strict_string(value, "GPU extracted standard model")
        if validated not in values:
            values.append(validated)
    if len(values) > 1:
        raise PlanningFeaturesError("GPU standard-model lineage is ambiguous")
    return values[0] if values else None
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_planning_context`

**Exact signature**

```python
def _planning_context(document: GpuPlanningDocument) -> _PlanningContext:
```

**Purpose**

Private `planning` helper for planning context; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `_PlanningContext`.
- Every observed return expression is reproduced without truncation:
```python
_PlanningContext(provider=_strict_string(metadata.provider, 'GPU provider'), portal=_strict_string(metadata.portal, 'GPU portal'), commune_code=_strict_string(metadata.commune_code, 'GPU commune code'), document_id=_strict_string(metadata.document_id, 'GPU document ID'), document_type=_strict_string(metadata.document_type, 'GPU document type'), archive_name=_strict_string(metadata.archive_name, 'GPU archive name'), archive_sha256=sha, standard_model=_standard_model(document))
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(document, GpuPlanningDocument)`.
- Guard with a raise path: `len(sha) != 64 or any((c not in '0123456789abcdefABCDEF' for c in sha))`.
- Explicit raise expressions: `PlanningFeaturesError('GPU archive SHA256 must contain 64 hex chars')`, `PlanningFeaturesError('planning_document must be a GpuPlanningDocument')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs` via `_planning_context`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_planning_context`.
- direct call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_planning_context`.

**Complete source-ordered implementation**

```python
def _planning_context(document: GpuPlanningDocument) -> _PlanningContext:
    if not isinstance(document, GpuPlanningDocument):
        raise PlanningFeaturesError("planning_document must be a GpuPlanningDocument")
    archive = document.extraction.archive
    metadata = archive.document
    sha = _strict_string(archive.sha256, "GPU archive SHA256")
    if len(sha) != 64 or any(c not in "0123456789abcdefABCDEF" for c in sha):
        raise PlanningFeaturesError("GPU archive SHA256 must contain 64 hex chars")
    return _PlanningContext(
        provider=_strict_string(metadata.provider, "GPU provider"),
        portal=_strict_string(metadata.portal, "GPU portal"),
        commune_code=_strict_string(metadata.commune_code, "GPU commune code"),
        document_id=_strict_string(metadata.document_id, "GPU document ID"),
        document_type=_strict_string(metadata.document_type, "GPU document type"),
        archive_name=_strict_string(metadata.archive_name, "GPU archive name"),
        archive_sha256=sha,
        standard_model=_standard_model(document),
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_summary_geometry_types`

**Exact signature**

```python
def _summary_geometry_types(frame: gpd.GeoDataFrame) -> tuple[tuple[str, int], ...]:
```

**Purpose**

Private `planning` helper for summary geometry types; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[tuple[str, int], ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(((str(key), int(value)) for key, value in counts.items()))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `frame.geometry.geom_type.value_counts`, `frame.geometry.geom_type.value_counts().sort_index`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_layer_summary` via `_summary_geometry_types`.

**Complete source-ordered implementation**

```python
def _summary_geometry_types(frame: gpd.GeoDataFrame) -> tuple[tuple[str, int], ...]:
    counts = frame.geometry.geom_type.value_counts().sort_index()
    return tuple((str(key), int(value)) for key, value in counts.items())
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_layer_summary`

**Exact signature**

```python
def _validate_layer_summary(
    layer: GpuInspectedLayer,
    context: _PlanningContext,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent layer summary; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `summary.source_document_id != context.document_id or summary.source_archive_sha256 != context.archive_sha256 or summary.source_layer != layer.reference.source_layer or (summary.feature_count != len(frame)) or (not actual_crs.equals(summary_crs)) or (summary.columns != tuple((str(column) for column in frame.columns))) or (summary.dtypes != expected_dtypes) or (summary.null_counts != expected_nulls) or (summary.geometry_types != _summary_geometry_types(frame)) or (summary.null_geometry_count != int((~non_null).sum())) or (summary.empty_geometry_count != int((non_null & geometry.is_empty).sum())) or (summary.invalid_geometry_count != int((non_empty & ~geometry.is_valid).sum()))`.
- Explicit raise expressions: `PlanningFeaturesError(f'{layer.logical_name} source summary is inconsistent with loaded data')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(non_empty & ~geometry.is_valid).sum`, `(non_null & geometry.is_empty).sum`, `_summary_geometry_types`, `geometry.notna`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_validate_layer_summary`.

**Complete source-ordered implementation**

```python
def _validate_layer_summary(
    layer: GpuInspectedLayer,
    context: _PlanningContext,
) -> None:
    frame = layer.data
    summary = layer.summary
    actual_crs = _crs(frame.crs, f"{layer.logical_name} source")
    summary_crs = _crs(summary.crs, f"{layer.logical_name} summary")
    expected_nulls = tuple(
        (str(column), int(frame[column].isna().sum())) for column in frame.columns
    )
    expected_dtypes = tuple(
        (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
    )
    geometry = frame.geometry
    non_null = geometry.notna()
    non_empty = non_null & ~geometry.is_empty
    _strict_nonnegative_integer(summary.feature_count, "summary feature_count")
    _strict_nonnegative_integer(
        summary.null_geometry_count, "summary null_geometry_count"
    )
    _strict_nonnegative_integer(
        summary.empty_geometry_count, "summary empty_geometry_count"
    )
    _strict_nonnegative_integer(
        summary.invalid_geometry_count, "summary invalid_geometry_count"
    )
    for column, value in summary.null_counts:
        _strict_nonnegative_integer(value, f"summary {column} null count")
    for geometry_type, value in summary.geometry_types:
        _strict_nonnegative_integer(value, f"summary {geometry_type} count")
    if (
        summary.source_document_id != context.document_id
        or summary.source_archive_sha256 != context.archive_sha256
        or summary.source_layer != layer.reference.source_layer
        or summary.feature_count != len(frame)
        or not actual_crs.equals(summary_crs)
        or summary.columns != tuple(str(column) for column in frame.columns)
        or summary.dtypes != expected_dtypes
        or summary.null_counts != expected_nulls
        or summary.geometry_types != _summary_geometry_types(frame)
        or summary.null_geometry_count != int((~non_null).sum())
        or summary.empty_geometry_count != int((non_null & geometry.is_empty).sum())
        or summary.invalid_geometry_count != int((non_empty & ~geometry.is_valid).sum())
    ):
        raise PlanningFeaturesError(
            f"{layer.logical_name} source summary is inconsistent with loaded data"
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_project_geometry`

**Exact signature**

```python
def _project_geometry(frame: gpd.GeoDataFrame, label: str) -> gpd.GeoSeries:
```

**Purpose**

Private `planning` helper for project geometry; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoSeries`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoSeries(force_2d(projected.array), crs=target)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} CRS cannot be transformed safely to EPSG:2154')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `force_2d`, `frame.geometry.copy`, `frame.to_crs`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_project_geometry`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_metric_parcels` via `_project_geometry`.

**Complete source-ordered implementation**

```python
def _project_geometry(frame: gpd.GeoDataFrame, label: str) -> gpd.GeoSeries:
    source = _crs(frame.crs, label)
    target = CRS.from_epsg(2154)
    try:
        projected = (
            frame.geometry.copy()
            if source.equals(target)
            else frame.to_crs(target).geometry
        )
        return gpd.GeoSeries(force_2d(projected.array), crs=target)
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} CRS cannot be transformed safely to EPSG:2154"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_feature_ids`

**Exact signature**

```python
def _source_feature_ids(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    validated_source: GpuValidatedSpatialLayerSource,
) -> tuple[pd.Series, SourceIdentityKind, str]:
```

**Purpose**

Private `planning` helper for source feature ids; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.Series, SourceIdentityKind, str]`.
- Every observed return expression is reproduced without truncation:
```python
(result, 'CNIG_ATTRIBUTE', spec.identity_field)

(values, 'ARCHIVE_SCOPED_OGR_FID', 'OGR_FID')

(pd.Series(dtype='object'), 'ARCHIVE_SCOPED_OGR_FID', 'OGR_FID')
```

**Validation and exceptions**

- Guard with a raise path: `spec.logical_layer == 'prescription_surface'`.
- Guard with a raise path: `len(validated_source.ogr_fids) != len(layer.data)`.
- Explicit raise expressions: `PlanningFeaturesError(f'{layer.logical_name} verified source FIDs are unavailable')`, `PlanningFeaturesError(f'{spec.logical_layer} is missing required identity field {spec.identity_field}')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_source_feature_ids`.

**Complete source-ordered implementation**

```python
def _source_feature_ids(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    validated_source: GpuValidatedSpatialLayerSource,
) -> tuple[pd.Series, SourceIdentityKind, str]:
    if spec.identity_field in layer.data.columns:
        result = layer.data[spec.identity_field].reset_index(drop=True).copy()
        _validate_ids(result, spec.identity_field)
        return result, "CNIG_ATTRIBUTE", spec.identity_field
    if spec.logical_layer == "prescription_surface":
        if layer.data.empty:
            return (
                pd.Series(dtype="object"),
                "ARCHIVE_SCOPED_OGR_FID",
                "OGR_FID",
            )
        if len(validated_source.ogr_fids) != len(layer.data):
            raise PlanningFeaturesError(
                f"{layer.logical_name} verified source FIDs are unavailable"
            )
        values = pd.Series(
            [f"OGR_FID:{value}" for value in validated_source.ogr_fids],
            dtype="object",
        )
        _validate_ids(values, f"{layer.logical_name} OGR FID")
        return values, "ARCHIVE_SCOPED_OGR_FID", "OGR_FID"
    raise PlanningFeaturesError(
        f"{spec.logical_layer} is missing required identity field {spec.identity_field}"
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_optional_values`

**Exact signature**

```python
def _optional_values(frame: gpd.GeoDataFrame, source_field: str) -> np.ndarray:
```

**Purpose**

Private `planning` helper for optional values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `np.ndarray`.
- Every observed return expression is reproduced without truncation:
```python
frame[source_field].to_numpy(copy=True)

np.full(len(frame), None, dtype='object')
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

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalize_layer` via `_optional_values`.

**Complete source-ordered implementation**

```python
def _optional_values(frame: gpd.GeoDataFrame, source_field: str) -> np.ndarray:
    if source_field not in frame.columns:
        return np.full(len(frame), None, dtype="object")
    return frame[source_field].to_numpy(copy=True)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalize_layer`

**Exact signature**

```python
def _normalize_layer(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    context: _PlanningContext,
    validated_source: GpuValidatedSpatialLayerSource,
) -> gpd.GeoDataFrame:
```

**Purpose**

Projects validated source facts into layer; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
projected
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `not frame['IDURBA'].eq(expected_reference).all()`.
- Guard with a raise path: `spec.geometry_kind == 'SURFACE'`.
- Guard with a raise path: `frame[field].isna().any()`.
- Guard with a raise path: `not np.isfinite(values).all() or (values <= 0).any()`.
- Guard with a raise path: `spec.geometry_kind == 'LINE'`.
- Guard with a raise path: `not np.isfinite(values).all() or (values <= 0).any()`.
- Explicit raise expressions: `PlanningFeaturesError(f'{spec.logical_layer} IDURBA does not match planning archive identity')`, `PlanningFeaturesError(f'{spec.logical_layer} area calculation failed')`, `PlanningFeaturesError(f'{spec.logical_layer} areas must be positive')`, `PlanningFeaturesError(f'{spec.logical_layer} is missing required source fields: ' + ', '.join(missing))`, `PlanningFeaturesError(f'{spec.logical_layer} length calculation failed')`, `PlanningFeaturesError(f'{spec.logical_layer} lengths must be positive')`, `PlanningFeaturesError(f'{spec.logical_layer} must be a GeoDataFrame')`, `PlanningFeaturesError(f'{spec.logical_layer} point-member calculation failed')`, `PlanningFeaturesError(f'{spec.logical_layer} {field} must not be null')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_active_geometry`, `_project_geometry`, `geometry.to_numpy`, `gpd.GeoDataFrame({'planning_feature_id': planning_ids.to_numpy(copy=True), 'source_feature_id': source_ids.to_numpy(copy=True), 'source_identity_kind': np.repeat(identity_kind, len(frame)), 'source_identity_field': np.repeat(identity_field, len(frame)), 'logical_layer': np.repeat(spec.logical_layer, len(frame)), 'feature_family': np.repeat(spec.feature_family, len(frame)), 'geometry_kind': np.repeat(spec.geometry_kind, len(frame)), 'type_code_raw': frame[spec.type_field].to_numpy(copy=True), 'subtype_code_raw': frame[spec.subtype_field].to_numpy(copy=True), **{normalized: _optional_values(frame, source) for normalized, source in COMMON_SOURCE_FIELDS.items()}, 'source_provider': np.repeat(context.provider, len(frame)), 'source_portal': np.repeat(context.portal, len(frame)), 'source_commune_code': np.repeat(context.commune_code, len(frame)), 'source_document_id': np.repeat(context.document_id, len(frame)), 'source_document_type': np.repeat(context.document_type, len(frame)), 'source_archive_name': np.repeat(context.archive_name, len(frame)), 'source_archive_sha256': np.repeat(context.archive_sha256, len(frame)), 'source_layer': np.repeat(layer.reference.source_layer, len(frame)), 'source_standard_model': np.full(len(frame), context.standard_model, dtype='object'), 'source_crs': np.repeat(layer.summary.crs, len(frame))}, geometry=geometry.to_numpy(copy=True), crs=CALCULATION_CRS).reset_index`, `projected.geometry.area.to_numpy`, `projected.geometry.length.to_numpy`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `projected['feature_area_m2']`, `projected['feature_length_m']`, `projected['point_member_count']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs` via `_normalize_layer`.

**Complete source-ordered implementation**

```python
def _normalize_layer(
    layer: GpuInspectedLayer,
    spec: _LayerSpec,
    context: _PlanningContext,
    validated_source: GpuValidatedSpatialLayerSource,
) -> gpd.GeoDataFrame:
    frame = layer.data
    if not isinstance(frame, gpd.GeoDataFrame):
        raise PlanningFeaturesError(f"{spec.logical_layer} must be a GeoDataFrame")
    _active_geometry(frame, spec.logical_layer)
    required = {spec.type_field, spec.subtype_field, "IDURBA", "geometry"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise PlanningFeaturesError(
            f"{spec.logical_layer} is missing required source fields: "
            + ", ".join(missing)
        )
    # Raw classification codes may repeat; validate hygiene without uniqueness.
    for field in (spec.type_field, spec.subtype_field, "IDURBA"):
        if frame[field].isna().any():
            raise PlanningFeaturesError(
                f"{spec.logical_layer} {field} must not be null"
            )
        for value in frame[field].tolist():
            _strict_string(value, f"{spec.logical_layer} {field}")
    _validate_geometries(frame, spec.allowed_geometry_types, spec.logical_layer)
    _validate_layer_summary(layer, context)
    expected_reference = (
        context.archive_name[:-4]
        if context.archive_name.casefold().endswith(".zip")
        else context.archive_name
    )
    if not frame["IDURBA"].eq(expected_reference).all():
        raise PlanningFeaturesError(
            f"{spec.logical_layer} IDURBA does not match planning archive identity"
        )

    source_ids, identity_kind, identity_field = _source_feature_ids(
        layer, spec, validated_source
    )
    planning_ids = source_ids.map(
        lambda value: f"GPU:{context.document_id}:{spec.logical_layer}:{value}"
    )
    geometry = _project_geometry(frame, spec.logical_layer)
    projected = gpd.GeoDataFrame(
        {
            "planning_feature_id": planning_ids.to_numpy(copy=True),
            "source_feature_id": source_ids.to_numpy(copy=True),
            "source_identity_kind": np.repeat(identity_kind, len(frame)),
            "source_identity_field": np.repeat(identity_field, len(frame)),
            "logical_layer": np.repeat(spec.logical_layer, len(frame)),
            "feature_family": np.repeat(spec.feature_family, len(frame)),
            "geometry_kind": np.repeat(spec.geometry_kind, len(frame)),
            "type_code_raw": frame[spec.type_field].to_numpy(copy=True),
            "subtype_code_raw": frame[spec.subtype_field].to_numpy(copy=True),
            **{
                normalized: _optional_values(frame, source)
                for normalized, source in COMMON_SOURCE_FIELDS.items()
            },
            "source_provider": np.repeat(context.provider, len(frame)),
            "source_portal": np.repeat(context.portal, len(frame)),
            "source_commune_code": np.repeat(context.commune_code, len(frame)),
            "source_document_id": np.repeat(context.document_id, len(frame)),
            "source_document_type": np.repeat(context.document_type, len(frame)),
            "source_archive_name": np.repeat(context.archive_name, len(frame)),
            "source_archive_sha256": np.repeat(context.archive_sha256, len(frame)),
            "source_layer": np.repeat(layer.reference.source_layer, len(frame)),
            "source_standard_model": np.full(
                len(frame), context.standard_model, dtype="object"
            ),
            "source_crs": np.repeat(layer.summary.crs, len(frame)),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    ).reset_index(drop=True)
    _validate_geometries(projected, spec.allowed_geometry_types, spec.logical_layer)
    if spec.geometry_kind == "SURFACE":
        try:
            values = projected.geometry.area.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} area calculation failed"
            ) from error
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(f"{spec.logical_layer} areas must be positive")
        projected["feature_area_m2"] = values
    elif spec.geometry_kind == "LINE":
        try:
            values = projected.geometry.length.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} length calculation failed"
            ) from error
        if not np.isfinite(values).all() or (values <= 0).any():
            raise PlanningFeaturesError(
                f"{spec.logical_layer} lengths must be positive"
            )
        projected["feature_length_m"] = values
    else:
        try:
            projected["point_member_count"] = [
                len(get_parts(value)) for value in projected.geometry.array
            ]
        except Exception as error:
            raise PlanningFeaturesError(
                f"{spec.logical_layer} point-member calculation failed"
            ) from error
    return projected
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_catalog_dtypes`

**Exact signature**

```python
def _canonical_catalog_dtypes(
    catalog: gpd.GeoDataFrame,
    kind: GeometryKind,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for canonical catalog dtypes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
catalog
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
- In-memory mutation: `catalog.index`, `catalog[column]`.
- Input mutation: `catalog.index`, `catalog[column]`.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_empty_catalog` via `_canonical_catalog_dtypes`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_combine_catalogs` via `_canonical_catalog_dtypes`.

**Complete source-ordered implementation**

```python
def _canonical_catalog_dtypes(
    catalog: gpd.GeoDataFrame,
    kind: GeometryKind,
) -> gpd.GeoDataFrame:
    for column, dtype in zip(
        NORMALIZED_FEATURE_COLUMNS[kind],
        normalized_feature_dtypes(kind, catalog),
        strict=True,
    ):
        if column == "geometry":
            continue
        catalog[column] = pd.Series(
            catalog[column].tolist(), index=catalog.index, dtype=dtype
        )
    catalog.index = pd.RangeIndex(len(catalog))
    return catalog
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_catalog`

**Exact signature**

```python
def _empty_catalog(kind: GeometryKind) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for empty catalog; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_catalog_dtypes(output, kind)
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
- In-memory mutation: `data[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_combine_catalogs` via `_empty_catalog`.

**Complete source-ordered implementation**

```python
def _empty_catalog(kind: GeometryKind) -> gpd.GeoDataFrame:
    data: dict[str, object] = {}
    for column, dtype in zip(
        NORMALIZED_FEATURE_COLUMNS[kind],
        NORMALIZED_FEATURE_DTYPES[kind],
        strict=True,
    ):
        data[column] = (
            gpd.GeoSeries([], crs=CALCULATION_CRS)
            if column == "geometry"
            else pd.Series(dtype=dtype)
        )
    output = gpd.GeoDataFrame(data, geometry="geometry", crs=CALCULATION_CRS)
    return _canonical_catalog_dtypes(output, kind)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_combine_catalogs`

**Exact signature**

```python
def _combine_catalogs(
    frames: list[gpd.GeoDataFrame], kind: GeometryKind
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for combine catalogs; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_catalog_dtypes(combined, kind)

_empty_catalog(kind)
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

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs.combined` via `_combine_catalogs`.

**Complete source-ordered implementation**

```python
def _combine_catalogs(
    frames: list[gpd.GeoDataFrame], kind: GeometryKind
) -> gpd.GeoDataFrame:
    if not frames:
        return _empty_catalog(kind)
    combined = gpd.GeoDataFrame(
        pd.concat(frames, ignore_index=True), geometry="geometry", crs=CALCULATION_CRS
    )
    _validate_ids(combined["planning_feature_id"], "planning_feature_id")
    return _canonical_catalog_dtypes(combined, kind)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_catalogs`

**Exact signature**

```python
def _normalized_catalogs(
    planning_document: GpuPlanningDocument,
) -> tuple[
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    tuple[GpuValidatedSpatialLayerSource, ...],
]:
```

**Purpose**

Rebuild canonical catalogs from the inspected GPU related layers only.

**Return contract**

- Declared return annotation: `tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, tuple[GpuValidatedSpatialLayerSource, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(combined('SURFACE'), combined('LINE'), combined('POINT'), validated_sources)

_combine_catalogs([normalized[logical] for logical, spec in LAYER_SPECS.items() if spec.geometry_kind == kind and logical in normalized], kind)
```

**Validation and exceptions**

- Guard with a raise path: `sum((reference == layer.reference for reference in spatial_inventory)) != 1`.
- Guard with a raise path: `logical not in LAYER_SPECS`.
- Guard with a raise path: `logical in layer_map`.
- Explicit raise expressions: `PlanningFeaturesError('Related GPU spatial sources failed physical revalidation')`, `PlanningFeaturesError(f'Duplicate related layer: {logical}')`, `PlanningFeaturesError(f'Unsupported related layer: {logical}')`, `PlanningFeaturesError(f'{layer.logical_name} inspected reference must occur exactly once in the GPU spatial-layer inventory')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `layer_map[logical]`, `normalized[logical]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_normalized_catalogs`.
- direct call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_normalized_catalogs`.

**Complete source-ordered implementation**

```python
def _normalized_catalogs(
    planning_document: GpuPlanningDocument,
) -> tuple[
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    tuple[GpuValidatedSpatialLayerSource, ...],
]:
    """Rebuild canonical catalogs from the inspected GPU related layers only."""

    context = _planning_context(planning_document)
    spatial_inventory = tuple(planning_document.all_spatial_layers)
    inspected_layers = (planning_document.zoning, *planning_document.related_layers)
    for layer in inspected_layers:
        if sum(reference == layer.reference for reference in spatial_inventory) != 1:
            raise PlanningFeaturesError(
                f"{layer.logical_name} inspected reference must occur exactly once "
                "in the GPU spatial-layer inventory"
            )
    layer_map: dict[str, GpuInspectedLayer] = {}
    for inspected_layer in planning_document.related_layers:
        logical = str(inspected_layer.logical_name)
        if logical not in LAYER_SPECS:
            raise PlanningFeaturesError(f"Unsupported related layer: {logical}")
        if logical in layer_map:
            raise PlanningFeaturesError(f"Duplicate related layer: {logical}")
        layer_map[logical] = inspected_layer

    try:
        validated_sources = revalidate_gpu_spatial_layer_sources(
            planning_document,
            tuple(
                layer_map[logical] for logical in LAYER_SPECS if logical in layer_map
            ),
        )
    except GpuSpatialInspectionError as error:
        raise PlanningFeaturesError(
            "Related GPU spatial sources failed physical revalidation"
        ) from error
    source_by_logical: dict[str, GpuValidatedSpatialLayerSource] = {
        source.logical_name: source for source in validated_sources
    }
    normalized: dict[str, gpd.GeoDataFrame] = {}
    for logical, layer in layer_map.items():
        source = source_by_logical[logical]
        fresh_layer = replace(layer, data=source.data)
        normalized[logical] = _normalize_layer(
            fresh_layer, LAYER_SPECS[logical], context, source
        )

    def combined(kind: GeometryKind) -> gpd.GeoDataFrame:
        return _combine_catalogs(
            [
                normalized[logical]
                for logical, spec in LAYER_SPECS.items()
                if spec.geometry_kind == kind and logical in normalized
            ],
            kind,
        )

    return (
        combined("SURFACE"),
        combined("LINE"),
        combined("POINT"),
        validated_sources,
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_catalogs.combined`

**Exact signature**

```python
def combined(kind: GeometryKind) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for combined; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_combine_catalogs([normalized[logical] for logical, spec in LAYER_SPECS.items() if spec.geometry_kind == kind and logical in normalized], kind)
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

- direct call: `src/landscout/stages/enrich_planning_features.py::_normalized_catalogs` via `combined`.

**Complete source-ordered implementation**

```python
def combined(kind: GeometryKind) -> gpd.GeoDataFrame:
        return _combine_catalogs(
            [
                normalized[logical]
                for logical, spec in LAYER_SPECS.items()
                if spec.geometry_kind == kind and logical in normalized
            ],
            kind,
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_metric_parcels`

**Exact signature**

```python
def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for metric parcels; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `not np.isfinite(areas).all() or (areas <= 0).any()`.
- Explicit raise expressions: `PlanningFeaturesError('Parcel metric areas must be finite and positive')`, `PlanningFeaturesError('Parcel metric-area calculation failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(areas <= 0).any`, `_project_geometry`, `geometry.to_numpy`, `np.isfinite(areas).all`, `result.geometry.area.to_numpy`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `result['_parcel_area_m2']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_metric_parcels`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `_metric_parcels`.
- direct call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_metric_parcels`.

**Complete source-ordered implementation**

```python
def _metric_parcels(parcels: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    geometry = _project_geometry(parcels, "Parcel")
    result = gpd.GeoDataFrame(
        {
            "_parcel_position": np.arange(len(parcels), dtype="int64"),
            "parcel_id": parcels["parcel_id"].to_numpy(copy=True),
        },
        geometry=geometry.to_numpy(copy=True),
        crs=CALCULATION_CRS,
    )
    try:
        areas = result.geometry.area.to_numpy(dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError("Parcel metric-area calculation failed") from error
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise PlanningFeaturesError("Parcel metric areas must be finite and positive")
    result["_parcel_area_m2"] = areas
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_relation_base`

**Exact signature**

```python
def _relation_base(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
```

**Purpose**

Private `planning` helper for relation base; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[pd.DataFrame, np.ndarray, np.ndarray]`.
- Every observed return expression is reproduced without truncation:
```python
(base, parcel_positions, feature_positions)

(pd.DataFrame(), np.array([], dtype='int64'), np.array([], dtype='int64'))

(pd.DataFrame(), np.array([], dtype='int64'), np.array([], dtype='int64'))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeaturesError('Planning-feature spatial join failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `catalog.geometry.to_numpy`, `metric['_parcel_area_m2'].to_numpy`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_surface_relations` via `_relation_base`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_line_relations` via `_relation_base`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_point_relations` via `_relation_base`.

**Complete source-ordered implementation**

```python
def _relation_base(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    if catalog.empty or metric.empty:
        return pd.DataFrame(), np.array([], dtype="int64"), np.array([], dtype="int64")
    try:
        candidates = gpd.sjoin(
            metric[["_parcel_position", "parcel_id", "geometry"]],
            gpd.GeoDataFrame(
                {"_feature_position": np.arange(len(catalog), dtype="int64")},
                geometry=catalog.geometry.to_numpy(copy=True),
                crs=CALCULATION_CRS,
            ),
            how="inner",
            predicate="intersects",
        )
    except Exception as error:
        raise PlanningFeaturesError("Planning-feature spatial join failed") from error
    if candidates.empty:
        return pd.DataFrame(), np.array([], dtype="int64"), np.array([], dtype="int64")
    parcel_positions = candidates["_parcel_position"].to_numpy(dtype="int64")
    feature_positions = candidates["_feature_position"].to_numpy(dtype="int64")
    selected = catalog.iloc[feature_positions]
    base = pd.DataFrame(
        {
            "_parcel_position": parcel_positions,
            "_feature_position": feature_positions,
            "parcel_id": metric["parcel_id"].to_numpy()[parcel_positions],
            **{
                column: selected[column].to_numpy(copy=True)
                for column in (
                    "planning_feature_id",
                    "source_feature_id",
                    "source_identity_kind",
                    "source_identity_field",
                    "logical_layer",
                    "feature_family",
                    "geometry_kind",
                    "type_code_raw",
                    "subtype_code_raw",
                    "label_raw",
                    "text_raw",
                )
            },
            "parcel_metric_area_m2": metric["_parcel_area_m2"].to_numpy()[
                parcel_positions
            ],
            "source_document_id": selected["source_document_id"].to_numpy(copy=True),
            "source_archive_sha256": selected["source_archive_sha256"].to_numpy(
                copy=True
            ),
            "source_layer": selected["source_layer"].to_numpy(copy=True),
            "source_validity_date_raw": selected["source_validity_date_raw"].to_numpy(
                copy=True
            ),
            "regulation_filename_raw": selected["regulation_filename_raw"].to_numpy(
                copy=True
            ),
        }
    )
    return base, parcel_positions, feature_positions
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_surface_relations`

**Exact signature**

```python
def _surface_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for surface relations; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
base

base
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeaturesError('Surface intersection calculation failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `catalog['feature_area_m2'].to_numpy`, `intersection`, `shapely_area`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `base['_intersection_geometry']`, `base['feature_area_m2']`, `base['feature_share_pct']`, `base['intersection_area_m2']`, `base['intersection_length_m']`, `base['parcel_share_pct']`, `base['relation_type']`, `base['source_line_length_m']`, `base[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_build_relation_tables` via `_surface_relations`.

**Complete source-ordered implementation**

```python
def _surface_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        geometries = intersection(
            metric.geometry.iloc[parcel_positions].array,
            catalog.geometry.iloc[feature_positions].array,
        )
        areas = np.asarray(shapely_area(geometries), dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError(
            "Surface intersection calculation failed"
        ) from error
    feature_areas = catalog["feature_area_m2"].to_numpy(dtype="float64")[
        feature_positions
    ]
    base["_intersection_geometry"] = list(geometries)
    base["relation_type"] = np.where(areas > 0, "AREA_OVERLAP", "TOUCH_ONLY")
    base["feature_area_m2"] = feature_areas
    base["source_line_length_m"] = np.nan
    base["intersection_area_m2"] = areas
    base["intersection_length_m"] = np.nan
    base["parcel_share_pct"] = 100.0 * areas / base["parcel_metric_area_m2"]
    base["feature_share_pct"] = 100.0 * areas / feature_areas
    for column in RELATION_COUNT_COLUMNS:
        base[column] = pd.array([pd.NA] * len(base), dtype="Int64")
    return base
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_line_relations`

**Exact signature**

```python
def _line_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for line relations; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
base

base
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeaturesError('Line intersection calculation failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `intersection`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `base['feature_area_m2']`, `base['feature_share_pct']`, `base['intersection_area_m2']`, `base['intersection_length_m']`, `base['parcel_share_pct']`, `base['relation_type']`, `base['source_line_length_m']`, `base[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_build_relation_tables` via `_line_relations`.

**Complete source-ordered implementation**

```python
def _line_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        geometries = intersection(
            metric.geometry.iloc[parcel_positions].array,
            catalog.geometry.iloc[feature_positions].array,
        )
        lengths = np.asarray(shapely_length(geometries), dtype="float64")
    except Exception as error:
        raise PlanningFeaturesError("Line intersection calculation failed") from error
    source_lengths = catalog["feature_length_m"].to_numpy(dtype="float64")[
        feature_positions
    ]
    base["relation_type"] = np.where(lengths > 0, "LENGTH_OVERLAP", "TOUCH_ONLY")
    base["feature_area_m2"] = np.nan
    base["source_line_length_m"] = source_lengths
    base["intersection_area_m2"] = np.nan
    base["intersection_length_m"] = lengths
    base["parcel_share_pct"] = np.nan
    base["feature_share_pct"] = np.nan
    for column in RELATION_COUNT_COLUMNS:
        base[column] = pd.array([pd.NA] * len(base), dtype="Int64")
    return base
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_point_relations`

**Exact signature**

```python
def _point_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for point relations; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
base

base
```

**Validation and exceptions**

- Guard with a raise path: `(inside_counts + boundary_counts <= 0).any()`.
- Explicit raise expressions: `PlanningFeaturesError('Point candidate has no covered source member')`, `PlanningFeaturesError('Point intersection calculation failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(inside_counts + boundary_counts <= 0).any`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `base['point_member_count']`, `base['point_members_boundary_count']`, `base['point_members_inside_count']`, `base['relation_type']`, `base[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_build_relation_tables` via `_point_relations`.

**Complete source-ordered implementation**

```python
def _point_relations(
    metric: gpd.GeoDataFrame,
    catalog: gpd.GeoDataFrame,
) -> pd.DataFrame:
    base, parcel_positions, feature_positions = _relation_base(metric, catalog)
    if base.empty:
        return base
    try:
        members, relation_positions = get_parts(
            catalog.geometry.iloc[feature_positions].array,
            return_index=True,
        )
        relation_positions = np.asarray(relation_positions, dtype="int64")
        member_parcels = metric.geometry.iloc[
            parcel_positions[relation_positions]
        ].array
        inside_mask = np.asarray(contains(member_parcels, members), dtype="bool")
        covered_mask = np.asarray(covers(member_parcels, members), dtype="bool")
    except Exception as error:
        raise PlanningFeaturesError("Point intersection calculation failed") from error
    member_counts = np.bincount(relation_positions, minlength=len(base))
    inside_counts = np.bincount(
        relation_positions, weights=inside_mask, minlength=len(base)
    ).astype("int64")
    covered_counts = np.bincount(
        relation_positions, weights=covered_mask, minlength=len(base)
    ).astype("int64")
    boundary_counts = covered_counts - inside_counts
    if ((inside_counts + boundary_counts) <= 0).any():
        raise PlanningFeaturesError("Point candidate has no covered source member")
    base["relation_type"] = np.where(inside_counts > 0, "INSIDE", "BOUNDARY_TOUCH")
    for column in RELATION_FLOAT_COLUMNS - {"parcel_metric_area_m2"}:
        base[column] = np.nan
    base["point_member_count"] = pd.array(member_counts, dtype="Int64")
    base["point_members_inside_count"] = pd.array(inside_counts, dtype="Int64")
    base["point_members_boundary_count"] = pd.array(boundary_counts, dtype="Int64")
    return base
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_empty_relations`

**Exact signature**

```python
def _empty_relations() -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for empty relations; its complete implementation below is the authoritative behavioral contract.

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
- In-memory mutation: `output.index`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_build_relation_tables` via `_empty_relations`.

**Complete source-ordered implementation**

```python
def _empty_relations() -> pd.DataFrame:
    output = pd.DataFrame(
        {
            column: pd.Series(
                dtype=(
                    "float64"
                    if column in RELATION_FLOAT_COLUMNS
                    else "Int64"
                    if column in RELATION_COUNT_COLUMNS
                    else "str"
                )
            )
            for column in RELATION_COLUMNS
        }
    )
    output.index = pd.RangeIndex(0)
    return output
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_relation_tables`

**Exact signature**

```python
def _build_relation_tables(
    metric: gpd.GeoDataFrame,
    surfaces: gpd.GeoDataFrame,
    lines: gpd.GeoDataFrame,
    points: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
```

**Purpose**

Constructs relation tables; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(surface_work, line_work, point_work, relations)

(surface_work, line_work, point_work, _empty_relations())
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
- In-memory mutation: `relations.index`, `relations[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_build_relation_tables`.
- direct call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_build_relation_tables`.

**Complete source-ordered implementation**

```python
def _build_relation_tables(
    metric: gpd.GeoDataFrame,
    surfaces: gpd.GeoDataFrame,
    lines: gpd.GeoDataFrame,
    points: gpd.GeoDataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    surface_work = _surface_relations(metric, surfaces)
    line_work = _line_relations(metric, lines)
    point_work = _point_relations(metric, points)
    work_frames = [
        frame for frame in (surface_work, line_work, point_work) if not frame.empty
    ]
    if not work_frames:
        return surface_work, line_work, point_work, _empty_relations()
    combined = pd.concat(work_frames, ignore_index=True)
    combined = combined.sort_values(
        ["_parcel_position", "planning_feature_id"], kind="stable"
    ).reset_index(drop=True)
    relations = combined.loc[:, RELATION_COLUMNS].copy()
    for column in RELATION_STRING_COLUMNS:
        relations[column] = relations[column].astype("str")
    for column in RELATION_COUNT_COLUMNS:
        relations[column] = pd.array(relations[column], dtype="Int64")
    relations.index = pd.RangeIndex(len(relations))
    return surface_work, line_work, point_work, relations
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_integrity_value`

**Exact signature**

```python
def _canonical_integrity_value(value: object) -> object:
```

**Purpose**

Private `planning` helper for canonical integrity value; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
value.isoformat()

_canonical_integrity_value(value.item())

None

None

value

int(value)

number

value
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, Real)`.
- Guard with a raise path: `not isfinite(number)`.
- Explicit raise expressions: `PlanningFeaturesError('Integrity payload contains non-finite numeric data')`, `PlanningFeaturesError(f'Integrity payload contains unsupported value {type(value).__name__}')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_expected_relations_content_sha256` via `_canonical_integrity_value`.

**Complete source-ordered implementation**

```python
def _canonical_integrity_value(value: object) -> object:
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_integrity_value(value.item())
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not isfinite(number):
            raise PlanningFeaturesError(
                "Integrity payload contains non-finite numeric data"
            )
        return number
    if isinstance(value, str):
        return value
    raise PlanningFeaturesError(
        f"Integrity payload contains unsupported value {type(value).__name__}"
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_integrity_sha256`

**Exact signature**

```python
def _canonical_integrity_sha256(payload: object) -> str:
```

**Purpose**

Private `planning` helper for canonical integrity sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(encoded).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeaturesError('Planning-feature integrity payload cannot be serialized')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(encoded).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_gpu_related_source_files_sha256` via `_canonical_integrity_sha256`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_expected_relations_content_sha256` via `_canonical_integrity_sha256`.

**Complete source-ordered implementation**

```python
def _canonical_integrity_sha256(payload: object) -> str:
    try:
        encoded = json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except Exception as error:
        raise PlanningFeaturesError(
            "Planning-feature integrity payload cannot be serialized"
        ) from error
    return sha256(encoded).hexdigest()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_gpu_related_source_files_sha256`

**Exact signature**

```python
def _gpu_related_source_files_sha256(
    planning_document: GpuPlanningDocument,
    sources: tuple[GpuValidatedSpatialLayerSource, ...],
) -> str:
```

**Purpose**

Private `planning` helper for gpu related source files sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_integrity_sha256({'domain': 'landscout.planning_features.verified_gpu_sources.v1', 'source_archive_sha256': planning_document.extraction.archive.sha256, 'layers': [{'logical_layer': source.logical_name, 'driver': source.driver, 'source_layer': source.source_layer, 'dataset_relative_path': source.dataset_relative_path, 'source_feature_count': source.feature_count, 'source_crs': source.source_crs, 'ogr_fids': list(source.ogr_fids), 'files': [{'relative_path': item.relative_path, 'file_type': item.file_type, 'size_bytes': item.size_bytes, 'sha256': item.sha256, 'category': item.category} for item in sorted(source.files, key=lambda value: value.relative_path)]} for source in sorted(sources, key=lambda value: value.logical_name)]})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_integrity_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_gpu_related_source_files_sha256`.

**Complete source-ordered implementation**

```python
def _gpu_related_source_files_sha256(
    planning_document: GpuPlanningDocument,
    sources: tuple[GpuValidatedSpatialLayerSource, ...],
) -> str:
    return _canonical_integrity_sha256(
        {
            "domain": "landscout.planning_features.verified_gpu_sources.v1",
            "source_archive_sha256": planning_document.extraction.archive.sha256,
            "layers": [
                {
                    "logical_layer": source.logical_name,
                    "driver": source.driver,
                    "source_layer": source.source_layer,
                    "dataset_relative_path": source.dataset_relative_path,
                    "source_feature_count": source.feature_count,
                    "source_crs": source.source_crs,
                    "ogr_fids": list(source.ogr_fids),
                    "files": [
                        {
                            "relative_path": item.relative_path,
                            "file_type": item.file_type,
                            "size_bytes": item.size_bytes,
                            "sha256": item.sha256,
                            "category": item.category,
                        }
                        for item in sorted(
                            source.files, key=lambda value: value.relative_path
                        )
                    ],
                }
                for source in sorted(sources, key=lambda value: value.logical_name)
            ],
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_expected_relations_content_sha256`

**Exact signature**

```python
def _expected_relations_content_sha256(relations: pd.DataFrame) -> str:
```

**Purpose**

Private `planning` helper for expected relations content sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_integrity_sha256({'domain': 'landscout.planning_features.expected_relations.v2', 'schema': deterministic_frame_schema_signature(relations), 'index': [_canonical_integrity_value(value) for value in relations.index.tolist()], 'rows': [[_canonical_integrity_value(value) for value in row] for row in relations.itertuples(index=False, name=None)]})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_integrity_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_expected_relations_content_sha256`.

**Complete source-ordered implementation**

```python
def _expected_relations_content_sha256(relations: pd.DataFrame) -> str:
    return _canonical_integrity_sha256(
        {
            "domain": "landscout.planning_features.expected_relations.v2",
            "schema": deterministic_frame_schema_signature(relations),
            "index": [
                _canonical_integrity_value(value) for value in relations.index.tolist()
            ],
            "rows": [
                [_canonical_integrity_value(value) for value in row]
                for row in relations.itertuples(index=False, name=None)
            ],
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_technical_tolerance`

**Exact signature**

```python
def _technical_tolerance(parcel_area: float) -> float:
```

**Purpose**

Private `planning` helper for technical tolerance; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
technical_overlay_tolerance(parcel_area)
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

- direct call: `src/landscout/stages/enrich_planning_features.py::_surface_union_summary` via `_technical_tolerance`.

**Complete source-ordered implementation**

```python
def _technical_tolerance(parcel_area: float) -> float:
    return technical_overlay_tolerance(parcel_area)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_surface_union_summary`

**Exact signature**

```python
def _surface_union_summary(
    positive: pd.DataFrame,
    parcel_areas: np.ndarray,
    count: int,
) -> np.ndarray:
```

**Purpose**

Private `planning` helper for surface union summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `np.ndarray`.
- Every observed return expression is reproduced without truncation:
```python
output

output
```

**Validation and exceptions**

- Guard with a raise path: `not isfinite(value) or value < 0`.
- Guard with a raise path: `value > area`.
- Guard with a raise path: `value - area > _technical_tolerance(area)`.
- Explicit raise expressions: `PlanningFeaturesError('Surface covered-union area exceeds parcel area')`, `PlanningFeaturesError('Surface covered-union area is invalid')`, `PlanningFeaturesError('Surface covered-union calculation failed')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `group['_intersection_geometry'].to_numpy`, `shapely_area`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output[position]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_attach_parcel_summaries` via `_surface_union_summary`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `_surface_union_summary`.

**Complete source-ordered implementation**

```python
def _surface_union_summary(
    positive: pd.DataFrame,
    parcel_areas: np.ndarray,
    count: int,
) -> np.ndarray:
    output = np.zeros(count, dtype="float64")
    if positive.empty:
        return output
    for position_value, group in positive.groupby("_parcel_position", sort=False):
        position = int(position_value)
        try:
            value = float(
                shapely_area(union_all(group["_intersection_geometry"].to_numpy()))
            )
        except Exception as error:
            raise PlanningFeaturesError(
                "Surface covered-union calculation failed"
            ) from error
        if not isfinite(value) or value < 0:
            raise PlanningFeaturesError("Surface covered-union area is invalid")
        area = float(parcel_areas[position])
        if value > area:
            if value - area > _technical_tolerance(area):
                raise PlanningFeaturesError(
                    "Surface covered-union area exceeds parcel area"
                )
            value = area
        output[position] = value
    return output
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_attach_parcel_summaries`

**Exact signature**

```python
def _attach_parcel_summaries(
    parcels: gpd.GeoDataFrame,
    metric: gpd.GeoDataFrame,
    surface_work: pd.DataFrame,
    line_work: pd.DataFrame,
    point_work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for attach parcel summaries; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output

result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `line_work.groupby('_parcel_position', sort=False)['intersection_length_m'].sum`, `metric['_parcel_area_m2'].to_numpy`, `surface_positive.groupby('_parcel_position', sort=False)['intersection_area_m2'].sum`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `line_sum[values.index.to_numpy(dtype='int64')]`, `output['planning_feature_archive_sha256']`, `output['planning_feature_document_id']`, `output['planning_line_intersection_length_sum_m']`, `output['planning_line_length_overlap_count']`, `output['planning_line_relation_count']`, `output['planning_line_touch_count']`, `output['planning_point_relation_count']`, `output['planning_surface_area_overlap_count']`, `output['planning_surface_covered_pct']`, `output['planning_surface_covered_union_area_m2']`, `output['planning_surface_intersection_area_sum_m2']`, `output['planning_surface_relation_count']`, `output['planning_surface_touch_count']`, `output[f'{prefix}_surface_covered_pct']`, `output[f'{prefix}_surface_covered_union_area_m2']`, `output[f'{prefix}_surface_relation_count']`, `output[target]`, `raw_sum[sums.index.to_numpy(dtype='int64')]`, `result[counts.index.to_numpy(dtype='int64')]`, `values[grouped.index.to_numpy(dtype='int64')]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_attach_parcel_summaries`.
- direct call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_attach_parcel_summaries`.

**Complete source-ordered implementation**

```python
def _attach_parcel_summaries(
    parcels: gpd.GeoDataFrame,
    metric: gpd.GeoDataFrame,
    surface_work: pd.DataFrame,
    line_work: pd.DataFrame,
    point_work: pd.DataFrame,
    context: _PlanningContext,
) -> gpd.GeoDataFrame:
    count = len(parcels)
    areas = metric["_parcel_area_m2"].to_numpy(dtype="float64")
    output = parcels.copy(deep=True)

    def relation_counts(
        frame: pd.DataFrame, mask: pd.Series | None = None
    ) -> np.ndarray:
        result = np.zeros(count, dtype="int64")
        selected = frame if mask is None else frame.loc[mask]
        if not selected.empty:
            counts = selected.groupby("_parcel_position", sort=False).size()
            result[counts.index.to_numpy(dtype="int64")] = counts.to_numpy(
                dtype="int64"
            )
        return result

    surface_positive = (
        surface_work.loc[surface_work["relation_type"] == "AREA_OVERLAP"]
        if not surface_work.empty
        else surface_work
    )
    surface_union = _surface_union_summary(surface_positive, areas, count)
    output["planning_surface_relation_count"] = relation_counts(surface_work)
    output["planning_surface_area_overlap_count"] = relation_counts(
        surface_work,
        surface_work["relation_type"].eq("AREA_OVERLAP")
        if not surface_work.empty
        else None,
    )
    output["planning_surface_touch_count"] = relation_counts(
        surface_work,
        surface_work["relation_type"].eq("TOUCH_ONLY")
        if not surface_work.empty
        else None,
    )
    raw_sum = np.zeros(count, dtype="float64")
    if not surface_positive.empty:
        sums = surface_positive.groupby("_parcel_position", sort=False)[
            "intersection_area_m2"
        ].sum()
        raw_sum[sums.index.to_numpy(dtype="int64")] = sums.to_numpy(dtype="float64")
    output["planning_surface_intersection_area_sum_m2"] = raw_sum
    output["planning_surface_covered_union_area_m2"] = surface_union
    output["planning_surface_covered_pct"] = np.where(
        surface_union == areas, 100.0, 100.0 * surface_union / areas
    )

    for family, prefix in (
        ("PRESCRIPTION", "prescription"),
        ("INFORMATION", "information"),
    ):
        family_work = (
            surface_work.loc[surface_work["feature_family"] == family]
            if not surface_work.empty
            else surface_work
        )
        family_positive = (
            family_work.loc[family_work["relation_type"] == "AREA_OVERLAP"]
            if not family_work.empty
            else family_work
        )
        union = _surface_union_summary(family_positive, areas, count)
        output[f"{prefix}_surface_relation_count"] = relation_counts(family_work)
        output[f"{prefix}_surface_covered_union_area_m2"] = union
        output[f"{prefix}_surface_covered_pct"] = np.where(
            union == areas, 100.0, 100.0 * union / areas
        )

    output["planning_line_relation_count"] = relation_counts(line_work)
    output["planning_line_length_overlap_count"] = relation_counts(
        line_work,
        line_work["relation_type"].eq("LENGTH_OVERLAP")
        if not line_work.empty
        else None,
    )
    output["planning_line_touch_count"] = relation_counts(
        line_work,
        line_work["relation_type"].eq("TOUCH_ONLY") if not line_work.empty else None,
    )
    line_sum = np.zeros(count, dtype="float64")
    if not line_work.empty:
        values = line_work.groupby("_parcel_position", sort=False)[
            "intersection_length_m"
        ].sum()
        line_sum[values.index.to_numpy(dtype="int64")] = values.to_numpy(
            dtype="float64"
        )
    output["planning_line_intersection_length_sum_m"] = line_sum

    output["planning_point_relation_count"] = relation_counts(point_work)
    for source, target in (
        ("point_members_inside_count", "planning_point_inside_count"),
        ("point_members_boundary_count", "planning_point_boundary_count"),
    ):
        values = np.zeros(count, dtype="int64")
        if not point_work.empty:
            grouped = point_work.groupby("_parcel_position", sort=False)[source].sum()
            values[grouped.index.to_numpy(dtype="int64")] = grouped.to_numpy(
                dtype="int64"
            )
        output[target] = values
    output["planning_feature_document_id"] = context.document_id
    output["planning_feature_archive_sha256"] = context.archive_sha256
    return output
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_attach_parcel_summaries.relation_counts`

**Exact signature**

```python
def relation_counts(
        frame: pd.DataFrame, mask: pd.Series | None = None
    ) -> np.ndarray:
```

**Purpose**

Private `planning` helper for relation counts; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `np.ndarray`.
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
- In-memory mutation: `result[counts.index.to_numpy(dtype='int64')]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_attach_parcel_summaries` via `relation_counts`.

**Complete source-ordered implementation**

```python
def relation_counts(
        frame: pd.DataFrame, mask: pd.Series | None = None
    ) -> np.ndarray:
        result = np.zeros(count, dtype="int64")
        selected = frame if mask is None else frame.loc[mask]
        if not selected.empty:
            counts = selected.groupby("_parcel_position", sort=False).size()
            result[counts.index.to_numpy(dtype="int64")] = counts.to_numpy(
                dtype="int64"
            )
        return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_numeric_values`

**Exact signature**

```python
def _numeric_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
```

**Purpose**

Private `planning` helper for numeric values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `pd.isna(value)`.
- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not isfinite(number) or number < 0`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} {column} must be finite and non-negative')`, `PlanningFeaturesError(f'{label} {column} must be finite')`, `PlanningFeaturesError(f'{label} {column} must be numeric')`, `PlanningFeaturesError(f'{label} {column} must not be null')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_numeric_values`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `_numeric_values`.

**Complete source-ordered implementation**

```python
def _numeric_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningFeaturesError(f"{label} {column} must not be null")
            if isinstance(value, bool) or not isinstance(value, Real):
                raise PlanningFeaturesError(f"{label} {column} must be numeric")
            try:
                number = float(value)
            except (TypeError, ValueError, OverflowError) as error:
                raise PlanningFeaturesError(
                    f"{label} {column} must be finite"
                ) from error
            if not isfinite(number) or number < 0:
                raise PlanningFeaturesError(
                    f"{label} {column} must be finite and non-negative"
                )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_integer_values`

**Exact signature**

```python
def _integer_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
```

**Purpose**

Private `planning` helper for integer values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `pd.isna(value)`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} {column} must not be null')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_integer_values`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `_integer_values`.

**Complete source-ordered implementation**

```python
def _integer_values(
    frame: pd.DataFrame,
    columns: set[str] | frozenset[str] | tuple[str, ...],
    label: str,
    *,
    allow_null: bool,
) -> None:
    for column in columns:
        for value in frame[column].tolist():
            if pd.isna(value):
                if allow_null:
                    continue
                raise PlanningFeaturesError(f"{label} {column} must not be null")
            _strict_nonnegative_integer(value, f"{label} {column}")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_safe_equal`

**Exact signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

**Purpose**

Private `planning` helper for null safe equal; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
False

left_null and right_null

bool(left == right)

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_relation_catalog_consistency` via `_null_safe_equal`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_relations` via `_null_safe_equal`.

**Complete source-ordered implementation**

```python
def _null_safe_equal(left: object, right: object) -> bool:
    try:
        left_missing = pd.isna(left)
        right_missing = pd.isna(right)
    except (TypeError, ValueError):
        return False
    if not isinstance(left_missing, (bool, np.bool_)) or not isinstance(
        right_missing, (bool, np.bool_)
    ):
        return False
    left_null = bool(left_missing)
    right_null = bool(right_missing)
    if left_null or right_null:
        return left_null and right_null
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_require_close`

**Exact signature**

```python
def _require_close(actual: object, expected: float, label: str) -> None:
```

**Purpose**

Private `planning` helper for require close; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `isinstance(actual, bool) or not isinstance(actual, Real)`.
- Guard with a raise path: `not isfinite(number)`.
- Guard with a raise path: `abs(number - expected) > technical_overlay_tolerance(reference)`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} is inconsistent')`, `PlanningFeaturesError(f'{label} must be finite')`, `PlanningFeaturesError(f'{label} must be numeric')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_require_close`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_relations` via `_require_close`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_parcel_output` via `_require_close`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_require_close`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `_require_close`.

**Complete source-ordered implementation**

```python
def _require_close(actual: object, expected: float, label: str) -> None:
    if isinstance(actual, bool) or not isinstance(actual, Real):
        raise PlanningFeaturesError(f"{label} must be numeric")
    try:
        number = float(actual)
    except (TypeError, ValueError, OverflowError) as error:
        raise PlanningFeaturesError(f"{label} must be finite") from error
    if not isfinite(number):
        raise PlanningFeaturesError(f"{label} must be finite")
    reference = max(abs(number), abs(expected))
    if abs(number - expected) > technical_overlay_tolerance(reference):
        raise PlanningFeaturesError(f"{label} is inconsistent")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_catalog_identity`

**Exact signature**

```python
def _validate_catalog_identity(catalog: gpd.GeoDataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent catalog identity; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `logical not in LAYER_SPECS`.
- Guard with a raise path: `row['feature_family'] != spec.feature_family`.
- Guard with a raise path: `row['geometry_kind'] != spec.geometry_kind`.
- Guard with a raise path: `row['planning_feature_id'] != expected_planning_id`.
- Guard with a raise path: `kind not in SOURCE_IDENTITY_KINDS`.
- Guard with a raise path: `kind == 'CNIG_ATTRIBUTE'`.
- Guard with a raise path: `field != spec.identity_field`.
- Guard with a raise path: `logical != 'prescription_surface' or field != 'OGR_FID' or (not str(row['source_feature_id']).startswith('OGR_FID:'))`.
- Explicit raise expressions: `PlanningFeaturesError('Archive-scoped OGR FID provenance is inconsistent')`, `PlanningFeaturesError('CNIG source identity field is inconsistent')`, `PlanningFeaturesError('Feature catalog family is inconsistent')`, `PlanningFeaturesError('Feature catalog logical layer and geometry kind are inconsistent')`, `PlanningFeaturesError('Feature catalog logical layer is invalid')`, `PlanningFeaturesError('Feature source identity kind is invalid')`, `PlanningFeaturesError('planning_feature_id differs from deterministic GPU identity')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_catalog_contract` via `_validate_catalog_identity`.

**Complete source-ordered implementation**

```python
def _validate_catalog_identity(catalog: gpd.GeoDataFrame) -> None:
    for column in _CATALOG_REQUIRED_EXACT_STRING_COLUMNS:
        _validate_exact_strings(
            catalog[column], f"Feature catalog {column.replace('_', ' ')}"
        )
    for column in _CATALOG_OPTIONAL_EXACT_STRING_COLUMNS:
        _validate_optional_exact_strings(
            catalog[column], f"Feature catalog {column.replace('_', ' ')}"
        )
    _validate_ids(catalog["planning_feature_id"], "planning_feature_id")
    for logical_layer, group in catalog.groupby("logical_layer", sort=False):
        _validate_ids(group["source_feature_id"], f"{logical_layer} source_feature_id")
    for _, row in catalog.iterrows():
        logical = _strict_string(row["logical_layer"], "logical_layer")
        if logical not in LAYER_SPECS:
            raise PlanningFeaturesError("Feature catalog logical layer is invalid")
        spec = LAYER_SPECS[logical]
        if row["feature_family"] != spec.feature_family:
            raise PlanningFeaturesError("Feature catalog family is inconsistent")
        if row["geometry_kind"] != spec.geometry_kind:
            raise PlanningFeaturesError(
                "Feature catalog logical layer and geometry kind are inconsistent"
            )
        expected_planning_id = (
            f"GPU:{row['source_document_id']}:{logical}:{row['source_feature_id']}"
        )
        if row["planning_feature_id"] != expected_planning_id:
            raise PlanningFeaturesError(
                "planning_feature_id differs from deterministic GPU identity"
            )
        kind = row["source_identity_kind"]
        field = row["source_identity_field"]
        if kind not in SOURCE_IDENTITY_KINDS:
            raise PlanningFeaturesError("Feature source identity kind is invalid")
        if kind == "CNIG_ATTRIBUTE":
            if field != spec.identity_field:
                raise PlanningFeaturesError(
                    "CNIG source identity field is inconsistent"
                )
        elif (
            logical != "prescription_surface"
            or field != "OGR_FID"
            or not str(row["source_feature_id"]).startswith("OGR_FID:")
        ):
            raise PlanningFeaturesError(
                "Archive-scoped OGR FID provenance is inconsistent"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_catalog_contract`

**Exact signature**

```python
def _validate_catalog_contract(
    catalog: object,
    geometry_kind: GeometryKind,
) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent catalog contract; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
catalog
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(catalog, gpd.GeoDataFrame)`.
- Guard with a raise path: `not catalog.empty and (not catalog['geometry_kind'].eq(geometry_kind).all())`.
- Guard with a raise path: `geometry_kind == 'SURFACE'`.
- Guard with a raise path: `(catalog['feature_area_m2'] <= 0).any()`.
- Guard with a raise path: `geometry_kind == 'LINE'`.
- Guard with a raise path: `(catalog['feature_length_m'] <= 0).any()`.
- Guard with a raise path: `(catalog['point_member_count'] < 1).any()`.
- Guard with a raise path: `catalog['point_member_count'].tolist() != member_counts`.
- Explicit raise expressions: `PlanningFeaturesError('Line feature lengths must be positive')`, `PlanningFeaturesError('Line feature metric validation failed')`, `PlanningFeaturesError('Point feature member count is inconsistent with geometry')`, `PlanningFeaturesError('Point feature member validation failed')`, `PlanningFeaturesError('Point features must contain a member')`, `PlanningFeaturesError('Surface feature areas must be positive')`, `PlanningFeaturesError('Surface feature metric validation failed')`, `PlanningFeaturesError(f'{label} geometry kind is invalid')`, `PlanningFeaturesError(f'{label} must be a GeoDataFrame')`, `PlanningFeaturesError(str(error))`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(catalog['feature_area_m2'] <= 0).any`, `_active_geometry`, `_validate_two_dimensional_geometry`, `catalog.geometry.area.to_numpy`, `catalog.geometry.length.to_numpy`, `catalog['feature_area_m2'].tolist`, `catalog['geometry_kind'].eq`, `catalog['geometry_kind'].eq(geometry_kind).all`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_validate_catalog_contract`.

**Complete source-ordered implementation**

```python
def _validate_catalog_contract(
    catalog: object,
    geometry_kind: GeometryKind,
) -> gpd.GeoDataFrame:
    label = f"{geometry_kind} feature catalog"
    if not isinstance(catalog, gpd.GeoDataFrame):
        raise PlanningFeaturesError(f"{label} must be a GeoDataFrame")
    try:
        validate_canonical_frame_schema(
            catalog,
            columns=NORMALIZED_FEATURE_COLUMNS[geometry_kind],
            dtypes=normalized_feature_dtypes(geometry_kind, catalog),
            label=label,
            geospatial=True,
            index_class="RangeIndex",
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error
    _active_geometry(catalog, label)
    _validate_catalog_identity(catalog)
    if not catalog.empty and not catalog["geometry_kind"].eq(geometry_kind).all():
        raise PlanningFeaturesError(f"{label} geometry kind is invalid")
    _validate_geometries(catalog, _CATALOG_GEOMETRY_TYPES[geometry_kind], label)
    _validate_two_dimensional_geometry(catalog, label)
    if geometry_kind == "SURFACE":
        _numeric_values(
            catalog,
            ("feature_area_m2",),
            "Surface feature",
            allow_null=False,
        )
        if (catalog["feature_area_m2"] <= 0).any():
            raise PlanningFeaturesError("Surface feature areas must be positive")
        try:
            measured = catalog.geometry.area.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                "Surface feature metric validation failed"
            ) from error
        for actual, expected in zip(
            catalog["feature_area_m2"].tolist(), measured, strict=True
        ):
            _require_close(actual, float(expected), "feature_area_m2")
    elif geometry_kind == "LINE":
        _numeric_values(
            catalog,
            ("feature_length_m",),
            "Line feature",
            allow_null=False,
        )
        if (catalog["feature_length_m"] <= 0).any():
            raise PlanningFeaturesError("Line feature lengths must be positive")
        try:
            measured = catalog.geometry.length.to_numpy(dtype="float64")
        except Exception as error:
            raise PlanningFeaturesError(
                "Line feature metric validation failed"
            ) from error
        for actual, expected in zip(
            catalog["feature_length_m"].tolist(), measured, strict=True
        ):
            _require_close(actual, float(expected), "feature_length_m")
    else:
        _integer_values(
            catalog,
            ("point_member_count",),
            "Point feature",
            allow_null=False,
        )
        if (catalog["point_member_count"] < 1).any():
            raise PlanningFeaturesError("Point features must contain a member")
        try:
            member_counts = [len(get_parts(value)) for value in catalog.geometry.array]
        except Exception as error:
            raise PlanningFeaturesError(
                "Point feature member validation failed"
            ) from error
        if catalog["point_member_count"].tolist() != member_counts:
            raise PlanningFeaturesError(
                "Point feature member count is inconsistent with geometry"
            )
    return catalog
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_normalized_catalog`

**Exact signature**

```python
def _compare_normalized_catalog(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
```

**Purpose**

Private `planning` helper for compare normalized catalog; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`.
- Guard with a raise path: `not supplied_crs.equals(expected_crs) or not geometry_equal or (not attributes_equal)`.
- Explicit raise expressions: `PlanningFeaturesError(f'{label} cannot be compared with normalized GPU source')`, `PlanningFeaturesError(f'{label} differs from normalized GPU source')`, `PlanningFeaturesError(f'{label} schema differs from normalized GPU source')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `expected.geometry.to_wkb`, `supplied.drop(columns='geometry').equals`, `supplied.geometry.to_wkb`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_compare_normalized_catalog`.

**Complete source-ordered implementation**

```python
def _compare_normalized_catalog(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
    label: str,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            f"{label} schema differs from normalized GPU source"
        )
    try:
        supplied_crs = _crs(supplied.crs, label)
        expected_crs = _crs(expected.crs, f"expected {label}")
        geometry_equal = np.array_equal(
            supplied.geometry.to_wkb(), expected.geometry.to_wkb()
        )
        attributes_equal = supplied.drop(columns="geometry").equals(
            expected.drop(columns="geometry")
        )
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            f"{label} cannot be compared with normalized GPU source"
        ) from error
    if (
        not supplied_crs.equals(expected_crs)
        or not geometry_equal
        or not attributes_equal
    ):
        raise PlanningFeaturesError(f"{label} differs from normalized GPU source")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_catalog_consistency`

**Exact signature**

```python
def _validate_relation_catalog_consistency(
    relations: pd.DataFrame,
    catalogs: tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame],
) -> None:
```

**Purpose**

Rejects malformed or inconsistent relation catalog consistency; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `feature_rows['planning_feature_id'].duplicated().any()`.
- Guard with a raise path: `identifier not in indexed.index`.
- Guard with a raise path: `metric_column is None or catalog_column is None or (not _null_safe_equal(relation[metric_column], feature[catalog_column]))`.
- Guard with a raise path: `not _null_safe_equal(relation[column], feature[column])`.
- Explicit raise expressions: `PlanningFeaturesError('Planning relation references an unknown feature')`, `PlanningFeaturesError('Relation feature metric is inconsistent with feature catalog')`, `PlanningFeaturesError('planning_feature_id values must be globally unique')`, `PlanningFeaturesError(f'Relation {column} is inconsistent with feature catalog')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `{'SURFACE': 'feature_area_m2', 'LINE': 'feature_length_m', 'POINT': 'point_member_count'}.get`, `{'SURFACE': 'feature_area_m2', 'LINE': 'source_line_length_m', 'POINT': 'point_member_count'}.get`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_validate_relation_catalog_consistency`.

**Complete source-ordered implementation**

```python
def _validate_relation_catalog_consistency(
    relations: pd.DataFrame,
    catalogs: tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame],
) -> None:
    feature_rows = pd.concat(
        [catalog.drop(columns="geometry") for catalog in catalogs],
        ignore_index=True,
    )
    if feature_rows["planning_feature_id"].duplicated().any():
        raise PlanningFeaturesError(
            "planning_feature_id values must be globally unique"
        )
    indexed = feature_rows.set_index("planning_feature_id", drop=False)
    for _, relation in relations.iterrows():
        identifier = relation["planning_feature_id"]
        if identifier not in indexed.index:
            raise PlanningFeaturesError(
                "Planning relation references an unknown feature"
            )
        feature = indexed.loc[identifier]
        for column in _RELATION_CATALOG_FIELDS:
            if not _null_safe_equal(relation[column], feature[column]):
                raise PlanningFeaturesError(
                    f"Relation {column} is inconsistent with feature catalog"
                )
        kind = relation["geometry_kind"]
        metric_column = {
            "SURFACE": "feature_area_m2",
            "LINE": "source_line_length_m",
            "POINT": "point_member_count",
        }.get(kind)
        catalog_column = {
            "SURFACE": "feature_area_m2",
            "LINE": "feature_length_m",
            "POINT": "point_member_count",
        }.get(kind)
        if (
            metric_column is None
            or catalog_column is None
            or not _null_safe_equal(relation[metric_column], feature[catalog_column])
        ):
            raise PlanningFeaturesError(
                "Relation feature metric is inconsistent with feature catalog"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_semantics`

**Exact signature**

```python
def _validate_relation_semantics(relations: pd.DataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent relation semantics; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeaturesError(str(error))`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_validate_relation_semantics`.

**Complete source-ordered implementation**

```python
def _validate_relation_semantics(relations: pd.DataFrame) -> None:
    try:
        validate_intrinsic_planning_feature_relations(relations)
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_rebuilt_relations`

**Exact signature**

```python
def _compare_rebuilt_relations(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
) -> None:
```

**Purpose**

Private `planning` helper for compare rebuilt relations; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`.
- Guard with a raise path: `not supplied.index.equals(expected.index)`.
- Guard with a raise path: `len(supplied) != len(expected)`.
- Guard with a raise path: `column in RELATION_FLOAT_COLUMNS`.
- Guard with a raise path: `actual_missing or expected_missing`.
- Guard with a raise path: `not _null_safe_equal(actual, rebuilt)`.
- Guard with a raise path: `actual_missing != expected_missing`.
- Explicit raise expressions: `PlanningFeaturesError('Planning relation count differs from the spatial reconstruction')`, `PlanningFeaturesError('Planning relation index or row order differs from the spatial reconstruction')`, `PlanningFeaturesError('Planning relation schema differs from the spatial reconstruction')`, `PlanningFeaturesError(f'{label} differs from the spatial reconstruction')`, `PlanningFeaturesError(f'{label} null pattern differs from spatial reconstruction')`.

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

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_compare_rebuilt_relations`.

**Complete source-ordered implementation**

```python
def _compare_rebuilt_relations(
    supplied: pd.DataFrame,
    expected: pd.DataFrame,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            "Planning relation schema differs from the spatial reconstruction"
        )
    if not supplied.index.equals(expected.index):
        raise PlanningFeaturesError(
            "Planning relation index or row order differs from the spatial reconstruction"
        )
    if len(supplied) != len(expected):
        raise PlanningFeaturesError(
            "Planning relation count differs from the spatial reconstruction"
        )
    for column in RELATION_COLUMNS:
        actual_values = supplied[column].tolist()
        expected_values = expected[column].tolist()
        for position, (actual, rebuilt) in enumerate(
            zip(actual_values, expected_values, strict=True)
        ):
            label = f"Planning relation {column} at row {position}"
            if column in RELATION_FLOAT_COLUMNS:
                actual_missing = bool(pd.isna(actual))
                expected_missing = bool(pd.isna(rebuilt))
                if actual_missing or expected_missing:
                    if actual_missing != expected_missing:
                        raise PlanningFeaturesError(
                            f"{label} null pattern differs from spatial reconstruction"
                        )
                    continue
                _require_close(actual, float(rebuilt), label)
            elif not _null_safe_equal(actual, rebuilt):
                raise PlanningFeaturesError(
                    f"{label} differs from the spatial reconstruction"
                )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_rebuilt_parcel_output`

**Exact signature**

```python
def _compare_rebuilt_parcel_output(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Private `planning` helper for compare rebuilt parcel output; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `deterministic_frame_schema_signature(supplied) != deterministic_frame_schema_signature(expected)`.
- Guard with a raise path: `not supplied.index.equals(expected.index)`.
- Guard with a raise path: `not _crs(supplied.crs, 'Parcel output').equals(_crs(expected.crs, 'Expected parcel output')) or not np.array_equal(supplied.geometry.to_wkb(), expected.geometry.to_wkb())`.
- Guard with a raise path: `not supplied[column].equals(expected[column])`.
- Explicit raise expressions: `PlanningFeaturesError('Planning-feature parcel geometry or CRS differs from reconstruction')`, `PlanningFeaturesError('Planning-feature parcel output index differs from reconstruction')`, `PlanningFeaturesError('Planning-feature parcel output schema differs from reconstruction')`, `PlanningFeaturesError(f'Planning-feature parcel column {column} differs from reconstruction')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `expected.geometry.to_wkb`, `supplied.geometry.to_wkb`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_compare_rebuilt_parcel_output`.

**Complete source-ordered implementation**

```python
def _compare_rebuilt_parcel_output(
    supplied: gpd.GeoDataFrame,
    expected: gpd.GeoDataFrame,
) -> None:
    if deterministic_frame_schema_signature(
        supplied
    ) != deterministic_frame_schema_signature(expected):
        raise PlanningFeaturesError(
            "Planning-feature parcel output schema differs from reconstruction"
        )
    if not supplied.index.equals(expected.index):
        raise PlanningFeaturesError(
            "Planning-feature parcel output index differs from reconstruction"
        )
    if not _crs(supplied.crs, "Parcel output").equals(
        _crs(expected.crs, "Expected parcel output")
    ) or not np.array_equal(supplied.geometry.to_wkb(), expected.geometry.to_wkb()):
        raise PlanningFeaturesError(
            "Planning-feature parcel geometry or CRS differs from reconstruction"
        )
    summary_float_columns = (
        PARCEL_OUTPUT_COLUMNS
        - PARCEL_COUNT_COLUMNS
        - {"planning_feature_document_id", "planning_feature_archive_sha256"}
    )
    for column in supplied.columns:
        if column == "geometry":
            continue
        if column in summary_float_columns:
            for position, (actual, rebuilt) in enumerate(
                zip(
                    supplied[column].tolist(),
                    expected[column].tolist(),
                    strict=True,
                )
            ):
                _require_close(
                    actual,
                    float(rebuilt),
                    f"Parcel summary {column} at row {position}",
                )
        elif not supplied[column].equals(expected[column]):
            raise PlanningFeaturesError(
                f"Planning-feature parcel column {column} differs from reconstruction"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_normalized_planning_feature_inputs`

**Exact signature**

```python
def _validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
```

**Purpose**

Validate exact STEP 7D.3.1 facts against their document and parcels.

**Return contract**

- Declared return annotation: `PlanningFeatureInputValidation`.
- Every observed return expression is reproduced without truncation:
```python
PlanningFeatureInputValidation(gpu_related_source_files_sha256=_gpu_related_source_files_sha256(planning_document, validated_sources), expected_relations_content_sha256=_expected_relations_content_sha256(expected_relations), related_source_layer_count=len(validated_sources), related_source_file_count=len(unique_files), expected_relation_count=len(expected_relations))
```

**Validation and exceptions**

- Guard with a raise path: `present_outputs and present_outputs != PARCEL_OUTPUT_COLUMNS`.
- Guard with a raise path: `len(all_feature_ids) != len(set(all_feature_ids))`.
- Guard with a raise path: `not isinstance(relations, pd.DataFrame) or isinstance(relations, gpd.GeoDataFrame)`.
- Guard with a raise path: `relations.duplicated(['parcel_id', 'planning_feature_id']).any()`.
- Guard with a raise path: `not set(relations['planning_feature_id']).issubset(set(all_feature_ids))`.
- Guard with a raise path: `present_outputs`.
- Guard with a raise path: `parcel_id not in parcel_areas`.
- Guard with a raise path: `not parcels['planning_feature_document_id'].eq(context.document_id).all()`.
- Guard with a raise path: `not parcels['planning_feature_archive_sha256'].eq(context.archive_sha256).all()`.
- Explicit raise expressions: `PlanningFeaturesError('Parcel planning-feature archive lineage differs')`, `PlanningFeaturesError('Parcel planning-feature document lineage differs')`, `PlanningFeaturesError('Parcel planning-feature summaries are incomplete: ' + ', '.join(missing))`, `PlanningFeaturesError('Parcel/planning-feature relations must be unique')`, `PlanningFeaturesError('Planning relation references an unknown feature')`, `PlanningFeaturesError('Planning relation references an unknown source parcel')`, `PlanningFeaturesError('Planning relations must be a DataFrame')`, `PlanningFeaturesError('planning_feature_id values must be globally unique')`, `PlanningFeaturesError(str(error))`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `metric_parcels['_parcel_area_m2'].tolist`, `relations[['parcel_id', 'parcel_metric_area_m2']].itertuples`.
- Hashing: `_expected_relations_content_sha256`, `_gpu_related_source_files_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::validate_normalized_planning_feature_inputs` via `_validate_normalized_planning_feature_inputs`.

**Complete source-ordered implementation**

```python
def _validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
    """Validate exact STEP 7D.3.1 facts against their document and parcels."""

    present_outputs = PARCEL_OUTPUT_COLUMNS & set(parcels.columns)
    if present_outputs and present_outputs != PARCEL_OUTPUT_COLUMNS:
        missing = sorted(PARCEL_OUTPUT_COLUMNS - present_outputs)
        raise PlanningFeaturesError(
            "Parcel planning-feature summaries are incomplete: " + ", ".join(missing)
        )
    _validate_parcels(parcels, allow_output_columns=True)
    source_parcels = (
        parcels.drop(columns=list(PARCEL_OUTPUT_COLUMNS))
        if present_outputs
        else parcels
    )
    _validate_parcels(source_parcels)
    metric_parcels = _metric_parcels(source_parcels)
    surfaces, lines, points, validated_sources = _normalized_catalogs(planning_document)
    expected_catalogs = (surfaces, lines, points)

    catalogs = (
        _validate_catalog_contract(surface_features, "SURFACE"),
        _validate_catalog_contract(line_features, "LINE"),
        _validate_catalog_contract(point_features, "POINT"),
    )
    for supplied, expected, label in zip(
        catalogs,
        expected_catalogs,
        ("SURFACE feature catalog", "LINE feature catalog", "POINT feature catalog"),
        strict=True,
    ):
        _compare_normalized_catalog(supplied, expected, label)
    all_feature_ids = [
        identifier
        for catalog in catalogs
        for identifier in catalog["planning_feature_id"].tolist()
    ]
    if len(all_feature_ids) != len(set(all_feature_ids)):
        raise PlanningFeaturesError(
            "planning_feature_id values must be globally unique"
        )

    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise PlanningFeaturesError("Planning relations must be a DataFrame")
    try:
        validate_canonical_frame_schema(
            relations,
            columns=RELATION_COLUMNS,
            dtypes=NORMALIZED_RELATION_DTYPES,
            label="Planning relations",
            geospatial=False,
            index_class="RangeIndex",
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeaturesError(str(error)) from error
    _validate_exact_strings(relations["parcel_id"], "planning relation parcel_id")
    _validate_exact_strings(
        relations["planning_feature_id"], "planning relation planning_feature_id"
    )
    if relations.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise PlanningFeaturesError("Parcel/planning-feature relations must be unique")
    if not set(relations["planning_feature_id"]).issubset(set(all_feature_ids)):
        raise PlanningFeaturesError("Planning relation references an unknown feature")
    parcel_areas = dict(
        zip(
            metric_parcels["parcel_id"].tolist(),
            metric_parcels["_parcel_area_m2"].tolist(),
            strict=True,
        )
    )
    for parcel_id, actual_area in relations[
        ["parcel_id", "parcel_metric_area_m2"]
    ].itertuples(index=False, name=None):
        if parcel_id not in parcel_areas:
            raise PlanningFeaturesError(
                "Planning relation references an unknown source parcel"
            )
        _require_close(
            actual_area,
            float(parcel_areas[parcel_id]),
            "Relation parcel metric area",
        )
    _validate_relation_semantics(relations)
    _validate_relation_catalog_consistency(relations, catalogs)
    surface_work, line_work, point_work, expected_relations = _build_relation_tables(
        metric_parcels, *expected_catalogs
    )
    _compare_rebuilt_relations(relations, expected_relations)

    if present_outputs:
        context = _planning_context(planning_document)
        expected_output = _attach_parcel_summaries(
            source_parcels,
            metric_parcels,
            surface_work,
            line_work,
            point_work,
            context,
        )
        _compare_rebuilt_parcel_output(parcels, expected_output)
        _validate_parcel_summaries(
            source_parcels, parcels, expected_relations, surface_work
        )
        if not parcels["planning_feature_document_id"].eq(context.document_id).all():
            raise PlanningFeaturesError(
                "Parcel planning-feature document lineage differs"
            )
        if (
            not parcels["planning_feature_archive_sha256"]
            .eq(context.archive_sha256)
            .all()
        ):
            raise PlanningFeaturesError(
                "Parcel planning-feature archive lineage differs"
            )

    unique_files = {
        item.relative_path for source in validated_sources for item in source.files
    }
    return PlanningFeatureInputValidation(
        gpu_related_source_files_sha256=_gpu_related_source_files_sha256(
            planning_document, validated_sources
        ),
        expected_relations_content_sha256=(
            _expected_relations_content_sha256(expected_relations)
        ),
        related_source_layer_count=len(validated_sources),
        related_source_file_count=len(unique_files),
        expected_relation_count=len(expected_relations),
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_normalized_planning_feature_inputs`

**Exact signature**

```python
def validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
```

**Purpose**

Validate exact STEP 7D.3.1 facts against their document and parcels.

**Return contract**

- Declared return annotation: `PlanningFeatureInputValidation`.
- Every observed return expression is reproduced without truncation:
```python
_validate_normalized_planning_feature_inputs(planning_document, parcels, surface_features, line_features, point_features, relations)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeaturesError('Normalized planning-feature input validation failed safely')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- import: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.stages.enrich_planning_features import (
    PlanningFeatureInputValidation,
    validate_normalized_planning_feature_inputs,
)`.
- import: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_result` via `validate_normalized_planning_feature_inputs`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `validate_normalized_planning_feature_inputs`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `validate_normalized_planning_feature_inputs`.
- direct call: `tests/unit/test_enrich_planning_features.py::_validate_source_complete` via `validate_normalized_planning_feature_inputs`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_validates_step_7d_3_1_result` via `validate_normalized_planning_feature_inputs`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_public_source_validation_hashes_survive_parquet_readback` via `validate_normalized_planning_feature_inputs`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_public_normalized_input_contract_rejects_stripped_catalog` via `validate_normalized_planning_feature_inputs`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_relation_index_class_change` via `validate_normalized_planning_feature_inputs`.

**Complete source-ordered implementation**

```python
def validate_normalized_planning_feature_inputs(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> PlanningFeatureInputValidation:
    """Validate exact STEP 7D.3.1 facts against their document and parcels."""

    try:
        return _validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
        )
    except PlanningFeaturesError:
        raise
    except Exception as error:
        raise PlanningFeaturesError(
            "Normalized planning-feature input validation failed safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcel_summaries`

**Exact signature**

```python
def _validate_parcel_summaries(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    surface_work: pd.DataFrame | None,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent parcel summaries; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `planning_union - raw_sum > technical_overlay_tolerance(raw_sum)`.
- Guard with a raise path: `planning_union - parcel_area > technical_overlay_tolerance(parcel_area)`.
- Guard with a raise path: `parcel[column] != expected`.
- Guard with a raise path: `union - planning_union > technical_overlay_tolerance(planning_union)`.
- Guard with a raise path: `abs(pct - expected_pct) > pct_tolerance`.
- Explicit raise expressions: `PlanningFeaturesError('Family surface union exceeds total union')`, `PlanningFeaturesError('Surface union exceeds parcel area')`, `PlanningFeaturesError('Surface union exceeds raw intersection sum')`, `PlanningFeaturesError(f'Parcel summary {column} is inconsistent with relations')`, `PlanningFeaturesError(f'{prefix} surface percentage is inconsistent')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `lines['intersection_length_m'].sum`, `metric['_parcel_area_m2'].to_numpy`, `metric['_parcel_area_m2'].tolist`, `points['point_members_boundary_count'].sum`, `positive_surfaces['intersection_area_m2'].sum`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` via `_validate_parcel_summaries`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_result` via `_validate_parcel_summaries`.

**Complete source-ordered implementation**

```python
def _validate_parcel_summaries(
    source: gpd.GeoDataFrame,
    output: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    surface_work: pd.DataFrame | None,
) -> None:
    metric = _metric_parcels(source)
    metric_areas = dict(
        zip(
            metric["parcel_id"].tolist(),
            metric["_parcel_area_m2"].tolist(),
            strict=True,
        )
    )
    _integer_values(output, PARCEL_COUNT_COLUMNS, "Parcel summary", allow_null=False)
    float_columns = tuple(
        PARCEL_OUTPUT_COLUMNS
        - PARCEL_COUNT_COLUMNS
        - {"planning_feature_document_id", "planning_feature_archive_sha256"}
    )
    _numeric_values(output, float_columns, "Parcel summary", allow_null=False)

    for _, parcel in output.iterrows():
        parcel_id = parcel["parcel_id"]
        rows = relations.loc[relations["parcel_id"] == parcel_id]
        surfaces = rows.loc[rows["geometry_kind"] == "SURFACE"]
        positive_surfaces = surfaces.loc[surfaces["relation_type"] == "AREA_OVERLAP"]
        lines = rows.loc[rows["geometry_kind"] == "LINE"]
        points = rows.loc[rows["geometry_kind"] == "POINT"]
        exact_counts = {
            "planning_surface_relation_count": len(surfaces),
            "planning_surface_area_overlap_count": len(positive_surfaces),
            "planning_surface_touch_count": int(
                surfaces["relation_type"].eq("TOUCH_ONLY").sum()
            ),
            "prescription_surface_relation_count": int(
                surfaces["feature_family"].eq("PRESCRIPTION").sum()
            ),
            "information_surface_relation_count": int(
                surfaces["feature_family"].eq("INFORMATION").sum()
            ),
            "planning_line_relation_count": len(lines),
            "planning_line_length_overlap_count": int(
                lines["relation_type"].eq("LENGTH_OVERLAP").sum()
            ),
            "planning_line_touch_count": int(
                lines["relation_type"].eq("TOUCH_ONLY").sum()
            ),
            "planning_point_relation_count": len(points),
            "planning_point_inside_count": int(
                points["point_members_inside_count"].sum()
            ),
            "planning_point_boundary_count": int(
                points["point_members_boundary_count"].sum()
            ),
        }
        for column, expected in exact_counts.items():
            if parcel[column] != expected:
                raise PlanningFeaturesError(
                    f"Parcel summary {column} is inconsistent with relations"
                )
        raw_sum = float(positive_surfaces["intersection_area_m2"].sum())
        line_sum = float(lines["intersection_length_m"].sum())
        _require_close(
            parcel["planning_surface_intersection_area_sum_m2"],
            raw_sum,
            "planning_surface_intersection_area_sum_m2",
        )
        _require_close(
            parcel["planning_line_intersection_length_sum_m"],
            line_sum,
            "planning_line_intersection_length_sum_m",
        )
        parcel_area = float(metric_areas[parcel_id])
        planning_union = float(parcel["planning_surface_covered_union_area_m2"])
        if planning_union - raw_sum > technical_overlay_tolerance(raw_sum):
            raise PlanningFeaturesError("Surface union exceeds raw intersection sum")
        if planning_union - parcel_area > technical_overlay_tolerance(parcel_area):
            raise PlanningFeaturesError("Surface union exceeds parcel area")
        for prefix in ("planning", "prescription", "information"):
            union = float(parcel[f"{prefix}_surface_covered_union_area_m2"])
            pct = float(parcel[f"{prefix}_surface_covered_pct"])
            if union - planning_union > technical_overlay_tolerance(planning_union):
                raise PlanningFeaturesError("Family surface union exceeds total union")
            expected_pct = (
                100.0 if union == parcel_area else 100.0 * union / parcel_area
            )
            pct_tolerance = (
                100.0 * technical_overlay_tolerance(parcel_area) / parcel_area
            )
            if abs(pct - expected_pct) > pct_tolerance:
                raise PlanningFeaturesError(
                    f"{prefix} surface percentage is inconsistent"
                )

    if surface_work is not None:
        areas = metric["_parcel_area_m2"].to_numpy(dtype="float64")
        positive = (
            surface_work.loc[surface_work["relation_type"] == "AREA_OVERLAP"]
            if not surface_work.empty
            else surface_work
        )
        expected_total = _surface_union_summary(positive, areas, len(output))
        for family, column in (
            (None, "planning_surface_covered_union_area_m2"),
            ("PRESCRIPTION", "prescription_surface_covered_union_area_m2"),
            ("INFORMATION", "information_surface_covered_union_area_m2"),
        ):
            expected_union = expected_total
            if family is not None:
                family_rows = (
                    positive.loc[positive["feature_family"] == family]
                    if not positive.empty
                    else positive
                )
                expected_union = _surface_union_summary(family_rows, areas, len(output))
            for actual, value in zip(
                output[column].tolist(), expected_union, strict=True
            ):
                _require_close(actual, float(value), column)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result`

**Exact signature**

```python
def _validate_result(
    source: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
    surface_work: pd.DataFrame | None = None,
    *,
    planning_document: GpuPlanningDocument,
    source_inputs_already_rebuilt: bool = False,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `missing_output`.
- Guard with a raise path: `len(output) != len(source)`.
- Guard with a raise path: `output['parcel_id'].tolist() != source['parcel_id'].tolist()`.
- Guard with a raise path: `not output.index.equals(source.index)`.
- Guard with a raise path: `output.crs != source.crs or not np.array_equal(output.geometry.to_wkb(), source.geometry.to_wkb())`.
- Guard with a raise path: `not set(relations['parcel_id']).issubset(set(output['parcel_id']))`.
- Guard with a raise path: `not set(relations['planning_feature_id']).issubset(known_features)`.
- Guard with a raise path: `nonempty_catalogs`.
- Guard with a raise path: `not output[column].equals(source[column])`.
- Guard with a raise path: `len(expected_document_ids) != 1 or len(expected_archive_hashes) != 1 or set(output['planning_feature_document_id']) != expected_document_ids or (set(output['planning_feature_archive_sha256']) != expected_archive_hashes)`.
- Explicit raise expressions: `PlanningFeaturesError('Parcel planning-feature lineage is inconsistent with catalogs')`, `PlanningFeaturesError('Planning relation references an unknown feature')`, `PlanningFeaturesError('Planning relation references an unknown parcel')`, `PlanningFeaturesError('Planning-feature parcel IDs or order changed')`, `PlanningFeaturesError('Planning-feature parcel count changed')`, `PlanningFeaturesError('Planning-feature parcel geometry or CRS changed')`, `PlanningFeaturesError('Planning-feature parcel index changed')`, `PlanningFeaturesError('Planning-feature parcel output is missing columns: ' + ', '.join(missing_output))`, `PlanningFeaturesError(f'Existing parcel column changed: {column}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `output.geometry.to_wkb`, `source.geometry.to_wkb`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- direct call: `src/landscout/stages/enrich_planning_features.py::intersect_parcels_with_gpu_planning_features` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_strict_relation_integer_counts_are_enforced` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_strict_parcel_summary_integer_counts_are_enforced` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_corrupted_relation_semantics_are_rejected` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_point_member_relation_semantics_are_exact` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_relation_must_match_feature_catalog` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_feature_ids_are_globally_unique_across_catalogs` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_corrupted_parcel_summary_is_rejected` via `_validate_result`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_corrupted_surface_union_contract_is_rejected` via `_validate_result`.

**Complete source-ordered implementation**

```python
def _validate_result(
    source: gpd.GeoDataFrame,
    result: ParcelPlanningFeaturesResult,
    surface_work: pd.DataFrame | None = None,
    *,
    planning_document: GpuPlanningDocument,
    source_inputs_already_rebuilt: bool = False,
) -> None:
    output = result.parcels
    missing_output = sorted(PARCEL_OUTPUT_COLUMNS - set(output.columns))
    if missing_output:
        raise PlanningFeaturesError(
            "Planning-feature parcel output is missing columns: "
            + ", ".join(missing_output)
        )
    if len(output) != len(source):
        raise PlanningFeaturesError("Planning-feature parcel count changed")
    if output["parcel_id"].tolist() != source["parcel_id"].tolist():
        raise PlanningFeaturesError("Planning-feature parcel IDs or order changed")
    if not output.index.equals(source.index):
        raise PlanningFeaturesError("Planning-feature parcel index changed")
    if output.crs != source.crs or not np.array_equal(
        output.geometry.to_wkb(), source.geometry.to_wkb()
    ):
        raise PlanningFeaturesError("Planning-feature parcel geometry or CRS changed")
    for column in source.columns:
        if column == "geometry":
            continue
        if not output[column].equals(source[column]):
            raise PlanningFeaturesError(f"Existing parcel column changed: {column}")

    catalogs = (
        result.surface_features,
        result.line_features,
        result.point_features,
    )
    if not source_inputs_already_rebuilt:
        validate_normalized_planning_feature_inputs(
            planning_document,
            source,
            *catalogs,
            result.relations,
        )
    all_feature_ids = [
        identifier
        for catalog in catalogs
        for identifier in catalog["planning_feature_id"].tolist()
    ]
    known_features = set(all_feature_ids)

    relations = result.relations
    if not set(relations["parcel_id"]).issubset(set(output["parcel_id"])):
        raise PlanningFeaturesError("Planning relation references an unknown parcel")
    if not set(relations["planning_feature_id"]).issubset(known_features):
        raise PlanningFeaturesError("Planning relation references an unknown feature")
    _validate_parcel_summaries(source, output, relations, surface_work)
    for column in (
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    ):
        _validate_exact_strings(output[column], column)
    nonempty_catalogs = [catalog for catalog in catalogs if not catalog.empty]
    if nonempty_catalogs:
        expected_document_ids = {
            value
            for catalog in nonempty_catalogs
            for value in catalog["source_document_id"].tolist()
        }
        expected_archive_hashes = {
            value
            for catalog in nonempty_catalogs
            for value in catalog["source_archive_sha256"].tolist()
        }
        if (
            len(expected_document_ids) != 1
            or len(expected_archive_hashes) != 1
            or set(output["planning_feature_document_id"]) != expected_document_ids
            or set(output["planning_feature_archive_sha256"]) != expected_archive_hashes
        ):
            raise PlanningFeaturesError(
                "Parcel planning-feature lineage is inconsistent with catalogs"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `intersect_parcels_with_gpu_planning_features`

**Exact signature**

```python
def intersect_parcels_with_gpu_planning_features(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelPlanningFeaturesResult:
```

**Purpose**

Measure factual GPU prescription/information relations to full parcels. All metric work is planar XY in EPSG:2154. Raw codes are preserved without interpretation, and every pre-existing parcel field and geometry is copied.

**Return contract**

- Declared return annotation: `ParcelPlanningFeaturesResult`.
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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- import: `tests/unit/test_enrich_planning_features.py::<module>` via `from landscout.stages.enrich_planning_features import (
    ParcelPlanningFeaturesResult,
    PlanningFeatureInputValidation,
    PlanningFeaturesError,
    _validate_result,
    intersect_parcels_with_gpu_planning_features,
    validate_normalized_planning_feature_inputs,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.enrich_planning_features import (
    RELATION_COLUMNS,
    intersect_parcels_with_gpu_planning_features,
)`.
- direct call: `tests/unit/test_enrich_planning_features.py::_run` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_mutated_source_summary_is_rejected` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_source_summary_counts_are_strict_integers` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_inputs_and_all_existing_parcel_fields_are_preserved` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::_contract_result` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::_source_complete_contract` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::_two_parcel_source_complete_contract` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_accepts_epsg4326_parcels` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_source_document_reference_allows_one_archive_zip_suffix` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::test_source_complete_contract_rejects_reordered_physical_gpkg_rows` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::_shapefile_source_complete_contract` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_enrich_planning_features.py::_shapefile_ogr_fid_source_complete_contract` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `intersect_parcels_with_gpu_planning_features`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `intersect_parcels_with_gpu_planning_features`.

**Complete source-ordered implementation**

```python
def intersect_parcels_with_gpu_planning_features(
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
) -> ParcelPlanningFeaturesResult:
    """Measure factual GPU prescription/information relations to full parcels.

    All metric work is planar XY in EPSG:2154.  Raw codes are preserved without
    interpretation, and every pre-existing parcel field and geometry is copied.
    """

    _validate_parcels(parcels)
    context = _planning_context(planning_document)
    surfaces, lines, points, _ = _normalized_catalogs(planning_document)
    metric = _metric_parcels(parcels)
    surface_work, line_work, point_work, relations = _build_relation_tables(
        metric, surfaces, lines, points
    )
    parcel_output = _attach_parcel_summaries(
        parcels, metric, surface_work, line_work, point_work, context
    )
    result = ParcelPlanningFeaturesResult(
        parcels=parcel_output,
        surface_features=surfaces,
        line_features=lines,
        point_features=points,
        relations=relations,
    )
    _validate_result(
        parcels,
        result,
        surface_work,
        planning_document=planning_document,
        source_inputs_already_rebuilt=True,
    )
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `PARCEL_REQUIRED_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
PARCEL_REQUIRED_COLUMNS = frozenset({"parcel_id", "geometry"})
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `geometry` | GeoPandas geometry dtype | nullable only where the owning geometry-status contract permits it | source/geometry fact | Active geometry; never an authorization or suitability result. |
| 2 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |

### `COMMON_SOURCE_FIELDS` — required input frame fields (unordered when stored as a set)

```python
COMMON_SOURCE_FIELDS = {
    "label_raw": "LIBELLE",
    "text_raw": "TXT",
    "regulation_filename_raw": "NOMFIC",
    "regulation_url_raw": "URLFIC",
    "source_document_reference_raw": "IDURBA",
    "source_validity_date_raw": "DATVALID",
}
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `label_raw` | LIBELLE | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `text_raw` | TXT | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `regulation_filename_raw` | NOMFIC | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `regulation_url_raw` | URLFIC | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_document_reference_raw` | IDURBA | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `source_validity_date_raw` | DATVALID | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `OPTIONAL_SOURCE_FIELDS` — required input frame fields (unordered when stored as a set)

```python
OPTIONAL_SOURCE_FIELDS = frozenset(
    {
        "LIBELLE",
        "TXT",
        "NOMFIC",
        "URLFIC",
        "DATVALID",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `DATVALID` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `LIBELLE` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `NOMFIC` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `TXT` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `URLFIC` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `_CATALOG_REQUIRED_EXACT_STRING_COLUMNS` — required input frame fields (unordered when stored as a set)

```python
_CATALOG_REQUIRED_EXACT_STRING_COLUMNS = (
    "planning_feature_id",
    "source_feature_id",
    "source_identity_kind",
    "source_identity_field",
    "logical_layer",
    "feature_family",
    "geometry_kind",
    "type_code_raw",
    "subtype_code_raw",
    "source_document_reference_raw",
    "source_provider",
    "source_portal",
    "source_commune_code",
    "source_document_id",
    "source_document_type",
    "source_archive_name",
    "source_archive_sha256",
    "source_layer",
    "source_crs",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `planning_feature_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_identity_kind` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_identity_field` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `logical_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `feature_family` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `geometry_kind` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `type_code_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `subtype_code_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `source_document_reference_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_provider` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `source_portal` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 13 | `source_commune_code` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_document_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `source_document_type` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_archive_name` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 18 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `source_crs` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS` — canonical or derived frame-column schema

```python
_CATALOG_OPTIONAL_EXACT_STRING_COLUMNS = (
    "label_raw",
    "text_raw",
    "regulation_filename_raw",
    "regulation_url_raw",
    "source_validity_date_raw",
    "source_standard_model",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `text_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `regulation_filename_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `regulation_url_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `source_validity_date_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `source_standard_model` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `PARCEL_OUTPUT_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_OUTPUT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "planning_surface_intersection_area_sum_m2",
        "planning_surface_covered_union_area_m2",
        "planning_surface_covered_pct",
        "prescription_surface_relation_count",
        "prescription_surface_covered_union_area_m2",
        "prescription_surface_covered_pct",
        "information_surface_relation_count",
        "information_surface_covered_union_area_m2",
        "information_surface_covered_pct",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_line_intersection_length_sum_m",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `information_surface_covered_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 2 | `information_surface_covered_union_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 3 | `information_surface_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 4 | `planning_feature_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 5 | `planning_feature_document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 6 | `planning_line_intersection_length_sum_m` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 7 | `planning_line_length_overlap_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 8 | `planning_line_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 9 | `planning_line_touch_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 10 | `planning_point_boundary_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 11 | `planning_point_inside_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 12 | `planning_point_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 13 | `planning_surface_area_overlap_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 14 | `planning_surface_covered_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 15 | `planning_surface_covered_union_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 16 | `planning_surface_intersection_area_sum_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 17 | `planning_surface_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 18 | `planning_surface_touch_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 19 | `prescription_surface_covered_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 20 | `prescription_surface_covered_union_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 21 | `prescription_surface_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |

### `PARCEL_COUNT_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_COUNT_COLUMNS = frozenset(
    {
        "planning_surface_relation_count",
        "planning_surface_area_overlap_count",
        "planning_surface_touch_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_line_length_overlap_count",
        "planning_line_touch_count",
        "planning_point_relation_count",
        "planning_point_inside_count",
        "planning_point_boundary_count",
    }
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `information_surface_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 2 | `planning_line_length_overlap_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 3 | `planning_line_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 4 | `planning_line_touch_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 5 | `planning_point_boundary_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 6 | `planning_point_inside_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 7 | `planning_point_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 8 | `planning_surface_area_overlap_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 9 | `planning_surface_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 10 | `planning_surface_touch_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 11 | `prescription_surface_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `ParcelPlanningFeaturesResult` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_planning_features.py`` | yes |
| `PlanningFeatureInputValidation` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_planning_features.py`` | yes |
| `PlanningFeaturesError` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_planning_features.py`` | yes |
| `intersect_parcels_with_gpu_planning_features` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_planning_features.py`` | yes |
| `validate_normalized_planning_feature_inputs` | public symbol defined in this module | `defined in `src/landscout/stages/enrich_planning_features.py`` | yes |

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

The module contributes to the planning flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
