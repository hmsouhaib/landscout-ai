# `tests/unit/test_apply_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_apply_bess_planning_feature_policy.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `660b1bf74db38c3c2fc9bc78916a25e703c336888a2b2902f7f43564ea5285f8`

## 1. Purpose

Provides complete unit and regression coverage for the `apply_bess_planning_feature_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from dataclasses import fields, replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from io import BytesIO` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import importlib` — required by the implementation paths and symbols documented below.
- `import inspect` — required by the implementation paths and symbols documented below.
- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from geopandas.testing import assert_geodataframe_equal` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from shapely import from_wkt, get_coordinate_dimension, to_wkb` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import ( LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon, )` — required by the implementation paths and symbols documented below.
- `from test_bess_planning_feature_policy import ( _canonical_empty_policy_result, _checked_in_policy_result, _compiled_fixture, )` — required by the implementation paths and symbols documented below.
- `from test_resolve_planning_feature_codes import _canonical_empty_coded_result` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_bess_planning_feature_policy import ( BessPlanningFeatureApplicationArtifactManifest, BessPlanningFeatureApplicationError, BessPlanningFeatureApplicationResult, apply_bess_planning_feature_policy, validate_bess_planning_feature_application_result, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_bess_planning_feature_policy import ( load_bess_planning_feature_application_artifacts as _load_application_artifacts, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `APPLICATION_SCOPE` | `"FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_COLUMNS` | `( "bess_cnig_policy_application_status", "bess_cnig_precheck_status", "bess_cnig_precheck_confidence", "bess_cnig_status_priority", "bess_cnig_rationale", "bess_cnig_required_human_action", "bess_cnig_limitations", "bess_cnig_application_scope", "bess_cnig_policy_scope", "bess_cnig_local_feature_text_interpreted", "bess_cnig_local_regulation_content_interpreted", "bess_cnig_legal_conclusion_produced", "bess_cnig_parcel_status_aggregated", "bess_cnig_parcel_rejection_performed", "bess_cnig_score_calculated", "bess_cnig_policy_profile", "bess_cnig_policy_sha256", "bess_cnig_policy_result_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `BOUNDARY_FLAG_COLUMNS` | `( "bess_cnig_local_feature_text_interpreted", "bess_cnig_local_regulation_content_interpreted", "bess_cnig_legal_conclusion_produced", "bess_cnig_parcel_status_aggregated", "bess_cnig_parcel_rejection_performed", "bess_cnig_score_calculated", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_FILES` | `{ "SURFACE_FEATURES": ("surface.parquet", True), "LINE_FEATURES": ("line.parquet", True), "POINT_FEATURES": ("point.parquet", True), "RELATIONS": ("relations.parquet", False), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_LAST_CODED_RESULT` | `None` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_LAST_POLICY_RESULT` | `None` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_application_fixture`

**Signature**

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

Implements application fixture according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[tuple[object, ...], object, object, object, BessPlanningFeatureApplicationResult]`. Observed return expression(s): `(inputs, coded, config, policy, result)`.

**Algorithm**

1. Executes `global _LAST_CODED_RESULT, _LAST_POLICY_RESULT`.
2. Computes `(inputs, coded, config, policy)` from `_compiled_fixture()`.
3. Computes `result` from `apply_bess_planning_feature_policy(*inputs, coded, config, policy)`.
4. Computes `_LAST_CODED_RESULT` from `coded`.
5. Computes `_LAST_POLICY_RESULT` from `policy`.
6. Returns `(inputs, coded, config, policy, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_compiled_fixture`, `apply_bess_planning_feature_policy`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_aggregation_fixture`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_build_from_relations`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_relation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_surface_touch_semantic_corruption_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_validate_parcel_geometries`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_one_aggregation_and_one_public_validation_each_call_heavy_once`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_any_true_row_boundary_flag_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_accepts_only_current_policy_and_cnig_source_schemas`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_feature_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_bad_upstream_before_artifact_reads`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_locks_cnig_result_schema_exactly`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_locks_policy_result_schema_exactly`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_manifest_filenames_are_casefold_unique`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_manifest_rejects_nonportable_filename`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_relation_feature_id_is_exact_and_portable`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_relation_parcel_id_is_exact`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_relation_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_artifact_loader_parses_only_verified_bytes`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_artifact_manifest_rejects_invalid_contract`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_complete_relation_facts_must_match_referenced_feature`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_coordinated_application_source_lock_mutation_fast_fails`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_coordinated_feature_or_relation_policy_mutation_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_coordinated_invalid_policy_domains_fail_local_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_coordinated_referenced_row_lineage_cannot_bypass_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_duplicate_application_relation_pair_is_rejected_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_duplicate_relation_identity_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_duplicate_relation_pair_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_every_output_row_has_all_six_false_boundary_flags`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_exact_policy_is_applied_to_every_feature_and_relation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_catalog_geometry_role_is_intrinsic`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_catalog_metric_must_match_geometry`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_catalog_requires_canonical_crs_and_global_identity`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_row_lineage_must_match_application_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_lineage_defect_fast_fails_before_policy_source_validation`
- 32 additional static callers are indexed by the completeness audit.

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_accepts_only_current_policy_and_cnig_source_schemas`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_filenames_are_casefold_unique`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_rejects_nonportable_filename`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_output_row_has_all_six_false_boundary_flags`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_policy_is_applied_to_every_feature_and_relation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_m_and_zm_application_geometries_are_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_policy_suffix_has_one_exact_deterministic_dtype_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_relations_inherit_only_from_referenced_enriched_feature`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_scope_has_no_parcel_output_aggregation_rejection_or_score`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_relation_feature_id_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_empty_optional_application_catalog_retains_schema_and_crs`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `load_bess_planning_feature_application_artifacts`

**Signature**

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

**Inputs**

- `manifest_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`object | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result` (`object | None`; optional/default `None`) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `_load_application_artifacts(manifest_path, surface_features_path, line_features_path, point_features_path, relations_path, coded_result, policy_result)`.

**Algorithm**

1. Checks `coded_result is None or policy_result is None`. When true: Computes `coded_result` from `_LAST_CODED_RESULT`. Computes `policy_result` from `_LAST_POLICY_RESULT`.
2. Asserts `coded_result is not None`.
3. Asserts `policy_result is not None`.
4. Returns `_load_application_artifacts(manifest_path, surface_features_path, line_features_path, point_features_path, relations_path, coded_result, policy_result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_load_application_artifacts`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_load_application_artifacts`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_artifact_loader_parses_only_verified_bytes`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_artifact_manifest_rejects_invalid_contract`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_duplicate_relation_pair_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_manifest_rejects_duplicate_json_key`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_physical_replacement_before_loading_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_factual_prefix_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_wrong_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_z_geoparquet_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_identity_is_validated_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_participates_in_global_policy_mapping`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_valid_four_file_manifest_and_verified_byte_readback`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_small_catalog`

**Signature**

```python
def _small_catalog(*rows: tuple[str, str, str, str, str]) -> gpd.GeoDataFrame:
```

**Purpose**

Implements small catalog according to the exact implementation and guards in this file.

**Inputs**

- `*rows` (`tuple[str, str, str, str, str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `gpd.GeoDataFrame({'planning_feature_id': [row[0] for row in rows], 'feature_family': [row[1] for row in rows], 'type_code_raw': [row[2] for row in rows], 'subtype_code_raw': [row[3] for row in rows], 'official_code_status': [row[4] for row in rows]}, geometry=[Point(position, position) for position in range(len(rows))], crs='EPSG:2154')`.

**Algorithm**

1. Returns `gpd.GeoDataFrame({'planning_feature_id': [row[0] for row in rows], 'feature_family': [row[1] for row in rows], 'type_code_raw': [row[2] for row in rows], 'subtype_code_raw': [row[3] for row in rows], 'official_code_status': [row[4] for row in rows]}, geometry=[Point(position, position) for position in range(len(rows))], crs='EPSG:2154')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `Point`, `gpd.GeoDataFrame`, `len`, `range`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_inconsistent_official_status_and_policy_match_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unknown_pair_remains_present_with_true_null_decision_fields`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_inconsistent_official_status_and_policy_match_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_pair_remains_present_with_true_null_decision_fields`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_application_artifacts`

**Signature**

```python
def _write_application_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

**Purpose**

Writes application artifacts according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[Path, dict[str, Path], dict[str, object]]`. Observed return expression(s): `(manifest_path, paths, manifest)`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Computes `frames` from `{'SURFACE_FEATURES': result.surface_features, 'LINE_FEATURES': result.line_features, 'POINT_FEATURES': result.point_features, 'RELATIONS': result.relations}`.
3. Defines `paths` with annotation `dict[str, Path]` from `{}`.
4. Defines `records` with annotation `list[dict[str, object]]` from `[]`.
5. Iterates `(role, (filename, geospatial))` over `ARTIFACT_FILES.items()`. For each value: Computes `path` from `tmp_path / filename`. Computes `frame` from `frames[role]`. Calls `frame.to_parquet(path, index=True)` for its validation or side effect. Executes 3 additional source-ordered statement(s).
6. Computes `scalar_names` from `tuple((field.name for field in fields(BessPlanningFeatureApplicationResult) if field.name not in {'surface_features', 'line_features', 'point_features', 'relations'}))`.
7. Computes `manifest` from `{'schema_version': 2, 'artifact_kind': 'BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT', **{name: getattr(result, name) for name in scalar_names}, 'artifacts': records}`.
8. Computes `validated` from `BessPlanningFeatureApplicationArtifactManifest.model_validate(manifest)`.
9. Asserts `validated.schema_version == 2`.
10. Computes `manifest_path` from `tmp_path / 'application.json'`.
11. Calls `manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8')` for its validation or side effect.
12. Asserts `module is not None`.
13. Returns `(manifest_path, paths, manifest)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `manifest_path.write_text`, `path.read_bytes`, `sha256(path.read_bytes()).hexdigest`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `ARTIFACT_FILES.items`, `BessPlanningFeatureApplicationArtifactManifest.model_validate`, `deterministic_frame_schema_signature`, `fields`, `frame.to_parquet`, `getattr`, `importlib.import_module`, `json.dumps`, `len`, `manifest_path.write_text`, `path.read_bytes`, `path.stat`, `records.append`, `sha256`, `sha256(path.read_bytes()).hexdigest`, `signature.get`, `tuple`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_bad_upstream_before_artifact_reads`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_manifest_filenames_are_casefold_unique`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_manifest_rejects_nonportable_filename`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_artifact_loader_parses_only_verified_bytes`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_artifact_manifest_rejects_invalid_contract`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_duplicate_relation_pair_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_manifest_rejects_duplicate_json_key`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_physical_replacement_before_loading_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_factual_prefix_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_wrong_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_z_geoparquet_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_application_loader_rejects_locally_valid_rationale_change`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_loader_rejects_all_null_raw_column_transition`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_loader_rejects_factual_prefix_lineage_change`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_identity_is_validated_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_participates_in_global_policy_mapping`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_valid_four_file_manifest_and_verified_byte_readback`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_filenames_are_casefold_unique`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_manifest_rejects_nonportable_filename`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coordinated_policy_mutation`

**Signature**

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

Implements coordinated policy mutation according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `dtype` (`str | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `module._result_with_hashes(replace(changed, relations=relation_frame))`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Computes `feature_id` from `str(result.relations.iloc[0]['planning_feature_id'])`.
3. Computes `changed` from `result`.
4. Iterates `frame_name` over `('surface_features', 'line_features', 'point_features')`. For each value: Computes `frame` from `getattr(changed, frame_name).copy(deep=True)`. Computes `mask` from `frame['planning_feature_id'].eq(feature_id)`. Checks `mask.any()`. When true: Computes `values` from `frame[column].tolist()`. Iterates `(position, selected)` over `enumerate(mask.tolist())`. For each value: Checks `selected`. When true: Computes `values[position]` from `value`. Checks `dtype == 'category'`. When true: Computes `frame[column]` from `pd.Series(pd.Categorical(values), index=frame.index)`. Otherwise: Checks `dtype is not None`. When true: Computes `frame[column]` from `pd.Series(values, index=frame.index, dtype=dtype)`. Otherwise: Computes `frame.loc[mask, column]` from `value`. Executes 1 additional source-ordered statement(s).
5. Computes `relation_frame` from `changed.relations.copy(deep=True)`.
6. Computes `relation_mask` from `relation_frame['planning_feature_id'].eq(feature_id)`.
7. Computes `relation_values` from `relation_frame[column].tolist()`.
8. Iterates `(position, selected)` over `enumerate(relation_mask.tolist())`. For each value: Checks `selected`. When true: Computes `relation_values[position]` from `value`.
9. Checks `dtype == 'category'`. When true: Computes `relation_frame[column]` from `pd.Series(pd.Categorical(relation_values), index=relation_frame.index)`. Otherwise: Checks `dtype is not None`. When true: Computes `relation_frame[column]` from `pd.Series(relation_values, index=relation_frame.index, dtype=dtype)`. Otherwise: Computes `relation_frame.loc[relation_mask, column]` from `value`.
10. Returns `module._result_with_hashes(replace(changed, relations=relation_frame))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `changed.relations.copy`, `getattr(changed, frame_name).copy`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `changed.relations.copy`, `enumerate`, `frame['planning_feature_id'].eq`, `frame[column].tolist`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `mask.any`, `mask.tolist`, `module._result_with_hashes`, `pd.Categorical`, `pd.Series`, `relation_frame['planning_feature_id'].eq`, `relation_frame[column].tolist`, `relation_mask.tolist`, `replace`, `str`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_any_true_row_boundary_flag_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_coordinated_invalid_policy_domains_fail_local_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_literal_null_replacements_are_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_official_and_application_statuses_cannot_contradict`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_wrong_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_wrong_policy_suffix_dtype_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_application_loader_rejects_locally_valid_rationale_change`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coordinated_feature_id_mutation`

**Signature**

```python
def _coordinated_feature_id_mutation(
    result: BessPlanningFeatureApplicationResult,
    feature_id: object,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Implements coordinated feature id mutation according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `feature_id` (`object`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `module._result_with_hashes(replace(changed, relations=relations))`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Computes `original` from `result.relations.iloc[0]['planning_feature_id']`.
3. Computes `changed` from `result`.
4. Iterates `frame_name` over `('surface_features', 'line_features', 'point_features')`. For each value: Computes `frame` from `getattr(changed, frame_name).copy(deep=True)`. Computes `frame.loc[frame['planning_feature_id'].eq(original), 'planning_feature_id']` from `feature_id`. Computes `changed` from `replace(changed, **{frame_name: frame})`.
5. Computes `relations` from `changed.relations.copy(deep=True)`.
6. Computes `relations.loc[relations['planning_feature_id'].eq(original), 'planning_feature_id']` from `feature_id`.
7. Returns `module._result_with_hashes(replace(changed, relations=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `changed.relations.copy`, `getattr(changed, frame_name).copy`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `changed.relations.copy`, `frame['planning_feature_id'].eq`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `relations['planning_feature_id'].eq`, `replace`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_relation_feature_id_is_exact_and_portable`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_zero_relation_feature`

**Signature**

```python
def _zero_relation_feature(
    result: BessPlanningFeatureApplicationResult,
) -> tuple[str, gpd.GeoDataFrame, object]:
```

**Purpose**

Implements zero relation feature according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, gpd.GeoDataFrame, object]`. Observed return expression(s): `(name, frame, unmatched.index[0])`.

**Algorithm**

1. Computes `related` from `set(result.relations['planning_feature_id'])`.
2. Iterates `name` over `('surface_features', 'line_features', 'point_features')`. For each value: Computes `frame` from `getattr(result, name)`. Computes `unmatched` from `frame.loc[~frame['planning_feature_id'].isin(related)]`. Checks `not unmatched.empty`. When true: Returns `(name, frame, unmatched.index[0])`.
3. Raises `AssertionError('fixture must contain a feature having zero relations')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`, `frame['planning_feature_id'].isin`, `getattr`, `set`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_row_lineage_must_match_application_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_lineage_defect_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_resolved_official_row_requires_label_and_envelope_profile`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unknown_official_row_rejects_invented_label_or_url`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_catalog_identity_fields_are_intrinsic`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_identity_is_validated_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_participates_in_global_policy_mapping`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_surface_touch_with_positive_area`

**Signature**

```python
def _surface_touch_with_positive_area(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Implements surface touch with positive area according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `module._result_with_hashes(replace(result, relations=relations))`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Computes `relations` from `result.relations.copy(deep=True)`.
3. Computes `index` from `relations.index[relations['geometry_kind'].eq('SURFACE')][0]`.
4. Asserts `relations.loc[index, 'intersection_area_m2'] > 0`.
5. Computes `relations.loc[index, 'relation_type']` from `'TOUCH_ONLY'`.
6. Returns `module._result_with_hashes(replace(result, relations=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`, `result.relations.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `importlib.import_module`, `module._result_with_hashes`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_surface_touch_semantic_corruption_result`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_z_geometry`

**Signature**

```python
def _z_geometry(kind: str) -> object:
```

**Purpose**

Implements z geometry according to the exact implementation and guards in this file.

**Inputs**

- `kind` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `{'Polygon': polygon, 'MultiPolygon': MultiPolygon([polygon]), 'LineString': line, 'MultiLineString': MultiLineString([line]), 'Point': point, 'MultiPoint': MultiPoint([point])}[kind]`.

**Algorithm**

1. Computes `polygon` from `Polygon([(0, 0, 7), (2, 0, 7), (2, 2, 7), (0, 2, 7)])`.
2. Computes `line` from `LineString([(0, 0, 7), (2, 0, 7)])`.
3. Computes `point` from `Point(1, 1, 7)`.
4. Returns `{'Polygon': polygon, 'MultiPolygon': MultiPolygon([polygon]), 'LineString': line, 'MultiLineString': MultiLineString([line]), 'Point': point, 'MultiPoint': MultiPoint([point])}[kind]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `LineString`, `MultiLineString`, `MultiPoint`, `MultiPolygon`, `Point`, `Polygon`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_and_public_validator_heavy_validation_counts.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.
3. Calls `actual(*args, **kwargs)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_local_result_fast_fails_before_heavy_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_application_source_lock_mutation_fast_fails.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_relation_identity_fast_fails_before_policy_source_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_only_verified_bytes.replace_after_read`

**Signature**

```python
def replace_after_read(path: Path) -> bytes:
```

**Purpose**

Implements replace after read according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `payload`.

**Algorithm**

1. Executes `nonlocal replaced`.
2. Computes `payload` from `original_read_bytes(path)`.
3. Checks `path == target and (not replaced)`. When true: Calls `path.write_bytes(replacement_bytes)` for its validation or side effect. Computes `replaced` from `True`.
4. Returns `payload`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_read_bytes`, `path.write_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `original_read_bytes`, `path.write_bytes`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_only_verified_bytes.observed_read`

**Signature**

```python
def observed_read(source: object, *args: object, **kwargs: object) -> object:
```

**Purpose**

Implements observed read according to the exact implementation and guards in this file.

**Inputs**

- `source` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `original_read_parquet(source, *args, **kwargs)`.

**Algorithm**

1. Checks `isinstance(source, BytesIO)`. When true: Calls `observed.append(('buffer', source.getvalue()))` for its validation or side effect.
2. Returns `original_read_parquet(source, *args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_read_parquet`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `isinstance`, `observed.append`, `original_read_parquet`, `source.getvalue`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_replace_application_frame`

**Signature**

```python
def _replace_application_frame(
    result: BessPlanningFeatureApplicationResult,
    frame_name: str,
    frame: pd.DataFrame,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Implements replace application frame according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame_name` (`str`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `module._result_with_hashes(replace(result, **{frame_name: frame}))`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Returns `module._result_with_hashes(replace(result, **{frame_name: frame}))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `importlib.import_module`, `module._result_with_hashes`, `replace`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_feature_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_relation_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_row_lineage_must_match_application_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_lineage_defect_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_resolved_official_row_requires_label_and_envelope_profile`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_self_consistent_factual_prefix_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unknown_official_row_rejects_invented_label_or_url`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coordinated_referenced_lineage_mutation`

**Signature**

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

Implements coordinated referenced lineage mutation according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `column` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `rename_id` (`bool`; optional/default `False`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `module._result_with_hashes(replace(changed, relations=relations))`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Computes `feature_id` from `str(result.relations.iloc[0]['planning_feature_id'])`.
3. Computes `changed` from `result`.
4. Computes `replacement_id` from `feature_id`.
5. Iterates `frame_name` over `('surface_features', 'line_features', 'point_features')`. For each value: Computes `frame` from `getattr(changed, frame_name).copy(deep=True)`. Computes `mask` from `frame['planning_feature_id'].eq(feature_id)`. Checks `mask.any()`. When true: Computes `frame.loc[mask, column]` from `value`. Checks `rename_id`. When true: Computes `row` from `frame.loc[mask].iloc[0]`. Computes `replacement_id` from `f"GPU:{row['source_document_id']}:{row['logical_layer']}:{row['source_feature_id']}"`. Computes `frame.loc[mask, 'planning_feature_id']` from `replacement_id`. Computes `changed` from `replace(changed, **{frame_name: frame})`.
6. Computes `relations` from `changed.relations.copy(deep=True)`.
7. Computes `mask` from `relations['planning_feature_id'].eq(feature_id)`.
8. Computes `relations.loc[mask, column]` from `value`.
9. Checks `rename_id`. When true: Computes `relations.loc[mask, 'planning_feature_id']` from `replacement_id`.
10. Returns `module._result_with_hashes(replace(changed, relations=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `changed.relations.copy`, `getattr(changed, frame_name).copy`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `changed.relations.copy`, `frame['planning_feature_id'].eq`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `mask.any`, `module._result_with_hashes`, `relations['planning_feature_id'].eq`, `replace`, `str`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_coordinated_referenced_row_lineage_cannot_bypass_envelope`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_lineage_defect_fast_fails_before_policy_source_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_swap_referenced_feature_values`

**Signature**

```python
def _swap_referenced_feature_values(
    result: BessPlanningFeatureApplicationResult,
    columns: tuple[str, ...],
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Implements swap referenced feature values according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `module._result_with_hashes(replace(changed, relations=relations))`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Computes `referenced` from `result.relations.loc[result.relations['bess_cnig_policy_application_status'].eq('APPLIED_EXACT_POLICY')]`.
3. Computes `first` from `referenced.iloc[0]`.
4. Computes `second` from `referenced.loc[referenced['bess_cnig_precheck_status'].ne(first['bess_cnig_precheck_status'])].iloc[0]`.
5. Computes `first_id` from `str(first['planning_feature_id'])`.
6. Computes `second_id` from `str(second['planning_feature_id'])`.
7. Computes `changed` from `result`.
8. Iterates `frame_name` over `('surface_features', 'line_features', 'point_features')`. For each value: Computes `frame` from `getattr(changed, frame_name).copy(deep=True)`. Computes `first_mask` from `frame['planning_feature_id'].eq(first_id)`. Computes `second_mask` from `frame['planning_feature_id'].eq(second_id)`. Executes 1 additional source-ordered statement(s).
9. Computes `relations` from `changed.relations.copy(deep=True)`.
10. Computes `first_mask` from `relations['planning_feature_id'].eq(first_id)`.
11. Computes `second_mask` from `relations['planning_feature_id'].eq(second_id)`.
12. Iterates `column` over `columns`. For each value: Computes `first_value` from `first[column]`. Computes `second_value` from `second[column]`. Computes `relations.loc[first_mask, column]` from `second_value`. Executes 1 additional source-ordered statement(s).
13. Returns `module._result_with_hashes(replace(changed, relations=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `changed.relations.copy`, `getattr(changed, frame_name).copy`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `changed.relations.copy`, `first_mask.any`, `frame['planning_feature_id'].eq`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `referenced['bess_cnig_precheck_status'].ne`, `relations['planning_feature_id'].eq`, `replace`, `result.relations['bess_cnig_policy_application_status'].eq`, `second_mask.any`, `str`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps.forbidden_heavy`

**Signature**

```python
def forbidden_heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements forbidden heavy according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal heavy_calls`.
2. Updates `heavy_calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.coded_envelope`

**Signature**

```python
def coded_envelope(value: object) -> None:
```

**Purpose**

Implements coded envelope according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['coded']` using `` and `1`.
2. Calls `actual_coded_envelope(value)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual_coded_envelope`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.policy_envelope`

**Signature**

```python
def policy_envelope(value: object) -> None:
```

**Purpose**

Implements policy envelope according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['policy']` using `` and `1`.
2. Calls `actual_policy_envelope(value)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual_policy_envelope`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.build`

**Signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Builds build according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `actual_build(*args, **kwargs)`.

**Algorithm**

1. Updates `calls['build']` using `` and `1`.
2. Returns `actual_build(*args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual_build`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight.heavy`

**Signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements heavy according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['heavy']` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_bad_upstream_before_artifact_reads.counted`

**Signature**

```python
def counted(path: Path) -> bytes:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `original(path)`.

**Algorithm**

1. Executes `nonlocal reads`.
2. Updates `reads` using `` and `1`.
3. Returns `original(path)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `original`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_compatible_policy_mutation`

**Signature**

```python
def _compatible_policy_mutation(policy: object, mutation: str) -> object:
```

**Purpose**

Implements compatible policy mutation according to the exact implementation and guards in this file.

**Inputs**

- `policy` (`object`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `mutation` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `module._result_with_hashes(changed)`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
2. Computes `table` from `policy.policy_table.copy(deep=True)`.
3. Defines `scalar_changes` with annotation `dict[str, object]` from `{}`.
4. Checks `mutation == 'profile-schema'`. When true: Computes `scalar_changes['cnig_profile_schema_version']` from `3`. Otherwise: Checks `mutation == 'extra-pair'`. When true: Computes `extra` from `table.iloc[[0]].copy(deep=True)`. Computes `extra['type_code']` from `pd.array(['98'], dtype='str')`. Computes `table` from `pd.concat([table, extra], ignore_index=True).sort_values(['feature_family', 'type_code', 'subtype_code'], kind='stable')`. Executes 1 additional source-ordered statement(s). Otherwise: Checks `mutation == 'missing-pair'`. When true: Computes `table` from `table.iloc[:-1].copy(deep=True)`. Computes `table.index` from `pd.Index(range(len(table)), dtype='int64')`. Otherwise: Checks `mutation == 'official-label'`. When true: Computes `table.loc[table.index[0], 'official_label']` from `'Another exact official label'`. Otherwise: Checks `mutation == 'legal-reference'`. When true: Computes `table.loc[table.index[0], 'official_legal_reference']` from `'Changed legal ref'`. Otherwise: Checks `mutation == 'regulation-reference'`. When true: Computes `table.loc[table.index[0], 'official_regulation_reference']` from `'Changed regulation ref'`. Otherwise: Checks `mutation == 'document'`. When true: Computes `scalar_changes['source_document_id']` from `'OTHER-DOCUMENT'`. Otherwise: Checks `mutation == 'archive'`. When true: Computes `scalar_changes['source_archive_sha256']` from `'b' * 64`. Otherwise: Checks `mutation == 'profile'`. When true: Computes `scalar_changes['cnig_profile']` from `'other-cnig-profile'`. Computes `table['cnig_profile']` from `pd.array(['other-cnig-profile'] * len(table), dtype='str')`. Otherwise: Checks `mutation == 'profile-sha'`. When true: Computes `scalar_changes['cnig_profile_sha256']` from `'a' * 64`. Computes `table['cnig_profile_sha256']` from `pd.array(['a' * 64] * len(table), dtype='str')`. Otherwise: Computes `scalar_changes['cnig_complete_result_content_sha256']` from `'a' * 64`. Computes `table['cnig_complete_result_content_sha256']` from `pd.array(['a' * 64] * len(table), dtype='str')`.
5. Computes `changed` from `replace(policy, policy_table=table, **scalar_changes)`.
6. Returns `module._result_with_hashes(changed)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `policy.policy_table.copy`, `replace`, `table.iloc[:-1].copy`, `table.iloc[[0]].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `importlib.import_module`, `len`, `module._result_with_hashes`, `pd.Index`, `pd.array`, `pd.concat`, `pd.concat([table, extra], ignore_index=True).sort_values`, `policy.policy_table.copy`, `range`, `replace`, `table.iloc[:-1].copy`, `table.iloc[[0]].copy`, `table.index.to_numpy`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.manifest_read`

**Signature**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
```

**Purpose**

Implements manifest read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['manifest']` using `` and `1`.
2. Raises `AssertionError('manifest read must not run')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.read`

**Signature**

```python
def read(*args: object, **kwargs: object) -> object:
```

**Purpose**

Reads and validates read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['read']` using `` and `1`.
2. Raises `AssertionError('artifact read must not run')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.build`

**Signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Builds build according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['build']` using `` and `1`.
2. Raises `AssertionError('application rebuild must not run')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild.heavy`

**Signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements heavy according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['heavy']` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.manifest_read`

**Signature**

```python
def manifest_read(*args: object, **kwargs: object) -> str:
```

**Purpose**

Implements manifest read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['manifest']` using `` and `1`.
2. Raises `AssertionError('manifest read must not run')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.artifact_read`

**Signature**

```python
def artifact_read(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements artifact read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['read']` using `` and `1`.
2. Raises `AssertionError('Parquet read must not run')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.build`

**Signature**

```python
def build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Builds build according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['build']` using `` and `1`.
2. Raises `AssertionError('application rebuild must not run')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild.heavy`

**Signature**

```python
def heavy(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements heavy according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['heavy']` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_policy_is_applied_to_every_feature_and_relation`

**Signature**

```python
def test_exact_policy_is_applied_to_every_feature_and_relation() -> None:
```

**Purpose**

Protects the `exact policy is applied to every feature and relation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, coded, policy_config, policy, result)` from `_application_fixture()`.
- Computes `lookup` from `policy.policy_table.set_index(['feature_family', 'type_code', 'subtype_code'])`.

**Action**

- Calls `_application_fixture`, `applied.itertuples`, `applied['bess_cnig_policy_application_status'].eq`, `applied['bess_cnig_policy_application_status'].eq('APPLIED_EXACT_POLICY').all`, `policy.policy_table.set_index`, `result.relations['bess_cnig_policy_application_status'].eq`, `result.relations['bess_cnig_policy_application_status'].eq('APPLIED_EXACT_POLICY').all`.

**Expected result**

- Direct assertions: `assert result.result_hash_schema_version == 2`; `assert result.application_scope == APPLICATION_SCOPE`; `assert result.policy_profile == policy.policy_profile`; `assert result.policy_sha256 == policy.policy_sha256`; `assert result.policy_complete_result_content_sha256 == policy.complete_result_content_sha256`; `assert result.relations['bess_cnig_policy_application_status'].eq('APPLIED_EXACT_POLICY').all()`; `assert policy_config.policy_scope == result.policy_scope`; `assert tuple(applied.columns[:len(source.columns)]) == tuple(source.columns)`; `assert applied['bess_cnig_policy_application_status'].eq('APPLIED_EXACT_POLICY').all()`; `assert row.bess_cnig_precheck_status == expected.precheck_status`; `assert row.bess_cnig_precheck_confidence == expected.confidence`; `assert row.bess_cnig_status_priority == expected.status_priority`; `assert row.bess_cnig_rationale == expected.rationale`; `assert row.bess_cnig_required_human_action == expected.required_human_action`; `assert row.bess_cnig_limitations == expected.limitations`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact policy is applied to every feature and relation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `applied.itertuples`, `applied['bess_cnig_policy_application_status'].eq`, `applied['bess_cnig_policy_application_status'].eq('APPLIED_EXACT_POLICY').all`, `len`, `policy.policy_table.set_index`, `result.relations['bess_cnig_policy_application_status'].eq`, `result.relations['bess_cnig_policy_application_status'].eq('APPLIED_EXACT_POLICY').all`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_output_row_has_all_six_false_boundary_flags`

**Signature**

```python
def test_every_output_row_has_all_six_false_boundary_flags() -> None:
```

**Purpose**

Protects the `every output row has all six false boundary flags` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.

**Action**

- Calls `_application_fixture`, `all`, `frame[column].eq`, `frame[column].eq(False).all`, `frame[column].notna`, `frame[column].notna().all`.

**Expected result**

- Direct assertions: `assert all((column in frame.columns for column in BOUNDARY_FLAG_COLUMNS))`; `assert str(frame[column].dtype) == 'bool'`; `assert frame[column].notna().all()`; `assert frame[column].eq(False).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `every output row has all six false boundary flags` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `all`, `frame[column].eq`, `frame[column].eq(False).all`, `frame[column].notna`, `frame[column].notna().all`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_suffix_has_one_exact_deterministic_dtype_schema`

**Signature**

```python
def test_policy_suffix_has_one_exact_deterministic_dtype_schema() -> None:
```

**Purpose**

Protects the `policy suffix has one exact deterministic dtype schema` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `expected` from `{column: 'str' for column in POLICY_COLUMNS if column not in {'bess_cnig_status_priority', *BOUNDARY_FLAG_COLUMNS}}`.
- Computes `expected['bess_cnig_status_priority']` from `'Int64'`.

**Action**

- Calls `_application_fixture`, `expected.update`.

**Expected result**

- Direct assertions: `assert tuple(frame.columns[-len(POLICY_COLUMNS):]) == POLICY_COLUMNS`; `assert {column: str(frame[column].dtype) for column in POLICY_COLUMNS} == expected`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy suffix has one exact deterministic dtype schema` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `expected.update`, `len`, `str`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_schema_v1_dimension_blind_hash_representation_is_rejected_locally`

**Signature**

```python
def test_schema_v1_dimension_blind_hash_representation_is_rejected_locally() -> None:
```

**Purpose**

Protects the `schema v1 dimension blind hash representation is rejected locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 9 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `original` from `surface.geometry.iloc[0]`.
- Computes `polygon_z` from `Polygon([(x, y, 7) for x, y in original.exterior.coords])`.
- Computes `surface.at[surface.index[0], surface.geometry.name]` from `polygon_z`.
- Computes `blind` from `replace(result, surface_features=surface)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')` and executes: Calls `module._validate_result_envelope(blind)` for its validation or side effect.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')` and executes: Calls `module._result_with_hashes(blind)` for its validation or side effect.

**Action**

- Calls `Polygon`, `_application_fixture`, `get_coordinate_dimension`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `result.surface_features.copy`, `to_wkb`.

**Expected result**

- Direct assertions: `assert get_coordinate_dimension(original) == 2`; `assert get_coordinate_dimension(polygon_z) == 3`; `assert to_wkb(original, hex=True, output_dimension=2) == to_wkb(polygon_z, hex=True, output_dimension=2)`; `assert blind.surface_features_content_sha256 == result.surface_features_content_sha256`; `assert blind.complete_result_content_sha256 == result.complete_result_content_sha256`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension'): module._validate_result_envelope(blind)`; `with pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension'): module._result_with_hashes(blind)`.

**Regression protected**

- Protects the exact `schema v1 dimension blind hash representation is rejected locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_application_fixture`, `get_coordinate_dimension`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.raises`, `replace`, `result.surface_features.copy`, `to_wkb`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation`

**Signature**

```python
def test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
    frame_name: str,
    geometry_kind: str,
) -> None:
```

**Purpose**

Protects the `every non 2d application geometry kind fast fails before source validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`, `frame_name`, `geometry_kind`.
- Contains 7 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `frame` from `getattr(result, frame_name).copy(deep=True)`.
- Computes `frame.at[frame.index[0], frame.geometry.name]` from `_z_geometry(geometry_kind)`.
- Computes `changed` from `replace(result, **{frame_name: frame})`.
- Computes `calls` from `0`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')` and executes: Calls `module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_z_geometry`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `replace`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension'): module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)`.

**Regression protected**

- Protects the exact `every non 2d application geometry kind fast fails before source validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_z_geometry`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_m_and_zm_application_geometries_are_rejected`

**Signature**

```python
def test_m_and_zm_application_geometries_are_rejected(wkt: str) -> None:
```

**Purpose**

Protects the `m and zm application geometries are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `wkt`.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `point` from `result.point_features.copy(deep=True)`.
- Computes `point.at[point.index[0], point.geometry.name]` from `from_wkt(wkt)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')` and executes: Calls `module._validate_result_envelope(replace(result, point_features=point))` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `from_wkt`, `importlib.import_module`, `module._validate_result_envelope`, `replace`, `result.point_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension'): module._validate_result_envelope(replace(result, point_features=point))`.

**Regression protected**

- Protects the exact `m and zm application geometries are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `from_wkt`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.point_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_empty_optional_application_catalog_retains_schema_and_crs`

**Signature**

```python
def test_valid_empty_optional_application_catalog_retains_schema_and_crs() -> None:
```

**Purpose**

Protects the `valid empty optional application catalog retains schema and crs` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, coded, _, policy, _)` from `_application_fixture()`.
- Computes `empty` from `coded.point_features.iloc[0:0].copy()`.
- Computes `applied` from `module._apply_feature_catalog(empty, policy)`.

**Action**

- Calls `_application_fixture`, `coded.point_features.iloc[0:0].copy`, `importlib.import_module`, `module._apply_feature_catalog`, `module._validate_application_geometry`.

**Expected result**

- Direct assertions: `assert applied.empty`; `assert tuple(applied.columns[:len(empty.columns)]) == tuple(empty.columns)`; `assert tuple(applied.columns[-len(POLICY_COLUMNS):]) == POLICY_COLUMNS`; `assert applied.geometry.name == empty.geometry.name`; `assert applied.crs == empty.crs`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid empty optional application catalog retains schema and crs` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `coded.point_features.iloc[0:0].copy`, `importlib.import_module`, `len`, `module._apply_feature_catalog`, `module._validate_application_geometry`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`

**Signature**

```python
def test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct() -> None:
```

**Purpose**

Protects the `exact pair identity keeps family subtype and leading zeroes distinct` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `policy` from `_checked_in_policy_result()`.
- Computes `catalog` from `_small_catalog(('F-1500', 'PRESCRIPTION', '15', '00', 'RESOLVED_OFFICIAL'), ('F-1501', 'PRESCRIPTION', '15', '01', 'RESOLVED_OFFICIAL'), ('F-NO-SUBTYPE', 'PRESCRIPTION', '15', '99', 'UNKNOWN_CODE_PAIR'), ('F-NO-FAMILY', 'INFORMATION', '15', '00', 'UNKNOWN_CODE_PAIR'), ('F-0100', 'PRESCRIPTION', '01', '00', 'RESOLVED_O…`.
- Computes `applied` from `module._apply_feature_catalog(catalog, policy)`.

**Action**

- Calls `_checked_in_policy_result`, `_small_catalog`, `importlib.import_module`, `module._apply_feature_catalog`.

**Expected result**

- Direct assertions: `assert applied.loc[0, 'bess_cnig_precheck_confidence'] == 'MEDIUM'`; `assert applied.loc[1, 'bess_cnig_precheck_confidence'] == 'HIGH'`; `assert applied.loc[0, 'bess_cnig_precheck_status'] == 'DESIGN_REVIEW_REQUIRED'`; `assert applied.loc[1, 'bess_cnig_precheck_status'] == 'DESIGN_REVIEW_REQUIRED'`; `assert applied.loc[2, 'bess_cnig_policy_application_status'] == 'UNRESOLVED_CODE_PAIR'`; `assert applied.loc[3, 'bess_cnig_policy_application_status'] == 'UNRESOLVED_CODE_PAIR'`; `assert applied.loc[4, 'type_code_raw'] == '01'`; `assert applied.loc[4, 'subtype_code_raw'] == '00'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact pair identity keeps family subtype and leading zeroes distinct` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_checked_in_policy_result`, `_small_catalog`, `importlib.import_module`, `module._apply_feature_catalog`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_pair_remains_present_with_true_null_decision_fields`

**Signature**

```python
def test_unknown_pair_remains_present_with_true_null_decision_fields() -> None:
```

**Purpose**

Protects the `unknown pair remains present with true null decision fields` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `policy` from `_checked_in_policy_result()`.
- Computes `catalog` from `_small_catalog(('F-UNKNOWN', 'PRESCRIPTION', '98', '00', 'UNKNOWN_CODE_PAIR'))`.
- Computes `applied` from `module._apply_feature_catalog(catalog, policy)`.

**Action**

- Calls `_checked_in_policy_result`, `_small_catalog`, `applied['planning_feature_id'].tolist`, `importlib.import_module`, `isinstance`, `module._apply_feature_catalog`, `pd.isna`.

**Expected result**

- Direct assertions: `assert applied['planning_feature_id'].tolist() == ['F-UNKNOWN']`; `assert applied.loc[0, 'bess_cnig_policy_application_status'] == 'UNRESOLVED_CODE_PAIR'`; `assert pd.isna(applied.loc[0, column])`; `assert not isinstance(applied.loc[0, column], str)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `unknown pair remains present with true null decision fields` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_checked_in_policy_result`, `_small_catalog`, `applied['planning_feature_id'].tolist`, `importlib.import_module`, `isinstance`, `module._apply_feature_catalog`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_inconsistent_official_status_and_policy_match_is_rejected`

**Signature**

```python
def test_inconsistent_official_status_and_policy_match_is_rejected(
    row: tuple[str, str, str, str, str],
) -> None:
```

**Purpose**

Protects the `inconsistent official status and policy match is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `row`.
- Contains 2 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='policy|official')` and executes: Calls `module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())` for its validation or side effect.

**Action**

- Calls `_checked_in_policy_result`, `_small_catalog`, `importlib.import_module`, `module._apply_feature_catalog`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='policy|official'): module._apply_feature_catalog(_small_catalog(row), _checked_in_policy_result())`.

**Regression protected**

- Protects the exact `inconsistent official status and policy match is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_checked_in_policy_result`, `_small_catalog`, `importlib.import_module`, `module._apply_feature_catalog`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_feature_and_relation_inputs_are_preserved_and_not_mutated`

**Signature**

```python
def test_feature_and_relation_inputs_are_preserved_and_not_mutated() -> None:
```

**Purpose**

Protects the `feature and relation inputs are preserved and not mutated` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy)` from `_compiled_fixture()`.
- Computes `coded_copies` from `(coded.surface_features.copy(deep=True), coded.line_features.copy(deep=True), coded.point_features.copy(deep=True), coded.relations.copy(deep=True))`.
- Computes `parcels_copy` from `inputs[1].copy(deep=True)`.
- Computes `result` from `apply_bess_planning_feature_policy(*inputs, coded, config, policy)`.
- Computes `relation_prefix` from `result.relations.loc[:, coded.relations.columns]`.

**Action**

- Calls `_compiled_fixture`, `applied.index.equals`, `apply_bess_planning_feature_policy`, `coded.line_features.copy`, `coded.point_features.copy`, `coded.relations.copy`, `coded.surface_features.copy`, `inputs[1].copy`, `type`.

**Expected result**

- Direct assertions: `assert tuple(result.relations.columns[-len(POLICY_COLUMNS):]) == POLICY_COLUMNS`; `assert tuple(applied.columns[-len(POLICY_COLUMNS):]) == POLICY_COLUMNS`; `assert type(applied.index) is type(source.index)`; `assert applied.index.equals(source.index)`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `feature and relation inputs are preserved and not mutated` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `applied.index.equals`, `apply_bess_planning_feature_policy`, `assert_frame_equal`, `assert_geodataframe_equal`, `coded.line_features.copy`, `coded.point_features.copy`, `coded.relations.copy`, `coded.surface_features.copy`, `inputs[1].copy`, `len`, `tuple`, `type`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relations_inherit_only_from_referenced_enriched_feature`

**Signature**

```python
def test_relations_inherit_only_from_referenced_enriched_feature() -> None:
```

**Purpose**

Protects the `relations inherit only from referenced enriched feature` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `features` from `pd.concat([result.surface_features.drop(columns='geometry'), result.line_features.drop(columns='geometry'), result.point_features.drop(columns='geometry')], ignore_index=True).set_index('planning_feature_id')`.

**Action**

- Calls `_application_fixture`, `getattr`, `pd.concat`, `pd.concat([result.surface_features.drop(columns='geometry'), result.line_features.drop(columns='geometry'), result.point_features.drop(columns='geometry')], ignore_index=True).set_index`, `result.line_features.drop`, `result.point_features.drop`, `result.relations.itertuples`, `result.surface_features.drop`.

**Expected result**

- Direct assertions: `assert getattr(relation, column) == feature[column]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `relations inherit only from referenced enriched feature` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `getattr`, `pd.concat`, `pd.concat([result.surface_features.drop(columns='geometry'), result.line_features.drop(columns='geometry'), result.point_features.drop(columns='geometry')], ignore_index=True).set_index`, `result.line_features.drop`, `result.point_features.drop`, `result.relations.itertuples`, `result.surface_features.drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_relation_facts_must_match_referenced_feature`

**Signature**

```python
def test_complete_relation_facts_must_match_referenced_feature(
    column: str, value: object
) -> None:
```

**Purpose**

Protects the `complete relation facts must match referenced feature` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 7 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `index` from `relations.index[relations['geometry_kind'].eq('SURFACE')][0]`.
- Computes `relations.loc[index, column]` from `value`.
- Computes `changed` from `module._result_with_hashes(replace(result, relations=relations))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='relation|feature')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='relation|feature'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `complete relation facts must match referenced feature` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `relations['geometry_kind'].eq`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_relation_feature_id_is_rejected`

**Signature**

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
```

**Purpose**

Protects the `unknown relation feature id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `relations` from `coded.relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'planning_feature_id']` from `'GPU:UNKNOWN'`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='feature ID')` and executes: Calls `module._apply_relations(relations, result.surface_features, result.line_features, result.point_features)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `coded.relations.copy`, `importlib.import_module`, `module._apply_relations`.

**Expected result**

- Direct assertions: `assert policy is not None`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='feature ID'): module._apply_relations(relations, result.surface_features, result.line_features, result.point_features)`.

**Regression protected**

- Protects the exact `unknown relation feature id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `coded.relations.copy`, `importlib.import_module`, `module._apply_relations`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_scope_has_no_parcel_output_aggregation_rejection_or_score`

**Signature**

```python
def test_scope_has_no_parcel_output_aggregation_rejection_or_score() -> None:
```

**Purpose**

Protects the `scope has no parcel output aggregation rejection or score` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `(inputs, _, _, _, result)` from `_application_fixture()`.

**Action**

- Calls `_application_fixture`, `hasattr`.

**Expected result**

- Direct assertions: `assert not hasattr(result, 'parcels')`; `assert result.local_feature_text_interpreted is False`; `assert result.local_regulation_content_interpreted is False`; `assert result.legal_conclusion_produced is False`; `assert result.parcel_status_aggregated is False`; `assert result.parcel_rejection_performed is False`; `assert result.score_calculated is False`; `assert 'parcel_id' not in result.surface_features.columns`; `assert len(inputs[1]) > 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `scope has no parcel output aggregation rejection or score` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `hasattr`, `len`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_feature_or_relation_policy_mutation_is_rejected`

**Signature**

```python
def test_coordinated_feature_or_relation_policy_mutation_is_rejected() -> None:
```

**Purpose**

Protects the `coordinated feature or relation policy mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 10 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `surface.loc[surface.index[0], 'bess_cnig_precheck_status']` from `'UNKNOWN'`.
- Computes `coordinated` from `module._result_with_hashes(replace(result, surface_features=surface))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='rebuilt|feature')` and executes: Calls `validate_bess_planning_feature_application_result(*inputs, coded, config, policy, coordinated)` for its validation or side effect.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'bess_cnig_precheck_confidence']` from `'LOW'`.
- Computes `coordinated` from `module._result_with_hashes(replace(result, relations=relations))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='relation|rebuilt')` and executes: Calls `validate_bess_planning_feature_application_result(*inputs, coded, config, policy, coordinated)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `replace`, `result.relations.copy`, `result.surface_features.copy`, `validate_bess_planning_feature_application_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='rebuilt|feature'): validate_bess_planning_feature_application_result(*inputs, coded, config, policy, coordinated)`; `with pytest.raises(BessPlanningFeatureApplicationError, match='relation|rebuilt'): validate_bess_planning_feature_application_result(*inputs, coded, config, policy, coordinated)`.

**Regression protected**

- Protects the exact `coordinated feature or relation policy mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `pytest.raises`, `replace`, `result.relations.copy`, `result.surface_features.copy`, `validate_bess_planning_feature_application_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_application_relation_pair_is_rejected_locally`

**Signature**

```python
def test_duplicate_application_relation_pair_is_rejected_locally() -> None:
```

**Purpose**

Protects the `duplicate application relation pair is rejected locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `relations` from `pd.concat([result.relations, result.relations.iloc[[0]]])`.
- Computes `changed` from `module._result_with_hashes(replace(result, relations=relations))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pd.concat`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `duplicate application relation pair is rejected locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pd.concat`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_relation_feature_id_is_exact_and_portable`

**Signature**

```python
def test_application_relation_feature_id_is_exact_and_portable(
    feature_id: object,
) -> None:
```

**Purpose**

Protects the `application relation feature id is exact and portable` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `feature_id`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_feature_id_mutation(result, feature_id)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='feature|identity')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_feature_id_mutation`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='feature|identity'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `application relation feature id is exact and portable` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_feature_id_mutation`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_relation_parcel_id_is_exact`

**Signature**

```python
def test_application_relation_parcel_id_is_exact(parcel_id: object) -> None:
```

**Purpose**

Protects the `application relation parcel id is exact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcel_id`.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'parcel_id']` from `parcel_id`.
- Computes `changed` from `module._result_with_hashes(replace(result, relations=relations))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='parcel|identity')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='parcel|identity'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `application relation parcel id is exact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_application_relation_type_is_rejected_locally`

**Signature**

```python
def test_unknown_application_relation_type_is_rejected_locally() -> None:
```

**Purpose**

Protects the `unknown application relation type is rejected locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `relations` from `result.relations.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'relation_type']` from `'BUFFERED_NEARBY'`.
- Computes `changed` from `module._result_with_hashes(replace(result, relations=relations))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='relation type')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='relation type'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `unknown application relation type is rejected locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.raises`, `replace`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_invalid_policy_domains_fail_local_validation`

**Signature**

```python
def test_coordinated_invalid_policy_domains_fail_local_validation(
    column: str,
    value: object,
    message: str,
) -> None:
```

**Purpose**

Protects the `coordinated invalid policy domains fail local validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`, `message`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_policy_mutation(result, column, value)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match=message)` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match=message): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `coordinated invalid policy domains fail local validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_literal_null_replacements_are_rejected`

**Signature**

```python
def test_literal_null_replacements_are_rejected(literal: str) -> None:
```

**Purpose**

Protects the `literal null replacements are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `literal`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_policy_mutation(result, 'bess_cnig_rationale', literal)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='literal|missing')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='literal|missing'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `literal null replacements are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_self_consistent_wrong_policy_suffix_dtype_is_rejected`

**Signature**

```python
def test_self_consistent_wrong_policy_suffix_dtype_is_rejected(
    column: str,
    dtype: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `self consistent wrong policy suffix dtype is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `dtype`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_policy_mutation(result, column, value, dtype=dtype)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='dtype|schema')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='dtype|schema'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `self consistent wrong policy suffix dtype is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_official_and_application_statuses_cannot_contradict`

**Signature**

```python
def test_official_and_application_statuses_cannot_contradict(
    official_status: str,
    application_status: str,
) -> None:
```

**Purpose**

Protects the `official and application statuses cannot contradict` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `official_status`, `application_status`.
- Contains 8 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_policy_mutation(result, 'bess_cnig_policy_application_status', application_status)`.
- Computes `feature_id` from `str(changed.relations.iloc[0]['planning_feature_id'])`.
- Computes `relation_frame` from `changed.relations.copy(deep=True)`.
- Computes `relation_frame.loc[relation_frame['planning_feature_id'].eq(feature_id), 'official_code_status']` from `official_status`.
- Computes `changed` from `module._result_with_hashes(replace(changed, relations=relation_frame))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='official|status')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `changed.relations.copy`, `frame['planning_feature_id'].eq`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `mask.any`, `module._result_with_hashes`, `module._validate_result_envelope`, `relation_frame['planning_feature_id'].eq`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='official|status'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `official and application statuses cannot contradict` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `changed.relations.copy`, `frame['planning_feature_id'].eq`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `mask.any`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `relation_frame['planning_feature_id'].eq`, `replace`, `str`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_any_true_row_boundary_flag_is_rejected`

**Signature**

```python
def test_any_true_row_boundary_flag_is_rejected(column: str) -> None:
```

**Purpose**

Protects the `any true row boundary flag is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_policy_mutation(result, column, True)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='flag|false')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='flag|false'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `any true row boundary flag is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_and_public_validator_heavy_validation_counts`

**Signature**

```python
def test_application_and_public_validator_heavy_validation_counts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `application and public validator heavy validation counts` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy)` from `_compiled_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `actual` from `module.validate_bess_planning_feature_policy_result`.
- Computes `calls` from `0`.
- Computes `result` from `module.apply_bess_planning_feature_policy(*inputs, coded, config, policy)`.

**Action**

- Calls `_compiled_fixture`, `actual`, `importlib.import_module`, `module.apply_bess_planning_feature_policy`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert calls == 1`; `assert calls == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `application and public validator heavy validation counts` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `actual`, `importlib.import_module`, `module.apply_bess_planning_feature_policy`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_local_result_fast_fails_before_heavy_validation`

**Signature**

```python
def test_malformed_local_result_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `malformed local result fast fails before heavy validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `calls` from `0`.
- Computes `invalid` from `replace(result, complete_result_content_sha256='f' * 64)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='hash|SHA|sha256|invalid')` and executes: Calls `module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, invalid)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `replace`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='hash|SHA|sha256|invalid'): module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, invalid)`.

**Regression protected**

- Protects the exact `malformed local result fast fails before heavy validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_application_source_lock_mutation_fast_fails`

**Signature**

```python
def test_coordinated_application_source_lock_mutation_fast_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `coordinated application source lock mutation fast fails` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 8 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `calls` from `0`.
- Computes `changed` from `replace(result, policy_sha256='f' * 64)`.
- Computes `relation_frame` from `changed.relations.copy(deep=True)`.
- Computes `relation_frame['bess_cnig_policy_sha256']` from `pd.array(['f' * 64] * len(relation_frame), dtype='str')`.
- Computes `changed` from `module._result_with_hashes(replace(changed, relations=relation_frame))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='source lock')` and executes: Calls `module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `changed.relations.copy`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `pd.array`, `replace`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='source lock'): module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)`.

**Regression protected**

- Protects the exact `coordinated application source lock mutation fast fails` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `changed.relations.copy`, `getattr`, `getattr(changed, frame_name).copy`, `importlib.import_module`, `len`, `module._result_with_hashes`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `pd.array`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_four_file_manifest_and_verified_byte_readback`

**Signature**

```python
def test_valid_four_file_manifest_and_verified_byte_readback(tmp_path: Path) -> None:
```

**Purpose**

Protects the `valid four file manifest and verified byte readback` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, result)` from `_application_fixture()`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `loaded` from `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `validate_bess_planning_feature_application_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid four file manifest and verified byte readback` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `assert_frame_equal`, `assert_geodataframe_equal`, `load_bess_planning_feature_application_artifacts`, `validate_bess_planning_feature_application_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_relation_pair_artifact_fails_local_loading`

**Signature**

```python
def test_duplicate_relation_pair_artifact_fails_local_loading(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate relation pair artifact fails local loading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `relations` from `pd.concat([result.relations, result.relations.iloc[[0]]])`.
- Computes `changed` from `module._result_with_hashes(replace(result, relations=relations))`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `importlib.import_module`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `pd.concat`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `duplicate relation pair artifact fails local loading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `importlib.import_module`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `pd.concat`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_wide_mapping_conflict_artifact_fails_local_loading`

**Signature**

```python
def test_document_wide_mapping_conflict_artifact_fails_local_loading(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `document wide mapping conflict artifact fails local loading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `first` from `result.relations.iloc[0]`.
- Computes `different` from `result.relations[result.relations['bess_cnig_precheck_status'].ne(first['bess_cnig_precheck_status'])].iloc[0]`.
- Computes `changed` from `_coordinated_policy_mutation(result, 'bess_cnig_status_priority', int(different['bess_cnig_status_priority']))`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='priority|mapping')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `_write_application_artifacts`, `int`, `load_bess_planning_feature_application_artifacts`, `result.relations['bess_cnig_precheck_status'].ne`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='priority|mapping'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `document wide mapping conflict artifact fails local loading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `_write_application_artifacts`, `int`, `load_bess_planning_feature_application_artifacts`, `pytest.raises`, `result.relations['bess_cnig_precheck_status'].ne`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact`

**Signature**

```python
def test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `positive surface overlap cannot be relabelled touch only in artifact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_surface_touch_with_positive_area(result)`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='surface|metric|type')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_surface_touch_with_positive_area`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='surface|metric|type'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `positive surface overlap cannot be relabelled touch only in artifact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_surface_touch_with_positive_area`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_wrong_2d_feature_geometry_fails_local_artifact_loading`

**Signature**

```python
def test_wrong_2d_feature_geometry_fails_local_artifact_loading(tmp_path: Path) -> None:
```

**Purpose**

Protects the `wrong 2d feature geometry fails local artifact loading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 7 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `surface.at[surface.index[0], surface.geometry.name]` from `Point(0, 0)`.
- Computes `changed` from `module._result_with_hashes(replace(result, surface_features=surface))`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='surface|geometry')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `Point`, `_application_fixture`, `_write_application_artifacts`, `importlib.import_module`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `replace`, `result.surface_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='surface|geometry'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `wrong 2d feature geometry fails local artifact loading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `_application_fixture`, `_write_application_artifacts`, `importlib.import_module`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `pytest.raises`, `replace`, `result.surface_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_feature_catalog_geometry_role_is_intrinsic`

**Signature**

```python
def test_feature_catalog_geometry_role_is_intrinsic(
    frame_name: str, geometry: object
) -> None:
```

**Purpose**

Protects the `feature catalog geometry role is intrinsic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `frame_name`, `geometry`.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `frame` from `getattr(result, frame_name).copy(deep=True)`.
- Computes `frame.at[frame.index[0], frame.geometry.name]` from `geometry`.
- Computes `changed` from `module._result_with_hashes(replace(result, **{frame_name: frame}))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='geometry')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_application_fixture`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='geometry'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `feature catalog geometry role is intrinsic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_application_fixture`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_feature_catalog_metric_must_match_geometry`

**Signature**

```python
def test_feature_catalog_metric_must_match_geometry(
    frame_name: str, metric: str
) -> None:
```

**Purpose**

Protects the `feature catalog metric must match geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `frame_name`, `metric`.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `frame` from `getattr(result, frame_name).copy(deep=True)`.
- Computes `changed` from `module._result_with_hashes(replace(result, **{frame_name: frame}))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='metric|geometry|count')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='metric|geometry|count'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `feature catalog metric must match geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unreferenced_feature_catalog_identity_fields_are_intrinsic`

**Signature**

```python
def test_unreferenced_feature_catalog_identity_fields_are_intrinsic(
    column: str, value: str
) -> None:
```

**Purpose**

Protects the `unreferenced feature catalog identity fields are intrinsic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 7 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.
- Computes `frame` from `source.copy(deep=True)`.
- Computes `frame.loc[index, column]` from `value`.
- Computes `changed` from `module._result_with_hashes(replace(result, **{name: frame}))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='identity|layer|kind')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_zero_relation_feature`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `source.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='identity|layer|kind'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `unreferenced feature catalog identity fields are intrinsic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_zero_relation_feature`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `source.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_feature_catalog_requires_canonical_crs_and_global_identity`

**Signature**

```python
def test_feature_catalog_requires_canonical_crs_and_global_identity() -> None:
```

**Purpose**

Protects the `feature catalog requires canonical crs and global identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `surface` from `result.surface_features.to_crs('EPSG:4326')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='EPSG:2154|CRS')` and executes: Calls `module._validate_result_envelope(module._result_with_hashes(replace(result, surface_features=surface)))` for its validation or side effect.
- Computes `point` from `result.point_features.copy(deep=True)`.
- Computes `point.loc[point.index[0], 'planning_feature_id']` from `result.surface_features.iloc[0]['planning_feature_id']`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='identity|unique')` and executes: Calls `module._validate_result_envelope(module._result_with_hashes(replace(result, point_features=point)))` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `result.point_features.copy`, `result.surface_features.to_crs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='EPSG:2154|CRS'): module._validate_result_envelope(module._result_with_hashes(replace(result, surface_features=surface)))`; `with pytest.raises(BessPlanningFeatureApplicationError, match='identity|unique'): module._validate_result_envelope(module._result_with_hashes(replace(result, point_features=point)))`.

**Regression protected**

- Protects the exact `feature catalog requires canonical crs and global identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.raises`, `replace`, `result.point_features.copy`, `result.surface_features.to_crs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unreferenced_feature_identity_is_validated_locally`

**Signature**

```python
def test_unreferenced_feature_identity_is_validated_locally(
    tmp_path: Path, feature_id: str
) -> None:
```

**Purpose**

Protects the `unreferenced feature identity is validated locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `feature_id`.
- Contains 8 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.
- Computes `frame` from `source.copy(deep=True)`.
- Computes `frame.loc[index, 'planning_feature_id']` from `feature_id`.
- Computes `changed` from `module._result_with_hashes(replace(result, **{name: frame}))`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='feature|identity|GPU')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `_zero_relation_feature`, `importlib.import_module`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `replace`, `source.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='feature|identity|GPU'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `unreferenced feature identity is validated locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `_zero_relation_feature`, `importlib.import_module`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `source.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unreferenced_feature_participates_in_global_policy_mapping`

**Signature**

```python
def test_unreferenced_feature_participates_in_global_policy_mapping(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `unreferenced feature participates in global policy mapping` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 11 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.
- Computes `frame` from `source.copy(deep=True)`.
- Computes `status` from `frame.loc[index, 'bess_cnig_precheck_status']`.
- Computes `conflicting` from `pd.concat([result.surface_features, result.line_features, result.point_features], ignore_index=True)`.
- Computes `conflicting` from `conflicting.loc[conflicting['bess_cnig_precheck_status'].ne(status)]`.
- Computes `frame.loc[index, 'bess_cnig_status_priority']` from `int(conflicting.iloc[0]['bess_cnig_status_priority'])`.
- Computes `changed` from `module._result_with_hashes(replace(result, **{name: frame}))`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='priority|mapping')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `_zero_relation_feature`, `conflicting['bess_cnig_precheck_status'].ne`, `importlib.import_module`, `int`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `pd.concat`, `replace`, `source.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='priority|mapping'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `unreferenced feature participates in global policy mapping` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `_zero_relation_feature`, `conflicting['bess_cnig_precheck_status'].ne`, `importlib.import_module`, `int`, `load_bess_planning_feature_application_artifacts`, `module._result_with_hashes`, `pd.concat`, `pytest.raises`, `replace`, `source.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_locks_policy_result_schema_exactly`

**Signature**

```python
def test_application_locks_policy_result_schema_exactly(policy_schema: int) -> None:
```

**Purpose**

Protects the `application locks policy result schema exactly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `policy_schema`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `module._result_with_hashes(replace(result, policy_result_hash_schema_version=policy_schema))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='policy.*schema')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='policy.*schema'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `application locks policy result schema exactly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_locks_cnig_result_schema_exactly`

**Signature**

```python
def test_application_locks_cnig_result_schema_exactly(cnig_schema: int) -> None:
```

**Purpose**

Protects the `application locks cnig result schema exactly` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `cnig_schema`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `module._result_with_hashes(replace(result, cnig_result_hash_schema_version=cnig_schema))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='CNIG|cnig.*schema')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='CNIG|cnig.*schema'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `application locks cnig result schema exactly` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_accepts_only_current_policy_and_cnig_source_schemas`

**Signature**

```python
def test_application_accepts_only_current_policy_and_cnig_source_schemas() -> None:
```

**Purpose**

Protects the `application accepts only current policy and cnig source schemas` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: `assert result.policy_result_hash_schema_version == 1`; `assert result.cnig_result_hash_schema_version == 5`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `application accepts only current policy and cnig source schemas` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._validate_result_envelope`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_relation_identity_fast_fails_before_policy_source_validation`

**Signature**

```python
def test_duplicate_relation_identity_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `duplicate relation identity fast fails before policy source validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 7 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `relations` from `pd.concat([result.relations, result.relations.iloc[[0]]], ignore_index=True)`.
- Computes `relations.index` from `pd.Index(relations.index.to_numpy(), dtype='int64')`.
- Computes `changed` from `module._result_with_hashes(replace(result, relations=relations))`.
- Computes `calls` from `0`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique')` and executes: Calls `module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `pd.Index`, `pd.concat`, `relations.index.to_numpy`, `replace`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique'): module.validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)`.

**Regression protected**

- Protects the exact `duplicate relation identity fast fails before policy source validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module.validate_bess_planning_feature_application_result`, `monkeypatch.setattr`, `pd.Index`, `pd.concat`, `pytest.raises`, `relations.index.to_numpy`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_self_consistent_z_geoparquet_artifact_is_rejected`

**Signature**

```python
def test_self_consistent_z_geoparquet_artifact_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `self consistent z geoparquet artifact is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 7 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `original` from `surface.geometry.iloc[0]`.
- Computes `surface.at[surface.index[0], surface.geometry.name]` from `Polygon([(x, y, 9) for x, y in original.exterior.coords])`.
- Computes `changed` from `replace(result, surface_features=surface)`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `Polygon`, `_application_fixture`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `replace`, `result.surface_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `self consistent z geoparquet artifact is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_application_fixture`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `pytest.raises`, `replace`, `result.surface_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_self_consistent_wrong_dtype_artifact_is_rejected`

**Signature**

```python
def test_self_consistent_wrong_dtype_artifact_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `self consistent wrong dtype artifact is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_policy_mutation(result, 'bess_cnig_precheck_status', 'UNKNOWN', dtype='object')`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='dtype|schema')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='dtype|schema'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `self consistent wrong dtype artifact is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_manifest_rejects_invalid_contract`

**Signature**

```python
def test_artifact_manifest_rejects_invalid_contract(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
```

**Purpose**

Protects the `artifact manifest rejects invalid contract` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`, `message`.
- Contains 3 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(manifest_path, paths, manifest)` from `_write_application_artifacts(tmp_path, result)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match=message)` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `callable`, `json.dumps`, `load_bess_planning_feature_application_artifacts`, `manifest_path.write_text`, `mutation`, `value.update`, `value['artifacts'].append`, `value['artifacts'].pop`, `value['artifacts'][0].update`, `value['artifacts'][0]['frame_schema_signature'].update`, `value['artifacts'][1].update`.

**Expected result**

- Direct assertions: `assert callable(mutation)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match=message): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `artifact manifest rejects invalid contract` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `callable`, `dict`, `json.dumps`, `load_bess_planning_feature_application_artifacts`, `manifest_path.write_text`, `mutation`, `pytest.mark.parametrize`, `pytest.raises`, `value.update`, `value['artifacts'].append`, `value['artifacts'].pop`, `value['artifacts'][0].update`, `value['artifacts'][0]['frame_schema_signature'].update`, `value['artifacts'][1].update`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_manifest_rejects_duplicate_json_key`

**Signature**

```python
def test_manifest_rejects_duplicate_json_key(tmp_path: Path) -> None:
```

**Purpose**

Protects the `manifest rejects duplicate json key` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='Duplicate JSON')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `manifest_path.write_text`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='Duplicate JSON'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `manifest rejects duplicate json key` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `manifest_path.write_text`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_only_verified_bytes`

**Signature**

```python
def test_artifact_loader_parses_only_verified_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `artifact loader parses only verified bytes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 12 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `target` from `paths['RELATIONS']`.
- Computes `replacement` from `tmp_path / 'replacement.parquet'`.
- Computes `original_read_bytes` from `Path.read_bytes`.
- Computes `verified` from `original_read_bytes(target)`.
- Computes `replacement_bytes` from `original_read_bytes(replacement)`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `original_read_parquet` from `module.pd.read_parquet`.
- Computes `replaced` from `False`.
- Defines `observed` with annotation `list[tuple[str, bytes]]` from `[]`.
- Computes `loaded` from `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `importlib.import_module`, `isinstance`, `load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `observed.append`, `original_read_bytes`, `original_read_parquet`, `path.write_bytes`, `result.relations.to_parquet`, `source.getvalue`.

**Expected result**

- Direct assertions: `assert replaced`; `assert ('buffer', verified) in observed`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `artifact loader parses only verified bytes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `assert_frame_equal`, `importlib.import_module`, `isinstance`, `load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `observed.append`, `original_read_bytes`, `original_read_parquet`, `path.write_bytes`, `result.relations.to_parquet`, `source.getvalue`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_physical_replacement_before_loading_is_rejected`

**Signature**

```python
def test_physical_replacement_before_loading_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `physical replacement before loading is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(manifest_path, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='size|SHA|hash')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `paths['RELATIONS'].read_bytes`, `paths['RELATIONS'].write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='size|SHA|hash'): load_bess_planning_feature_application_artifacts(manifest_path, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `physical replacement before loading is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `paths['RELATIONS'].read_bytes`, `paths['RELATIONS'].write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_application_api_exports_only_stable_symbols`

**Signature**

```python
def test_public_application_api_exports_only_stable_symbols() -> None:
```

**Purpose**

Protects the `public application api exports only stable symbols` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `required` from `{'BessPlanningFeatureApplicationArtifactManifest', 'BessPlanningFeatureApplicationError', 'BessPlanningFeatureApplicationResult', 'apply_bess_planning_feature_policy', 'load_bess_planning_feature_application_artifacts', 'validate_bess_planning_feature_application_result', 'validate_bess_planning_feature_application_re…`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.

**Action**

- Calls `any`, `importlib.import_module`, `name.startswith`, `required.issubset`.

**Expected result**

- Direct assertions: `assert set(module.__all__) == required`; `assert required.issubset(set(stages.__all__))`; `assert not any((name.startswith('_') for name in module.__all__))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public application api exports only stable symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `any`, `importlib.import_module`, `name.startswith`, `required.issubset`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact`

**Signature**

```python
def test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `unreferenced feature document lineage is bound to envelope artifact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 8 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.
- Computes `frame` from `source.copy(deep=True)`.
- Computes `frame.loc[index, 'source_document_id']` from `'MUTATED-DOCUMENT'`.
- Computes `frame.loc[index, 'planning_feature_id']` from `f"GPU:MUTATED-DOCUMENT:{frame.loc[index, 'logical_layer']}:{frame.loc[index, 'source_feature_id']}"`.
- Computes `changed` from `_replace_application_frame(result, name, frame)`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='document|lineage')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `_write_application_artifacts`, `_zero_relation_feature`, `load_bess_planning_feature_application_artifacts`, `source.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='document|lineage'): load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `unreferenced feature document lineage is bound to envelope artifact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `_write_application_artifacts`, `_zero_relation_feature`, `load_bess_planning_feature_application_artifacts`, `pytest.raises`, `source.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_feature_row_lineage_must_match_application_envelope`

**Signature**

```python
def test_feature_row_lineage_must_match_application_envelope(mutation: str) -> None:
```

**Purpose**

Protects the `feature row lineage must match application envelope` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='lineage|document')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `source.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='lineage|document'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `feature row lineage must match application envelope` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `source.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_referenced_row_lineage_cannot_bypass_envelope`

**Signature**

```python
def test_coordinated_referenced_row_lineage_cannot_bypass_envelope(
    column: str,
    value: str,
    rename_id: bool,
) -> None:
```

**Purpose**

Protects the `coordinated referenced row lineage cannot bypass envelope` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`, `rename_id`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `changed` from `_coordinated_referenced_lineage_mutation(result, column, value, rename_id=rename_id)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='lineage|document')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_referenced_lineage_mutation`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='lineage|document'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `coordinated referenced row lineage cannot bypass envelope` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_referenced_lineage_mutation`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_resolved_official_row_requires_label_and_envelope_profile`

**Signature**

```python
def test_resolved_official_row_requires_label_and_envelope_profile() -> None:
```

**Purpose**

Protects the `resolved official row requires label and envelope profile` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `module._validate_result_envelope`, `source.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='official|profile|label'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `resolved official row requires label and envelope profile` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.raises`, `source.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_official_row_rejects_invented_label_or_url`

**Signature**

```python
def test_unknown_official_row_rejects_invented_label_or_url() -> None:
```

**Purpose**

Protects the `unknown official row rejects invented label or url` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `module._validate_result_envelope`, `source.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='official|null'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `unknown official row rejects invented label or url` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `module._validate_result_envelope`, `pytest.raises`, `source.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_feature_prefix_has_exact_canonical_schema`

**Signature**

```python
def test_application_feature_prefix_has_exact_canonical_schema(
    frame_name: str,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `application feature prefix has exact canonical schema` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `frame_name`, `mutation`.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `frame` from `getattr(result, frame_name).copy(deep=True)`.
- Computes `changed` from `_replace_application_frame(result, frame_name, frame)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype|index')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `frame.columns.get_loc`, `frame.drop`, `frame.iloc[0:0].copy`, `frame.index.rename`, `frame.index.to_numpy`, `frame.insert`, `frame['official_legal_reference'].tolist`, `frame[metric].tolist`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module._validate_result_envelope`, `pd.Index`, `pd.Series`, `pd.array`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype|index'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `application feature prefix has exact canonical schema` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `frame.columns.get_loc`, `frame.drop`, `frame.iloc[0:0].copy`, `frame.index.rename`, `frame.index.to_numpy`, `frame.insert`, `frame['official_legal_reference'].tolist`, `frame[metric].tolist`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `len`, `list`, `module._validate_result_envelope`, `pd.Index`, `pd.Series`, `pd.array`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_relation_prefix_has_exact_canonical_schema`

**Signature**

```python
def test_application_relation_prefix_has_exact_canonical_schema(
    mutation: str,
) -> None:
```

**Purpose**

Protects the `application relation prefix has exact canonical schema` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `frame` from `result.relations.copy(deep=True)`.
- Computes `changed` from `_replace_application_frame(result, 'relations', frame)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `frame.columns.get_loc`, `frame.drop`, `frame.iloc[0:0].drop`, `frame.insert`, `frame['intersection_area_m2'].tolist`, `frame['point_member_count'].tolist`, `importlib.import_module`, `module._validate_result_envelope`, `pd.Categorical`, `pd.Series`, `pd.array`, `result.relations.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `application relation prefix has exact canonical schema` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `frame.columns.get_loc`, `frame.drop`, `frame.iloc[0:0].drop`, `frame.insert`, `frame['intersection_area_m2'].tolist`, `frame['point_member_count'].tolist`, `importlib.import_module`, `len`, `list`, `module._validate_result_envelope`, `pd.Categorical`, `pd.Series`, `pd.array`, `pytest.mark.parametrize`, `pytest.raises`, `result.relations.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_self_consistent_factual_prefix_dtype_artifact_is_rejected`

**Signature**

```python
def test_self_consistent_factual_prefix_dtype_artifact_is_rejected(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `self consistent factual prefix dtype artifact is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `surface['feature_area_m2']` from `pd.Series(surface['feature_area_m2'].tolist(), index=surface.index, dtype='object')`.
- Computes `changed` from `_replace_application_frame(result, 'surface_features', surface)`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype')` and executes: Calls `load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `pd.Series`, `result.surface_features.copy`, `surface['feature_area_m2'].tolist`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype'): load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'])`.

**Regression protected**

- Protects the exact `self consistent factual prefix dtype artifact is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `_write_application_artifacts`, `load_bess_planning_feature_application_artifacts`, `pd.Series`, `pytest.raises`, `result.surface_features.copy`, `surface['feature_area_m2'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_lineage_defect_fast_fails_before_policy_source_validation`

**Signature**

```python
def test_lineage_defect_fast_fails_before_policy_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `lineage defect fast fails before policy source validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 8 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `calls` from `0`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.
- Computes `frame` from `source.copy(deep=True)`.
- Computes `frame.loc[index, 'source_archive_sha256']` from `'f' * 64`.
- Computes `changed` from `_replace_application_frame(result, name, frame)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError)` and executes: Calls `validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `monkeypatch.setattr`, `source.copy`, `validate_bess_planning_feature_application_result`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError): validate_bess_planning_feature_application_result(*inputs, coded, config, policy, changed)`.

**Regression protected**

- Protects the exact `lineage defect fast fails before policy source validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_replace_application_frame`, `_zero_relation_feature`, `importlib.import_module`, `monkeypatch.setattr`, `pytest.raises`, `source.copy`, `validate_bess_planning_feature_application_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams`

**Signature**

```python
def test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams() -> None:
```

**Purpose**

Protects the `step 7d 5b 2b 5 application loader requires exact upstreams` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='hash|invalid')` and executes: Calls `module.validate_bess_planning_feature_application_result_envelope(replace(result, complete_result_content_sha256='0' * 64))` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `hasattr`, `importlib.import_module`, `inspect.signature`, `module.validate_bess_planning_feature_application_result_envelope`, `replace`.

**Expected result**

- Direct assertions: `assert tuple(inspect.signature(module.load_bess_planning_feature_application_artifacts).parameters) == ('manifest_path', 'surface_features_path', 'line_features_path', 'point_features_path', 'relations_path', 'coded_result', 'policy_result')`; `assert hasattr(module, 'validate_bess_planning_feature_application_result_envelope')`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='hash|invalid'): module.validate_bess_planning_feature_application_result_envelope(replace(result, complete_result_content_sha256='0' * 64))`.

**Regression protected**

- Protects the exact `step 7d 5b 2b 5 application loader requires exact upstreams` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `hasattr`, `importlib.import_module`, `inspect.signature`, `module.validate_bess_planning_feature_application_result_envelope`, `pytest.raises`, `replace`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_application_loader_rejects_locally_valid_rationale_change`

**Signature**

```python
def test_source_bound_application_loader_rejects_locally_valid_rationale_change(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source bound application loader rejects locally valid rationale change` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `changed` from `_coordinated_policy_mutation(result, 'bess_cnig_rationale', 'A different exact non-empty rationale.')`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='upstream|rebuilt')` and executes: Calls `module.load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'], coded, policy)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_coordinated_policy_mutation`, `_write_application_artifacts`, `importlib.import_module`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='upstream|rebuilt'): module.load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'], coded, policy)`.

**Regression protected**

- Protects the exact `source bound application loader rejects locally valid rationale change` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_coordinated_policy_mutation`, `_write_application_artifacts`, `importlib.import_module`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_manifest_filenames_are_casefold_unique`

**Signature**

```python
def test_application_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
```

**Purpose**

Protects the `application manifest filenames are casefold unique` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(_, _, payload)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `payload['artifacts'][1]['filename']` from `str(payload['artifacts'][0]['filename']).upper()`.
- Enters managed context(s) `pytest.raises(ValueError, match='filename|duplicate')` and executes: Calls `BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeatureApplicationArtifactManifest.model_validate`, `_application_fixture`, `_write_application_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='filename|duplicate'): BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)`.

**Regression protected**

- Protects the exact `application manifest filenames are casefold unique` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeatureApplicationArtifactManifest.model_validate`, `_application_fixture`, `_write_application_artifacts`, `pytest.raises`, `str`, `str(payload['artifacts'][0]['filename']).upper`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_loader_rejects_valid_domain_cross_pair_swaps`

**Signature**

```python
def test_source_bound_loader_rejects_valid_domain_cross_pair_swaps(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    columns: tuple[str, ...],
) -> None:
```

**Purpose**

Protects the `source bound loader rejects valid domain cross pair swaps` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `columns`.
- Contains 6 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `changed` from `_swap_referenced_feature_values(result, columns)`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Computes `heavy_calls` from `0`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='upstream')` and executes: Calls `module.load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'], coded, policy)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_swap_referenced_feature_values`, `_write_application_artifacts`, `importlib.import_module`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert heavy_calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='upstream'): module.load_bess_planning_feature_application_artifacts(manifest, paths['SURFACE_FEATURES'], paths['LINE_FEATURES'], paths['POINT_FEATURES'], paths['RELATIONS'], coded, policy)`.

**Regression protected**

- Protects the exact `source bound loader rejects valid domain cross pair swaps` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_swap_referenced_feature_values`, `_write_application_artifacts`, `importlib.import_module`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_loader_rejects_factual_prefix_lineage_change`

**Signature**

```python
def test_source_bound_loader_rejects_factual_prefix_lineage_change(
    tmp_path: Path, column: str
) -> None:
```

**Purpose**

Protects the `source bound loader rejects factual prefix lineage change` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `column`.
- Contains 7 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `surface` from `result.surface_features.copy(deep=True)`.
- Computes `surface.loc[surface.index[0], column]` from `f'changed-{column}'`.
- Computes `changed` from `module._result_with_hashes(replace(result, surface_features=surface))`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='upstream')` and executes: Calls `module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `paths.values`, `replace`, `result.surface_features.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='upstream'): module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)`.

**Regression protected**

- Protects the exact `source bound loader rejects factual prefix lineage change` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `paths.values`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.surface_features.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_loader_rejects_all_null_raw_column_transition`

**Signature**

```python
def test_source_bound_loader_rejects_all_null_raw_column_transition(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source bound loader rejects all null raw column transition` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 29 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, _)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `coding_module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
- Computes `policy_module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `coded_surface` from `coded.surface_features.copy(deep=True)`.
- Computes `coded_surface['text_raw']` from `pd.Series(['source text'] * len(coded_surface), index=coded_surface.index, dtype='str')`.
- Computes `coded_relations` from `coded.relations.copy(deep=True)`.
- Computes `surface_ids` from `set(coded_surface['planning_feature_id'])`.
- Computes `coded_relations.loc[coded_relations['planning_feature_id'].isin(surface_ids), 'text_raw']` from `'source text'`.
- Computes `coded_relations['text_raw']` from `pd.Series(coded_relations['text_raw'].tolist(), index=coded_relations.index, dtype='str')`.
- Computes `coded` from `coding_module._result_with_hashes(replace(coded, surface_features=coded_surface, relations=coded_relations))`.
- Computes `policy_table` from `policy.policy_table.copy(deep=True)`.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `coded.relations.copy`, `coded.surface_features.copy`, `coded_relations['planning_feature_id'].isin`, `coded_relations['text_raw'].tolist`, `coding_module._result_with_hashes`, `importlib.import_module`, `module._build_result`, `module._result_with_hashes`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `paths.values`, `pd.Series`, `pd.array`, `policy.policy_table.copy`, `policy_module._result_with_hashes`, `relations['geometry_kind'].eq`, `relations['text_raw'].tolist`, `reordered_dir.mkdir`, `replace`, `result.relations.copy`, `result.surface_features.copy`, `result.surface_features.iloc[::-1].copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='upstream'): module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)`; `with pytest.raises(BessPlanningFeatureApplicationError, match='upstream'): module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)`.

**Regression protected**

- Protects the exact `source bound loader rejects all null raw column transition` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `coded.relations.copy`, `coded.surface_features.copy`, `coded_relations['planning_feature_id'].isin`, `coded_relations['text_raw'].tolist`, `coding_module._result_with_hashes`, `importlib.import_module`, `len`, `module._build_result`, `module._result_with_hashes`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `paths.values`, `pd.Series`, `pd.array`, `policy.policy_table.copy`, `policy_module._result_with_hashes`, `pytest.raises`, `relations['geometry_kind'].eq`, `relations['text_raw'].tolist`, `reordered_dir.mkdir`, `replace`, `result.relations.copy`, `result.surface_features.copy`, `result.surface_features.iloc[::-1].copy`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering`

**Signature**

```python
def test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source bound loader rejects unreferenced feature and row reordering` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 9 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `(name, source, index)` from `_zero_relation_feature(result)`.
- Computes `unreferenced` from `source.copy(deep=True)`.
- Computes `unreferenced.loc[index, 'label_raw']` from `'changed unreferenced label'`.
- Computes `changed` from `module._result_with_hashes(replace(result, **{name: unreferenced}))`.
- Computes `unreferenced_dir` from `tmp_path / 'unreferenced'`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(unreferenced_dir, changed)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='upstream')` and executes: Calls `module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `_zero_relation_feature`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `paths.values`, `replace`, `source.copy`, `unreferenced_dir.mkdir`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='upstream'): module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)`.

**Regression protected**

- Protects the exact `source bound loader rejects unreferenced feature and row reordering` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `_zero_relation_feature`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `module.load_bess_planning_feature_application_artifacts`, `paths.values`, `pytest.raises`, `replace`, `source.copy`, `unreferenced_dir.mkdir`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_validates_upstreams_and_rebuilds_once_lightweight`

**Signature**

```python
def test_application_loader_validates_upstreams_and_rebuilds_once_lightweight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `application loader validates upstreams and rebuilds once lightweight` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 10 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `coded_before` from `coded.surface_features.copy(deep=True)`.
- Computes `policy_before` from `policy.policy_table.copy(deep=True)`.
- Computes `actual_coded_envelope` from `module.validate_planning_feature_code_result_envelope`.
- Computes `actual_policy_envelope` from `module.validate_bess_planning_feature_policy_result_envelope`.
- Computes `actual_build` from `module._build_result`.
- Computes `calls` from `{'coded': 0, 'policy': 0, 'build': 0, 'heavy': 0}`.
- Computes `loaded` from `module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)`.

**Action**

- Calls `_application_fixture`, `_write_application_artifacts`, `actual_build`, `actual_coded_envelope`, `actual_policy_envelope`, `coded.surface_features.copy`, `importlib.import_module`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `paths.values`, `policy.policy_table.copy`.

**Expected result**

- Direct assertions: `assert loaded.complete_result_content_sha256 == result.complete_result_content_sha256`; `assert calls == {'coded': 1, 'policy': 1, 'build': 1, 'heavy': 0}`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `application loader validates upstreams and rebuilds once lightweight` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_write_application_artifacts`, `actual_build`, `actual_coded_envelope`, `actual_policy_envelope`, `assert_frame_equal`, `assert_geodataframe_equal`, `coded.surface_features.copy`, `importlib.import_module`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `paths.values`, `policy.policy_table.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_bad_upstream_before_artifact_reads`

**Signature**

```python
def test_application_loader_rejects_bad_upstream_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `application loader rejects bad upstream before artifact reads` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `reads` from `0`.
- Computes `original` from `Path.read_bytes`.
- Computes `forged` from `replace(coded, complete_result_content_sha256='0' * 64)`.
- Enters managed context(s) `pytest.raises(Exception, match='hash|SHA|invalid')` and executes: Calls `_load_application_artifacts(manifest, *paths.values(), forged, policy)` for its validation or side effect.

**Action**

- Calls `_application_fixture`, `_load_application_artifacts`, `_write_application_artifacts`, `monkeypatch.setattr`, `original`, `paths.values`, `replace`.

**Expected result**

- Direct assertions: `assert reads == 0`.
- Expected exception contexts: `with pytest.raises(Exception, match='hash|SHA|invalid'): _load_application_artifacts(manifest, *paths.values(), forged, policy)`.

**Regression protected**

- Protects the exact `application loader rejects bad upstream before artifact reads` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `_load_application_artifacts`, `_write_application_artifacts`, `monkeypatch.setattr`, `original`, `paths.values`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_manifest_rejects_nonportable_filename`

**Signature**

```python
def test_application_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
```

**Purpose**

Protects the `application manifest rejects nonportable filename` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `filename`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, _, result)` from `_application_fixture()`.
- Computes `(_, _, payload)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `payload['artifacts'][0]['filename']` from `filename`.
- Enters managed context(s) `pytest.raises(ValueError, match='filename|basename|portable')` and executes: Calls `BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeatureApplicationArtifactManifest.model_validate`, `_application_fixture`, `_write_application_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='filename|basename|portable'): BessPlanningFeatureApplicationArtifactManifest.model_validate(payload)`.

**Regression protected**

- Protects the exact `application manifest rejects nonportable filename` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeatureApplicationArtifactManifest.model_validate`, `_application_fixture`, `_write_application_artifacts`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild`

**Signature**

```python
def test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `application loader rejects incompatible upstreams before io or rebuild` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `mutation`.
- Contains 6 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `changed_policy` from `_compatible_policy_mutation(policy, mutation)`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `calls` from `{'manifest': 0, 'read': 0, 'build': 0, 'heavy': 0}`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='Policy|policy|CNIG|pair|source|schema|official|reference')` and executes: Calls `module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, changed_policy)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `_application_fixture`, `_compatible_policy_mutation`, `_write_application_artifacts`, `importlib.import_module`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `paths.values`.

**Expected result**

- Direct assertions: `assert calls == {'manifest': 0, 'read': 0, 'build': 0, 'heavy': 0}`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='Policy|policy|CNIG|pair|source|schema|official|reference'): module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, changed_policy)`.

**Regression protected**

- Protects the exact `application loader rejects incompatible upstreams before io or rebuild` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_application_fixture`, `_compatible_policy_mutation`, `_write_application_artifacts`, `importlib.import_module`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `paths.values`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`

**Signature**

```python
def test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    empty_upstream: str,
) -> None:
```

**Purpose**

Protects the `application loader rejects empty upstreams before any io or rebuild` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `empty_upstream`.
- Contains 5 explicit setup/context statement(s).
- Computes `(_, coded, _, policy, result)` from `_application_fixture()`.
- Computes `(manifest, paths, _)` from `_write_application_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
- Computes `calls` from `{'manifest': 0, 'read': 0, 'build': 0, 'heavy': 0}`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureApplicationError, match='dictionary|policy|table|pair|empty|record|entry')` and executes: Calls `module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `_application_fixture`, `_canonical_empty_coded_result`, `_canonical_empty_policy_result`, `_write_application_artifacts`, `importlib.import_module`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `paths.values`, `policy_module._result_with_hashes`, `replace`.

**Expected result**

- Direct assertions: `assert calls == {'manifest': 0, 'read': 0, 'build': 0, 'heavy': 0}`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureApplicationError, match='dictionary|policy|table|pair|empty|record|entry'): module.load_bess_planning_feature_application_artifacts(manifest, *paths.values(), coded, policy)`.

**Regression protected**

- Protects the exact `application loader rejects empty upstreams before any io or rebuild` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_application_fixture`, `_canonical_empty_coded_result`, `_canonical_empty_policy_result`, `_write_application_artifacts`, `importlib.import_module`, `module.load_bess_planning_feature_application_artifacts`, `monkeypatch.setattr`, `paths.values`, `policy_module._result_with_hashes`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `LINE_FEATURES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `POINT_FEATURES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `RELATIONS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SURFACE_FEATURES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `artifacts` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_application_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_legal_conclusion_produced` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_limitations` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_feature_text_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_regulation_content_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_rejection_performed` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_status_aggregated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_application_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_result_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_required_human_action` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_score_calculated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `build` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_complete_result_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_profile_schema_version` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `coded` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `feature_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `filename` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `frame_schema_signature` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `heavy` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `kind` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `logical_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `manifest` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `official_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_regulation_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `point_member_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `policy` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `read` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `text_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `type_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `type_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
