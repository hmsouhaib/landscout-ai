# `tests/unit/test_apply_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_apply_bess_planning_feature_policy.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.
- Source SHA256: `563c9382062de5406384bd574df5ca169dde642ae768102c4973bd8d9be68184`

## 1. STEP 7F.1A.4.1 contract delta

- Adds permanent nested-alias and immediate-mutation regressions for the application artifact record while retaining all prior application tests.
- Runtime trust objects are deeply immutable without removing any public reconstruction/revalidation boundary or changing business semantics.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `APPLICATION_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POLICY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_policy_application_status`
  - `bess_cnig_precheck_status`
  - `bess_cnig_precheck_confidence`
  - `bess_cnig_status_priority`
  - `bess_cnig_rationale`
  - `bess_cnig_required_human_action`
  - `bess_cnig_limitations`
  - `bess_cnig_application_scope`
  - `bess_cnig_policy_scope`
  - `bess_cnig_local_feature_text_interpreted`
  - `bess_cnig_local_regulation_content_interpreted`
  - `bess_cnig_legal_conclusion_produced`
  - `bess_cnig_parcel_status_aggregated`
  - `bess_cnig_parcel_rejection_performed`
  - `bess_cnig_score_calculated`
  - `bess_cnig_policy_profile`
  - `bess_cnig_policy_sha256`
  - `bess_cnig_policy_result_sha256`

### `BOUNDARY_FLAG_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_local_feature_text_interpreted`
  - `bess_cnig_local_regulation_content_interpreted`
  - `bess_cnig_legal_conclusion_produced`
  - `bess_cnig_parcel_status_aggregated`
  - `bess_cnig_parcel_rejection_performed`
  - `bess_cnig_score_calculated`

### `ARTIFACT_FILES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARTIFACT_FILES = {
    "SURFACE_FEATURES": ("surface.parquet", True),
    "LINE_FEATURES": ("line.parquet", True),
    "POINT_FEATURES": ("point.parquet", True),
    "RELATIONS": ("relations.parquet", False),
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `SURFACE_FEATURES`
  - `LINE_FEATURES`
  - `POINT_FEATURES`
  - `RELATIONS`

### `_LAST_CODED_RESULT`

- Category: module constant or closed domain.
- Exact declaration:

```python
_LAST_CODED_RESULT: object | None = None
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_LAST_POLICY_RESULT`

- Category: module constant or closed domain.
- Exact declaration:

```python
_LAST_POLICY_RESULT: object | None = None
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_application_fixture`

**Purpose:** Implements `application fixture` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[object, ...], object, object, object, BessPlanningFeatureApplicationResult]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `inputs, coded, config, policy, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_exact_policy_is_applied_to_every_feature_and_relation` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_exact_policy_is_applied_to_every_feature_and_relation` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_every_output_row_has_all_six_false_boundary_flags` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_every_output_row_has_all_six_false_boundary_flags` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_policy_suffix_has_one_exact_deterministic_dtype_schema` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_policy_suffix_has_one_exact_deterministic_dtype_schema` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_m_and_zm_application_geometries_are_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_m_and_zm_application_geometries_are_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_empty_optional_application_catalog_retains_schema_and_crs` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_empty_optional_application_catalog_retains_schema_and_crs` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_relations_inherit_only_from_referenced_enriched_feature` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_relations_inherit_only_from_referenced_enriched_feature` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_complete_relation_facts_must_match_referenced_feature` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_complete_relation_facts_must_match_referenced_feature` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_relation_feature_id_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_relation_feature_id_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_scope_has_no_parcel_output_aggregation_rejection_or_score` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_scope_has_no_parcel_output_aggregation_rejection_or_score` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_application_relation_pair_is_rejected_locally` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_application_relation_pair_is_rejected_locally` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_feature_id_is_exact_and_portable` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_feature_id_is_exact_and_portable` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_parcel_id_is_exact` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_parcel_id_is_exact` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_application_relation_type_is_rejected_locally` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_application_relation_type_is_rejected_locally` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_invalid_policy_domains_fail_local_validation` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_invalid_policy_domains_fail_local_validation` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_literal_null_replacements_are_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_literal_null_replacements_are_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_official_and_application_statuses_cannot_contradict` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_official_and_application_statuses_cannot_contradict` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_any_true_row_boundary_flag_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_any_true_row_boundary_flag_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_malformed_local_result_fast_fails_before_heavy_validation` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_malformed_local_result_fast_fails_before_heavy_validation` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_application_source_lock_mutation_fast_fails` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_application_source_lock_mutation_fast_fails` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_pair_artifact_fails_local_loading` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_pair_artifact_fails_local_loading` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_geometry_role_is_intrinsic` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_geometry_role_is_intrinsic` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_metric_must_match_geometry` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_metric_must_match_geometry` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_requires_canonical_crs_and_global_identity` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_requires_canonical_crs_and_global_identity` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_locks_policy_result_schema_exactly` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_locks_policy_result_schema_exactly` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_locks_cnig_result_schema_exactly` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_locks_cnig_result_schema_exactly` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_accepts_only_current_policy_and_cnig_source_schemas` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_accepts_only_current_policy_and_cnig_source_schemas` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_z_geoparquet_artifact_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_z_geoparquet_artifact_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_manifest_rejects_invalid_contract` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_manifest_rejects_invalid_contract` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_uses_strict_json_before_artifact_read` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_uses_strict_json_before_artifact_read` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_loader_parses_only_verified_bytes` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_loader_parses_only_verified_bytes` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_physical_replacement_before_loading_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_physical_replacement_before_loading_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_row_lineage_must_match_application_envelope` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_row_lineage_must_match_application_envelope` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_resolved_official_row_requires_label_and_envelope_profile` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_resolved_official_row_requires_label_and_envelope_profile` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_official_row_rejects_invented_label_or_url` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_official_row_rejects_invented_label_or_url` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_feature_prefix_has_exact_canonical_schema` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_feature_prefix_has_exact_canonical_schema` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_prefix_has_exact_canonical_schema` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_prefix_has_exact_canonical_schema` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_filenames_are_casefold_unique` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_filenames_are_casefold_unique` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_all_null_raw_column_transition` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_all_null_raw_column_transition` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_rejects_nonportable_filename` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_rejects_nonportable_filename` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_application_fixture`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `_application_fixture`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `_application_fixture`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `test_bess_planning_feature_policy._compiled_fixture` |
| `apply_bess_planning_feature_policy` | `landscout.stages.apply_bess_planning_feature_policy.apply_bess_planning_feature_policy` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `load_bess_planning_feature_application_artifacts`

**Purpose:** Test adapter supplying the newly mandatory exact upstream envelopes.

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

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `manifest_path` | positional-or-keyword | `str \| Path` | `required` |
| `surface_features_path` | positional-or-keyword | `str \| Path` | `required` |
| `line_features_path` | positional-or-keyword | `str \| Path` | `required` |
| `point_features_path` | positional-or-keyword | `str \| Path` | `required` |
| `relations_path` | positional-or-keyword | `str \| Path` | `required` |
| `coded_result` | positional-or-keyword | `object \| None` | `None` |
| `policy_result` | positional-or-keyword | `object \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_load_application_artifacts(<br>        manifest_path,<br>        surface_features_path,<br>        line_features_path,<br>        point_features_path,<br>        relations_path,<br>        coded_result,<br>        policy_result,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert coded_result is not None`
  - `assert policy_result is not None`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_pair_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_pair_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_z_geoparquet_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_z_geoparquet_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_manifest_rejects_invalid_contract` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_manifest_rejects_invalid_contract` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_uses_strict_json_before_artifact_read` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_uses_strict_json_before_artifact_read` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_loader_parses_only_verified_bytes` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_loader_parses_only_verified_bytes` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_physical_replacement_before_loading_is_rejected` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_physical_replacement_before_loading_is_rejected` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `load_bess_planning_feature_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_load_application_artifacts` | `landscout.stages.apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_small_catalog`

**Purpose:** Implements `small catalog` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _small_catalog(*rows: tuple[str, str, str, str, str]) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*rows` | variadic positional | `tuple[str, str, str, str, str]` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "planning_feature_id": [row[0] for row in rows],<br>            "feature_family": [row[1] for row in rows],<br>            "type_code_raw": [row[2] for row in rows],<br>            "subtype_code_raw": [row[3] for row in rows],<br>            "official_code_status": [row[4] for row in rows],<br>        },<br>        geometry=[Point(position, position) for position in range(len(rows))],<br>        crs="EPSG:2154",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct` via `_small_catalog`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct` via `_small_catalog`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_pair_remains_present_with_true_null_decision_fields` via `_small_catalog`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_pair_remains_present_with_true_null_decision_fields` via `_small_catalog`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_inconsistent_official_status_and_policy_match_is_rejected` via `_small_catalog`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_inconsistent_official_status_and_policy_match_is_rejected` via `_small_catalog`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Point` | `shapely.geometry.Point` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_application_artifacts`

**Purpose:** Implements `write application artifacts` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _write_application_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[Path, dict[str, Path], dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `manifest_path, paths, manifest`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert validated.schema_version == 2`
  - `assert module is not None`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_pair_artifact_fails_local_loading` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_pair_artifact_fails_local_loading` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_z_geoparquet_artifact_is_rejected` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_z_geoparquet_artifact_is_rejected` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_manifest_rejects_invalid_contract` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_manifest_rejects_invalid_contract` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_uses_strict_json_before_artifact_read` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_uses_strict_json_before_artifact_read` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_loader_parses_only_verified_bytes` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_loader_parses_only_verified_bytes` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_physical_replacement_before_loading_is_rejected` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_physical_replacement_before_loading_is_rejected` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_filenames_are_casefold_unique` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_filenames_are_casefold_unique` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_all_null_raw_column_transition` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_all_null_raw_column_transition` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_rejects_nonportable_filename` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_rejects_nonportable_filename` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_write_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `_write_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `_write_application_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `ARTIFACT_FILES.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `records.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(path.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `signature.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `fields` | `dataclasses.fields` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureApplicationArtifactManifest.model_validate` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.model_validate` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.stat`<br>`sha256(path.read_bytes()).hexdigest`<br>`path.read_bytes` |
| Filesystem/archive write or publication | `frame.to_parquet`<br>`manifest_path.write_text` |
| Hashing/byte identity | `sha256(path.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `paths[role] = path`<br>`records.append(<br>            {<br>                "artifact_role": role,<br>                "filename": filename,<br>                "row_count": len(frame),<br>                "size_bytes": path.stat().st_size,<br>                "sha256": sha256(path.read_bytes()).hexdigest(),<br>                "frame_schema_signature": signature,<br>                "geospatial": geospatial,<br>                "crs": signature.get("crs"),<br>            }<br>        )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_coordinated_policy_mutation`

**Purpose:** Implements `coordinated policy mutation` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |
| `dtype` | keyword-only | `str \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(replace(changed, relations=relation_frame))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_invalid_policy_domains_fail_local_validation` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_invalid_policy_domains_fail_local_validation` via `_coordinated_policy_mutation`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_literal_null_replacements_are_rejected` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_literal_null_replacements_are_rejected` via `_coordinated_policy_mutation`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `_coordinated_policy_mutation`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_official_and_application_statuses_cannot_contradict` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_official_and_application_statuses_cannot_contradict` via `_coordinated_policy_mutation`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_any_true_row_boundary_flag_is_rejected` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_any_true_row_boundary_flag_is_rejected` via `_coordinated_policy_mutation`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `_coordinated_policy_mutation`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `_coordinated_policy_mutation`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_coordinated_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `_coordinated_policy_mutation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr(changed, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `mask.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `mask.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `pd.Categorical` | `pandas.Categorical` |
| `replace` | `dataclasses.replace` |
| `changed.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_frame["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_frame[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_mask.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `values[position] = value`<br>`frame[column] = pd.Series(pd.Categorical(values), index=frame.index)`<br>`frame[column] = pd.Series(values, index=frame.index, dtype=dtype)`<br>`frame.loc[mask, column] = value`<br>`relation_values[position] = value`<br>`relation_frame[column] = pd.Series(<br>            pd.Categorical(relation_values), index=relation_frame.index<br>        )`<br>`relation_frame[column] = pd.Series(<br>            relation_values, index=relation_frame.index, dtype=dtype<br>        )`<br>`relation_frame.loc[relation_mask, column] = value` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_coordinated_feature_id_mutation`

**Purpose:** Implements `coordinated feature id mutation` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _coordinated_feature_id_mutation(
    result: BessPlanningFeatureApplicationResult,
    feature_id: object,
) -> BessPlanningFeatureApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |
| `feature_id` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(replace(changed, relations=relations))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_feature_id_is_exact_and_portable` via `_coordinated_feature_id_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_feature_id_is_exact_and_portable` via `_coordinated_feature_id_mutation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `getattr(changed, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `changed.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[frame["planning_feature_id"].eq(original), "planning_feature_id"] = (<br>            feature_id<br>        )`<br>`relations.loc[<br>        relations["planning_feature_id"].eq(original), "planning_feature_id"<br>    ] = feature_id` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_zero_relation_feature`

**Purpose:** Implements `zero relation feature` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _zero_relation_feature(
    result: BessPlanningFeatureApplicationResult,
) -> tuple[str, gpd.GeoDataFrame, object]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, gpd.GeoDataFrame, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `name, frame, unmatched.index[0]`
- Explicit raise paths:
  - `AssertionError("fixture must contain a feature having zero relations")`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_row_lineage_must_match_application_envelope` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_row_lineage_must_match_application_envelope` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_resolved_official_row_requires_label_and_envelope_profile` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_resolved_official_row_requires_label_and_envelope_profile` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_official_row_rejects_invented_label_or_url` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_official_row_rejects_invented_label_or_url` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `_zero_relation_feature`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_zero_relation_feature`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `_zero_relation_feature`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["planning_feature_id"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_surface_touch_with_positive_area`

**Purpose:** Implements `surface touch with positive area` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _surface_touch_with_positive_area(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(replace(result, relations=relations))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert relations.loc[index, "intersection_area_m2"] > 0`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_surface_touch_with_positive_area`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `_surface_touch_with_positive_area`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[index, "relation_type"] = "TOUCH_ONLY"` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_z_geometry`

**Purpose:** Implements `z geometry` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _z_geometry(kind: str) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "Polygon": polygon,<br>        "MultiPolygon": MultiPolygon([polygon]),<br>        "LineString": line,<br>        "MultiLineString": MultiLineString([line]),<br>        "Point": point,<br>        "MultiPoint": MultiPoint([point]),<br>    }[kind]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `_z_geometry`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `_z_geometry`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `MultiPoint` | `shapely.geometry.MultiPoint` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_policy_is_applied_to_every_feature_and_relation`

**Purpose:** Regression invariant: exact policy is applied to every feature and relation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_policy_is_applied_to_every_feature_and_relation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.result_hash_schema_version == 2`
  - `assert result.application_scope == APPLICATION_SCOPE`
  - `assert result.policy_profile == policy.policy_profile`
  - `assert result.policy_sha256 == policy.policy_sha256`
  - `assert result.policy_complete_result_content_sha256 == (<br>        policy.complete_result_content_sha256<br>    )`
  - `assert tuple(applied.columns[: len(source.columns)]) == tuple(source.columns)`
  - `assert (<br>            applied["bess_cnig_policy_application_status"]<br>            .eq("APPLIED_EXACT_POLICY")<br>            .all()<br>        )`
  - `assert row.bess_cnig_precheck_status == expected.precheck_status`
  - `assert row.bess_cnig_precheck_confidence == expected.confidence`
  - `assert row.bess_cnig_status_priority == expected.status_priority`
  - `assert row.bess_cnig_rationale == expected.rationale`
  - `assert row.bess_cnig_required_human_action == (<br>                expected.required_human_action<br>            )`
  - `assert row.bess_cnig_limitations == expected.limitations`
  - `assert (<br>        result.relations["bess_cnig_policy_application_status"]<br>        .eq("APPLIED_EXACT_POLICY")<br>        .all()<br>    )`
  - `assert policy_config.policy_scope == result.policy_scope`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `policy.policy_table.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `applied["bess_cnig_policy_application_status"]<br>            .eq("APPLIED_EXACT_POLICY")<br>            .all` | `unresolved local/third-party receiver; no ownership inferred` |
| `applied["bess_cnig_policy_application_status"]<br>            .eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `applied.itertuples` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations["bess_cnig_policy_application_status"]<br>        .eq("APPLIED_EXACT_POLICY")<br>        .all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations["bess_cnig_policy_application_status"]<br>        .eq` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_output_row_has_all_six_false_boundary_flags`

**Purpose:** Regression invariant: every output row has all six false boundary flags. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_output_row_has_all_six_false_boundary_flags() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert all(column in frame.columns for column in BOUNDARY_FLAG_COLUMNS)`
  - `assert str(frame[column].dtype) == "bool"`
  - `assert frame[column].notna().all()`
  - `assert frame[column].eq(False).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].notna().all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].notna` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].eq(False).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_suffix_has_one_exact_deterministic_dtype_schema`

**Purpose:** Regression invariant: policy suffix has one exact deterministic dtype schema. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_suffix_has_one_exact_deterministic_dtype_schema() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(frame.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS`
  - `assert {column: str(frame[column].dtype) for column in POLICY_COLUMNS} == (<br>            expected<br>        )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `expected.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `expected["bess_cnig_status_priority"] = "Int64"`<br>`expected.update({column: "bool" for column in BOUNDARY_FLAG_COLUMNS})` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v1_dimension_blind_hash_representation_is_rejected_locally`

**Purpose:** Regression invariant: schema v1 dimension blind hash representation is rejected locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v1_dimension_blind_hash_representation_is_rejected_locally() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension")`
- Exact assertions:
  - `assert get_coordinate_dimension(original) == 2`
  - `assert get_coordinate_dimension(polygon_z) == 3`
  - `assert to_wkb(original, hex=True, output_dimension=2) == to_wkb(<br>        polygon_z, hex=True, output_dimension=2<br>    )`
  - `assert blind.surface_features_content_sha256 == (<br>        result.surface_features_content_sha256<br>    )`
  - `assert blind.complete_result_content_sha256 == result.complete_result_content_sha256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `Polygon` | `shapely.geometry.Polygon` |
| `get_coordinate_dimension` | `shapely.get_coordinate_dimension` |
| `to_wkb` | `shapely.to_wkb` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | `to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | `surface.at[surface.index[0], surface.geometry.name] = polygon_z` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`

**Purpose:** Regression invariant: every non 2d application geometry kind fast fails before source validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
    frame_name: str,
    geometry_kind: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("frame_name", "geometry_kind"),
    [
        ("surface_features", "Polygon"),
        ("surface_features", "MultiPolygon"),
        ("line_features", "LineString"),
        ("line_features", "MultiLineString"),
        ("point_features", "Point"),
        ("point_features", "MultiPoint"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `frame_name` | positional-or-keyword | `str` | `required` |
| `geometry_kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension")`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `getattr(result, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_z_geometry` | `tests.unit.test_apply_bess_planning_feature_policy._z_geometry` |
| `replace` | `dataclasses.replace` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_application_result` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_z_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | `frame.at[frame.index[0], frame.geometry.name] = _z_geometry(geometry_kind)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_m_and_zm_application_geometries_are_rejected`

**Purpose:** Regression invariant: m and zm application geometries are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_m_and_zm_application_geometries_are_rejected(wkt: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("wkt", ["POINT M (1 1 7)", "POINT ZM (1 1 7 8)"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `wkt` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.point_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `from_wkt` | `shapely.from_wkt` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `point.at[point.index[0], point.geometry.name] = from_wkt(wkt)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_empty_optional_application_catalog_retains_schema_and_crs`

**Purpose:** Regression invariant: valid empty optional application catalog retains schema and crs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_empty_optional_application_catalog_retains_schema_and_crs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert applied.empty`
  - `assert tuple(applied.columns[: len(empty.columns)]) == tuple(empty.columns)`
  - `assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS`
  - `assert applied.geometry.name == empty.geometry.name`
  - `assert applied.crs == empty.crs`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `coded.point_features.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._apply_feature_catalog` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._validate_application_geometry` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `module._validate_application_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`

**Purpose:** Regression invariant: exact pair identity keeps family subtype and leading zeroes distinct. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert applied.loc[0, "bess_cnig_precheck_confidence"] == "MEDIUM"`
  - `assert applied.loc[1, "bess_cnig_precheck_confidence"] == "HIGH"`
  - `assert applied.loc[0, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"`
  - `assert applied.loc[1, "bess_cnig_precheck_status"] == "DESIGN_REVIEW_REQUIRED"`
  - `assert applied.loc[2, "bess_cnig_policy_application_status"] == (<br>        "UNRESOLVED_CODE_PAIR"<br>    )`
  - `assert applied.loc[3, "bess_cnig_policy_application_status"] == (<br>        "UNRESOLVED_CODE_PAIR"<br>    )`
  - `assert applied.loc[4, "type_code_raw"] == "01"`
  - `assert applied.loc[4, "subtype_code_raw"] == "00"`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_checked_in_policy_result` | `test_bess_planning_feature_policy._checked_in_policy_result` |
| `_small_catalog` | `tests.unit.test_apply_bess_planning_feature_policy._small_catalog` |
| `module._apply_feature_catalog` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_pair_remains_present_with_true_null_decision_fields`

**Purpose:** Regression invariant: unknown pair remains present with true null decision fields. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_pair_remains_present_with_true_null_decision_fields() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert applied["planning_feature_id"].tolist() == ["F-UNKNOWN"]`
  - `assert applied.loc[0, "bess_cnig_policy_application_status"] == (<br>        "UNRESOLVED_CODE_PAIR"<br>    )`
  - `assert pd.isna(applied.loc[0, column])`
  - `assert not isinstance(applied.loc[0, column], str)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_checked_in_policy_result` | `test_bess_planning_feature_policy._checked_in_policy_result` |
| `_small_catalog` | `tests.unit.test_apply_bess_planning_feature_policy._small_catalog` |
| `module._apply_feature_catalog` | `unresolved local/third-party receiver; no ownership inferred` |
| `applied["planning_feature_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inconsistent_official_status_and_policy_match_is_rejected`

**Purpose:** Regression invariant: inconsistent official status and policy match is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "row",
    [
        ("F-MISSING", "PRESCRIPTION", "98", "00", "RESOLVED_OFFICIAL"),
        ("F-UNEXPECTED", "PRESCRIPTION", "15", "00", "UNKNOWN_CODE_PAIR"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `tuple[str, str, str, str, str]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="policy\|official")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `pytest.raises` | `pytest.raises` |
| `module._apply_feature_catalog` | `unresolved local/third-party receiver; no ownership inferred` |
| `_small_catalog` | `tests.unit.test_apply_bess_planning_feature_policy._small_catalog` |
| `_checked_in_policy_result` | `test_bess_planning_feature_policy._checked_in_policy_result` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy|official"):
        module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_feature_and_relation_inputs_are_preserved_and_not_mutated`

**Purpose:** Regression invariant: feature and relation inputs are preserved and not mutated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_feature_and_relation_inputs_are_preserved_and_not_mutated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(applied.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS`
  - `assert type(applied.index) is type(source.index)`
  - `assert applied.index.equals(source.index)`
  - `assert tuple(result.relations.columns[-len(POLICY_COLUMNS) :]) == POLICY_COLUMNS`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `test_bess_planning_feature_policy._compiled_fixture` |
| `coded.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded.line_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded.point_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `inputs[1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `apply_bess_planning_feature_policy` | `landscout.stages.apply_bess_planning_feature_policy.apply_bess_planning_feature_policy` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `applied.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relations_inherit_only_from_referenced_enriched_feature`

**Purpose:** Regression invariant: relations inherit only from referenced enriched feature. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relations_inherit_only_from_referenced_enriched_feature() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert getattr(relation, column) == feature[column]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `pd.concat(<br>        [<br>            result.surface_features.drop(columns="geometry"),<br>            result.line_features.drop(columns="geometry"),<br>            result.point_features.drop(columns="geometry"),<br>        ],<br>        ignore_index=True,<br>    ).set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `result.surface_features.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.line_features.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.point_features.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.itertuples` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `pd.concat(<br>        [<br>            result.surface_features.drop(columns="geometry"),<br>            result.line_features.drop(columns="geometry"),<br>            result.point_features.drop(columns="geometry"),<br>        ],<br>        ignore_index=True,<br>    ).set_index` |
| External process/environment | None directly present. |
| In-memory mutation | `result.surface_features.drop(columns="geometry")`<br>`result.line_features.drop(columns="geometry")`<br>`result.point_features.drop(columns="geometry")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_relation_facts_must_match_referenced_feature`

**Purpose:** Regression invariant: complete relation facts must match referenced feature. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_complete_relation_facts_must_match_referenced_feature(
    column: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_feature_id", "MUTATED"),
        ("source_identity_kind", "MUTATED"),
        ("source_identity_field", "MUTATED"),
        ("logical_layer", "information_surface"),
        ("label_raw", "MUTATED"),
        ("text_raw", "MUTATED"),
        ("source_document_id", "MUTATED"),
        ("source_archive_sha256", "f" * 64),
        ("source_layer", "MUTATED"),
        ("source_validity_date_raw", "2099-01-01"),
        ("regulation_filename_raw", "MUTATED.pdf"),
        ("official_code_label", "MUTATED"),
        ("official_code_profile", "MUTATED"),
        ("feature_area_m2", 999.0),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="relation\|feature")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_relation_feature_id_is_rejected`

**Purpose:** Regression invariant: unknown relation feature id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="feature ID")`
- Exact assertions:
  - `assert policy is not None`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `coded.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module._apply_relations` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `relations.loc[relations.index[0], "planning_feature_id"] = "GPU:UNKNOWN"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_scope_has_no_parcel_output_aggregation_rejection_or_score`

**Purpose:** Regression invariant: scope has no parcel output aggregation rejection or score. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_scope_has_no_parcel_output_aggregation_rejection_or_score() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert not hasattr(result, "parcels")`
  - `assert result.local_feature_text_interpreted is False`
  - `assert result.local_regulation_content_interpreted is False`
  - `assert result.legal_conclusion_produced is False`
  - `assert result.parcel_status_aggregated is False`
  - `assert result.parcel_rejection_performed is False`
  - `assert result.score_calculated is False`
  - `assert "parcel_id" not in result.surface_features.columns`
  - `assert len(inputs[1]) > 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_feature_or_relation_policy_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated feature or relation policy mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_feature_or_relation_policy_mutation_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="rebuilt\|feature")`
  - `pytest.raises(BessPlanningFeatureApplicationError, match="relation\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_application_result` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], "bess_cnig_precheck_status"] = "UNKNOWN"`<br>`relations.loc[relations.index[0], "bess_cnig_precheck_confidence"] = "LOW"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_application_relation_pair_is_rejected_locally`

**Purpose:** Regression invariant: duplicate application relation pair is rejected locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_application_relation_pair_is_rejected_locally() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="duplicate\|unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `pd.concat` | `pandas.concat` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_relation_feature_id_is_exact_and_portable`

**Purpose:** Regression invariant: application relation feature id is exact and portable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_relation_feature_id_is_exact_and_portable(
    feature_id: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature", r"C:\feature", " GPU:F "],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `feature_id` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="feature\|identity")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_feature_id_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_feature_id_mutation` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_relation_parcel_id_is_exact`

**Purpose:** Regression invariant: application relation parcel id is exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_relation_parcel_id_is_exact(parcel_id: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("parcel_id", [None, "", "None", " PARCEL-1 "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_id` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="parcel\|identity")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[relations.index[0], "parcel_id"] = parcel_id` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_application_relation_type_is_rejected_locally`

**Purpose:** Regression invariant: unknown application relation type is rejected locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_application_relation_type_is_rejected_locally() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="relation type")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[relations.index[0], "relation_type"] = "BUFFERED_NEARBY"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_invalid_policy_domains_fail_local_validation`

**Purpose:** Regression invariant: coordinated invalid policy domains fail local validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_invalid_policy_domains_fail_local_validation(
    column: str,
    value: object,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("bess_cnig_precheck_status", "AUTHORIZED", "status|domain"),
        ("bess_cnig_precheck_status", "FORBIDDEN", "status|domain"),
        ("bess_cnig_precheck_status", "PROHIBITED", "status|domain"),
        ("bess_cnig_precheck_confidence", "CERTAIN", "confidence|domain"),
        ("bess_cnig_status_priority", 0, "priority|positive"),
        ("bess_cnig_status_priority", -1, "priority|positive"),
        ("bess_cnig_rationale", "", "rationale|exact|non-empty"),
        ("bess_cnig_rationale", " leading", "rationale|exact|whitespace"),
        ("bess_cnig_required_human_action", "trailing ", "action|exact|whitespace"),
        ("bess_cnig_limitations", "", "limitations|exact|non-empty"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_literal_null_replacements_are_rejected`

**Purpose:** Regression invariant: literal null replacements are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_literal_null_replacements_are_rejected(literal: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("literal", ["None", "nan", "<NA>"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `literal` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="literal\|missing")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_literal_null_replacements_are_rejected(literal: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, "bess_cnig_rationale", literal)
    with pytest.raises(BessPlanningFeatureApplicationError, match="literal|missing"):
        module._validate_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_self_consistent_wrong_policy_suffix_dtype_is_rejected`

**Purpose:** Regression invariant: self consistent wrong policy suffix dtype is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_self_consistent_wrong_policy_suffix_dtype_is_rejected(
    column: str,
    dtype: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "dtype", "value"),
    [
        ("bess_cnig_precheck_status", "object", "UNKNOWN"),
        ("bess_cnig_precheck_confidence", "category", "HIGH"),
        ("bess_cnig_rationale", "object", "Still a factual policy rationale."),
        ("bess_cnig_status_priority", "Float64", 1.0),
        ("bess_cnig_status_priority", "str", "1"),
        ("bess_cnig_parcel_status_aggregated", "boolean", False),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `dtype` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="dtype\|schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_official_and_application_statuses_cannot_contradict`

**Purpose:** Regression invariant: official and application statuses cannot contradict. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_official_and_application_statuses_cannot_contradict(
    official_status: str,
    application_status: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("official_status", "application_status"),
    [
        ("RESOLVED_OFFICIAL", "UNRESOLVED_CODE_PAIR"),
        ("UNKNOWN_CODE_PAIR", "APPLIED_EXACT_POLICY"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `official_status` | positional-or-keyword | `str` | `required` |
| `application_status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="official\|status")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr(changed, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `mask.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `changed.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_frame["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[mask, "official_code_status"] = official_status`<br>`relation_frame.loc[<br>        relation_frame["planning_feature_id"].eq(feature_id), "official_code_status"<br>    ] = official_status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_any_true_row_boundary_flag_is_rejected`

**Purpose:** Regression invariant: any true row boundary flag is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", BOUNDARY_FLAG_COLUMNS)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="flag\|false")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, True)
    with pytest.raises(BessPlanningFeatureApplicationError, match="flag|false"):
        module._validate_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_and_public_validator_heavy_validation_counts`

**Purpose:** Regression invariant: application and public validator heavy validation counts. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_and_public_validator_heavy_validation_counts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert calls == 1`
  - `assert calls == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `test_bess_planning_feature_policy._compiled_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.apply_bess_planning_feature_policy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.validate_bess_planning_feature_application_result` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_and_public_validator_heavy_validation_counts.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual` | `unresolved local/third-party receiver; no ownership inferred` |

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
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_local_result_fast_fails_before_heavy_validation`

**Purpose:** Regression invariant: malformed local result fast fails before heavy validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_local_result_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError, match="hash\|SHA\|sha256\|invalid"<br>    )`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_application_result` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_local_result_fast_fails_before_heavy_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_application_source_lock_mutation_fast_fails`

**Purpose:** Regression invariant: coordinated application source lock mutation fast fails. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_application_source_lock_mutation_fast_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="source lock")`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `replace` | `dataclasses.replace` |
| `getattr(changed, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `changed.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_application_result` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame["bess_cnig_policy_sha256"] = pd.array(<br>            ["f" * 64] * len(frame), dtype="str"<br>        )`<br>`relation_frame["bess_cnig_policy_sha256"] = pd.array(<br>        ["f" * 64] * len(relation_frame), dtype="str"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_application_source_lock_mutation_fast_fails.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_four_file_manifest_and_verified_byte_readback`

**Purpose:** Regression invariant: valid four file manifest and verified byte readback. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_four_file_manifest_and_verified_byte_readback(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `validate_bess_planning_feature_application_result` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_relation_pair_artifact_fails_local_loading`

**Purpose:** Regression invariant: duplicate relation pair artifact fails local loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_relation_pair_artifact_fails_local_loading(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="duplicate\|unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `pd.concat` | `pandas.concat` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_document_wide_mapping_conflict_artifact_fails_local_loading`

**Purpose:** Regression invariant: document wide mapping conflict artifact fails local loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_document_wide_mapping_conflict_artifact_fails_local_loading(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="priority\|mapping")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.relations["bess_cnig_precheck_status"].ne` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`

**Purpose:** Regression invariant: positive surface overlap cannot be relabelled touch only in artifact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError, match="surface\|metric\|type"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_surface_touch_with_positive_area` | `tests.unit.test_apply_bess_planning_feature_policy._surface_touch_with_positive_area` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Purpose:** Regression invariant: wrong 2d feature geometry fails local artifact loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_2d_feature_geometry_fails_local_artifact_loading(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="surface\|geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `Point` | `shapely.geometry.Point` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.at[surface.index[0], surface.geometry.name] = Point(0, 0)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_feature_catalog_geometry_role_is_intrinsic`

**Purpose:** Regression invariant: feature catalog geometry role is intrinsic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_feature_catalog_geometry_role_is_intrinsic(
    frame_name: str, geometry: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("frame_name", "geometry"),
    [
        ("surface_features", Point(0, 0)),
        ("line_features", Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])),
        ("point_features", LineString([(0, 0), (1, 1)])),
        ("surface_features", Polygon()),
        (
            "surface_features",
            Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        ),
    ],
    ids=["surface-point", "line-polygon", "point-line", "empty", "invalid"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame_name` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `getattr(result, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Point` | `shapely.geometry.Point` |
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.at[frame.index[0], frame.geometry.name] = geometry` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_feature_catalog_metric_must_match_geometry`

**Purpose:** Regression invariant: feature catalog metric must match geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_feature_catalog_metric_must_match_geometry(
    frame_name: str, metric: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("frame_name", "metric"),
    [
        ("surface_features", "feature_area_m2"),
        ("line_features", "feature_length_m"),
        ("point_features", "point_member_count"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame_name` | positional-or-keyword | `str` | `required` |
| `metric` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError, match="metric\|geometry\|count"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `getattr(result, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[frame.index[0], metric] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unreferenced_feature_catalog_identity_fields_are_intrinsic`

**Purpose:** Regression invariant: unreferenced feature catalog identity fields are intrinsic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unreferenced_feature_catalog_identity_fields_are_intrinsic(
    column: str, value: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_id", "GPU:malformed"),
        ("logical_layer", "prescription_line"),
        ("geometry_kind", "LINE"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError, match="identity\|layer\|kind"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_feature_catalog_requires_canonical_crs_and_global_identity`

**Purpose:** Regression invariant: feature catalog requires canonical crs and global identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_feature_catalog_requires_canonical_crs_and_global_identity() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="EPSG:2154\|CRS")`
  - `pytest.raises(BessPlanningFeatureApplicationError, match="identity\|unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.surface_features.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `result.point_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | `result.surface_features.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `point.loc[point.index[0], "planning_feature_id"] = result.surface_features.iloc[0][<br>        "planning_feature_id"<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unreferenced_feature_identity_is_validated_locally`

**Purpose:** Regression invariant: unreferenced feature identity is validated locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unreferenced_feature_identity_is_validated_locally(
    tmp_path: Path, feature_id: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("feature_id", ["None", "/tmp/feature", r"C:\feature", " bad "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `feature_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError, match="feature\|identity\|GPU"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[index, "planning_feature_id"] = feature_id` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unreferenced_feature_participates_in_global_policy_mapping`

**Purpose:** Regression invariant: unreferenced feature participates in global policy mapping. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unreferenced_feature_participates_in_global_policy_mapping(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="priority\|mapping")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `conflicting["bess_cnig_precheck_status"].ne` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[index, "bess_cnig_status_priority"] = int(<br>        conflicting.iloc[0]["bess_cnig_status_priority"]<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_locks_policy_result_schema_exactly`

**Purpose:** Regression invariant: application locks policy result schema exactly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_locks_policy_result_schema_exactly(policy_schema: int) -> None:
```

- Exact decorators: `pytest.mark.parametrize("policy_schema", [0, 2, 999])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy_schema` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="policy.*schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_locks_cnig_result_schema_exactly`

**Purpose:** Regression invariant: application locks cnig result schema exactly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_locks_cnig_result_schema_exactly(cnig_schema: int) -> None:
```

- Exact decorators: `pytest.mark.parametrize("cnig_schema", [1, 4, 6, 999])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `cnig_schema` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="CNIG\|cnig.*schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_accepts_only_current_policy_and_cnig_source_schemas`

**Purpose:** Regression invariant: application accepts only current policy and cnig source schemas. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.policy_result_hash_schema_version == 1`
  - `assert result.cnig_result_hash_schema_version == 5`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    assert result.policy_result_hash_schema_version == 1
    assert result.cnig_result_hash_schema_version == 5
    module._validate_result_envelope(result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_relation_identity_fast_fails_before_policy_source_validation`

**Purpose:** Regression invariant: duplicate relation identity fast fails before policy source validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_relation_identity_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="duplicate\|unique")`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `pd.concat` | `pandas.concat` |
| `pd.Index` | `pandas.Index` |
| `relations.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_application_result` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_relation_identity_fast_fails_before_policy_source_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_self_consistent_z_geoparquet_artifact_is_rejected`

**Purpose:** Regression invariant: self consistent z geoparquet artifact is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_self_consistent_z_geoparquet_artifact_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `Polygon` | `shapely.geometry.Polygon` |
| `replace` | `dataclasses.replace` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

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
| In-memory mutation | `surface.at[surface.index[0], surface.geometry.name] = Polygon(<br>        [(x, y, 9) for x, y in original.exterior.coords]<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_self_consistent_wrong_dtype_artifact_is_rejected`

**Purpose:** Regression invariant: self consistent wrong dtype artifact is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_self_consistent_wrong_dtype_artifact_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="dtype\|schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_manifest_rejects_invalid_contract`

**Purpose:** Regression invariant: artifact manifest rejects invalid contract. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_manifest_rejects_invalid_contract(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
        (lambda value: value["artifacts"].pop(), "role|artifact"),
        (
            lambda value: value["artifacts"].append(
                {**value["artifacts"][0], "artifact_role": "EXTRA"}
            ),
            "role|artifact",
        ),
        (
            lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
            "duplicate|role|artifact",
        ),
        (
            lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
            "filename",
        ),
        (
            lambda value: value["artifacts"][1].update(
                filename=value["artifacts"][0]["filename"]
            ),
            "duplicate|filename",
        ),
        (
            lambda value: value["artifacts"][0].update(
                filename="C:/absolute/surface.parquet"
            ),
            "filename",
        ),
        (lambda value: value["artifacts"][0].update(size_bytes=1), "size"),
        (lambda value: value["artifacts"][0].update(sha256="f" * 64), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(sha256="bad"), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(row_count=999), "row"),
        (
            lambda value: value["artifacts"][0]["frame_schema_signature"].update(
                index_names=["wrong"]
            ),
            "schema",
        ),
        (lambda value: value["artifacts"][0].update(crs={"wrong": True}), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(crs=None), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(geospatial=False), "geospatial"),
        (lambda value: value.update(unknown=True), "manifest|artifact"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match=message)`
- Exact assertions:
  - `assert callable(mutation)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `callable` | `unresolved local/third-party receiver; no ownership inferred` |
| `mutation` | `unresolved local/third-party receiver; no ownership inferred` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `manifest_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_manifest_uses_strict_json_before_artifact_read`

**Purpose:** Regression invariant: application manifest uses strict json before artifact read. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "document",
    [
        '{"schema_version": 2, "schema_version": 2}\n',
        '{"schema_version": NaN}\n',
        '{"schema_version": Infinity}\n',
        "[]\n",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `document` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError,<br>        match="Duplicate JSON\|finite\|top-level\|invalid",<br>    )`
- Exact assertions:
  - `assert artifact_reads == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `manifest_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_application_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    artifact_reads = 0
    original_read_bytes = Path.read_bytes

    def counted_bytes(path: Path) -> bytes:
        nonlocal artifact_reads
        if path in paths.values():
            artifact_reads += 1
        return original_read_bytes(path)

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal artifact_reads
        artifact_reads += 1
        raise AssertionError("Artifact read preceded strict manifest validation")

    monkeypatch.setattr(Path, "read_bytes", counted_bytes)
    monkeypatch.setattr(module.pd, "read_parquet", counted)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
    assert artifact_reads == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_manifest_uses_strict_json_before_artifact_read.counted_bytes`

**Purpose:** Implements `counted bytes` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted_bytes(path: Path) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_read_bytes(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def counted_bytes(path: Path) -> bytes:
        nonlocal artifact_reads
        if path in paths.values():
            artifact_reads += 1
        return original_read_bytes(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_manifest_uses_strict_json_before_artifact_read.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("Artifact read preceded strict manifest validation")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def counted(*args: object, **kwargs: object) -> object:
        nonlocal artifact_reads
        artifact_reads += 1
        raise AssertionError("Artifact read preceded strict manifest validation")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_parses_only_verified_bytes`

**Purpose:** Regression invariant: artifact loader parses only verified bytes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_loader_parses_only_verified_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert replaced`
  - `assert ("buffer", verified) in observed`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `result.relations.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read_bytes` |
| Filesystem/archive write or publication | `result.relations.to_parquet` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_parses_only_verified_bytes.replace_after_read`

**Purpose:** Implements `replace after read` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def replace_after_read(path: Path) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read_bytes` |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_parses_only_verified_bytes.observed_read`

**Purpose:** Implements `observed read` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def observed_read(source: object, *args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source` | positional-or-keyword | `object` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_read_parquet(source, *args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `observed.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `source.getvalue` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_read_parquet` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read_parquet` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `observed.append(("buffer", source.getvalue()))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def observed_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(("buffer", source.getvalue()))
        return original_read_parquet(source, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_physical_replacement_before_loading_is_rejected`

**Purpose:** Regression invariant: physical replacement before loading is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_physical_replacement_before_loading_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="size\|SHA\|hash")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `paths["RELATIONS"].write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths["RELATIONS"].read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `paths["RELATIONS"].read_bytes` |
| Filesystem/archive write or publication | `paths["RELATIONS"].write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_application_api_exports_only_stable_symbols`

**Purpose:** Regression invariant: public application api exports only stable symbols. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_application_api_exports_only_stable_symbols() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert set(module.__all__) == required`
  - `assert required.issubset(set(stages.__all__))`
  - `assert not any(name.startswith("_") for name in module.__all__)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `name.startswith` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_replace_application_frame`

**Purpose:** Implements `replace application frame` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |
| `frame_name` | positional-or-keyword | `str` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(replace(result, **{frame_name: frame}))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `_replace_application_frame`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_row_lineage_must_match_application_envelope` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_row_lineage_must_match_application_envelope` via `_replace_application_frame`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_resolved_official_row_requires_label_and_envelope_profile` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_resolved_official_row_requires_label_and_envelope_profile` via `_replace_application_frame`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_official_row_rejects_invented_label_or_url` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_official_row_rejects_invented_label_or_url` via `_replace_application_frame`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_feature_prefix_has_exact_canonical_schema` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_feature_prefix_has_exact_canonical_schema` via `_replace_application_frame`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_prefix_has_exact_canonical_schema` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_prefix_has_exact_canonical_schema` via `_replace_application_frame`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `_replace_application_frame`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `_replace_application_frame`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `_replace_application_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_coordinated_referenced_lineage_mutation`

**Purpose:** Implements `coordinated referenced lineage mutation` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |
| `rename_id` | keyword-only | `bool` | `False` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(replace(changed, relations=relations))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `_coordinated_referenced_lineage_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `_coordinated_referenced_lineage_mutation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr(changed, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `mask.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `changed.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[mask, column] = value`<br>`frame.loc[mask, "planning_feature_id"] = replacement_id`<br>`relations.loc[mask, column] = value`<br>`relations.loc[mask, "planning_feature_id"] = replacement_id` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`

**Purpose:** Regression invariant: unreferenced feature document lineage is bound to envelope artifact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="document\|lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

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
| In-memory mutation | `frame.loc[index, "source_document_id"] = "MUTATED-DOCUMENT"`<br>`frame.loc[index, "planning_feature_id"] = (<br>        f"GPU:MUTATED-DOCUMENT:{frame.loc[index, 'logical_layer']}:"<br>        f"{frame.loc[index, 'source_feature_id']}"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_feature_row_lineage_must_match_application_envelope`

**Purpose:** Regression invariant: feature row lineage must match application envelope. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_feature_row_lineage_must_match_application_envelope(mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    ["archive", "official-profile", "envelope-document"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="lineage\|document")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[index, "source_archive_sha256"] = "f" * 64`<br>`frame.loc[index, "official_code_profile"] = "mutated_profile"`<br>`frame.loc[index, "official_code_profile_sha256"] = "f" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_referenced_row_lineage_cannot_bypass_envelope`

**Purpose:** Regression invariant: coordinated referenced row lineage cannot bypass envelope. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_referenced_row_lineage_cannot_bypass_envelope(
    column: str,
    value: str,
    rename_id: bool,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value", "rename_id"),
    [
        ("source_document_id", "MUTATED-DOCUMENT", True),
        ("source_archive_sha256", "f" * 64, False),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |
| `rename_id` | positional-or-keyword | `bool` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="lineage\|document")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_coordinated_referenced_lineage_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_referenced_lineage_mutation` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_resolved_official_row_requires_label_and_envelope_profile`

**Purpose:** Regression invariant: resolved official row requires label and envelope profile. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_resolved_official_row_requires_label_and_envelope_profile() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>            BessPlanningFeatureApplicationError, match="official\|profile\|label"<br>        )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `frame.loc[index, column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_official_row_rejects_invented_label_or_url`

**Purpose:** Regression invariant: unknown official row rejects invented label or url. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_official_row_rejects_invented_label_or_url() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="official\|null")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `frame.loc[index, "official_code_status"] = "UNKNOWN_CODE_PAIR"`<br>`frame.loc[index, "bess_cnig_policy_application_status"] = "UNRESOLVED_CODE_PAIR"`<br>`frame.loc[index, column] = pd.NA`<br>`frame.loc[index, "bess_cnig_status_priority"] = pd.NA`<br>`frame.loc[index, invented_column] = (<br>            "Invented label"<br>            if invented_column == "official_code_label"<br>            else "https://example.invalid/invented"<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_feature_prefix_has_exact_canonical_schema`

**Purpose:** Regression invariant: application feature prefix has exact canonical schema. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_feature_prefix_has_exact_canonical_schema(
    frame_name: str,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("frame_name", "mutation"),
    [
        ("surface_features", "missing-column"),
        ("surface_features", "unexpected-column"),
        ("surface_features", "reordered-columns"),
        ("surface_features", "metric-object"),
        ("line_features", "metric-object"),
        ("point_features", "metric-object"),
        ("surface_features", "official-object"),
        ("surface_features", "index-name"),
        ("surface_features", "index-dtype"),
        ("point_features", "malformed-empty"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame_name` | positional-or-keyword | `str` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="schema\|dtype\|index")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `getattr(result, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.get_loc` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.insert` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `frame[metric].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["official_legal_reference"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.index.rename` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `frame.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `frame.drop(columns="regulation_url_raw")`<br>`frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))`<br>`frame[metric] = pd.Series(<br>            frame[metric].tolist(), index=frame.index, dtype="object"<br>        )`<br>`frame["official_legal_reference"] = pd.Series(<br>            frame["official_legal_reference"].tolist(),<br>            index=frame.index,<br>            dtype="object",<br>        )`<br>`frame.index = frame.index.rename("wrong")`<br>`frame.index.rename("wrong")`<br>`frame.index = pd.Index(frame.index.to_numpy(dtype="int32"), dtype="int32")`<br>`frame["point_member_count"] = pd.Series(dtype="object")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_relation_prefix_has_exact_canonical_schema`

**Purpose:** Regression invariant: application relation prefix has exact canonical schema. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_relation_prefix_has_exact_canonical_schema(
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        "missing-column",
        "unexpected-column",
        "reordered-columns",
        "float-object",
        "count-object",
        "official-category",
        "malformed-empty",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="schema\|dtype")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.get_loc` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.insert` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `frame["intersection_area_m2"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["point_member_count"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Categorical` | `pandas.Categorical` |
| `frame.iloc[0:0].drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `frame.drop(columns="label_raw")`<br>`frame.insert(position, "unexpected_factual", pd.array(["x"] * len(frame)))`<br>`frame["intersection_area_m2"] = pd.Series(<br>            frame["intersection_area_m2"].tolist(), index=frame.index, dtype="object"<br>        )`<br>`frame["point_member_count"] = pd.Series(<br>            frame["point_member_count"].tolist(), index=frame.index, dtype="object"<br>        )`<br>`frame["official_code_label"] = pd.Series(<br>            pd.Categorical(frame["official_code_label"]), index=frame.index<br>        )`<br>`frame.iloc[0:0].drop(columns="label_raw")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_self_consistent_factual_prefix_dtype_artifact_is_rejected`

**Purpose:** Regression invariant: self consistent factual prefix dtype artifact is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_self_consistent_factual_prefix_dtype_artifact_is_rejected(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="schema\|dtype")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `surface["feature_area_m2"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |

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
| In-memory mutation | `surface["feature_area_m2"] = pd.Series(<br>        surface["feature_area_m2"].tolist(), index=surface.index, dtype="object"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_lineage_defect_fast_fails_before_policy_source_validation`

**Purpose:** Regression invariant: lineage defect fast fails before policy source validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_lineage_defect_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError)`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_replace_application_frame` | `tests.unit.test_apply_bess_planning_feature_policy._replace_application_frame` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_application_result` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result` |

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
| In-memory mutation | `frame.loc[index, "source_archive_sha256"] = "f" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_lineage_defect_fast_fails_before_policy_source_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams`

**Purpose:** Regression invariant: step 7d 5b 2b 5 application loader requires exact upstreams. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="hash\|invalid")`
- Exact assertions:
  - `assert tuple(<br>        inspect.signature(<br>            module.load_bess_planning_feature_application_artifacts<br>        ).parameters<br>    ) == (<br>        "manifest_path",<br>        "surface_features_path",<br>        "line_features_path",<br>        "point_features_path",<br>        "relations_path",<br>        "coded_result",<br>        "policy_result",<br>    )`
  - `assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `inspect.signature` | `inspect.signature` |
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `module.validate_bess_planning_feature_application_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `replace` | `dataclasses.replace` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_application_loader_rejects_locally_valid_rationale_change`

**Purpose:** Regression invariant: source bound application loader rejects locally valid rationale change. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_application_loader_rejects_locally_valid_rationale_change(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="upstream\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `_coordinated_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_manifest_filenames_are_casefold_unique`

**Purpose:** Regression invariant: application manifest filenames are casefold unique. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="filename\|duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `str(<br>        payload["artifacts"][0]["filename"]<br>    ).upper` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeatureApplicationArtifactManifest.model_validate` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.model_validate` |

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
| In-memory mutation | `payload["artifacts"][1]["filename"] = str(<br>        payload["artifacts"][0]["filename"]<br>    ).upper()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_swap_referenced_feature_values`

**Purpose:** Implements `swap referenced feature values` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _swap_referenced_feature_values(
    result: BessPlanningFeatureApplicationResult,
    columns: tuple[str, ...],
) -> BessPlanningFeatureApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |
| `columns` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(replace(changed, relations=relations))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_swap_referenced_feature_values`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `_swap_referenced_feature_values`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `result.relations["bess_cnig_policy_application_status"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `referenced["bess_cnig_precheck_status"].ne` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr(changed, frame_name).copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `first_mask.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `second_mask.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `changed.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `frame.loc[first_mask, column] = second_value`<br>`frame.loc[second_mask, column] = first_value`<br>`relations.loc[first_mask, column] = second_value`<br>`relations.loc[second_mask, column] = first_value` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`

**Purpose:** Regression invariant: source bound loader rejects valid domain cross pair swaps. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_loader_rejects_valid_domain_cross_pair_swaps(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    columns: tuple[str, ...],
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "columns",
    [
        (
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_status_priority",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ),
        (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
        ),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `columns` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="upstream")`
- Exact assertions:
  - `assert heavy_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `_swap_referenced_feature_values` | `tests.unit.test_apply_bess_planning_feature_policy._swap_referenced_feature_values` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps.forbidden_heavy`

**Purpose:** Implements `forbidden heavy` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def forbidden_heavy(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_loader_rejects_factual_prefix_lineage_change`

**Purpose:** Regression invariant: source bound loader rejects factual prefix lineage change. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_loader_rejects_factual_prefix_lineage_change(
    tmp_path: Path, column: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["source_provider", "source_portal"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="upstream")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], column] = f"changed-{column}"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_loader_rejects_all_null_raw_column_transition`

**Purpose:** Regression invariant: source bound loader rejects all null raw column transition. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_loader_rejects_all_null_raw_column_transition(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="upstream")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `coded.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded_relations["planning_feature_id"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded_relations["text_raw"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `coding_module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `policy.policy_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `policy_module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._build_result` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["text_raw"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.surface_features.iloc[::-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `reordered_dir.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `reordered_dir.mkdir` |
| Hashing/byte identity | `coding_module._result_with_hashes`<br>`policy_module._result_with_hashes`<br>`module._result_with_hashes` |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `coded_surface["text_raw"] = pd.Series(<br>        ["source text"] * len(coded_surface), index=coded_surface.index, dtype="str"<br>    )`<br>`coded_relations.loc[<br>        coded_relations["planning_feature_id"].isin(surface_ids), "text_raw"<br>    ] = "source text"`<br>`coded_relations["text_raw"] = pd.Series(<br>        coded_relations["text_raw"].tolist(),<br>        index=coded_relations.index,<br>        dtype="str",<br>    )`<br>`policy_table["cnig_complete_result_content_sha256"] = pd.array(<br>        [coded.complete_result_content_sha256] * len(policy_table), dtype="str"<br>    )`<br>`surface["text_raw"] = pd.Series(None, index=surface.index, dtype="object")`<br>`relations.loc[mask, "text_raw"] = pd.NA`<br>`relations["text_raw"] = pd.Series(<br>        relations["text_raw"].tolist(), index=relations.index, dtype="str"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`

**Purpose:** Regression invariant: source bound loader rejects unreferenced feature and row reordering. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureApplicationError, match="upstream")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `_zero_relation_feature` | `tests.unit.test_apply_bess_planning_feature_policy._zero_relation_feature` |
| `source.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `unreferenced_dir.mkdir` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `unreferenced_dir.mkdir` |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `unreferenced.loc[index, "label_raw"] = "changed unreferenced label"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`

**Purpose:** Regression invariant: application loader validates upstreams and rebuilds once lightweight. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_loader_validates_upstreams_and_rebuilds_once_lightweight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        loaded.complete_result_content_sha256 == result.complete_result_content_sha256<br>    )`
  - `assert calls == {"coded": 1, "policy": 1, "build": 1, "heavy": 0}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `importlib.import_module` | `importlib.import_module` |
| `coded.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy.policy_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.coded_envelope`

**Purpose:** Implements `coded envelope` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def coded_envelope(value: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual_coded_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["coded"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def coded_envelope(value: object) -> None:
        calls["coded"] += 1
        actual_coded_envelope(value)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.policy_envelope`

**Purpose:** Implements `policy envelope` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def policy_envelope(value: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual_policy_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["policy"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def policy_envelope(value: object) -> None:
        calls["policy"] += 1
        actual_policy_envelope(value)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.build`

**Purpose:** Implements `build` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `actual_build(*args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual_build` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["build"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        return actual_build(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.heavy`

**Purpose:** Implements `heavy` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
| In-memory mutation | `calls["heavy"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_bad_upstream_before_artifact_reads`

**Purpose:** Regression invariant: application loader rejects bad upstream before artifact reads. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_loader_rejects_bad_upstream_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(Exception, match="hash\|SHA\|invalid")`
- Exact assertions:
  - `assert reads == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_load_application_artifacts` | `landscout.stages.apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_bad_upstream_before_artifact_reads.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted(path: Path) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `original(path)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original` | `unresolved local/third-party receiver; no ownership inferred` |

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
def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_manifest_rejects_nonportable_filename`

**Purpose:** Regression invariant: application manifest rejects nonportable filename. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "filename",
    [
        "/tmp/file.parquet",
        "../file.parquet",
        "subdir/file.parquet",
        r"C:\absolute\file.parquet",
        "C:/absolute/file.parquet",
        r"\\server\share\file.parquet",
        r"subdir\file.parquet",
        "CON.parquet",
        "con.PARQUET",
        "NUL.parquet",
        "PRN.parquet",
        "AUX.parquet",
        "CLOCK$.parquet",
        "COM1.parquet",
        "COM9.parquet",
        "LPT1.parquet",
        "LPT9.parquet",
        "COM¹.parquet",
        "COM².parquet",
        "COM³.parquet",
        "LPT¹.parquet",
        "LPT².parquet",
        "LPT³.parquet",
        "file:name.parquet",
        "base.parquet:stream.parquet",
        "file?.parquet",
        "file*.parquet",
        "file<.parquet",
        "file>.parquet",
        "file|.parquet",
        'file".parquet',
        "nul\x00.parquet",
        "line\nbreak.parquet",
        "del\x7f.parquet",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `filename` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="filename\|basename\|portable")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeatureApplicationArtifactManifest.model_validate` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `payload["artifacts"][0]["filename"] = filename` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_compatible_policy_mutation`

**Purpose:** Implements `compatible policy mutation` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _compatible_policy_mutation(policy: object, mutation: str) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy` | positional-or-keyword | `object` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(changed)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_compatible_policy_mutation`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `_compatible_policy_mutation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `policy.policy_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.iloc[[0]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `pd.concat([table, extra], ignore_index=True).sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `pd.Index` | `pandas.Index` |
| `table.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.iloc[:-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `scalar_changes["cnig_profile_schema_version"] = 3`<br>`extra["type_code"] = pd.array(["98"], dtype="str")`<br>`table.index = pd.Index(table.index.to_numpy(), dtype="int64")`<br>`table.index = pd.Index(range(len(table)), dtype="int64")`<br>`table.loc[table.index[0], "official_label"] = "Another exact official label"`<br>`table.loc[table.index[0], "official_legal_reference"] = "Changed legal ref"`<br>`table.loc[table.index[0], "official_regulation_reference"] = (<br>            "Changed regulation ref"<br>        )`<br>`scalar_changes["source_document_id"] = "OTHER-DOCUMENT"`<br>`scalar_changes["source_archive_sha256"] = "b" * 64`<br>`scalar_changes["cnig_profile"] = "other-cnig-profile"`<br>`table["cnig_profile"] = pd.array(<br>            ["other-cnig-profile"] * len(table), dtype="str"<br>        )`<br>`scalar_changes["cnig_profile_sha256"] = "a" * 64`<br>`table["cnig_profile_sha256"] = pd.array(["a" * 64] * len(table), dtype="str")`<br>`scalar_changes["cnig_complete_result_content_sha256"] = "a" * 64`<br>`table["cnig_complete_result_content_sha256"] = pd.array(<br>            ["a" * 64] * len(table), dtype="str"<br>        )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`

**Purpose:** Regression invariant: application loader rejects incompatible upstreams before io or rebuild. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        "profile-schema",
        "extra-pair",
        "missing-pair",
        "official-label",
        "legal-reference",
        "regulation-reference",
        "document",
        "archive",
        "profile",
        "profile-sha",
        "complete-result-sha",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError,<br>        match="Policy\|policy\|CNIG\|pair\|source\|schema\|official\|reference",<br>    )`
- Exact assertions:
  - `assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `_compatible_policy_mutation` | `tests.unit.test_apply_bess_planning_feature_policy._compatible_policy_mutation` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.manifest_read`

**Purpose:** Implements `manifest read` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("manifest read must not run")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["manifest"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.read`

**Purpose:** Implements `read` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def read(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("artifact read must not run")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["read"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("artifact read must not run")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.build`

**Purpose:** Implements `build` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("application rebuild must not run")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["build"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.heavy`

**Purpose:** Implements `heavy` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
| In-memory mutation | `calls["heavy"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`

**Purpose:** Regression invariant: application loader rejects empty upstreams before any io or rebuild. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    empty_upstream: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("empty_upstream", ["coded", "policy", "both"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `empty_upstream` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureApplicationError,<br>        match="dictionary\|policy\|table\|pair\|empty\|record\|entry",<br>    )`
- Exact assertions:
  - `assert calls == {"manifest": 0, "read": 0, "build": 0, "heavy": 0}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `tests.unit.test_apply_bess_planning_feature_policy._application_fixture` |
| `_write_application_artifacts` | `tests.unit.test_apply_bess_planning_feature_policy._write_application_artifacts` |
| `_canonical_empty_coded_result` | `test_resolve_planning_feature_codes._canonical_empty_coded_result` |
| `_canonical_empty_policy_result` | `test_bess_planning_feature_policy._canonical_empty_policy_result` |
| `importlib.import_module` | `importlib.import_module` |
| `policy_module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_application_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `policy_module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.manifest_read`

**Purpose:** Implements `manifest read` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("manifest read must not run")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["manifest"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
        calls["manifest"] += 1
        raise AssertionError("manifest read must not run")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.artifact_read`

**Purpose:** Implements `artifact read` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def artifact_read(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("Parquet read must not run")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["read"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def artifact_read(*args: object, **kwargs: object) -> object:
        calls["read"] += 1
        raise AssertionError("Parquet read must not run")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.build`

**Purpose:** Implements `build` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("application rebuild must not run")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `calls["build"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def build(*args: object, **kwargs: object) -> object:
        calls["build"] += 1
        raise AssertionError("application rebuild must not run")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.heavy`

**Purpose:** Implements `heavy` within the file role: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

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
| In-memory mutation | `calls["heavy"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def heavy(*args: object, **kwargs: object) -> None:
        calls["heavy"] += 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 6A. STEP 7F.1A.4.1 changed callable contracts

### `_application_artifact_record_payload`

- Exact signature: `def _application_artifact_record_payload() -> dict[str, object]:`
- Builds the nested plain schema/CRS payload used to prove recursive copying, retained canonical serialization, and alias isolation.

### `test_application_artifact_record_is_deeply_immutable_without_aliases`

- Exact signature: `def test_application_artifact_record_is_deeply_immutable_without_aliases() -> None:`
- Mutates caller-owned nested input after validation and requires the retained record to remain unchanged; direct mapping and nested sequence/mapping mutation must fail immediately.

## 7. Test-specific regression contract

- Test functions: **71**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_exact_policy_is_applied_to_every_feature_and_relation` | none | none | 15 | Proves exact policy is applied to every feature and relation using the exact source reproduced in section 7. |
| `test_every_output_row_has_all_six_false_boundary_flags` | none | none | 4 | Proves every output row has all six false boundary flags using the exact source reproduced in section 7. |
| `test_policy_suffix_has_one_exact_deterministic_dtype_schema` | none | none | 2 | Proves policy suffix has one exact deterministic dtype schema using the exact source reproduced in section 7. |
| `test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` | none | pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension"); pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension") | 5 | Proves schema v1 dimension blind hash representation is rejected locally using the exact source reproduced in section 7. |
| `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` | pytest.mark.parametrize(<br>    ("frame_name", "geometry_kind"),<br>    [<br>        ("surface_features", "Polygon"),<br>        ("surface_features", "MultiPolygon"),<br>        ("line_features", "LineString"),<br>        ("line_features", "MultiLineString"),<br>        ("point_features", "Point"),<br>        ("point_features", "MultiPoint"),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension") | 1 | Proves every non 2d application geometry kind fast fails before source validation using the exact source reproduced in section 7. |
| `test_m_and_zm_application_geometries_are_rejected` | pytest.mark.parametrize("wkt", ["POINT M (1 1 7)", "POINT ZM (1 1 7 8)"]) | pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension") | 0 | Proves m and zm application geometries are rejected using the exact source reproduced in section 7. |
| `test_valid_empty_optional_application_catalog_retains_schema_and_crs` | none | none | 5 | Proves valid empty optional application catalog retains schema and crs using the exact source reproduced in section 7. |
| `test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct` | none | none | 8 | Proves exact pair identity keeps family subtype and leading zeroes distinct using the exact source reproduced in section 7. |
| `test_unknown_pair_remains_present_with_true_null_decision_fields` | none | none | 4 | Proves unknown pair remains present with true null decision fields using the exact source reproduced in section 7. |
| `test_inconsistent_official_status_and_policy_match_is_rejected` | pytest.mark.parametrize(<br>    "row",<br>    [<br>        ("F-MISSING", "PRESCRIPTION", "98", "00", "RESOLVED_OFFICIAL"),<br>        ("F-UNEXPECTED", "PRESCRIPTION", "15", "00", "UNKNOWN_CODE_PAIR"),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="policy\|official") | 0 | Proves inconsistent official status and policy match is rejected using the exact source reproduced in section 7. |
| `test_feature_and_relation_inputs_are_preserved_and_not_mutated` | none | none | 4 | Proves feature and relation inputs are preserved and not mutated using the exact source reproduced in section 7. |
| `test_relations_inherit_only_from_referenced_enriched_feature` | none | none | 1 | Proves relations inherit only from referenced enriched feature using the exact source reproduced in section 7. |
| `test_complete_relation_facts_must_match_referenced_feature` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("source_feature_id", "MUTATED"),<br>        ("source_identity_kind", "MUTATED"),<br>        ("source_identity_field", "MUTATED"),<br>        ("logical_layer", "information_surface"),<br>        ("label_raw", "MUTATED"),<br>        ("text_raw", "MUTATED"),<br>        ("source_document_id", "MUTATED"),<br>        ("source_archive_sha256", "f" * 64),<br>        ("source_layer", "MUTATED"),<br>        ("source_validity_date_raw", "2099-01-01"),<br>        ("regulation_filename_raw", "MUTATED.pdf"),<br>        ("official_code_label", "MUTATED"),<br>        ("official_code_profile", "MUTATED"),<br>        ("feature_area_m2", 999.0),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="relation\|feature") | 0 | Proves complete relation facts must match referenced feature using the exact source reproduced in section 7. |
| `test_unknown_relation_feature_id_is_rejected` | none | pytest.raises(BessPlanningFeatureApplicationError, match="feature ID") | 1 | Proves unknown relation feature id is rejected using the exact source reproduced in section 7. |
| `test_scope_has_no_parcel_output_aggregation_rejection_or_score` | none | none | 9 | Proves scope has no parcel output aggregation rejection or score using the exact source reproduced in section 7. |
| `test_coordinated_feature_or_relation_policy_mutation_is_rejected` | none | pytest.raises(BessPlanningFeatureApplicationError, match="rebuilt\|feature"); pytest.raises(BessPlanningFeatureApplicationError, match="relation\|rebuilt") | 0 | Proves coordinated feature or relation policy mutation is rejected using the exact source reproduced in section 7. |
| `test_duplicate_application_relation_pair_is_rejected_locally` | none | pytest.raises(BessPlanningFeatureApplicationError, match="duplicate\|unique") | 0 | Proves duplicate application relation pair is rejected locally using the exact source reproduced in section 7. |
| `test_application_relation_feature_id_is_exact_and_portable` | pytest.mark.parametrize(<br>    "feature_id",<br>    [None, "", "None", "/tmp/feature", r"C:\feature", " GPU:F "],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="feature\|identity") | 0 | Proves application relation feature id is exact and portable using the exact source reproduced in section 7. |
| `test_application_relation_parcel_id_is_exact` | pytest.mark.parametrize("parcel_id", [None, "", "None", " PARCEL-1 "]) | pytest.raises(BessPlanningFeatureApplicationError, match="parcel\|identity") | 0 | Proves application relation parcel id is exact using the exact source reproduced in section 7. |
| `test_unknown_application_relation_type_is_rejected_locally` | none | pytest.raises(BessPlanningFeatureApplicationError, match="relation type") | 0 | Proves unknown application relation type is rejected locally using the exact source reproduced in section 7. |
| `test_coordinated_invalid_policy_domains_fail_local_validation` | pytest.mark.parametrize(<br>    ("column", "value", "message"),<br>    [<br>        ("bess_cnig_precheck_status", "AUTHORIZED", "status\|domain"),<br>        ("bess_cnig_precheck_status", "FORBIDDEN", "status\|domain"),<br>        ("bess_cnig_precheck_status", "PROHIBITED", "status\|domain"),<br>        ("bess_cnig_precheck_confidence", "CERTAIN", "confidence\|domain"),<br>        ("bess_cnig_status_priority", 0, "priority\|positive"),<br>        ("bess_cnig_status_priority", -1, "priority\|positive"),<br>        ("bess_cnig_rationale", "", "rationale\|exact\|non-empty"),<br>        ("bess_cnig_rationale", " leading", "rationale\|exact\|whitespace"),<br>        ("bess_cnig_required_human_action", "trailing ", "action\|exact\|whitespace"),<br>        ("bess_cnig_limitations", "", "limitations\|exact\|non-empty"),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match=message) | 0 | Proves coordinated invalid policy domains fail local validation using the exact source reproduced in section 7. |
| `test_literal_null_replacements_are_rejected` | pytest.mark.parametrize("literal", ["None", "nan", "<NA>"]) | pytest.raises(BessPlanningFeatureApplicationError, match="literal\|missing") | 0 | Proves literal null replacements are rejected using the exact source reproduced in section 7. |
| `test_self_consistent_wrong_policy_suffix_dtype_is_rejected` | pytest.mark.parametrize(<br>    ("column", "dtype", "value"),<br>    [<br>        ("bess_cnig_precheck_status", "object", "UNKNOWN"),<br>        ("bess_cnig_precheck_confidence", "category", "HIGH"),<br>        ("bess_cnig_rationale", "object", "Still a factual policy rationale."),<br>        ("bess_cnig_status_priority", "Float64", 1.0),<br>        ("bess_cnig_status_priority", "str", "1"),<br>        ("bess_cnig_parcel_status_aggregated", "boolean", False),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="dtype\|schema") | 0 | Proves self consistent wrong policy suffix dtype is rejected using the exact source reproduced in section 7. |
| `test_official_and_application_statuses_cannot_contradict` | pytest.mark.parametrize(<br>    ("official_status", "application_status"),<br>    [<br>        ("RESOLVED_OFFICIAL", "UNRESOLVED_CODE_PAIR"),<br>        ("UNKNOWN_CODE_PAIR", "APPLIED_EXACT_POLICY"),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="official\|status") | 0 | Proves official and application statuses cannot contradict using the exact source reproduced in section 7. |
| `test_any_true_row_boundary_flag_is_rejected` | pytest.mark.parametrize("column", BOUNDARY_FLAG_COLUMNS) | pytest.raises(BessPlanningFeatureApplicationError, match="flag\|false") | 0 | Proves any true row boundary flag is rejected using the exact source reproduced in section 7. |
| `test_application_and_public_validator_heavy_validation_counts` | none | none | 2 | Proves application and public validator heavy validation counts using the exact source reproduced in section 7. |
| `test_malformed_local_result_fast_fails_before_heavy_validation` | none | pytest.raises(<br>        BessPlanningFeatureApplicationError, match="hash\|SHA\|sha256\|invalid"<br>    ) | 1 | Proves malformed local result fast fails before heavy validation using the exact source reproduced in section 7. |
| `test_coordinated_application_source_lock_mutation_fast_fails` | none | pytest.raises(BessPlanningFeatureApplicationError, match="source lock") | 1 | Proves coordinated application source lock mutation fast fails using the exact source reproduced in section 7. |
| `test_valid_four_file_manifest_and_verified_byte_readback` | none | none | 0 | Proves valid four file manifest and verified byte readback using the exact source reproduced in section 7. |
| `test_duplicate_relation_pair_artifact_fails_local_loading` | none | pytest.raises(BessPlanningFeatureApplicationError, match="duplicate\|unique") | 0 | Proves duplicate relation pair artifact fails local loading using the exact source reproduced in section 7. |
| `test_document_wide_mapping_conflict_artifact_fails_local_loading` | none | pytest.raises(BessPlanningFeatureApplicationError, match="priority\|mapping") | 0 | Proves document wide mapping conflict artifact fails local loading using the exact source reproduced in section 7. |
| `test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` | none | pytest.raises(<br>        BessPlanningFeatureApplicationError, match="surface\|metric\|type"<br>    ) | 0 | Proves positive surface overlap cannot be relabelled touch only in artifact using the exact source reproduced in section 7. |
| `test_wrong_2d_feature_geometry_fails_local_artifact_loading` | none | pytest.raises(BessPlanningFeatureApplicationError, match="surface\|geometry") | 0 | Proves wrong 2d feature geometry fails local artifact loading using the exact source reproduced in section 7. |
| `test_feature_catalog_geometry_role_is_intrinsic` | pytest.mark.parametrize(<br>    ("frame_name", "geometry"),<br>    [<br>        ("surface_features", Point(0, 0)),<br>        ("line_features", Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])),<br>        ("point_features", LineString([(0, 0), (1, 1)])),<br>        ("surface_features", Polygon()),<br>        (<br>            "surface_features",<br>            Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),<br>        ),<br>    ],<br>    ids=["surface-point", "line-polygon", "point-line", "empty", "invalid"],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="geometry") | 0 | Proves feature catalog geometry role is intrinsic using the exact source reproduced in section 7. |
| `test_feature_catalog_metric_must_match_geometry` | pytest.mark.parametrize(<br>    ("frame_name", "metric"),<br>    [<br>        ("surface_features", "feature_area_m2"),<br>        ("line_features", "feature_length_m"),<br>        ("point_features", "point_member_count"),<br>    ],<br>) | pytest.raises(<br>        BessPlanningFeatureApplicationError, match="metric\|geometry\|count"<br>    ) | 0 | Proves feature catalog metric must match geometry using the exact source reproduced in section 7. |
| `test_unreferenced_feature_catalog_identity_fields_are_intrinsic` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("planning_feature_id", "GPU:malformed"),<br>        ("logical_layer", "prescription_line"),<br>        ("geometry_kind", "LINE"),<br>    ],<br>) | pytest.raises(<br>        BessPlanningFeatureApplicationError, match="identity\|layer\|kind"<br>    ) | 0 | Proves unreferenced feature catalog identity fields are intrinsic using the exact source reproduced in section 7. |
| `test_feature_catalog_requires_canonical_crs_and_global_identity` | none | pytest.raises(BessPlanningFeatureApplicationError, match="EPSG:2154\|CRS"); pytest.raises(BessPlanningFeatureApplicationError, match="identity\|unique") | 0 | Proves feature catalog requires canonical crs and global identity using the exact source reproduced in section 7. |
| `test_unreferenced_feature_identity_is_validated_locally` | pytest.mark.parametrize("feature_id", ["None", "/tmp/feature", r"C:\feature", " bad "]) | pytest.raises(<br>        BessPlanningFeatureApplicationError, match="feature\|identity\|GPU"<br>    ) | 0 | Proves unreferenced feature identity is validated locally using the exact source reproduced in section 7. |
| `test_unreferenced_feature_participates_in_global_policy_mapping` | none | pytest.raises(BessPlanningFeatureApplicationError, match="priority\|mapping") | 0 | Proves unreferenced feature participates in global policy mapping using the exact source reproduced in section 7. |
| `test_application_locks_policy_result_schema_exactly` | pytest.mark.parametrize("policy_schema", [0, 2, 999]) | pytest.raises(BessPlanningFeatureApplicationError, match="policy.*schema") | 0 | Proves application locks policy result schema exactly using the exact source reproduced in section 7. |
| `test_application_locks_cnig_result_schema_exactly` | pytest.mark.parametrize("cnig_schema", [1, 4, 6, 999]) | pytest.raises(BessPlanningFeatureApplicationError, match="CNIG\|cnig.*schema") | 0 | Proves application locks cnig result schema exactly using the exact source reproduced in section 7. |
| `test_application_accepts_only_current_policy_and_cnig_source_schemas` | none | none | 2 | Proves application accepts only current policy and cnig source schemas using the exact source reproduced in section 7. |
| `test_duplicate_relation_identity_fast_fails_before_policy_source_validation` | none | pytest.raises(BessPlanningFeatureApplicationError, match="duplicate\|unique") | 1 | Proves duplicate relation identity fast fails before policy source validation using the exact source reproduced in section 7. |
| `test_self_consistent_z_geoparquet_artifact_is_rejected` | none | pytest.raises(BessPlanningFeatureApplicationError, match="2D\|dimension") | 0 | Proves self consistent z geoparquet artifact is rejected using the exact source reproduced in section 7. |
| `test_self_consistent_wrong_dtype_artifact_is_rejected` | none | pytest.raises(BessPlanningFeatureApplicationError, match="dtype\|schema") | 0 | Proves self consistent wrong dtype artifact is rejected using the exact source reproduced in section 7. |
| `test_artifact_manifest_rejects_invalid_contract` | pytest.mark.parametrize(<br>    ("mutation", "message"),<br>    [<br>        (lambda value: value.update(schema_version=1), "schema"),<br>        (lambda value: value["artifacts"].pop(), "role\|artifact"),<br>        (<br>            lambda value: value["artifacts"].append(<br>                {**value["artifacts"][0], "artifact_role": "EXTRA"}<br>            ),<br>            "role\|artifact",<br>        ),<br>        (<br>            lambda value: value["artifacts"].append(dict(value["artifacts"][0])),<br>            "duplicate\|role\|artifact",<br>        ),<br>        (<br>            lambda value: value["artifacts"][0].update(filename="wrong.parquet"),<br>            "filename",<br>        ),<br>        (<br>            lambda value: value["artifacts"][1].update(<br>                filename=value["artifacts"][0]["filename"]<br>            ),<br>            "duplicate\|filename",<br>        ),<br>        (<br>            lambda value: value["artifacts"][0].update(<br>                filename="C:/absolute/surface.parquet"<br>            ),<br>            "filename",<br>        ),<br>        (lambda value: value["artifacts"][0].update(size_bytes=1), "size"),<br>        (lambda value: value["artifacts"][0].update(sha256="f" * 64), "SHA\|hash"),<br>        (lambda value: value["artifacts"][0].update(sha256="bad"), "SHA\|hash"),<br>        (lambda value: value["artifacts"][0].update(row_count=999), "row"),<br>        (<br>            lambda value: value["artifacts"][0]["frame_schema_signature"].update(<br>                index_names=["wrong"]<br>            ),<br>            "schema",<br>        ),<br>        (lambda value: value["artifacts"][0].update(crs={"wrong": True}), "CRS\|crs"),<br>        (lambda value: value["artifacts"][0].update(crs=None), "CRS\|crs"),<br>        (lambda value: value["artifacts"][0].update(geospatial=False), "geospatial"),<br>        (lambda value: value.update(unknown=True), "manifest\|artifact"),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match=message) | 1 | Proves artifact manifest rejects invalid contract using the exact source reproduced in section 7. |
| `test_application_manifest_uses_strict_json_before_artifact_read` | pytest.mark.parametrize(<br>    "document",<br>    [<br>        '{"schema_version": 2, "schema_version": 2}\n',<br>        '{"schema_version": NaN}\n',<br>        '{"schema_version": Infinity}\n',<br>        "[]\n",<br>    ],<br>    ids=["duplicate-key", "nan", "infinity", "non-object"],<br>) | pytest.raises(<br>        BessPlanningFeatureApplicationError,<br>        match="Duplicate JSON\|finite\|top-level\|invalid",<br>    ) | 1 | Proves application manifest uses strict json before artifact read using the exact source reproduced in section 7. |
| `test_artifact_loader_parses_only_verified_bytes` | none | none | 2 | Proves artifact loader parses only verified bytes using the exact source reproduced in section 7. |
| `test_physical_replacement_before_loading_is_rejected` | none | pytest.raises(BessPlanningFeatureApplicationError, match="size\|SHA\|hash") | 0 | Proves physical replacement before loading is rejected using the exact source reproduced in section 7. |
| `test_public_application_api_exports_only_stable_symbols` | none | none | 3 | Proves public application api exports only stable symbols using the exact source reproduced in section 7. |
| `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` | none | pytest.raises(BessPlanningFeatureApplicationError, match="document\|lineage") | 0 | Proves unreferenced feature document lineage is bound to envelope artifact using the exact source reproduced in section 7. |
| `test_feature_row_lineage_must_match_application_envelope` | pytest.mark.parametrize(<br>    "mutation",<br>    ["archive", "official-profile", "envelope-document"],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="lineage\|document") | 0 | Proves feature row lineage must match application envelope using the exact source reproduced in section 7. |
| `test_coordinated_referenced_row_lineage_cannot_bypass_envelope` | pytest.mark.parametrize(<br>    ("column", "value", "rename_id"),<br>    [<br>        ("source_document_id", "MUTATED-DOCUMENT", True),<br>        ("source_archive_sha256", "f" * 64, False),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="lineage\|document") | 0 | Proves coordinated referenced row lineage cannot bypass envelope using the exact source reproduced in section 7. |
| `test_resolved_official_row_requires_label_and_envelope_profile` | none | pytest.raises(<br>            BessPlanningFeatureApplicationError, match="official\|profile\|label"<br>        ) | 0 | Proves resolved official row requires label and envelope profile using the exact source reproduced in section 7. |
| `test_unknown_official_row_rejects_invented_label_or_url` | none | pytest.raises(BessPlanningFeatureApplicationError, match="official\|null") | 0 | Proves unknown official row rejects invented label or url using the exact source reproduced in section 7. |
| `test_application_feature_prefix_has_exact_canonical_schema` | pytest.mark.parametrize(<br>    ("frame_name", "mutation"),<br>    [<br>        ("surface_features", "missing-column"),<br>        ("surface_features", "unexpected-column"),<br>        ("surface_features", "reordered-columns"),<br>        ("surface_features", "metric-object"),<br>        ("line_features", "metric-object"),<br>        ("point_features", "metric-object"),<br>        ("surface_features", "official-object"),<br>        ("surface_features", "index-name"),<br>        ("surface_features", "index-dtype"),<br>        ("point_features", "malformed-empty"),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="schema\|dtype\|index") | 0 | Proves application feature prefix has exact canonical schema using the exact source reproduced in section 7. |
| `test_application_relation_prefix_has_exact_canonical_schema` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "missing-column",<br>        "unexpected-column",<br>        "reordered-columns",<br>        "float-object",<br>        "count-object",<br>        "official-category",<br>        "malformed-empty",<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="schema\|dtype") | 0 | Proves application relation prefix has exact canonical schema using the exact source reproduced in section 7. |
| `test_self_consistent_factual_prefix_dtype_artifact_is_rejected` | none | pytest.raises(BessPlanningFeatureApplicationError, match="schema\|dtype") | 0 | Proves self consistent factual prefix dtype artifact is rejected using the exact source reproduced in section 7. |
| `test_lineage_defect_fast_fails_before_policy_source_validation` | none | pytest.raises(BessPlanningFeatureApplicationError) | 1 | Proves lineage defect fast fails before policy source validation using the exact source reproduced in section 7. |
| `test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` | none | pytest.raises(BessPlanningFeatureApplicationError, match="hash\|invalid") | 2 | Proves step 7d 5b 2b 5 application loader requires exact upstreams using the exact source reproduced in section 7. |
| `test_source_bound_application_loader_rejects_locally_valid_rationale_change` | none | pytest.raises(BessPlanningFeatureApplicationError, match="upstream\|rebuilt") | 0 | Proves source bound application loader rejects locally valid rationale change using the exact source reproduced in section 7. |
| `test_application_manifest_filenames_are_casefold_unique` | none | pytest.raises(ValueError, match="filename\|duplicate") | 0 | Proves application manifest filenames are casefold unique using the exact source reproduced in section 7. |
| `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` | pytest.mark.parametrize(<br>    "columns",<br>    [<br>        (<br>            "bess_cnig_precheck_status",<br>            "bess_cnig_precheck_confidence",<br>            "bess_cnig_status_priority",<br>            "bess_cnig_rationale",<br>            "bess_cnig_required_human_action",<br>            "bess_cnig_limitations",<br>        ),<br>        (<br>            "official_code_label",<br>            "official_legal_reference",<br>            "official_regulation_reference",<br>            "official_code_source_url",<br>        ),<br>    ],<br>) | pytest.raises(BessPlanningFeatureApplicationError, match="upstream") | 1 | Proves source bound loader rejects valid domain cross pair swaps using the exact source reproduced in section 7. |
| `test_source_bound_loader_rejects_factual_prefix_lineage_change` | pytest.mark.parametrize("column", ["source_provider", "source_portal"]) | pytest.raises(BessPlanningFeatureApplicationError, match="upstream") | 0 | Proves source bound loader rejects factual prefix lineage change using the exact source reproduced in section 7. |
| `test_source_bound_loader_rejects_all_null_raw_column_transition` | none | pytest.raises(BessPlanningFeatureApplicationError, match="upstream"); pytest.raises(BessPlanningFeatureApplicationError, match="upstream") | 0 | Proves source bound loader rejects all null raw column transition using the exact source reproduced in section 7. |
| `test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` | none | pytest.raises(BessPlanningFeatureApplicationError, match="upstream") | 0 | Proves source bound loader rejects unreferenced feature and row reordering using the exact source reproduced in section 7. |
| `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` | none | none | 2 | Proves application loader validates upstreams and rebuilds once lightweight using the exact source reproduced in section 7. |
| `test_application_loader_rejects_bad_upstream_before_artifact_reads` | none | pytest.raises(Exception, match="hash\|SHA\|invalid") | 1 | Proves application loader rejects bad upstream before artifact reads using the exact source reproduced in section 7. |
| `test_application_manifest_rejects_nonportable_filename` | pytest.mark.parametrize(<br>    "filename",<br>    [<br>        "/tmp/file.parquet",<br>        "../file.parquet",<br>        "subdir/file.parquet",<br>        r"C:\absolute\file.parquet",<br>        "C:/absolute/file.parquet",<br>        r"\\server\share\file.parquet",<br>        r"subdir\file.parquet",<br>        "CON.parquet",<br>        "con.PARQUET",<br>        "NUL.parquet",<br>        "PRN.parquet",<br>        "AUX.parquet",<br>        "CLOCK$.parquet",<br>        "COM1.parquet",<br>        "COM9.parquet",<br>        "LPT1.parquet",<br>        "LPT9.parquet",<br>        "COM¹.parquet",<br>        "COM².parquet",<br>        "COM³.parquet",<br>        "LPT¹.parquet",<br>        "LPT².parquet",<br>        "LPT³.parquet",<br>        "file:name.parquet",<br>        "base.parquet:stream.parquet",<br>        "file?.parquet",<br>        "file*.parquet",<br>        "file<.parquet",<br>        "file>.parquet",<br>        "file\|.parquet",<br>        'file".parquet',<br>        "nul\x00.parquet",<br>        "line\nbreak.parquet",<br>        "del\x7f.parquet",<br>    ],<br>) | pytest.raises(ValueError, match="filename\|basename\|portable") | 0 | Proves application manifest rejects nonportable filename using the exact source reproduced in section 7. |
| `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "profile-schema",<br>        "extra-pair",<br>        "missing-pair",<br>        "official-label",<br>        "legal-reference",<br>        "regulation-reference",<br>        "document",<br>        "archive",<br>        "profile",<br>        "profile-sha",<br>        "complete-result-sha",<br>    ],<br>) | pytest.raises(<br>        BessPlanningFeatureApplicationError,<br>        match="Policy\|policy\|CNIG\|pair\|source\|schema\|official\|reference",<br>    ) | 1 | Proves application loader rejects incompatible upstreams before io or rebuild using the exact source reproduced in section 7. |
| `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` | pytest.mark.parametrize("empty_upstream", ["coded", "policy", "both"]) | pytest.raises(<br>        BessPlanningFeatureApplicationError,<br>        match="dictionary\|policy\|table\|pair\|empty\|record\|entry",<br>    ) | 1 | Proves application loader rejects empty upstreams before any io or rebuild using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from __future__ import annotations

import importlib
import inspect
import json
from collections.abc import Mapping
from dataclasses import fields, replace
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely import from_wkt, get_coordinate_dimension, to_wkb
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from test_bess_planning_feature_policy import (
    _canonical_empty_policy_result,
    _checked_in_policy_result,
    _compiled_fixture,
)
from test_resolve_planning_feature_codes import _canonical_empty_coded_result

from landscout import stages
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationArtifactRecord,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)
from landscout.stages.apply_bess_planning_feature_policy import (
    load_bess_planning_feature_application_artifacts as _load_application_artifacts,
)

APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
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
BOUNDARY_FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
ARTIFACT_FILES = {
    "SURFACE_FEATURES": ("surface.parquet", True),
    "LINE_FEATURES": ("line.parquet", True),
    "POINT_FEATURES": ("point.parquet", True),
    "RELATIONS": ("relations.parquet", False),
}
_LAST_CODED_RESULT: object | None = None
_LAST_POLICY_RESULT: object | None = None


def _application_artifact_record_payload() -> dict[str, object]:
    crs = {
        "type": "ProjectedCRS",
        "name": "RGF93 v1 / Lambert-93",
        "coordinate_system": {"axis": [{"name": "Easting"}]},
    }
    return {
        "artifact_role": "SURFACE_FEATURES",
        "filename": "surface.parquet",
        "row_count": 1,
        "size_bytes": 1,
        "sha256": "a" * 64,
        "frame_schema_signature": {
            "columns": ["geometry"],
            "dtypes": ["geometry"],
            "index_class": "pandas.core.indexes.range.RangeIndex",
            "index_names": [None],
            "index_level_dtypes": ["int64"],
            "geometry_column": "geometry",
            "crs": crs,
        },
        "geospatial": True,
        "crs": crs,
    }


def test_application_artifact_record_is_deeply_immutable_without_aliases() -> None:
    payload = _application_artifact_record_payload()
    record = BessPlanningFeatureApplicationArtifactRecord.model_validate(payload)

    payload_signature = payload["frame_schema_signature"]
    assert isinstance(payload_signature, dict)
    payload_columns = payload_signature["columns"]
    assert isinstance(payload_columns, list)
    payload_columns.append("caller_mutation")
    payload_crs = payload["crs"]
    assert isinstance(payload_crs, dict)
    payload_crs["caller_mutation"] = True

    assert record.frame_schema_signature["columns"] == ("geometry",)
    assert record.crs is not None
    assert "caller_mutation" not in record.crs
    assert record.model_dump(mode="json", warnings="error") == (
        _application_artifact_record_payload()
    )
    with pytest.raises(TypeError, match="frozen"):
        record.frame_schema_signature["new"] = "value"
    with pytest.raises(AttributeError):
        record.frame_schema_signature["columns"].append("new")
    with pytest.raises(TypeError, match="frozen"):
        record.crs["new"] = "value"
    coordinate_system = record.crs["coordinate_system"]
    assert isinstance(coordinate_system, Mapping)
    with pytest.raises(TypeError, match="frozen"):
        coordinate_system["new"] = "value"


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


@pytest.mark.parametrize(
    ("frame_name", "geometry_kind"),
    [
        ("surface_features", "Polygon"),
        ("surface_features", "MultiPolygon"),
        ("line_features", "LineString"),
        ("line_features", "MultiLineString"),
        ("point_features", "Point"),
        ("point_features", "MultiPoint"),
    ],
)
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


@pytest.mark.parametrize("wkt", ["POINT M (1 1 7)", "POINT ZM (1 1 7 8)"])
def test_m_and_zm_application_geometries_are_rejected(wkt: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    point = result.point_features.copy(deep=True)
    point.at[point.index[0], point.geometry.name] = from_wkt(wkt)
    with pytest.raises(BessPlanningFeatureApplicationError, match="2D|dimension"):
        module._validate_result_envelope(replace(result, point_features=point))


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


@pytest.mark.parametrize(
    "row",
    [
        ("F-MISSING", "PRESCRIPTION", "98", "00", "RESOLVED_OFFICIAL"),
        ("F-UNEXPECTED", "PRESCRIPTION", "15", "00", "UNKNOWN_CODE_PAIR"),
    ],
)
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    with pytest.raises(BessPlanningFeatureApplicationError, match="policy|official"):
        module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())


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


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_feature_id", "MUTATED"),
        ("source_identity_kind", "MUTATED"),
        ("source_identity_field", "MUTATED"),
        ("logical_layer", "information_surface"),
        ("label_raw", "MUTATED"),
        ("text_raw", "MUTATED"),
        ("source_document_id", "MUTATED"),
        ("source_archive_sha256", "f" * 64),
        ("source_layer", "MUTATED"),
        ("source_validity_date_raw", "2099-01-01"),
        ("regulation_filename_raw", "MUTATED.pdf"),
        ("official_code_label", "MUTATED"),
        ("official_code_profile", "MUTATED"),
        ("feature_area_m2", 999.0),
    ],
)
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


def test_duplicate_application_relation_pair_is_rejected_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    relations = pd.concat([result.relations, result.relations.iloc[[0]]])
    changed = module._result_with_hashes(replace(result, relations=relations))
    with pytest.raises(BessPlanningFeatureApplicationError, match="duplicate|unique"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature", r"C:\feature", " GPU:F "],
)
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


@pytest.mark.parametrize("parcel_id", [None, "", "None", " PARCEL-1 "])
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


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("bess_cnig_precheck_status", "AUTHORIZED", "status|domain"),
        ("bess_cnig_precheck_status", "FORBIDDEN", "status|domain"),
        ("bess_cnig_precheck_status", "PROHIBITED", "status|domain"),
        ("bess_cnig_precheck_confidence", "CERTAIN", "confidence|domain"),
        ("bess_cnig_status_priority", 0, "priority|positive"),
        ("bess_cnig_status_priority", -1, "priority|positive"),
        ("bess_cnig_rationale", "", "rationale|exact|non-empty"),
        ("bess_cnig_rationale", " leading", "rationale|exact|whitespace"),
        ("bess_cnig_required_human_action", "trailing ", "action|exact|whitespace"),
        ("bess_cnig_limitations", "", "limitations|exact|non-empty"),
    ],
)
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


@pytest.mark.parametrize("literal", ["None", "nan", "<NA>"])
def test_literal_null_replacements_are_rejected(literal: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, "bess_cnig_rationale", literal)
    with pytest.raises(BessPlanningFeatureApplicationError, match="literal|missing"):
        module._validate_result_envelope(changed)


@pytest.mark.parametrize(
    ("column", "dtype", "value"),
    [
        ("bess_cnig_precheck_status", "object", "UNKNOWN"),
        ("bess_cnig_precheck_confidence", "category", "HIGH"),
        ("bess_cnig_rationale", "object", "Still a factual policy rationale."),
        ("bess_cnig_status_priority", "Float64", 1.0),
        ("bess_cnig_status_priority", "str", "1"),
        ("bess_cnig_parcel_status_aggregated", "boolean", False),
    ],
)
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


@pytest.mark.parametrize(
    ("official_status", "application_status"),
    [
        ("RESOLVED_OFFICIAL", "UNRESOLVED_CODE_PAIR"),
        ("UNKNOWN_CODE_PAIR", "APPLIED_EXACT_POLICY"),
    ],
)
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


@pytest.mark.parametrize("column", BOUNDARY_FLAG_COLUMNS)
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    changed = _coordinated_policy_mutation(result, column, True)
    with pytest.raises(BessPlanningFeatureApplicationError, match="flag|false"):
        module._validate_result_envelope(changed)


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


@pytest.mark.parametrize(
    ("frame_name", "geometry"),
    [
        ("surface_features", Point(0, 0)),
        ("line_features", Polygon([(0, 0), (1, 0), (1, 1), (0, 0)])),
        ("point_features", LineString([(0, 0), (1, 1)])),
        ("surface_features", Polygon()),
        (
            "surface_features",
            Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        ),
    ],
    ids=["surface-point", "line-polygon", "point-line", "empty", "invalid"],
)
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


@pytest.mark.parametrize(
    ("frame_name", "metric"),
    [
        ("surface_features", "feature_area_m2"),
        ("line_features", "feature_length_m"),
        ("point_features", "point_member_count"),
    ],
)
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


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("planning_feature_id", "GPU:malformed"),
        ("logical_layer", "prescription_line"),
        ("geometry_kind", "LINE"),
    ],
)
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


@pytest.mark.parametrize("feature_id", ["None", "/tmp/feature", r"C:\feature", " bad "])
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


@pytest.mark.parametrize("policy_schema", [0, 2, 999])
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


@pytest.mark.parametrize("cnig_schema", [1, 4, 6, 999])
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


def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    _, _, _, _, result = _application_fixture()
    assert result.policy_result_hash_schema_version == 1
    assert result.cnig_result_hash_schema_version == 5
    module._validate_result_envelope(result)


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


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
        (lambda value: value["artifacts"].pop(), "role|artifact"),
        (
            lambda value: value["artifacts"].append(
                {**value["artifacts"][0], "artifact_role": "EXTRA"}
            ),
            "role|artifact",
        ),
        (
            lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
            "duplicate|role|artifact",
        ),
        (
            lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
            "filename",
        ),
        (
            lambda value: value["artifacts"][1].update(
                filename=value["artifacts"][0]["filename"]
            ),
            "duplicate|filename",
        ),
        (
            lambda value: value["artifacts"][0].update(
                filename="C:/absolute/surface.parquet"
            ),
            "filename",
        ),
        (lambda value: value["artifacts"][0].update(size_bytes=1), "size"),
        (lambda value: value["artifacts"][0].update(sha256="f" * 64), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(sha256="bad"), "SHA|hash"),
        (lambda value: value["artifacts"][0].update(row_count=999), "row"),
        (
            lambda value: value["artifacts"][0]["frame_schema_signature"].update(
                index_names=["wrong"]
            ),
            "schema",
        ),
        (lambda value: value["artifacts"][0].update(crs={"wrong": True}), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(crs=None), "CRS|crs"),
        (lambda value: value["artifacts"][0].update(geospatial=False), "geospatial"),
        (lambda value: value.update(unknown=True), "manifest|artifact"),
    ],
)
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


@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version": 2, "schema_version": 2}\n',
        '{"schema_version": NaN}\n',
        '{"schema_version": Infinity}\n',
        "[]\n",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
def test_application_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, _, result = _application_fixture()
    manifest_path, paths, _ = _write_application_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    artifact_reads = 0
    original_read_bytes = Path.read_bytes

    def counted_bytes(path: Path) -> bytes:
        nonlocal artifact_reads
        if path in paths.values():
            artifact_reads += 1
        return original_read_bytes(path)

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal artifact_reads
        artifact_reads += 1
        raise AssertionError("Artifact read preceded strict manifest validation")

    monkeypatch.setattr(Path, "read_bytes", counted_bytes)
    monkeypatch.setattr(module.pd, "read_parquet", counted)
    with pytest.raises(
        BessPlanningFeatureApplicationError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        load_bess_planning_feature_application_artifacts(
            manifest_path,
            paths["SURFACE_FEATURES"],
            paths["LINE_FEATURES"],
            paths["POINT_FEATURES"],
            paths["RELATIONS"],
        )
    assert artifact_reads == 0


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


def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
    module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    return module._result_with_hashes(replace(result, **{frame_name: frame}))


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


@pytest.mark.parametrize(
    "mutation",
    ["archive", "official-profile", "envelope-document"],
)
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


@pytest.mark.parametrize(
    ("column", "value", "rename_id"),
    [
        ("source_document_id", "MUTATED-DOCUMENT", True),
        ("source_archive_sha256", "f" * 64, False),
    ],
)
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


@pytest.mark.parametrize(
    ("frame_name", "mutation"),
    [
        ("surface_features", "missing-column"),
        ("surface_features", "unexpected-column"),
        ("surface_features", "reordered-columns"),
        ("surface_features", "metric-object"),
        ("line_features", "metric-object"),
        ("point_features", "metric-object"),
        ("surface_features", "official-object"),
        ("surface_features", "index-name"),
        ("surface_features", "index-dtype"),
        ("point_features", "malformed-empty"),
    ],
)
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


@pytest.mark.parametrize(
    "mutation",
    [
        "missing-column",
        "unexpected-column",
        "reordered-columns",
        "float-object",
        "count-object",
        "official-category",
        "malformed-empty",
    ],
)
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


def test_application_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)


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


@pytest.mark.parametrize(
    "columns",
    [
        (
            "bess_cnig_precheck_status",
            "bess_cnig_precheck_confidence",
            "bess_cnig_status_priority",
            "bess_cnig_rationale",
            "bess_cnig_required_human_action",
            "bess_cnig_limitations",
        ),
        (
            "official_code_label",
            "official_legal_reference",
            "official_regulation_reference",
            "official_code_source_url",
        ),
    ],
)
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


@pytest.mark.parametrize("column", ["source_provider", "source_portal"])
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


@pytest.mark.parametrize(
    "filename",
    [
        "/tmp/file.parquet",
        "../file.parquet",
        "subdir/file.parquet",
        r"C:\absolute\file.parquet",
        "C:/absolute/file.parquet",
        r"\\server\share\file.parquet",
        r"subdir\file.parquet",
        "CON.parquet",
        "con.PARQUET",
        "NUL.parquet",
        "PRN.parquet",
        "AUX.parquet",
        "CLOCK$.parquet",
        "COM1.parquet",
        "COM9.parquet",
        "LPT1.parquet",
        "LPT9.parquet",
        "COM¹.parquet",
        "COM².parquet",
        "COM³.parquet",
        "LPT¹.parquet",
        "LPT².parquet",
        "LPT³.parquet",
        "file:name.parquet",
        "base.parquet:stream.parquet",
        "file?.parquet",
        "file*.parquet",
        "file<.parquet",
        "file>.parquet",
        "file|.parquet",
        'file".parquet',
        "nul\x00.parquet",
        "line\nbreak.parquet",
        "del\x7f.parquet",
    ],
)
def test_application_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, result = _application_fixture()
    _, _, payload = _write_application_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)


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


@pytest.mark.parametrize(
    "mutation",
    [
        "profile-schema",
        "extra-pair",
        "missing-pair",
        "official-label",
        "legal-reference",
        "regulation-reference",
        "document",
        "archive",
        "profile",
        "profile-sha",
        "complete-result-sha",
    ],
)
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


@pytest.mark.parametrize("empty_upstream", ["coded", "policy", "both"])
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
