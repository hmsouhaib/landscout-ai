# `tests/unit/test_aggregate_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_aggregate_bess_planning_feature_policy.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.
- Source SHA256: `1d7ebf63f11dea764e93c8f78e7b9b7f456a4401e5afb1c1998d9bcdfbb31c94`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for aggregate bess planning feature policy; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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
- `from landscout.common.strict_json import loads_strict_json_object`
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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `PARCEL_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_parcel_aggregation_status`
  - `bess_cnig_parcel_precheck_status`
  - `bess_cnig_parcel_precheck_confidence`
  - `bess_cnig_parcel_status_priority`
  - `bess_cnig_controlling_relation_count`
  - `bess_cnig_exact_controlling_relation_count`
  - `bess_cnig_unresolved_controlling_relation_count`
  - `bess_cnig_touch_only_relation_count`
  - `bess_cnig_selected_relation_count`
  - `bess_cnig_lower_priority_controlling_relation_count`
  - `bess_cnig_distinct_exact_status_count`
  - `bess_cnig_multiple_exact_statuses`
  - `bess_cnig_selected_feature_ids_json`
  - `bess_cnig_unresolved_feature_ids_json`
  - `bess_cnig_touch_only_feature_ids_json`
  - `bess_cnig_confidence_aggregation_method`
  - `bess_cnig_formal_review_required`
  - `bess_cnig_aggregation_scope`
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
  - `bess_cnig_application_result_sha256`

### `RELATION_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_parcel_relation_role`
  - `bess_cnig_selected_for_parcel_status`
  - `bess_cnig_resulting_parcel_aggregation_status`
  - `bess_cnig_resulting_parcel_precheck_status`
  - `bess_cnig_resulting_parcel_precheck_confidence`
  - `bess_cnig_resulting_parcel_status_priority`

### `_LAST_SOURCE_PARCELS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_LAST_SOURCE_PARCELS: gpd.GeoDataFrame | None = None
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_LAST_APPLICATION_RESULT`

- Category: module constant or closed domain.
- Exact declaration:

```python
_LAST_APPLICATION_RESULT: object | None = None
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

No top-level class/model/dataclass is declared.

## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_aggregation_fixture`

**Purpose:** Implements `aggregation fixture` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[object, ...], object, object, object, object, BessPlanningFeatureParcelAggregationResult]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `inputs, coded, config, policy, application, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_local_corruption_fast_fails_before_heavy_validation` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_local_corruption_fast_fails_before_heavy_validation` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_output_columns_are_rejected_intrinsically` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_output_columns_are_rejected_intrinsically` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_only_application_result_schema_two_is_accepted` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_only_application_result_schema_two_is_accepted` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_application_result_schema_two_remains_accepted` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_application_result_schema_two_remains_accepted` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_persisted_feature_id_json_must_be_portable_and_canonical` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_persisted_feature_id_json_must_be_portable_and_canonical` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_artifact_manifest_corruption_is_rejected` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_artifact_manifest_corruption_is_rejected` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_uses_strict_json_before_artifact_read` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_uses_strict_json_before_artifact_read` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_physical_replacement_is_rejected` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_physical_replacement_is_rejected` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_verified_bytes_are_the_bytes_parsed` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_verified_bytes_are_the_bytes_parsed` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_filenames_are_casefold_unique` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_filenames_are_casefold_unique` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_aggregation_fixture`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_rejects_nonportable_filename` via `_aggregation_fixture`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_rejects_nonportable_filename` via `_aggregation_fixture`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `test_apply_bess_planning_feature_policy._application_fixture` |
| `aggregate_bess_planning_feature_policy_to_parcels` | `landscout.stages.aggregate_bess_planning_feature_policy.aggregate_bess_planning_feature_policy_to_parcels` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `load_bess_planning_feature_parcel_aggregation_artifacts`

**Purpose:** Test adapter supplying the newly mandatory exact upstream envelopes.

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

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `manifest_path` | positional-or-keyword | `str \| Path` | `required` |
| `parcels_path` | positional-or-keyword | `str \| Path` | `required` |
| `relation_assessments_path` | positional-or-keyword | `str \| Path` | `required` |
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame \| None` | `None` |
| `application_result` | positional-or-keyword | `object \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_load_legacy_local_aggregation_artifacts(<br>            manifest_path, parcels_path, relation_assessments_path<br>        )`
  - `_load_aggregation_artifacts(<br>            manifest_path,<br>            parcels_path,<br>            relation_assessments_path,<br>            source_parcels,<br>            application_result,<br>        )`
- Explicit raise paths:
  - `re-raise` under lexical guard `not legacy_synthetic or "unknown feature" not in str(error)`.
- Exact assertions:
  - `assert source_parcels is not None`
  - `assert application_result is not None`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_artifact_manifest_corruption_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_artifact_manifest_corruption_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_uses_strict_json_before_artifact_read` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_uses_strict_json_before_artifact_read` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_physical_replacement_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_physical_replacement_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_verified_bytes_are_the_bytes_parsed` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_verified_bytes_are_the_bytes_parsed` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `load_bess_planning_feature_parcel_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `load_bess_planning_feature_parcel_aggregation_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_load_legacy_local_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._load_legacy_local_aggregation_artifacts` |
| `_load_aggregation_artifacts` | `landscout.stages.aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_load_legacy_local_aggregation_artifacts`

**Purpose:** Exercise pre-2B.5 local-only assertions for retained synthetic fixtures.

**Exact signature**

```python
def _load_legacy_local_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `manifest_path` | positional-or-keyword | `str \| Path` | `required` |
| `parcels_path` | positional-or-keyword | `str \| Path` | `required` |
| `relation_assessments_path` | positional-or-keyword | `str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_load_legacy_local_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_load_legacy_local_aggregation_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `Path(manifest_path).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` |
| `module._read_verified_artifact` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationResult` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path(manifest_path).read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
    payload = loads_strict_json_object(Path(manifest_path).read_bytes())
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_build_from_relations`

**Purpose:** Implements `build from relations` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _build_from_relations(
    relations: pd.DataFrame,
    *,
    parcel_ids: tuple[str, ...] = ("PARCEL-1", "PARCEL-2"),
    canonicalize_application_dtypes: bool = True,
) -> BessPlanningFeatureParcelAggregationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `parcel_ids` | keyword-only | `tuple[str, ...]` | `('PARCEL-1', 'PARCEL-2')` |
| `canonicalize_application_dtypes` | keyword-only | `bool` | `True` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._build_result(parcels, application)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_duplicate_selected_pair_result` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_duplicate_selected_pair_result` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_invalid_lower_feature_id_result` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_invalid_lower_feature_id_result` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_cross_parcel_priority_conflict_result` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_cross_parcel_priority_conflict_result` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_exact_relations_select_configured_max_priority_and_lowest_confidence` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_exact_relations_select_configured_max_priority_and_lowest_confidence` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_policy_unknown_is_exact_but_unresolved_controlling_overrides` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_policy_unknown_is_exact_but_unresolved_controlling_overrides` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_positive_relation_type_controls_without_threshold` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_positive_relation_type_controls_without_threshold` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_boundary_only_relations_are_contextual` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_boundary_only_relations_are_contextual` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_touch_relation_remains_context_beside_a_controlling_relation` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_touch_relation_remains_context_beside_a_controlling_relation` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_is_retained_without_a_decision` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_is_retained_without_a_decision` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_local_cross_table_corruption_is_rejected` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_local_cross_table_corruption_is_rejected` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_inherited_application_relation_domain_is_validated_locally` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_inherited_application_relation_domain_is_validated_locally` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unresolved_relation_cannot_contain_a_decision` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unresolved_relation_cannot_contain_a_decision` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_application_relation_suffix_dtype_is_validated_locally` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_application_relation_suffix_dtype_is_validated_locally` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_status_and_priority_mapping_is_one_to_one_at_every_level` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_status_and_priority_mapping_is_one_to_one_at_every_level` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_parcel_feature_identity_is_rejected_for_every_role` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_parcel_feature_identity_is_rejected_for_every_role` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_relation_parcel_id_is_rejected` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_relation_parcel_id_is_rejected` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_priority_cannot_map_to_two_statuses` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_priority_cannot_map_to_two_statuses` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_status_cannot_map_to_two_priorities` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_status_cannot_map_to_two_priorities` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_complete_five_status_policy_mapping_is_globally_valid` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_complete_five_status_policy_mapping_is_globally_valid` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_selected_relation_role_requires_selected_status_and_priority` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_selected_relation_role_requires_selected_status_and_priority` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_noncanonical_feature_ids_are_rejected` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_noncanonical_feature_ids_are_rejected` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_current_gpu_feature_id_is_canonical` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_current_gpu_feature_id_is_canonical` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_build_from_relations`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_build_from_relations`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_build_from_relations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `test_apply_bess_planning_feature_policy._application_fixture` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pd.Index` | `pandas.Index` |
| `relations.reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.loc[surface_mask, "intersection_area_m2"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_columns` | `landscout.common.planning_feature_schema.relation_columns` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_dtypes` | `landscout.common.planning_feature_schema.relation_dtypes` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `relations[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `importlib.import_module(<br>        "landscout.stages.apply_bess_planning_feature_policy"<br>    )._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._build_result` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `importlib.import_module(<br>        "landscout.stages.apply_bess_planning_feature_policy"<br>    )._result_with_hashes` |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations["parcel_metric_area_m2"] = 4000.0`<br>`relations.loc[surface_mask, "parcel_share_pct"] = (<br>        100.0<br>        * relations.loc[surface_mask, "intersection_area_m2"].astype("float64")<br>        / 4000.0<br>    )`<br>`relations["bess_cnig_policy_profile"] = application.policy_profile`<br>`relations["bess_cnig_policy_sha256"] = application.policy_sha256`<br>`relations["bess_cnig_policy_result_sha256"] = (<br>        application.policy_complete_result_content_sha256<br>    )`<br>`relations[column] = pd.Series(<br>                relations[column].tolist(), index=relations.index, dtype=dtype<br>            )`<br>`relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")` |
| Direct parameter mutation | `relations["parcel_metric_area_m2"] = 4000.0`<br>`relations.loc[surface_mask, "parcel_share_pct"] = (<br>        100.0<br>        * relations.loc[surface_mask, "intersection_area_m2"].astype("float64")<br>        / 4000.0<br>    )`<br>`relations["bess_cnig_policy_profile"] = application.policy_profile`<br>`relations["bess_cnig_policy_sha256"] = application.policy_sha256`<br>`relations["bess_cnig_policy_result_sha256"] = (<br>        application.policy_complete_result_content_sha256<br>    )`<br>`relations[column] = pd.Series(<br>                relations[column].tolist(), index=relations.index, dtype=dtype<br>            )`<br>`relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_relation`

**Purpose:** Implements `relation` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_id` | keyword-only | `str` | `'PARCEL-1'` |
| `feature_id` | keyword-only | `str` | `'F-1'` |
| `relation_type` | keyword-only | `str` | `'AREA_OVERLAP'` |
| `application_status` | keyword-only | `str` | `'APPLIED_EXACT_POLICY'` |
| `status` | keyword-only | `str \| None` | `'MATERIAL_REVIEW_REQUIRED'` |
| `confidence` | keyword-only | `str \| None` | `'HIGH'` |
| `priority` | keyword-only | `int \| None` | `30` |
| `area` | keyword-only | `float` | `1e-06` |

**Return and exception contract**

- Exact observed return expressions:
  - `row`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_duplicate_selected_pair_result` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_duplicate_selected_pair_result` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_invalid_lower_feature_id_result` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_invalid_lower_feature_id_result` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_cross_parcel_priority_conflict_result` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_cross_parcel_priority_conflict_result` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_exact_relations_select_configured_max_priority_and_lowest_confidence` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_exact_relations_select_configured_max_priority_and_lowest_confidence` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_policy_unknown_is_exact_but_unresolved_controlling_overrides` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_policy_unknown_is_exact_but_unresolved_controlling_overrides` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_positive_relation_type_controls_without_threshold` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_positive_relation_type_controls_without_threshold` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_boundary_only_relations_are_contextual` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_boundary_only_relations_are_contextual` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_touch_relation_remains_context_beside_a_controlling_relation` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_touch_relation_remains_context_beside_a_controlling_relation` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_is_retained_without_a_decision` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_is_retained_without_a_decision` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_local_cross_table_corruption_is_rejected` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_local_cross_table_corruption_is_rejected` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_inherited_application_relation_domain_is_validated_locally` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_inherited_application_relation_domain_is_validated_locally` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unresolved_relation_cannot_contain_a_decision` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unresolved_relation_cannot_contain_a_decision` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_application_relation_suffix_dtype_is_validated_locally` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_application_relation_suffix_dtype_is_validated_locally` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_status_and_priority_mapping_is_one_to_one_at_every_level` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_status_and_priority_mapping_is_one_to_one_at_every_level` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_repeated_status_and_priority_mapping_selects_every_exact_match` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_parcel_feature_identity_is_rejected_for_every_role` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_parcel_feature_identity_is_rejected_for_every_role` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_relation_parcel_id_is_rejected` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_relation_parcel_id_is_rejected` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_priority_cannot_map_to_two_statuses` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_priority_cannot_map_to_two_statuses` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_status_cannot_map_to_two_priorities` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_status_cannot_map_to_two_priorities` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_repeated_mapping_and_unresolved_rows_are_valid` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_complete_five_status_policy_mapping_is_globally_valid` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_complete_five_status_policy_mapping_is_globally_valid` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_selected_relation_role_requires_selected_status_and_priority` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_selected_relation_role_requires_selected_status_and_priority` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_noncanonical_feature_ids_are_rejected` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_noncanonical_feature_ids_are_rejected` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_current_gpu_feature_id_is_canonical` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_current_gpu_feature_id_is_canonical` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_relation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_relation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_relation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `test_apply_bess_planning_feature_policy._application_fixture` |
| `application.relations.loc[application.relations["geometry_kind"].eq("LINE")]<br>            .iloc[0]<br>            .to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `application.relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `application.relations.loc[<br>                application.relations["geometry_kind"].eq("SURFACE")<br>            ]<br>            .iloc[0]<br>            .to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `row.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `application.relations.loc[application.relations["geometry_kind"].eq("LINE")]<br>            .iloc[0]<br>            .to_dict`<br>`application.relations["geometry_kind"].eq`<br>`application.relations.loc[<br>                application.relations["geometry_kind"].eq("SURFACE")<br>            ]<br>            .iloc[0]<br>            .to_dict` |
| External process/environment | None directly present. |
| In-memory mutation | `row.update(<br>        parcel_id=parcel_id,<br>        planning_feature_id=feature_id,<br>        relation_type=relation_type,<br>        official_code_status=(<br>            "UNKNOWN_CODE_PAIR"<br>            if application_status == "UNRESOLVED_CODE_PAIR"<br>            else "RESOLVED_OFFICIAL"<br>        ),<br>        bess_cnig_policy_application_status=application_status,<br>        bess_cnig_precheck_status=status,<br>        bess_cnig_precheck_confidence=confidence,<br>        bess_cnig_status_priority=priority,<br>        bess_cnig_rationale=(<br>            None<br>            if application_status == "UNRESOLVED_CODE_PAIR"<br>            else row["bess_cnig_rationale"]<br>        ),<br>        bess_cnig_required_human_action=(<br>            None<br>            if application_status == "UNRESOLVED_CODE_PAIR"<br>            else row["bess_cnig_required_human_action"]<br>        ),<br>        bess_cnig_limitations=(<br>            None<br>            if application_status == "UNRESOLVED_CODE_PAIR"<br>            else row["bess_cnig_limitations"]<br>        ),<br>    )`<br>`row.update(<br>            official_code_label=None,<br>            official_legal_reference=None,<br>            official_regulation_reference=None,<br>            official_code_source_url=None,<br>        )`<br>`row["parcel_metric_area_m2"] = max(float(row["parcel_metric_area_m2"]), area)`<br>`row["feature_area_m2"] = max(float(row["feature_area_m2"]), area)`<br>`row.update(<br>            intersection_area_m2=area,<br>            parcel_share_pct=100.0 * area / float(row["parcel_metric_area_m2"]),<br>            feature_share_pct=100.0 * area / float(row["feature_area_m2"]),<br>        )`<br>`row["source_line_length_m"] = max(float(row["source_line_length_m"]), area)`<br>`row["intersection_length_m"] = area`<br>`row.update(<br>            intersection_area_m2=0.0,<br>            parcel_share_pct=0.0,<br>            feature_share_pct=0.0,<br>        )`<br>`row.update(<br>            geometry_kind="POINT",<br>            feature_area_m2=None,<br>            source_line_length_m=None,<br>            intersection_area_m2=None,<br>            intersection_length_m=None,<br>            parcel_share_pct=None,<br>            feature_share_pct=None,<br>            point_member_count=1,<br>            point_members_inside_count=1 if relation_type == "INSIDE" else 0,<br>            point_members_boundary_count=(0 if relation_type == "INSIDE" else 1),<br>        )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_artifacts`

**Purpose:** Implements `write artifacts` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureParcelAggregationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[Path, dict[str, Path], dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `result` | positional-or-keyword | `BessPlanningFeatureParcelAggregationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `manifest_path, paths, manifest`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_artifact_manifest_corruption_is_rejected` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_artifact_manifest_corruption_is_rejected` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_uses_strict_json_before_artifact_read` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_uses_strict_json_before_artifact_read` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_physical_replacement_is_rejected` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_physical_replacement_is_rejected` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_verified_bytes_are_the_bytes_parsed` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_verified_bytes_are_the_bytes_parsed` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_filenames_are_casefold_unique` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_filenames_are_casefold_unique` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_write_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_rejects_nonportable_filename` via `_write_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_rejects_nonportable_filename` via `_write_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frames.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `records.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `signature.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `fields` | `dataclasses.fields` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes` |
| Filesystem/archive write or publication | `frame.to_parquet`<br>`manifest_path.write_text` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `paths[role] = path`<br>`records.append(<br>            {<br>                "artifact_role": role,<br>                "filename": filename,<br>                "row_count": len(frame),<br>                "size_bytes": len(payload),<br>                "sha256": sha256(payload).hexdigest(),<br>                "frame_schema_signature": signature,<br>                "geospatial": geospatial,<br>                "crs": signature.get("crs"),<br>            }<br>        )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_rehash_coordinated_result`

**Purpose:** Implements `rehash coordinated result` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _rehash_coordinated_result(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureParcelAggregationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(updated)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_duplicate_selected_pair_result` via `_rehash_coordinated_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_duplicate_selected_pair_result` via `_rehash_coordinated_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_invalid_lower_feature_id_result` via `_rehash_coordinated_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_invalid_lower_feature_id_result` via `_rehash_coordinated_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_cross_parcel_priority_conflict_result` via `_rehash_coordinated_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_cross_parcel_priority_conflict_result` via `_rehash_coordinated_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_rehash_coordinated_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `_rehash_coordinated_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_coherent_parcel_area_mutation` via `_rehash_coordinated_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_coherent_parcel_area_mutation` via `_rehash_coordinated_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_rehash_coordinated_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_rehash_coordinated_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_rehash_coordinated_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_validation_uses_reprojected_calculation_copy` via `_rehash_coordinated_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `result.parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relation_assessments.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `module._frame_sha256` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._frame_sha256`<br>`module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `result.parcels.drop(columns=list(PARCEL_COLUMNS))`<br>`result.relation_assessments.drop(columns=list(RELATION_COLUMNS))` |
| Direct parameter mutation | `result.parcels.drop(columns=list(PARCEL_COLUMNS))`<br>`result.relation_assessments.drop(columns=list(RELATION_COLUMNS))` |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_duplicate_selected_pair_result`

**Purpose:** Implements `duplicate selected pair result` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _duplicate_selected_pair_result() -> BessPlanningFeatureParcelAggregationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `_rehash_coordinated_result(<br>        replace(result, parcels=parcels, relation_assessments=relations)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_duplicate_selected_pair_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_duplicate_selected_pair_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_duplicate_selected_pair_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rehash_coordinated_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result` |
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
| In-memory mutation | `relations.loc[relations.index[1], "planning_feature_id"] = "A"`<br>`parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = '["A"]'` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_invalid_lower_feature_id_result`

**Purpose:** Implements `invalid lower feature id result` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _invalid_lower_feature_id_result() -> BessPlanningFeatureParcelAggregationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `_rehash_coordinated_result(replace(result, relation_assessments=relations))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_invalid_lower_feature_id_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_invalid_lower_feature_id_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_invalid_lower_feature_id_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rehash_coordinated_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result` |
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
| In-memory mutation | `relations.loc[relations.index[0], "planning_feature_id"] = "/tmp/feature"` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_cross_parcel_priority_conflict_result`

**Purpose:** Implements `cross parcel priority conflict result` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _cross_parcel_priority_conflict_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `_rehash_coordinated_result(<br>        replace(result, parcels=parcels, relation_assessments=relations)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_cross_parcel_priority_conflict_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_cross_parcel_priority_conflict_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `_cross_parcel_priority_conflict_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["parcel_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["parcel_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rehash_coordinated_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result` |
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
| In-memory mutation | `relations.loc[mask, "bess_cnig_status_priority"] = 50`<br>`relations.loc[mask, "bess_cnig_resulting_parcel_status_priority"] = 50`<br>`parcels.loc[<br>        parcels["parcel_id"].eq("PARCEL-2"), "bess_cnig_parcel_status_priority"<br>    ] = 50` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_surface_touch_semantic_corruption_result`

**Purpose:** Implements `surface touch semantic corruption result` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _surface_touch_semantic_corruption_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `module._build_result(inputs[1], changed_application)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_surface_touch_semantic_corruption_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_surface_touch_semantic_corruption_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `_surface_touch_semantic_corruption_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `_surface_touch_semantic_corruption_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `test_apply_bess_planning_feature_policy._application_fixture` |
| `_surface_touch_with_positive_area` | `test_apply_bess_planning_feature_policy._surface_touch_with_positive_area` |
| `importlib.import_module` | `importlib.import_module` |
| `module._build_result` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `module.validate_bess_application_relation_frame = bypass`<br>`module.validate_bess_application_relation_frame = original` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_surface_touch_semantic_corruption_result.bypass`

**Purpose:** Implements `bypass` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def bypass(*args: object, **kwargs: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
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
def bypass(*args: object, **kwargs: object) -> None:
        return None
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_relations_select_configured_max_priority_and_lowest_confidence`

**Purpose:** Regression invariant: exact relations select configured max priority and lowest confidence. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_relations_select_configured_max_priority_and_lowest_confidence() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel.bess_cnig_parcel_aggregation_status == "AGGREGATED_EXACT_POLICY"`
  - `assert parcel.bess_cnig_parcel_precheck_status == "LIKELY_MATERIAL_CONSTRAINT"`
  - `assert parcel.bess_cnig_parcel_precheck_confidence == "LOW"`
  - `assert parcel.bess_cnig_parcel_status_priority == 50`
  - `assert parcel.bess_cnig_selected_feature_ids_json == '["HIGH-A","HIGH-B"]'`
  - `assert parcel.bess_cnig_distinct_exact_status_count == 2`
  - `assert bool(parcel.bess_cnig_multiple_exact_statuses) is True`
  - `assert parcel.bess_cnig_selected_relation_count == 2`
  - `assert parcel.bess_cnig_lower_priority_controlling_relation_count == 1`
  - `assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [<br>        "LOWER_PRIORITY_CONTROLLING",<br>        "SELECTED_CONTROLLING",<br>        "SELECTED_CONTROLLING",<br>    ]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relation_assessments["bess_cnig_parcel_relation_role"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_unknown_is_exact_but_unresolved_controlling_overrides`

**Purpose:** Regression invariant: policy unknown is exact but unresolved controlling overrides. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_unknown_is_exact_but_unresolved_controlling_overrides() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert exact_unknown.parcels.iloc[0].bess_cnig_parcel_precheck_status == "UNKNOWN"`
  - `assert (<br>        parcel.bess_cnig_parcel_aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR"<br>    )`
  - `assert pd.isna(parcel.bess_cnig_parcel_precheck_status)`
  - `assert pd.isna(parcel.bess_cnig_parcel_precheck_confidence)`
  - `assert pd.isna(parcel.bess_cnig_parcel_status_priority)`
  - `assert parcel.bess_cnig_unresolved_feature_ids_json == '["UNRESOLVED"]'`
  - `assert mixed.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [<br>        "DEFERRED_BY_UNRESOLVED_CONTROLLING",<br>        "UNRESOLVED_CONTROLLING",<br>    ]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pd.isna` | `pandas.isna` |
| `mixed.relation_assessments["bess_cnig_parcel_relation_role"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_positive_relation_type_controls_without_threshold`

**Purpose:** Regression invariant: every positive relation type controls without threshold. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_positive_relation_type_controls_without_threshold(
    relation_type: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("relation_type", ["AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relation_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.iloc[0].bess_cnig_controlling_relation_count == 1`
  - `assert (<br>        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role<br>        == "SELECTED_CONTROLLING"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_boundary_only_relations_are_contextual`

**Purpose:** Regression invariant: boundary only relations are contextual. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_boundary_only_relations_are_contextual(relation_type: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("relation_type", ["TOUCH_ONLY", "BOUNDARY_TOUCH"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relation_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel.bess_cnig_parcel_aggregation_status == "TOUCH_ONLY_RELATIONS_ONLY"`
  - `assert pd.isna(parcel.bess_cnig_parcel_precheck_status)`
  - `assert parcel.bess_cnig_touch_only_feature_ids_json == '["F-1"]'`
  - `assert (<br>        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role<br>        == "TOUCH_ONLY_CONTEXT"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pd.isna` | `pandas.isna` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_touch_relation_remains_context_beside_a_controlling_relation`

**Purpose:** Regression invariant: touch relation remains context beside a controlling relation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_touch_relation_remains_context_beside_a_controlling_relation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.iloc[0].bess_cnig_parcel_precheck_status == (<br>        "MATERIAL_REVIEW_REQUIRED"<br>    )`
  - `assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [<br>        "SELECTED_CONTROLLING",<br>        "TOUCH_ONLY_CONTEXT",<br>    ]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.relation_assessments["bess_cnig_parcel_relation_role"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_relation_parcel_is_retained_without_a_decision`

**Purpose:** Regression invariant: no relation parcel is retained without a decision. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_relation_parcel_is_retained_without_a_decision() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert parcel.bess_cnig_parcel_aggregation_status == "NO_PLANNING_FEATURE_RELATION"`
  - `assert pd.isna(parcel.bess_cnig_parcel_precheck_status)`
  - `assert bool(parcel.bess_cnig_formal_review_required) is True`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pd.isna` | `pandas.isna` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_no_relation_parcel_is_retained_without_a_decision() -> None:
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcel = result.parcels.iloc[1]
    assert parcel.bess_cnig_parcel_aggregation_status == "NO_PLANNING_FEATURE_RELATION"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert bool(parcel.bess_cnig_formal_review_required) is True
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`

**Purpose:** Regression invariant: parcel and relation prefixes order and inputs are preserved. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_and_relation_prefixes_order_and_inputs_are_preserved() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) == PARCEL_COLUMNS`
  - `assert (<br>        tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])<br>        == RELATION_COLUMNS<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_application_fixture` | `test_apply_bess_planning_feature_policy._application_fixture` |
| `inputs[1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `application.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `aggregate_bess_planning_feature_policy_to_parcels` | `landscout.stages.aggregate_bess_planning_feature_policy.aggregate_bess_planning_feature_policy_to_parcels` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_local_corruption_fast_fails_before_heavy_validation`

**Purpose:** Regression invariant: local corruption fast fails before heavy validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_local_corruption_fast_fails_before_heavy_validation(
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |

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
| In-memory mutation | `parcels.loc[parcels.index[0], "bess_cnig_selected_relation_count"] = 999` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_local_corruption_fast_fails_before_heavy_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_coordinated_local_cross_table_corruption_is_rejected`

**Purpose:** Regression invariant: coordinated local cross table corruption is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_local_cross_table_corruption_is_rejected(
    frame_name: str,
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("frame_name", "column", "value"),
    [
        ("parcels", "bess_cnig_selected_relation_count", 999),
        ("parcels", "bess_cnig_parcel_precheck_status", "UNKNOWN"),
        ("parcels", "bess_cnig_parcel_status_priority", 999),
        ("parcels", "bess_cnig_parcel_precheck_confidence", "LOW"),
        ("parcels", "bess_cnig_selected_feature_ids_json", "[]"),
        (
            "relation_assessments",
            "bess_cnig_parcel_relation_role",
            "TOUCH_ONLY_CONTEXT",
        ),
        ("relation_assessments", "parcel_id", "PARCEL-OTHER"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame_name` | positional-or-keyword | `str` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
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
| In-memory mutation | `frame.loc[frame.index[0], column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_output_dtype_and_non_2d_parcel_fail_locally`

**Purpose:** Regression invariant: invalid output dtype and non 2d parcel fail locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_output_dtype_and_non_2d_parcel_fail_locally() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype")`
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="2D")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[<br>        "bess_cnig_selected_relation_count"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations[<br>        "bess_cnig_selected_for_parcel_status"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `Polygon` | `shapely.geometry.Polygon` |

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
| In-memory mutation | `parcels["bess_cnig_selected_relation_count"] = parcels[<br>        "bess_cnig_selected_relation_count"<br>    ].astype("object")`<br>`relations["bess_cnig_selected_for_parcel_status"] = relations[<br>        "bess_cnig_selected_for_parcel_status"<br>    ].astype("object")`<br>`parcels.at[parcels.index[0], parcels.geometry.name] = Polygon(<br>        [(x, y, 5) for x, y in geometry.exterior.coords]<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_inherited_application_relation_domain_is_validated_locally`

**Purpose:** Regression invariant: every inherited application relation domain is validated locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(status="AUTHORIZED")]),
        pd.DataFrame([_relation(status="FORBIDDEN")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="PROHIBITED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    confidence="CERTAIN",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    relation_type="TOUCH_ONLY",
                    application_status="INVALID_APPLICATION_STATUS",
                )
            ]
        ),
    ],
    ids=[
        "selected-authorized",
        "selected-forbidden",
        "lower-prohibited",
        "lower-certain-confidence",
        "contextual-invalid-application-status",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |

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
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(relations)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unresolved_relation_cannot_contain_a_decision`

**Purpose:** Regression invariant: unresolved relation cannot contain a decision. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unresolved_relation_cannot_contain_a_decision() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |

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
| In-memory mutation | `row["official_code_status"] = "UNKNOWN_CODE_PAIR"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_all_application_identity_scope_and_boundary_fields_are_intrinsic`

**Purpose:** Regression invariant: all application identity scope and boundary fields are intrinsic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("feature_family", "OTHER"),
        ("type_code_raw", "7"),
        ("subtype_code_raw", "AA"),
        ("bess_cnig_application_scope", "WRONG_SCOPE"),
        ("bess_cnig_local_feature_text_interpreted", True),
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
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
| In-memory mutation | `row[column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
    row = _relation(relation_type="TOUCH_ONLY")
    row[column] = value
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_relation_suffix_dtype_is_validated_locally`

**Purpose:** Regression invariant: application relation suffix dtype is validated locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_relation_suffix_dtype_is_validated_locally() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `relations[<br>        "bess_cnig_precheck_status"<br>    ].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |

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
| In-memory mutation | `relations["bess_cnig_precheck_status"] = relations[<br>        "bess_cnig_precheck_status"<br>    ].astype("category")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_application_relation_suffix_dtype_is_validated_locally() -> None:
    relations = pd.DataFrame([_relation()])
    relations["bess_cnig_precheck_status"] = relations[
        "bess_cnig_precheck_status"
    ].astype("category")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        _build_from_relations(relations, canonicalize_application_dtypes=False)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_status_and_priority_mapping_is_one_to_one_at_every_level`

**Purpose:** Regression invariant: status and priority mapping is one to one at every level. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="MAX",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="LOW-A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW-B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=10,
                ),
            ]
        ),
    ],
    ids=[
        "same-maximum-priority-two-statuses",
        "same-lower-priority-two-statuses",
        "same-status-two-priorities",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |

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
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority"):
        _build_from_relations(relations)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

**Purpose:** Regression invariant: valid repeated status and priority mapping selects every exact match. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_repeated_status_and_priority_mapping_selects_every_exact_match() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.iloc[0].bess_cnig_selected_relation_count == 2`
  - `assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [<br>        "SELECTED_CONTROLLING",<br>        "SELECTED_CONTROLLING",<br>    ]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.relation_assessments["bess_cnig_parcel_relation_role"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_feature_identity_is_rejected_for_every_role`

**Purpose:** Regression invariant: duplicate parcel feature identity is rejected for every role. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(feature_id="A"), _relation(feature_id="A")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="DEFERRED"),
                _relation(feature_id="DEFERRED"),
                _relation(
                    feature_id="UNRESOLVED",
                    application_status="UNRESOLVED_CODE_PAIR",
                    status=None,
                    confidence=None,
                    priority=None,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="A", relation_type="AREA_OVERLAP"),
                _relation(feature_id="A", relation_type="LENGTH_OVERLAP"),
            ]
        ),
    ],
    ids=[
        "selected",
        "lower-priority",
        "contextual",
        "deferred",
        "different-relation-types",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="duplicate\|unique"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |

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
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="duplicate|unique"
    ):
        _build_from_relations(relations)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`

**Purpose:** Regression invariant: invalid lower priority feature id is rejected independently of json role. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role(
    feature_id: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature"],
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
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="feature\|identity"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`

**Purpose:** Regression invariant: invalid deferred feature id is rejected independently of json role. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_deferred_feature_id_is_rejected_independently_of_json_role(
    feature_id: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("feature_id", [r"C:\feature", " GPU:F "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `feature_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="feature\|identity"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_relation_parcel_id_is_rejected`

**Purpose:** Regression invariant: invalid relation parcel id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("parcel_id", [None, " PARCEL-1 "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_id` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="parcel\|identity"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
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
| In-memory mutation | `relation["parcel_id"] = parcel_id` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
    relation = _relation()
    relation["parcel_id"] = parcel_id
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel|identity"
    ):
        _build_from_relations(pd.DataFrame([relation]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_relation_type_is_rejected_by_shared_relation_contract`

**Purpose:** Regression invariant: unknown relation type is rejected by shared relation contract. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="relation type"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |

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
def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="relation type"
    ):
        _build_from_relations(pd.DataFrame([_relation(relation_type="NEARBY")]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_document_wide_same_priority_cannot_map_to_two_statuses`

**Purpose:** Regression invariant: document wide same priority cannot map to two statuses. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_document_wide_same_priority_cannot_map_to_two_statuses(
    context_type: str | None,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("context_type", [None, "TOUCH_ONLY", "BOUNDARY_TOUCH"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `context_type` | positional-or-keyword | `str \| None` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="priority\|mapping"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_document_wide_same_status_cannot_map_to_two_priorities`

**Purpose:** Regression invariant: document wide same status cannot map to two priorities. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_document_wide_same_status_cannot_map_to_two_priorities() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="priority\|mapping"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`

**Purpose:** Regression invariant: document wide repeated mapping and unresolved rows are valid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_document_wide_repeated_mapping_and_unresolved_rows_are_valid() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.relation_assessments) == 3`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_five_status_policy_mapping_is_globally_valid`

**Purpose:** Regression invariant: complete five status policy mapping is globally valid. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_complete_five_status_policy_mapping_is_globally_valid() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.relation_assessments) == 5`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_selected_relation_role_requires_selected_status_and_priority`

**Purpose:** Regression invariant: selected relation role requires selected status and priority. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_selected_relation_role_requires_selected_status_and_priority() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `relations.loc[relations.index[0], "bess_cnig_parcel_relation_role"] = (<br>        "SELECTED_CONTROLLING"<br>    )`<br>`relations.loc[relations.index[0], "bess_cnig_selected_for_parcel_status"] = True` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_validate_parcel_geometries`

**Purpose:** Implements `validate parcel geometries` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _validate_parcel_geometries(geometries: list[object]) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometries` | positional-or-keyword | `list[object]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_malformed_parcel_geometry_is_rejected_intrinsically` via `_validate_parcel_geometries`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_malformed_parcel_geometry_is_rejected_intrinsically` via `_validate_parcel_geometries`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_polygon_and_multipolygon_parcels_are_accepted` via `_validate_parcel_geometries`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_polygon_and_multipolygon_parcels_are_accepted` via `_validate_parcel_geometries`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_application_fixture` | `test_apply_bess_planning_feature_policy._application_fixture` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `range` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._build_result` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_parcel_geometry_is_rejected_intrinsically`

**Purpose:** Regression invariant: malformed parcel geometry is rejected intrinsically. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "geometry",
    [
        Point(0, 0),
        LineString([(0, 0), (1, 1)]),
        Polygon(),
        Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        None,
    ],
    ids=["point", "line", "empty", "invalid", "null"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_validate_parcel_geometries` | `tests.unit.test_aggregate_bess_planning_feature_policy._validate_parcel_geometries` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Point` | `shapely.geometry.Point` |
| `LineString` | `shapely.geometry.LineString` |
| `Polygon` | `shapely.geometry.Polygon` |

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
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _validate_parcel_geometries([geometry])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_polygon_and_multipolygon_parcels_are_accepted`

**Purpose:** Regression invariant: valid polygon and multipolygon parcels are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `_validate_parcel_geometries` | `tests.unit.test_aggregate_bess_planning_feature_policy._validate_parcel_geometries` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |

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
def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
    polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
    _validate_parcel_geometries([polygon, MultiPolygon([polygon])])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_output_columns_are_rejected_intrinsically`

**Purpose:** Regression invariant: duplicate output columns are rejected intrinsically. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_output_columns_are_rejected_intrinsically(frame_name: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("frame_name", ["parcels", "relation_assessments"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame_name` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
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
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_only_application_result_schema_two_is_accepted`

**Purpose:** Regression invariant: only application result schema two is accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_only_application_result_schema_two_is_accepted(version: int) -> None:
```

- Exact decorators: `pytest.mark.parametrize("version", [1, 3, 999])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="application.*schema"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_application_result_schema_two_remains_accepted`

**Purpose:** Regression invariant: application result schema two remains accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_application_result_schema_two_remains_accepted() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.application_result_hash_schema_version == 2`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
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
def test_application_result_schema_two_remains_accepted() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    assert result.application_result_hash_schema_version == 2
    module._validate_result_envelope(result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_noncanonical_feature_ids_are_rejected`

**Purpose:** Regression invariant: noncanonical feature ids are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "feature_id",
    ["None", "nan", "<NA>", "/tmp/feature", r"C:\feature", " GPU:F "],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `feature_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
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
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID"):
        _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_current_gpu_feature_id_is_canonical`

**Purpose:** Regression invariant: current gpu feature id is canonical. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_current_gpu_feature_id_is_canonical() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == (<br>        f'["{feature_id}"]'<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |

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
def test_current_gpu_feature_id_is_canonical() -> None:
    feature_id = "GPU:DOC:prescription_surface:FEATURE-01"
    result = _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
    assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == (
        f'["{feature_id}"]'
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_authorized_status_artifact_fails_local_verified_byte_loading`

**Purpose:** Regression invariant: authorized status artifact fails local verified byte loading. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_authorized_status_artifact_fails_local_verified_byte_loading(
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `assessed.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `module._frame_sha256` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `module._frame_sha256`<br>`module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `parcels.loc[parcels.index[0], "bess_cnig_parcel_precheck_status"] = "AUTHORIZED"`<br>`assessed.loc[assessed.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"`<br>`assessed.loc[assessed.index[0], "bess_cnig_resulting_parcel_precheck_status"] = (<br>        "AUTHORIZED"<br>    )`<br>`assessed.drop(columns=list(RELATION_COLUMNS))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_relation_identity_artifact_corruption_fails_locally`

**Purpose:** Regression invariant: coordinated relation identity artifact corruption fails locally. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_relation_identity_artifact_corruption_fails_locally(
    tmp_path: Path,
    factory: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "factory",
    [
        _duplicate_selected_pair_result,
        _invalid_lower_feature_id_result,
        _cross_parcel_priority_conflict_result,
    ],
    ids=["duplicate-pair", "invalid-lower-feature-id", "global-priority-conflict"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `factory` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`
- Exact assertions:
  - `assert callable(factory)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `callable` | `unresolved local/third-party receiver; no ownership inferred` |
| `factory` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`

**Purpose:** Regression invariant: controlling relation cannot be relabelled contextual in artifact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_controlling_relation_cannot_be_relabelled_contextual_in_artifact(
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
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="surface\|metric\|type"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_surface_touch_semantic_corruption_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._surface_touch_semantic_corruption_result` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_relation_parcel_rejects_textual_null_identity`

**Purpose:** Regression invariant: no relation parcel rejects textual null identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_relation_parcel_rejects_textual_null_identity(
    tmp_path: Path, parcel_id: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("parcel_id", ["None", "nan", "<NA>"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `parcel_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="parcel ID")`
- Exact assertions:
  - `assert no_relation.any()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels["bess_cnig_parcel_aggregation_status"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `no_relation.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `parcels["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `gpd.read_parquet` | `geopandas.read_parquet` |
| `pd.read_parquet` | `pandas.read_parquet` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `manifest.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_parquet`<br>`pd.read_parquet` |
| Filesystem/archive write or publication | `manifest.write_text` |
| Hashing/byte identity | `module._result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `parcels.loc[parcels.index[no_relation][0], "parcel_id"] = parcel_id`<br>`parcels["parcel_id"] = pd.array(<br>        parcels["parcel_id"].tolist(), dtype=parcel_id_dtype<br>    )`<br>`record["frame_schema_signature"] = deterministic_frame_schema_signature(<br>                persisted_parcels<br>            )`<br>`record["frame_schema_signature"] = deterministic_frame_schema_signature(<br>                persisted_relations<br>            )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_identity_and_global_mapping_fail_before_heavy_validation`

**Purpose:** Regression invariant: relation identity and global mapping fail before heavy validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_identity_and_global_mapping_fail_before_heavy_validation(
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_duplicate_selected_pair_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._duplicate_selected_pair_result` |
| `_invalid_lower_feature_id_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._invalid_lower_feature_id_result` |
| `_cross_parcel_priority_conflict_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._cross_parcel_priority_conflict_result` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_identity_and_global_mapping_fail_before_heavy_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_relation_semantic_failure_fast_fails_before_heavy_validation`

**Purpose:** Regression invariant: relation semantic failure fast fails before heavy validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_semantic_failure_fast_fails_before_heavy_validation(
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |
| `_surface_touch_semantic_corruption_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._surface_touch_semantic_corruption_result` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_semantic_failure_fast_fails_before_heavy_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_parcel_decision_status_domain_rejects_forbidden_vocabulary`

**Purpose:** Regression invariant: parcel decision status domain rejects forbidden vocabulary. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_decision_status_domain_rejects_forbidden_vocabulary(
    status: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "status",
    [
        "ALLOWED",
        "AUTHORIZED",
        "COMPATIBLE",
        "CLEAR",
        "FORBIDDEN",
        "PROHIBITED",
        "BLOCKED",
        "BUILDABLE",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="status")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `parcels.loc[decision_index, "bess_cnig_parcel_precheck_status"] = status` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_persisted_feature_id_json_must_be_portable_and_canonical`

**Purpose:** Regression invariant: persisted feature id json must be portable and canonical. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_persisted_feature_id_json_must_be_portable_and_canonical(
    json_value: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "json_value",
    [
        '["None"]',
        '["nan"]',
        '["<NA>"]',
        '["/tmp/feature"]',
        r'["C:\\feature"]',
        '[" GPU:F "]',
        '["B","A"]',
        '["A", "B"]',
        '["A","A"]',
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `json_value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = json_value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_representative_intrinsic_failures_all_precede_heavy_validation`

**Purpose:** Regression invariant: representative intrinsic failures all precede heavy validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_representative_intrinsic_failures_all_precede_heavy_validation(
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `invalid_results.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rehash_coordinated_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result` |
| `replace` | `dataclasses.replace` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `ambiguous.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `Point` | `shapely.geometry.Point` |
| `pd.concat` | `pandas.concat` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |

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
| In-memory mutation | `inherited.loc[inherited.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"`<br>`invalid_results.append(<br>        _rehash_coordinated_result(replace(result, relation_assessments=inherited))<br>    )`<br>`parcel_status.loc[parcel_status.index[0], "bess_cnig_parcel_precheck_status"] = (<br>        "AUTHORIZED"<br>    )`<br>`invalid_results.append(<br>        module._result_with_hashes(replace(result, parcels=parcel_status))<br>    )`<br>`ambiguous_relations.loc[<br>        ambiguous_relations.index[1], "bess_cnig_status_priority"<br>    ] = 50`<br>`invalid_results.append(<br>        _rehash_coordinated_result(<br>            replace(ambiguous, relation_assessments=ambiguous_relations)<br>        )<br>    )`<br>`point_parcels.at[point_parcels.index[0], point_parcels.geometry.name] = Point(0, 0)`<br>`invalid_results.append(replace(result, parcels=point_parcels))`<br>`invalid_results.append(<br>        replace(<br>            result,<br>            parcels=gpd.GeoDataFrame(<br>                duplicate,<br>                geometry=result.parcels.geometry.name,<br>                crs=result.parcels.crs,<br>            ),<br>        )<br>    )`<br>`invalid_results.append(<br>        module._result_with_hashes(<br>            replace(result, application_result_hash_schema_version=3)<br>        )<br>    )`<br>`json_parcels.loc[json_parcels.index[0], "bess_cnig_selected_feature_ids_json"] = (<br>        '["/tmp/feature"]'<br>    )`<br>`invalid_results.append(<br>        module._result_with_hashes(replace(result, parcels=json_parcels))<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_representative_intrinsic_failures_all_precede_heavy_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_one_aggregation_and_one_public_validation_each_call_heavy_once`

**Purpose:** Regression invariant: one aggregation and one public validation each call heavy once. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_one_aggregation_and_one_public_validation_each_call_heavy_once(
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
| `_application_fixture` | `test_apply_bess_planning_feature_policy._application_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.aggregate_bess_planning_feature_policy_to_parcels` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.validate_bess_planning_feature_parcel_aggregation_result` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_one_aggregation_and_one_public_validation_each_call_heavy_once.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_valid_two_file_verified_byte_artifacts_and_source_readback`

**Purpose:** Regression invariant: valid two file verified byte artifacts and source readback. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_two_file_verified_byte_artifacts_and_source_readback(
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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_manifest_corruption_is_rejected`

**Purpose:** Regression invariant: artifact manifest corruption is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_manifest_corruption_is_rejected(
    tmp_path: Path, mutation: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        lambda value: value.update(schema_version=2),
        lambda value: value.update(application_result_hash_schema_version=1),
        lambda value: value.update(application_result_hash_schema_version=3),
        lambda value: value.update(application_result_hash_schema_version=999),
        lambda value: value["artifacts"].pop(),
        lambda value: value["artifacts"].append(
            {**value["artifacts"][0], "artifact_role": "EXTRA"}
        ),
        lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
        lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
        lambda value: value["artifacts"][1].update(
            filename=value["artifacts"][0]["filename"]
        ),
        lambda value: value["artifacts"][0].update(filename="C:/absolute.parquet"),
        lambda value: value["artifacts"][0].update(size_bytes=1),
        lambda value: value["artifacts"][0].update(sha256="f" * 64),
        lambda value: value["artifacts"][0].update(sha256="bad"),
        lambda value: value["artifacts"][0].update(row_count=999),
        lambda value: value["artifacts"][0]["frame_schema_signature"].update(
            index_names=["wrong"]
        ),
        lambda value: value["artifacts"][0].update(crs=None),
        lambda value: value["artifacts"][0].update(crs={"wrong": True}),
        lambda value: value["artifacts"][0].update(geospatial=False),
        lambda value: value.update(unknown=True),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`
- Exact assertions:
  - `assert callable(mutation)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `callable` | `unresolved local/third-party receiver; no ownership inferred` |
| `mutation` | `unresolved local/third-party receiver; no ownership inferred` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_aggregation_manifest_uses_strict_json_before_artifact_read`

**Purpose:** Regression invariant: aggregation manifest uses strict json before artifact read. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_aggregation_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "document",
    [
        '{"schema_version":1,"schema_version":1}',
        '{"schema_version":NaN}',
        '{"schema_version":Infinity}',
        "[]",
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
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError,<br>        match="Duplicate JSON\|finite\|top-level\|invalid",<br>    )`
- Exact assertions:
  - `assert artifact_reads == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
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
def test_aggregation_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
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
        BessPlanningFeatureParcelAggregationError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
    assert artifact_reads == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_aggregation_manifest_uses_strict_json_before_artifact_read.counted_bytes`

**Purpose:** Implements `counted bytes` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_aggregation_manifest_uses_strict_json_before_artifact_read.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_aggregation_physical_replacement_is_rejected`

**Purpose:** Regression invariant: aggregation physical replacement is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_aggregation_physical_replacement_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="size\|SHA")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `paths["RELATION_ASSESSMENTS"].write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `paths["RELATION_ASSESSMENTS"].read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `paths["RELATION_ASSESSMENTS"].read_bytes` |
| Filesystem/archive write or publication | `paths["RELATION_ASSESSMENTS"].write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_aggregation_physical_replacement_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    paths["RELATION_ASSESSMENTS"].write_bytes(
        paths["RELATION_ASSESSMENTS"].read_bytes() + b"tamper"
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="size|SHA"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_verified_bytes_are_the_bytes_parsed`

**Purpose:** Regression invariant: verified bytes are the bytes parsed. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_verified_bytes_are_the_bytes_parsed(
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
  - `assert verified in observed`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `target.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relation_assessments.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `replacement.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `target.read_bytes`<br>`replacement.read_bytes` |
| Filesystem/archive write or publication | `result.relation_assessments.to_parquet` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_verified_bytes_are_the_bytes_parsed.replace_after_read`

**Purpose:** Implements `replace after read` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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
        payload = original_read_bytes(path)
        if path == target:
            path.write_bytes(replacement_bytes)
        return payload
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_verified_bytes_are_the_bytes_parsed.inspect_read`

**Purpose:** Implements `inspect read` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def inspect_read(source: object, *args: object, **kwargs: object) -> object:
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
  - `original_read(source, *args, **kwargs)`
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
| `original_read` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `observed.append(source.getvalue())` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def inspect_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(source.getvalue())
        return original_read(source, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_public_exports_are_stable`

**Purpose:** Regression invariant: public exports are stable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_exports_are_stable() -> None:
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

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.issubset` | `unresolved local/third-party receiver; no ownership inferred` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_coherent_parcel_area_mutation`

**Purpose:** Implements `coherent parcel area mutation` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _coherent_parcel_area_mutation(
    result: BessPlanningFeatureParcelAggregationResult,
    geometry_kind: str,
) -> BessPlanningFeatureParcelAggregationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureParcelAggregationResult` | `required` |
| `geometry_kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_rehash_coordinated_result(replace(result, relation_assessments=relations))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_coherent_parcel_area_mutation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `_coherent_parcel_area_mutation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_coherent_parcel_area_mutation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `_coherent_parcel_area_mutation`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_coherent_parcel_area_mutation`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `_coherent_parcel_area_mutation`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.relation_assessments.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rehash_coordinated_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[index, "parcel_metric_area_m2"] = 8000.0`<br>`relations.loc[index, "parcel_share_pct"] = (<br>            100.0 * float(relations.loc[index, "intersection_area_m2"]) / 8000.0<br>        )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_parcel_area_is_bound_to_real_parcel_geometry`

**Purpose:** Regression invariant: relation parcel area is bound to real parcel geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_parcel_area_is_bound_to_real_parcel_geometry(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("LINE", "LENGTH_OVERLAP"),
        ("POINT", "INSIDE"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry_kind` | positional-or-keyword | `str` | `required` |
| `relation_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="parcel.*area\|area.*parcel"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `_coherent_parcel_area_mutation` | `tests.unit.test_aggregate_bess_planning_feature_policy._coherent_parcel_area_mutation` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_self_consistent_parcel_area_artifact_is_rejected`

**Purpose:** Regression invariant: self consistent parcel area artifact is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_self_consistent_parcel_area_artifact_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="parcel.*area\|area.*parcel"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `_coherent_parcel_area_mutation` | `tests.unit.test_aggregate_bess_planning_feature_policy._coherent_parcel_area_mutation` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `gpd.read_parquet` | `geopandas.read_parquet` |
| `pd.read_parquet` | `pandas.read_parquet` |
| `_rehash_coordinated_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result` |
| `replace` | `dataclasses.replace` |
| `fields` | `dataclasses.fields` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `manifest.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_parquet`<br>`pd.read_parquet` |
| Filesystem/archive write or publication | `manifest.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload[field.name] = getattr(persisted_result, field.name)`<br>`record["frame_schema_signature"] = deterministic_frame_schema_signature(<br>            persisted[record["artifact_role"]]<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_area_validation_uses_reprojected_calculation_copy`

**Purpose:** Regression invariant: parcel area validation uses reprojected calculation copy. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_area_validation_uses_reprojected_calculation_copy() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `result.parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rehash_coordinated_result` | `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result` |
| `replace` | `dataclasses.replace` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `result.parcels.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_area_defect_fast_fails_before_application_source_validation`

**Purpose:** Regression invariant: parcel area defect fast fails before application source validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_area_defect_fast_fails_before_application_source_validation(
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError)`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `_build_from_relations` | `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_relation` | `tests.unit.test_aggregate_bess_planning_feature_policy._relation` |
| `_coherent_parcel_area_mutation` | `tests.unit.test_aggregate_bess_planning_feature_policy._coherent_parcel_area_mutation` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_area_defect_fast_fails_before_application_source_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams`

**Purpose:** Regression invariant: step 7d 5b 2b 5 aggregation loader requires exact upstreams. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(<br>        inspect.signature(<br>            module.load_bess_planning_feature_parcel_aggregation_artifacts<br>        ).parameters<br>    ) == (<br>        "manifest_path",<br>        "parcels_path",<br>        "relation_assessments_path",<br>        "source_parcels",<br>        "application_result",<br>    )`
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`

**Purpose:** Regression invariant: source bound aggregation loader accepts only supplied upstreams. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_aggregation_loader_accepts_only_supplied_upstreams(
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
- Exact assertions:
  - `assert (<br>        loaded.complete_result_content_sha256 == result.complete_result_content_sha256<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_aggregation_manifest_filenames_are_casefold_unique`

**Purpose:** Regression invariant: aggregation manifest filenames are casefold unique. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_aggregation_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
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
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `str(<br>        payload["artifacts"][0]["filename"]<br>    ).upper` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` |

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
def test_aggregation_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_changed_parcel_geometry_upstreams`

**Purpose:** Implements `changed parcel geometry upstreams` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _changed_parcel_geometry_upstreams(
    source_parcels: gpd.GeoDataFrame,
    application: object,
) -> tuple[gpd.GeoDataFrame, object]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[gpd.GeoDataFrame, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `application` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `changed_parcels, changed_application`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_changed_parcel_geometry_upstreams`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_changed_parcel_geometry_upstreams`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `source_parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `changed_parcels["parcel_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `affinity.scale` | `shapely.affinity.scale` |
| `changed_parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `application.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["parcel_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.loc[surface, "intersection_area_m2"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `application_module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `application_module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `application_module._result_with_hashes` |
| CRS/geometry/spatial calculation | `changed_parcels.to_crs`<br>`relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `changed_parcels.loc[parcel_index, geometry_column] = affinity.scale(<br>        geometry, xfact=2.0, yfact=2.0, origin="centroid"<br>    )`<br>`relations.loc[mask, "parcel_metric_area_m2"] = float(metric)`<br>`relations.loc[surface, "parcel_share_pct"] = (<br>        100.0<br>        * relations.loc[surface, "intersection_area_m2"].astype("float64")<br>        / float(metric)<br>    )` |
| Direct parameter mutation | None directly present. |

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

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`

**Purpose:** Regression invariant: source bound aggregation loader rejects coordinated upstream changes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        "parcel_geometry",
        "parcel_crs",
        "application_relation",
        "parcel_order",
        "unrelated_parcel_geometry",
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
  - `pytest.raises(BessPlanningFeatureParcelAggregationError, match="source lock")`
- Exact assertions:
  - `assert not available.empty`
  - `assert heavy_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `source_parcels.iloc[[0]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `extra.geometry.map` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_parcels.index.max` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pd.concat` | `pandas.concat` |
| `source_parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_changed_parcel_geometry_upstreams` | `tests.unit.test_aggregate_bess_planning_feature_policy._changed_parcel_geometry_upstreams` |
| `source_parcels.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `_coordinated_policy_mutation` | `test_apply_bess_planning_feature_policy._coordinated_policy_mutation` |
| `source_parcels.iloc[::-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `changed_parcels["parcel_id"].isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `affinity.translate` | `shapely.affinity.translate` |
| `importlib.import_module` | `importlib.import_module` |
| `module._build_result` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._validate_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_parcel_aggregation_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `extra.geometry.map`<br>`_changed_parcel_geometry_upstreams`<br>`source_parcels.to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `extra["parcel_id"] = pd.array(["NO-RELATION-PARCEL"], dtype="str")`<br>`extra.geometry = extra.geometry.map(<br>            lambda geometry: affinity.translate(geometry, xoff=10_000.0)<br>        )`<br>`extra.index = pd.Index(<br>            [int(source_parcels.index.max()) + 1],<br>            dtype=source_parcels.index.dtype,<br>            name=source_parcels.index.name,<br>        )`<br>`changed_parcels.loc[index, changed_parcels.geometry.name] = affinity.translate(<br>            changed_parcels.loc[index, changed_parcels.geometry.name], xoff=1.0<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes.forbidden_heavy`

**Purpose:** Implements `forbidden heavy` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`

**Purpose:** Regression invariant: source bound aggregation loader rebuilds once without mutating upstreams. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams(
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
  - `assert build_calls == 1`
  - `assert heavy_calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `source_parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `application.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.load_bess_planning_feature_parcel_aggregation_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.counted_build`

**Purpose:** Implements `counted build` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def counted_build(*args: object, **kwargs: object) -> object:
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def counted_build(*args: object, **kwargs: object) -> object:
        nonlocal build_calls
        build_calls += 1
        return actual_build(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.forbidden_heavy`

**Purpose:** Implements `forbidden heavy` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_aggregation_loader_rejects_bad_application_before_artifact_reads`

**Purpose:** Regression invariant: aggregation loader rejects bad application before artifact reads. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_aggregation_loader_rejects_bad_application_before_artifact_reads(
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
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_load_aggregation_artifacts` | `landscout.stages.aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |

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

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_aggregation_loader_rejects_bad_application_before_artifact_reads.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `aggregate_bess_planning_feature_policy` contracts exercised in this file.

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

### `test_aggregation_manifest_rejects_nonportable_filename`

**Purpose:** Regression invariant: aggregation manifest rejects nonportable filename. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_aggregation_manifest_rejects_nonportable_filename(
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
| `_aggregation_fixture` | `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture` |
| `_write_artifacts` | `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` |
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
def test_aggregation_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **60**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_exact_relations_select_configured_max_priority_and_lowest_confidence` | none | none | 10 | Proves exact relations select configured max priority and lowest confidence using the exact source reproduced in section 7. |
| `test_policy_unknown_is_exact_but_unresolved_controlling_overrides` | none | none | 7 | Proves policy unknown is exact but unresolved controlling overrides using the exact source reproduced in section 7. |
| `test_every_positive_relation_type_controls_without_threshold` | pytest.mark.parametrize("relation_type", ["AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"]) | none | 2 | Proves every positive relation type controls without threshold using the exact source reproduced in section 7. |
| `test_boundary_only_relations_are_contextual` | pytest.mark.parametrize("relation_type", ["TOUCH_ONLY", "BOUNDARY_TOUCH"]) | none | 4 | Proves boundary only relations are contextual using the exact source reproduced in section 7. |
| `test_touch_relation_remains_context_beside_a_controlling_relation` | none | none | 2 | Proves touch relation remains context beside a controlling relation using the exact source reproduced in section 7. |
| `test_no_relation_parcel_is_retained_without_a_decision` | none | none | 3 | Proves no relation parcel is retained without a decision using the exact source reproduced in section 7. |
| `test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` | none | none | 2 | Proves parcel and relation prefixes order and inputs are preserved using the exact source reproduced in section 7. |
| `test_local_corruption_fast_fails_before_heavy_validation` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 1 | Proves local corruption fast fails before heavy validation using the exact source reproduced in section 7. |
| `test_coordinated_local_cross_table_corruption_is_rejected` | pytest.mark.parametrize(<br>    ("frame_name", "column", "value"),<br>    [<br>        ("parcels", "bess_cnig_selected_relation_count", 999),<br>        ("parcels", "bess_cnig_parcel_precheck_status", "UNKNOWN"),<br>        ("parcels", "bess_cnig_parcel_status_priority", 999),<br>        ("parcels", "bess_cnig_parcel_precheck_confidence", "LOW"),<br>        ("parcels", "bess_cnig_selected_feature_ids_json", "[]"),<br>        (<br>            "relation_assessments",<br>            "bess_cnig_parcel_relation_role",<br>            "TOUCH_ONLY_CONTEXT",<br>        ),<br>        ("relation_assessments", "parcel_id", "PARCEL-OTHER"),<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves coordinated local cross table corruption is rejected using the exact source reproduced in section 7. |
| `test_invalid_output_dtype_and_non_2d_parcel_fail_locally` | none | pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"); pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"); pytest.raises(BessPlanningFeatureParcelAggregationError, match="2D") | 0 | Proves invalid output dtype and non 2d parcel fail locally using the exact source reproduced in section 7. |
| `test_every_inherited_application_relation_domain_is_validated_locally` | pytest.mark.parametrize(<br>    "relations",<br>    [<br>        pd.DataFrame([_relation(status="AUTHORIZED")]),<br>        pd.DataFrame([_relation(status="FORBIDDEN")]),<br>        pd.DataFrame(<br>            [<br>                _relation(<br>                    feature_id="LOW",<br>                    status="PROHIBITED",<br>                    priority=10,<br>                ),<br>                _relation(<br>                    feature_id="HIGH",<br>                    status="LIKELY_MATERIAL_CONSTRAINT",<br>                    priority=50,<br>                ),<br>            ]<br>        ),<br>        pd.DataFrame(<br>            [<br>                _relation(<br>                    feature_id="LOW",<br>                    confidence="CERTAIN",<br>                    priority=10,<br>                ),<br>                _relation(<br>                    feature_id="HIGH",<br>                    status="LIKELY_MATERIAL_CONSTRAINT",<br>                    priority=50,<br>                ),<br>            ]<br>        ),<br>        pd.DataFrame(<br>            [<br>                _relation(<br>                    relation_type="TOUCH_ONLY",<br>                    application_status="INVALID_APPLICATION_STATUS",<br>                )<br>            ]<br>        ),<br>    ],<br>    ids=[<br>        "selected-authorized",<br>        "selected-forbidden",<br>        "lower-prohibited",<br>        "lower-certain-confidence",<br>        "contextual-invalid-application-status",<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves every inherited application relation domain is validated locally using the exact source reproduced in section 7. |
| `test_unresolved_relation_cannot_contain_a_decision` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves unresolved relation cannot contain a decision using the exact source reproduced in section 7. |
| `test_all_application_identity_scope_and_boundary_fields_are_intrinsic` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("feature_family", "OTHER"),<br>        ("type_code_raw", "7"),<br>        ("subtype_code_raw", "AA"),<br>        ("bess_cnig_application_scope", "WRONG_SCOPE"),<br>        ("bess_cnig_local_feature_text_interpreted", True),<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves all application identity scope and boundary fields are intrinsic using the exact source reproduced in section 7. |
| `test_application_relation_suffix_dtype_is_validated_locally` | none | pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype") | 0 | Proves application relation suffix dtype is validated locally using the exact source reproduced in section 7. |
| `test_status_and_priority_mapping_is_one_to_one_at_every_level` | pytest.mark.parametrize(<br>    "relations",<br>    [<br>        pd.DataFrame(<br>            [<br>                _relation(<br>                    feature_id="A",<br>                    status="MATERIAL_REVIEW_REQUIRED",<br>                    priority=50,<br>                ),<br>                _relation(<br>                    feature_id="B",<br>                    status="DESIGN_REVIEW_REQUIRED",<br>                    priority=50,<br>                ),<br>            ]<br>        ),<br>        pd.DataFrame(<br>            [<br>                _relation(<br>                    feature_id="MAX",<br>                    status="LIKELY_MATERIAL_CONSTRAINT",<br>                    priority=50,<br>                ),<br>                _relation(<br>                    feature_id="LOW-A",<br>                    status="MATERIAL_REVIEW_REQUIRED",<br>                    priority=10,<br>                ),<br>                _relation(<br>                    feature_id="LOW-B",<br>                    status="DESIGN_REVIEW_REQUIRED",<br>                    priority=10,<br>                ),<br>            ]<br>        ),<br>        pd.DataFrame(<br>            [<br>                _relation(<br>                    feature_id="A",<br>                    status="LIKELY_MATERIAL_CONSTRAINT",<br>                    priority=50,<br>                ),<br>                _relation(<br>                    feature_id="B",<br>                    status="LIKELY_MATERIAL_CONSTRAINT",<br>                    priority=10,<br>                ),<br>            ]<br>        ),<br>    ],<br>    ids=[<br>        "same-maximum-priority-two-statuses",<br>        "same-lower-priority-two-statuses",<br>        "same-status-two-priorities",<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority") | 0 | Proves status and priority mapping is one to one at every level using the exact source reproduced in section 7. |
| `test_valid_repeated_status_and_priority_mapping_selects_every_exact_match` | none | none | 2 | Proves valid repeated status and priority mapping selects every exact match using the exact source reproduced in section 7. |
| `test_duplicate_parcel_feature_identity_is_rejected_for_every_role` | pytest.mark.parametrize(<br>    "relations",<br>    [<br>        pd.DataFrame([_relation(feature_id="A"), _relation(feature_id="A")]),<br>        pd.DataFrame(<br>            [<br>                _relation(<br>                    feature_id="LOW",<br>                    status="CONTEXT_REVIEW_REQUIRED",<br>                    priority=10,<br>                ),<br>                _relation(<br>                    feature_id="LOW",<br>                    status="CONTEXT_REVIEW_REQUIRED",<br>                    priority=10,<br>                ),<br>                _relation(feature_id="HIGH", priority=30),<br>            ]<br>        ),<br>        pd.DataFrame(<br>            [<br>                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),<br>                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),<br>            ]<br>        ),<br>        pd.DataFrame(<br>            [<br>                _relation(feature_id="DEFERRED"),<br>                _relation(feature_id="DEFERRED"),<br>                _relation(<br>                    feature_id="UNRESOLVED",<br>                    application_status="UNRESOLVED_CODE_PAIR",<br>                    status=None,<br>                    confidence=None,<br>                    priority=None,<br>                ),<br>            ]<br>        ),<br>        pd.DataFrame(<br>            [<br>                _relation(feature_id="A", relation_type="AREA_OVERLAP"),<br>                _relation(feature_id="A", relation_type="LENGTH_OVERLAP"),<br>            ]<br>        ),<br>    ],<br>    ids=[<br>        "selected",<br>        "lower-priority",<br>        "contextual",<br>        "deferred",<br>        "different-relation-types",<br>    ],<br>) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="duplicate\|unique"<br>    ) | 0 | Proves duplicate parcel feature identity is rejected for every role using the exact source reproduced in section 7. |
| `test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` | pytest.mark.parametrize(<br>    "feature_id",<br>    [None, "", "None", "/tmp/feature"],<br>) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="feature\|identity"<br>    ) | 0 | Proves invalid lower priority feature id is rejected independently of json role using the exact source reproduced in section 7. |
| `test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` | pytest.mark.parametrize("feature_id", [r"C:\feature", " GPU:F "]) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="feature\|identity"<br>    ) | 0 | Proves invalid deferred feature id is rejected independently of json role using the exact source reproduced in section 7. |
| `test_invalid_relation_parcel_id_is_rejected` | pytest.mark.parametrize("parcel_id", [None, " PARCEL-1 "]) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="parcel\|identity"<br>    ) | 0 | Proves invalid relation parcel id is rejected using the exact source reproduced in section 7. |
| `test_unknown_relation_type_is_rejected_by_shared_relation_contract` | none | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="relation type"<br>    ) | 0 | Proves unknown relation type is rejected by shared relation contract using the exact source reproduced in section 7. |
| `test_document_wide_same_priority_cannot_map_to_two_statuses` | pytest.mark.parametrize("context_type", [None, "TOUCH_ONLY", "BOUNDARY_TOUCH"]) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="priority\|mapping"<br>    ) | 0 | Proves document wide same priority cannot map to two statuses using the exact source reproduced in section 7. |
| `test_document_wide_same_status_cannot_map_to_two_priorities` | none | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="priority\|mapping"<br>    ) | 0 | Proves document wide same status cannot map to two priorities using the exact source reproduced in section 7. |
| `test_document_wide_repeated_mapping_and_unresolved_rows_are_valid` | none | none | 1 | Proves document wide repeated mapping and unresolved rows are valid using the exact source reproduced in section 7. |
| `test_complete_five_status_policy_mapping_is_globally_valid` | none | none | 1 | Proves complete five status policy mapping is globally valid using the exact source reproduced in section 7. |
| `test_selected_relation_role_requires_selected_status_and_priority` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves selected relation role requires selected status and priority using the exact source reproduced in section 7. |
| `test_malformed_parcel_geometry_is_rejected_intrinsically` | pytest.mark.parametrize(<br>    "geometry",<br>    [<br>        Point(0, 0),<br>        LineString([(0, 0), (1, 1)]),<br>        Polygon(),<br>        Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),<br>        None,<br>    ],<br>    ids=["point", "line", "empty", "invalid", "null"],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves malformed parcel geometry is rejected intrinsically using the exact source reproduced in section 7. |
| `test_valid_polygon_and_multipolygon_parcels_are_accepted` | none | none | 0 | Proves valid polygon and multipolygon parcels are accepted using the exact source reproduced in section 7. |
| `test_duplicate_output_columns_are_rejected_intrinsically` | pytest.mark.parametrize("frame_name", ["parcels", "relation_assessments"]) | pytest.raises(BessPlanningFeatureParcelAggregationError, match="duplicate") | 0 | Proves duplicate output columns are rejected intrinsically using the exact source reproduced in section 7. |
| `test_only_application_result_schema_two_is_accepted` | pytest.mark.parametrize("version", [1, 3, 999]) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="application.*schema"<br>    ) | 0 | Proves only application result schema two is accepted using the exact source reproduced in section 7. |
| `test_application_result_schema_two_remains_accepted` | none | none | 1 | Proves application result schema two remains accepted using the exact source reproduced in section 7. |
| `test_noncanonical_feature_ids_are_rejected` | pytest.mark.parametrize(<br>    "feature_id",<br>    ["None", "nan", "<NA>", "/tmp/feature", r"C:\feature", " GPU:F "],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID") | 0 | Proves noncanonical feature ids are rejected using the exact source reproduced in section 7. |
| `test_current_gpu_feature_id_is_canonical` | none | none | 1 | Proves current gpu feature id is canonical using the exact source reproduced in section 7. |
| `test_authorized_status_artifact_fails_local_verified_byte_loading` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves authorized status artifact fails local verified byte loading using the exact source reproduced in section 7. |
| `test_coordinated_relation_identity_artifact_corruption_fails_locally` | pytest.mark.parametrize(<br>    "factory",<br>    [<br>        _duplicate_selected_pair_result,<br>        _invalid_lower_feature_id_result,<br>        _cross_parcel_priority_conflict_result,<br>    ],<br>    ids=["duplicate-pair", "invalid-lower-feature-id", "global-priority-conflict"],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError) | 1 | Proves coordinated relation identity artifact corruption fails locally using the exact source reproduced in section 7. |
| `test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` | none | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="surface\|metric\|type"<br>    ) | 0 | Proves controlling relation cannot be relabelled contextual in artifact using the exact source reproduced in section 7. |
| `test_no_relation_parcel_rejects_textual_null_identity` | pytest.mark.parametrize("parcel_id", ["None", "nan", "<NA>"]) | pytest.raises(BessPlanningFeatureParcelAggregationError, match="parcel ID") | 1 | Proves no relation parcel rejects textual null identity using the exact source reproduced in section 7. |
| `test_relation_identity_and_global_mapping_fail_before_heavy_validation` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 1 | Proves relation identity and global mapping fail before heavy validation using the exact source reproduced in section 7. |
| `test_relation_semantic_failure_fast_fails_before_heavy_validation` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 1 | Proves relation semantic failure fast fails before heavy validation using the exact source reproduced in section 7. |
| `test_parcel_decision_status_domain_rejects_forbidden_vocabulary` | pytest.mark.parametrize(<br>    "status",<br>    [<br>        "ALLOWED",<br>        "AUTHORIZED",<br>        "COMPATIBLE",<br>        "CLEAR",<br>        "FORBIDDEN",<br>        "PROHIBITED",<br>        "BLOCKED",<br>        "BUILDABLE",<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError, match="status") | 0 | Proves parcel decision status domain rejects forbidden vocabulary using the exact source reproduced in section 7. |
| `test_persisted_feature_id_json_must_be_portable_and_canonical` | pytest.mark.parametrize(<br>    "json_value",<br>    [<br>        '["None"]',<br>        '["nan"]',<br>        '["<NA>"]',<br>        '["/tmp/feature"]',<br>        r'["C:\\feature"]',<br>        '[" GPU:F "]',<br>        '["B","A"]',<br>        '["A", "B"]',<br>        '["A","A"]',<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError) | 0 | Proves persisted feature id json must be portable and canonical using the exact source reproduced in section 7. |
| `test_representative_intrinsic_failures_all_precede_heavy_validation` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 1 | Proves representative intrinsic failures all precede heavy validation using the exact source reproduced in section 7. |
| `test_one_aggregation_and_one_public_validation_each_call_heavy_once` | none | none | 2 | Proves one aggregation and one public validation each call heavy once using the exact source reproduced in section 7. |
| `test_valid_two_file_verified_byte_artifacts_and_source_readback` | none | none | 0 | Proves valid two file verified byte artifacts and source readback using the exact source reproduced in section 7. |
| `test_artifact_manifest_corruption_is_rejected` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        lambda value: value.update(schema_version=2),<br>        lambda value: value.update(application_result_hash_schema_version=1),<br>        lambda value: value.update(application_result_hash_schema_version=3),<br>        lambda value: value.update(application_result_hash_schema_version=999),<br>        lambda value: value["artifacts"].pop(),<br>        lambda value: value["artifacts"].append(<br>            {**value["artifacts"][0], "artifact_role": "EXTRA"}<br>        ),<br>        lambda value: value["artifacts"].append(dict(value["artifacts"][0])),<br>        lambda value: value["artifacts"][0].update(filename="wrong.parquet"),<br>        lambda value: value["artifacts"][1].update(<br>            filename=value["artifacts"][0]["filename"]<br>        ),<br>        lambda value: value["artifacts"][0].update(filename="C:/absolute.parquet"),<br>        lambda value: value["artifacts"][0].update(size_bytes=1),<br>        lambda value: value["artifacts"][0].update(sha256="f" * 64),<br>        lambda value: value["artifacts"][0].update(sha256="bad"),<br>        lambda value: value["artifacts"][0].update(row_count=999),<br>        lambda value: value["artifacts"][0]["frame_schema_signature"].update(<br>            index_names=["wrong"]<br>        ),<br>        lambda value: value["artifacts"][0].update(crs=None),<br>        lambda value: value["artifacts"][0].update(crs={"wrong": True}),<br>        lambda value: value["artifacts"][0].update(geospatial=False),<br>        lambda value: value.update(unknown=True),<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError) | 1 | Proves artifact manifest corruption is rejected using the exact source reproduced in section 7. |
| `test_aggregation_manifest_uses_strict_json_before_artifact_read` | pytest.mark.parametrize(<br>    "document",<br>    [<br>        '{"schema_version":1,"schema_version":1}',<br>        '{"schema_version":NaN}',<br>        '{"schema_version":Infinity}',<br>        "[]",<br>    ],<br>    ids=["duplicate-key", "nan", "infinity", "non-object"],<br>) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError,<br>        match="Duplicate JSON\|finite\|top-level\|invalid",<br>    ) | 1 | Proves aggregation manifest uses strict json before artifact read using the exact source reproduced in section 7. |
| `test_aggregation_physical_replacement_is_rejected` | none | pytest.raises(BessPlanningFeatureParcelAggregationError, match="size\|SHA") | 0 | Proves aggregation physical replacement is rejected using the exact source reproduced in section 7. |
| `test_verified_bytes_are_the_bytes_parsed` | none | none | 1 | Proves verified bytes are the bytes parsed using the exact source reproduced in section 7. |
| `test_public_exports_are_stable` | none | none | 2 | Proves public exports are stable using the exact source reproduced in section 7. |
| `test_relation_parcel_area_is_bound_to_real_parcel_geometry` | pytest.mark.parametrize(<br>    ("geometry_kind", "relation_type"),<br>    [<br>        ("SURFACE", "AREA_OVERLAP"),<br>        ("LINE", "LENGTH_OVERLAP"),<br>        ("POINT", "INSIDE"),<br>    ],<br>) | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="parcel.*area\|area.*parcel"<br>    ) | 0 | Proves relation parcel area is bound to real parcel geometry using the exact source reproduced in section 7. |
| `test_self_consistent_parcel_area_artifact_is_rejected` | none | pytest.raises(<br>        BessPlanningFeatureParcelAggregationError, match="parcel.*area\|area.*parcel"<br>    ) | 0 | Proves self consistent parcel area artifact is rejected using the exact source reproduced in section 7. |
| `test_parcel_area_validation_uses_reprojected_calculation_copy` | none | none | 0 | Proves parcel area validation uses reprojected calculation copy using the exact source reproduced in section 7. |
| `test_parcel_area_defect_fast_fails_before_application_source_validation` | none | pytest.raises(BessPlanningFeatureParcelAggregationError) | 1 | Proves parcel area defect fast fails before application source validation using the exact source reproduced in section 7. |
| `test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams` | none | none | 2 | Proves step 7d 5b 2b 5 aggregation loader requires exact upstreams using the exact source reproduced in section 7. |
| `test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` | none | none | 1 | Proves source bound aggregation loader accepts only supplied upstreams using the exact source reproduced in section 7. |
| `test_aggregation_manifest_filenames_are_casefold_unique` | none | pytest.raises(ValueError, match="filename\|duplicate") | 0 | Proves aggregation manifest filenames are casefold unique using the exact source reproduced in section 7. |
| `test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "parcel_geometry",<br>        "parcel_crs",<br>        "application_relation",<br>        "parcel_order",<br>        "unrelated_parcel_geometry",<br>    ],<br>) | pytest.raises(BessPlanningFeatureParcelAggregationError, match="source lock") | 2 | Proves source bound aggregation loader rejects coordinated upstream changes using the exact source reproduced in section 7. |
| `test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` | none | none | 3 | Proves source bound aggregation loader rebuilds once without mutating upstreams using the exact source reproduced in section 7. |
| `test_aggregation_loader_rejects_bad_application_before_artifact_reads` | none | pytest.raises(Exception, match="hash\|SHA\|invalid") | 1 | Proves aggregation loader rejects bad application before artifact reads using the exact source reproduced in section 7. |
| `test_aggregation_manifest_rejects_nonportable_filename` | pytest.mark.parametrize(<br>    "filename",<br>    [<br>        "/tmp/file.parquet",<br>        "../file.parquet",<br>        "subdir/file.parquet",<br>        r"C:\absolute\file.parquet",<br>        "C:/absolute/file.parquet",<br>        r"\\server\share\file.parquet",<br>        r"subdir\file.parquet",<br>        "CON.parquet",<br>        "con.PARQUET",<br>        "NUL.parquet",<br>        "PRN.parquet",<br>        "AUX.parquet",<br>        "CLOCK$.parquet",<br>        "COM1.parquet",<br>        "COM9.parquet",<br>        "LPT1.parquet",<br>        "LPT9.parquet",<br>        "COM¹.parquet",<br>        "COM².parquet",<br>        "COM³.parquet",<br>        "LPT¹.parquet",<br>        "LPT².parquet",<br>        "LPT³.parquet",<br>        "file:name.parquet",<br>        "base.parquet:stream.parquet",<br>        "file?.parquet",<br>        "file*.parquet",<br>        "file<.parquet",<br>        "file>.parquet",<br>        "file\|.parquet",<br>        'file".parquet',<br>        "nul\x00.parquet",<br>        "line\nbreak.parquet",<br>        "del\x7f.parquet",<br>    ],<br>) | pytest.raises(ValueError, match="filename\|basename\|portable") | 0 | Proves aggregation manifest rejects nonportable filename using the exact source reproduced in section 7. |

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
from dataclasses import fields, replace
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Point, Polygon
from test_apply_bess_planning_feature_policy import (
    _application_fixture,
    _coordinated_policy_mutation,
    _surface_touch_with_positive_area,
)

from landscout import stages
from landscout.common.bess_application_contract import (
    POLICY_COLUMNS,
    POLICY_SUFFIX_DTYPES,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.planning_feature_schema import relation_columns, relation_dtypes
from landscout.common.strict_json import loads_strict_json_object
from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)
from landscout.stages.aggregate_bess_planning_feature_policy import (
    load_bess_planning_feature_parcel_aggregation_artifacts as _load_aggregation_artifacts,
)

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
RELATION_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_selected_for_parcel_status",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
    "bess_cnig_resulting_parcel_status_priority",
)
_LAST_SOURCE_PARCELS: gpd.GeoDataFrame | None = None
_LAST_APPLICATION_RESULT: object | None = None


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


def _load_legacy_local_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
    """Exercise pre-2B.5 local-only assertions for retained synthetic fixtures."""

    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    payload = loads_strict_json_object(Path(manifest_path).read_bytes())
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


@pytest.mark.parametrize("relation_type", ["AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"])
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


@pytest.mark.parametrize("relation_type", ["TOUCH_ONLY", "BOUNDARY_TOUCH"])
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


def test_no_relation_parcel_is_retained_without_a_decision() -> None:
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcel = result.parcels.iloc[1]
    assert parcel.bess_cnig_parcel_aggregation_status == "NO_PLANNING_FEATURE_RELATION"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert bool(parcel.bess_cnig_formal_review_required) is True


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


@pytest.mark.parametrize(
    ("frame_name", "column", "value"),
    [
        ("parcels", "bess_cnig_selected_relation_count", 999),
        ("parcels", "bess_cnig_parcel_precheck_status", "UNKNOWN"),
        ("parcels", "bess_cnig_parcel_status_priority", 999),
        ("parcels", "bess_cnig_parcel_precheck_confidence", "LOW"),
        ("parcels", "bess_cnig_selected_feature_ids_json", "[]"),
        (
            "relation_assessments",
            "bess_cnig_parcel_relation_role",
            "TOUCH_ONLY_CONTEXT",
        ),
        ("relation_assessments", "parcel_id", "PARCEL-OTHER"),
    ],
)
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


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(status="AUTHORIZED")]),
        pd.DataFrame([_relation(status="FORBIDDEN")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="PROHIBITED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    confidence="CERTAIN",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    relation_type="TOUCH_ONLY",
                    application_status="INVALID_APPLICATION_STATUS",
                )
            ]
        ),
    ],
    ids=[
        "selected-authorized",
        "selected-forbidden",
        "lower-prohibited",
        "lower-certain-confidence",
        "contextual-invalid-application-status",
    ],
)
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(relations)


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


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("feature_family", "OTHER"),
        ("type_code_raw", "7"),
        ("subtype_code_raw", "AA"),
        ("bess_cnig_application_scope", "WRONG_SCOPE"),
        ("bess_cnig_local_feature_text_interpreted", True),
    ],
)
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
    row = _relation(relation_type="TOUCH_ONLY")
    row[column] = value
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))


def test_application_relation_suffix_dtype_is_validated_locally() -> None:
    relations = pd.DataFrame([_relation()])
    relations["bess_cnig_precheck_status"] = relations[
        "bess_cnig_precheck_status"
    ].astype("category")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        _build_from_relations(relations, canonicalize_application_dtypes=False)


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="MAX",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="LOW-A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW-B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=10,
                ),
            ]
        ),
    ],
    ids=[
        "same-maximum-priority-two-statuses",
        "same-lower-priority-two-statuses",
        "same-status-two-priorities",
    ],
)
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority"):
        _build_from_relations(relations)


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


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(feature_id="A"), _relation(feature_id="A")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="DEFERRED"),
                _relation(feature_id="DEFERRED"),
                _relation(
                    feature_id="UNRESOLVED",
                    application_status="UNRESOLVED_CODE_PAIR",
                    status=None,
                    confidence=None,
                    priority=None,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="A", relation_type="AREA_OVERLAP"),
                _relation(feature_id="A", relation_type="LENGTH_OVERLAP"),
            ]
        ),
    ],
    ids=[
        "selected",
        "lower-priority",
        "contextual",
        "deferred",
        "different-relation-types",
    ],
)
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="duplicate|unique"
    ):
        _build_from_relations(relations)


@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature"],
)
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


@pytest.mark.parametrize("feature_id", [r"C:\feature", " GPU:F "])
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


@pytest.mark.parametrize("parcel_id", [None, " PARCEL-1 "])
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
    relation = _relation()
    relation["parcel_id"] = parcel_id
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel|identity"
    ):
        _build_from_relations(pd.DataFrame([relation]))


def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="relation type"
    ):
        _build_from_relations(pd.DataFrame([_relation(relation_type="NEARBY")]))


@pytest.mark.parametrize("context_type", [None, "TOUCH_ONLY", "BOUNDARY_TOUCH"])
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


@pytest.mark.parametrize(
    "geometry",
    [
        Point(0, 0),
        LineString([(0, 0), (1, 1)]),
        Polygon(),
        Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        None,
    ],
    ids=["point", "line", "empty", "invalid", "null"],
)
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _validate_parcel_geometries([geometry])


def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
    polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
    _validate_parcel_geometries([polygon, MultiPolygon([polygon])])


@pytest.mark.parametrize("frame_name", ["parcels", "relation_assessments"])
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


@pytest.mark.parametrize("version", [1, 3, 999])
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


def test_application_result_schema_two_remains_accepted() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    assert result.application_result_hash_schema_version == 2
    module._validate_result_envelope(result)


@pytest.mark.parametrize(
    "feature_id",
    ["None", "nan", "<NA>", "/tmp/feature", r"C:\feature", " GPU:F "],
)
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID"):
        _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))


def test_current_gpu_feature_id_is_canonical() -> None:
    feature_id = "GPU:DOC:prescription_surface:FEATURE-01"
    result = _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
    assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == (
        f'["{feature_id}"]'
    )


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


@pytest.mark.parametrize(
    "factory",
    [
        _duplicate_selected_pair_result,
        _invalid_lower_feature_id_result,
        _cross_parcel_priority_conflict_result,
    ],
    ids=["duplicate-pair", "invalid-lower-feature-id", "global-priority-conflict"],
)
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


@pytest.mark.parametrize("parcel_id", ["None", "nan", "<NA>"])
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


@pytest.mark.parametrize(
    "status",
    [
        "ALLOWED",
        "AUTHORIZED",
        "COMPATIBLE",
        "CLEAR",
        "FORBIDDEN",
        "PROHIBITED",
        "BLOCKED",
        "BUILDABLE",
    ],
)
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


@pytest.mark.parametrize(
    "json_value",
    [
        '["None"]',
        '["nan"]',
        '["<NA>"]',
        '["/tmp/feature"]',
        r'["C:\\feature"]',
        '[" GPU:F "]',
        '["B","A"]',
        '["A", "B"]',
        '["A","A"]',
    ],
)
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


@pytest.mark.parametrize(
    "mutation",
    [
        lambda value: value.update(schema_version=2),
        lambda value: value.update(application_result_hash_schema_version=1),
        lambda value: value.update(application_result_hash_schema_version=3),
        lambda value: value.update(application_result_hash_schema_version=999),
        lambda value: value["artifacts"].pop(),
        lambda value: value["artifacts"].append(
            {**value["artifacts"][0], "artifact_role": "EXTRA"}
        ),
        lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
        lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
        lambda value: value["artifacts"][1].update(
            filename=value["artifacts"][0]["filename"]
        ),
        lambda value: value["artifacts"][0].update(filename="C:/absolute.parquet"),
        lambda value: value["artifacts"][0].update(size_bytes=1),
        lambda value: value["artifacts"][0].update(sha256="f" * 64),
        lambda value: value["artifacts"][0].update(sha256="bad"),
        lambda value: value["artifacts"][0].update(row_count=999),
        lambda value: value["artifacts"][0]["frame_schema_signature"].update(
            index_names=["wrong"]
        ),
        lambda value: value["artifacts"][0].update(crs=None),
        lambda value: value["artifacts"][0].update(crs={"wrong": True}),
        lambda value: value["artifacts"][0].update(geospatial=False),
        lambda value: value.update(unknown=True),
    ],
)
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


@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version":1,"schema_version":1}',
        '{"schema_version":NaN}',
        '{"schema_version":Infinity}',
        "[]",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
def test_aggregation_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
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
        BessPlanningFeatureParcelAggregationError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
    assert artifact_reads == 0


def test_aggregation_physical_replacement_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    paths["RELATION_ASSESSMENTS"].write_bytes(
        paths["RELATION_ASSESSMENTS"].read_bytes() + b"tamper"
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="size|SHA"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


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


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("LINE", "LENGTH_OVERLAP"),
        ("POINT", "INSIDE"),
    ],
)
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


def test_aggregation_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)


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


@pytest.mark.parametrize(
    "mutation",
    [
        "parcel_geometry",
        "parcel_crs",
        "application_relation",
        "parcel_order",
        "unrelated_parcel_geometry",
    ],
)
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
def test_aggregation_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```
