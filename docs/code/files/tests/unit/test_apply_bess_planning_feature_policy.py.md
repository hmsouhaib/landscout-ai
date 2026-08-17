# `tests/unit/test_apply_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_apply_bess_planning_feature_policy.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.
- Source SHA256: `660b1bf74db38c3c2fc9bc78916a25e703c336888a2b2902f7f43564ea5285f8`

## 1. Purpose

Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import importlib`
- `import inspect`
- `import json`
- `from dataclasses import fields, replace`
- `from hashlib import sha256`
- `from io import BytesIO`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `from geopandas.testing import assert_geodataframe_equal`
- `from pandas.testing import assert_frame_equal`
- `from shapely import from_wkt, get_coordinate_dimension, to_wkb`
- `from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)`
- `from test_bess_planning_feature_policy import (
    _canonical_empty_policy_result,
    _checked_in_policy_result,
    _compiled_fixture,
)`
- `from test_resolve_planning_feature_codes import _canonical_empty_coded_result`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`
- `from landscout.stages.apply_bess_planning_feature_policy import (
    load_bess_planning_feature_application_artifacts as _load_application_artifacts,
)`

## 4. Contract taxonomy

### A. Python constants

#### `APPLICATION_SCOPE`

```python
APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import/re-export).

#### `POLICY_COLUMNS`

```python
POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value argument/reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` (value argument/reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` (value argument/reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import/re-export), `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` (import/re-export), `tests/unit/test_apply_bess_planning_feature_policy.py::test_policy_suffix_has_one_exact_deterministic_dtype_schema` (value argument/reference), `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_empty_optional_application_catalog_retains_schema_and_crs` (value argument/reference), `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_and_relation_inputs_are_preserved_and_not_mutated` (value argument/reference), `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_normalized_facts_rows_index_crs_and_geometry_are_preserved` (value argument/reference).

#### `BOUNDARY_FLAG_COLUMNS`

```python
BOUNDARY_FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` (value argument/reference).

#### `ARTIFACT_FILES`

```python
ARTIFACT_FILES = {
    "SURFACE_FEATURES": ("surface.parquet", True),
    "LINE_FEATURES": ("line.parquet", True),
    "POINT_FEATURES": ("point.parquet", True),
    "RELATIONS": ("relations.parquet", False),
}
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_LAST_CODED_RESULT`

```python
_LAST_CODED_RESULT: object | None = None
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_LAST_POLICY_RESULT`

```python
_LAST_POLICY_RESULT: object | None = None
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_application_fixture`

**Exact signature**

```python
def _application_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    BessPlanningFeatureApplicationResult,
]:
```

**Purpose**

Private `test` helper for application fixture; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[tuple[object, ...], object, object, object, BessPlanningFeatureApplicationResult]`.
- Every observed return expression is reproduced without truncation:
```python
(inputs, coded, config, policy, result)
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

- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_aggregation_fixture` via `_application_fixture`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `_application_fixture`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_relation` via `_application_fixture`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_surface_touch_semantic_corruption_result` via `_application_fixture`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` via `_application_fixture`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `_application_fixture`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `_application_fixture`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from test_apply_bess_planning_feature_policy import (
    _application_fixture,
    _coordinated_policy_mutation,
    _surface_touch_with_positive_area,
)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_policy_is_applied_to_every_feature_and_relation` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_output_row_has_all_six_false_boundary_flags` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_policy_suffix_has_one_exact_deterministic_dtype_schema` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_m_and_zm_application_geometries_are_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_empty_optional_application_catalog_retains_schema_and_crs` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_relations_inherit_only_from_referenced_enriched_feature` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_relation_feature_id_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_scope_has_no_parcel_output_aggregation_rejection_or_score` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_accepts_only_current_policy_and_cnig_source_schemas` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_filenames_are_casefold_unique` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_rejects_nonportable_filename` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_application_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `_application_fixture`.

**Complete source-ordered implementation**

```python
def _application_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    BessPlanningFeatureApplicationResult,
]:
    global _LAST_CODED_RESULT, _LAST_POLICY_RESULT
    inputs, coded, config, policy = _compiled_fixture()
    result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    _LAST_CODED_RESULT = coded
    _LAST_POLICY_RESULT = policy
    return inputs, coded, config, policy, result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `load_bess_planning_feature_application_artifacts`

**Exact signature**

```python
def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: object | None = None,
    policy_result: object | None = None,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Test adapter supplying the newly mandatory exact upstream envelopes.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
_load_application_artifacts(manifest_path, surface_features_path, line_features_path, point_features_path, relations_path, coded_result, policy_result)
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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- callback/property argument: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `inspect.signature(module.load_bess_planning_feature_application_artifacts)`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    load_bess_planning_feature_application_artifacts as _load_application_artifacts,
)`.

**Complete source-ordered implementation**

```python
def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: object | None = None,
    policy_result: object | None = None,
) -> BessPlanningFeatureApplicationResult:
    """Test adapter supplying the newly mandatory exact upstream envelopes."""

    if coded_result is None or policy_result is None:
        coded_result = _LAST_CODED_RESULT
        policy_result = _LAST_POLICY_RESULT
    assert coded_result is not None
    assert policy_result is not None
    return _load_application_artifacts(
        manifest_path,
        surface_features_path,
        line_features_path,
        point_features_path,
        relations_path,
        coded_result,
        policy_result,
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_small_catalog`

**Exact signature**

```python
def _small_catalog(*rows: tuple[str, str, str, str, str]) -> gpd.GeoDataFrame:
```

**Purpose**

Private `test` helper for small catalog; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
gpd.GeoDataFrame({'planning_feature_id': [row[0] for row in rows], 'feature_family': [row[1] for row in rows], 'type_code_raw': [row[2] for row in rows], 'subtype_code_raw': [row[3] for row in rows], 'official_code_status': [row[4] for row in rows]}, geometry=[Point(position, position) for position in range(len(rows))], crs='EPSG:2154')
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

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct` via `_small_catalog`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_pair_remains_present_with_true_null_decision_fields` via `_small_catalog`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_inconsistent_official_status_and_policy_match_is_rejected` via `_small_catalog`.

**Complete source-ordered implementation**

```python
def _small_catalog(*rows: tuple[str, str, str, str, str]) -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {
            "planning_feature_id": [row[0] for row in rows],
            "feature_family": [row[1] for row in rows],
            "type_code_raw": [row[2] for row in rows],
            "subtype_code_raw": [row[3] for row in rows],
            "official_code_status": [row[4] for row in rows],
        },
        geometry=[Point(position, position) for position in range(len(rows))],
        crs="EPSG:2154",
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_application_artifacts`

**Exact signature**

```python
def _write_application_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

**Purpose**

Serializes application artifacts; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[Path, dict[str, Path], dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
(manifest_path, paths, manifest)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `path.read_bytes`, `path.stat`, `sha256(path.read_bytes()).hexdigest`.
- Filesystem write: `frame.to_parquet`, `manifest_path.write_text`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(path.read_bytes()).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: `paths[role]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_filenames_are_casefold_unique` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_rejects_nonportable_filename` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_write_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `_write_application_artifacts`.

**Complete source-ordered implementation**

```python
def _write_application_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    frames = {
        "SURFACE_FEATURES": result.surface_features,
        "LINE_FEATURES": result.line_features,
        "POINT_FEATURES": result.point_features,
        "RELATIONS": result.relations,
    }
    paths: dict[str, Path] = {}
    records: list[dict[str, object]] = []
    for role, (filename, geospatial) in ARTIFACT_FILES.items():
        path = tmp_path / filename
        frame = frames[role]
        frame.to_parquet(path, index=True)
        paths[role] = path
        signature = deterministic_frame_schema_signature(frame)
        records.append(
            {
                "artifact_role": role,
                "filename": filename,
                "row_count": len(frame),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path.read_bytes()).hexdigest(),
                "frame_schema_signature": signature,
                "geospatial": geospatial,
                "crs": signature.get("crs"),
            }
        )
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeatureApplicationResult)
        if field.name
        not in {"surface_features", "line_features", "point_features", "relations"}
    )
    manifest = {
        "schema_version": 2,
        "artifact_kind": "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT",
        **{name: getattr(result, name) for name in scalar_names},
        "artifacts": records,
    }
    validated = BessPlanningFeatureApplicationArtifactManifest.model_validate(manifest)
    assert validated.schema_version == 2
    manifest_path = tmp_path / "application.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    assert module is not None
    return manifest_path, paths, manifest
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coordinated_policy_mutation`

**Exact signature**

```python
def _coordinated_policy_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: object,
    *,
    dtype: str | None = None,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Private `test` helper for coordinated policy mutation; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(replace(changed, relations=relation_frame))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame.loc[mask, column]`, `frame[column]`, `relation_frame.loc[relation_mask, column]`, `relation_frame[column]`, `relation_values[position]`, `values[position]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_coordinated_policy_mutation`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from test_apply_bess_planning_feature_policy import (
    _application_fixture,
    _coordinated_policy_mutation,
    _surface_touch_with_positive_area,
)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation` via `_coordinated_policy_mutation`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected` via `_coordinated_policy_mutation`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `_coordinated_policy_mutation`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `_coordinated_policy_mutation`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` via `_coordinated_policy_mutation`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_coordinated_policy_mutation`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_coordinated_policy_mutation`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_coordinated_policy_mutation`.

**Complete source-ordered implementation**

```python
def _coordinated_policy_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: object,
    *,
    dtype: str | None = None,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    feature_id = str(result.relations.iloc[0]["planning_feature_id"])
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            values = frame[column].tolist()
            for position, selected in enumerate(mask.tolist()):
                if selected:
                    values[position] = value
            if dtype == "category":
                frame[column] = pd.Series(pd.Categorical(values), index=frame.index)
            elif dtype is not None:
                frame[column] = pd.Series(values, index=frame.index, dtype=dtype)
            else:
                frame.loc[mask, column] = value
            changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_mask = relation_frame["planning_feature_id"].eq(feature_id)
    relation_values = relation_frame[column].tolist()
    for position, selected in enumerate(relation_mask.tolist()):
        if selected:
            relation_values[position] = value
    if dtype == "category":
        relation_frame[column] = pd.Series(
            pd.Categorical(relation_values), index=relation_frame.index
        )
    elif dtype is not None:
        relation_frame[column] = pd.Series(
            relation_values, index=relation_frame.index, dtype=dtype
        )
    else:
        relation_frame.loc[relation_mask, column] = value
    return module._result_with_hashes(replace(changed, relations=relation_frame))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coordinated_feature_id_mutation`

**Exact signature**

```python
def _coordinated_feature_id_mutation(
    result: BessPlanningFeatureApplicationResult,
    feature_id: object,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Private `test` helper for coordinated feature id mutation; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(replace(changed, relations=relations))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame.loc[frame['planning_feature_id'].eq(original), 'planning_feature_id']`, `relations.loc[relations['planning_feature_id'].eq(original), 'planning_feature_id']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable` via `_coordinated_feature_id_mutation`.

**Complete source-ordered implementation**

```python
def _coordinated_feature_id_mutation(
    result: BessPlanningFeatureApplicationResult,
    feature_id: object,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    original = result.relations.iloc[0]["planning_feature_id"]
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        frame.loc[frame["planning_feature_id"].eq(original), "planning_feature_id"] = (
            feature_id
        )
        changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    relations.loc[
        relations["planning_feature_id"].eq(original), "planning_feature_id"
    ] = feature_id
    return module._result_with_hashes(replace(changed, relations=relations))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zero_relation_feature`

**Exact signature**

```python
def _zero_relation_feature(
    result: BessPlanningFeatureApplicationResult,
) -> tuple[str, gpd.GeoDataFrame, object]:
```

**Purpose**

Private `test` helper for zero relation feature; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, gpd.GeoDataFrame, object]`.
- Every observed return expression is reproduced without truncation:
```python
(name, frame, unmatched.index[0])
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('fixture must contain a feature having zero relations')`.

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

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `_zero_relation_feature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_zero_relation_feature`.

**Complete source-ordered implementation**

```python
def _zero_relation_feature(
    result: BessPlanningFeatureApplicationResult,
) -> tuple[str, gpd.GeoDataFrame, object]:
    related = set(result.relations["planning_feature_id"])
    for name in ("surface_features", "line_features", "point_features"):
        frame = getattr(result, name)
        unmatched = frame.loc[~frame["planning_feature_id"].isin(related)]
        if not unmatched.empty:
            return name, frame, unmatched.index[0]
    raise AssertionError("fixture must contain a feature having zero relations")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_surface_touch_with_positive_area`

**Exact signature**

```python
def _surface_touch_with_positive_area(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Private `test` helper for surface touch with positive area; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(replace(result, relations=relations))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `relations['geometry_kind'].eq`.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: `relations.loc[index, 'relation_type']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_surface_touch_semantic_corruption_result` via `_surface_touch_with_positive_area`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from test_apply_bess_planning_feature_policy import (
    _application_fixture,
    _coordinated_policy_mutation,
    _surface_touch_with_positive_area,
)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_surface_touch_with_positive_area`.

**Complete source-ordered implementation**

```python
def _surface_touch_with_positive_area(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    assert relations.loc[index, "intersection_area_m2"] > 0
    relations.loc[index, "relation_type"] = "TOUCH_ONLY"
    return module._result_with_hashes(replace(result, relations=relations))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_z_geometry`

**Exact signature**

```python
def _z_geometry(kind: str) -> object:
```

**Purpose**

Private `test` helper for z geometry; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
{'Polygon': polygon, 'MultiPolygon': MultiPolygon([polygon]), 'LineString': line, 'MultiLineString': MultiLineString([line]), 'Point': point, 'MultiPoint': MultiPoint([point])}[kind]
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

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `_z_geometry`.

**Complete source-ordered implementation**

```python
def _z_geometry(kind: str) -> object:
    polygon = Polygon([(0, 0, 7), (2, 0, 7), (2, 2, 7), (0, 2, 7)])
    line = LineString([(0, 0, 7), (2, 0, 7)])
    point = Point(1, 1, 7)
    return {
        "Polygon": polygon,
        "MultiPolygon": MultiPolygon([polygon]),
        "LineString": line,
        "MultiLineString": MultiLineString([line]),
        "Point": point,
        "MultiPoint": MultiPoint([point]),
    }[kind]
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_policy_is_applied_to_every_feature_and_relation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, coded, policy_config, policy, result = _application_fixture()
lookup = policy.policy_table.set_index(
        ["feature_family", "type_code", "subtype_code"]
    )
for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        assert tuple(applied.columns[: len(source.columns)]) == tuple(source.columns)
        assert (
            applied["bess_cnig_policy_application_status"]
            .eq("APPLIED_EXACT_POLICY")
            .all()
        )
        for row in applied.itertuples(index=False):
            expected = lookup.loc[
                (row.feature_family, row.type_code_raw, row.subtype_code_raw)
            ]
            assert row.bess_cnig_precheck_status == expected.precheck_status
            assert row.bess_cnig_precheck_confidence == expected.confidence
            assert row.bess_cnig_status_priority == expected.status_priority
            assert row.bess_cnig_rationale == expected.rationale
            assert row.bess_cnig_required_human_action == (
                expected.required_human_action
            )
            assert row.bess_cnig_limitations == expected.limitations
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.result_hash_schema_version == 2
assert result.application_scope == APPLICATION_SCOPE
assert result.policy_profile == policy.policy_profile
assert result.policy_sha256 == policy.policy_sha256
assert result.policy_complete_result_content_sha256 == (
        policy.complete_result_content_sha256
    )
assert (
        result.relations["bess_cnig_policy_application_status"]
        .eq("APPLIED_EXACT_POLICY")
        .all()
    )
assert policy_config.policy_scope == result.policy_scope
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_policy_is_applied_to_every_feature_and_relation() -> None:
    _, coded, policy_config, policy, result = _application_fixture()
    assert result.result_hash_schema_version == 2
    assert result.application_scope == APPLICATION_SCOPE
    assert result.policy_profile == policy.policy_profile
    assert result.policy_sha256 == policy.policy_sha256
    assert result.policy_complete_result_content_sha256 == (
        policy.complete_result_content_sha256
    )
    lookup = policy.policy_table.set_index(
        ["feature_family", "type_code", "subtype_code"]
    )
    for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        assert tuple(applied.columns[: len(source.columns)]) == tuple(source.columns)
        assert (
            applied["bess_cnig_policy_application_status"]
            .eq("APPLIED_EXACT_POLICY")
            .all()
        )
        for row in applied.itertuples(index=False):
            expected = lookup.loc[
                (row.feature_family, row.type_code_raw, row.subtype_code_raw)
            ]
            assert row.bess_cnig_precheck_status == expected.precheck_status
            assert row.bess_cnig_precheck_confidence == expected.confidence
            assert row.bess_cnig_status_priority == expected.status_priority
            assert row.bess_cnig_rationale == expected.rationale
            assert row.bess_cnig_required_human_action == (
                expected.required_human_action
            )
            assert row.bess_cnig_limitations == expected.limitations
    assert (
        result.relations["bess_cnig_policy_application_status"]
        .eq("APPLIED_EXACT_POLICY")
        .all()
    )
    assert policy_config.policy_scope == result.policy_scope
```

### `test_every_output_row_has_all_six_false_boundary_flags`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert all(column in frame.columns for column in BOUNDARY_FLAG_COLUMNS)
        for column in BOUNDARY_FLAG_COLUMNS:
            assert str(frame[column].dtype) == "bool"
            assert frame[column].notna().all()
            assert frame[column].eq(False).all()
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

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_every_output_row_has_all_six_false_boundary_flags() -> None:
    _, _, _, _, result = _application_fixture()
    for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert all(column in frame.columns for column in BOUNDARY_FLAG_COLUMNS)
        for column in BOUNDARY_FLAG_COLUMNS:
            assert str(frame[column].dtype) == "bool"
            assert frame[column].notna().all()
            assert frame[column].eq(False).all()
```

### `test_policy_suffix_has_one_exact_deterministic_dtype_schema`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
expected = {
        column: "str"
        for column in POLICY_COLUMNS
        if column
        not in {
            "bess_cnig_status_priority",
            *BOUNDARY_FLAG_COLUMNS,
        }
    }
expected["bess_cnig_status_priority"] = "Int64"
expected.update({column: "bool" for column in BOUNDARY_FLAG_COLUMNS})
for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert tuple(frame.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert {column: str(frame[column].dtype) for column in POLICY_COLUMNS} == (
            expected
        )
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

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_suffix_has_one_exact_deterministic_dtype_schema() -> None:
    _, _, _, _, result = _application_fixture()
    expected = {
        column: "str"
        for column in POLICY_COLUMNS
        if column
        not in {
            "bess_cnig_status_priority",
            *BOUNDARY_FLAG_COLUMNS,
        }
    }
    expected["bess_cnig_status_priority"] = "Int64"
    expected.update({column: "bool" for column in BOUNDARY_FLAG_COLUMNS})
    for frame in (
        result.surface_features,
        result.line_features,
        result.point_features,
        result.relations,
    ):
        assert tuple(frame.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert {column: str(frame[column].dtype) for column in POLICY_COLUMNS} == (
            expected
        )
```

### `test_schema_v1_dimension_blind_hash_representation_is_rejected_locally`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
surface = result.surface_features.copy(deep=True)
original = surface.geometry.iloc[0]
polygon_z = Polygon([(x, y, 7) for x, y in original.exterior.coords])
surface.at[surface.index[0], surface.geometry.name] = polygon_z
blind = replace(result, surface_features=surface)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert get_coordinate_dimension(original) == 2
assert get_coordinate_dimension(polygon_z) == 3
assert to_wkb(original, hex=True, output_dimension=2) == to_wkb(
        polygon_z, hex=True, output_dimension=2
    )
assert blind.surface_features_content_sha256 == (
        result.surface_features_content_sha256
    )
assert blind.complete_result_content_sha256 == result.complete_result_content_sha256
with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(blind)
with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._result_with_hashes(blind)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_schema_v1_dimension_blind_hash_representation_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    original = surface.geometry.iloc[0]
    polygon_z = Polygon([(x, y, 7) for x, y in original.exterior.coords])
    assert get_coordinate_dimension(original) == 2
    assert get_coordinate_dimension(polygon_z) == 3
    assert to_wkb(original, hex=True, output_dimension=2) == to_wkb(
        polygon_z, hex=True, output_dimension=2
    )
    surface.at[surface.index[0], surface.geometry.name] = polygon_z
    blind = replace(result, surface_features=surface)
    assert blind.surface_features_content_sha256 == (
        result.surface_features_content_sha256
    )
    assert blind.complete_result_content_sha256 == result.complete_result_content_sha256
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(blind)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._result_with_hashes(blind)
```

### `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `frame_name`, `geometry_kind`.

**Setup**

```python
inputs, coded, config, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
frame = getattr(result, frame_name).copy(deep=True)
frame.at[frame.index[0], frame.geometry.name] = _z_geometry(geometry_kind)
changed = replace(result, **{frame_name: frame})
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
assert calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
    frame_name: str,
    geometry_kind: str,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    frame = getattr(result, frame_name).copy(deep=True)
    frame.at[frame.index[0], frame.geometry.name] = _z_geometry(geometry_kind)
    changed = replace(result, **{frame_name: frame})
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0
```

### `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation.counted`

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_m_and_zm_application_geometries_are_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `wkt`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
point = result.point_features.copy(deep=True)
point.at[point.index[0], point.geometry.name] = from_wkt(wkt)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(replace(result, point_features=point))
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_m_and_zm_application_geometries_are_rejected(wkt: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    point = result.point_features.copy(deep=True)
    point.at[point.index[0], point.geometry.name] = from_wkt(wkt)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(replace(result, point_features=point))
```

### `test_valid_empty_optional_application_catalog_retains_schema_and_crs`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, coded, _, policy, _ = _application_fixture()
empty = coded.point_features.iloc[0:0].copy()
applied = module._apply_feature_catalog(empty, policy)
module._validate_application_geometry(applied, "empty point features")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert applied.empty
assert tuple(applied.columns[: len(empty.columns)]) == tuple(empty.columns)
assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
assert applied.geometry.name == empty.geometry.name
assert applied.crs == empty.crs
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_empty_optional_application_catalog_retains_schema_and_crs() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, coded, _, policy, _ = _application_fixture()
    empty = coded.point_features.iloc[0:0].copy()
    applied = module._apply_feature_catalog(empty, policy)
    assert applied.empty
    assert tuple(applied.columns[: len(empty.columns)]) == tuple(empty.columns)
    assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
    assert applied.geometry.name == empty.geometry.name
    assert applied.crs == empty.crs
    module._validate_application_geometry(applied, "empty point features")
```

### `test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
policy = _checked_in_policy_result()
catalog = _small_catalog(
        ("F-1500", "PRESCRIPTION", "15", "00", "RESOLVED_OFFICIAL"),
        ("F-1501", "PRESCRIPTION", "15", "01", "RESOLVED_OFFICIAL"),
        ("F-NO-SUBTYPE", "PRESCRIPTION", "15", "99", "UNKNOWN_CODE_PAIR"),
        ("F-NO-FAMILY", "INFORMATION", "15", "00", "UNKNOWN_CODE_PAIR"),
        ("F-0100", "PRESCRIPTION", "01", "00", "RESOLVED_OFFICIAL"),
    )
applied = module._apply_feature_catalog(catalog, policy)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert applied.loc[0, "bess_cnig_precheck_confidence"] == "MEDIUM"
assert applied.loc[1, "bess_cnig_precheck_confidence"] == "HIGH"
assert applied.loc[0, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
assert applied.loc[1, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
assert applied.loc[2, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
assert applied.loc[3, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
assert applied.loc[4, "type_code_raw"] == "01"
assert applied.loc[4, "subtype_code_raw"] == "00"
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    policy = _checked_in_policy_result()
    catalog = _small_catalog(
        ("F-1500", "PRESCRIPTION", "15", "00", "RESOLVED_OFFICIAL"),
        ("F-1501", "PRESCRIPTION", "15", "01", "RESOLVED_OFFICIAL"),
        ("F-NO-SUBTYPE", "PRESCRIPTION", "15", "99", "UNKNOWN_CODE_PAIR"),
        ("F-NO-FAMILY", "INFORMATION", "15", "00", "UNKNOWN_CODE_PAIR"),
        ("F-0100", "PRESCRIPTION", "01", "00", "RESOLVED_OFFICIAL"),
    )
    applied = module._apply_feature_catalog(catalog, policy)
    assert applied.loc[0, "bess_cnig_precheck_confidence"] == "MEDIUM"
    assert applied.loc[1, "bess_cnig_precheck_confidence"] == "HIGH"
    assert applied.loc[0, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
    assert applied.loc[1, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"
    assert applied.loc[2, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    assert applied.loc[3, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    assert applied.loc[4, "type_code_raw"] == "01"
    assert applied.loc[4, "subtype_code_raw"] == "00"
```

### `test_unknown_pair_remains_present_with_true_null_decision_fields`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
policy = _checked_in_policy_result()
catalog = _small_catalog(
        ("F-UNKNOWN", "PRESCRIPTION", "98", "00", "UNKNOWN_CODE_PAIR"),
    )
applied = module._apply_feature_catalog(catalog, policy)
for column in POLICY_COLUMNS[1:7]:
        assert pd.isna(applied.loc[0, column])
        assert not isinstance(applied.loc[0, column], str)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert applied["planning_feature_id"].tolist() == ["F-UNKNOWN"]
assert applied.loc[0, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_pair_remains_present_with_true_null_decision_fields() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    policy = _checked_in_policy_result()
    catalog = _small_catalog(
        ("F-UNKNOWN", "PRESCRIPTION", "98", "00", "UNKNOWN_CODE_PAIR"),
    )
    applied = module._apply_feature_catalog(catalog, policy)
    assert applied["planning_feature_id"].tolist() == ["F-UNKNOWN"]
    assert applied.loc[0, "bess_cnig_policy_application_status"] == (
        "UNRESOLVED_CODE_PAIR"
    )
    for column in POLICY_COLUMNS[1:7]:
        assert pd.isna(applied.loc[0, column])
        assert not isinstance(applied.loc[0, column], str)
```

### `test_inconsistent_official_status_and_policy_match_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `row`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="policy|official"):
        module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy|official"):
        module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())
```

### `test_feature_and_relation_inputs_are_preserved_and_not_mutated`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy = _compiled_fixture()
coded_copies = (
        coded.surface_features.copy(deep=True),
        coded.line_features.copy(deep=True),
        coded.point_features.copy(deep=True),
        coded.relations.copy(deep=True),
    )
parcels_copy = inputs[1].copy(deep=True)
assert_geodataframe_equal(coded_copies[0], coded.surface_features)
assert_geodataframe_equal(coded_copies[1], coded.line_features)
assert_geodataframe_equal(coded_copies[2], coded.point_features)
assert_frame_equal(coded_copies[3], coded.relations)
assert_geodataframe_equal(parcels_copy, inputs[1])
for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        prefix = applied.loc[:, source.columns]
        assert_geodataframe_equal(source, prefix, check_dtype=True, check_crs=True)
        assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert type(applied.index) is type(source.index)
        assert applied.index.equals(source.index)
relation_prefix = result.relations.loc[:, coded.relations.columns]
assert_frame_equal(coded.relations, relation_prefix, check_dtype=True)
```

**Action**

```python
result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
```

**Expected result**

```python
assert tuple(result.relations.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_feature_and_relation_inputs_are_preserved_and_not_mutated() -> None:
    inputs, coded, config, policy = _compiled_fixture()
    coded_copies = (
        coded.surface_features.copy(deep=True),
        coded.line_features.copy(deep=True),
        coded.point_features.copy(deep=True),
        coded.relations.copy(deep=True),
    )
    parcels_copy = inputs[1].copy(deep=True)
    result = apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    assert_geodataframe_equal(coded_copies[0], coded.surface_features)
    assert_geodataframe_equal(coded_copies[1], coded.line_features)
    assert_geodataframe_equal(coded_copies[2], coded.point_features)
    assert_frame_equal(coded_copies[3], coded.relations)
    assert_geodataframe_equal(parcels_copy, inputs[1])
    for source, applied in (
        (coded.surface_features, result.surface_features),
        (coded.line_features, result.line_features),
        (coded.point_features, result.point_features),
    ):
        prefix = applied.loc[:, source.columns]
        assert_geodataframe_equal(source, prefix, check_dtype=True, check_crs=True)
        assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
        assert type(applied.index) is type(source.index)
        assert applied.index.equals(source.index)
    relation_prefix = result.relations.loc[:, coded.relations.columns]
    assert_frame_equal(coded.relations, relation_prefix, check_dtype=True)
    assert tuple(result.relations.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS
```

### `test_relations_inherit_only_from_referenced_enriched_feature`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
features = pd.concat(
        [
            result.surface_features.drop(columns="geometry"),
            result.line_features.drop(columns="geometry"),
            result.point_features.drop(columns="geometry"),
        ],
        ignore_index=True,
    ).set_index("planning_feature_id")
for relation in result.relations.itertuples(index=False):
        feature = features.loc[relation.planning_feature_id]
        for column in POLICY_COLUMNS:
            assert getattr(relation, column) == feature[column]
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

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_relations_inherit_only_from_referenced_enriched_feature() -> None:
    _, _, _, _, result = _application_fixture()
    features = pd.concat(
        [
            result.surface_features.drop(columns="geometry"),
            result.line_features.drop(columns="geometry"),
            result.point_features.drop(columns="geometry"),
        ],
        ignore_index=True,
    ).set_index("planning_feature_id")
    for relation in result.relations.itertuples(index=False):
        feature = features.loc[relation.planning_feature_id]
        for column in POLICY_COLUMNS:
            assert getattr(relation, column) == feature[column]
```

### `test_complete_relation_facts_must_match_referenced_feature`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
relations = result.relations.copy(deep=True)
index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
relations.loc[index, column] = value
changed = module._result_with_hashes(replace(result, relations=relations))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="relation|feature"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_complete_relation_facts_must_match_referenced_feature(
    column: str, value: object
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq("SURFACE")][0]
    relations.loc[index, column] = value
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation|feature"):
        module._validate_result_envelope(changed)
```

### `test_unknown_relation_feature_id_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, coded, _, policy, result = _application_fixture()
relations = coded.relations.copy(deep=True)
relations.loc[relations.index[0], "planning_feature_id"] = "GPU:UNKNOWN"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="feature ID"):
        module._apply_relations(
            relations,
            result.surface_features,
            result.line_features,
            result.point_features,
        )
assert policy is not None
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, coded, _, policy, result = _application_fixture()
    relations = coded.relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "GPU:UNKNOWN"
    with pytest.raises(BessPlanningFeatureApplicationError, match="feature ID"):
        module._apply_relations(
            relations,
            result.surface_features,
            result.line_features,
            result.point_features,
        )
    assert policy is not None
```

### `test_scope_has_no_parcel_output_aggregation_rejection_or_score`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, _, _, _, result = _application_fixture()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert not hasattr(result, "parcels")
assert result.local_feature_text_interpreted is False
assert result.local_regulation_content_interpreted is False
assert result.legal_conclusion_produced is False
assert result.parcel_status_aggregated is False
assert result.parcel_rejection_performed is False
assert result.score_calculated is False
assert "parcel_id" not in result.surface_features.columns
assert len(inputs[1]) > 0
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_scope_has_no_parcel_output_aggregation_rejection_or_score() -> None:
    inputs, _, _, _, result = _application_fixture()
    assert not hasattr(result, "parcels")
    assert result.local_feature_text_interpreted is False
    assert result.local_regulation_content_interpreted is False
    assert result.legal_conclusion_produced is False
    assert result.parcel_status_aggregated is False
    assert result.parcel_rejection_performed is False
    assert result.score_calculated is False
    assert "parcel_id" not in result.surface_features.columns
    assert len(inputs[1]) > 0
```

### `test_coordinated_feature_or_relation_policy_mutation_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
surface = result.surface_features.copy(deep=True)
surface.loc[surface.index[0], "bess_cnig_precheck_status"] = "UNKNOWN"
coordinated = module._result_with_hashes(replace(result, surface_features=surface))
relations = result.relations.copy(deep=True)
relations.loc[relations.index[0], "bess_cnig_precheck_confidence"] = "LOW"
coordinated = module._result_with_hashes(replace(result, relations=relations))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="rebuilt|feature"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )
with pytest.raises(BessPlanningFeatureApplicationError, match="relation|rebuilt"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_feature_or_relation_policy_mutation_is_rejected() -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "bess_cnig_precheck_status"] = "UNKNOWN"
    coordinated = module._result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(BessPlanningFeatureApplicationError, match="rebuilt|feature"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "bess_cnig_precheck_confidence"] = "LOW"
    coordinated = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation|rebuilt"):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, coordinated
        )
```

### `test_duplicate_application_relation_pair_is_rejected_locally`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
relations = pd.concat([result.relations, result.relations.iloc[[0]]])
changed = module._result_with_hashes(replace(result, relations=relations))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_application_relation_pair_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = pd.concat([result.relations, result.relations.iloc[[0]]])
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module._validate_result_envelope(changed)
```

### `test_application_relation_feature_id_is_exact_and_portable`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `feature_id`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = _coordinated_feature_id_mutation(result, feature_id)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="feature|identity"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_relation_feature_id_is_exact_and_portable(
    feature_id: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_feature_id_mutation(result, feature_id)
    with pytest.raises(BessPlanningFeatureApplicationError, match="feature|identity"):
        module._validate_result_envelope(changed)
```

### `test_application_relation_parcel_id_is_exact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `parcel_id`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
relations = result.relations.copy(deep=True)
relations.loc[relations.index[0], "parcel_id"] = parcel_id
changed = module._result_with_hashes(replace(result, relations=relations))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="parcel|identity"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_relation_parcel_id_is_exact(parcel_id: object) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "parcel_id"] = parcel_id
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="parcel|identity"):
        module._validate_result_envelope(changed)
```

### `test_unknown_application_relation_type_is_rejected_locally`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
relations = result.relations.copy(deep=True)
relations.loc[relations.index[0], "relation_type"] = "BUFFERED_NEARBY"
changed = module._result_with_hashes(replace(result, relations=relations))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="relation type"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_application_relation_type_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "relation_type"] = "BUFFERED_NEARBY"
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="relation type"):
        module._validate_result_envelope(changed)
```

### `test_coordinated_invalid_policy_domains_fail_local_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `message`, `value`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = _coordinated_policy_mutation(result, column, value)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_invalid_policy_domains_fail_local_validation(
    column: str,
    value: object,
    message: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, value)
    with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        module._validate_result_envelope(changed)
```

### `test_literal_null_replacements_are_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `literal`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = _coordinated_policy_mutation(result, "bess_cnig_rationale", literal)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="literal|missing"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_literal_null_replacements_are_rejected(literal: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, "bess_cnig_rationale", literal)
    with pytest.raises(BessPlanningFeatureApplicationError, match="literal|missing"):
        module._validate_result_envelope(changed)
```

### `test_self_consistent_wrong_policy_suffix_dtype_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `dtype`, `value`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = _coordinated_policy_mutation(result, column, value, dtype=dtype)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_self_consistent_wrong_policy_suffix_dtype_is_rejected(
    column: str,
    dtype: str,
    value: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, value, dtype=dtype)
    with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        module._validate_result_envelope(changed)
```

### `test_official_and_application_statuses_cannot_contradict`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `application_status`, `official_status`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_policy_application_status",
        application_status,
    )
feature_id = str(changed.relations.iloc[0]["planning_feature_id"])
for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            frame.loc[mask, "official_code_status"] = official_status
            changed = replace(changed, **{frame_name: frame})
relation_frame = changed.relations.copy(deep=True)
relation_frame.loc[
        relation_frame["planning_feature_id"].eq(feature_id), "official_code_status"
    ] = official_status
changed = module._result_with_hashes(replace(changed, relations=relation_frame))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="official|status"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_official_and_application_statuses_cannot_contradict(
    official_status: str,
    application_status: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_policy_application_status",
        application_status,
    )
    feature_id = str(changed.relations.iloc[0]["planning_feature_id"])
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            frame.loc[mask, "official_code_status"] = official_status
            changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_frame.loc[
        relation_frame["planning_feature_id"].eq(feature_id), "official_code_status"
    ] = official_status
    changed = module._result_with_hashes(replace(changed, relations=relation_frame))
    with pytest.raises(BessPlanningFeatureApplicationError, match="official|status"):
        module._validate_result_envelope(changed)
```

### `test_any_true_row_boundary_flag_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = _coordinated_policy_mutation(result, column, True)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="flag|false"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, True)
    with pytest.raises(BessPlanningFeatureApplicationError, match="flag|false"):
        module._validate_result_envelope(changed)
```

### `test_application_and_public_validator_heavy_validation_counts`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy = _compiled_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
actual = module.validate_bess_planning_feature_policy_result
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
```

**Action**

```python
result = module.apply_bess_planning_feature_policy(*inputs, coded, config, policy)
module.validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, result
    )
```

**Expected result**

```python
assert calls == 1
assert calls == 2
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_application_and_public_validator_heavy_validation_counts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy = _compiled_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    actual = module.validate_bess_planning_feature_policy_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    result = module.apply_bess_planning_feature_policy(*inputs, coded, config, policy)
    assert calls == 1
    module.validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, result
    )
    assert calls == 2
```

### `test_application_and_public_validator_heavy_validation_counts.counted`

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_local_result_fast_fails_before_heavy_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
invalid = replace(result, complete_result_content_sha256="f" * 64)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureApplicationError, match="hash|SHA|sha256|invalid"
    ):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, invalid
        )
assert calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_malformed_local_result_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    invalid = replace(result, complete_result_content_sha256="f" * 64)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="hash|SHA|sha256|invalid"
    ):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, invalid
        )
    assert calls == 0
```

### `test_malformed_local_result_fast_fails_before_heavy_validation.counted`

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_application_source_lock_mutation_fast_fails`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
changed = replace(result, policy_sha256="f" * 64)
for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        frame["bess_cnig_policy_sha256"] = pd.array(
            ["f" * 64] * len(frame), dtype="str"
        )
        changed = replace(changed, **{frame_name: frame})
relation_frame = changed.relations.copy(deep=True)
relation_frame["bess_cnig_policy_sha256"] = pd.array(
        ["f" * 64] * len(relation_frame), dtype="str"
    )
changed = module._result_with_hashes(replace(changed, relations=relation_frame))
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="source lock"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
assert calls == 0
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_coordinated_application_source_lock_mutation_fast_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    changed = replace(result, policy_sha256="f" * 64)
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        frame["bess_cnig_policy_sha256"] = pd.array(
            ["f" * 64] * len(frame), dtype="str"
        )
        changed = replace(changed, **{frame_name: frame})
    relation_frame = changed.relations.copy(deep=True)
    relation_frame["bess_cnig_policy_sha256"] = pd.array(
        ["f" * 64] * len(relation_frame), dtype="str"
    )
    changed = module._result_with_hashes(replace(changed, relations=relation_frame))
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="source lock"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0
```

### `test_coordinated_application_source_lock_mutation_fast_fails.counted`

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_four_file_manifest_and_verified_byte_readback`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, result = _application_fixture()
manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
assert_geodataframe_equal(result.surface_features, loaded.surface_features)
assert_geodataframe_equal(result.line_features, loaded.line_features)
assert_geodataframe_equal(result.point_features, loaded.point_features)
assert_frame_equal(result.relations, loaded.relations)
```

**Action**

```python
validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, loaded
    )
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Pins the exact framework interaction and outcome reproduced in the complete test source.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_four_file_manifest_and_verified_byte_readback(tmp_path: Path) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
    assert_geodataframe_equal(result.surface_features, loaded.surface_features)
    assert_geodataframe_equal(result.line_features, loaded.line_features)
    assert_geodataframe_equal(result.point_features, loaded.point_features)
    assert_frame_equal(result.relations, loaded.relations)
    validate_bess_planning_feature_application_result(
        *inputs, coded, config, policy, loaded
    )
```

### `test_duplicate_relation_pair_artifact_fails_local_loading`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
relations = pd.concat([result.relations, result.relations.iloc[[0]]])
changed = module._result_with_hashes(replace(result, relations=relations))
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_relation_pair_artifact_fails_local_loading(tmp_path: Path) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = pd.concat([result.relations, result.relations.iloc[[0]]])
    changed = module._result_with_hashes(replace(result, relations=relations))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_document_wide_mapping_conflict_artifact_fails_local_loading`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
first = result.relations.iloc[0]
different = result.relations[
        result.relations["bess_cnig_precheck_status"].ne(
            first["bess_cnig_precheck_status"]
        )
    ].iloc[0]
changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_status_priority",
        int(different["bess_cnig_status_priority"]),
    )
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_document_wide_mapping_conflict_artifact_fails_local_loading(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    first = result.relations.iloc[0]
    different = result.relations[
        result.relations["bess_cnig_precheck_status"].ne(
            first["bess_cnig_precheck_status"]
        )
    ].iloc[0]
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_status_priority",
        int(different["bess_cnig_status_priority"]),
    )
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
changed = _surface_touch_with_positive_area(result)
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureApplicationError, match="surface|metric|type"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    changed = _surface_touch_with_positive_area(result)
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="surface|metric|type"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
surface = result.surface_features.copy(deep=True)
surface.at[surface.index[0], surface.geometry.name] = Point(0, 0)
changed = module._result_with_hashes(replace(result, surface_features=surface))
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="surface|geometry"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_wrong_2d_feature_geometry_fails_local_artifact_loading(tmp_path: Path) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    surface.at[surface.index[0], surface.geometry.name] = Point(0, 0)
    changed = module._result_with_hashes(replace(result, surface_features=surface))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="surface|geometry"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_feature_catalog_geometry_role_is_intrinsic`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `frame_name`, `geometry`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
frame = getattr(result, frame_name).copy(deep=True)
frame.at[frame.index[0], frame.geometry.name] = geometry
changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="geometry"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_feature_catalog_geometry_role_is_intrinsic(
    frame_name: str, geometry: object
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    frame.at[frame.index[0], frame.geometry.name] = geometry
    changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(BessPlanningFeatureApplicationError, match="geometry"):
        module._validate_result_envelope(changed)
```

### `test_feature_catalog_metric_must_match_geometry`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `frame_name`, `metric`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
frame = getattr(result, frame_name).copy(deep=True)
frame.loc[frame.index[0], metric] += 1
changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureApplicationError, match="metric|geometry|count"
    ):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_feature_catalog_metric_must_match_geometry(
    frame_name: str, metric: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    frame.loc[frame.index[0], metric] += 1
    changed = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="metric|geometry|count"
    ):
        module._validate_result_envelope(changed)
```

### `test_unreferenced_feature_catalog_identity_fields_are_intrinsic`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
name, source, index = _zero_relation_feature(result)
frame = source.copy(deep=True)
frame.loc[index, column] = value
changed = module._result_with_hashes(replace(result, **{name: frame}))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureApplicationError, match="identity|layer|kind"
    ):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_unreferenced_feature_catalog_identity_fields_are_intrinsic(
    column: str, value: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, column] = value
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="identity|layer|kind"
    ):
        module._validate_result_envelope(changed)
```

### `test_feature_catalog_requires_canonical_crs_and_global_identity`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
surface = result.surface_features.to_crs("EPSG:4326")
point = result.point_features.copy(deep=True)
point.loc[point.index[0], "planning_feature_id"] = result.surface_features.iloc[0][
        "planning_feature_id"
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="EPSG:2154|CRS"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, surface_features=surface))
        )
with pytest.raises(BessPlanningFeatureApplicationError, match="identity|unique"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, point_features=point))
        )
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_feature_catalog_requires_canonical_crs_and_global_identity() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.to_crs("EPSG:4326")
    with pytest.raises(BessPlanningFeatureApplicationError, match="EPSG:2154|CRS"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, surface_features=surface))
        )
    point = result.point_features.copy(deep=True)
    point.loc[point.index[0], "planning_feature_id"] = result.surface_features.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(BessPlanningFeatureApplicationError, match="identity|unique"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, point_features=point))
        )
```

### `test_unreferenced_feature_identity_is_validated_locally`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `feature_id`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
name, source, index = _zero_relation_feature(result)
frame = source.copy(deep=True)
frame.loc[index, "planning_feature_id"] = feature_id
changed = module._result_with_hashes(replace(result, **{name: frame}))
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureApplicationError, match="feature|identity|GPU"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unreferenced_feature_identity_is_validated_locally(
    tmp_path: Path, feature_id: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "planning_feature_id"] = feature_id
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(
        BessPlanningFeatureApplicationError, match="feature|identity|GPU"
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_unreferenced_feature_participates_in_global_policy_mapping`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
name, source, index = _zero_relation_feature(result)
frame = source.copy(deep=True)
status = frame.loc[index, "bess_cnig_precheck_status"]
conflicting = pd.concat(
        [result.surface_features, result.line_features, result.point_features],
        ignore_index=True,
    )
conflicting = conflicting.loc[conflicting["bess_cnig_precheck_status"].ne(status)]
frame.loc[index, "bess_cnig_status_priority"] = int(
        conflicting.iloc[0]["bess_cnig_status_priority"]
    )
changed = module._result_with_hashes(replace(result, **{name: frame}))
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unreferenced_feature_participates_in_global_policy_mapping(
    tmp_path: Path,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    status = frame.loc[index, "bess_cnig_precheck_status"]
    conflicting = pd.concat(
        [result.surface_features, result.line_features, result.point_features],
        ignore_index=True,
    )
    conflicting = conflicting.loc[conflicting["bess_cnig_precheck_status"].ne(status)]
    frame.loc[index, "bess_cnig_status_priority"] = int(
        conflicting.iloc[0]["bess_cnig_status_priority"]
    )
    changed = module._result_with_hashes(replace(result, **{name: frame}))
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="priority|mapping"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_application_locks_policy_result_schema_exactly`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `policy_schema`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = module._result_with_hashes(
        replace(result, policy_result_hash_schema_version=policy_schema)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="policy.*schema"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_locks_policy_result_schema_exactly(policy_schema: int) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = module._result_with_hashes(
        replace(result, policy_result_hash_schema_version=policy_schema)
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy.*schema"):
        module._validate_result_envelope(changed)
```

### `test_application_locks_cnig_result_schema_exactly`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `cnig_schema`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=cnig_schema)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="CNIG|cnig.*schema"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_locks_cnig_result_schema_exactly(cnig_schema: int) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=cnig_schema)
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="CNIG|cnig.*schema"):
        module._validate_result_envelope(changed)
```

### `test_application_accepts_only_current_policy_and_cnig_source_schemas`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
module._validate_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.policy_result_hash_schema_version == 1
assert result.cnig_result_hash_schema_version == 5
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    assert result.policy_result_hash_schema_version == 1
    assert result.cnig_result_hash_schema_version == 5
    module._validate_result_envelope(result)
```

### `test_duplicate_relation_identity_fast_fails_before_policy_source_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
relations = pd.concat(
        [result.relations, result.relations.iloc[[0]]], ignore_index=True
    )
relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
changed = module._result_with_hashes(replace(result, relations=relations))
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
assert calls == 0
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_duplicate_relation_identity_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    relations = pd.concat(
        [result.relations, result.relations.iloc[[0]]], ignore_index=True
    )
    relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    changed = module._result_with_hashes(replace(result, relations=relations))
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module.validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0
```

### `test_duplicate_relation_identity_fast_fails_before_policy_source_validation.counted`

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_self_consistent_z_geoparquet_artifact_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
surface = result.surface_features.copy(deep=True)
original = surface.geometry.iloc[0]
surface.at[surface.index[0], surface.geometry.name] = Polygon(
        [(x, y, 9) for x, y in original.exterior.coords]
    )
changed = replace(result, surface_features=surface)
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_self_consistent_z_geoparquet_artifact_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    original = surface.geometry.iloc[0]
    surface.at[surface.index[0], surface.geometry.name] = Polygon(
        [(x, y, 9) for x, y in original.exterior.coords]
    )
    changed = replace(result, surface_features=surface)
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_self_consistent_wrong_dtype_artifact_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_precheck_status",
        "UNKNOWN",
        dtype="object",
    )
manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_self_consistent_wrong_dtype_artifact_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_precheck_status",
        "UNKNOWN",
        dtype="object",
    )
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="dtype|schema"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_artifact_manifest_rejects_invalid_contract`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `message`, `mutation`.

**Setup**

```python
_, _, _, _, result = _application_fixture()
manifest_path, paths, manifest = _write_application_artifacts(tmp_path, result)
mutation(manifest)
manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert callable(mutation)
with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_artifact_manifest_rejects_invalid_contract(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, manifest = _write_application_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match=message):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_manifest_rejects_duplicate_json_key`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
manifest_path.write_text(
        '{"schema_version": 2, "schema_version": 2}\n', encoding="utf-8"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="Duplicate JSON"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_manifest_rejects_duplicate_json_key(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    manifest_path.write_text(
        '{"schema_version": 2, "schema_version": 2}\n', encoding="utf-8"
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="Duplicate JSON"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_artifact_loader_parses_only_verified_bytes`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
target = paths["RELATIONS"]
replacement = tmp_path / "replacement.parquet"
result.relations.to_parquet(replacement, index=True, compression="gzip")
original_read_bytes = Path.read_bytes
verified = original_read_bytes(target)
replacement_bytes = original_read_bytes(replacement)
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
original_read_parquet = module.pd.read_parquet
replaced = False
observed: list[tuple[str, bytes]] = []
def replace_after_read(path: Path) -> bytes:
        nonlocal replaced
        payload = original_read_bytes(path)
        if path == target and not replaced:
            path.write_bytes(replacement_bytes)
            replaced = True
        return payload
def observed_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(("buffer", source.getvalue()))
        return original_read_parquet(source, *args, **kwargs)
monkeypatch.setattr(Path, "read_bytes", replace_after_read)
monkeypatch.setattr(module.pd, "read_parquet", observed_read)
loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
assert_frame_equal(result.relations, loaded.relations)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert replaced
assert ("buffer", verified) in observed
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_artifact_loader_parses_only_verified_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    target = paths["RELATIONS"]
    replacement = tmp_path / "replacement.parquet"
    result.relations.to_parquet(replacement, index=True, compression="gzip")
    original_read_bytes = Path.read_bytes
    verified = original_read_bytes(target)
    replacement_bytes = original_read_bytes(replacement)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    original_read_parquet = module.pd.read_parquet
    replaced = False
    observed: list[tuple[str, bytes]] = []

    def replace_after_read(path: Path) -> bytes:
        nonlocal replaced
        payload = original_read_bytes(path)
        if path == target and not replaced:
            path.write_bytes(replacement_bytes)
            replaced = True
        return payload

    def observed_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(("buffer", source.getvalue()))
        return original_read_parquet(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_read)
    monkeypatch.setattr(module.pd, "read_parquet", observed_read)
    loaded = load_bess_planning_feature_application_artifacts(
        manifest_path,
        paths["SURFACE_FEATURES"],
        paths["LINE_FEATURES"],
        paths["POINT_FEATURES"],
        paths["RELATIONS"],
    )
    assert replaced
    assert ("buffer", verified) in observed
    assert_frame_equal(result.relations, loaded.relations)
```

### `test_artifact_loader_parses_only_verified_bytes.replace_after_read`

**Exact signature**

```python
def replace_after_read(path: Path) -> bytes:
```

**Purpose**

Private `test` helper for replace after read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
payload
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `original_read_bytes`.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `monkeypatch.setattr(Path, 'read_bytes', replace_after_read)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes` via `monkeypatch.setattr(Path, 'read_bytes', replace_after_read)`.

**Complete source-ordered implementation**

```python
def replace_after_read(path: Path) -> bytes:
        nonlocal replaced
        payload = original_read_bytes(path)
        if path == target and not replaced:
            path.write_bytes(replacement_bytes)
            replaced = True
        return payload
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_only_verified_bytes.observed_read`

**Exact signature**

```python
def observed_read(source: object, *args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for observed read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
original_read_parquet(source, *args, **kwargs)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `original_read_parquet`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes` via `monkeypatch.setattr(module.pd, 'read_parquet', observed_read)`.

**Complete source-ordered implementation**

```python
def observed_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(("buffer", source.getvalue()))
        return original_read_parquet(source, *args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_physical_replacement_before_loading_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
paths["RELATIONS"].write_bytes(paths["RELATIONS"].read_bytes() + b"tamper")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="size|SHA|hash"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_physical_replacement_before_loading_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    paths["RELATIONS"].write_bytes(paths["RELATIONS"].read_bytes() + b"tamper")
    with pytest.raises(BessPlanningFeatureApplicationError, match="size|SHA|hash"):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_public_application_api_exports_only_stable_symbols`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
required = {
        "BessPlanningFeatureApplicationArtifactManifest",
        "BessPlanningFeatureApplicationError",
        "BessPlanningFeatureApplicationResult",
        "apply_bess_planning_feature_policy",
        "load_bess_planning_feature_application_artifacts",
        "validate_bess_planning_feature_application_result",
        "validate_bess_planning_feature_application_result_envelope",
    }
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(module.__all__) == required
assert required.issubset(set(stages.__all__))
assert not any(name.startswith("_") for name in module.__all__)
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_application_api_exports_only_stable_symbols() -> None:
    required = {
        "BessPlanningFeatureApplicationArtifactManifest",
        "BessPlanningFeatureApplicationError",
        "BessPlanningFeatureApplicationResult",
        "apply_bess_planning_feature_policy",
        "load_bess_planning_feature_application_artifacts",
        "validate_bess_planning_feature_application_result",
        "validate_bess_planning_feature_application_result_envelope",
    }
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert not any(name.startswith("_") for name in module.__all__)
```

### `_replace_application_frame`

**Exact signature**

```python
def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Private `test` helper for replace application frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(replace(result, **{frame_name: frame}))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_replace_application_frame`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `_replace_application_frame`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `_replace_application_frame`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `_replace_application_frame`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema` via `_replace_application_frame`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema` via `_replace_application_frame`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_replace_application_frame`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `_replace_application_frame`.

**Complete source-ordered implementation**

```python
def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    return module._result_with_hashes(replace(result, **{frame_name: frame}))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coordinated_referenced_lineage_mutation`

**Exact signature**

```python
def _coordinated_referenced_lineage_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: str,
    *,
    rename_id: bool = False,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Private `test` helper for coordinated referenced lineage mutation; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(replace(changed, relations=relations))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame.loc[mask, 'planning_feature_id']`, `frame.loc[mask, column]`, `relations.loc[mask, 'planning_feature_id']`, `relations.loc[mask, column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `_coordinated_referenced_lineage_mutation`.

**Complete source-ordered implementation**

```python
def _coordinated_referenced_lineage_mutation(
    result: BessPlanningFeatureApplicationResult,
    column: str,
    value: str,
    *,
    rename_id: bool = False,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    feature_id = str(result.relations.iloc[0]["planning_feature_id"])
    changed = result
    replacement_id = feature_id
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        mask = frame["planning_feature_id"].eq(feature_id)
        if mask.any():
            frame.loc[mask, column] = value
            if rename_id:
                row = frame.loc[mask].iloc[0]
                replacement_id = (
                    f"GPU:{row['source_document_id']}:"
                    f"{row['logical_layer']}:{row['source_feature_id']}"
                )
                frame.loc[mask, "planning_feature_id"] = replacement_id
            changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    mask = relations["planning_feature_id"].eq(feature_id)
    relations.loc[mask, column] = value
    if rename_id:
        relations.loc[mask, "planning_feature_id"] = replacement_id
    return module._result_with_hashes(replace(changed, relations=relations))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
name, source, index = _zero_relation_feature(result)
frame = source.copy(deep=True)
frame.loc[index, "source_document_id"] = "MUTATED-DOCUMENT"
frame.loc[index, "planning_feature_id"] = (
        f"GPU:MUTATED-DOCUMENT:{frame.loc[index, 'logical_layer']}:"
        f"{frame.loc[index, 'source_feature_id']}"
    )
changed = _replace_application_frame(result, name, frame)
manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="document|lineage"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "source_document_id"] = "MUTATED-DOCUMENT"
    frame.loc[index, "planning_feature_id"] = (
        f"GPU:MUTATED-DOCUMENT:{frame.loc[index, 'logical_layer']}:"
        f"{frame.loc[index, 'source_feature_id']}"
    )
    changed = _replace_application_frame(result, name, frame)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="document|lineage"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_feature_row_lineage_must_match_application_envelope`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
if mutation == "envelope-document":
        changed = module._result_with_hashes(
            replace(result, source_document_id="MUTATED-DOCUMENT")
        )
    else:
        name, source, index = _zero_relation_feature(result)
        frame = source.copy(deep=True)
        if mutation == "archive":
            frame.loc[index, "source_archive_sha256"] = "f" * 64
        else:
            frame.loc[index, "official_code_profile"] = "mutated_profile"
            frame.loc[index, "official_code_profile_sha256"] = "f" * 64
        changed = _replace_application_frame(result, name, frame)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_feature_row_lineage_must_match_application_envelope(mutation: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    if mutation == "envelope-document":
        changed = module._result_with_hashes(
            replace(result, source_document_id="MUTATED-DOCUMENT")
        )
    else:
        name, source, index = _zero_relation_feature(result)
        frame = source.copy(deep=True)
        if mutation == "archive":
            frame.loc[index, "source_archive_sha256"] = "f" * 64
        else:
            frame.loc[index, "official_code_profile"] = "mutated_profile"
            frame.loc[index, "official_code_profile_sha256"] = "f" * 64
        changed = _replace_application_frame(result, name, frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)
```

### `test_coordinated_referenced_row_lineage_cannot_bypass_envelope`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `rename_id`, `value`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
changed = _coordinated_referenced_lineage_mutation(
        result, column, value, rename_id=rename_id
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_referenced_row_lineage_cannot_bypass_envelope(
    column: str,
    value: str,
    rename_id: bool,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_referenced_lineage_mutation(
        result, column, value, rename_id=rename_id
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="lineage|document"):
        module._validate_result_envelope(changed)
```

### `test_resolved_official_row_requires_label_and_envelope_profile`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
name, source, index = _zero_relation_feature(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
for column, value in (
        ("official_code_label", pd.NA),
        ("official_code_profile", "wrong_profile"),
    ):
        frame = source.copy(deep=True)
        frame.loc[index, column] = value
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(
            BessPlanningFeatureApplicationError, match="official|profile|label"
        ):
            module._validate_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_resolved_official_row_requires_label_and_envelope_profile() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    for column, value in (
        ("official_code_label", pd.NA),
        ("official_code_profile", "wrong_profile"),
    ):
        frame = source.copy(deep=True)
        frame.loc[index, column] = value
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(
            BessPlanningFeatureApplicationError, match="official|profile|label"
        ):
            module._validate_result_envelope(changed)
```

### `test_unknown_official_row_rejects_invented_label_or_url`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
name, source, index = _zero_relation_feature(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
for invented_column in ("official_code_label", "official_code_source_url"):
        frame = source.copy(deep=True)
        frame.loc[index, "official_code_status"] = "UNKNOWN_CODE_PAIR"
        frame.loc[index, "bess_cnig_policy_application_status"] = "UNRESOLVED_CODE_PAIR"
        for column in (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ):
            frame.loc[index, column] = pd.NA
        frame.loc[index, "bess_cnig_status_priority"] = pd.NA
        frame.loc[index, invented_column] = (
            "Invented label"
            if invented_column == "official_code_label"
            else "https://example.invalid/invented"
        )
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(BessPlanningFeatureApplicationError, match="official|null"):
            module._validate_result_envelope(changed)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_official_row_rejects_invented_label_or_url() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    name, source, index = _zero_relation_feature(result)
    for invented_column in ("official_code_label", "official_code_source_url"):
        frame = source.copy(deep=True)
        frame.loc[index, "official_code_status"] = "UNKNOWN_CODE_PAIR"
        frame.loc[index, "bess_cnig_policy_application_status"] = "UNRESOLVED_CODE_PAIR"
        for column in (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ):
            frame.loc[index, column] = pd.NA
        frame.loc[index, "bess_cnig_status_priority"] = pd.NA
        frame.loc[index, invented_column] = (
            "Invented label"
            if invented_column == "official_code_label"
            else "https://example.invalid/invented"
        )
        changed = _replace_application_frame(result, name, frame)
        with pytest.raises(BessPlanningFeatureApplicationError, match="official|null"):
            module._validate_result_envelope(changed)
```

### `test_application_feature_prefix_has_exact_canonical_schema`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `frame_name`, `mutation`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
frame = getattr(result, frame_name).copy(deep=True)
if mutation == "missing-column":
        frame = frame.drop(columns="regulation_url_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "metric-object":
        metric = {
            "surface_features": "feature_area_m2",
            "line_features": "feature_length_m",
            "point_features": "point_member_count",
        }[frame_name]
        frame[metric] = pd.Series(
            frame[metric].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-object":
        frame["official_legal_reference"] = pd.Series(
            frame["official_legal_reference"].tolist(),
            index=frame.index,
            dtype="object",
        )
    elif mutation == "index-name":
        frame.index = frame.index.rename("wrong")
    elif mutation == "index-dtype":
        frame.index = pd.Index(frame.index.to_numpy(dtype="int32"), dtype="int32")
    else:
        frame = frame.iloc[0:0].copy()
        frame["point_member_count"] = pd.Series(dtype="object")
changed = _replace_application_frame(result, frame_name, frame)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype|index"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_feature_prefix_has_exact_canonical_schema(
    frame_name: str,
    mutation: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = getattr(result, frame_name).copy(deep=True)
    if mutation == "missing-column":
        frame = frame.drop(columns="regulation_url_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "metric-object":
        metric = {
            "surface_features": "feature_area_m2",
            "line_features": "feature_length_m",
            "point_features": "point_member_count",
        }[frame_name]
        frame[metric] = pd.Series(
            frame[metric].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-object":
        frame["official_legal_reference"] = pd.Series(
            frame["official_legal_reference"].tolist(),
            index=frame.index,
            dtype="object",
        )
    elif mutation == "index-name":
        frame.index = frame.index.rename("wrong")
    elif mutation == "index-dtype":
        frame.index = pd.Index(frame.index.to_numpy(dtype="int32"), dtype="int32")
    else:
        frame = frame.iloc[0:0].copy()
        frame["point_member_count"] = pd.Series(dtype="object")
    changed = _replace_application_frame(result, frame_name, frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype|index"):
        module._validate_result_envelope(changed)
```

### `test_application_relation_prefix_has_exact_canonical_schema`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
frame = result.relations.copy(deep=True)
if mutation == "missing-column":
        frame = frame.drop(columns="label_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "float-object":
        frame["intersection_area_m2"] = pd.Series(
            frame["intersection_area_m2"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "count-object":
        frame["point_member_count"] = pd.Series(
            frame["point_member_count"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-category":
        frame["official_code_label"] = pd.Series(
            pd.Categorical(frame["official_code_label"]), index=frame.index
        )
    else:
        frame = frame.iloc[0:0].drop(columns="label_raw")
changed = _replace_application_frame(result, "relations", frame)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_relation_prefix_has_exact_canonical_schema(
    mutation: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    frame = result.relations.copy(deep=True)
    if mutation == "missing-column":
        frame = frame.drop(columns="label_raw")
    elif mutation == "unexpected-column":
        position = frame.columns.get_loc(POLICY_COLUMNS[0])
        frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))
    elif mutation == "reordered-columns":
        columns = list(frame.columns)
        columns[0], columns[1] = columns[1], columns[0]
        frame = frame.loc[:, columns]
    elif mutation == "float-object":
        frame["intersection_area_m2"] = pd.Series(
            frame["intersection_area_m2"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "count-object":
        frame["point_member_count"] = pd.Series(
            frame["point_member_count"].tolist(), index=frame.index, dtype="object"
        )
    elif mutation == "official-category":
        frame["official_code_label"] = pd.Series(
            pd.Categorical(frame["official_code_label"]), index=frame.index
        )
    else:
        frame = frame.iloc[0:0].drop(columns="label_raw")
    changed = _replace_application_frame(result, "relations", frame)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        module._validate_result_envelope(changed)
```

### `test_self_consistent_factual_prefix_dtype_artifact_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
surface = result.surface_features.copy(deep=True)
surface["feature_area_m2"] = pd.Series(
        surface["feature_area_m2"].tolist(), index=surface.index, dtype="object"
    )
changed = _replace_application_frame(result, "surface_features", surface)
manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_self_consistent_factual_prefix_dtype_artifact_is_rejected(
    tmp_path: Path,
) -> None:
    _, _, _, _, result = _application_fixture()
    surface = result.surface_features.copy(deep=True)
    surface["feature_area_m2"] = pd.Series(
        surface["feature_area_m2"].tolist(), index=surface.index, dtype="object"
    )
    changed = _replace_application_frame(result, "surface_features", surface)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="schema|dtype"):
        load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
```

### `test_lineage_defect_fast_fails_before_policy_source_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
name, source, index = _zero_relation_feature(result)
frame = source.copy(deep=True)
frame.loc[index, "source_archive_sha256"] = "f" * 64
changed = _replace_application_frame(result, name, frame)
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
assert calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_lineage_defect_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    name, source, index = _zero_relation_feature(result)
    frame = source.copy(deep=True)
    frame.loc[index, "source_archive_sha256"] = "f" * 64
    changed = _replace_application_frame(result, name, frame)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", counted)
    with pytest.raises(BessPlanningFeatureApplicationError):
        validate_bess_planning_feature_application_result(
            *inputs, coded, config, policy, changed
        )
    assert calls == 0
```

### `test_lineage_defect_fast_fails_before_policy_source_validation.counted`

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
_, _, _, _, result = _application_fixture()
module.validate_bess_planning_feature_application_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(
        inspect.signature(
            module.load_bess_planning_feature_application_artifacts
        ).parameters
    ) == (
        "manifest_path",
        "surface_features_path",
        "line_features_path",
        "point_features_path",
        "relations_path",
        "coded_result",
        "policy_result",
    )
assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")
with pytest.raises(BessPlanningFeatureApplicationError, match="hash|invalid"):
        module.validate_bess_planning_feature_application_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    assert tuple(
        inspect.signature(
            module.load_bess_planning_feature_application_artifacts
        ).parameters
    ) == (
        "manifest_path",
        "surface_features_path",
        "line_features_path",
        "point_features_path",
        "relations_path",
        "coded_result",
        "policy_result",
    )
    assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")
    _, _, _, _, result = _application_fixture()
    module.validate_bess_planning_feature_application_result_envelope(result)
    with pytest.raises(BessPlanningFeatureApplicationError, match="hash|invalid"):
        module.validate_bess_planning_feature_application_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )
```

### `test_source_bound_application_loader_rejects_locally_valid_rationale_change`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_rationale",
        "A different exact non-empty rationale.",
    )
module._validate_result_envelope(changed)
manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="upstream|rebuilt"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_bound_application_loader_rejects_locally_valid_rationale_change(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed = _coordinated_policy_mutation(
        result,
        "bess_cnig_rationale",
        "A different exact non-empty rationale.",
    )
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream|rebuilt"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )
```

### `test_application_manifest_filenames_are_casefold_unique`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, result = _application_fixture()
_, _, payload = _write_application_artifacts(tmp_path, result)
payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_application_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)
```

### `_swap_referenced_feature_values`

**Exact signature**

```python
def _swap_referenced_feature_values(
    result: BessPlanningFeatureApplicationResult,
    columns: tuple[str, ...],
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Private `test` helper for swap referenced feature values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(replace(changed, relations=relations))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame.loc[first_mask, column]`, `frame.loc[second_mask, column]`, `relations.loc[first_mask, column]`, `relations.loc[second_mask, column]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_swap_referenced_feature_values`.

**Complete source-ordered implementation**

```python
def _swap_referenced_feature_values(
    result: BessPlanningFeatureApplicationResult,
    columns: tuple[str, ...],
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    referenced = result.relations.loc[
        result.relations["bess_cnig_policy_application_status"].eq(
            "APPLIED_EXACT_POLICY"
        )
    ]
    first = referenced.iloc[0]
    second = referenced.loc[
        referenced["bess_cnig_precheck_status"].ne(first["bess_cnig_precheck_status"])
    ].iloc[0]
    first_id = str(first["planning_feature_id"])
    second_id = str(second["planning_feature_id"])
    changed = result
    for frame_name in ("surface_features", "line_features", "point_features"):
        frame = getattr(changed, frame_name).copy(deep=True)
        first_mask = frame["planning_feature_id"].eq(first_id)
        second_mask = frame["planning_feature_id"].eq(second_id)
        if first_mask.any() or second_mask.any():
            for column in columns:
                first_value = first[column]
                second_value = second[column]
                frame.loc[first_mask, column] = second_value
                frame.loc[second_mask, column] = first_value
            changed = replace(changed, **{frame_name: frame})
    relations = changed.relations.copy(deep=True)
    first_mask = relations["planning_feature_id"].eq(first_id)
    second_mask = relations["planning_feature_id"].eq(second_id)
    for column in columns:
        first_value = first[column]
        second_value = second[column]
        relations.loc[first_mask, column] = second_value
        relations.loc[second_mask, column] = first_value
    return module._result_with_hashes(replace(changed, relations=relations))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `columns`.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
changed = _swap_referenced_feature_values(result, columns)
module._validate_result_envelope(changed)
manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
heavy_calls = 0
def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1
monkeypatch.setattr(
        module, "validate_bess_planning_feature_policy_result", forbidden_heavy
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )
assert heavy_calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_bound_loader_rejects_valid_domain_cross_pair_swaps(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    columns: tuple[str, ...],
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed = _swap_referenced_feature_values(result, columns)
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    heavy_calls = 0

    def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_policy_result", forbidden_heavy
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
            coded,
            policy,
        )
    assert heavy_calls == 0
```

### `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps.forbidden_heavy`

**Exact signature**

```python
def forbidden_heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for forbidden heavy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', forbidden_heavy)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', forbidden_heavy)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', forbidden_heavy)`.

**Complete source-ordered implementation**

```python
def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_loader_rejects_factual_prefix_lineage_change`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `column`.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
surface = result.surface_features.copy(deep=True)
surface.loc[surface.index[0], column] = f"changed-{column}"
changed = module._result_with_hashes(replace(result, surface_features=surface))
module._validate_result_envelope(changed)
manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_bound_loader_rejects_factual_prefix_lineage_change(
    tmp_path: Path, column: str
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], column] = f"changed-{column}"
    changed = module._result_with_hashes(replace(result, surface_features=surface))
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
```

### `test_source_bound_loader_rejects_all_null_raw_column_transition`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, coded, _, policy, _ = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
policy_module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
coded_surface = coded.surface_features.copy(deep=True)
coded_surface["text_raw"] = pd.Series(
        ["source text"] * len(coded_surface), index=coded_surface.index, dtype="str"
    )
coded_relations = coded.relations.copy(deep=True)
surface_ids = set(coded_surface["planning_feature_id"])
coded_relations.loc[
        coded_relations["planning_feature_id"].isin(surface_ids), "text_raw"
    ] = "source text"
coded_relations["text_raw"] = pd.Series(
        coded_relations["text_raw"].tolist(),
        index=coded_relations.index,
        dtype="str",
    )
coded = coding_module._result_with_hashes(
        replace(
            coded,
            surface_features=coded_surface,
            relations=coded_relations,
        )
    )
policy_table = policy.policy_table.copy(deep=True)
policy_table["cnig_complete_result_content_sha256"] = pd.array(
        [coded.complete_result_content_sha256] * len(policy_table), dtype="str"
    )
policy = policy_module._result_with_hashes(
        replace(
            policy,
            cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
            policy_table=policy_table,
        )
    )
result = module._build_result(coded, policy)
surface = result.surface_features.copy(deep=True)
surface["text_raw"] = pd.Series(None, index=surface.index, dtype="object")
relations = result.relations.copy(deep=True)
mask = relations["geometry_kind"].eq("SURFACE")
relations.loc[mask, "text_raw"] = pd.NA
relations["text_raw"] = pd.Series(
        relations["text_raw"].tolist(), index=relations.index, dtype="str"
    )
changed = module._result_with_hashes(
        replace(result, surface_features=surface, relations=relations)
    )
module._validate_result_envelope(changed)
manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
reordered = result.surface_features.iloc[::-1].copy(deep=True)
changed = module._result_with_hashes(replace(result, surface_features=reordered))
module._validate_result_envelope(changed)
reordered_dir = tmp_path / "reordered"
reordered_dir.mkdir()
manifest, paths, _ = _write_application_artifacts(reordered_dir, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_source_bound_loader_rejects_all_null_raw_column_transition(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, _ = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    policy_module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    coded_surface = coded.surface_features.copy(deep=True)
    coded_surface["text_raw"] = pd.Series(
        ["source text"] * len(coded_surface), index=coded_surface.index, dtype="str"
    )
    coded_relations = coded.relations.copy(deep=True)
    surface_ids = set(coded_surface["planning_feature_id"])
    coded_relations.loc[
        coded_relations["planning_feature_id"].isin(surface_ids), "text_raw"
    ] = "source text"
    coded_relations["text_raw"] = pd.Series(
        coded_relations["text_raw"].tolist(),
        index=coded_relations.index,
        dtype="str",
    )
    coded = coding_module._result_with_hashes(
        replace(
            coded,
            surface_features=coded_surface,
            relations=coded_relations,
        )
    )
    policy_table = policy.policy_table.copy(deep=True)
    policy_table["cnig_complete_result_content_sha256"] = pd.array(
        [coded.complete_result_content_sha256] * len(policy_table), dtype="str"
    )
    policy = policy_module._result_with_hashes(
        replace(
            policy,
            cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
            policy_table=policy_table,
        )
    )
    result = module._build_result(coded, policy)
    surface = result.surface_features.copy(deep=True)
    surface["text_raw"] = pd.Series(None, index=surface.index, dtype="object")
    relations = result.relations.copy(deep=True)
    mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[mask, "text_raw"] = pd.NA
    relations["text_raw"] = pd.Series(
        relations["text_raw"].tolist(), index=relations.index, dtype="str"
    )
    changed = module._result_with_hashes(
        replace(result, surface_features=surface, relations=relations)
    )
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_application_artifacts(tmp_path, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )

    reordered = result.surface_features.iloc[::-1].copy(deep=True)
    changed = module._result_with_hashes(replace(result, surface_features=reordered))
    module._validate_result_envelope(changed)
    reordered_dir = tmp_path / "reordered"
    reordered_dir.mkdir()
    manifest, paths, _ = _write_application_artifacts(reordered_dir, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
```

### `test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
name, source, index = _zero_relation_feature(result)
unreferenced = source.copy(deep=True)
unreferenced.loc[index, "label_raw"] = "changed unreferenced label"
changed = module._result_with_hashes(replace(result, **{name: unreferenced}))
module._validate_result_envelope(changed)
unreferenced_dir = tmp_path / "unreferenced"
unreferenced_dir.mkdir()
manifest, paths, _ = _write_application_artifacts(unreferenced_dir, changed)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering(
    tmp_path: Path,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    name, source, index = _zero_relation_feature(result)
    unreferenced = source.copy(deep=True)
    unreferenced.loc[index, "label_raw"] = "changed unreferenced label"
    changed = module._result_with_hashes(replace(result, **{name: unreferenced}))
    module._validate_result_envelope(changed)
    unreferenced_dir = tmp_path / "unreferenced"
    unreferenced_dir.mkdir()
    manifest, paths, _ = _write_application_artifacts(unreferenced_dir, changed)
    with pytest.raises(BessPlanningFeatureApplicationError, match="upstream"):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
```

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
manifest, paths, _ = _write_application_artifacts(tmp_path, result)
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
coded_before = coded.surface_features.copy(deep=True)
policy_before = policy.policy_table.copy(deep=True)
actual_coded_envelope = module.validate_planning_feature_code_result_envelope
actual_policy_envelope = (
        module.validate_bess_planning_feature_policy_result_envelope
    )
actual_build = module._build_result
calls = {"coded": 0, "policy": 0, "build": 0, "heavy": 0}
def coded_envelope(value: object) -> None:
        calls["coded"] += 1
        actual_coded_envelope(value)
def policy_envelope(value: object) -> None:
        calls["policy"] += 1
        actual_policy_envelope(value)
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        return actual_build(*args, **kwargs)
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
monkeypatch.setattr(
        module, "validate_planning_feature_code_result_envelope", coded_envelope
    )
monkeypatch.setattr(
        module,
        "validate_bess_planning_feature_policy_result_envelope",
        policy_envelope,
    )
monkeypatch.setattr(module, "_build_result", build)
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
loaded = module.load_bess_planning_feature_application_artifacts(
        manifest, *paths.values(), coded, policy
    )
assert_geodataframe_equal(coded.surface_features, coded_before)
assert_frame_equal(policy.policy_table, policy_before)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )
assert calls == {"coded": 1, "policy": 1, "build": 1, "heavy": 0}
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_application_loader_validates_upstreams_and_rebuilds_once_lightweight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    coded_before = coded.surface_features.copy(deep=True)
    policy_before = policy.policy_table.copy(deep=True)
    actual_coded_envelope = module.validate_planning_feature_code_result_envelope
    actual_policy_envelope = (
        module.validate_bess_planning_feature_policy_result_envelope
    )
    actual_build = module._build_result
    calls = {"coded": 0, "policy": 0, "build": 0, "heavy": 0}

    def coded_envelope(value: object) -> None:
        calls["coded"] += 1
        actual_coded_envelope(value)

    def policy_envelope(value: object) -> None:
        calls["policy"] += 1
        actual_policy_envelope(value)

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        return actual_build(*args, **kwargs)

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(
        module, "validate_planning_feature_code_result_envelope", coded_envelope
    )
    monkeypatch.setattr(
        module,
        "validate_bess_planning_feature_policy_result_envelope",
        policy_envelope,
    )
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    loaded = module.load_bess_planning_feature_application_artifacts(
        manifest, *paths.values(), coded, policy
    )
    assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )
    assert calls == {"coded": 1, "policy": 1, "build": 1, "heavy": 0}
    assert_geodataframe_equal(coded.surface_features, coded_before)
    assert_frame_equal(policy.policy_table, policy_before)
```

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.coded_envelope`

**Exact signature**

```python
def coded_envelope(value: object) -> None:
```

**Purpose**

Private `test` helper for coded envelope; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result_envelope', coded_envelope)`.

**Complete source-ordered implementation**

```python
def coded_envelope(value: object) -> None:
        calls["coded"] += 1
        actual_coded_envelope(value)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.policy_envelope`

**Exact signature**

```python
def policy_envelope(value: object) -> None:
```

**Purpose**

Private `test` helper for policy envelope; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result_envelope', policy_envelope)`.

**Complete source-ordered implementation**

```python
def policy_envelope(value: object) -> None:
        calls["policy"] += 1
        actual_policy_envelope(value)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.build`

**Exact signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Constructs build; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
actual_build(*args, **kwargs)
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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, '_build_result', build)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, '_build_result', build)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(module, '_build_result', build)`.

**Complete source-ordered implementation**

```python
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        return actual_build(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.heavy`

**Exact signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for heavy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.

**Complete source-ordered implementation**

```python
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_bad_upstream_before_artifact_reads`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
manifest, paths, _ = _write_application_artifacts(tmp_path, result)
reads = 0
original = Path.read_bytes
def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)
monkeypatch.setattr(Path, "read_bytes", counted)
forged = replace(coded, complete_result_content_sha256="0" * 64)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(Exception, match="hash|SHA|invalid"):
        _load_application_artifacts(manifest, *paths.values(), forged, policy)
assert reads == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_application_loader_rejects_bad_upstream_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    reads = 0
    original = Path.read_bytes

    def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted)
    forged = replace(coded, complete_result_content_sha256="0" * 64)
    with pytest.raises(Exception, match="hash|SHA|invalid"):
        _load_application_artifacts(manifest, *paths.values(), forged, policy)
    assert reads == 0
```

### `test_application_loader_rejects_bad_upstream_before_artifact_reads.counted`

**Exact signature**

```python
def counted(path: Path) -> bytes:
```

**Purpose**

Private `test` helper for counted; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- Every observed return expression is reproduced without truncation:
```python
original(path)
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

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_manifest_rejects_nonportable_filename`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `filename`.

**Setup**

```python
_, _, _, _, result = _application_fixture()
_, _, payload = _write_application_artifacts(tmp_path, result)
payload["artifacts"][0]["filename"] = filename
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_application_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)
```

### `_compatible_policy_mutation`

**Exact signature**

```python
def _compatible_policy_mutation(policy: object, mutation: str) -> object:
```

**Purpose**

Private `test` helper for compatible policy mutation; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(changed)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: `extra['type_code']`, `scalar_changes['cnig_complete_result_content_sha256']`, `scalar_changes['cnig_profile']`, `scalar_changes['cnig_profile_schema_version']`, `scalar_changes['cnig_profile_sha256']`, `scalar_changes['source_archive_sha256']`, `scalar_changes['source_document_id']`, `table.index`, `table.loc[table.index[0], 'official_label']`, `table.loc[table.index[0], 'official_legal_reference']`, `table.loc[table.index[0], 'official_regulation_reference']`, `table['cnig_complete_result_content_sha256']`, `table['cnig_profile']`, `table['cnig_profile_sha256']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_compatible_policy_mutation`.

**Complete source-ordered implementation**

```python
def _compatible_policy_mutation(policy: object, mutation: str) -> object:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = policy.policy_table.copy(deep=True)
    scalar_changes: dict[str, object] = {}
    if mutation == "profile-schema":
        scalar_changes["cnig_profile_schema_version"] = 3
    elif mutation == "extra-pair":
        extra = table.iloc[[0]].copy(deep=True)
        extra["type_code"] = pd.array(["98"], dtype="str")
        table = pd.concat([table, extra], ignore_index=True).sort_values(
            ["feature_family", "type_code", "subtype_code"], kind="stable"
        )
        table.index = pd.Index(table.index.to_numpy(), dtype="int64")
    elif mutation == "missing-pair":
        table = table.iloc[:-1].copy(deep=True)
        table.index = pd.Index(range(len(table)), dtype="int64")
    elif mutation == "official-label":
        table.loc[table.index[0], "official_label"] = "Another exact official label"
    elif mutation == "legal-reference":
        table.loc[table.index[0], "official_legal_reference"] = "Changed legal ref"
    elif mutation == "regulation-reference":
        table.loc[table.index[0], "official_regulation_reference"] = (
            "Changed regulation ref"
        )
    elif mutation == "document":
        scalar_changes["source_document_id"] = "OTHER-DOCUMENT"
    elif mutation == "archive":
        scalar_changes["source_archive_sha256"] = "b" * 64
    elif mutation == "profile":
        scalar_changes["cnig_profile"] = "other-cnig-profile"
        table["cnig_profile"] = pd.array(
            ["other-cnig-profile"] * len(table), dtype="str"
        )
    elif mutation == "profile-sha":
        scalar_changes["cnig_profile_sha256"] = "a" * 64
        table["cnig_profile_sha256"] = pd.array(["a" * 64] * len(table), dtype="str")
    else:
        scalar_changes["cnig_complete_result_content_sha256"] = "a" * 64
        table["cnig_complete_result_content_sha256"] = pd.array(
            ["a" * 64] * len(table), dtype="str"
        )
    changed = replace(policy, policy_table=table, **scalar_changes)
    return module._result_with_hashes(changed)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
manifest, paths, _ = _write_application_artifacts(tmp_path, result)
changed_policy = _compatible_policy_mutation(policy, mutation)
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")
def read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("artifact read must not run")
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
monkeypatch.setattr(module, "_read_verified_artifact", read)
monkeypatch.setattr(module, "_build_result", build)
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
monkeypatch.setattr(Path, "read_text", manifest_read)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Policy|policy|CNIG|pair|source|schema|official|reference",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, changed_policy
        )
assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    changed_policy = _compatible_policy_mutation(policy, mutation)
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}

    def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")

    def read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("artifact read must not run")

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(module, "_read_verified_artifact", read)
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    monkeypatch.setattr(Path, "read_text", manifest_read)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Policy|policy|CNIG|pair|source|schema|official|reference",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, changed_policy
        )
    assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
```

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.manifest_read`

**Exact signature**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
```

**Purpose**

Private `test` helper for manifest read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('manifest read must not run')`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(Path, 'read_text', manifest_read)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(Path, 'read_text', manifest_read)`.

**Complete source-ordered implementation**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.read`

**Exact signature**

```python
def read(*args: object, **kwargs: object) -> object:
```

**Purpose**

Reads read; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `object`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('artifact read must not run')`.

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

- direct call or construction: `src/landscout/common/safe_http.py::SafeHttpsResponse.read` via `self._response.read`.
- property/attribute access: `src/landscout/common/safe_http.py::SafeHttpsResponse.read` via `self._response.read`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::_sha256` via `stream.read`.
- property/attribute access: `src/landscout/sources/cadastre_fr.py::_sha256` via `stream.read`.
- direct call or construction: `src/landscout/sources/cadastre_fr.py::_is_valid_gzip` via `stream.read`.
- property/attribute access: `src/landscout/sources/cadastre_fr.py::_is_valid_gzip` via `stream.read`.
- direct call or construction: `src/landscout/sources/cadastre_loader_fr.py::_validate_download` via `stream.read`.
- property/attribute access: `src/landscout/sources/cadastre_loader_fr.py::_validate_download` via `stream.read`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_request_json` via `response.read`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_request_json` via `response.read`.
- direct call or construction: `src/landscout/sources/gpu_fr.py::_sha256` via `stream.read`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_sha256` via `stream.read`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` via `stream.read`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_calculate_checksums` via `stream.read`.
- direct call or construction: `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` via `stream.read`.
- property/attribute access: `src/landscout/sources/ign_bdtopo_fr.py::_geopackage_integrity` via `stream.read`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::_sha256_file` via `stream.read`.
- property/attribute access: `src/landscout/sources/inpn_protected_areas_fr.py::_sha256_file` via `stream.read`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_read_response_json` via `response.read`.
- property/attribute access: `src/landscout/sources/rte_odre_fr.py::_read_response_json` via `response.read`.
- direct call or construction: `src/landscout/sources/rte_odre_fr.py::_sha256` via `stream.read`.
- property/attribute access: `src/landscout/sources/rte_odre_fr.py::_sha256` via `stream.read`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_file_sha256` via `stream.read`.
- property/attribute access: `src/landscout/stages/index_planning_regulation.py::_file_sha256` via `stream.read`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, '_read_verified_artifact', read)`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_Response.iter_content` via `self.raw.read`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::_Response.iter_content` via `self.raw.read`.
- direct call or construction: `tests/unit/test_inpn_protected_areas_fr.py::_Response.read` via `self.raw.read`.
- property/attribute access: `tests/unit/test_inpn_protected_areas_fr.py::_Response.read` via `self.raw.read`.
- direct call or construction: `tests/unit/test_safe_http.py::_read` via `response.read`.
- property/attribute access: `tests/unit/test_safe_http.py::_read` via `response.read`.
- direct call or construction: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `response.read`.
- property/attribute access: `tests/unit/test_safe_http.py::test_safe_https_redirect_is_manually_revalidated` via `response.read`.

**Complete source-ordered implementation**

```python
def read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("artifact read must not run")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.build`

**Exact signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Constructs build; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `object`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('application rebuild must not run')`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, '_build_result', build)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, '_build_result', build)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(module, '_build_result', build)`.

**Complete source-ordered implementation**

```python
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.heavy`

**Exact signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for heavy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.

**Complete source-ordered implementation**

```python
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `empty_upstream`.

**Setup**

```python
_, coded, _, policy, result = _application_fixture()
manifest, paths, _ = _write_application_artifacts(tmp_path, result)
if empty_upstream in {"coded", "both"}:
        coded = _canonical_empty_coded_result(coded, empty_dictionary=True)
if empty_upstream in {"policy", "both"}:
        policy = _canonical_empty_policy_result(policy)
if empty_upstream == "both":
        policy_module = importlib.import_module(
            "landscout.stages.bess_planning_feature_policy"
        )
        policy = policy_module._result_with_hashes(
            replace(
                policy,
                cnig_complete_result_content_sha256=(
                    coded.complete_result_content_sha256
                ),
            )
        )
module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")
def artifact_read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("Parquet read must not run")
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
monkeypatch.setattr(Path, "read_text", manifest_read)
monkeypatch.setattr(module, "_read_verified_artifact", artifact_read)
monkeypatch.setattr(module, "_build_result", build)
monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="dictionary|policy|table|pair|empty|record|entry",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    empty_upstream: str,
) -> None:
    _, coded, _, policy, result = _application_fixture()
    manifest, paths, _ = _write_application_artifacts(tmp_path, result)
    if empty_upstream in {"coded", "both"}:
        coded = _canonical_empty_coded_result(coded, empty_dictionary=True)
    if empty_upstream in {"policy", "both"}:
        policy = _canonical_empty_policy_result(policy)
    if empty_upstream == "both":
        policy_module = importlib.import_module(
            "landscout.stages.bess_planning_feature_policy"
        )
        policy = policy_module._result_with_hashes(
            replace(
                policy,
                cnig_complete_result_content_sha256=(
                    coded.complete_result_content_sha256
                ),
            )
        )
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    calls = {"manifest": 0, "read": 0, "build": 0, "heavy": 0}

    def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")

    def artifact_read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("Parquet read must not run")

    def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")

    def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1

    monkeypatch.setattr(Path, "read_text", manifest_read)
    monkeypatch.setattr(module, "_read_verified_artifact", artifact_read)
    monkeypatch.setattr(module, "_build_result", build)
    monkeypatch.setattr(module, "validate_bess_planning_feature_policy_result", heavy)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="dictionary|policy|table|pair|empty|record|entry",
    ):
        module.load_bess_planning_feature_application_artifacts(
            manifest, *paths.values(), coded, policy
        )
    assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}
```

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.manifest_read`

**Exact signature**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
```

**Purpose**

Private `test` helper for manifest read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('manifest read must not run')`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(Path, 'read_text', manifest_read)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(Path, 'read_text', manifest_read)`.

**Complete source-ordered implementation**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.artifact_read`

**Exact signature**

```python
def artifact_read(*args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for artifact read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('Parquet read must not run')`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(module, '_read_verified_artifact', artifact_read)`.

**Complete source-ordered implementation**

```python
def artifact_read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("Parquet read must not run")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.build`

**Exact signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Constructs build; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `object`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('application rebuild must not run')`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, '_build_result', build)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, '_build_result', build)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(module, '_build_result', build)`.

**Complete source-ordered implementation**

```python
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.heavy`

**Exact signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for heavy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

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

- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', heavy)`.

**Complete source-ordered implementation**

```python
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.


## 7. Data contracts

### `POLICY_COLUMNS` — canonical or derived frame-column schema

```python
POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
```

### `BOUNDARY_FLAG_COLUMNS` — canonical or derived frame-column schema

```python
BOUNDARY_FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
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
