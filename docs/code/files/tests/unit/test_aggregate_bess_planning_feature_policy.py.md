# `tests/unit/test_aggregate_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_aggregate_bess_planning_feature_policy.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `37eb958e761dc00eb6dde5389923fd24f0a60457f0beeacac976be0dc96a3cc2`

## 1. Purpose

Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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
- `from shapely import affinity` — required by the implementation paths and symbols documented below.
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon` — required by the implementation paths and symbols documented below.
- `from test_apply_bess_planning_feature_policy import ( _application_fixture, _coordinated_policy_mutation, _surface_touch_with_positive_area, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.common.bess_application_contract import ( POLICY_COLUMNS, POLICY_SUFFIX_DTYPES, )` — required by the implementation paths and symbols documented below.
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_feature_schema import relation_columns, relation_dtypes` — required by the implementation paths and symbols documented below.
- `from landscout.stages.aggregate_bess_planning_feature_policy import ( BessPlanningFeatureParcelAggregationArtifactManifest, BessPlanningFeatureParcelAggregationError, BessPlanningFeatureParcelAggregationResult, aggregate_bess_planning_feature_policy_to_parcels, validate_bess_planning_feature_parcel…` — required by the implementation paths and symbols documented below.
- `from landscout.stages.aggregate_bess_planning_feature_policy import ( load_bess_planning_feature_parcel_aggregation_artifacts as _load_aggregation_artifacts, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `PARCEL_COLUMNS` | `( "bess_cnig_parcel_aggregation_status", "bess_cnig_parcel_precheck_status", "bess_cnig_parcel_precheck_confidence", "bess_cnig_parcel_status_priority", "bess_cnig_controlling_relation_count", "bess_cnig_exact_controlling_relation_count", "bess_cnig_unresolved_controlling_relation_count", "bess_cnig_touch_only_relation_count", "bess_cnig_selected_relation_count", "bess_cnig_lower_priority_controlling_relation_count", "bess_cnig_distinct_exact_status_count", "bess_cnig_multiple_exact_statuses", "bess_cnig_selected_feature_ids_json", "bess_cnig_unresolved_feature_ids_json", "bess_cnig_touch_only_feature_ids_json", "bess_cnig_confidence_aggregation_method", "bess_cnig_formal_review_required", "bess_cnig_aggregation_scope", "bess_cnig_policy_scope", "bess_cnig_local_feature_text_interpreted", "bess_cnig_local_regulation_content_interpreted", "bess_cnig_legal_conclusion_produced", "bess_cnig_parcel_status_aggregated", "bess_cnig_parcel_rejection_performed", "bess_cnig_score_calculated", "bess_cnig_policy_profile", "bess_cnig_policy_sha256", "bess_cnig_policy_result_sha256", "bess_cnig_application_result_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_COLUMNS` | `( "bess_cnig_parcel_relation_role", "bess_cnig_selected_for_parcel_status", "bess_cnig_resulting_parcel_aggregation_status", "bess_cnig_resulting_parcel_precheck_status", "bess_cnig_resulting_parcel_precheck_confidence", "bess_cnig_resulting_parcel_status_priority", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_LAST_SOURCE_PARCELS` | `None` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_LAST_APPLICATION_RESULT` | `None` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_aggregation_fixture`

**Signature**

```python
def _aggregation_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    object,
    BessPlanningFeatureParcelAggregationResult,
]:
```

**Purpose**

Implements aggregation fixture according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[tuple[object, ...], object, object, object, object, BessPlanningFeatureParcelAggregationResult]`. Observed return expression(s): `(inputs, coded, config, policy, application, result)`.

**Algorithm**

1. Executes `global _LAST_SOURCE_PARCELS, _LAST_APPLICATION_RESULT`.
2. Computes `(inputs, coded, config, policy, application)` from `_application_fixture()`.
3. Computes `result` from `aggregate_bess_planning_feature_policy_to_parcels(*inputs, coded, config, policy, application)`.
4. Computes `_LAST_SOURCE_PARCELS` from `inputs[1]`.
5. Computes `_LAST_APPLICATION_RESULT` from `application`.
6. Returns `(inputs, coded, config, policy, application, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_application_fixture`, `aggregate_bess_planning_feature_policy_to_parcels`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_aggregation_loader_rejects_bad_application_before_artifact_reads`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_aggregation_manifest_filenames_are_casefold_unique`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_aggregation_manifest_rejects_nonportable_filename`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_application_result_schema_two_remains_accepted`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_artifact_manifest_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_duplicate_json_and_physical_replacement_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_duplicate_output_columns_are_rejected_intrinsically`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_local_corruption_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_only_application_result_schema_two_is_accepted`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_decision_status_domain_rejects_forbidden_vocabulary`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_persisted_feature_id_json_must_be_portable_and_canonical`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_identity_and_global_mapping_fail_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_semantic_failure_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_valid_two_file_verified_byte_artifacts_and_source_readback`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_verified_bytes_are_the_bytes_parsed`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_filenames_are_casefold_unique`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_rejects_nonportable_filename`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_result_schema_two_remains_accepted`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `load_bess_planning_feature_parcel_aggregation_artifacts`

**Signature**

```python
def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame | None = None,
    application_result: object | None = None,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Test adapter supplying the newly mandatory exact upstream envelopes.

**Inputs**

- `manifest_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relation_assessments_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_parcels` (`gpd.GeoDataFrame | None`; optional/default `None`) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application_result` (`object | None`; optional/default `None`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `_load_legacy_local_aggregation_artifacts(manifest_path, parcels_path, relation_assessments_path)`; `_load_aggregation_artifacts(manifest_path, parcels_path, relation_assessments_path, source_parcels, application_result)`.

**Algorithm**

1. Computes `legacy_synthetic` from `source_parcels is None or application_result is None`.
2. Checks `source_parcels is None or application_result is None`. When true: Computes `source_parcels` from `_LAST_SOURCE_PARCELS`. Computes `application_result` from `_LAST_APPLICATION_RESULT`.
3. Checks `source_parcels is None or application_result is None`. When true: Returns `_load_legacy_local_aggregation_artifacts(manifest_path, parcels_path, relation_assessments_path)`.
4. Asserts `source_parcels is not None`.
5. Asserts `application_result is not None`.
6. Runs guarded operation: Returns `_load_aggregation_artifacts(manifest_path, parcels_path, relation_assessments_path, source_parcels, application_result)`. Handles `BessPlanningFeatureParcelAggregationError`.

**Validation and invariants**

- Rejects or diverts the path when `not legacy_synthetic or 'unknown feature' not in str(error)` is true.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `_load_aggregation_artifacts`, `_load_legacy_local_aggregation_artifacts`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_load_aggregation_artifacts`, `_load_legacy_local_aggregation_artifacts`, `str`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_artifact_manifest_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_coordinated_relation_identity_artifact_corruption_fails_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_duplicate_json_and_physical_replacement_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_valid_two_file_verified_byte_artifacts_and_source_readback`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_verified_bytes_are_the_bytes_parsed`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_load_legacy_local_aggregation_artifacts`

**Signature**

```python
def _load_legacy_local_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Exercise pre-2B.5 local-only assertions for retained synthetic fixtures.

**Inputs**

- `manifest_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relation_assessments_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
2. Computes `payload` from `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=module._unique_json_object)`.
3. Computes `manifest` from `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)`.
4. Computes `records` from `{record.artifact_role: record for record in manifest.artifacts}`.
5. Computes `parcels` from `module._read_verified_artifact(Path(parcels_path), records['PARCELS'])`.
6. Computes `relations` from `module._read_verified_artifact(Path(relation_assessments_path), records['RELATION_ASSESSMENTS'])`.
7. Computes `result` from `BessPlanningFeatureParcelAggregationResult(**{field: getattr(manifest, field) for field in module.RESULT_SCALAR_FIELDS}, parcels=parcels, relation_assessments=relations)`.
8. Calls `module._validate_result_envelope(result)` for its validation or side effect.
9. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `Path(manifest_path).read_text`, `module._read_verified_artifact`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate`, `BessPlanningFeatureParcelAggregationResult`, `Path`, `Path(manifest_path).read_text`, `getattr`, `importlib.import_module`, `json.loads`, `module._read_verified_artifact`, `module._validate_result_envelope`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_build_from_relations`

**Signature**

```python
def _build_from_relations(
    relations: pd.DataFrame,
    *,
    parcel_ids: tuple[str, ...] = ("PARCEL-1", "PARCEL-2"),
    canonicalize_application_dtypes: bool = True,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Builds from relations according to the exact implementation and guards in this file.

**Inputs**

- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcel_ids` (`tuple[str, ...]`; optional/default `('PARCEL-1', 'PARCEL-2')`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `canonicalize_application_dtypes` (`bool`; optional/default `True`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `module._build_result(parcels, application)`.

**Algorithm**

1. Executes `global _LAST_SOURCE_PARCELS, _LAST_APPLICATION_RESULT`.
2. Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
3. Computes `(_, _, _, _, application)` from `_application_fixture()`.
4. Computes `parcels` from `gpd.GeoDataFrame({'parcel_id': list(parcel_ids), 'prior': range(len(parcel_ids))}, geometry=[Polygon([(i * 101, 0), (i * 101 + 100, 0), (i * 101 + 100, 40), (i * 101, 40)]) for i in range(len(parcel_ids))], crs='EPSG:2154', index=pd.Index(range(10, 10 + len(parcel_ids)), name='parcel_row'))`.
5. Computes `relations` from `relations.reset_index(drop=True)`.
6. Computes `relations['parcel_metric_area_m2']` from `4000.0`.
7. Computes `surface_mask` from `relations['geometry_kind'].eq('SURFACE')`.
8. Computes `relations.loc[surface_mask, 'parcel_share_pct']` from `100.0 * relations.loc[surface_mask, 'intersection_area_m2'].astype('float64') / 4000.0`.
9. Computes `relations['bess_cnig_policy_profile']` from `application.policy_profile`.
10. Computes `relations['bess_cnig_policy_sha256']` from `application.policy_sha256`.
11. Computes `relations['bess_cnig_policy_result_sha256']` from `application.policy_complete_result_content_sha256`.
12. Checks `canonicalize_application_dtypes`. When true: Computes `suffix` from `POLICY_COLUMNS`. Computes `relations` from `relations.loc[:, relation_columns(suffix)]`. Iterates `(column, dtype)` over `zip(relation_columns(suffix), relation_dtypes(tuple((POLICY_SUFFIX_DTYPES[column] for column in suffix))), strict=True)`. For each value: Computes `relations[column]` from `pd.Series(relations[column].tolist(), index=relations.index, dtype=dtype)`. Executes 1 additional source-ordered statement(s).
13. Computes `application` from `replace(application, relations=relations)`.
14. Computes `application` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes(application)`.
15. Computes `_LAST_SOURCE_PARCELS` from `parcels`.
16. Computes `_LAST_APPLICATION_RESULT` from `application`.
17. Returns `module._build_result(parcels, application)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `Polygon`, `_application_fixture`, `gpd.GeoDataFrame`, `importlib.import_module`, `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes`, `len`, `list`, `module._build_result`, `pd.Index`, `pd.Series`, `range`, `relation_columns`, `relation_dtypes`, `relations.index.to_numpy`, `relations.loc[surface_mask, 'intersection_area_m2'].astype`, `relations.reset_index`, `relations['geometry_kind'].eq`, `relations[column].tolist`, `replace`, `tuple`, `zip`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_cross_parcel_priority_conflict_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_duplicate_selected_pair_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_invalid_lower_feature_id_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_all_application_identity_scope_and_boundary_fields_are_intrinsic`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_application_relation_suffix_dtype_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_boundary_only_relations_are_contextual`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_complete_five_status_policy_mapping_is_globally_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_coordinated_local_cross_table_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_current_gpu_feature_id_is_canonical`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_document_wide_same_priority_cannot_map_to_two_statuses`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_document_wide_same_status_cannot_map_to_two_priorities`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_duplicate_parcel_feature_identity_is_rejected_for_every_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_every_inherited_application_relation_domain_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_every_positive_relation_type_controls_without_threshold`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_exact_relations_select_configured_max_priority_and_lowest_confidence`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_output_dtype_and_non_2d_parcel_fail_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_relation_parcel_id_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_no_relation_parcel_is_retained_without_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_noncanonical_feature_ids_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_validation_uses_reprojected_calculation_copy`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_policy_unknown_is_exact_but_unresolved_controlling_overrides`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_parcel_area_is_bound_to_real_parcel_geometry`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_selected_relation_role_requires_selected_status_and_priority`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_status_and_priority_mapping_is_one_to_one_at_every_level`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_touch_relation_remains_context_beside_a_controlling_relation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_unknown_relation_type_is_rejected_by_shared_relation_contract`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_unresolved_relation_cannot_contain_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_all_application_identity_scope_and_boundary_fields_are_intrinsic`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_relation_suffix_dtype_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_boundary_only_relations_are_contextual`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_complete_five_status_policy_mapping_is_globally_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_current_gpu_feature_id_is_canonical`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_priority_cannot_map_to_two_statuses`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_status_cannot_map_to_two_priorities`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_parcel_feature_identity_is_rejected_for_every_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_inherited_application_relation_domain_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_positive_relation_type_controls_without_threshold`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_exact_relations_select_configured_max_priority_and_lowest_confidence`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_relation_parcel_id_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_is_retained_without_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_noncanonical_feature_ids_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_policy_unknown_is_exact_but_unresolved_controlling_overrides`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_status_and_priority_mapping_is_one_to_one_at_every_level`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_touch_relation_remains_context_beside_a_controlling_relation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unknown_relation_type_is_rejected_by_shared_relation_contract`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unresolved_relation_cannot_contain_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_relation`

**Signature**

```python
def _relation(
    *,
    parcel_id: str = "PARCEL-1",
    feature_id: str = "F-1",
    relation_type: str = "AREA_OVERLAP",
    application_status: str = "APPLIED_EXACT_POLICY",
    status: str | None = "MATERIAL_REVIEW_REQUIRED",
    confidence: str | None = "HIGH",
    priority: int | None = 30,
    area: float = 0.000001,
) -> dict[str, object]:
```

**Purpose**

Implements relation according to the exact implementation and guards in this file.

**Inputs**

- `parcel_id` (`str`; optional/default `'PARCEL-1'`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `feature_id` (`str`; optional/default `'F-1'`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relation_type` (`str`; optional/default `'AREA_OVERLAP'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application_status` (`str`; optional/default `'APPLIED_EXACT_POLICY'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `status` (`str | None`; optional/default `'MATERIAL_REVIEW_REQUIRED'`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `confidence` (`str | None`; optional/default `'HIGH'`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `priority` (`int | None`; optional/default `30`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `area` (`float`; optional/default `1e-06`) — area quantity, normally square metres where the name ends in `_m2`. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `row`.

**Algorithm**

1. Computes `(_, _, _, _, application)` from `_application_fixture()`.
2. Checks `relation_type == 'LENGTH_OVERLAP'`. When true: Computes `row` from `application.relations.loc[application.relations['geometry_kind'].eq('LINE')].iloc[0].to_dict()`. Otherwise: Computes `row` from `application.relations.loc[application.relations['geometry_kind'].eq('SURFACE')].iloc[0].to_dict()`.
3. Calls `row.update(parcel_id=parcel_id, planning_feature_id=feature_id, relation_type=relation_type, official_code_status='UNKNOWN_CODE_PAIR' if application_status == 'UNRESOLVED_CODE_PAIR' else 'RESOLVED_OFFICIAL', bess_cnig_policy_application_status=application_status, bess_cnig_precheck_status=status, bess_cnig_precheck_confidence=confidence, bess_cnig_status_pr…` for its validation or side effect.
4. Checks `application_status == 'UNRESOLVED_CODE_PAIR'`. When true: Calls `row.update(official_code_label=None, official_legal_reference=None, official_regulation_reference=None, official_code_source_url=None)` for its validation or side effect.
5. Checks `relation_type == 'AREA_OVERLAP'`. When true: Computes `row['parcel_metric_area_m2']` from `max(float(row['parcel_metric_area_m2']), area)`. Computes `row['feature_area_m2']` from `max(float(row['feature_area_m2']), area)`. Calls `row.update(intersection_area_m2=area, parcel_share_pct=100.0 * area / float(row['parcel_metric_area_m2']), feature_share_pct=100.0 * area / float(row['feature_area_m2']))` for its validation or side effect. Otherwise: Checks `relation_type == 'LENGTH_OVERLAP'`. When true: Computes `row['source_line_length_m']` from `max(float(row['source_line_length_m']), area)`. Computes `row['intersection_length_m']` from `area`. Otherwise: Checks `relation_type == 'TOUCH_ONLY'`. When true: Calls `row.update(intersection_area_m2=0.0, parcel_share_pct=0.0, feature_share_pct=0.0)` for its validation or side effect. Otherwise: Checks `relation_type in {'INSIDE', 'BOUNDARY_TOUCH'}`. When true: Calls `row.update(geometry_kind='POINT', feature_area_m2=None, source_line_length_m=None, intersection_area_m2=None, intersection_length_m=None, parcel_share_pct=None, feature_share_pct=None, point_member_count=1, point_members_inside_count=1 if relation_type == 'INSIDE' else 0, point_members_boundary_count=0 if relation_type == 'INSIDE' else 1)` for its validation or side effect.
6. Returns `row`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_application_fixture`, `application.relations.loc[application.relations['geometry_kind'].eq('LINE')].iloc[0].to_dict`, `application.relations.loc[application.relations['geometry_kind'].eq('SURFACE')].iloc[0].to_dict`, `application.relations['geometry_kind'].eq`, `float`, `max`, `row.update`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_cross_parcel_priority_conflict_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_duplicate_selected_pair_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_invalid_lower_feature_id_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_all_application_identity_scope_and_boundary_fields_are_intrinsic`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_application_relation_suffix_dtype_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_boundary_only_relations_are_contextual`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_complete_five_status_policy_mapping_is_globally_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_coordinated_local_cross_table_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_current_gpu_feature_id_is_canonical`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_document_wide_same_priority_cannot_map_to_two_statuses`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_document_wide_same_status_cannot_map_to_two_priorities`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_duplicate_parcel_feature_identity_is_rejected_for_every_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_every_inherited_application_relation_domain_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_every_positive_relation_type_controls_without_threshold`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_exact_relations_select_configured_max_priority_and_lowest_confidence`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_output_dtype_and_non_2d_parcel_fail_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_invalid_relation_parcel_id_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_no_relation_parcel_is_retained_without_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_noncanonical_feature_ids_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_validation_uses_reprojected_calculation_copy`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_policy_unknown_is_exact_but_unresolved_controlling_overrides`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_parcel_area_is_bound_to_real_parcel_geometry`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_selected_relation_role_requires_selected_status_and_priority`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_status_and_priority_mapping_is_one_to_one_at_every_level`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_touch_relation_remains_context_beside_a_controlling_relation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_unknown_relation_type_is_rejected_by_shared_relation_contract`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_unresolved_relation_cannot_contain_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_all_application_identity_scope_and_boundary_fields_are_intrinsic`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_relation_suffix_dtype_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_boundary_only_relations_are_contextual`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_complete_five_status_policy_mapping_is_globally_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_current_gpu_feature_id_is_canonical`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_priority_cannot_map_to_two_statuses`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_status_cannot_map_to_two_priorities`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_parcel_feature_identity_is_rejected_for_every_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_inherited_application_relation_domain_is_validated_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_positive_relation_type_controls_without_threshold`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_exact_relations_select_configured_max_priority_and_lowest_confidence`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_relation_parcel_id_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_is_retained_without_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_noncanonical_feature_ids_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_policy_unknown_is_exact_but_unresolved_controlling_overrides`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_status_and_priority_mapping_is_one_to_one_at_every_level`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_touch_relation_remains_context_beside_a_controlling_relation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unknown_relation_type_is_rejected_by_shared_relation_contract`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unresolved_relation_cannot_contain_a_decision`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_artifacts`

**Signature**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureParcelAggregationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

**Purpose**

Writes artifacts according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessPlanningFeatureParcelAggregationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[Path, dict[str, Path], dict[str, object]]`. Observed return expression(s): `(manifest_path, paths, manifest)`.

**Algorithm**

1. Computes `frames` from `{'PARCELS': (result.parcels, 'parcels.parquet', True), 'RELATION_ASSESSMENTS': (result.relation_assessments, 'relations.parquet', False)}`.
2. Defines `paths` with annotation `dict[str, Path]` from `{}`.
3. Defines `records` with annotation `list[dict[str, object]]` from `[]`.
4. Iterates `(role, (frame, filename, geospatial))` over `frames.items()`. For each value: Computes `path` from `tmp_path / filename`. Calls `frame.to_parquet(path, index=True)` for its validation or side effect. Computes `paths[role]` from `path`. Executes 3 additional source-ordered statement(s).
5. Computes `scalar_names` from `tuple((field.name for field in fields(BessPlanningFeatureParcelAggregationResult) if field.name not in {'parcels', 'relation_assessments'}))`.
6. Computes `manifest` from `{'schema_version': 1, 'artifact_kind': 'BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT', **{name: getattr(result, name) for name in scalar_names}, 'artifacts': records}`.
7. Calls `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(manifest)` for its validation or side effect.
8. Computes `manifest_path` from `tmp_path / 'aggregation.json'`.
9. Calls `manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8')` for its validation or side effect.
10. Returns `(manifest_path, paths, manifest)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `manifest_path.write_text`, `path.read_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate`, `deterministic_frame_schema_signature`, `fields`, `frame.to_parquet`, `frames.items`, `getattr`, `json.dumps`, `len`, `manifest_path.write_text`, `path.read_bytes`, `records.append`, `sha256`, `sha256(payload).hexdigest`, `signature.get`, `tuple`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_aggregation_loader_rejects_bad_application_before_artifact_reads`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_aggregation_manifest_filenames_are_casefold_unique`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_aggregation_manifest_rejects_nonportable_filename`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_artifact_manifest_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_coordinated_relation_identity_artifact_corruption_fails_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_duplicate_json_and_physical_replacement_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_valid_two_file_verified_byte_artifacts_and_source_readback`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_verified_bytes_are_the_bytes_parsed`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_filenames_are_casefold_unique`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_rejects_nonportable_filename`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_rehash_coordinated_result`

**Signature**

```python
def _rehash_coordinated_result(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Implements rehash coordinated result according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureParcelAggregationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `module._result_with_hashes(updated)`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
2. Computes `source_parcels` from `result.parcels.drop(columns=list(PARCEL_COLUMNS))`.
3. Computes `source_relations` from `result.relation_assessments.drop(columns=list(RELATION_COLUMNS))`.
4. Computes `updated` from `replace(result, source_parcels_content_sha256=module._frame_sha256(source_parcels, 'landscout.bess_cnig_parcel_aggregation.source_parcels'), source_application_relations_content_sha256=module._frame_sha256(source_relations, 'landscout.bess_cnig_parcel_aggregation.source_application_relations'))`.
5. Returns `module._result_with_hashes(updated)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `importlib.import_module`, `list`, `module._frame_sha256`, `module._result_with_hashes`, `replace`, `result.parcels.drop`, `result.relation_assessments.drop`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_coherent_parcel_area_mutation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_cross_parcel_priority_conflict_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_duplicate_selected_pair_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_invalid_lower_feature_id_result`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_validation_uses_reprojected_calculation_copy`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_self_consistent_parcel_area_artifact_is_rejected`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_duplicate_selected_pair_result`

**Signature**

```python
def _duplicate_selected_pair_result() -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Implements duplicate selected pair result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `_rehash_coordinated_result(replace(result, parcels=parcels, relation_assessments=relations))`.

**Algorithm**

1. Computes `result` from `_build_from_relations(pd.DataFrame([_relation(feature_id='A'), _relation(feature_id='B')]))`.
2. Computes `relations` from `result.relation_assessments.copy(deep=True)`.
3. Computes `relations.loc[relations.index[1], 'planning_feature_id']` from `'A'`.
4. Computes `parcels` from `result.parcels.copy(deep=True)`.
5. Computes `parcels.loc[parcels.index[0], 'bess_cnig_selected_feature_ids_json']` from `'["A"]'`.
6. Returns `_rehash_coordinated_result(replace(result, parcels=parcels, relation_assessments=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`, `result.parcels.copy`, `result.relation_assessments.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_build_from_relations`, `_rehash_coordinated_result`, `_relation`, `pd.DataFrame`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_invalid_lower_feature_id_result`

**Signature**

```python
def _invalid_lower_feature_id_result() -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Implements invalid lower feature id result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `_rehash_coordinated_result(replace(result, relation_assessments=relations))`.

**Algorithm**

1. Computes `result` from `_build_from_relations(pd.DataFrame([_relation(feature_id='LOW', status='CONTEXT_REVIEW_REQUIRED', priority=10), _relation(feature_id='HIGH', priority=30)]))`.
2. Computes `relations` from `result.relation_assessments.copy(deep=True)`.
3. Computes `relations.loc[relations.index[0], 'planning_feature_id']` from `'/tmp/feature'`.
4. Returns `_rehash_coordinated_result(replace(result, relation_assessments=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`, `result.relation_assessments.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_build_from_relations`, `_rehash_coordinated_result`, `_relation`, `pd.DataFrame`, `replace`, `result.relation_assessments.copy`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_cross_parcel_priority_conflict_result`

**Signature**

```python
def _cross_parcel_priority_conflict_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

**Purpose**

Implements cross parcel priority conflict result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `_rehash_coordinated_result(replace(result, parcels=parcels, relation_assessments=relations))`.

**Algorithm**

1. Computes `result` from `_build_from_relations(pd.DataFrame([_relation(parcel_id='PARCEL-1', feature_id='A', status='LIKELY_MATERIAL_CONSTRAINT', priority=50), _relation(parcel_id='PARCEL-2', feature_id='B', status='MATERIAL_REVIEW_REQUIRED', priority=30)]))`.
2. Computes `relations` from `result.relation_assessments.copy(deep=True)`.
3. Computes `mask` from `relations['parcel_id'].eq('PARCEL-2')`.
4. Computes `relations.loc[mask, 'bess_cnig_status_priority']` from `50`.
5. Computes `relations.loc[mask, 'bess_cnig_resulting_parcel_status_priority']` from `50`.
6. Computes `parcels` from `result.parcels.copy(deep=True)`.
7. Computes `parcels.loc[parcels['parcel_id'].eq('PARCEL-2'), 'bess_cnig_parcel_status_priority']` from `50`.
8. Returns `_rehash_coordinated_result(replace(result, parcels=parcels, relation_assessments=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`, `result.parcels.copy`, `result.relation_assessments.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_build_from_relations`, `_rehash_coordinated_result`, `_relation`, `parcels['parcel_id'].eq`, `pd.DataFrame`, `relations['parcel_id'].eq`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_surface_touch_semantic_corruption_result`

**Signature**

```python
def _surface_touch_semantic_corruption_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

**Purpose**

Implements surface touch semantic corruption result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `None`; `module._build_result(inputs[1], changed_application)`.

**Algorithm**

1. Computes `(inputs, _, _, _, application)` from `_application_fixture()`.
2. Computes `changed_application` from `_surface_touch_with_positive_area(application)`.
3. Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
4. Computes `original` from `module.validate_bess_application_relation_frame`.
5. Defines the local helper `bypass`; its behavior is documented with the parent function's nested helpers.
6. Computes `module.validate_bess_application_relation_frame` from `bypass`.
7. Runs guarded operation: Returns `module._build_result(inputs[1], changed_application)`. Handles no explicit exception types. Finally: Computes `module.validate_bess_application_relation_frame` from `original`.

**Meaningful nested/local helpers**

- `bypass` — `def bypass(*args: object, **kwargs: object) -> None:`. It executes 1 top-level statement(s), uses no calls, and has no explicit raises. Trivial test callbacks are intentionally grouped here with their parent.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_application_fixture`, `_surface_touch_with_positive_area`, `importlib.import_module`, `module._build_result`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_semantic_failure_fast_fails_before_heavy_validation`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_surface_touch_semantic_corruption_result.bypass`

**Signature**

```python
def bypass(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements bypass according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Returns `None`.

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

### `test_local_corruption_fast_fails_before_heavy_validation.counted`

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

### `_validate_parcel_geometries`

**Signature**

```python
def _validate_parcel_geometries(geometries: list[object]) -> None:
```

**Purpose**

Validates and rejects malformed parcel geometries according to the exact implementation and guards in this file.

**Inputs**

- `geometries` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
2. Computes `(_, _, _, _, application)` from `_application_fixture()`.
3. Computes `parcels` from `gpd.GeoDataFrame({'parcel_id': [f'P-{index}' for index in range(len(geometries))]}, geometry=geometries, crs='EPSG:2154')`.
4. Computes `result` from `module._build_result(parcels, replace(application, relations=application.relations.iloc[0:0]))`.
5. Calls `module._validate_result_envelope(result)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_application_fixture`, `gpd.GeoDataFrame`, `importlib.import_module`, `len`, `module._build_result`, `module._validate_result_envelope`, `range`, `replace`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_malformed_parcel_geometry_is_rejected_intrinsically`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_valid_polygon_and_multipolygon_parcels_are_accepted`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_malformed_parcel_geometry_is_rejected_intrinsically`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_polygon_and_multipolygon_parcels_are_accepted`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_identity_and_global_mapping_fail_before_heavy_validation.counted`

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

### `test_relation_semantic_failure_fast_fails_before_heavy_validation.counted`

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

### `test_representative_intrinsic_failures_all_precede_heavy_validation.counted`

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

### `test_one_aggregation_and_one_public_validation_each_call_heavy_once.counted`

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

### `test_verified_bytes_are_the_bytes_parsed.replace_after_read`

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

1. Computes `payload` from `original_read_bytes(path)`.
2. Checks `path == target`. When true: Calls `path.write_bytes(replacement_bytes)` for its validation or side effect.
3. Returns `payload`.

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

### `test_verified_bytes_are_the_bytes_parsed.inspect_read`

**Signature**

```python
def inspect_read(source: object, *args: object, **kwargs: object) -> object:
```

**Purpose**

Implements inspect read according to the exact implementation and guards in this file.

**Inputs**

- `source` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `original_read(source, *args, **kwargs)`.

**Algorithm**

1. Checks `isinstance(source, BytesIO)`. When true: Calls `observed.append(source.getvalue())` for its validation or side effect.
2. Returns `original_read(source, *args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `isinstance`, `observed.append`, `original_read`, `source.getvalue`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_coherent_parcel_area_mutation`

**Signature**

```python
def _coherent_parcel_area_mutation(
    result: BessPlanningFeatureParcelAggregationResult,
    geometry_kind: str,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Implements coherent parcel area mutation according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureParcelAggregationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `geometry_kind` (`str`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `_rehash_coordinated_result(replace(result, relation_assessments=relations))`.

**Algorithm**

1. Computes `relations` from `result.relation_assessments.copy(deep=True)`.
2. Computes `index` from `relations.index[relations['geometry_kind'].eq(geometry_kind)][0]`.
3. Computes `relations.loc[index, 'parcel_metric_area_m2']` from `8000.0`.
4. Checks `geometry_kind == 'SURFACE'`. When true: Computes `relations.loc[index, 'parcel_share_pct']` from `100.0 * float(relations.loc[index, 'intersection_area_m2']) / 8000.0`.
5. Returns `_rehash_coordinated_result(replace(result, relation_assessments=relations))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`, `result.relation_assessments.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_rehash_coordinated_result`, `float`, `relations['geometry_kind'].eq`, `replace`, `result.relation_assessments.copy`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_parcel_area_is_bound_to_real_parcel_geometry`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_self_consistent_parcel_area_artifact_is_rejected`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_area_defect_fast_fails_before_application_source_validation.counted`

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

### `_changed_parcel_geometry_upstreams`

**Signature**

```python
def _changed_parcel_geometry_upstreams(
    source_parcels: gpd.GeoDataFrame,
    application: object,
) -> tuple[gpd.GeoDataFrame, object]:
```

**Purpose**

Implements changed parcel geometry upstreams according to the exact implementation and guards in this file.

**Inputs**

- `source_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[gpd.GeoDataFrame, object]`. Observed return expression(s): `(changed_parcels, changed_application)`.

**Algorithm**

1. Computes `application_module` from `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')`.
2. Computes `changed_parcels` from `source_parcels.copy(deep=True)`.
3. Computes `parcel_id` from `str(application.relations.iloc[0]['parcel_id'])`.
4. Computes `parcel_index` from `changed_parcels.index[changed_parcels['parcel_id'].eq(parcel_id)][0]`.
5. Computes `geometry_column` from `changed_parcels.geometry.name`.
6. Computes `geometry` from `changed_parcels.loc[parcel_index, geometry_column]`.
7. Computes `changed_parcels.loc[parcel_index, geometry_column]` from `affinity.scale(geometry, xfact=2.0, yfact=2.0, origin='centroid')`.
8. Computes `metric` from `changed_parcels.to_crs(2154).loc[parcel_index, geometry_column].area`.
9. Computes `relations` from `application.relations.copy(deep=True)`.
10. Computes `mask` from `relations['parcel_id'].eq(parcel_id)`.
11. Computes `relations.loc[mask, 'parcel_metric_area_m2']` from `float(metric)`.
12. Computes `surface` from `mask & relations['geometry_kind'].eq('SURFACE')`.
13. Computes `relations.loc[surface, 'parcel_share_pct']` from `100.0 * relations.loc[surface, 'intersection_area_m2'].astype('float64') / float(metric)`.
14. Computes `changed_application` from `application_module._result_with_hashes(replace(application, relations=relations))`.
15. Calls `application_module._validate_result_envelope(changed_application)` for its validation or side effect.
16. Returns `(changed_parcels, changed_application)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `application.relations.copy`, `changed_parcels.to_crs`, `replace`, `source_parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `affinity.scale`, `application.relations.copy`, `application_module._result_with_hashes`, `application_module._validate_result_envelope`, `changed_parcels.to_crs`, `changed_parcels['parcel_id'].eq`, `float`, `importlib.import_module`, `relations.loc[surface, 'intersection_area_m2'].astype`, `relations['geometry_kind'].eq`, `relations['parcel_id'].eq`, `replace`, `source_parcels.copy`, `str`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes.forbidden_heavy`

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

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.counted_build`

**Signature**

```python
def counted_build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Implements counted build according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `actual_build(*args, **kwargs)`.

**Algorithm**

1. Executes `nonlocal build_calls`.
2. Updates `build_calls` using `` and `1`.
3. Returns `actual_build(*args, **kwargs)`.

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

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.forbidden_heavy`

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

### `test_aggregation_loader_rejects_bad_application_before_artifact_reads.counted`

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

### `test_exact_relations_select_configured_max_priority_and_lowest_confidence`

**Signature**

```python
def test_exact_relations_select_configured_max_priority_and_lowest_confidence() -> None:
```

**Purpose**

Protects the `exact relations select configured max priority and lowest confidence` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `relations` from `pd.DataFrame([_relation(feature_id='LOW', priority=10, status='CONTEXT_REVIEW_REQUIRED', area=1000.0), _relation(feature_id='HIGH-A', priority=50, status='LIKELY_MATERIAL_CONSTRAINT', confidence='HIGH'), _relation(feature_id='HIGH-B', priority=50, status='LIKELY_MATERIAL_CONSTRAINT', confidence='LOW')])`.
- Computes `result` from `_build_from_relations(relations)`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_build_from_relations`, `_relation`, `bool`, `pd.DataFrame`, `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist`.

**Expected result**

- Direct assertions: `assert parcel.bess_cnig_parcel_aggregation_status == 'AGGREGATED_EXACT_POLICY'`; `assert parcel.bess_cnig_parcel_precheck_status == 'LIKELY_MATERIAL_CONSTRAINT'`; `assert parcel.bess_cnig_parcel_precheck_confidence == 'LOW'`; `assert parcel.bess_cnig_parcel_status_priority == 50`; `assert parcel.bess_cnig_selected_feature_ids_json == '["HIGH-A","HIGH-B"]'`; `assert parcel.bess_cnig_distinct_exact_status_count == 2`; `assert bool(parcel.bess_cnig_multiple_exact_statuses) is True`; `assert parcel.bess_cnig_selected_relation_count == 2`; `assert parcel.bess_cnig_lower_priority_controlling_relation_count == 1`; `assert result.relation_assessments['bess_cnig_parcel_relation_role'].tolist() == ['LOWER_PRIORITY_CONTROLLING', 'SELECTED_CONTROLLING', 'SELECTED_CONTROLLING']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `exact relations select configured max priority and lowest confidence` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `bool`, `pd.DataFrame`, `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_unknown_is_exact_but_unresolved_controlling_overrides`

**Signature**

```python
def test_policy_unknown_is_exact_but_unresolved_controlling_overrides() -> None:
```

**Purpose**

Protects the `policy unknown is exact but unresolved controlling overrides` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `exact_unknown` from `_build_from_relations(pd.DataFrame([_relation(status='UNKNOWN', confidence='LOW', priority=40)]))`.
- Computes `unresolved` from `_relation(feature_id='UNRESOLVED', application_status='UNRESOLVED_CODE_PAIR', status=None, confidence=None, priority=None)`.
- Computes `mixed` from `_build_from_relations(pd.DataFrame([_relation(), unresolved]))`.
- Computes `parcel` from `mixed.parcels.iloc[0]`.

**Action**

- Calls `_build_from_relations`, `_relation`, `mixed.relation_assessments['bess_cnig_parcel_relation_role'].tolist`, `pd.DataFrame`, `pd.isna`.

**Expected result**

- Direct assertions: `assert exact_unknown.parcels.iloc[0].bess_cnig_parcel_precheck_status == 'UNKNOWN'`; `assert parcel.bess_cnig_parcel_aggregation_status == 'UNRESOLVED_CONTROLLING_CODE_PAIR'`; `assert pd.isna(parcel.bess_cnig_parcel_precheck_status)`; `assert pd.isna(parcel.bess_cnig_parcel_precheck_confidence)`; `assert pd.isna(parcel.bess_cnig_parcel_status_priority)`; `assert parcel.bess_cnig_unresolved_feature_ids_json == '["UNRESOLVED"]'`; `assert mixed.relation_assessments['bess_cnig_parcel_relation_role'].tolist() == ['DEFERRED_BY_UNRESOLVED_CONTROLLING', 'UNRESOLVED_CONTROLLING']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy unknown is exact but unresolved controlling overrides` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `mixed.relation_assessments['bess_cnig_parcel_relation_role'].tolist`, `pd.DataFrame`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_positive_relation_type_controls_without_threshold`

**Signature**

```python
def test_every_positive_relation_type_controls_without_threshold(
    relation_type: str,
) -> None:
```

**Purpose**

Protects the `every positive relation type controls without threshold` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `relation_type`.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(relation_type=relation_type, area=1e-15)]))`.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: `assert result.parcels.iloc[0].bess_cnig_controlling_relation_count == 1`; `assert result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role == 'SELECTED_CONTROLLING'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `every positive relation type controls without threshold` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_boundary_only_relations_are_contextual`

**Signature**

```python
def test_boundary_only_relations_are_contextual(relation_type: str) -> None:
```

**Purpose**

Protects the `boundary only relations are contextual` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `relation_type`.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(relation_type=relation_type)]))`.
- Computes `parcel` from `result.parcels.iloc[0]`.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`, `pd.isna`.

**Expected result**

- Direct assertions: `assert parcel.bess_cnig_parcel_aggregation_status == 'TOUCH_ONLY_RELATIONS_ONLY'`; `assert pd.isna(parcel.bess_cnig_parcel_precheck_status)`; `assert parcel.bess_cnig_touch_only_feature_ids_json == '["F-1"]'`; `assert result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role == 'TOUCH_ONLY_CONTEXT'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `boundary only relations are contextual` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pd.isna`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_touch_relation_remains_context_beside_a_controlling_relation`

**Signature**

```python
def test_touch_relation_remains_context_beside_a_controlling_relation() -> None:
```

**Purpose**

Protects the `touch relation remains context beside a controlling relation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(feature_id='EXACT'), _relation(feature_id='TOUCH', relation_type='TOUCH_ONLY', priority=50, status='LIKELY_MATERIAL_CONSTRAINT')]))`.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`, `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist`.

**Expected result**

- Direct assertions: `assert result.parcels.iloc[0].bess_cnig_parcel_precheck_status == 'MATERIAL_REVIEW_REQUIRED'`; `assert result.relation_assessments['bess_cnig_parcel_relation_role'].tolist() == ['SELECTED_CONTROLLING', 'TOUCH_ONLY_CONTEXT']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `touch relation remains context beside a controlling relation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_relation_parcel_is_retained_without_a_decision`

**Signature**

```python
def test_no_relation_parcel_is_retained_without_a_decision() -> None:
```

**Purpose**

Protects the `no relation parcel is retained without a decision` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation()]))`.
- Computes `parcel` from `result.parcels.iloc[1]`.

**Action**

- Calls `_build_from_relations`, `_relation`, `bool`, `pd.DataFrame`, `pd.isna`.

**Expected result**

- Direct assertions: `assert parcel.bess_cnig_parcel_aggregation_status == 'NO_PLANNING_FEATURE_RELATION'`; `assert pd.isna(parcel.bess_cnig_parcel_precheck_status)`; `assert bool(parcel.bess_cnig_formal_review_required) is True`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `no relation parcel is retained without a decision` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `bool`, `pd.DataFrame`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`

**Signature**

```python
def test_parcel_and_relation_prefixes_order_and_inputs_are_preserved() -> None:
```

**Purpose**

Protects the `parcel and relation prefixes order and inputs are preserved` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application)` from `_application_fixture()`.
- Computes `parcels_copy` from `inputs[1].copy(deep=True)`.
- Computes `relations_copy` from `application.relations.copy(deep=True)`.
- Computes `result` from `aggregate_bess_planning_feature_policy_to_parcels(*inputs, coded, config, policy, application)`.

**Action**

- Calls `_application_fixture`, `aggregate_bess_planning_feature_policy_to_parcels`, `application.relations.copy`, `inputs[1].copy`.

**Expected result**

- Direct assertions: `assert tuple(result.parcels.columns[-len(PARCEL_COLUMNS):]) == PARCEL_COLUMNS`; `assert tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS):]) == RELATION_COLUMNS`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel and relation prefixes order and inputs are preserved` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `aggregate_bess_planning_feature_policy_to_parcels`, `application.relations.copy`, `assert_frame_equal`, `assert_geodataframe_equal`, `inputs[1].copy`, `len`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_local_corruption_fast_fails_before_heavy_validation`

**Signature**

```python
def test_local_corruption_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `local corruption fast fails before heavy validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 7 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application, result)` from `_aggregation_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `parcels.loc[parcels.index[0], 'bess_cnig_selected_relation_count']` from `999`.
- Computes `corrupted` from `module._result_with_hashes(replace(result, parcels=parcels))`.
- Computes `calls` from `0`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, corrupted)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `monkeypatch.setattr`, `replace`, `result.parcels.copy`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, corrupted)`.

**Regression protected**

- Protects the exact `local corruption fast fails before heavy validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `monkeypatch.setattr`, `pytest.raises`, `replace`, `result.parcels.copy`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_local_cross_table_corruption_is_rejected`

**Signature**

```python
def test_coordinated_local_cross_table_corruption_is_rejected(
    frame_name: str,
    column: str,
    value: object,
) -> None:
```

**Purpose**

Protects the `coordinated local cross table corruption is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `frame_name`, `column`, `value`.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(parcel_id='PARCEL-1')]))`.
- Computes `frame` from `getattr(result, frame_name).copy(deep=True)`.
- Computes `frame.loc[frame.index[0], column]` from `value`.
- Computes `corrupted` from `module._result_with_hashes(replace(result, **{frame_name: frame}))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `module._validate_result_envelope(corrupted)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pd.DataFrame`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): module._validate_result_envelope(corrupted)`.

**Regression protected**

- Protects the exact `coordinated local cross table corruption is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `getattr`, `getattr(result, frame_name).copy`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_output_dtype_and_non_2d_parcel_fail_locally`

**Signature**

```python
def test_invalid_output_dtype_and_non_2d_parcel_fail_locally() -> None:
```

**Purpose**

Protects the `invalid output dtype and non 2d parcel fail locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 12 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(parcel_id='PARCEL-1')]))`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `parcels['bess_cnig_selected_relation_count']` from `parcels['bess_cnig_selected_relation_count'].astype('object')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype')` and executes: Calls `module._validate_result_envelope(module._result_with_hashes(replace(result, parcels=parcels)))` for its validation or side effect.
- Computes `relations` from `result.relation_assessments.copy(deep=True)`.
- Computes `relations['bess_cnig_selected_for_parcel_status']` from `relations['bess_cnig_selected_for_parcel_status'].astype('object')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype')` and executes: Calls `module._validate_result_envelope(module._result_with_hashes(replace(result, relation_assessments=relations)))` for its validation or side effect.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `geometry` from `parcels.geometry.iloc[0]`.
- Computes `parcels.at[parcels.index[0], parcels.geometry.name]` from `Polygon([(x, y, 5) for x, y in geometry.exterior.coords])`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='2D')` and executes: Calls `module._validate_result_envelope(replace(result, parcels=parcels))` for its validation or side effect.

**Action**

- Calls `Polygon`, `_build_from_relations`, `_relation`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `parcels['bess_cnig_selected_relation_count'].astype`, `pd.DataFrame`, `relations['bess_cnig_selected_for_parcel_status'].astype`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype'): module._validate_result_envelope(module._result_with_hashes(replace(result, parcels=parcels)))`; `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype'): module._validate_result_envelope(module._result_with_hashes(replace(result, relation_assessments=relations)))`; `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='2D'): module._validate_result_envelope(replace(result, parcels=parcels))`.

**Regression protected**

- Protects the exact `invalid output dtype and non 2d parcel fail locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Polygon`, `_build_from_relations`, `_relation`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `parcels['bess_cnig_selected_relation_count'].astype`, `pd.DataFrame`, `pytest.raises`, `relations['bess_cnig_selected_for_parcel_status'].astype`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_every_inherited_application_relation_domain_is_validated_locally`

**Signature**

```python
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
```

**Purpose**

Protects the `every inherited application relation domain is validated locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `relations`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `_build_from_relations(relations)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): _build_from_relations(relations)`.

**Regression protected**

- Protects the exact `every inherited application relation domain is validated locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unresolved_relation_cannot_contain_a_decision`

**Signature**

```python
def test_unresolved_relation_cannot_contain_a_decision() -> None:
```

**Purpose**

Protects the `unresolved relation cannot contain a decision` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `row` from `_relation(application_status='UNRESOLVED_CODE_PAIR', status='UNKNOWN', confidence='LOW', priority=40)`.
- Computes `row['official_code_status']` from `'UNKNOWN_CODE_PAIR'`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `_build_from_relations(pd.DataFrame([row]))` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): _build_from_relations(pd.DataFrame([row]))`.

**Regression protected**

- Protects the exact `unresolved relation cannot contain a decision` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_all_application_identity_scope_and_boundary_fields_are_intrinsic`

**Signature**

```python
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
```

**Purpose**

Protects the `all application identity scope and boundary fields are intrinsic` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `value`.
- Contains 3 explicit setup/context statement(s).
- Computes `row` from `_relation(relation_type='TOUCH_ONLY')`.
- Computes `row[column]` from `value`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `_build_from_relations(pd.DataFrame([row]))` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): _build_from_relations(pd.DataFrame([row]))`.

**Regression protected**

- Protects the exact `all application identity scope and boundary fields are intrinsic` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_relation_suffix_dtype_is_validated_locally`

**Signature**

```python
def test_application_relation_suffix_dtype_is_validated_locally() -> None:
```

**Purpose**

Protects the `application relation suffix dtype is validated locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `relations` from `pd.DataFrame([_relation()])`.
- Computes `relations['bess_cnig_precheck_status']` from `relations['bess_cnig_precheck_status'].astype('category')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype')` and executes: Calls `_build_from_relations(relations, canonicalize_application_dtypes=False)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`, `relations['bess_cnig_precheck_status'].astype`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype'): _build_from_relations(relations, canonicalize_application_dtypes=False)`.

**Regression protected**

- Protects the exact `application relation suffix dtype is validated locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.raises`, `relations['bess_cnig_precheck_status'].astype`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_status_and_priority_mapping_is_one_to_one_at_every_level`

**Signature**

```python
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
```

**Purpose**

Protects the `status and priority mapping is one to one at every level` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `relations`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority')` and executes: Calls `_build_from_relations(relations)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority'): _build_from_relations(relations)`.

**Regression protected**

- Protects the exact `status and priority mapping is one to one at every level` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

**Signature**

```python
def test_valid_repeated_status_and_priority_mapping_selects_every_exact_match() -> None:
```

**Purpose**

Protects the `valid repeated status and priority mapping selects every exact match` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(feature_id='A', priority=30), _relation(feature_id='B', priority=30)]))`.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`, `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist`.

**Expected result**

- Direct assertions: `assert result.parcels.iloc[0].bess_cnig_selected_relation_count == 2`; `assert result.relation_assessments['bess_cnig_parcel_relation_role'].tolist() == ['SELECTED_CONTROLLING', 'SELECTED_CONTROLLING']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid repeated status and priority mapping selects every exact match` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_parcel_feature_identity_is_rejected_for_every_role`

**Signature**

```python
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
```

**Purpose**

Protects the `duplicate parcel feature identity is rejected for every role` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `relations`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='duplicate|unique')` and executes: Calls `_build_from_relations(relations)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='duplicate|unique'): _build_from_relations(relations)`.

**Regression protected**

- Protects the exact `duplicate parcel feature identity is rejected for every role` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`

**Signature**

```python
def test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role(
    feature_id: object,
) -> None:
```

**Purpose**

Protects the `invalid lower priority feature id is rejected independently of json role` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `feature_id`.
- Contains 2 explicit setup/context statement(s).
- Computes `relations` from `pd.DataFrame([_relation(feature_id=feature_id, status='CONTEXT_REVIEW_REQUIRED', priority=10), _relation(feature_id='HIGH', priority=30)])`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='feature|identity')` and executes: Calls `_build_from_relations(relations)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='feature|identity'): _build_from_relations(relations)`.

**Regression protected**

- Protects the exact `invalid lower priority feature id is rejected independently of json role` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`

**Signature**

```python
def test_invalid_deferred_feature_id_is_rejected_independently_of_json_role(
    feature_id: str,
) -> None:
```

**Purpose**

Protects the `invalid deferred feature id is rejected independently of json role` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `feature_id`.
- Contains 2 explicit setup/context statement(s).
- Computes `relations` from `pd.DataFrame([_relation(feature_id=feature_id), _relation(feature_id='UNRESOLVED', application_status='UNRESOLVED_CODE_PAIR', status=None, confidence=None, priority=None)])`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='feature|identity')` and executes: Calls `_build_from_relations(relations)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='feature|identity'): _build_from_relations(relations)`.

**Regression protected**

- Protects the exact `invalid deferred feature id is rejected independently of json role` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_relation_parcel_id_is_rejected`

**Signature**

```python
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
```

**Purpose**

Protects the `invalid relation parcel id is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `parcel_id`.
- Contains 3 explicit setup/context statement(s).
- Computes `relation` from `_relation()`.
- Computes `relation['parcel_id']` from `parcel_id`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel|identity')` and executes: Calls `_build_from_relations(pd.DataFrame([relation]))` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel|identity'): _build_from_relations(pd.DataFrame([relation]))`.

**Regression protected**

- Protects the exact `invalid relation parcel id is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_relation_type_is_rejected_by_shared_relation_contract`

**Signature**

```python
def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
```

**Purpose**

Protects the `unknown relation type is rejected by shared relation contract` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='relation type')` and executes: Calls `_build_from_relations(pd.DataFrame([_relation(relation_type='NEARBY')]))` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='relation type'): _build_from_relations(pd.DataFrame([_relation(relation_type='NEARBY')]))`.

**Regression protected**

- Protects the exact `unknown relation type is rejected by shared relation contract` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_wide_same_priority_cannot_map_to_two_statuses`

**Signature**

```python
def test_document_wide_same_priority_cannot_map_to_two_statuses(
    context_type: str | None,
) -> None:
```

**Purpose**

Protects the `document wide same priority cannot map to two statuses` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `context_type`.
- Contains 3 explicit setup/context statement(s).
- Computes `second_type` from `context_type or 'AREA_OVERLAP'`.
- Computes `relations` from `pd.DataFrame([_relation(parcel_id='PARCEL-1', feature_id='A', status='LIKELY_MATERIAL_CONSTRAINT', priority=50), _relation(parcel_id='PARCEL-2', feature_id='B', relation_type=second_type, status='MATERIAL_REVIEW_REQUIRED', priority=50)])`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority|mapping')` and executes: Calls `_build_from_relations(relations)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority|mapping'): _build_from_relations(relations)`.

**Regression protected**

- Protects the exact `document wide same priority cannot map to two statuses` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_wide_same_status_cannot_map_to_two_priorities`

**Signature**

```python
def test_document_wide_same_status_cannot_map_to_two_priorities() -> None:
```

**Purpose**

Protects the `document wide same status cannot map to two priorities` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `relations` from `pd.DataFrame([_relation(parcel_id='PARCEL-1', feature_id='A', status='LIKELY_MATERIAL_CONSTRAINT', priority=50), _relation(parcel_id='PARCEL-2', feature_id='B', status='LIKELY_MATERIAL_CONSTRAINT', priority=10)])`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority|mapping')` and executes: Calls `_build_from_relations(relations)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority|mapping'): _build_from_relations(relations)`.

**Regression protected**

- Protects the exact `document wide same status cannot map to two priorities` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`

**Signature**

```python
def test_document_wide_repeated_mapping_and_unresolved_rows_are_valid() -> None:
```

**Purpose**

Protects the `document wide repeated mapping and unresolved rows are valid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `relations` from `pd.DataFrame([_relation(parcel_id='PARCEL-1', feature_id='A', priority=30), _relation(parcel_id='PARCEL-2', feature_id='B', priority=30), _relation(parcel_id='PARCEL-2', feature_id='U', application_status='UNRESOLVED_CODE_PAIR', status=None, confidence=None, priority=None)])`.
- Computes `result` from `_build_from_relations(relations)`.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: `assert len(result.relation_assessments) == 3`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `document wide repeated mapping and unresolved rows are valid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `len`, `pd.DataFrame`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_complete_five_status_policy_mapping_is_globally_valid`

**Signature**

```python
def test_complete_five_status_policy_mapping_is_globally_valid() -> None:
```

**Purpose**

Protects the `complete five status policy mapping is globally valid` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `mapping` from `(('LIKELY_MATERIAL_CONSTRAINT', 50, 'HIGH'), ('UNKNOWN', 40, 'LOW'), ('MATERIAL_REVIEW_REQUIRED', 30, 'HIGH'), ('DESIGN_REVIEW_REQUIRED', 20, 'MEDIUM'), ('CONTEXT_REVIEW_REQUIRED', 10, 'HIGH'))`.
- Computes `relations` from `pd.DataFrame([_relation(parcel_id=f'PARCEL-{position}', feature_id=f'FEATURE-{position}', status=status, priority=priority, confidence=confidence) for position, (status, priority, confidence) in enumerate(mapping, start=1)])`.
- Computes `result` from `_build_from_relations(relations, parcel_ids=tuple((f'PARCEL-{position}' for position in range(1, 6))))`.

**Action**

- Calls `_build_from_relations`, `_relation`, `enumerate`, `pd.DataFrame`, `range`.

**Expected result**

- Direct assertions: `assert len(result.relation_assessments) == 5`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `complete five status policy mapping is globally valid` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `enumerate`, `len`, `pd.DataFrame`, `range`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_selected_relation_role_requires_selected_status_and_priority`

**Signature**

```python
def test_selected_relation_role_requires_selected_status_and_priority() -> None:
```

**Purpose**

Protects the `selected relation role requires selected status and priority` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(feature_id='LOW', status='CONTEXT_REVIEW_REQUIRED', priority=10), _relation(feature_id='HIGH', status='LIKELY_MATERIAL_CONSTRAINT', priority=50)]))`.
- Computes `relations` from `result.relation_assessments.copy(deep=True)`.
- Computes `relations.loc[relations.index[0], 'bess_cnig_parcel_relation_role']` from `'SELECTED_CONTROLLING'`.
- Computes `relations.loc[relations.index[0], 'bess_cnig_selected_for_parcel_status']` from `True`.
- Computes `corrupted` from `module._result_with_hashes(replace(result, relation_assessments=relations))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `module._validate_result_envelope(corrupted)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pd.DataFrame`, `replace`, `result.relation_assessments.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): module._validate_result_envelope(corrupted)`.

**Regression protected**

- Protects the exact `selected relation role requires selected status and priority` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pd.DataFrame`, `pytest.raises`, `replace`, `result.relation_assessments.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_parcel_geometry_is_rejected_intrinsically`

**Signature**

```python
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
```

**Purpose**

Protects the `malformed parcel geometry is rejected intrinsically` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `_validate_parcel_geometries([geometry])` for its validation or side effect.

**Action**

- Calls `LineString`, `Point`, `Polygon`, `_validate_parcel_geometries`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): _validate_parcel_geometries([geometry])`.

**Regression protected**

- Protects the exact `malformed parcel geometry is rejected intrinsically` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `LineString`, `Point`, `Polygon`, `_validate_parcel_geometries`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_polygon_and_multipolygon_parcels_are_accepted`

**Signature**

```python
def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
```

**Purpose**

Protects the `valid polygon and multipolygon parcels are accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `polygon` from `Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])`.

**Action**

- Calls `MultiPolygon`, `Polygon`, `_validate_parcel_geometries`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid polygon and multipolygon parcels are accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `MultiPolygon`, `Polygon`, `_validate_parcel_geometries`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_output_columns_are_rejected_intrinsically`

**Signature**

```python
def test_duplicate_output_columns_are_rejected_intrinsically(frame_name: str) -> None:
```

**Purpose**

Protects the `duplicate output columns are rejected intrinsically` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `frame_name`.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `frame` from `getattr(result, frame_name)`.
- Computes `duplicate` from `pd.concat([frame, frame.iloc[:, [0]]], axis=1)`.
- Computes `corrupted` from `replace(result, **{frame_name: duplicate})`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='duplicate')` and executes: Calls `module._validate_result_envelope(corrupted)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `getattr`, `gpd.GeoDataFrame`, `importlib.import_module`, `module._validate_result_envelope`, `pd.concat`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='duplicate'): module._validate_result_envelope(corrupted)`.

**Regression protected**

- Protects the exact `duplicate output columns are rejected intrinsically` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `getattr`, `gpd.GeoDataFrame`, `importlib.import_module`, `module._validate_result_envelope`, `pd.concat`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_only_application_result_schema_two_is_accepted`

**Signature**

```python
def test_only_application_result_schema_two_is_accepted(version: int) -> None:
```

**Purpose**

Protects the `only application result schema two is accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `version`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `corrupted` from `module._result_with_hashes(replace(result, application_result_hash_schema_version=version))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='application.*schema')` and executes: Calls `module._validate_result_envelope(corrupted)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='application.*schema'): module._validate_result_envelope(corrupted)`.

**Regression protected**

- Protects the exact `only application result schema two is accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_application_result_schema_two_remains_accepted`

**Signature**

```python
def test_application_result_schema_two_remains_accepted() -> None:
```

**Purpose**

Protects the `application result schema two remains accepted` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.

**Action**

- Calls `_aggregation_fixture`, `importlib.import_module`, `module._validate_result_envelope`.

**Expected result**

- Direct assertions: `assert result.application_result_hash_schema_version == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `application result schema two remains accepted` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `importlib.import_module`, `module._validate_result_envelope`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_noncanonical_feature_ids_are_rejected`

**Signature**

```python
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
```

**Purpose**

Protects the `noncanonical feature ids are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `feature_id`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='Feature ID')` and executes: Calls `_build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='Feature ID'): _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))`.

**Regression protected**

- Protects the exact `noncanonical feature ids are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_current_gpu_feature_id_is_canonical`

**Signature**

```python
def test_current_gpu_feature_id_is_canonical() -> None:
```

**Purpose**

Protects the `current gpu feature id is canonical` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `feature_id` from `'GPU:DOC:prescription_surface:FEATURE-01'`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))`.

**Action**

- Calls `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Expected result**

- Direct assertions: `assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == f'["{feature_id}"]'`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `current gpu feature id is canonical` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `pd.DataFrame`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_authorized_status_artifact_fails_local_verified_byte_loading`

**Signature**

```python
def test_authorized_status_artifact_fails_local_verified_byte_loading(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `authorized status artifact fails local verified byte loading` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 12 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation()]))`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `parcels.loc[parcels.index[0], 'bess_cnig_parcel_precheck_status']` from `'AUTHORIZED'`.
- Computes `assessed` from `result.relation_assessments.copy(deep=True)`.
- Computes `assessed.loc[assessed.index[0], 'bess_cnig_precheck_status']` from `'AUTHORIZED'`.
- Computes `assessed.loc[assessed.index[0], 'bess_cnig_resulting_parcel_precheck_status']` from `'AUTHORIZED'`.
- Computes `source` from `assessed.drop(columns=list(RELATION_COLUMNS))`.
- Computes `corrupted` from `replace(result, parcels=parcels, relation_assessments=assessed, source_application_relations_content_sha256=module._frame_sha256(source, 'landscout.bess_cnig_parcel_aggregation.source_application_relations'))`.
- Computes `corrupted` from `module._result_with_hashes(corrupted)`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, corrupted)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `_write_artifacts`, `assessed.drop`, `importlib.import_module`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `module._frame_sha256`, `module._result_with_hashes`, `pd.DataFrame`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Regression protected**

- Protects the exact `authorized status artifact fails local verified byte loading` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `_write_artifacts`, `assessed.drop`, `importlib.import_module`, `list`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `module._frame_sha256`, `module._result_with_hashes`, `pd.DataFrame`, `pytest.raises`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_relation_identity_artifact_corruption_fails_locally`

**Signature**

```python
def test_coordinated_relation_identity_artifact_corruption_fails_locally(
    tmp_path: Path,
    factory: object,
) -> None:
```

**Purpose**

Protects the `coordinated relation identity artifact corruption fails locally` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `factory`.
- Contains 3 explicit setup/context statement(s).
- Computes `corrupted` from `factory()`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, corrupted)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.

**Action**

- Calls `_write_artifacts`, `callable`, `factory`, `load_bess_planning_feature_parcel_aggregation_artifacts`.

**Expected result**

- Direct assertions: `assert callable(factory)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Regression protected**

- Protects the exact `coordinated relation identity artifact corruption fails locally` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_write_artifacts`, `callable`, `factory`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`

**Signature**

```python
def test_controlling_relation_cannot_be_relabelled_contextual_in_artifact(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `controlling relation cannot be relabelled contextual in artifact` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `corrupted` from `_surface_touch_semantic_corruption_result()`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, corrupted)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='surface|metric|type')` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.

**Action**

- Calls `_surface_touch_semantic_corruption_result`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='surface|metric|type'): load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Regression protected**

- Protects the exact `controlling relation cannot be relabelled contextual in artifact` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_surface_touch_semantic_corruption_result`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_no_relation_parcel_rejects_textual_null_identity`

**Signature**

```python
def test_no_relation_parcel_rejects_textual_null_identity(
    tmp_path: Path, parcel_id: str
) -> None:
```

**Purpose**

Protects the `no relation parcel rejects textual null identity` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `parcel_id`.
- Contains 12 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(parcel_id='PARCEL-1')]))`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `no_relation` from `parcels['bess_cnig_parcel_aggregation_status'].eq('NO_PLANNING_FEATURE_RELATION')`.
- Computes `parcel_id_dtype` from `parcels['parcel_id'].dtype`.
- Computes `parcels.loc[parcels.index[no_relation][0], 'parcel_id']` from `parcel_id`.
- Computes `parcels['parcel_id']` from `pd.array(parcels['parcel_id'].tolist(), dtype=parcel_id_dtype)`.
- Computes `corrupted` from `module._result_with_hashes(replace(result, parcels=parcels))`.
- Computes `(manifest, paths, payload)` from `_write_artifacts(tmp_path, corrupted)`.
- Computes `persisted_parcels` from `gpd.read_parquet(paths['PARCELS'])`.
- Computes `persisted_relations` from `pd.read_parquet(paths['RELATION_ASSESSMENTS'])`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel ID')` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_relation`, `_write_artifacts`, `deterministic_frame_schema_signature`, `gpd.read_parquet`, `importlib.import_module`, `json.dumps`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest.write_text`, `module._result_with_hashes`, `no_relation.any`, `parcels['bess_cnig_parcel_aggregation_status'].eq`, `parcels['parcel_id'].tolist`, `pd.DataFrame`, `pd.array`, `pd.read_parquet`, `replace`, `result.parcels.copy`.

**Expected result**

- Direct assertions: `assert no_relation.any()`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel ID'): load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Regression protected**

- Protects the exact `no relation parcel rejects textual null identity` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_relation`, `_write_artifacts`, `deterministic_frame_schema_signature`, `gpd.read_parquet`, `importlib.import_module`, `json.dumps`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest.write_text`, `module._result_with_hashes`, `no_relation.any`, `parcels['bess_cnig_parcel_aggregation_status'].eq`, `parcels['parcel_id'].tolist`, `pd.DataFrame`, `pd.array`, `pd.read_parquet`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Signature**

```python
def test_relation_identity_and_global_mapping_fail_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `relation identity and global mapping fail before heavy validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 3 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application, _)` from `_aggregation_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `calls` from `0`.

**Action**

- Calls `_aggregation_fixture`, `_cross_parcel_priority_conflict_result`, `_duplicate_selected_pair_result`, `_invalid_lower_feature_id_result`, `importlib.import_module`, `monkeypatch.setattr`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, corrupted)`.

**Regression protected**

- Protects the exact `relation identity and global mapping fail before heavy validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_cross_parcel_priority_conflict_result`, `_duplicate_selected_pair_result`, `_invalid_lower_feature_id_result`, `importlib.import_module`, `monkeypatch.setattr`, `pytest.raises`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_semantic_failure_fast_fails_before_heavy_validation`

**Signature**

```python
def test_relation_semantic_failure_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `relation semantic failure fast fails before heavy validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 4 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application, _)` from `_aggregation_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `calls` from `0`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, _surface_touch_semantic_corruption_result())` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `_surface_touch_semantic_corruption_result`, `importlib.import_module`, `monkeypatch.setattr`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, _surface_touch_semantic_corruption_result())`.

**Regression protected**

- Protects the exact `relation semantic failure fast fails before heavy validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_surface_touch_semantic_corruption_result`, `importlib.import_module`, `monkeypatch.setattr`, `pytest.raises`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_decision_status_domain_rejects_forbidden_vocabulary`

**Signature**

```python
def test_parcel_decision_status_domain_rejects_forbidden_vocabulary(
    status: str,
) -> None:
```

**Purpose**

Protects the `parcel decision status domain rejects forbidden vocabulary` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `status`.
- Contains 7 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `decision_index` from `parcels.index[parcels['bess_cnig_parcel_aggregation_status'] == 'AGGREGATED_EXACT_POLICY'][0]`.
- Computes `parcels.loc[decision_index, 'bess_cnig_parcel_precheck_status']` from `status`.
- Computes `corrupted` from `module._result_with_hashes(replace(result, parcels=parcels))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='status')` and executes: Calls `module._validate_result_envelope(corrupted)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='status'): module._validate_result_envelope(corrupted)`.

**Regression protected**

- Protects the exact `parcel decision status domain rejects forbidden vocabulary` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_persisted_feature_id_json_must_be_portable_and_canonical`

**Signature**

```python
def test_persisted_feature_id_json_must_be_portable_and_canonical(
    json_value: str,
) -> None:
```

**Purpose**

Protects the `persisted feature id json must be portable and canonical` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `json_value`.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `parcels` from `result.parcels.copy(deep=True)`.
- Computes `parcels.loc[parcels.index[0], 'bess_cnig_selected_feature_ids_json']` from `json_value`.
- Computes `corrupted` from `module._result_with_hashes(replace(result, parcels=parcels))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `module._validate_result_envelope(corrupted)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `result.parcels.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): module._validate_result_envelope(corrupted)`.

**Regression protected**

- Protects the exact `persisted feature id json must be portable and canonical` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_representative_intrinsic_failures_all_precede_heavy_validation`

**Signature**

```python
def test_representative_intrinsic_failures_all_precede_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `representative intrinsic failures all precede heavy validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 16 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application, result)` from `_aggregation_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `calls` from `0`.
- Defines `invalid_results` with annotation `list[BessPlanningFeatureParcelAggregationResult]` from `[]`.
- Computes `inherited` from `result.relation_assessments.copy(deep=True)`.
- Computes `inherited.loc[inherited.index[0], 'bess_cnig_precheck_status']` from `'AUTHORIZED'`.
- Computes `parcel_status` from `result.parcels.copy(deep=True)`.
- Computes `parcel_status.loc[parcel_status.index[0], 'bess_cnig_parcel_precheck_status']` from `'AUTHORIZED'`.
- Computes `ambiguous` from `_build_from_relations(pd.DataFrame([_relation(feature_id='A', priority=50), _relation(feature_id='B', status='DESIGN_REVIEW_REQUIRED', priority=10)]))`.
- Computes `ambiguous_relations` from `ambiguous.relation_assessments.copy(deep=True)`.
- Computes `ambiguous_relations.loc[ambiguous_relations.index[1], 'bess_cnig_status_priority']` from `50`.
- Computes `point_parcels` from `result.parcels.copy(deep=True)`.

**Action**

- Calls `Point`, `_aggregation_fixture`, `_build_from_relations`, `_rehash_coordinated_result`, `_relation`, `ambiguous.relation_assessments.copy`, `gpd.GeoDataFrame`, `importlib.import_module`, `invalid_results.append`, `module._result_with_hashes`, `monkeypatch.setattr`, `pd.DataFrame`, `pd.concat`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, invalid)`.

**Regression protected**

- Protects the exact `representative intrinsic failures all precede heavy validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Point`, `_aggregation_fixture`, `_build_from_relations`, `_rehash_coordinated_result`, `_relation`, `ambiguous.relation_assessments.copy`, `gpd.GeoDataFrame`, `importlib.import_module`, `invalid_results.append`, `module._result_with_hashes`, `monkeypatch.setattr`, `pd.DataFrame`, `pd.concat`, `pytest.raises`, `replace`, `result.parcels.copy`, `result.relation_assessments.copy`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_aggregation_and_one_public_validation_each_call_heavy_once`

**Signature**

```python
def test_one_aggregation_and_one_public_validation_each_call_heavy_once(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `one aggregation and one public validation each call heavy once` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application)` from `_application_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `actual` from `module.validate_bess_planning_feature_application_result`.
- Computes `calls` from `0`.
- Computes `result` from `module.aggregate_bess_planning_feature_policy_to_parcels(*inputs, coded, config, policy, application)`.

**Action**

- Calls `_application_fixture`, `actual`, `importlib.import_module`, `module.aggregate_bess_planning_feature_policy_to_parcels`, `module.validate_bess_planning_feature_parcel_aggregation_result`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert calls == 1`; `assert calls == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `one aggregation and one public validation each call heavy once` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_application_fixture`, `actual`, `importlib.import_module`, `module.aggregate_bess_planning_feature_policy_to_parcels`, `module.validate_bess_planning_feature_parcel_aggregation_result`, `monkeypatch.setattr`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_two_file_verified_byte_artifacts_and_source_readback`

**Signature**

```python
def test_valid_two_file_verified_byte_artifacts_and_source_readback(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `valid two file verified byte artifacts and source readback` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application, result)` from `_aggregation_fixture()`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `loaded` from `load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Action**

- Calls `_aggregation_fixture`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid two file verified byte artifacts and source readback` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_write_artifacts`, `assert_frame_equal`, `assert_geodataframe_equal`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_manifest_corruption_is_rejected`

**Signature**

```python
def test_artifact_manifest_corruption_is_rejected(
    tmp_path: Path, mutation: object
) -> None:
```

**Purpose**

Protects the `artifact manifest corruption is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`.
- Contains 3 explicit setup/context statement(s).
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `(manifest_path, paths, manifest)` from `_write_artifacts(tmp_path, result)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest_path, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `_write_artifacts`, `callable`, `json.dumps`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest_path.write_text`, `mutation`, `value.update`, `value['artifacts'].append`, `value['artifacts'].pop`, `value['artifacts'][0].update`, `value['artifacts'][0]['frame_schema_signature'].update`, `value['artifacts'][1].update`.

**Expected result**

- Direct assertions: `assert callable(mutation)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): load_bess_planning_feature_parcel_aggregation_artifacts(manifest_path, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Regression protected**

- Protects the exact `artifact manifest corruption is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_write_artifacts`, `callable`, `dict`, `json.dumps`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest_path.write_text`, `mutation`, `pytest.mark.parametrize`, `pytest.raises`, `value.update`, `value['artifacts'].append`, `value['artifacts'].pop`, `value['artifacts'][0].update`, `value['artifacts'][0]['frame_schema_signature'].update`, `value['artifacts'][1].update`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_json_and_physical_replacement_are_rejected`

**Signature**

```python
def test_duplicate_json_and_physical_replacement_are_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate json and physical replacement are rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `(manifest_path, paths, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `original` from `manifest_path.read_text(encoding='utf-8')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='Duplicate JSON')` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest_path, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='size|SHA')` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest_path, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest_path.read_text`, `manifest_path.write_text`, `paths['RELATION_ASSESSMENTS'].read_bytes`, `paths['RELATION_ASSESSMENTS'].write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='Duplicate JSON'): load_bess_planning_feature_parcel_aggregation_artifacts(manifest_path, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`; `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='size|SHA'): load_bess_planning_feature_parcel_aggregation_artifacts(manifest_path, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Regression protected**

- Protects the exact `duplicate json and physical replacement are rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest_path.read_text`, `manifest_path.write_text`, `paths['RELATION_ASSESSMENTS'].read_bytes`, `paths['RELATION_ASSESSMENTS'].write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_verified_bytes_are_the_bytes_parsed`

**Signature**

```python
def test_verified_bytes_are_the_bytes_parsed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `verified bytes are the bytes parsed` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 11 explicit setup/context statement(s).
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `(manifest_path, paths, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `target` from `paths['RELATION_ASSESSMENTS']`.
- Computes `verified` from `target.read_bytes()`.
- Computes `replacement` from `tmp_path / 'replacement.parquet'`.
- Computes `replacement_bytes` from `replacement.read_bytes()`.
- Computes `original_read_bytes` from `Path.read_bytes`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `original_read` from `module.pd.read_parquet`.
- Defines `observed` with annotation `list[bytes]` from `[]`.
- Computes `loaded` from `load_bess_planning_feature_parcel_aggregation_artifacts(manifest_path, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Action**

- Calls `_aggregation_fixture`, `_write_artifacts`, `importlib.import_module`, `isinstance`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `monkeypatch.setattr`, `observed.append`, `original_read`, `original_read_bytes`, `path.write_bytes`, `replacement.read_bytes`, `result.relation_assessments.to_parquet`, `source.getvalue`, `target.read_bytes`.

**Expected result**

- Direct assertions: `assert verified in observed`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `verified bytes are the bytes parsed` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_write_artifacts`, `assert_frame_equal`, `importlib.import_module`, `isinstance`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `monkeypatch.setattr`, `observed.append`, `original_read`, `original_read_bytes`, `path.write_bytes`, `replacement.read_bytes`, `result.relation_assessments.to_parquet`, `source.getvalue`, `target.read_bytes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_exports_are_stable`

**Signature**

```python
def test_public_exports_are_stable() -> None:
```

**Purpose**

Protects the `public exports are stable` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `required` from `{'BessPlanningFeatureParcelAggregationArtifactManifest', 'BessPlanningFeatureParcelAggregationError', 'BessPlanningFeatureParcelAggregationResult', 'aggregate_bess_planning_feature_policy_to_parcels', 'load_bess_planning_feature_parcel_aggregation_artifacts', 'validate_bess_planning_feature_parcel_aggregation_result'}`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.

**Action**

- Calls `importlib.import_module`, `required.issubset`.

**Expected result**

- Direct assertions: `assert set(module.__all__) == required`; `assert required.issubset(set(stages.__all__))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public exports are stable` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `importlib.import_module`, `required.issubset`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_parcel_area_is_bound_to_real_parcel_geometry`

**Signature**

```python
def test_relation_parcel_area_is_bound_to_real_parcel_geometry(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

**Purpose**

Protects the `relation parcel area is bound to real parcel geometry` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `geometry_kind`, `relation_type`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(relation_type=relation_type)]))`.
- Computes `changed` from `_coherent_parcel_area_mutation(result, geometry_kind)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel.*area|area.*parcel')` and executes: Calls `module._validate_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_coherent_parcel_area_mutation`, `_relation`, `importlib.import_module`, `module._validate_result_envelope`, `pd.DataFrame`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel.*area|area.*parcel'): module._validate_result_envelope(changed)`.

**Regression protected**

- Protects the exact `relation parcel area is bound to real parcel geometry` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_coherent_parcel_area_mutation`, `_relation`, `importlib.import_module`, `module._validate_result_envelope`, `pd.DataFrame`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_self_consistent_parcel_area_artifact_is_rejected`

**Signature**

```python
def test_self_consistent_parcel_area_artifact_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `self consistent parcel area artifact is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 6 explicit setup/context statement(s).
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(area=1.0)]))`.
- Computes `changed` from `_coherent_parcel_area_mutation(result, 'SURFACE')`.
- Computes `(manifest, paths, payload)` from `_write_artifacts(tmp_path, changed)`.
- Computes `persisted` from `{'PARCELS': gpd.read_parquet(paths['PARCELS']), 'RELATION_ASSESSMENTS': pd.read_parquet(paths['RELATION_ASSESSMENTS'])}`.
- Computes `persisted_result` from `_rehash_coordinated_result(replace(changed, parcels=persisted['PARCELS'], relation_assessments=persisted['RELATION_ASSESSMENTS']))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel.*area|area.*parcel')` and executes: Calls `load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])` for its validation or side effect.

**Action**

- Calls `_build_from_relations`, `_coherent_parcel_area_mutation`, `_rehash_coordinated_result`, `_relation`, `_write_artifacts`, `deterministic_frame_schema_signature`, `fields`, `getattr`, `gpd.read_parquet`, `json.dumps`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest.write_text`, `pd.DataFrame`, `pd.read_parquet`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel.*area|area.*parcel'): load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'])`.

**Regression protected**

- Protects the exact `self consistent parcel area artifact is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_coherent_parcel_area_mutation`, `_rehash_coordinated_result`, `_relation`, `_write_artifacts`, `deterministic_frame_schema_signature`, `fields`, `getattr`, `gpd.read_parquet`, `json.dumps`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `manifest.write_text`, `pd.DataFrame`, `pd.read_parquet`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_area_validation_uses_reprojected_calculation_copy`

**Signature**

```python
def test_parcel_area_validation_uses_reprojected_calculation_copy() -> None:
```

**Purpose**

Protects the `parcel area validation uses reprojected calculation copy` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(area=1.0)]))`.
- Computes `original` from `result.parcels.copy(deep=True)`.
- Computes `geographic` from `result.parcels.to_crs('EPSG:4326')`.
- Computes `changed` from `_rehash_coordinated_result(replace(result, parcels=geographic))`.

**Action**

- Calls `_build_from_relations`, `_rehash_coordinated_result`, `_relation`, `importlib.import_module`, `module._validate_result_envelope`, `pd.DataFrame`, `replace`, `result.parcels.copy`, `result.parcels.to_crs`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `parcel area validation uses reprojected calculation copy` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_build_from_relations`, `_rehash_coordinated_result`, `_relation`, `assert_geodataframe_equal`, `importlib.import_module`, `module._validate_result_envelope`, `pd.DataFrame`, `replace`, `result.parcels.copy`, `result.parcels.to_crs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_area_defect_fast_fails_before_application_source_validation`

**Signature**

```python
def test_parcel_area_defect_fast_fails_before_application_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `parcel area defect fast fails before application source validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(inputs, coded, config, policy, application, _)` from `_aggregation_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `result` from `_build_from_relations(pd.DataFrame([_relation(area=1.0)]))`.
- Computes `changed` from `_coherent_parcel_area_mutation(result, 'SURFACE')`.
- Computes `calls` from `0`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError)` and executes: Calls `validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, changed)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `_build_from_relations`, `_coherent_parcel_area_mutation`, `_relation`, `importlib.import_module`, `monkeypatch.setattr`, `pd.DataFrame`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError): validate_bess_planning_feature_parcel_aggregation_result(*inputs, coded, config, policy, application, changed)`.

**Regression protected**

- Protects the exact `parcel area defect fast fails before application source validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_build_from_relations`, `_coherent_parcel_area_mutation`, `_relation`, `importlib.import_module`, `monkeypatch.setattr`, `pd.DataFrame`, `pytest.raises`, `validate_bess_planning_feature_parcel_aggregation_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams`

**Signature**

```python
def test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams() -> None:
```

**Purpose**

Protects the `step 7d 5b 2b 5 aggregation loader requires exact upstreams` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.

**Action**

- Calls `hasattr`, `importlib.import_module`, `inspect.signature`.

**Expected result**

- Direct assertions: `assert tuple(inspect.signature(module.load_bess_planning_feature_parcel_aggregation_artifacts).parameters) == ('manifest_path', 'parcels_path', 'relation_assessments_path', 'source_parcels', 'application_result')`; `assert hasattr(module, 'validate_bess_planning_feature_application_result_envelope')`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `step 7d 5b 2b 5 aggregation loader requires exact upstreams` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `hasattr`, `importlib.import_module`, `inspect.signature`, `tuple`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`

**Signature**

```python
def test_source_bound_aggregation_loader_accepts_only_supplied_upstreams(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `source bound aggregation loader accepts only supplied upstreams` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 3 explicit setup/context statement(s).
- Computes `(inputs, _, _, _, application, result)` from `_aggregation_fixture()`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `loaded` from `load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'], inputs[1], application)`.

**Action**

- Calls `_aggregation_fixture`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`.

**Expected result**

- Direct assertions: `assert loaded.complete_result_content_sha256 == result.complete_result_content_sha256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source bound aggregation loader accepts only supplied upstreams` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_aggregation_manifest_filenames_are_casefold_unique`

**Signature**

```python
def test_aggregation_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
```

**Purpose**

Protects the `aggregation manifest filenames are casefold unique` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `(_, _, payload)` from `_write_artifacts(tmp_path, result)`.
- Computes `payload['artifacts'][1]['filename']` from `str(payload['artifacts'][0]['filename']).upper()`.
- Enters managed context(s) `pytest.raises(ValueError, match='filename|duplicate')` and executes: Calls `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate`, `_aggregation_fixture`, `_write_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='filename|duplicate'): BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)`.

**Regression protected**

- Protects the exact `aggregation manifest filenames are casefold unique` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate`, `_aggregation_fixture`, `_write_artifacts`, `pytest.raises`, `str`, `str(payload['artifacts'][0]['filename']).upper`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`

**Signature**

```python
def test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

**Purpose**

Protects the `source bound aggregation loader rejects coordinated upstream changes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `mutation`.
- Contains 9 explicit setup/context statement(s).
- Computes `(inputs, _, _, _, application, _)` from `_aggregation_fixture()`.
- Computes `source_parcels` from `inputs[1]`.
- Computes `changed_parcels` from `source_parcels.copy(deep=True)`.
- Computes `changed_application` from `application`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `changed` from `module._build_result(changed_parcels, changed_application)`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, changed)`.
- Computes `heavy_calls` from `0`.
- Enters managed context(s) `pytest.raises(BessPlanningFeatureParcelAggregationError, match='source lock')` and executes: Calls `module.load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'], source_parcels, application)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `_changed_parcel_geometry_upstreams`, `_coordinated_policy_mutation`, `_write_artifacts`, `affinity.translate`, `changed_parcels['parcel_id'].isin`, `extra.geometry.map`, `gpd.GeoDataFrame`, `importlib.import_module`, `int`, `module._build_result`, `module._validate_result_envelope`, `module.load_bess_planning_feature_parcel_aggregation_artifacts`, `monkeypatch.setattr`, `pd.Index`, `pd.array`, `pd.concat`, `source_parcels.copy`, `source_parcels.iloc[::-1].copy`, `source_parcels.iloc[[0]].copy`, `source_parcels.index.max`, `source_parcels.to_crs`.

**Expected result**

- Direct assertions: `assert heavy_calls == 0`; `assert not available.empty`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeatureParcelAggregationError, match='source lock'): module.load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'], source_parcels, application)`.

**Regression protected**

- Protects the exact `source bound aggregation loader rejects coordinated upstream changes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_changed_parcel_geometry_upstreams`, `_coordinated_policy_mutation`, `_write_artifacts`, `affinity.translate`, `changed_parcels['parcel_id'].isin`, `extra.geometry.map`, `gpd.GeoDataFrame`, `importlib.import_module`, `int`, `module._build_result`, `module._validate_result_envelope`, `module.load_bess_planning_feature_parcel_aggregation_artifacts`, `monkeypatch.setattr`, `pd.Index`, `pd.array`, `pd.concat`, `pytest.mark.parametrize`, `pytest.raises`, `set`, `source_parcels.copy`, `source_parcels.iloc[::-1].copy`, `source_parcels.iloc[[0]].copy`, `source_parcels.index.max`, `source_parcels.to_crs`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`

**Signature**

```python
def test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `source bound aggregation loader rebuilds once without mutating upstreams` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 10 explicit setup/context statement(s).
- Computes `(inputs, _, _, _, application, result)` from `_aggregation_fixture()`.
- Computes `source_parcels` from `inputs[1]`.
- Computes `parcels_before` from `source_parcels.copy(deep=True)`.
- Computes `relations_before` from `application.relations.copy(deep=True)`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.aggregate_bess_planning_feature_policy')`.
- Computes `actual_build` from `module._build_result`.
- Computes `build_calls` from `0`.
- Computes `heavy_calls` from `0`.
- Computes `loaded` from `module.load_bess_planning_feature_parcel_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'], source_parcels, application)`.

**Action**

- Calls `_aggregation_fixture`, `_write_artifacts`, `actual_build`, `application.relations.copy`, `importlib.import_module`, `module.load_bess_planning_feature_parcel_aggregation_artifacts`, `monkeypatch.setattr`, `source_parcels.copy`.

**Expected result**

- Direct assertions: `assert loaded.complete_result_content_sha256 == result.complete_result_content_sha256`; `assert build_calls == 1`; `assert heavy_calls == 0`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `source bound aggregation loader rebuilds once without mutating upstreams` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks; actual in-memory geometry. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_write_artifacts`, `actual_build`, `application.relations.copy`, `assert_frame_equal`, `assert_geodataframe_equal`, `importlib.import_module`, `module.load_bess_planning_feature_parcel_aggregation_artifacts`, `monkeypatch.setattr`, `source_parcels.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_aggregation_loader_rejects_bad_application_before_artifact_reads`

**Signature**

```python
def test_aggregation_loader_rejects_bad_application_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

**Purpose**

Protects the `aggregation loader rejects bad application before artifact reads` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(inputs, _, _, _, application, result)` from `_aggregation_fixture()`.
- Computes `(manifest, paths, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `reads` from `0`.
- Computes `original` from `Path.read_bytes`.
- Computes `forged` from `replace(application, complete_result_content_sha256='0' * 64)`.
- Enters managed context(s) `pytest.raises(Exception, match='hash|SHA|invalid')` and executes: Calls `_load_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'], inputs[1], forged)` for its validation or side effect.

**Action**

- Calls `_aggregation_fixture`, `_load_aggregation_artifacts`, `_write_artifacts`, `monkeypatch.setattr`, `original`, `replace`.

**Expected result**

- Direct assertions: `assert reads == 0`.
- Expected exception contexts: `with pytest.raises(Exception, match='hash|SHA|invalid'): _load_aggregation_artifacts(manifest, paths['PARCELS'], paths['RELATION_ASSESSMENTS'], inputs[1], forged)`.

**Regression protected**

- Protects the exact `aggregation loader rejects bad application before artifact reads` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_aggregation_fixture`, `_load_aggregation_artifacts`, `_write_artifacts`, `monkeypatch.setattr`, `original`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_aggregation_manifest_rejects_nonportable_filename`

**Signature**

```python
def test_aggregation_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
```

**Purpose**

Protects the `aggregation manifest rejects nonportable filename` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `filename`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, _, _, result)` from `_aggregation_fixture()`.
- Computes `(_, _, payload)` from `_write_artifacts(tmp_path, result)`.
- Computes `payload['artifacts'][0]['filename']` from `filename`.
- Enters managed context(s) `pytest.raises(ValueError, match='filename|basename|portable')` and executes: Calls `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate`, `_aggregation_fixture`, `_write_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='filename|basename|portable'): BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)`.

**Regression protected**

- Protects the exact `aggregation manifest rejects nonportable filename` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate`, `_aggregation_fixture`, `_write_artifacts`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `PARCELS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `RELATION_ASSESSMENTS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `artifact_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `artifacts` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_aggregation_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_application_result_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_confidence_aggregation_method` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_distinct_exact_status_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_exact_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_formal_review_required` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_legal_conclusion_produced` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_limitations` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_feature_text_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_regulation_content_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_lower_priority_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_multiple_exact_statuses` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_aggregation_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_rejection_performed` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_relation_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_status_aggregated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_result_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_required_human_action` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_aggregation_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_score_calculated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_selected_feature_ids_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_selected_for_parcel_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_selected_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_touch_only_feature_ids_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_touch_only_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_unresolved_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_unresolved_feature_ids_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `feature_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `filename` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `frame_schema_signature` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `prior` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_line_length_m` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | linear distance/length in metres; proxy meaning is limited by the introducing stage. Consumers and exact calculations are the functions that reference this column above. |

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
