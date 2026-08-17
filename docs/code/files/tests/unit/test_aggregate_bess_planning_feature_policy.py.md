# `tests/unit/test_aggregate_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_aggregate_bess_planning_feature_policy.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.
- Source SHA256: `37eb958e761dc00eb6dde5389923fd24f0a60457f0beeacac976be0dc96a3cc2`

## 1. Purpose

Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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
- `from shapely import affinity`
- `from shapely.geometry import LineString, MultiPolygon, Point, Polygon`
- `from test_apply_bess_planning_feature_policy import (
    _application_fixture,
    _coordinated_policy_mutation,
    _surface_touch_with_positive_area,
)`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.common.bess_application_contract import (
    POLICY_COLUMNS,
    POLICY_SUFFIX_DTYPES,
)`
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.common.planning_feature_schema import relation_columns, relation_dtypes`
- `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- `from landscout.stages.aggregate_bess_planning_feature_policy import (
    load_bess_planning_feature_parcel_aggregation_artifacts as _load_aggregation_artifacts,
)`

## 4. Contract taxonomy

### A. Python constants

#### `PARCEL_COLUMNS`

```python
PARCEL_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_formal_review_required",
    "bess_cnig_aggregation_scope",
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
    "bess_cnig_application_result_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` (value reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` (value reference).

#### `RELATION_COLUMNS`

```python
RELATION_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_selected_for_parcel_status",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
    "bess_cnig_resulting_parcel_status_priority",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` (value reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` (value reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` (value reference).

#### `_LAST_SOURCE_PARCELS`

```python
_LAST_SOURCE_PARCELS: gpd.GeoDataFrame | None = None
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` (value reference).

#### `_LAST_APPLICATION_RESULT`

```python
_LAST_APPLICATION_RESULT: object | None = None
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_aggregation_fixture`

**Exact signature**

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

Private `test` helper for aggregation fixture; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[tuple[object, ...], object, object, object, object, BessPlanningFeatureParcelAggregationResult]`.
- Every observed return expression is reproduced without truncation:
```python
(inputs, coded, config, policy, application, result)
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

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_result_schema_two_remains_accepted` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_filenames_are_casefold_unique` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_aggregation_fixture`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_rejects_nonportable_filename` via `_aggregation_fixture`.

**Complete source-ordered implementation**

```python
def _aggregation_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    object,
    BessPlanningFeatureParcelAggregationResult,
]:
    global _LAST_SOURCE_PARCELS, _LAST_APPLICATION_RESULT
    inputs, coded, config, policy, application = _application_fixture()
    result = aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    _LAST_SOURCE_PARCELS = inputs[1]
    _LAST_APPLICATION_RESULT = application
    return inputs, coded, config, policy, application, result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `load_bess_planning_feature_parcel_aggregation_artifacts`

**Exact signature**

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

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
_load_legacy_local_aggregation_artifacts(manifest_path, parcels_path, relation_assessments_path)

_load_aggregation_artifacts(manifest_path, parcels_path, relation_assessments_path, source_parcels, application_result)

_load_legacy_local_aggregation_artifacts(manifest_path, parcels_path, relation_assessments_path)
```

**Validation and exceptions**

- Guard with a raise path: `not legacy_synthetic or 'unknown feature' not in str(error)`.
- Explicit raise expressions: `re-raise`.

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

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `load_bess_planning_feature_parcel_aggregation_artifacts`.

**Complete source-ordered implementation**

```python
def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame | None = None,
    application_result: object | None = None,
) -> BessPlanningFeatureParcelAggregationResult:
    """Test adapter supplying the newly mandatory exact upstream envelopes."""

    legacy_synthetic = source_parcels is None or application_result is None
    if source_parcels is None or application_result is None:
        source_parcels = _LAST_SOURCE_PARCELS
        application_result = _LAST_APPLICATION_RESULT
    if source_parcels is None or application_result is None:
        return _load_legacy_local_aggregation_artifacts(
            manifest_path, parcels_path, relation_assessments_path
        )
    assert source_parcels is not None
    assert application_result is not None
    try:
        return _load_aggregation_artifacts(
            manifest_path,
            parcels_path,
            relation_assessments_path,
            source_parcels,
            application_result,
        )
    except BessPlanningFeatureParcelAggregationError as error:
        if not legacy_synthetic or "unknown feature" not in str(error):
            raise
        return _load_legacy_local_aggregation_artifacts(
            manifest_path, parcels_path, relation_assessments_path
        )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_load_legacy_local_aggregation_artifacts`

**Exact signature**

```python
def _load_legacy_local_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Exercise pre-2B.5 local-only assertions for retained synthetic fixtures.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: `Path(manifest_path).read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_load_legacy_local_aggregation_artifacts`.

**Complete source-ordered implementation**

```python
def _load_legacy_local_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
    """Exercise pre-2B.5 local-only assertions for retained synthetic fixtures."""

    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    payload = json.loads(
        Path(manifest_path).read_text(encoding="utf-8"),
        object_pairs_hook=module._unique_json_object,
    )
    manifest = BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(
        payload
    )
    records = {record.artifact_role: record for record in manifest.artifacts}
    parcels = module._read_verified_artifact(Path(parcels_path), records["PARCELS"])
    relations = module._read_verified_artifact(
        Path(relation_assessments_path), records["RELATION_ASSESSMENTS"]
    )
    result = BessPlanningFeatureParcelAggregationResult(
        **{field: getattr(manifest, field) for field in module.RESULT_SCALAR_FIELDS},
        parcels=parcels,
        relation_assessments=relations,
    )
    module._validate_result_envelope(result)
    return result
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_build_from_relations`

**Exact signature**

```python
def _build_from_relations(
    relations: pd.DataFrame,
    *,
    parcel_ids: tuple[str, ...] = ("PARCEL-1", "PARCEL-2"),
    canonicalize_application_dtypes: bool = True,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Constructs from relations; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._build_result(parcels, application)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `relations.loc[surface_mask, 'intersection_area_m2'].astype`, `relations['geometry_kind'].eq`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `relations.index`, `relations.loc[surface_mask, 'parcel_share_pct']`, `relations['bess_cnig_policy_profile']`, `relations['bess_cnig_policy_result_sha256']`, `relations['bess_cnig_policy_sha256']`, `relations['parcel_metric_area_m2']`, `relations[column]`.
- Input mutation: `relations.index`, `relations.loc[surface_mask, 'parcel_share_pct']`, `relations['bess_cnig_policy_profile']`, `relations['bess_cnig_policy_result_sha256']`, `relations['bess_cnig_policy_sha256']`, `relations['parcel_metric_area_m2']`, `relations[column]`.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_duplicate_selected_pair_result` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_invalid_lower_feature_id_result` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_cross_parcel_priority_conflict_result` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_exact_relations_select_configured_max_priority_and_lowest_confidence` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_policy_unknown_is_exact_but_unresolved_controlling_overrides` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_positive_relation_type_controls_without_threshold` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_boundary_only_relations_are_contextual` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_touch_relation_remains_context_beside_a_controlling_relation` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_is_retained_without_a_decision` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_inherited_application_relation_domain_is_validated_locally` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unresolved_relation_cannot_contain_a_decision` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_relation_suffix_dtype_is_validated_locally` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_status_and_priority_mapping_is_one_to_one_at_every_level` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_parcel_feature_identity_is_rejected_for_every_role` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_relation_parcel_id_is_rejected` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_priority_cannot_map_to_two_statuses` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_status_cannot_map_to_two_priorities` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_complete_five_status_policy_mapping_is_globally_valid` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_noncanonical_feature_ids_are_rejected` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_current_gpu_feature_id_is_canonical` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_build_from_relations`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_build_from_relations`.

**Complete source-ordered implementation**

```python
def _build_from_relations(
    relations: pd.DataFrame,
    *,
    parcel_ids: tuple[str, ...] = ("PARCEL-1", "PARCEL-2"),
    canonicalize_application_dtypes: bool = True,
) -> BessPlanningFeatureParcelAggregationResult:
    global _LAST_SOURCE_PARCELS, _LAST_APPLICATION_RESULT
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, application = _application_fixture()
    parcels = gpd.GeoDataFrame(
        {"parcel_id": list(parcel_ids), "prior": range(len(parcel_ids))},
        geometry=[
            Polygon(
                [
                    (i * 101, 0),
                    (i * 101 + 100, 0),
                    (i * 101 + 100, 40),
                    (i * 101, 40),
                ]
            )
            for i in range(len(parcel_ids))
        ],
        crs="EPSG:2154",
        index=pd.Index(range(10, 10 + len(parcel_ids)), name="parcel_row"),
    )
    relations = relations.reset_index(drop=True)
    relations["parcel_metric_area_m2"] = 4000.0
    surface_mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface_mask, "parcel_share_pct"] = (
        100.0
        * relations.loc[surface_mask, "intersection_area_m2"].astype("float64")
        / 4000.0
    )
    relations["bess_cnig_policy_profile"] = application.policy_profile
    relations["bess_cnig_policy_sha256"] = application.policy_sha256
    relations["bess_cnig_policy_result_sha256"] = (
        application.policy_complete_result_content_sha256
    )
    if canonicalize_application_dtypes:
        suffix = POLICY_COLUMNS
        relations = relations.loc[:, relation_columns(suffix)]
        for column, dtype in zip(
            relation_columns(suffix),
            relation_dtypes(tuple(POLICY_SUFFIX_DTYPES[column] for column in suffix)),
            strict=True,
        ):
            relations[column] = pd.Series(
                relations[column].tolist(), index=relations.index, dtype=dtype
            )
        relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    application = replace(application, relations=relations)
    application = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )._result_with_hashes(application)
    _LAST_SOURCE_PARCELS = parcels
    _LAST_APPLICATION_RESULT = application
    return module._build_result(parcels, application)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_relation`

**Exact signature**

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

Private `test` helper for relation; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
row
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `application.relations.loc[application.relations['geometry_kind'].eq('LINE')].iloc[0].to_dict`, `application.relations.loc[application.relations['geometry_kind'].eq('SURFACE')].iloc[0].to_dict`, `application.relations['geometry_kind'].eq`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `row`, `row['feature_area_m2']`, `row['intersection_length_m']`, `row['parcel_metric_area_m2']`, `row['source_line_length_m']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_duplicate_selected_pair_result` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_invalid_lower_feature_id_result` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_cross_parcel_priority_conflict_result` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_exact_relations_select_configured_max_priority_and_lowest_confidence` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_policy_unknown_is_exact_but_unresolved_controlling_overrides` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_positive_relation_type_controls_without_threshold` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_boundary_only_relations_are_contextual` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_touch_relation_remains_context_beside_a_controlling_relation` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_is_retained_without_a_decision` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unresolved_relation_cannot_contain_a_decision` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_relation_suffix_dtype_is_validated_locally` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_relation_parcel_id_is_rejected` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_priority_cannot_map_to_two_statuses` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_status_cannot_map_to_two_priorities` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_complete_five_status_policy_mapping_is_globally_valid` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_noncanonical_feature_ids_are_rejected` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_current_gpu_feature_id_is_canonical` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_relation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_relation`.

**Complete source-ordered implementation**

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
    _, _, _, _, application = _application_fixture()
    if relation_type == "LENGTH_OVERLAP":
        row = (
            application.relations.loc[application.relations["geometry_kind"].eq("LINE")]
            .iloc[0]
            .to_dict()
        )
    else:
        row = (
            application.relations.loc[
                application.relations["geometry_kind"].eq("SURFACE")
            ]
            .iloc[0]
            .to_dict()
        )
    row.update(
        parcel_id=parcel_id,
        planning_feature_id=feature_id,
        relation_type=relation_type,
        official_code_status=(
            "UNKNOWN_CODE_PAIR"
            if application_status == "UNRESOLVED_CODE_PAIR"
            else "RESOLVED_OFFICIAL"
        ),
        bess_cnig_policy_application_status=application_status,
        bess_cnig_precheck_status=status,
        bess_cnig_precheck_confidence=confidence,
        bess_cnig_status_priority=priority,
        bess_cnig_rationale=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_rationale"]
        ),
        bess_cnig_required_human_action=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_required_human_action"]
        ),
        bess_cnig_limitations=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_limitations"]
        ),
    )
    if application_status == "UNRESOLVED_CODE_PAIR":
        row.update(
            official_code_label=None,
            official_legal_reference=None,
            official_regulation_reference=None,
            official_code_source_url=None,
        )
    if relation_type == "AREA_OVERLAP":
        row["parcel_metric_area_m2"] = max(float(row["parcel_metric_area_m2"]), area)
        row["feature_area_m2"] = max(float(row["feature_area_m2"]), area)
        row.update(
            intersection_area_m2=area,
            parcel_share_pct=100.0 * area / float(row["parcel_metric_area_m2"]),
            feature_share_pct=100.0 * area / float(row["feature_area_m2"]),
        )
    elif relation_type == "LENGTH_OVERLAP":
        row["source_line_length_m"] = max(float(row["source_line_length_m"]), area)
        row["intersection_length_m"] = area
    elif relation_type == "TOUCH_ONLY":
        row.update(
            intersection_area_m2=0.0,
            parcel_share_pct=0.0,
            feature_share_pct=0.0,
        )
    elif relation_type in {"INSIDE", "BOUNDARY_TOUCH"}:
        row.update(
            geometry_kind="POINT",
            feature_area_m2=None,
            source_line_length_m=None,
            intersection_area_m2=None,
            intersection_length_m=None,
            parcel_share_pct=None,
            feature_share_pct=None,
            point_member_count=1,
            point_members_inside_count=1 if relation_type == "INSIDE" else 0,
            point_members_boundary_count=(0 if relation_type == "INSIDE" else 1),
        )
    return row
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_artifacts`

**Exact signature**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureParcelAggregationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

**Purpose**

Serializes artifacts; exact branches, calls, and return construction are reproduced below.

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

- Network I/O: none.
- Filesystem read: `path.read_bytes`.
- Filesystem write: `frame.to_parquet`, `manifest_path.write_text`.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: `paths[role]`, `records`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_filenames_are_casefold_unique` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_write_artifacts`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_rejects_nonportable_filename` via `_write_artifacts`.

**Complete source-ordered implementation**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureParcelAggregationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
    frames = {
        "PARCELS": (result.parcels, "parcels.parquet", True),
        "RELATION_ASSESSMENTS": (
            result.relation_assessments,
            "relations.parquet",
            False,
        ),
    }
    paths: dict[str, Path] = {}
    records: list[dict[str, object]] = []
    for role, (frame, filename, geospatial) in frames.items():
        path = tmp_path / filename
        frame.to_parquet(path, index=True)
        paths[role] = path
        signature = deterministic_frame_schema_signature(frame)
        payload = path.read_bytes()
        records.append(
            {
                "artifact_role": role,
                "filename": filename,
                "row_count": len(frame),
                "size_bytes": len(payload),
                "sha256": sha256(payload).hexdigest(),
                "frame_schema_signature": signature,
                "geospatial": geospatial,
                "crs": signature.get("crs"),
            }
        )
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeatureParcelAggregationResult)
        if field.name not in {"parcels", "relation_assessments"}
    )
    manifest = {
        "schema_version": 1,
        "artifact_kind": "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT",
        **{name: getattr(result, name) for name in scalar_names},
        "artifacts": records,
    }
    BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(manifest)
    manifest_path = tmp_path / "aggregation.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest_path, paths, manifest
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_rehash_coordinated_result`

**Exact signature**

```python
def _rehash_coordinated_result(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Private `test` helper for rehash coordinated result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(updated)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `module._frame_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_duplicate_selected_pair_result` via `_rehash_coordinated_result`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_invalid_lower_feature_id_result` via `_rehash_coordinated_result`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_cross_parcel_priority_conflict_result` via `_rehash_coordinated_result`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_rehash_coordinated_result`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_coherent_parcel_area_mutation` via `_rehash_coordinated_result`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `_rehash_coordinated_result`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_rehash_coordinated_result`.

**Complete source-ordered implementation**

```python
def _rehash_coordinated_result(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    source_parcels = result.parcels.drop(columns=list(PARCEL_COLUMNS))
    source_relations = result.relation_assessments.drop(columns=list(RELATION_COLUMNS))
    updated = replace(
        result,
        source_parcels_content_sha256=module._frame_sha256(
            source_parcels,
            "landscout.bess_cnig_parcel_aggregation.source_parcels",
        ),
        source_application_relations_content_sha256=module._frame_sha256(
            source_relations,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
    )
    return module._result_with_hashes(updated)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_duplicate_selected_pair_result`

**Exact signature**

```python
def _duplicate_selected_pair_result() -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Private `test` helper for duplicate selected pair result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
_rehash_coordinated_result(replace(result, parcels=parcels, relation_assessments=relations))
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
- In-memory mutation: `parcels.loc[parcels.index[0], 'bess_cnig_selected_feature_ids_json']`, `relations.loc[relations.index[1], 'planning_feature_id']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_duplicate_selected_pair_result`.

**Complete source-ordered implementation**

```python
def _duplicate_selected_pair_result() -> BessPlanningFeatureParcelAggregationResult:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A"),
                _relation(feature_id="B"),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[1], "planning_feature_id"] = "A"
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = '["A"]'
    return _rehash_coordinated_result(
        replace(result, parcels=parcels, relation_assessments=relations)
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_invalid_lower_feature_id_result`

**Exact signature**

```python
def _invalid_lower_feature_id_result() -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Private `test` helper for invalid lower feature id result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
_rehash_coordinated_result(replace(result, relation_assessments=relations))
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
- In-memory mutation: `relations.loc[relations.index[0], 'planning_feature_id']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_invalid_lower_feature_id_result`.

**Complete source-ordered implementation**

```python
def _invalid_lower_feature_id_result() -> BessPlanningFeatureParcelAggregationResult:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "/tmp/feature"
    return _rehash_coordinated_result(replace(result, relation_assessments=relations))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_cross_parcel_priority_conflict_result`

**Exact signature**

```python
def _cross_parcel_priority_conflict_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

**Purpose**

Private `test` helper for cross parcel priority conflict result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
_rehash_coordinated_result(replace(result, parcels=parcels, relation_assessments=relations))
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
- In-memory mutation: `parcels.loc[parcels['parcel_id'].eq('PARCEL-2'), 'bess_cnig_parcel_status_priority']`, `relations.loc[mask, 'bess_cnig_resulting_parcel_status_priority']`, `relations.loc[mask, 'bess_cnig_status_priority']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_cross_parcel_priority_conflict_result`.

**Complete source-ordered implementation**

```python
def _cross_parcel_priority_conflict_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    parcel_id="PARCEL-1",
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    parcel_id="PARCEL-2",
                    feature_id="B",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=30,
                ),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    mask = relations["parcel_id"].eq("PARCEL-2")
    relations.loc[mask, "bess_cnig_status_priority"] = 50
    relations.loc[mask, "bess_cnig_resulting_parcel_status_priority"] = 50
    parcels = result.parcels.copy(deep=True)
    parcels.loc[
        parcels["parcel_id"].eq("PARCEL-2"), "bess_cnig_parcel_status_priority"
    ] = 50
    return _rehash_coordinated_result(
        replace(result, parcels=parcels, relation_assessments=relations)
    )
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_surface_touch_semantic_corruption_result`

**Exact signature**

```python
def _surface_touch_semantic_corruption_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

**Purpose**

Private `test` helper for surface touch semantic corruption result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
None

module._build_result(inputs[1], changed_application)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `_surface_touch_with_positive_area`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `module.validate_bess_application_relation_frame`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_surface_touch_semantic_corruption_result`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `_surface_touch_semantic_corruption_result`.

**Complete source-ordered implementation**

```python
def _surface_touch_semantic_corruption_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
    inputs, _, _, _, application = _application_fixture()
    changed_application = _surface_touch_with_positive_area(application)
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    original = module.validate_bess_application_relation_frame

    def bypass(*args: object, **kwargs: object) -> None:
        return None

    module.validate_bess_application_relation_frame = bypass
    try:
        return module._build_result(inputs[1], changed_application)
    finally:
        module.validate_bess_application_relation_frame = original
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_surface_touch_semantic_corruption_result.bypass`

**Exact signature**

```python
def bypass(*args: object, **kwargs: object) -> None:
```

**Purpose**

Private `test` helper for bypass; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def bypass(*args: object, **kwargs: object) -> None:
        return None
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_exact_relations_select_configured_max_priority_and_lowest_confidence`

**Purpose**

Exercises `exact relations select configured max priority and lowest confidence`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
relations = pd.DataFrame(
        [
            _relation(
                feature_id="LOW",
                priority=10,
                status="CONTEXT_REVIEW_REQUIRED",
                area=1000.0,
            ),
            _relation(
                feature_id="HIGH-A",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="HIGH",
            ),
            _relation(
                feature_id="HIGH-B",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="LOW",
            ),
        ]
    )
result = _build_from_relations(relations)
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parcel.bess_cnig_parcel_aggregation_status == "AGGREGATED_EXACT_POLICY"
assert parcel.bess_cnig_parcel_precheck_status == "LIKELY_MATERIAL_CONSTRAINT"
assert parcel.bess_cnig_parcel_precheck_confidence == "LOW"
assert parcel.bess_cnig_parcel_status_priority == 50
assert parcel.bess_cnig_selected_feature_ids_json == '["HIGH-A","HIGH-B"]'
assert parcel.bess_cnig_distinct_exact_status_count == 2
assert bool(parcel.bess_cnig_multiple_exact_statuses) is True
assert parcel.bess_cnig_selected_relation_count == 2
assert parcel.bess_cnig_lower_priority_controlling_relation_count == 1
assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "LOWER_PRIORITY_CONTROLLING",
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]
```

**Regression protected**

Locks `exact relations select configured max priority and lowest confidence` through the exact asserted conditions: `parcel.bess_cnig_parcel_aggregation_status == 'AGGREGATED_EXACT_POLICY'`; `parcel.bess_cnig_parcel_precheck_status == 'LIKELY_MATERIAL_CONSTRAINT'`; `parcel.bess_cnig_parcel_precheck_confidence == 'LOW'`; `parcel.bess_cnig_parcel_status_priority == 50`; plus 6 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_exact_relations_select_configured_max_priority_and_lowest_confidence() -> None:
    relations = pd.DataFrame(
        [
            _relation(
                feature_id="LOW",
                priority=10,
                status="CONTEXT_REVIEW_REQUIRED",
                area=1000.0,
            ),
            _relation(
                feature_id="HIGH-A",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="HIGH",
            ),
            _relation(
                feature_id="HIGH-B",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="LOW",
            ),
        ]
    )
    result = _build_from_relations(relations)
    parcel = result.parcels.iloc[0]
    assert parcel.bess_cnig_parcel_aggregation_status == "AGGREGATED_EXACT_POLICY"
    assert parcel.bess_cnig_parcel_precheck_status == "LIKELY_MATERIAL_CONSTRAINT"
    assert parcel.bess_cnig_parcel_precheck_confidence == "LOW"
    assert parcel.bess_cnig_parcel_status_priority == 50
    assert parcel.bess_cnig_selected_feature_ids_json == '["HIGH-A","HIGH-B"]'
    assert parcel.bess_cnig_distinct_exact_status_count == 2
    assert bool(parcel.bess_cnig_multiple_exact_statuses) is True
    assert parcel.bess_cnig_selected_relation_count == 2
    assert parcel.bess_cnig_lower_priority_controlling_relation_count == 1
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "LOWER_PRIORITY_CONTROLLING",
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]
```

### `test_policy_unknown_is_exact_but_unresolved_controlling_overrides`

**Purpose**

Exercises `policy unknown is exact but unresolved controlling overrides`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
exact_unknown = _build_from_relations(
        pd.DataFrame([_relation(status="UNKNOWN", confidence="LOW", priority=40)])
    )
unresolved = _relation(
        feature_id="UNRESOLVED",
        application_status="UNRESOLVED_CODE_PAIR",
        status=None,
        confidence=None,
        priority=None,
    )
mixed = _build_from_relations(pd.DataFrame([_relation(), unresolved]))
parcel = mixed.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert exact_unknown.parcels.iloc[0].bess_cnig_parcel_precheck_status == "UNKNOWN"
assert (
        parcel.bess_cnig_parcel_aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR"
    )
assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
assert pd.isna(parcel.bess_cnig_parcel_precheck_confidence)
assert pd.isna(parcel.bess_cnig_parcel_status_priority)
assert parcel.bess_cnig_unresolved_feature_ids_json == '["UNRESOLVED"]'
assert mixed.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
    ]
```

**Regression protected**

Locks `policy unknown is exact but unresolved controlling overrides` through the exact asserted conditions: `exact_unknown.parcels.iloc[0].bess_cnig_parcel_precheck_status == 'UNKNOWN'`; `parcel.bess_cnig_parcel_aggregation_status == 'UNRESOLVED_CONTROLLING_CODE_PAIR'`; `pd.isna(parcel.bess_cnig_parcel_precheck_status)`; `pd.isna(parcel.bess_cnig_parcel_precheck_confidence)`; plus 3 additional reproduced assertion(s).

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_unknown_is_exact_but_unresolved_controlling_overrides() -> None:
    exact_unknown = _build_from_relations(
        pd.DataFrame([_relation(status="UNKNOWN", confidence="LOW", priority=40)])
    )
    assert exact_unknown.parcels.iloc[0].bess_cnig_parcel_precheck_status == "UNKNOWN"
    unresolved = _relation(
        feature_id="UNRESOLVED",
        application_status="UNRESOLVED_CODE_PAIR",
        status=None,
        confidence=None,
        priority=None,
    )
    mixed = _build_from_relations(pd.DataFrame([_relation(), unresolved]))
    parcel = mixed.parcels.iloc[0]
    assert (
        parcel.bess_cnig_parcel_aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR"
    )
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert pd.isna(parcel.bess_cnig_parcel_precheck_confidence)
    assert pd.isna(parcel.bess_cnig_parcel_status_priority)
    assert parcel.bess_cnig_unresolved_feature_ids_json == '["UNRESOLVED"]'
    assert mixed.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
    ]
```

### `test_every_positive_relation_type_controls_without_threshold`

**Purpose**

Exercises `every positive relation type controls without threshold`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `relation_type`.

**Setup**

```python
result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type, area=1e-15)])
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.iloc[0].bess_cnig_controlling_relation_count == 1
assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "SELECTED_CONTROLLING"
    )
```

**Regression protected**

Locks `every positive relation type controls without threshold` through the exact asserted conditions: `result.parcels.iloc[0].bess_cnig_controlling_relation_count == 1`; `result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role == 'SELECTED_CONTROLLING'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_every_positive_relation_type_controls_without_threshold(
    relation_type: str,
) -> None:
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type, area=1e-15)])
    )
    assert result.parcels.iloc[0].bess_cnig_controlling_relation_count == 1
    assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "SELECTED_CONTROLLING"
    )
```

### `test_boundary_only_relations_are_contextual`

**Purpose**

Exercises `boundary only relations are contextual`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `relation_type`.

**Setup**

```python
result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type)])
    )
parcel = result.parcels.iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parcel.bess_cnig_parcel_aggregation_status == "TOUCH_ONLY_RELATIONS_ONLY"
assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
assert parcel.bess_cnig_touch_only_feature_ids_json == '["F-1"]'
assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "TOUCH_ONLY_CONTEXT"
    )
```

**Regression protected**

Locks `boundary only relations are contextual` through the exact asserted conditions: `parcel.bess_cnig_parcel_aggregation_status == 'TOUCH_ONLY_RELATIONS_ONLY'`; `pd.isna(parcel.bess_cnig_parcel_precheck_status)`; `parcel.bess_cnig_touch_only_feature_ids_json == '["F-1"]'`; `result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role == 'TOUCH_ONLY_CONTEXT'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_boundary_only_relations_are_contextual(relation_type: str) -> None:
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type)])
    )
    parcel = result.parcels.iloc[0]
    assert parcel.bess_cnig_parcel_aggregation_status == "TOUCH_ONLY_RELATIONS_ONLY"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert parcel.bess_cnig_touch_only_feature_ids_json == '["F-1"]'
    assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "TOUCH_ONLY_CONTEXT"
    )
```

### `test_touch_relation_remains_context_beside_a_controlling_relation`

**Purpose**

Exercises `touch relation remains context beside a controlling relation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="EXACT"),
                _relation(
                    feature_id="TOUCH",
                    relation_type="TOUCH_ONLY",
                    priority=50,
                    status="LIKELY_MATERIAL_CONSTRAINT",
                ),
            ]
        )
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.iloc[0].bess_cnig_parcel_precheck_status == (
        "MATERIAL_REVIEW_REQUIRED"
    )
assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    ]
```

**Regression protected**

Locks `touch relation remains context beside a controlling relation` through the exact asserted conditions: `result.parcels.iloc[0].bess_cnig_parcel_precheck_status == 'MATERIAL_REVIEW_REQUIRED'`; `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist() == ['SELECTED_CONTROLLING', 'TOUCH_ONLY_CONTEXT']`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_touch_relation_remains_context_beside_a_controlling_relation() -> None:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="EXACT"),
                _relation(
                    feature_id="TOUCH",
                    relation_type="TOUCH_ONLY",
                    priority=50,
                    status="LIKELY_MATERIAL_CONSTRAINT",
                ),
            ]
        )
    )
    assert result.parcels.iloc[0].bess_cnig_parcel_precheck_status == (
        "MATERIAL_REVIEW_REQUIRED"
    )
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    ]
```

### `test_no_relation_parcel_is_retained_without_a_decision`

**Purpose**

Exercises `no relation parcel is retained without a decision`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _build_from_relations(pd.DataFrame([_relation()]))
parcel = result.parcels.iloc[1]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert parcel.bess_cnig_parcel_aggregation_status == "NO_PLANNING_FEATURE_RELATION"
assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
assert bool(parcel.bess_cnig_formal_review_required) is True
```

**Regression protected**

Locks `no relation parcel is retained without a decision` through the exact asserted conditions: `parcel.bess_cnig_parcel_aggregation_status == 'NO_PLANNING_FEATURE_RELATION'`; `pd.isna(parcel.bess_cnig_parcel_precheck_status)`; `bool(parcel.bess_cnig_formal_review_required) is True`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_no_relation_parcel_is_retained_without_a_decision() -> None:
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcel = result.parcels.iloc[1]
    assert parcel.bess_cnig_parcel_aggregation_status == "NO_PLANNING_FEATURE_RELATION"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert bool(parcel.bess_cnig_formal_review_required) is True
```

### `test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`

**Purpose**

Exercises `parcel and relation prefixes order and inputs are preserved`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application = _application_fixture()
parcels_copy = inputs[1].copy(deep=True)
relations_copy = application.relations.copy(deep=True)
assert_geodataframe_equal(inputs[1], parcels_copy)
assert_frame_equal(application.relations, relations_copy)
assert_geodataframe_equal(
        inputs[1], result.parcels.loc[:, inputs[1].columns], check_dtype=True
    )
assert_frame_equal(
        application.relations,
        result.relation_assessments.loc[:, application.relations.columns],
        check_dtype=True,
    )
```

**Action**

```python
result = aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
```

**Expected result**

```python
assert tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) == PARCEL_COLUMNS
assert (
        tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])
        == RELATION_COLUMNS
    )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_parcel_and_relation_prefixes_order_and_inputs_are_preserved() -> None:
    inputs, coded, config, policy, application = _application_fixture()
    parcels_copy = inputs[1].copy(deep=True)
    relations_copy = application.relations.copy(deep=True)
    result = aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    assert_geodataframe_equal(inputs[1], parcels_copy)
    assert_frame_equal(application.relations, relations_copy)
    assert_geodataframe_equal(
        inputs[1], result.parcels.loc[:, inputs[1].columns], check_dtype=True
    )
    assert_frame_equal(
        application.relations,
        result.relation_assessments.loc[:, application.relations.columns],
        check_dtype=True,
    )
    assert tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) == PARCEL_COLUMNS
    assert (
        tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])
        == RELATION_COLUMNS
    )
```

### `test_local_corruption_fast_fails_before_heavy_validation`

**Purpose**

Exercises `local corruption fast fails before heavy validation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application, result = _aggregation_fixture()
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
parcels = result.parcels.copy(deep=True)
parcels.loc[parcels.index[0], "bess_cnig_selected_relation_count"] = 999
corrupted = module._result_with_hashes(replace(result, parcels=parcels))
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs, coded, config, policy, application, corrupted
        )
assert calls == 0
```

**Regression protected**

Locks `local corruption fast fails before heavy validation`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_local_corruption_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_relation_count"] = 999
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs, coded, config, policy, application, corrupted
        )
    assert calls == 0
```

### `test_local_corruption_fast_fails_before_heavy_validation.counted`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_local_cross_table_corruption_is_rejected`

**Purpose**

Exercises `coordinated local cross table corruption is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `frame_name`, `value`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
frame = getattr(result, frame_name).copy(deep=True)
frame.loc[frame.index[0], column] = value
corrupted = module._result_with_hashes(replace(result, **{frame_name: frame}))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)
```

**Regression protected**

Locks `coordinated local cross table corruption is rejected`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_coordinated_local_cross_table_corruption_is_rejected(
    frame_name: str,
    column: str,
    value: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
    frame = getattr(result, frame_name).copy(deep=True)
    frame.loc[frame.index[0], column] = value
    corrupted = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)
```

### `test_invalid_output_dtype_and_non_2d_parcel_fail_locally`

**Purpose**

Exercises `invalid output dtype and non 2d parcel fail locally`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
parcels = result.parcels.copy(deep=True)
parcels["bess_cnig_selected_relation_count"] = parcels[
        "bess_cnig_selected_relation_count"
    ].astype("object")
relations = result.relation_assessments.copy(deep=True)
relations["bess_cnig_selected_for_parcel_status"] = relations[
        "bess_cnig_selected_for_parcel_status"
    ].astype("object")
parcels = result.parcels.copy(deep=True)
geometry = parcels.geometry.iloc[0]
parcels.at[parcels.index[0], parcels.geometry.name] = Polygon(
        [(x, y, 5) for x, y in geometry.exterior.coords]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, parcels=parcels))
        )
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, relation_assessments=relations))
        )
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="2D"):
        module._validate_result_envelope(replace(result, parcels=parcels))
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_invalid_output_dtype_and_non_2d_parcel_fail_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
    parcels = result.parcels.copy(deep=True)
    parcels["bess_cnig_selected_relation_count"] = parcels[
        "bess_cnig_selected_relation_count"
    ].astype("object")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, parcels=parcels))
        )
    relations = result.relation_assessments.copy(deep=True)
    relations["bess_cnig_selected_for_parcel_status"] = relations[
        "bess_cnig_selected_for_parcel_status"
    ].astype("object")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, relation_assessments=relations))
        )
    parcels = result.parcels.copy(deep=True)
    geometry = parcels.geometry.iloc[0]
    parcels.at[parcels.index[0], parcels.geometry.name] = Polygon(
        [(x, y, 5) for x, y in geometry.exterior.coords]
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="2D"):
        module._validate_result_envelope(replace(result, parcels=parcels))
```

### `test_every_inherited_application_relation_domain_is_validated_locally`

**Purpose**

Exercises `every inherited application relation domain is validated locally`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `relations`.

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
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(relations)
```

**Regression protected**

Locks `every inherited application relation domain is validated locally`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(relations)
```

### `test_unresolved_relation_cannot_contain_a_decision`

**Purpose**

Exercises `unresolved relation cannot contain a decision`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
row = _relation(
        application_status="UNRESOLVED_CODE_PAIR",
        status="UNKNOWN",
        confidence="LOW",
        priority=40,
    )
row["official_code_status"] = "UNKNOWN_CODE_PAIR"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))
```

**Regression protected**

Locks `unresolved relation cannot contain a decision`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unresolved_relation_cannot_contain_a_decision() -> None:
    row = _relation(
        application_status="UNRESOLVED_CODE_PAIR",
        status="UNKNOWN",
        confidence="LOW",
        priority=40,
    )
    row["official_code_status"] = "UNKNOWN_CODE_PAIR"
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))
```

### `test_all_application_identity_scope_and_boundary_fields_are_intrinsic`

**Purpose**

Exercises `all application identity scope and boundary fields are intrinsic`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `value`.

**Setup**

```python
row = _relation(relation_type="TOUCH_ONLY")
row[column] = value
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))
```

**Regression protected**

Locks `all application identity scope and boundary fields are intrinsic`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
    row = _relation(relation_type="TOUCH_ONLY")
    row[column] = value
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))
```

### `test_application_relation_suffix_dtype_is_validated_locally`

**Purpose**

Exercises `application relation suffix dtype is validated locally`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
relations = pd.DataFrame([_relation()])
relations["bess_cnig_precheck_status"] = relations[
        "bess_cnig_precheck_status"
    ].astype("category")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        _build_from_relations(relations, canonicalize_application_dtypes=False)
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_relation_suffix_dtype_is_validated_locally() -> None:
    relations = pd.DataFrame([_relation()])
    relations["bess_cnig_precheck_status"] = relations[
        "bess_cnig_precheck_status"
    ].astype("category")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        _build_from_relations(relations, canonicalize_application_dtypes=False)
```

### `test_status_and_priority_mapping_is_one_to_one_at_every_level`

**Purpose**

Exercises `status and priority mapping is one to one at every level`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `relations`.

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
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority"):
        _build_from_relations(relations)
```

**Regression protected**

Locks `status and priority mapping is one to one at every level`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority"):
        _build_from_relations(relations)
```

### `test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

**Purpose**

Exercises `valid repeated status and priority mapping selects every exact match`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=30),
                _relation(feature_id="B", priority=30),
            ]
        )
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.iloc[0].bess_cnig_selected_relation_count == 2
assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]
```

**Regression protected**

Locks `valid repeated status and priority mapping selects every exact match` through the exact asserted conditions: `result.parcels.iloc[0].bess_cnig_selected_relation_count == 2`; `result.relation_assessments['bess_cnig_parcel_relation_role'].tolist() == ['SELECTED_CONTROLLING', 'SELECTED_CONTROLLING']`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_valid_repeated_status_and_priority_mapping_selects_every_exact_match() -> None:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=30),
                _relation(feature_id="B", priority=30),
            ]
        )
    )
    assert result.parcels.iloc[0].bess_cnig_selected_relation_count == 2
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]
```

### `test_duplicate_parcel_feature_identity_is_rejected_for_every_role`

**Purpose**

Exercises `duplicate parcel feature identity is rejected for every role`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `relations`.

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
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="duplicate|unique"
    ):
        _build_from_relations(relations)
```

**Regression protected**

Locks `duplicate parcel feature identity is rejected for every role`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="duplicate|unique"
    ):
        _build_from_relations(relations)
```

### `test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`

**Purpose**

Exercises `invalid lower priority feature id is rejected independently of json role`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `feature_id`.

**Setup**

```python
relations = pd.DataFrame(
        [
            _relation(
                feature_id=feature_id,
                status="CONTEXT_REVIEW_REQUIRED",
                priority=10,
            ),
            _relation(feature_id="HIGH", priority=30),
        ]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)
```

**Regression protected**

Locks `invalid lower priority feature id is rejected independently of json role`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role(
    feature_id: object,
) -> None:
    relations = pd.DataFrame(
        [
            _relation(
                feature_id=feature_id,
                status="CONTEXT_REVIEW_REQUIRED",
                priority=10,
            ),
            _relation(feature_id="HIGH", priority=30),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)
```

### `test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`

**Purpose**

Exercises `invalid deferred feature id is rejected independently of json role`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `feature_id`.

**Setup**

```python
relations = pd.DataFrame(
        [
            _relation(feature_id=feature_id),
            _relation(
                feature_id="UNRESOLVED",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)
```

**Regression protected**

Locks `invalid deferred feature id is rejected independently of json role`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_deferred_feature_id_is_rejected_independently_of_json_role(
    feature_id: str,
) -> None:
    relations = pd.DataFrame(
        [
            _relation(feature_id=feature_id),
            _relation(
                feature_id="UNRESOLVED",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)
```

### `test_invalid_relation_parcel_id_is_rejected`

**Purpose**

Exercises `invalid relation parcel id is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `parcel_id`.

**Setup**

```python
relation = _relation()
relation["parcel_id"] = parcel_id
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel|identity"
    ):
        _build_from_relations(pd.DataFrame([relation]))
```

**Regression protected**

Locks `invalid relation parcel id is rejected`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
    relation = _relation()
    relation["parcel_id"] = parcel_id
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel|identity"
    ):
        _build_from_relations(pd.DataFrame([relation]))
```

### `test_unknown_relation_type_is_rejected_by_shared_relation_contract`

**Purpose**

Exercises `unknown relation type is rejected by shared relation contract`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="relation type"
    ):
        _build_from_relations(pd.DataFrame([_relation(relation_type="NEARBY")]))
```

**Regression protected**

Locks `unknown relation type is rejected by shared relation contract`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="relation type"
    ):
        _build_from_relations(pd.DataFrame([_relation(relation_type="NEARBY")]))
```

### `test_document_wide_same_priority_cannot_map_to_two_statuses`

**Purpose**

Exercises `document wide same priority cannot map to two statuses`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `context_type`.

**Setup**

```python
second_type = context_type or "AREA_OVERLAP"
relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                relation_type=second_type,
                status="MATERIAL_REVIEW_REQUIRED",
                priority=50,
            ),
        ]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)
```

**Regression protected**

Locks `document wide same priority cannot map to two statuses`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_document_wide_same_priority_cannot_map_to_two_statuses(
    context_type: str | None,
) -> None:
    second_type = context_type or "AREA_OVERLAP"
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                relation_type=second_type,
                status="MATERIAL_REVIEW_REQUIRED",
                priority=50,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)
```

### `test_document_wide_same_status_cannot_map_to_two_priorities`

**Purpose**

Exercises `document wide same status cannot map to two priorities`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=10,
            ),
        ]
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)
```

**Regression protected**

Locks `document wide same status cannot map to two priorities`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_document_wide_same_status_cannot_map_to_two_priorities() -> None:
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=10,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)
```

### `test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`

**Purpose**

Exercises `document wide repeated mapping and unresolved rows are valid`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
relations = pd.DataFrame(
        [
            _relation(parcel_id="PARCEL-1", feature_id="A", priority=30),
            _relation(parcel_id="PARCEL-2", feature_id="B", priority=30),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="U",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
result = _build_from_relations(relations)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.relation_assessments) == 3
```

**Regression protected**

Locks `document wide repeated mapping and unresolved rows are valid` through the exact asserted conditions: `len(result.relation_assessments) == 3`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_document_wide_repeated_mapping_and_unresolved_rows_are_valid() -> None:
    relations = pd.DataFrame(
        [
            _relation(parcel_id="PARCEL-1", feature_id="A", priority=30),
            _relation(parcel_id="PARCEL-2", feature_id="B", priority=30),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="U",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
    result = _build_from_relations(relations)
    assert len(result.relation_assessments) == 3
```

### `test_complete_five_status_policy_mapping_is_globally_valid`

**Purpose**

Exercises `complete five status policy mapping is globally valid`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
mapping = (
        ("LIKELY_MATERIAL_CONSTRAINT", 50, "HIGH"),
        ("UNKNOWN", 40, "LOW"),
        ("MATERIAL_REVIEW_REQUIRED", 30, "HIGH"),
        ("DESIGN_REVIEW_REQUIRED", 20, "MEDIUM"),
        ("CONTEXT_REVIEW_REQUIRED", 10, "HIGH"),
    )
relations = pd.DataFrame(
        [
            _relation(
                parcel_id=f"PARCEL-{position}",
                feature_id=f"FEATURE-{position}",
                status=status,
                priority=priority,
                confidence=confidence,
            )
            for position, (status, priority, confidence) in enumerate(mapping, start=1)
        ]
    )
result = _build_from_relations(
        relations,
        parcel_ids=tuple(f"PARCEL-{position}" for position in range(1, 6)),
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.relation_assessments) == 5
```

**Regression protected**

Locks `complete five status policy mapping is globally valid` through the exact asserted conditions: `len(result.relation_assessments) == 5`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_complete_five_status_policy_mapping_is_globally_valid() -> None:
    mapping = (
        ("LIKELY_MATERIAL_CONSTRAINT", 50, "HIGH"),
        ("UNKNOWN", 40, "LOW"),
        ("MATERIAL_REVIEW_REQUIRED", 30, "HIGH"),
        ("DESIGN_REVIEW_REQUIRED", 20, "MEDIUM"),
        ("CONTEXT_REVIEW_REQUIRED", 10, "HIGH"),
    )
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id=f"PARCEL-{position}",
                feature_id=f"FEATURE-{position}",
                status=status,
                priority=priority,
                confidence=confidence,
            )
            for position, (status, priority, confidence) in enumerate(mapping, start=1)
        ]
    )
    result = _build_from_relations(
        relations,
        parcel_ids=tuple(f"PARCEL-{position}" for position in range(1, 6)),
    )
    assert len(result.relation_assessments) == 5
```

### `test_selected_relation_role_requires_selected_status_and_priority`

**Purpose**

Exercises `selected relation role requires selected status and priority`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        )
    )
relations = result.relation_assessments.copy(deep=True)
relations.loc[relations.index[0], "bess_cnig_parcel_relation_role"] = (
        "SELECTED_CONTROLLING"
    )
relations.loc[relations.index[0], "bess_cnig_selected_for_parcel_status"] = True
corrupted = module._result_with_hashes(
        replace(result, relation_assessments=relations)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)
```

**Regression protected**

Locks `selected relation role requires selected status and priority`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_selected_relation_role_requires_selected_status_and_priority() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[0], "bess_cnig_parcel_relation_role"] = (
        "SELECTED_CONTROLLING"
    )
    relations.loc[relations.index[0], "bess_cnig_selected_for_parcel_status"] = True
    corrupted = module._result_with_hashes(
        replace(result, relation_assessments=relations)
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)
```

### `_validate_parcel_geometries`

**Exact signature**

```python
def _validate_parcel_geometries(geometries: list[object]) -> None:
```

**Purpose**

Rejects malformed or inconsistent parcel geometries; exact branches, calls, and return construction are reproduced below.

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

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_malformed_parcel_geometry_is_rejected_intrinsically` via `_validate_parcel_geometries`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_polygon_and_multipolygon_parcels_are_accepted` via `_validate_parcel_geometries`.

**Complete source-ordered implementation**

```python
def _validate_parcel_geometries(geometries: list[object]) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, application = _application_fixture()
    parcels = gpd.GeoDataFrame(
        {"parcel_id": [f"P-{index}" for index in range(len(geometries))]},
        geometry=geometries,
        crs="EPSG:2154",
    )
    result = module._build_result(
        parcels, replace(application, relations=application.relations.iloc[0:0])
    )
    module._validate_result_envelope(result)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_parcel_geometry_is_rejected_intrinsically`

**Purpose**

Exercises `malformed parcel geometry is rejected intrinsically`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

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
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _validate_parcel_geometries([geometry])
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _validate_parcel_geometries([geometry])
```

### `test_valid_polygon_and_multipolygon_parcels_are_accepted`

**Purpose**

Exercises `valid polygon and multipolygon parcels are accepted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
_validate_parcel_geometries([polygon, MultiPolygon([polygon])])
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

Locks `valid polygon and multipolygon parcels are accepted` by requiring the reproduced call path `Polygon`, `_validate_parcel_geometries`, `MultiPolygon` without an unasserted exception.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
    polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
    _validate_parcel_geometries([polygon, MultiPolygon([polygon])])
```

### `test_duplicate_output_columns_are_rejected_intrinsically`

**Purpose**

Exercises `duplicate output columns are rejected intrinsically`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `frame_name`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
_, _, _, _, _, result = _aggregation_fixture()
frame = getattr(result, frame_name)
duplicate = pd.concat([frame, frame.iloc[:, [0]]], axis=1)
if frame_name == "parcels":
        duplicate = gpd.GeoDataFrame(
            duplicate, geometry=frame.geometry.name, crs=frame.crs
        )
corrupted = replace(result, **{frame_name: duplicate})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="duplicate"):
        module._validate_result_envelope(corrupted)
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_duplicate_output_columns_are_rejected_intrinsically(frame_name: str) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    frame = getattr(result, frame_name)
    duplicate = pd.concat([frame, frame.iloc[:, [0]]], axis=1)
    if frame_name == "parcels":
        duplicate = gpd.GeoDataFrame(
            duplicate, geometry=frame.geometry.name, crs=frame.crs
        )
    corrupted = replace(result, **{frame_name: duplicate})
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="duplicate"):
        module._validate_result_envelope(corrupted)
```

### `test_only_application_result_schema_two_is_accepted`

**Purpose**

Exercises `only application result schema two is accepted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `version`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
_, _, _, _, _, result = _aggregation_fixture()
corrupted = module._result_with_hashes(
        replace(result, application_result_hash_schema_version=version)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="application.*schema"
    ):
        module._validate_result_envelope(corrupted)
```

**Regression protected**

Locks `only application result schema two is accepted`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_only_application_result_schema_two_is_accepted(version: int) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    corrupted = module._result_with_hashes(
        replace(result, application_result_hash_schema_version=version)
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="application.*schema"
    ):
        module._validate_result_envelope(corrupted)
```

### `test_application_result_schema_two_remains_accepted`

**Purpose**

Exercises `application result schema two remains accepted`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
_, _, _, _, _, result = _aggregation_fixture()
module._validate_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.application_result_hash_schema_version == 2
```

**Regression protected**

Locks `application result schema two remains accepted` through the exact asserted conditions: `result.application_result_hash_schema_version == 2`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_application_result_schema_two_remains_accepted() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    assert result.application_result_hash_schema_version == 2
    module._validate_result_envelope(result)
```

### `test_noncanonical_feature_ids_are_rejected`

**Purpose**

Exercises `noncanonical feature ids are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `feature_id`.

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
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID"):
        _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
```

**Regression protected**

Locks `noncanonical feature ids are rejected`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID"):
        _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
```

### `test_current_gpu_feature_id_is_canonical`

**Purpose**

Exercises `current gpu feature id is canonical`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
feature_id = "GPU:DOC:prescription_surface:FEATURE-01"
result = _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == (
        f'["{feature_id}"]'
    )
```

**Regression protected**

Locks `current gpu feature id is canonical` through the exact asserted conditions: `result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == f'["{feature_id}"]'`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_current_gpu_feature_id_is_canonical() -> None:
    feature_id = "GPU:DOC:prescription_surface:FEATURE-01"
    result = _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
    assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == (
        f'["{feature_id}"]'
    )
```

### `test_authorized_status_artifact_fails_local_verified_byte_loading`

**Purpose**

Exercises `authorized status artifact fails local verified byte loading`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(pd.DataFrame([_relation()]))
parcels = result.parcels.copy(deep=True)
parcels.loc[parcels.index[0], "bess_cnig_parcel_precheck_status"] = "AUTHORIZED"
assessed = result.relation_assessments.copy(deep=True)
assessed.loc[assessed.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
assessed.loc[assessed.index[0], "bess_cnig_resulting_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
source = assessed.drop(columns=list(RELATION_COLUMNS))
corrupted = replace(
        result,
        parcels=parcels,
        relation_assessments=assessed,
        source_application_relations_content_sha256=module._frame_sha256(
            source,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
    )
corrupted = module._result_with_hashes(corrupted)
manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Regression protected**

Locks `authorized status artifact fails local verified byte loading`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_authorized_status_artifact_fails_local_verified_byte_loading(
    tmp_path: Path,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_parcel_precheck_status"] = "AUTHORIZED"
    assessed = result.relation_assessments.copy(deep=True)
    assessed.loc[assessed.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
    assessed.loc[assessed.index[0], "bess_cnig_resulting_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
    source = assessed.drop(columns=list(RELATION_COLUMNS))
    corrupted = replace(
        result,
        parcels=parcels,
        relation_assessments=assessed,
        source_application_relations_content_sha256=module._frame_sha256(
            source,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
    )
    corrupted = module._result_with_hashes(corrupted)
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

### `test_coordinated_relation_identity_artifact_corruption_fails_locally`

**Purpose**

Exercises `coordinated relation identity artifact corruption fails locally`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `factory`.

**Setup**

```python
corrupted = factory()
manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert callable(factory)
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Regression protected**

Locks `coordinated relation identity artifact corruption fails locally`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_coordinated_relation_identity_artifact_corruption_fails_locally(
    tmp_path: Path,
    factory: object,
) -> None:
    assert callable(factory)
    corrupted = factory()
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

### `test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`

**Purpose**

Exercises `controlling relation cannot be relabelled contextual in artifact`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
corrupted = _surface_touch_semantic_corruption_result()
manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="surface|metric|type"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Regression protected**

Locks `controlling relation cannot be relabelled contextual in artifact`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_controlling_relation_cannot_be_relabelled_contextual_in_artifact(
    tmp_path: Path,
) -> None:
    corrupted = _surface_touch_semantic_corruption_result()
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="surface|metric|type"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

### `test_no_relation_parcel_rejects_textual_null_identity`

**Purpose**

Exercises `no relation parcel rejects textual null identity`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `parcel_id`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
parcels = result.parcels.copy(deep=True)
no_relation = parcels["bess_cnig_parcel_aggregation_status"].eq(
        "NO_PLANNING_FEATURE_RELATION"
    )
parcel_id_dtype = parcels["parcel_id"].dtype
parcels.loc[parcels.index[no_relation][0], "parcel_id"] = parcel_id
parcels["parcel_id"] = pd.array(
        parcels["parcel_id"].tolist(), dtype=parcel_id_dtype
    )
corrupted = module._result_with_hashes(replace(result, parcels=parcels))
manifest, paths, payload = _write_artifacts(tmp_path, corrupted)
persisted_parcels = gpd.read_parquet(paths["PARCELS"])
persisted_relations = pd.read_parquet(paths["RELATION_ASSESSMENTS"])
manifest.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
```

**Action**

```python
for record in payload["artifacts"]:
        if record["artifact_role"] == "PARCELS":
            record["frame_schema_signature"] = deterministic_frame_schema_signature(
                persisted_parcels
            )
        else:
            record["frame_schema_signature"] = deterministic_frame_schema_signature(
                persisted_relations
            )
```

**Expected result**

```python
assert no_relation.any()
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="parcel ID"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_no_relation_parcel_rejects_textual_null_identity(
    tmp_path: Path, parcel_id: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
    parcels = result.parcels.copy(deep=True)
    no_relation = parcels["bess_cnig_parcel_aggregation_status"].eq(
        "NO_PLANNING_FEATURE_RELATION"
    )
    assert no_relation.any()
    parcel_id_dtype = parcels["parcel_id"].dtype
    parcels.loc[parcels.index[no_relation][0], "parcel_id"] = parcel_id
    parcels["parcel_id"] = pd.array(
        parcels["parcel_id"].tolist(), dtype=parcel_id_dtype
    )
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    manifest, paths, payload = _write_artifacts(tmp_path, corrupted)
    persisted_parcels = gpd.read_parquet(paths["PARCELS"])
    persisted_relations = pd.read_parquet(paths["RELATION_ASSESSMENTS"])
    for record in payload["artifacts"]:
        if record["artifact_role"] == "PARCELS":
            record["frame_schema_signature"] = deterministic_frame_schema_signature(
                persisted_parcels
            )
        else:
            record["frame_schema_signature"] = deterministic_frame_schema_signature(
                persisted_relations
            )
    manifest.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="parcel ID"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

### `test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Purpose**

Exercises `relation identity and global mapping fail before heavy validation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application, _ = _aggregation_fixture()
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
for corrupted in (
        _duplicate_selected_pair_result(),
        _invalid_lower_feature_id_result(),
        _cross_parcel_priority_conflict_result(),
    ):
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, corrupted
            )
assert calls == 0
```

**Regression protected**

Locks `relation identity and global mapping fail before heavy validation`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_relation_identity_and_global_mapping_fail_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, _ = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    for corrupted in (
        _duplicate_selected_pair_result(),
        _invalid_lower_feature_id_result(),
        _cross_parcel_priority_conflict_result(),
    ):
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, corrupted
            )
    assert calls == 0
```

### `test_relation_identity_and_global_mapping_fail_before_heavy_validation.counted`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_semantic_failure_fast_fails_before_heavy_validation`

**Purpose**

Exercises `relation semantic failure fast fails before heavy validation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application, _ = _aggregation_fixture()
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs,
            coded,
            config,
            policy,
            application,
            _surface_touch_semantic_corruption_result(),
        )
assert calls == 0
```

**Regression protected**

Locks `relation semantic failure fast fails before heavy validation`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_relation_semantic_failure_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, _ = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs,
            coded,
            config,
            policy,
            application,
            _surface_touch_semantic_corruption_result(),
        )
    assert calls == 0
```

### `test_relation_semantic_failure_fast_fails_before_heavy_validation.counted`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_parcel_decision_status_domain_rejects_forbidden_vocabulary`

**Purpose**

Exercises `parcel decision status domain rejects forbidden vocabulary`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
_, _, _, _, _, result = _aggregation_fixture()
parcels = result.parcels.copy(deep=True)
decision_index = parcels.index[
        parcels["bess_cnig_parcel_aggregation_status"] == "AGGREGATED_EXACT_POLICY"
    ][0]
parcels.loc[decision_index, "bess_cnig_parcel_precheck_status"] = status
corrupted = module._result_with_hashes(replace(result, parcels=parcels))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="status"):
        module._validate_result_envelope(corrupted)
```

**Regression protected**

Locks `parcel decision status domain rejects forbidden vocabulary`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_parcel_decision_status_domain_rejects_forbidden_vocabulary(
    status: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    parcels = result.parcels.copy(deep=True)
    decision_index = parcels.index[
        parcels["bess_cnig_parcel_aggregation_status"] == "AGGREGATED_EXACT_POLICY"
    ][0]
    parcels.loc[decision_index, "bess_cnig_parcel_precheck_status"] = status
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="status"):
        module._validate_result_envelope(corrupted)
```

### `test_persisted_feature_id_json_must_be_portable_and_canonical`

**Purpose**

Exercises `persisted feature id json must be portable and canonical`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `json_value`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
_, _, _, _, _, result = _aggregation_fixture()
parcels = result.parcels.copy(deep=True)
parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = json_value
corrupted = module._result_with_hashes(replace(result, parcels=parcels))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)
```

**Regression protected**

Locks `persisted feature id json must be portable and canonical`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_persisted_feature_id_json_must_be_portable_and_canonical(
    json_value: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = json_value
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)
```

### `test_representative_intrinsic_failures_all_precede_heavy_validation`

**Purpose**

Exercises `representative intrinsic failures all precede heavy validation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application, result = _aggregation_fixture()
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
invalid_results: list[BessPlanningFeatureParcelAggregationResult] = []
inherited = result.relation_assessments.copy(deep=True)
inherited.loc[inherited.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
invalid_results.append(
        _rehash_coordinated_result(replace(result, relation_assessments=inherited))
    )
parcel_status = result.parcels.copy(deep=True)
parcel_status.loc[parcel_status.index[0], "bess_cnig_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
invalid_results.append(
        module._result_with_hashes(replace(result, parcels=parcel_status))
    )
ambiguous = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=50),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        )
    )
ambiguous_relations = ambiguous.relation_assessments.copy(deep=True)
ambiguous_relations.loc[
        ambiguous_relations.index[1], "bess_cnig_status_priority"
    ] = 50
invalid_results.append(
        _rehash_coordinated_result(
            replace(ambiguous, relation_assessments=ambiguous_relations)
        )
    )
point_parcels = result.parcels.copy(deep=True)
point_parcels.at[point_parcels.index[0], point_parcels.geometry.name] = Point(0, 0)
invalid_results.append(replace(result, parcels=point_parcels))
duplicate = pd.concat([result.parcels, result.parcels.iloc[:, [0]]], axis=1)
invalid_results.append(
        replace(
            result,
            parcels=gpd.GeoDataFrame(
                duplicate,
                geometry=result.parcels.geometry.name,
                crs=result.parcels.crs,
            ),
        )
    )
invalid_results.append(
        module._result_with_hashes(
            replace(result, application_result_hash_schema_version=3)
        )
    )
json_parcels = result.parcels.copy(deep=True)
json_parcels.loc[json_parcels.index[0], "bess_cnig_selected_feature_ids_json"] = (
        '["/tmp/feature"]'
    )
invalid_results.append(
        module._result_with_hashes(replace(result, parcels=json_parcels))
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
for invalid in invalid_results:
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, invalid
            )
assert calls == 0
```

**Regression protected**

Prevents geometry calculations or source acceptance under an unapproved/missing coordinate reference system.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_representative_intrinsic_failures_all_precede_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    invalid_results: list[BessPlanningFeatureParcelAggregationResult] = []

    inherited = result.relation_assessments.copy(deep=True)
    inherited.loc[inherited.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
    invalid_results.append(
        _rehash_coordinated_result(replace(result, relation_assessments=inherited))
    )

    parcel_status = result.parcels.copy(deep=True)
    parcel_status.loc[parcel_status.index[0], "bess_cnig_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
    invalid_results.append(
        module._result_with_hashes(replace(result, parcels=parcel_status))
    )

    ambiguous = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=50),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        )
    )
    ambiguous_relations = ambiguous.relation_assessments.copy(deep=True)
    ambiguous_relations.loc[
        ambiguous_relations.index[1], "bess_cnig_status_priority"
    ] = 50
    invalid_results.append(
        _rehash_coordinated_result(
            replace(ambiguous, relation_assessments=ambiguous_relations)
        )
    )

    point_parcels = result.parcels.copy(deep=True)
    point_parcels.at[point_parcels.index[0], point_parcels.geometry.name] = Point(0, 0)
    invalid_results.append(replace(result, parcels=point_parcels))

    duplicate = pd.concat([result.parcels, result.parcels.iloc[:, [0]]], axis=1)
    invalid_results.append(
        replace(
            result,
            parcels=gpd.GeoDataFrame(
                duplicate,
                geometry=result.parcels.geometry.name,
                crs=result.parcels.crs,
            ),
        )
    )
    invalid_results.append(
        module._result_with_hashes(
            replace(result, application_result_hash_schema_version=3)
        )
    )

    json_parcels = result.parcels.copy(deep=True)
    json_parcels.loc[json_parcels.index[0], "bess_cnig_selected_feature_ids_json"] = (
        '["/tmp/feature"]'
    )
    invalid_results.append(
        module._result_with_hashes(replace(result, parcels=json_parcels))
    )

    for invalid in invalid_results:
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, invalid
            )
    assert calls == 0
```

### `test_representative_intrinsic_failures_all_precede_heavy_validation.counted`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_one_aggregation_and_one_public_validation_each_call_heavy_once`

**Purpose**

Exercises `one aggregation and one public validation each call heavy once`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application = _application_fixture()
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
actual = module.validate_bess_planning_feature_application_result
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
```

**Action**

```python
result = module.aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
module.validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, result
    )
```

**Expected result**

```python
assert calls == 1
assert calls == 2
```

**Regression protected**

Locks `one aggregation and one public validation each call heavy once` through the exact asserted conditions: `calls == 1`; `calls == 2`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_one_aggregation_and_one_public_validation_each_call_heavy_once(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    actual = module.validate_bess_planning_feature_application_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    result = module.aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    assert calls == 1
    module.validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, result
    )
    assert calls == 2
```

### `test_one_aggregation_and_one_public_validation_each_call_heavy_once.counted`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_two_file_verified_byte_artifacts_and_source_readback`

**Purpose**

Exercises `valid two file verified byte artifacts and source readback`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application, result = _aggregation_fixture()
manifest, paths, _ = _write_artifacts(tmp_path, result)
loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
assert_geodataframe_equal(result.parcels, loaded.parcels)
assert_frame_equal(result.relation_assessments, loaded.relation_assessments)
```

**Action**

```python
validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, loaded
    )
```

**Expected result**

```python
# Completion without an exception is the asserted outcome.
```

**Regression protected**

Locks `valid two file verified byte artifacts and source readback` by requiring the reproduced call path `_aggregation_fixture`, `_write_artifacts`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `assert_geodataframe_equal` without an unasserted exception.

**Test boundary**

- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_valid_two_file_verified_byte_artifacts_and_source_readback(
    tmp_path: Path,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
    assert_geodataframe_equal(result.parcels, loaded.parcels)
    assert_frame_equal(result.relation_assessments, loaded.relation_assessments)
    validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, loaded
    )
```

### `test_artifact_manifest_corruption_is_rejected`

**Purpose**

Exercises `artifact manifest corruption is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
_, _, _, _, _, result = _aggregation_fixture()
manifest_path, paths, manifest = _write_artifacts(tmp_path, result)
mutation(manifest)
manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert callable(mutation)
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_artifact_manifest_corruption_is_rejected(
    tmp_path: Path, mutation: object
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, manifest = _write_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

### `test_duplicate_json_and_physical_replacement_are_rejected`

**Purpose**

Exercises `duplicate json and physical replacement are rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, _, result = _aggregation_fixture()
manifest_path, paths, _ = _write_artifacts(tmp_path, result)
original = manifest_path.read_text(encoding="utf-8")
manifest_path.write_text(
        '{"schema_version":1,"schema_version":1}', encoding="utf-8"
    )
manifest_path.write_text(original, encoding="utf-8")
paths["RELATION_ASSESSMENTS"].write_bytes(
        paths["RELATION_ASSESSMENTS"].read_bytes() + b"tamper"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="Duplicate JSON"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="size|SHA"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Regression protected**

Locks `duplicate json and physical replacement are rejected`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_json_and_physical_replacement_are_rejected(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    original = manifest_path.read_text(encoding="utf-8")
    manifest_path.write_text(
        '{"schema_version":1,"schema_version":1}', encoding="utf-8"
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="Duplicate JSON"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
    manifest_path.write_text(original, encoding="utf-8")
    paths["RELATION_ASSESSMENTS"].write_bytes(
        paths["RELATION_ASSESSMENTS"].read_bytes() + b"tamper"
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="size|SHA"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

### `test_verified_bytes_are_the_bytes_parsed`

**Purpose**

Exercises `verified bytes are the bytes parsed`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, _, result = _aggregation_fixture()
manifest_path, paths, _ = _write_artifacts(tmp_path, result)
target = paths["RELATION_ASSESSMENTS"]
verified = target.read_bytes()
replacement = tmp_path / "replacement.parquet"
result.relation_assessments.to_parquet(replacement, compression="gzip", index=True)
replacement_bytes = replacement.read_bytes()
original_read_bytes = Path.read_bytes
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
original_read = module.pd.read_parquet
observed: list[bytes] = []
def replace_after_read(path: Path) -> bytes:
        payload = original_read_bytes(path)
        if path == target:
            path.write_bytes(replacement_bytes)
        return payload
def inspect_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(source.getvalue())
        return original_read(source, *args, **kwargs)
monkeypatch.setattr(Path, "read_bytes", replace_after_read)
monkeypatch.setattr(module.pd, "read_parquet", inspect_read)
loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
assert_frame_equal(result.relation_assessments, loaded.relation_assessments)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert verified in observed
```

**Regression protected**

Locks `verified bytes are the bytes parsed` through the exact asserted conditions: `verified in observed`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_verified_bytes_are_the_bytes_parsed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    target = paths["RELATION_ASSESSMENTS"]
    verified = target.read_bytes()
    replacement = tmp_path / "replacement.parquet"
    result.relation_assessments.to_parquet(replacement, compression="gzip", index=True)
    replacement_bytes = replacement.read_bytes()
    original_read_bytes = Path.read_bytes
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    original_read = module.pd.read_parquet
    observed: list[bytes] = []

    def replace_after_read(path: Path) -> bytes:
        payload = original_read_bytes(path)
        if path == target:
            path.write_bytes(replacement_bytes)
        return payload

    def inspect_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(source.getvalue())
        return original_read(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_read)
    monkeypatch.setattr(module.pd, "read_parquet", inspect_read)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
    assert verified in observed
    assert_frame_equal(result.relation_assessments, loaded.relation_assessments)
```

### `test_verified_bytes_are_the_bytes_parsed.replace_after_read`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `monkeypatch.setattr(Path, 'read_bytes', replace_after_read)`.

**Complete source-ordered implementation**

```python
def replace_after_read(path: Path) -> bytes:
        payload = original_read_bytes(path)
        if path == target:
            path.write_bytes(replacement_bytes)
        return payload
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_verified_bytes_are_the_bytes_parsed.inspect_read`

**Exact signature**

```python
def inspect_read(source: object, *args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for inspect read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
original_read(source, *args, **kwargs)
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
- In-memory mutation: `observed`.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `monkeypatch.setattr(module.pd, 'read_parquet', inspect_read)`.

**Complete source-ordered implementation**

```python
def inspect_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(source.getvalue())
        return original_read(source, *args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_exports_are_stable`

**Purpose**

Exercises `public exports are stable`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
required = {
        "BessPlanningFeatureParcelAggregationArtifactManifest",
        "BessPlanningFeatureParcelAggregationError",
        "BessPlanningFeatureParcelAggregationResult",
        "aggregate_bess_planning_feature_policy_to_parcels",
        "load_bess_planning_feature_parcel_aggregation_artifacts",
        "validate_bess_planning_feature_parcel_aggregation_result",
    }
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
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
```

**Regression protected**

Locks `public exports are stable` through the exact asserted conditions: `set(module.__all__) == required`; `required.issubset(set(stages.__all__))`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_public_exports_are_stable() -> None:
    required = {
        "BessPlanningFeatureParcelAggregationArtifactManifest",
        "BessPlanningFeatureParcelAggregationError",
        "BessPlanningFeatureParcelAggregationResult",
        "aggregate_bess_planning_feature_policy_to_parcels",
        "load_bess_planning_feature_parcel_aggregation_artifacts",
        "validate_bess_planning_feature_parcel_aggregation_result",
    }
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
```

### `_coherent_parcel_area_mutation`

**Exact signature**

```python
def _coherent_parcel_area_mutation(
    result: BessPlanningFeatureParcelAggregationResult,
    geometry_kind: str,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Private `test` helper for coherent parcel area mutation; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
_rehash_coordinated_result(replace(result, relation_assessments=relations))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `relations['geometry_kind'].eq`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `relations.loc[index, 'parcel_metric_area_m2']`, `relations.loc[index, 'parcel_share_pct']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_coherent_parcel_area_mutation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `_coherent_parcel_area_mutation`.
- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_coherent_parcel_area_mutation`.

**Complete source-ordered implementation**

```python
def _coherent_parcel_area_mutation(
    result: BessPlanningFeatureParcelAggregationResult,
    geometry_kind: str,
) -> BessPlanningFeatureParcelAggregationResult:
    relations = result.relation_assessments.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq(geometry_kind)][0]
    relations.loc[index, "parcel_metric_area_m2"] = 8000.0
    if geometry_kind == "SURFACE":
        relations.loc[index, "parcel_share_pct"] = (
            100.0 * float(relations.loc[index, "intersection_area_m2"]) / 8000.0
        )
    return _rehash_coordinated_result(replace(result, relation_assessments=relations))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_relation_parcel_area_is_bound_to_real_parcel_geometry`

**Purpose**

Exercises `relation parcel area is bound to real parcel geometry`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `geometry_kind`, `relation_type`.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type)])
    )
changed = _coherent_parcel_area_mutation(result, geometry_kind)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel.*area|area.*parcel"
    ):
        module._validate_result_envelope(changed)
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_relation_parcel_area_is_bound_to_real_parcel_geometry(
    geometry_kind: str,
    relation_type: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type)])
    )
    changed = _coherent_parcel_area_mutation(result, geometry_kind)
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel.*area|area.*parcel"
    ):
        module._validate_result_envelope(changed)
```

### `test_self_consistent_parcel_area_artifact_is_rejected`

**Purpose**

Exercises `self consistent parcel area artifact is rejected`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
changed = _coherent_parcel_area_mutation(result, "SURFACE")
manifest, paths, payload = _write_artifacts(tmp_path, changed)
persisted = {
        "PARCELS": gpd.read_parquet(paths["PARCELS"]),
        "RELATION_ASSESSMENTS": pd.read_parquet(paths["RELATION_ASSESSMENTS"]),
    }
persisted_result = _rehash_coordinated_result(
        replace(
            changed,
            parcels=persisted["PARCELS"],
            relation_assessments=persisted["RELATION_ASSESSMENTS"],
        )
    )
for field in fields(BessPlanningFeatureParcelAggregationResult):
        if field.name not in {"parcels", "relation_assessments"}:
            payload[field.name] = getattr(persisted_result, field.name)
manifest.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
```

**Action**

```python
for record in payload["artifacts"]:
        record["frame_schema_signature"] = deterministic_frame_schema_signature(
            persisted[record["artifact_role"]]
        )
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel.*area|area.*parcel"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Regression protected**

Locks `self consistent parcel area artifact is rejected`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_self_consistent_parcel_area_artifact_is_rejected(tmp_path: Path) -> None:
    result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
    changed = _coherent_parcel_area_mutation(result, "SURFACE")
    manifest, paths, payload = _write_artifacts(tmp_path, changed)
    persisted = {
        "PARCELS": gpd.read_parquet(paths["PARCELS"]),
        "RELATION_ASSESSMENTS": pd.read_parquet(paths["RELATION_ASSESSMENTS"]),
    }
    persisted_result = _rehash_coordinated_result(
        replace(
            changed,
            parcels=persisted["PARCELS"],
            relation_assessments=persisted["RELATION_ASSESSMENTS"],
        )
    )
    for field in fields(BessPlanningFeatureParcelAggregationResult):
        if field.name not in {"parcels", "relation_assessments"}:
            payload[field.name] = getattr(persisted_result, field.name)
    for record in payload["artifacts"]:
        record["frame_schema_signature"] = deterministic_frame_schema_signature(
            persisted[record["artifact_role"]]
        )
    manifest.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel.*area|area.*parcel"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

### `test_parcel_area_validation_uses_reprojected_calculation_copy`

**Purpose**

Exercises `parcel area validation uses reprojected calculation copy`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
original = result.parcels.copy(deep=True)
geographic = result.parcels.to_crs("EPSG:4326")
changed = _rehash_coordinated_result(replace(result, parcels=geographic))
module._validate_result_envelope(changed)
assert_geodataframe_equal(
        result.parcels, original, check_dtype=True, check_crs=True
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

- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_parcel_area_validation_uses_reprojected_calculation_copy() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
    original = result.parcels.copy(deep=True)
    geographic = result.parcels.to_crs("EPSG:4326")
    changed = _rehash_coordinated_result(replace(result, parcels=geographic))
    module._validate_result_envelope(changed)
    assert_geodataframe_equal(
        result.parcels, original, check_dtype=True, check_crs=True
    )
```

### `test_parcel_area_defect_fast_fails_before_application_source_validation`

**Purpose**

Exercises `parcel area defect fast fails before application source validation`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, policy, application, _ = _aggregation_fixture()
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
changed = _coherent_parcel_area_mutation(result, "SURFACE")
calls = 0
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs, coded, config, policy, application, changed
        )
assert calls == 0
```

**Regression protected**

Locks `parcel area defect fast fails before application source validation`: the reproduced adversarial input must raise `BessPlanningFeatureParcelAggregationError` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

```python
def test_parcel_area_defect_fast_fails_before_application_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, _ = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
    changed = _coherent_parcel_area_mutation(result, "SURFACE")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs, coded, config, policy, application, changed
        )
    assert calls == 0
```

### `test_parcel_area_defect_fast_fails_before_application_source_validation.counted`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams`

**Purpose**

Exercises `step 7d 5b 2b 5 aggregation loader requires exact upstreams`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert tuple(
        inspect.signature(
            module.load_bess_planning_feature_parcel_aggregation_artifacts
        ).parameters
    ) == (
        "manifest_path",
        "parcels_path",
        "relation_assessments_path",
        "source_parcels",
        "application_result",
    )
assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")
```

**Regression protected**

Locks `step 7d 5b 2b 5 aggregation loader requires exact upstreams` through the exact asserted conditions: `tuple(inspect.signature(module.load_bess_planning_feature_parcel_aggregation_artifacts).parameters) == ('manifest_path', 'parcels_path', 'relation_assessments_path', 'source_parcels', 'application_result')`; `hasattr(module, 'validate_bess_planning_feature_application_result_envelope')`.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    assert tuple(
        inspect.signature(
            module.load_bess_planning_feature_parcel_aggregation_artifacts
        ).parameters
    ) == (
        "manifest_path",
        "parcels_path",
        "relation_assessments_path",
        "source_parcels",
        "application_result",
    )
    assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")
```

### `test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`

**Purpose**

Exercises `source bound aggregation loader accepts only supplied upstreams`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, _, _, _, application, result = _aggregation_fixture()
manifest, paths, _ = _write_artifacts(tmp_path, result)
loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest,
        paths["PARCELS"],
        paths["RELATION_ASSESSMENTS"],
        inputs[1],
        application,
    )
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
```

**Regression protected**

Locks `source bound aggregation loader accepts only supplied upstreams` through the exact asserted conditions: `loaded.complete_result_content_sha256 == result.complete_result_content_sha256`.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_source_bound_aggregation_loader_accepts_only_supplied_upstreams(
    tmp_path: Path,
) -> None:
    inputs, _, _, _, application, result = _aggregation_fixture()
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest,
        paths["PARCELS"],
        paths["RELATION_ASSESSMENTS"],
        inputs[1],
        application,
    )
    assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )
```

### `test_aggregation_manifest_filenames_are_casefold_unique`

**Purpose**

Exercises `aggregation manifest filenames are casefold unique`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, _, _, result = _aggregation_fixture()
_, _, payload = _write_artifacts(tmp_path, result)
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
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```

**Regression protected**

Locks `aggregation manifest filenames are casefold unique`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_aggregation_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```

### `_changed_parcel_geometry_upstreams`

**Exact signature**

```python
def _changed_parcel_geometry_upstreams(
    source_parcels: gpd.GeoDataFrame,
    application: object,
) -> tuple[gpd.GeoDataFrame, object]:
```

**Purpose**

Private `test` helper for changed parcel geometry upstreams; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[gpd.GeoDataFrame, object]`.
- Every observed return expression is reproduced without truncation:
```python
(changed_parcels, changed_application)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `changed_parcels.to_crs`, `relations.loc[surface, 'intersection_area_m2'].astype`, `relations['geometry_kind'].eq`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `changed_parcels.loc[parcel_index, geometry_column]`, `relations.loc[mask, 'parcel_metric_area_m2']`, `relations.loc[surface, 'parcel_share_pct']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_changed_parcel_geometry_upstreams`.

**Complete source-ordered implementation**

```python
def _changed_parcel_geometry_upstreams(
    source_parcels: gpd.GeoDataFrame,
    application: object,
) -> tuple[gpd.GeoDataFrame, object]:
    application_module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed_parcels = source_parcels.copy(deep=True)
    parcel_id = str(application.relations.iloc[0]["parcel_id"])
    parcel_index = changed_parcels.index[changed_parcels["parcel_id"].eq(parcel_id)][0]
    geometry_column = changed_parcels.geometry.name
    geometry = changed_parcels.loc[parcel_index, geometry_column]
    changed_parcels.loc[parcel_index, geometry_column] = affinity.scale(
        geometry, xfact=2.0, yfact=2.0, origin="centroid"
    )
    metric = changed_parcels.to_crs(2154).loc[parcel_index, geometry_column].area
    relations = application.relations.copy(deep=True)
    mask = relations["parcel_id"].eq(parcel_id)
    relations.loc[mask, "parcel_metric_area_m2"] = float(metric)
    surface = mask & relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface, "parcel_share_pct"] = (
        100.0
        * relations.loc[surface, "intersection_area_m2"].astype("float64")
        / float(metric)
    )
    changed_application = application_module._result_with_hashes(
        replace(application, relations=relations)
    )
    application_module._validate_result_envelope(changed_application)
    return changed_parcels, changed_application
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`

**Purpose**

Exercises `source bound aggregation loader rejects coordinated upstream changes`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
inputs, _, _, _, application, _ = _aggregation_fixture()
source_parcels = inputs[1]
if mutation in {"parcel_order", "unrelated_parcel_geometry"}:
        extra = source_parcels.iloc[[0]].copy(deep=True)
        extra["parcel_id"] = pd.array(["NO-RELATION-PARCEL"], dtype="str")
        extra.geometry = extra.geometry.map(
            lambda geometry: affinity.translate(geometry, xoff=10_000.0)
        )
        extra.index = pd.Index(
            [int(source_parcels.index.max()) + 1],
            dtype=source_parcels.index.dtype,
            name=source_parcels.index.name,
        )
        source_parcels = gpd.GeoDataFrame(
            pd.concat([source_parcels, extra]),
            geometry=source_parcels.geometry.name,
            crs=source_parcels.crs,
        )
changed_parcels = source_parcels.copy(deep=True)
changed_application = application
if mutation == "parcel_geometry":
        changed_parcels, changed_application = _changed_parcel_geometry_upstreams(
            source_parcels, application
        )
    elif mutation == "parcel_crs":
        changed_parcels = source_parcels.to_crs(4326)
    elif mutation == "application_relation":
        changed_application = _coordinated_policy_mutation(
            application,
            "bess_cnig_rationale",
            "A different exact relation rationale.",
        )
    elif mutation == "parcel_order":
        changed_parcels = source_parcels.iloc[::-1].copy(deep=True)
    else:
        related_ids = set(application.relations["parcel_id"])
        available = changed_parcels.loc[~changed_parcels["parcel_id"].isin(related_ids)]
        assert not available.empty
        index = available.index[0]
        changed_parcels.loc[index, changed_parcels.geometry.name] = affinity.translate(
            changed_parcels.loc[index, changed_parcels.geometry.name], xoff=1.0
        )
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
changed = module._build_result(changed_parcels, changed_application)
module._validate_result_envelope(changed)
manifest, paths, _ = _write_artifacts(tmp_path, changed)
heavy_calls = 0
def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", forbidden_heavy
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeatureParcelAggregationError, match="source lock"):
        module.load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest,
            paths["PARCELS"],
            paths["RELATION_ASSESSMENTS"],
            source_parcels,
            application,
        )
assert heavy_calls == 0
```

**Regression protected**

Prevents geometry changes from passing a preservation or source-bound comparison merely because other fields were updated coherently.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    inputs, _, _, _, application, _ = _aggregation_fixture()
    source_parcels = inputs[1]
    if mutation in {"parcel_order", "unrelated_parcel_geometry"}:
        extra = source_parcels.iloc[[0]].copy(deep=True)
        extra["parcel_id"] = pd.array(["NO-RELATION-PARCEL"], dtype="str")
        extra.geometry = extra.geometry.map(
            lambda geometry: affinity.translate(geometry, xoff=10_000.0)
        )
        extra.index = pd.Index(
            [int(source_parcels.index.max()) + 1],
            dtype=source_parcels.index.dtype,
            name=source_parcels.index.name,
        )
        source_parcels = gpd.GeoDataFrame(
            pd.concat([source_parcels, extra]),
            geometry=source_parcels.geometry.name,
            crs=source_parcels.crs,
        )
    changed_parcels = source_parcels.copy(deep=True)
    changed_application = application
    if mutation == "parcel_geometry":
        changed_parcels, changed_application = _changed_parcel_geometry_upstreams(
            source_parcels, application
        )
    elif mutation == "parcel_crs":
        changed_parcels = source_parcels.to_crs(4326)
    elif mutation == "application_relation":
        changed_application = _coordinated_policy_mutation(
            application,
            "bess_cnig_rationale",
            "A different exact relation rationale.",
        )
    elif mutation == "parcel_order":
        changed_parcels = source_parcels.iloc[::-1].copy(deep=True)
    else:
        related_ids = set(application.relations["parcel_id"])
        available = changed_parcels.loc[~changed_parcels["parcel_id"].isin(related_ids)]
        assert not available.empty
        index = available.index[0]
        changed_parcels.loc[index, changed_parcels.geometry.name] = affinity.translate(
            changed_parcels.loc[index, changed_parcels.geometry.name], xoff=1.0
        )
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    changed = module._build_result(changed_parcels, changed_application)
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_artifacts(tmp_path, changed)
    heavy_calls = 0

    def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", forbidden_heavy
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="source lock"):
        module.load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest,
            paths["PARCELS"],
            paths["RELATION_ASSESSMENTS"],
            source_parcels,
            application,
        )
    assert heavy_calls == 0
```

### `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes.forbidden_heavy`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', forbidden_heavy)`.

**Complete source-ordered implementation**

```python
def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`

**Purpose**

Exercises `source bound aggregation loader rebuilds once without mutating upstreams`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, _, _, _, application, result = _aggregation_fixture()
source_parcels = inputs[1]
parcels_before = source_parcels.copy(deep=True)
relations_before = application.relations.copy(deep=True)
manifest, paths, _ = _write_artifacts(tmp_path, result)
module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
actual_build = module._build_result
build_calls = 0
heavy_calls = 0
def counted_build(*args: object, **kwargs: object) -> object:
        nonlocal build_calls
        build_calls += 1
        return actual_build(*args, **kwargs)
def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1
monkeypatch.setattr(module, "_build_result", counted_build)
monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", forbidden_heavy
    )
loaded = module.load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest,
        paths["PARCELS"],
        paths["RELATION_ASSESSMENTS"],
        source_parcels,
        application,
    )
assert_geodataframe_equal(source_parcels, parcels_before)
assert_frame_equal(application.relations, relations_before)
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
assert build_calls == 1
assert heavy_calls == 0
```

**Regression protected**

Locks `source bound aggregation loader rebuilds once without mutating upstreams` through the exact asserted conditions: `loaded.complete_result_content_sha256 == result.complete_result_content_sha256`; `build_calls == 1`; `heavy_calls == 0`.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.
- Uses real in-memory Shapely/GeoPandas geometry operations unless the target is patched.

**Complete test implementation**

```python
def test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    inputs, _, _, _, application, result = _aggregation_fixture()
    source_parcels = inputs[1]
    parcels_before = source_parcels.copy(deep=True)
    relations_before = application.relations.copy(deep=True)
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    actual_build = module._build_result
    build_calls = 0
    heavy_calls = 0

    def counted_build(*args: object, **kwargs: object) -> object:
        nonlocal build_calls
        build_calls += 1
        return actual_build(*args, **kwargs)

    def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1

    monkeypatch.setattr(module, "_build_result", counted_build)
    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", forbidden_heavy
    )
    loaded = module.load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest,
        paths["PARCELS"],
        paths["RELATION_ASSESSMENTS"],
        source_parcels,
        application,
    )
    assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )
    assert build_calls == 1
    assert heavy_calls == 0
    assert_geodataframe_equal(source_parcels, parcels_before)
    assert_frame_equal(application.relations, relations_before)
```

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.counted_build`

**Exact signature**

```python
def counted_build(*args: object, **kwargs: object) -> object:
```

**Purpose**

Private `test` helper for counted build; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `monkeypatch.setattr(module, '_build_result', counted_build)`.

**Complete source-ordered implementation**

```python
def counted_build(*args: object, **kwargs: object) -> object:
        nonlocal build_calls
        build_calls += 1
        return actual_build(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.forbidden_heavy`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', forbidden_heavy)`.

**Complete source-ordered implementation**

```python
def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_aggregation_loader_rejects_bad_application_before_artifact_reads`

**Purpose**

Exercises `aggregation loader rejects bad application before artifact reads`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, _, _, _, application, result = _aggregation_fixture()
manifest, paths, _ = _write_artifacts(tmp_path, result)
reads = 0
original = Path.read_bytes
def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)
monkeypatch.setattr(Path, "read_bytes", counted)
forged = replace(application, complete_result_content_sha256="0" * 64)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(Exception, match="hash|SHA|invalid"):
        _load_aggregation_artifacts(
            manifest,
            paths["PARCELS"],
            paths["RELATION_ASSESSMENTS"],
            inputs[1],
            forged,
        )
assert reads == 0
```

**Regression protected**

Locks `aggregation loader rejects bad application before artifact reads`: the reproduced adversarial input must raise `Exception` before the prohibited success path.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_aggregation_loader_rejects_bad_application_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    inputs, _, _, _, application, result = _aggregation_fixture()
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    reads = 0
    original = Path.read_bytes

    def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted)
    forged = replace(application, complete_result_content_sha256="0" * 64)
    with pytest.raises(Exception, match="hash|SHA|invalid"):
        _load_aggregation_artifacts(
            manifest,
            paths["PARCELS"],
            paths["RELATION_ASSESSMENTS"],
            inputs[1],
            forged,
        )
    assert reads == 0
```

### `test_aggregation_loader_rejects_bad_application_before_artifact_reads.counted`

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.

**Complete source-ordered implementation**

```python
def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_aggregation_manifest_rejects_nonportable_filename`

**Purpose**

Exercises `aggregation manifest rejects nonportable filename`; the exact setup, action, expected exception, and assertions reproduced below define the locked regression.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `filename`.

**Setup**

```python
_, _, _, _, _, result = _aggregation_fixture()
_, _, payload = _write_artifacts(tmp_path, result)
payload["artifacts"][0]["filename"] = filename
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```

**Regression protected**

Locks `aggregation manifest rejects nonportable filename`: the reproduced adversarial input must raise `ValueError` before the prohibited success path.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_aggregation_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```


## 7. Data contracts

### `PARCEL_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_formal_review_required",
    "bess_cnig_aggregation_scope",
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
    "bess_cnig_application_result_sha256",
)
```

### `RELATION_COLUMNS` — canonical or derived frame-column schema

```python
RELATION_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_selected_for_parcel_status",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
    "bess_cnig_resulting_parcel_status_priority",
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
