# `src/landscout/stages/aggregate_bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/aggregate_bess_planning_feature_policy.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: planning
- Responsibility: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.
- Source SHA256: `d715ed2a3127c6b7e2d5c87158f7719a1f5ff0365930e465efab3e8e9b184a3a`

## 1. Purpose

Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `import re`
- `from dataclasses import dataclass, replace`
- `from datetime import date, datetime`
- `from hashlib import sha256`
- `from io import BytesIO`
- `from numbers import Integral, Real`
- `from pathlib import Path, PurePosixPath, PureWindowsPath`
- `from typing import Literal`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
    model_validator,
)`
- `from pyproj import CRS`
- `from shapely import get_coordinate_dimension, to_wkb`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.common.artifact_paths import validate_portable_parquet_filename`
- `from landscout.common.bess_application_contract import (
    ALLOWED_CONFIDENCES,
    ALLOWED_PRECHECK_STATUSES,
    NULL_LITERALS,
    POLICY_SCOPE,
    validate_bess_application_relation_frame,
)`
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.common.planning_overlay import technical_overlay_tolerance`
- `from landscout.sources.gpu_fr import GpuPlanningDocument`
- `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)`

## 4. Contract taxonomy

### A. Python constants

#### `RESULT_HASH_SCHEMA_VERSION`

```python
RESULT_HASH_SCHEMA_VERSION = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/interpret_bess_zoning.py::_build_result` (value argument/reference), `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` (value argument/reference).

#### `ARTIFACT_MANIFEST_SCHEMA_VERSION`

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing.

#### `APPLICATION_RESULT_HASH_SCHEMA_VERSION`

```python
APPLICATION_RESULT_HASH_SCHEMA_VERSION = 2
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing.

#### `AGGREGATION_SCOPE`

```python
AGGREGATION_SCOPE = "PARCEL_POLICY_AGGREGATION_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` (value argument/reference).

#### `CONFIDENCE_METHOD`

```python
CONFIDENCE_METHOD = "LOWEST_CONFIDENCE_FOR_SELECTED_STATUS"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `ARTIFACT_KIND`

```python
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `CONTROLLING_RELATION_TYPES`

```python
CONTROLLING_RELATION_TYPES = frozenset({"AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `CONTEXT_RELATION_TYPES`

```python
CONTEXT_RELATION_TYPES = frozenset({"TOUCH_ONLY", "BOUNDARY_TOUCH"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `AGGREGATION_STATUSES`

```python
AGGREGATION_STATUSES = frozenset(
    {
        "AGGREGATED_EXACT_POLICY",
        "UNRESOLVED_CONTROLLING_CODE_PAIR",
        "TOUCH_ONLY_RELATIONS_ONLY",
        "NO_PLANNING_FEATURE_RELATION",
    }
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `RELATION_ROLES`

```python
RELATION_ROLES = frozenset(
    {
        "SELECTED_CONTROLLING",
        "LOWER_PRIORITY_CONTROLLING",
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    }
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `CONFIDENCE_RANK`

```python
CONFIDENCE_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `SHA_PATTERN`

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` (value argument/reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` (value argument/reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` (value argument/reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` (value argument/reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` (value argument/reference).

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/planning_feature_schema.py::<module>` (value argument/reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` (value argument/reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` (value argument/reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::_validate_normalized_planning_feature_inputs` (value argument/reference), `src/landscout/stages/enrich_planning_features.py::<module>` (import/re-export), `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` (value argument/reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` (value argument/reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` (value argument/reference), `tests/unit/test_resolve_planning_feature_codes.py::_canonical_relation_schema` (value argument/reference), `tests/unit/test_resolve_planning_feature_codes.py::_legacy_inputs` (value argument/reference), `tests/unit/test_resolve_planning_feature_codes.py::<module>` (import/re-export).

#### `PARCEL_STRING_COLUMNS`

```python
PARCEL_STRING_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `PARCEL_INTEGER_COLUMNS`

```python
PARCEL_INTEGER_COLUMNS = (
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `PARCEL_BOOL_COLUMNS`

```python
PARCEL_BOOL_COLUMNS = (
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_formal_review_required",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `RELATION_STRING_COLUMNS`

```python
RELATION_STRING_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/enrich_planning_features.py::<module>` (import/re-export).

#### `ARTIFACT_ROLES`

```python
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = ("PARCELS", "RELATION_ASSESSMENTS")
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `RESULT_FRAME_FIELDS`

```python
RESULT_FRAME_FIELDS = ("relation_assessments", "parcels")
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `RESULT_SCALAR_FIELDS`

```python
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureParcelAggregationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` (property/attribute access).


### B. Type aliases and closed domains

#### `ArtifactRole`

```python
ArtifactRole = Literal["PARCELS", "RELATION_ASSESSMENTS"]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. It is consumed by annotations or Pydantic validation in this module.


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "BessPlanningFeatureParcelAggregationArtifactManifest",
    "BessPlanningFeatureParcelAggregationError",
    "BessPlanningFeatureParcelAggregationResult",
    "aggregate_bess_planning_feature_policy_to_parcels",
    "load_bess_planning_feature_parcel_aggregation_artifacts",
    "validate_bess_planning_feature_parcel_aggregation_result",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `BessPlanningFeatureParcelAggregationError`

**Purpose:** Raised when parcel aggregation integrity cannot be proven.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_canonical_value` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_canonical_sha256` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_feature_id` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_json_ids` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_parcel_frame` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_relations` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_relation_parcel_areas` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_local_domains` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_relation_priority` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_compare_frame` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_source_locks` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_source` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_unique_json_object` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_read_verified_artifact` via `BessPlanningFeatureParcelAggregationError`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationError`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='2D')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_every_inherited_application_relation_domain_is_validated_locally` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unresolved_relation_cannot_contain_a_decision` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_relation_suffix_dtype_is_validated_locally` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='dtype')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_status_and_priority_mapping_is_one_to_one_at_every_level` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_parcel_feature_identity_is_rejected_for_every_role` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='duplicate|unique')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='feature|identity')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='feature|identity')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_relation_parcel_id_is_rejected` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel|identity')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='relation type')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_priority_cannot_map_to_two_statuses` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority|mapping')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_document_wide_same_status_cannot_map_to_two_priorities` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='priority|mapping')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_malformed_parcel_geometry_is_rejected_intrinsically` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='duplicate')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='application.*schema')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_noncanonical_feature_ids_are_rejected` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='Feature ID')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='surface|metric|type')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel ID')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='status')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='Duplicate JSON')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='size|SHA')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel.*area|area.*parcel')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='parcel.*area|area.*parcel')`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `pytest.raises(BessPlanningFeatureParcelAggregationError)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `pytest.raises(BessPlanningFeatureParcelAggregationError, match='source lock')`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.

**Exact class source**

```python
class BessPlanningFeatureParcelAggregationError(ValueError):
    """Raised when parcel aggregation integrity cannot be proven."""
```

### `_ApplicationLineage`

**Purpose:** Immutable result/value envelope carrying `source_document_id`, `source_archive_sha256`, `cnig_profile`, `cnig_profile_sha256`, `policy_profile`, `policy_sha256`, `policy_complete_result_content_sha256`, `complete_result_content_sha256`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `source_document_id` | `source_document_id: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: str` | Stores `_ApplicationLineage`'s `cnig profile` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `cnig_profile_sha256` | `cnig_profile_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_profile` | `policy_profile: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_sha256` | `policy_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_complete_result_content_sha256` | `policy_complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Interface consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_ApplicationLineage`.

**Exact class source**

```python
class _ApplicationLineage:
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    policy_profile: str
    policy_sha256: str
    policy_complete_result_content_sha256: str
    complete_result_content_sha256: str
```

### `_StrictModel`

**Purpose:** Validates the planning contract carried by its explicit validators and inherited fields.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `BessPlanningFeatureParcelAggregationArtifactRecord`

**Purpose:** Validates the planning contract carried by `artifact_role`, `filename`, `row_count`, `size_bytes`, `sha256`, `frame_schema_signature`, `geospatial`, `crs`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `artifact_role` | `artifact_role: ArtifactRole` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |
| `filename` | `filename: StrictStr` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `row_count` | `row_count: StrictInt` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `size_bytes` | `size_bytes: StrictInt` | Stores `BessPlanningFeatureParcelAggregationArtifactRecord`'s `size bytes` value under exact annotation `StrictInt`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `sha256` | `sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `frame_schema_signature` | `frame_schema_signature: dict[StrictStr, object]` | Structured `frame schema signature` collection owned by `BessPlanningFeatureParcelAggregationArtifactRecord`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `geospatial` | `geospatial: StrictBool` | Boolean `geospatial` flag on `BessPlanningFeatureParcelAggregationArtifactRecord`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `crs` | `crs: dict[StrictStr, object] \| None` | Coordinate reference system identity; exact accepted/storage/calculation behavior is enforced by the owning CRS validator. |

**Validators (exact source)**

`_validate_record`:

```python
def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be non-negative")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be positive")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geo = self.artifact_role == "PARCELS"
        if self.geospatial is not expected_geo:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        if expected_geo:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("parcel artifact CRS is missing or inconsistent")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("relation artifact must not declare CRS")
        return self
```

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class BessPlanningFeatureParcelAggregationArtifactRecord(_StrictModel):
    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: dict[StrictStr, object]
    geospatial: StrictBool
    crs: dict[StrictStr, object] | None

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be non-negative")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be positive")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geo = self.artifact_role == "PARCELS"
        if self.geospatial is not expected_geo:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        if expected_geo:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("parcel artifact CRS is missing or inconsistent")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("relation artifact must not declare CRS")
        return self
```

### `BessPlanningFeatureParcelAggregationResult`

**Purpose:** Immutable result/value envelope carrying `result_hash_schema_version`, `aggregation_scope`, `policy_scope`, `local_feature_text_interpreted`, `local_regulation_content_interpreted`, `legal_conclusion_produced`, `parcel_status_aggregated`, `parcel_rejection_performed`, `score_calculated`, `source_document_id`, `source_archive_sha256`, `cnig_profile`, `cnig_profile_sha256`, `cnig_complete_result_content_sha256`, `policy_profile`, `policy_sha256`, `policy_complete_result_content_sha256`, `application_result_hash_schema_version`, `application_complete_result_content_sha256`, `source_parcels_content_sha256`, `source_application_relations_content_sha256`, `relation_assessments_content_sha256`, `parcels_content_sha256`, `complete_result_content_sha256`, `relation_assessments`, `parcels`.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `result_hash_schema_version` | `result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `aggregation_scope` | `aggregation_scope: str` | Closed or validated `aggregation scope` classification on `BessPlanningFeatureParcelAggregationResult`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `policy_scope` | `policy_scope: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `local_feature_text_interpreted` | `local_feature_text_interpreted: bool` | Boolean `local feature text interpreted` flag on `BessPlanningFeatureParcelAggregationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `local_regulation_content_interpreted` | `local_regulation_content_interpreted: bool` | Boolean `local regulation content interpreted` flag on `BessPlanningFeatureParcelAggregationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `legal_conclusion_produced` | `legal_conclusion_produced: bool` | Boolean `legal conclusion produced` flag on `BessPlanningFeatureParcelAggregationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_status_aggregated` | `parcel_status_aggregated: bool` | Boolean `parcel status aggregated` flag on `BessPlanningFeatureParcelAggregationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_rejection_performed` | `parcel_rejection_performed: bool` | Boolean `parcel rejection performed` flag on `BessPlanningFeatureParcelAggregationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `score_calculated` | `score_calculated: bool` | Boolean `score calculated` flag on `BessPlanningFeatureParcelAggregationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `source_document_id` | `source_document_id: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: str` | Stores `BessPlanningFeatureParcelAggregationResult`'s `cnig profile` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `cnig_profile_sha256` | `cnig_profile_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_complete_result_content_sha256` | `cnig_complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_profile` | `policy_profile: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_sha256` | `policy_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_complete_result_content_sha256` | `policy_complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `application_result_hash_schema_version` | `application_result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `application_complete_result_content_sha256` | `application_complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_parcels_content_sha256` | `source_parcels_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_application_relations_content_sha256` | `source_application_relations_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `relation_assessments_content_sha256` | `relation_assessments_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `parcels_content_sha256` | `parcels_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `relation_assessments` | `relation_assessments: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` via `BessPlanningFeatureParcelAggregationResult`.
- callback/function object: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `isinstance(result, BessPlanningFeatureParcelAggregationResult)`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationResult`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationResult`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_write_artifacts` via `fields(BessPlanningFeatureParcelAggregationResult)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `fields(BessPlanningFeatureParcelAggregationResult)`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.

**Exact class source**

```python
class BessPlanningFeatureParcelAggregationResult:
    result_hash_schema_version: int
    aggregation_scope: str
    policy_scope: str
    local_feature_text_interpreted: bool
    local_regulation_content_interpreted: bool
    legal_conclusion_produced: bool
    parcel_status_aggregated: bool
    parcel_rejection_performed: bool
    score_calculated: bool
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    cnig_complete_result_content_sha256: str
    policy_profile: str
    policy_sha256: str
    policy_complete_result_content_sha256: str
    application_result_hash_schema_version: int
    application_complete_result_content_sha256: str
    source_parcels_content_sha256: str
    source_application_relations_content_sha256: str
    relation_assessments_content_sha256: str
    parcels_content_sha256: str
    complete_result_content_sha256: str
    relation_assessments: pd.DataFrame
    parcels: gpd.GeoDataFrame
```

### `BessPlanningFeatureParcelAggregationArtifactManifest`

**Purpose:** Validates the planning contract carried by `schema_version`, `artifact_kind`, `result_hash_schema_version`, `aggregation_scope`, `policy_scope`, `local_feature_text_interpreted`, `local_regulation_content_interpreted`, `legal_conclusion_produced`, `parcel_status_aggregated`, `parcel_rejection_performed`, `score_calculated`, `source_document_id`, `source_archive_sha256`, `cnig_profile`, `cnig_profile_sha256`, `cnig_complete_result_content_sha256`, `policy_profile`, `policy_sha256`, `policy_complete_result_content_sha256`, `application_result_hash_schema_version`, `application_complete_result_content_sha256`, `source_parcels_content_sha256`, `source_application_relations_content_sha256`, `relation_assessments_content_sha256`, `parcels_content_sha256`, `complete_result_content_sha256`, `artifacts`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `artifact_kind` | `artifact_kind: Literal["BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"]` | Closed or validated `artifact kind` classification on `BessPlanningFeatureParcelAggregationArtifactManifest`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `result_hash_schema_version` | `result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `aggregation_scope` | `aggregation_scope: Literal["PARCEL_POLICY_AGGREGATION_ONLY"]` | Closed or validated `aggregation scope` classification on `BessPlanningFeatureParcelAggregationArtifactManifest`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `policy_scope` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `local_feature_text_interpreted` | `local_feature_text_interpreted: StrictBool` | Boolean `local feature text interpreted` flag on `BessPlanningFeatureParcelAggregationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `local_regulation_content_interpreted` | `local_regulation_content_interpreted: StrictBool` | Boolean `local regulation content interpreted` flag on `BessPlanningFeatureParcelAggregationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `legal_conclusion_produced` | `legal_conclusion_produced: StrictBool` | Boolean `legal conclusion produced` flag on `BessPlanningFeatureParcelAggregationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_status_aggregated` | `parcel_status_aggregated: StrictBool` | Boolean `parcel status aggregated` flag on `BessPlanningFeatureParcelAggregationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_rejection_performed` | `parcel_rejection_performed: StrictBool` | Boolean `parcel rejection performed` flag on `BessPlanningFeatureParcelAggregationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `score_calculated` | `score_calculated: StrictBool` | Boolean `score calculated` flag on `BessPlanningFeatureParcelAggregationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `source_document_id` | `source_document_id: StrictStr` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: StrictStr` | Stores `BessPlanningFeatureParcelAggregationArtifactManifest`'s `cnig profile` value under exact annotation `StrictStr`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `cnig_profile_sha256` | `cnig_profile_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_complete_result_content_sha256` | `cnig_complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_profile` | `policy_profile: StrictStr` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_sha256` | `policy_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_complete_result_content_sha256` | `policy_complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `application_result_hash_schema_version` | `application_result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `application_complete_result_content_sha256` | `application_complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_parcels_content_sha256` | `source_parcels_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_application_relations_content_sha256` | `source_application_relations_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `relation_assessments_content_sha256` | `relation_assessments_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `parcels_content_sha256` | `parcels_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `artifacts` | `artifacts: tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]` | Structured `artifacts` collection owned by `BessPlanningFeatureParcelAggregationArtifactManifest`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Validators (exact source)**

`_validate_manifest`:

```python
def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation artifact schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation result schema")
        if any(
            value is not expected
            for value, expected in (
                (self.local_feature_text_interpreted, False),
                (self.local_regulation_content_interpreted, False),
                (self.legal_conclusion_produced, False),
                (self.parcel_status_aggregated, True),
                (self.parcel_rejection_performed, False),
                (self.score_calculated, False),
            )
        ):
            raise ValueError("parcel aggregation boundary flags are invalid")
        for field in RESULT_SCALAR_FIELDS:
            value = getattr(self, field)
            if field.endswith("sha256"):
                _sha256_string(value, field)
        if (
            type(self.application_result_hash_schema_version) is not int
            or self.application_result_hash_schema_version
            != APPLICATION_RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("application result schema must be exactly 2")
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError("parcel aggregation artifact roles differ")
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("parcel aggregation artifact filename is duplicated")
        return self
```

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.

**Exact class source**

```python
class BessPlanningFeatureParcelAggregationArtifactManifest(_StrictModel):
    schema_version: StrictInt
    artifact_kind: Literal["BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"]
    result_hash_schema_version: StrictInt
    aggregation_scope: Literal["PARCEL_POLICY_AGGREGATION_ONLY"]
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    parcel_status_aggregated: StrictBool
    parcel_rejection_performed: StrictBool
    score_calculated: StrictBool
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_sha256: StrictStr
    cnig_complete_result_content_sha256: StrictStr
    policy_profile: StrictStr
    policy_sha256: StrictStr
    policy_complete_result_content_sha256: StrictStr
    application_result_hash_schema_version: StrictInt
    application_complete_result_content_sha256: StrictStr
    source_parcels_content_sha256: StrictStr
    source_application_relations_content_sha256: StrictStr
    relation_assessments_content_sha256: StrictStr
    parcels_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    artifacts: tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]

    @model_validator(mode="after")
    def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation artifact schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation result schema")
        if any(
            value is not expected
            for value, expected in (
                (self.local_feature_text_interpreted, False),
                (self.local_regulation_content_interpreted, False),
                (self.legal_conclusion_produced, False),
                (self.parcel_status_aggregated, True),
                (self.parcel_rejection_performed, False),
                (self.score_calculated, False),
            )
        ):
            raise ValueError("parcel aggregation boundary flags are invalid")
        for field in RESULT_SCALAR_FIELDS:
            value = getattr(self, field)
            if field.endswith("sha256"):
                _sha256_string(value, field)
        if (
            type(self.application_result_hash_schema_version) is not int
            or self.application_result_hash_schema_version
            != APPLICATION_RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("application result schema must be exactly 2")
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError("parcel aggregation artifact roles differ")
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("parcel aggregation artifact filename is duplicated")
        return self
```


## 6. Functions and methods

### `_exact_string`

**Exact signature**

```python
def _exact_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for exact string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `ValueError(f'{label} must be an exact non-empty string')`.

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

- direct call or construction: `src/landscout/common/bess_application_contract.py::_sha256` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::_optional_official_string` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::_relation_identity_string` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_exact_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_optional_exact_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry._validate_entry` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_official_text` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_strict_string` via `_exact_string`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `AfterValidator(_exact_string)`.

**Complete source-ordered implementation**

```python
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_sha256_string`

**Exact signature**

```python
def _sha256_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for sha256 string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
text
```

**Validation and exceptions**

- Guard with a raise path: `SHA_PATTERN.fullmatch(text) is None`.
- Explicit raise expressions: `ValueError(f'{label} must be a lowercase SHA256')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `SHA_PATTERN.fullmatch`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::BessPlanningFeatureParcelAggregationArtifactRecord._validate_record` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactRecord._validate_record` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_sha256_string`.

**Complete source-ordered implementation**

```python
def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureParcelAggregationArtifactRecord._validate_record`

**Exact signature**

```python
def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
```

**Purpose**

Rejects malformed or inconsistent record; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationArtifactRecord`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `type(self.row_count) is not int or self.row_count < 0`.
- Guard with a raise path: `type(self.size_bytes) is not int or self.size_bytes < 1`.
- Guard with a raise path: `self.geospatial is not expected_geo`.
- Guard with a raise path: `expected_geo`.
- Guard with a raise path: `self.crs is None or signature_crs != self.crs`.
- Guard with a raise path: `self.crs is not None or signature_crs is not None`.
- Explicit raise expressions: `ValueError('artifact geospatial flag differs from its role')`, `ValueError('artifact row_count must be non-negative')`, `ValueError('artifact size_bytes must be positive')`, `ValueError('parcel artifact CRS is missing or inconsistent')`, `ValueError('relation artifact must not declare CRS')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256_string`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be non-negative")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be positive")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geo = self.artifact_role == "PARCELS"
        if self.geospatial is not expected_geo:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        if expected_geo:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("parcel artifact CRS is missing or inconsistent")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("relation artifact must not declare CRS")
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest`

**Exact signature**

```python
def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
```

**Purpose**

Rejects malformed or inconsistent manifest; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationArtifactManifest`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`.
- Guard with a raise path: `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `any((value is not expected for value, expected in ((self.local_feature_text_interpreted, False), (self.local_regulation_content_interpreted, False), (self.legal_conclusion_produced, False), (self.parcel_status_aggregated, True), (self.parcel_rejection_performed, False), (self.score_calculated, False))))`.
- Guard with a raise path: `type(self.application_result_hash_schema_version) is not int or self.application_result_hash_schema_version != APPLICATION_RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `roles != ARTIFACT_ROLES`.
- Guard with a raise path: `len(filenames) != len(set(filenames))`.
- Explicit raise expressions: `ValueError('application result schema must be exactly 2')`, `ValueError('parcel aggregation artifact filename is duplicated')`, `ValueError('parcel aggregation artifact roles differ')`, `ValueError('parcel aggregation boundary flags are invalid')`, `ValueError('unsupported parcel aggregation artifact schema')`, `ValueError('unsupported parcel aggregation result schema')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256_string`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation artifact schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation result schema")
        if any(
            value is not expected
            for value, expected in (
                (self.local_feature_text_interpreted, False),
                (self.local_regulation_content_interpreted, False),
                (self.legal_conclusion_produced, False),
                (self.parcel_status_aggregated, True),
                (self.parcel_rejection_performed, False),
                (self.score_calculated, False),
            )
        ):
            raise ValueError("parcel aggregation boundary flags are invalid")
        for field in RESULT_SCALAR_FIELDS:
            value = getattr(self, field)
            if field.endswith("sha256"):
                _sha256_string(value, field)
        if (
            type(self.application_result_hash_schema_version) is not int
            or self.application_result_hash_schema_version
            != APPLICATION_RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("application result schema must be exactly 2")
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError("parcel aggregation artifact roles differ")
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("parcel aggregation artifact filename is duplicated")
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_value`

**Exact signature**

```python
def _null_value(value: object) -> object:
```

**Purpose**

Private `planning` helper for null value; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
value

None

None
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

- direct call or construction: `src/landscout/common/bess_application_contract.py::_optional_official_string` via `_null_value`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_null_value`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_canonical_value` via `_null_value`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_local_domains` via `_null_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_canonical_value` via `_null_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_null_safe_equal` via `_null_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_null_safe_equal` via `_null_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_value` via `_null_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `_null_value`.

**Complete source-ordered implementation**

```python
def _null_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_value`

**Exact signature**

```python
def _canonical_value(value: object) -> object:
```

**Purpose**

Private `planning` helper for canonical value; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
None

{'coordinate_dimension': dimension, 'wkb_hex': to_wkb(value, hex=True, output_dimension=2, byte_order=1, include_srid=False)}

value.isoformat()

_canonical_value(value.item())

value

int(value)

number

value
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, BaseGeometry)`.
- Guard with a raise path: `isinstance(value, Real)`.
- Guard with a raise path: `dimension != 2`.
- Guard with a raise path: `not math.isfinite(number)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Aggregation payload contains non-finite data')`, `BessPlanningFeatureParcelAggregationError('Parcel aggregation geometry must be canonical 2D')`, `BessPlanningFeatureParcelAggregationError(f'Unsupported aggregation integrity value {type(value).__name__}')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_canonical_sha256` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_sha256` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_frame_rows` via `_canonical_value`.

**Complete source-ordered implementation**

```python
def _canonical_value(value: object) -> object:
    value = _null_value(value)
    if value is None:
        return None
    if isinstance(value, BaseGeometry):
        dimension = int(get_coordinate_dimension(value))
        if dimension != 2:
            raise BessPlanningFeatureParcelAggregationError(
                "Parcel aggregation geometry must be canonical 2D"
            )
        return {
            "coordinate_dimension": dimension,
            "wkb_hex": to_wkb(
                value, hex=True, output_dimension=2, byte_order=1, include_srid=False
            ),
        }
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not math.isfinite(number):
            raise BessPlanningFeatureParcelAggregationError(
                "Aggregation payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeatureParcelAggregationError(
        f"Unsupported aggregation integrity value {type(value).__name__}"
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_payload`

**Exact signature**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for frame payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'schema': deterministic_frame_schema_signature(frame), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': [[_canonical_value(value) for value in row] for row in frame.itertuples(index=False, name=None)]}
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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_result_with_hashes` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_compare_frame` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_component_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_compare_frame` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_zone_mapping_input_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_source_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_normalized_catalogs_input_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `_frame_payload`.

**Complete source-ordered implementation**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    return {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_sha256`

**Exact signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Private `planning` helper for canonical sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(payload).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Aggregation payload is not canonical JSON')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_result_with_hashes` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_page_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_pages_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_index_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_source_selection_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/index_planning_regulation.py::_hits_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_policy_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_factual_structure_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_zone_mapping_input_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_complete_result_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_config_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_source_records_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_section_content_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_input_frame_sha256` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_frame_hash` via `_canonical_sha256`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_structure_result_content_sha256` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_policy_payload` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_validated_config` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_complete_snapshot_is_immutable` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_policy_text_drift` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_source_lock_drift` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order` via `_canonical_sha256`.
- direct call or construction: `tests/unit/test_index_planning_regulation.py::test_canonical_hash_serialization_failure_is_controlled_and_chained` via `regulation_module._canonical_sha256`.
- property/attribute access: `tests/unit/test_index_planning_regulation.py::test_canonical_hash_serialization_failure_is_controlled_and_chained` via `regulation_module._canonical_sha256`.

**Complete source-ordered implementation**

```python
def _canonical_sha256(value: object) -> str:
    try:
        payload = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation payload is not canonical JSON"
        ) from error
    return sha256(payload).hexdigest()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_sha256`

**Exact signature**

```python
def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
```

**Purpose**

Private `planning` helper for frame sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': domain, 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'frame': _frame_payload(frame)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` via `_frame_sha256`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_frame_sha256`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_source_locks` via `_frame_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_frame_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_result_with_hashes` via `_frame_sha256`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._frame_sha256`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._frame_sha256`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._frame_sha256`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._frame_sha256`.

**Complete source-ordered implementation**

```python
def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "frame": _frame_payload(frame),
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_feature_id`

**Exact signature**

```python
def _validate_feature_id(value: object) -> str:
```

**Purpose**

Rejects malformed or inconsistent feature id; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip() or (value in NULL_LITERALS) or PurePosixPath(value).is_absolute() or PureWindowsPath(value).is_absolute()`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Feature ID is not an exact portable string')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_json_ids` via `_validate_feature_id`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_json_ids` via `_validate_feature_id`.

**Complete source-ordered implementation**

```python
def _validate_feature_id(value: object) -> str:
    if (
        not isinstance(value, str)
        or not value
        or value != value.strip()
        or value in NULL_LITERALS
        or PurePosixPath(value).is_absolute()
        or PureWindowsPath(value).is_absolute()
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Feature ID is not an exact portable string"
        )
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_json_ids`

**Exact signature**

```python
def _json_ids(values: list[object]) -> str:
```

**Purpose**

Private `planning` helper for json ids; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(',', ':'))
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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` via `_json_ids`.

**Complete source-ordered implementation**

```python
def _json_ids(values: list[object]) -> str:
    ids = sorted({_validate_feature_id(value) for value in values})
    return json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_json_ids`

**Exact signature**

```python
def _validate_json_ids(value: object, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent json ids; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str)`.
- Guard with a raise path: `not isinstance(parsed, list)`.
- Guard with a raise path: `len(ids) != len(set(ids)) or ids != sorted(ids) or value != canonical`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError(f'{label} is not canonical')`, `BessPlanningFeatureParcelAggregationError(f'{label} must be a JSON array')`, `BessPlanningFeatureParcelAggregationError(f'{label} must be canonical JSON')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_local_domains` via `_validate_json_ids`.

**Complete source-ordered implementation**

```python
def _validate_json_ids(value: object, label: str) -> None:
    if not isinstance(value, str):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        )
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        ) from error
    if not isinstance(parsed, list):
        raise BessPlanningFeatureParcelAggregationError(f"{label} must be a JSON array")
    ids = [_validate_feature_id(item) for item in parsed]
    canonical = json.dumps(
        sorted(set(ids)),
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
    )
    if len(ids) != len(set(ids)) or ids != sorted(ids) or value != canonical:
        raise BessPlanningFeatureParcelAggregationError(f"{label} is not canonical")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcel_frame`

**Exact signature**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent parcel frame; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `'parcel_id' not in frame.columns`.
- Guard with a raise path: `parcel_ids.isna().any() or parcel_ids.duplicated().any() or any((not isinstance(value, str) or not value or value != value.strip() or (value in NULL_LITERALS) for value in parcel_ids))`.
- Guard with a raise path: `geometry_name not in frame.columns`.
- Guard with a raise path: `frame.crs is None`.
- Guard with a raise path: `geometry is None or geometry.is_empty or (not geometry.is_valid) or (geometry.geom_type not in {'Polygon', 'MultiPolygon'}) or (int(get_coordinate_dimension(geometry)) != 2)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError(f'{label} contains duplicate columns')`, `BessPlanningFeatureParcelAggregationError(f'{label} geometry or CRS contract is invalid')`, `BessPlanningFeatureParcelAggregationError(f'{label} lacks parcel_id')`, `BessPlanningFeatureParcelAggregationError(f'{label} must be a GeoDataFrame')`, `BessPlanningFeatureParcelAggregationError(f'{label} parcel IDs must be unique exact strings')`, `BessPlanningFeatureParcelAggregationError(f'{label} requires valid canonical 2D polygon geometry')`, `ValueError('CRS is absent')`, `ValueError('active geometry column is absent')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` via `_validate_parcel_frame`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_validate_parcel_frame`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_parcel_frame`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_upstream_result` via `_validate_parcel_frame`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_validate_assessment_result` via `_validate_parcel_frame`.
- direct call or construction: `src/landscout/stages/assess_road_proximity_coverage.py::_assess_road_proximity_coverage` via `_validate_parcel_frame`.

**Complete source-ordered implementation**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be a GeoDataFrame"
        )
    if frame.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} contains duplicate columns"
        )
    if "parcel_id" not in frame.columns:
        raise BessPlanningFeatureParcelAggregationError(f"{label} lacks parcel_id")
    try:
        geometry_name = frame.geometry.name
        if geometry_name not in frame.columns:
            raise ValueError("active geometry column is absent")
        if frame.crs is None:
            raise ValueError("CRS is absent")
        CRS.from_user_input(frame.crs)
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} geometry or CRS contract is invalid"
        ) from error
    parcel_ids = frame["parcel_id"]
    if (
        parcel_ids.isna().any()
        or parcel_ids.duplicated().any()
        or any(
            not isinstance(value, str)
            or not value
            or value != value.strip()
            or value in NULL_LITERALS
            for value in parcel_ids
        )
    ):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} parcel IDs must be unique exact strings"
        )
    for geometry in frame.geometry.array:
        if (
            geometry is None
            or geometry.is_empty
            or not geometry.is_valid
            or geometry.geom_type not in {"Polygon", "MultiPolygon"}
            or int(get_coordinate_dimension(geometry)) != 2
        ):
            raise BessPlanningFeatureParcelAggregationError(
                f"{label} requires valid canonical 2D polygon geometry"
            )
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_application_relations`

**Exact signature**

```python
def _validate_application_relations(
    frame: object,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> pd.DataFrame:
```

**Purpose**

Rejects malformed or inconsistent application relations; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame) or isinstance(frame, gpd.GeoDataFrame)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Application relations must be a DataFrame')`, `BessPlanningFeatureParcelAggregationError(str(error))`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` via `_validate_application_relations`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_validate_application_relations`.

**Complete source-ordered implementation**

```python
def _validate_application_relations(
    frame: object,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> pd.DataFrame:
    if not isinstance(frame, pd.DataFrame) or isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            "Application relations must be a DataFrame"
        )
    try:
        validate_bess_application_relation_frame(
            frame,
            label="application relations",
            policy_profile=application.policy_profile,
            policy_sha256=application.policy_sha256,
            policy_result_sha256=application.policy_complete_result_content_sha256,
            source_document_id=application.source_document_id,
            source_archive_sha256=application.source_archive_sha256,
            cnig_profile=application.cnig_profile,
            cnig_profile_sha256=application.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_parcel_areas`

**Exact signature**

```python
def _validate_relation_parcel_areas(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent relation parcel areas; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not np.isfinite(areas).all() or (areas <= 0).any()`.
- Guard with a raise path: `parcels.geometry.name != geometry_name`.
- Guard with a raise path: `measured is None`.
- Guard with a raise path: `isinstance(stored, bool) or not isinstance(stored, Real)`.
- Guard with a raise path: `not math.isfinite(actual)`.
- Guard with a raise path: `abs(actual - measured) > tolerance`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('parcel active geometry changed during metric validation')`, `BessPlanningFeatureParcelAggregationError('parcel metric areas must be finite and positive')`, `BessPlanningFeatureParcelAggregationError('parcel metric-area calculation failed')`, `BessPlanningFeatureParcelAggregationError('relation parcel metric area differs from parcel geometry')`, `BessPlanningFeatureParcelAggregationError('relation parcel metric area must be finite')`, `BessPlanningFeatureParcelAggregationError('relation parcel metric area must be numeric')`, `BessPlanningFeatureParcelAggregationError('relation references an unknown parcel for metric area')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `(areas <= 0).any`, `areas.tolist`, `calculation.geometry.area.to_numpy`, `calculation.to_crs`, `np.isfinite(areas).all`, `parcels.geometry.copy`, `relations[['parcel_id', 'parcel_metric_area_m2']].itertuples`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` via `_validate_relation_parcel_areas`.

**Complete source-ordered implementation**

```python
def _validate_relation_parcel_areas(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> None:
    geometry_name = parcels.geometry.name
    calculation = gpd.GeoDataFrame(
        {"parcel_id": parcels["parcel_id"].copy(deep=True)},
        geometry=parcels.geometry.copy(deep=True),
        crs=parcels.crs,
        index=parcels.index.copy(deep=True),
    )
    try:
        if not CRS.from_user_input(calculation.crs).equals(CRS.from_epsg(2154)):
            calculation = calculation.to_crs("EPSG:2154")
        areas = calculation.geometry.area.to_numpy(dtype="float64")
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "parcel metric-area calculation failed"
        ) from error
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise BessPlanningFeatureParcelAggregationError(
            "parcel metric areas must be finite and positive"
        )
    expected = dict(zip(calculation["parcel_id"].tolist(), areas.tolist(), strict=True))
    for parcel_id, stored in relations[
        ["parcel_id", "parcel_metric_area_m2"]
    ].itertuples(index=False, name=None):
        measured = expected.get(parcel_id)
        if measured is None:
            raise BessPlanningFeatureParcelAggregationError(
                "relation references an unknown parcel for metric area"
            )
        if isinstance(stored, bool) or not isinstance(stored, Real):
            raise BessPlanningFeatureParcelAggregationError(
                "relation parcel metric area must be numeric"
            )
        actual = float(stored)
        if not math.isfinite(actual):
            raise BessPlanningFeatureParcelAggregationError(
                "relation parcel metric area must be finite"
            )
        tolerance = technical_overlay_tolerance(max(abs(actual), measured))
        if abs(actual - measured) > tolerance:
            raise BessPlanningFeatureParcelAggregationError(
                "relation parcel metric area differs from parcel geometry"
            )
    if parcels.geometry.name != geometry_name:
        raise BessPlanningFeatureParcelAggregationError(
            "parcel active geometry changed during metric validation"
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_local_domains`

**Exact signature**

```python
def _validate_local_domains(parcels: gpd.GeoDataFrame, relations: pd.DataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent local domains; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `aggregation_status not in AGGREGATION_STATUSES`.
- Guard with a raise path: `aggregation_status == 'AGGREGATED_EXACT_POLICY'`.
- Guard with a raise path: `role not in RELATION_ROLES`.
- Guard with a raise path: `selected is not (role == 'SELECTED_CONTROLLING')`.
- Guard with a raise path: `aggregation_status not in AGGREGATION_STATUSES`.
- Guard with a raise path: `aggregation_status == 'AGGREGATED_EXACT_POLICY'`.
- Guard with a raise path: `status not in ALLOWED_PRECHECK_STATUSES`.
- Guard with a raise path: `confidence not in ALLOWED_CONFIDENCES`.
- Guard with a raise path: `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0`.
- Guard with a raise path: `any((value is not None for value in (status, confidence, priority)))`.
- Guard with a raise path: `status not in ALLOWED_PRECHECK_STATUSES`.
- Guard with a raise path: `confidence not in ALLOWED_CONFIDENCES`.
- Guard with a raise path: `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0`.
- Guard with a raise path: `any((value is not None for value in (status, confidence, priority)))`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('non-decision parcel contains an invented decision')`, `BessPlanningFeatureParcelAggregationError('non-decision relation contains an invented parcel decision')`, `BessPlanningFeatureParcelAggregationError('parcel aggregation status is outside the allowed domain')`, `BessPlanningFeatureParcelAggregationError('parcel confidence is outside the allowed domain')`, `BessPlanningFeatureParcelAggregationError('parcel precheck status is outside the allowed domain')`, `BessPlanningFeatureParcelAggregationError('parcel relation role is outside the allowed domain')`, `BessPlanningFeatureParcelAggregationError('parcel relation selected flag contradicts its role')`, `BessPlanningFeatureParcelAggregationError('parcel status priority must be a positive integer')`, `BessPlanningFeatureParcelAggregationError('relation aggregation status is outside the allowed domain')`, `BessPlanningFeatureParcelAggregationError('relation parcel confidence is outside the allowed domain')`, `BessPlanningFeatureParcelAggregationError('relation parcel priority must be a positive integer')`, `BessPlanningFeatureParcelAggregationError('relation parcel status is outside the allowed domain')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_validate_local_domains`.

**Complete source-ordered implementation**

```python
def _validate_local_domains(parcels: gpd.GeoDataFrame, relations: pd.DataFrame) -> None:
    for row in parcels.to_dict("records"):
        aggregation_status = row["bess_cnig_parcel_aggregation_status"]
        if aggregation_status not in AGGREGATION_STATUSES:
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation status is outside the allowed domain"
            )
        status = _null_value(row["bess_cnig_parcel_precheck_status"])
        confidence = _null_value(row["bess_cnig_parcel_precheck_confidence"])
        priority = _null_value(row["bess_cnig_parcel_status_priority"])
        if aggregation_status == "AGGREGATED_EXACT_POLICY":
            if status not in ALLOWED_PRECHECK_STATUSES:
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel precheck status is outside the allowed domain"
                )
            if confidence not in ALLOWED_CONFIDENCES:
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel confidence is outside the allowed domain"
                )
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel status priority must be a positive integer"
                )
        elif any(value is not None for value in (status, confidence, priority)):
            raise BessPlanningFeatureParcelAggregationError(
                "non-decision parcel contains an invented decision"
            )
        for column in (
            "bess_cnig_selected_feature_ids_json",
            "bess_cnig_unresolved_feature_ids_json",
            "bess_cnig_touch_only_feature_ids_json",
        ):
            _validate_json_ids(row[column], column)
    for row in relations.to_dict("records"):
        role = row["bess_cnig_parcel_relation_role"]
        if role not in RELATION_ROLES:
            raise BessPlanningFeatureParcelAggregationError(
                "parcel relation role is outside the allowed domain"
            )
        selected = row["bess_cnig_selected_for_parcel_status"]
        if selected is not (role == "SELECTED_CONTROLLING"):
            raise BessPlanningFeatureParcelAggregationError(
                "parcel relation selected flag contradicts its role"
            )
        aggregation_status = row["bess_cnig_resulting_parcel_aggregation_status"]
        if aggregation_status not in AGGREGATION_STATUSES:
            raise BessPlanningFeatureParcelAggregationError(
                "relation aggregation status is outside the allowed domain"
            )
        status = _null_value(row["bess_cnig_resulting_parcel_precheck_status"])
        confidence = _null_value(row["bess_cnig_resulting_parcel_precheck_confidence"])
        priority = _null_value(row["bess_cnig_resulting_parcel_status_priority"])
        if aggregation_status == "AGGREGATED_EXACT_POLICY":
            if status not in ALLOWED_PRECHECK_STATUSES:
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel status is outside the allowed domain"
                )
            if confidence not in ALLOWED_CONFIDENCES:
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel confidence is outside the allowed domain"
                )
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel priority must be a positive integer"
                )
        elif any(value is not None for value in (status, confidence, priority)):
            raise BessPlanningFeatureParcelAggregationError(
                "non-decision relation contains an invented parcel decision"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_relation_priority`

**Exact signature**

```python
def _relation_priority(row: dict[str, object]) -> int:
```

**Purpose**

Private `planning` helper for relation priority; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
int(value)
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Applied relation priority must be a positive integer')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` via `_relation_priority`.

**Complete source-ordered implementation**

```python
def _relation_priority(row: dict[str, object]) -> int:
    value = row["bess_cnig_status_priority"]
    if isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0:
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation priority must be a positive integer"
        )
    return int(value)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_parcel_summary`

**Exact signature**

```python
def _parcel_summary(
    parcel_relations: list[dict[str, object]],
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[dict[str, object], list[dict[str, object]]]:
```

**Purpose**

Private `planning` helper for parcel summary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[dict[str, object], list[dict[str, object]]]`.
- Every observed return expression is reproduced without truncation:
```python
(summary, assessed)
```

**Validation and exceptions**

- Guard with a raise path: `len(controlling) + len(contextual) != len(parcel_relations)`.
- Guard with a raise path: `len(exact) + len(unresolved) != len(controlling)`.
- Guard with a raise path: `any((len(statuses) != 1 for statuses in priority_statuses.values())) or any((len(priority_values) != 1 for priority_values in status_priorities.values()))`.
- Guard with a raise path: `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0 or (not isinstance(status, str))`.
- Guard with a raise path: `controlling`.
- Guard with a raise path: `any((value not in CONFIDENCE_RANK for value in confidences))`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Applied relation status and priority are invalid')`, `BessPlanningFeatureParcelAggregationError('Applied relation status and priority mapping is not one-to-one')`, `BessPlanningFeatureParcelAggregationError('Controlling application status is invalid')`, `BessPlanningFeatureParcelAggregationError('Relation type is outside the aggregation contract')`, `BessPlanningFeatureParcelAggregationError('Selected relation confidence is invalid')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` via `_parcel_summary`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::intersect_parcels_with_gpu_zoning` via `_parcel_summary`.

**Complete source-ordered implementation**

```python
def _parcel_summary(
    parcel_relations: list[dict[str, object]],
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    controlling = [
        row
        for row in parcel_relations
        if row["relation_type"] in CONTROLLING_RELATION_TYPES
    ]
    contextual = [
        row
        for row in parcel_relations
        if row["relation_type"] in CONTEXT_RELATION_TYPES
    ]
    if len(controlling) + len(contextual) != len(parcel_relations):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation type is outside the aggregation contract"
        )
    exact = [
        row
        for row in controlling
        if row["bess_cnig_policy_application_status"] == "APPLIED_EXACT_POLICY"
    ]
    unresolved = [
        row
        for row in controlling
        if row["bess_cnig_policy_application_status"] == "UNRESOLVED_CODE_PAIR"
    ]
    if len(exact) + len(unresolved) != len(controlling):
        raise BessPlanningFeatureParcelAggregationError(
            "Controlling application status is invalid"
        )
    selected_status: str | None = None
    selected_confidence: str | None = None
    selected_priority: int | None = None
    priorities: list[int] = []
    priority_statuses: dict[int, set[str]] = {}
    status_priorities: dict[str, set[int]] = {}
    for row in exact:
        priority = row["bess_cnig_status_priority"]
        status = row["bess_cnig_precheck_status"]
        if (
            isinstance(priority, bool)
            or not isinstance(priority, Integral)
            or int(priority) <= 0
            or not isinstance(status, str)
        ):
            raise BessPlanningFeatureParcelAggregationError(
                "Applied relation status and priority are invalid"
            )
        normalized_priority = int(priority)
        priorities.append(normalized_priority)
        priority_statuses.setdefault(normalized_priority, set()).add(status)
        status_priorities.setdefault(status, set()).add(normalized_priority)
    if any(len(statuses) != 1 for statuses in priority_statuses.values()) or any(
        len(priority_values) != 1 for priority_values in status_priorities.values()
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation status and priority mapping is not one-to-one"
        )
    if unresolved:
        aggregation_status = "UNRESOLVED_CONTROLLING_CODE_PAIR"
    elif controlling:
        aggregation_status = "AGGREGATED_EXACT_POLICY"
        selected_priority = max(priorities)
        selected_status = next(iter(priority_statuses[selected_priority]))
        confidences = [
            str(row["bess_cnig_precheck_confidence"])
            for row in exact
            if row["bess_cnig_precheck_status"] == selected_status
            and _relation_priority(row) == selected_priority
        ]
        if any(value not in CONFIDENCE_RANK for value in confidences):
            raise BessPlanningFeatureParcelAggregationError(
                "Selected relation confidence is invalid"
            )
        selected_confidence = min(confidences, key=CONFIDENCE_RANK.__getitem__)
    elif parcel_relations:
        aggregation_status = "TOUCH_ONLY_RELATIONS_ONLY"
    else:
        aggregation_status = "NO_PLANNING_FEATURE_RELATION"

    assessed: list[dict[str, object]] = []
    for row in parcel_relations:
        if row["relation_type"] in CONTEXT_RELATION_TYPES:
            role = "TOUCH_ONLY_CONTEXT"
        elif aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR":
            role = (
                "UNRESOLVED_CONTROLLING"
                if row["bess_cnig_policy_application_status"] == "UNRESOLVED_CODE_PAIR"
                else "DEFERRED_BY_UNRESOLVED_CONTROLLING"
            )
        else:
            role = (
                "SELECTED_CONTROLLING"
                if row["bess_cnig_precheck_status"] == selected_status
                and _relation_priority(row) == selected_priority
                else "LOWER_PRIORITY_CONTROLLING"
            )
        assessed.append(
            {
                **row,
                "bess_cnig_parcel_relation_role": role,
                "bess_cnig_selected_for_parcel_status": role == "SELECTED_CONTROLLING",
                "bess_cnig_resulting_parcel_aggregation_status": aggregation_status,
                "bess_cnig_resulting_parcel_precheck_status": selected_status,
                "bess_cnig_resulting_parcel_precheck_confidence": selected_confidence,
                "bess_cnig_resulting_parcel_status_priority": selected_priority,
            }
        )
    roles = [row["bess_cnig_parcel_relation_role"] for row in assessed]
    exact_statuses = {str(row["bess_cnig_precheck_status"]) for row in exact}
    summary: dict[str, object] = {
        "bess_cnig_parcel_aggregation_status": aggregation_status,
        "bess_cnig_parcel_precheck_status": selected_status,
        "bess_cnig_parcel_precheck_confidence": selected_confidence,
        "bess_cnig_parcel_status_priority": selected_priority,
        "bess_cnig_controlling_relation_count": len(controlling),
        "bess_cnig_exact_controlling_relation_count": len(exact),
        "bess_cnig_unresolved_controlling_relation_count": len(unresolved),
        "bess_cnig_touch_only_relation_count": len(contextual),
        "bess_cnig_selected_relation_count": roles.count("SELECTED_CONTROLLING"),
        "bess_cnig_lower_priority_controlling_relation_count": roles.count(
            "LOWER_PRIORITY_CONTROLLING"
        ),
        "bess_cnig_distinct_exact_status_count": len(exact_statuses),
        "bess_cnig_multiple_exact_statuses": len(exact_statuses) > 1,
        "bess_cnig_selected_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "SELECTED_CONTROLLING"
            ]
        ),
        "bess_cnig_unresolved_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "UNRESOLVED_CONTROLLING"
            ]
        ),
        "bess_cnig_touch_only_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "TOUCH_ONLY_CONTEXT"
            ]
        ),
        "bess_cnig_confidence_aggregation_method": CONFIDENCE_METHOD,
        "bess_cnig_formal_review_required": True,
        "bess_cnig_aggregation_scope": AGGREGATION_SCOPE,
        "bess_cnig_policy_scope": POLICY_SCOPE,
        "bess_cnig_local_feature_text_interpreted": False,
        "bess_cnig_local_regulation_content_interpreted": False,
        "bess_cnig_legal_conclusion_produced": False,
        "bess_cnig_parcel_status_aggregated": True,
        "bess_cnig_parcel_rejection_performed": False,
        "bess_cnig_score_calculated": False,
        "bess_cnig_policy_profile": application.policy_profile,
        "bess_cnig_policy_sha256": application.policy_sha256,
        "bess_cnig_policy_result_sha256": application.policy_complete_result_content_sha256,
        "bess_cnig_application_result_sha256": application.complete_result_content_sha256,
    }
    return summary, assessed
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_assign_columns`

**Exact signature**

```python
def _assign_columns(
    frame: pd.DataFrame, rows: list[dict[str, object]], columns: tuple[str, ...]
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for assign columns; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
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
- In-memory mutation: `frame[column]`.
- Input mutation: `frame[column]`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_aggregate_frames` via `_assign_columns`.

**Complete source-ordered implementation**

```python
def _assign_columns(
    frame: pd.DataFrame, rows: list[dict[str, object]], columns: tuple[str, ...]
) -> pd.DataFrame:
    for column in columns:
        values = [row[column] for row in rows]
        if (
            column in PARCEL_INTEGER_COLUMNS
            or column == "bess_cnig_resulting_parcel_status_priority"
        ):
            frame[column] = pd.array(values, dtype="Int64")
        elif (
            column in PARCEL_BOOL_COLUMNS
            or column == "bess_cnig_selected_for_parcel_status"
        ):
            frame[column] = pd.array(values, dtype="bool")
        else:
            frame[column] = pd.array(values, dtype="str")
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_aggregate_frames`

**Exact signature**

```python
def _aggregate_frames(
    source_parcels: gpd.GeoDataFrame,
    source_relations: pd.DataFrame,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame]:
```

**Purpose**

Combines source-bound relation evidence into frames; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[gpd.GeoDataFrame, pd.DataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(parcels, assessments)
```

**Validation and exceptions**

- Guard with a raise path: `any((column in source_parcels.columns for column in PARCEL_COLUMNS)) or any((column in source_relations.columns for column in RELATION_COLUMNS))`.
- Guard with a raise path: `'parcel_id' not in source_parcels or 'parcel_id' not in source_relations`.
- Guard with a raise path: `any((value not in known for value in source_relations['parcel_id']))`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Aggregation columns already exist on source inputs')`, `BessPlanningFeatureParcelAggregationError('Aggregation inputs lack parcel_id')`, `BessPlanningFeatureParcelAggregationError('Relation references an unknown parcel')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_validate_relation_parcel_areas`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` via `_aggregate_frames`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_aggregate_frames`.

**Complete source-ordered implementation**

```python
def _aggregate_frames(
    source_parcels: gpd.GeoDataFrame,
    source_relations: pd.DataFrame,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame]:
    _validate_parcel_frame(source_parcels, "source parcels")
    _validate_application_relations(source_relations, application)
    _validate_relation_parcel_areas(source_parcels, source_relations)
    if any(column in source_parcels.columns for column in PARCEL_COLUMNS) or any(
        column in source_relations.columns for column in RELATION_COLUMNS
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation columns already exist on source inputs"
        )
    if "parcel_id" not in source_parcels or "parcel_id" not in source_relations:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation inputs lack parcel_id"
        )
    parcel_ids = source_parcels["parcel_id"]
    known = set(parcel_ids.tolist())
    if any(value not in known for value in source_relations["parcel_id"]):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation references an unknown parcel"
        )
    relation_rows = source_relations.to_dict("records")
    grouped: dict[str, list[dict[str, object]]] = {
        value: [] for value in parcel_ids.tolist()
    }
    for row in relation_rows:
        grouped[str(row["parcel_id"])].append(row)
    summaries: list[dict[str, object]] = []
    assessment_rows: list[dict[str, object]] = []
    for parcel_id in parcel_ids.tolist():
        summary, assessed = _parcel_summary(grouped[parcel_id], application)
        summaries.append(summary)
        assessment_rows.extend(assessed)
    parcels = source_parcels.copy(deep=True)
    _assign_columns(parcels, summaries, PARCEL_COLUMNS)
    parcels = gpd.GeoDataFrame(
        parcels, geometry=source_parcels.geometry.name, crs=source_parcels.crs
    )
    assessments = source_relations.copy(deep=True)
    # assessed rows were grouped by parcel; restore exact source relation order by stable source position.
    cursor: dict[str, int] = {parcel_id: 0 for parcel_id in grouped}
    assessed_by_parcel: dict[str, list[dict[str, object]]] = {
        parcel_id: [] for parcel_id in grouped
    }
    for row in assessment_rows:
        assessed_by_parcel[str(row["parcel_id"])].append(row)
    ordered_assessed: list[dict[str, object]] = []
    for source_row in relation_rows:
        parcel_id = str(source_row["parcel_id"])
        item = assessed_by_parcel[parcel_id][cursor[parcel_id]]
        cursor[parcel_id] += 1
        ordered_assessed.append(item)
    _assign_columns(assessments, ordered_assessed, RELATION_COLUMNS)
    return parcels, assessments
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_metadata`

**Exact signature**

```python
def _component_metadata(
    result: BessPlanningFeatureParcelAggregationResult,
) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for component metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{field: getattr(result, field) for field in RESULT_SCALAR_FIELDS if field not in {'relation_assessments_content_sha256', 'parcels_content_sha256', 'complete_result_content_sha256'}}
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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_result_with_hashes` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_component_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_complete_result_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_complete_result_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_complete_sha256` via `_component_metadata`.

**Complete source-ordered implementation**

```python
def _component_metadata(
    result: BessPlanningFeatureParcelAggregationResult,
) -> dict[str, object]:
    return {
        field: getattr(result, field)
        for field in RESULT_SCALAR_FIELDS
        if field
        not in {
            "relation_assessments_content_sha256",
            "parcels_content_sha256",
            "complete_result_content_sha256",
        }
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Exact signature**

```python
def _result_with_hashes(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Private `planning` helper for result with hashes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(components, complete_result_content_sha256=complete)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_feature_id_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_feature_id_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_surface_touch_with_positive_area` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_surface_touch_with_positive_area` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_replace_application_frame` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_replace_application_frame` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_referenced_lineage_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_referenced_lineage_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_swap_referenced_feature_values` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_swap_referenced_feature_values` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `coding_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `coding_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `policy_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `policy_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_compatible_policy_mutation` via `module._result_with_hashes`.

**Complete source-ordered implementation**

```python
def _result_with_hashes(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    metadata = _component_metadata(result)
    relations_hash = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.relation_assessments",
            **metadata,
            "frame": _frame_payload(result.relation_assessments),
        }
    )
    parcels_hash = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.parcels",
            **metadata,
            "frame": _frame_payload(result.parcels),
        }
    )
    components = replace(
        result,
        relation_assessments_content_sha256=relations_hash,
        parcels_content_sha256=parcels_hash,
    )
    complete = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.result",
            **metadata,
            "relation_assessments_content_sha256": relations_hash,
            "parcels_content_sha256": parcels_hash,
        }
    )
    return replace(components, complete_result_content_sha256=complete)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

**Exact signature**

```python
def _build_result(
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Constructs result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
_result_with_hashes(result)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_frame_sha256`, `_result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `_build_result`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_build_result`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `_build_result`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_build_result`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_build_result`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `_build_result`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `_build_result`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `module._build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_surface_touch_semantic_corruption_result` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_surface_touch_semantic_corruption_result` via `module._build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `module._build_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._build_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._build_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `module._build_result`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `policy_module._build_result`.
- property/attribute access: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `policy_module._build_result`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `interpret_module._build_result`.
- property/attribute access: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `interpret_module._build_result`.

**Complete source-ordered implementation**

```python
def _build_result(
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    parcels, assessments = _aggregate_frames(
        source_parcels, application.relations, application
    )
    result = BessPlanningFeatureParcelAggregationResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        aggregation_scope=AGGREGATION_SCOPE,
        policy_scope=POLICY_SCOPE,
        local_feature_text_interpreted=False,
        local_regulation_content_interpreted=False,
        legal_conclusion_produced=False,
        parcel_status_aggregated=True,
        parcel_rejection_performed=False,
        score_calculated=False,
        source_document_id=application.source_document_id,
        source_archive_sha256=application.source_archive_sha256,
        cnig_profile=application.cnig_profile,
        cnig_profile_sha256=application.cnig_profile_sha256,
        cnig_complete_result_content_sha256=application.cnig_complete_result_content_sha256,
        policy_profile=application.policy_profile,
        policy_sha256=application.policy_sha256,
        policy_complete_result_content_sha256=application.policy_complete_result_content_sha256,
        application_result_hash_schema_version=application.result_hash_schema_version,
        application_complete_result_content_sha256=application.complete_result_content_sha256,
        source_parcels_content_sha256=_frame_sha256(
            source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
        ),
        source_application_relations_content_sha256=_frame_sha256(
            application.relations,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
        relation_assessments_content_sha256="",
        parcels_content_sha256="",
        complete_result_content_sha256="",
        relation_assessments=assessments,
        parcels=parcels,
    )
    return _result_with_hashes(result)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_frame`

**Exact signature**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

**Purpose**

Private `planning` helper for compare frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `_frame_payload(actual) != _frame_payload(expected)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError(f'{label} differs from deterministic aggregation')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_compare_frame`.

**Complete source-ordered implementation**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} differs from deterministic aggregation"
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Exact signature**

```python
def _validate_result_envelope(
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent result envelope; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(result, BessPlanningFeatureParcelAggregationResult)`.
- Guard with a raise path: `type(result.result_hash_schema_version) is not int or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `result.aggregation_scope != AGGREGATION_SCOPE or result.policy_scope != POLICY_SCOPE`.
- Guard with a raise path: `type(result.application_result_hash_schema_version) is not int or result.application_result_hash_schema_version != APPLICATION_RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `any((value is not expected for value, expected in ((result.local_feature_text_interpreted, False), (result.local_regulation_content_interpreted, False), (result.legal_conclusion_produced, False), (result.parcel_status_aggregated, True), (result.parcel_rejection_performed, False), (result.score_calculated, False))))`.
- Guard with a raise path: `not isinstance(result.parcels, gpd.GeoDataFrame) or not isinstance(result.relation_assessments, pd.DataFrame) or isinstance(result.relation_assessments, gpd.GeoDataFrame)`.
- Guard with a raise path: `result.parcels.columns.duplicated().any()`.
- Guard with a raise path: `result.relation_assessments.columns.duplicated().any()`.
- Guard with a raise path: `tuple(result.parcels.columns[-len(PARCEL_COLUMNS):]) != PARCEL_COLUMNS or tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS):]) != RELATION_COLUMNS`.
- Guard with a raise path: `str(result.relation_assessments['bess_cnig_selected_for_parcel_status'].dtype) != 'bool' or str(result.relation_assessments['bess_cnig_resulting_parcel_status_priority'].dtype) != 'Int64'`.
- Guard with a raise path: `result.source_parcels_content_sha256 != _frame_sha256(source_parcels, 'landscout.bess_cnig_parcel_aggregation.source_parcels')`.
- Guard with a raise path: `result.source_application_relations_content_sha256 != _frame_sha256(source_relations, 'landscout.bess_cnig_parcel_aggregation.source_application_relations')`.
- Guard with a raise path: `field.endswith('sha256')`.
- Guard with a raise path: `str(result.parcels[column].dtype) != 'str'`.
- Guard with a raise path: `str(result.parcels[column].dtype) != 'Int64'`.
- Guard with a raise path: `str(result.parcels[column].dtype) != 'bool'`.
- Guard with a raise path: `str(result.relation_assessments[column].dtype) != 'str'`.
- Guard with a raise path: `getattr(result, field) != getattr(rebuilt, field)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('aggregation output frame types are invalid')`, `BessPlanningFeatureParcelAggregationError('aggregation output suffix schema is invalid')`, `BessPlanningFeatureParcelAggregationError('application result schema must be exactly 2')`, `BessPlanningFeatureParcelAggregationError('parcel aggregation bool dtype is invalid')`, `BessPlanningFeatureParcelAggregationError('parcel aggregation flags are invalid')`, `BessPlanningFeatureParcelAggregationError('parcel aggregation integer dtype is invalid')`, `BessPlanningFeatureParcelAggregationError('parcel aggregation scope is invalid')`, `BessPlanningFeatureParcelAggregationError('parcel aggregation string dtype is invalid')`, `BessPlanningFeatureParcelAggregationError('parcel output contains duplicate columns')`, `BessPlanningFeatureParcelAggregationError('relation assessment dtype is invalid')`, `BessPlanningFeatureParcelAggregationError('relation assessment string dtype is invalid')`, `BessPlanningFeatureParcelAggregationError('relation assessments contain duplicate columns')`, `BessPlanningFeatureParcelAggregationError('result has the wrong type')`, `BessPlanningFeatureParcelAggregationError('source application relation content SHA256 is invalid')`, `BessPlanningFeatureParcelAggregationError('source parcel content SHA256 is invalid')`, `BessPlanningFeatureParcelAggregationError('unsupported parcel aggregation result schema')`, `BessPlanningFeatureParcelAggregationError(f'{field} is invalid')`, `BessPlanningFeatureParcelAggregationError(str(error))`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_frame_sha256`, `_result_with_hashes`, `_sha256_string`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result_envelope` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result_envelope` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result_envelope` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_result_schema_two_remains_accepted` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_result_schema_two_remains_accepted` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_m_and_zm_application_geometries_are_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_m_and_zm_application_geometries_are_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_accepts_only_current_policy_and_cnig_source_schemas` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_accepts_only_current_policy_and_cnig_source_schemas` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._validate_result_envelope`.

**Complete source-ordered implementation**

```python
def _validate_result_envelope(
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
    if not isinstance(result, BessPlanningFeatureParcelAggregationResult):
        raise BessPlanningFeatureParcelAggregationError("result has the wrong type")
    if (
        type(result.result_hash_schema_version) is not int
        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "unsupported parcel aggregation result schema"
        )
    if (
        result.aggregation_scope != AGGREGATION_SCOPE
        or result.policy_scope != POLICY_SCOPE
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation scope is invalid"
        )
    for field in RESULT_SCALAR_FIELDS:
        if field.endswith("sha256"):
            try:
                _sha256_string(getattr(result, field), field)
            except ValueError as error:
                raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    for value, label in (
        (result.source_document_id, "source_document_id"),
        (result.cnig_profile, "cnig_profile"),
        (result.policy_profile, "policy_profile"),
    ):
        try:
            _exact_string(value, label)
        except ValueError as error:
            raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    if (
        type(result.application_result_hash_schema_version) is not int
        or result.application_result_hash_schema_version
        != APPLICATION_RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "application result schema must be exactly 2"
        )
    if any(
        value is not expected
        for value, expected in (
            (result.local_feature_text_interpreted, False),
            (result.local_regulation_content_interpreted, False),
            (result.legal_conclusion_produced, False),
            (result.parcel_status_aggregated, True),
            (result.parcel_rejection_performed, False),
            (result.score_calculated, False),
        )
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation flags are invalid"
        )
    if (
        not isinstance(result.parcels, gpd.GeoDataFrame)
        or not isinstance(result.relation_assessments, pd.DataFrame)
        or isinstance(result.relation_assessments, gpd.GeoDataFrame)
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "aggregation output frame types are invalid"
        )
    if result.parcels.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            "parcel output contains duplicate columns"
        )
    if result.relation_assessments.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            "relation assessments contain duplicate columns"
        )
    if (
        tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) != PARCEL_COLUMNS
        or tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])
        != RELATION_COLUMNS
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "aggregation output suffix schema is invalid"
        )
    for column in PARCEL_STRING_COLUMNS:
        if str(result.parcels[column].dtype) != "str":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation string dtype is invalid"
            )
    for column in PARCEL_INTEGER_COLUMNS:
        if str(result.parcels[column].dtype) != "Int64":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation integer dtype is invalid"
            )
    for column in PARCEL_BOOL_COLUMNS:
        if str(result.parcels[column].dtype) != "bool":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation bool dtype is invalid"
            )
    for column in RELATION_STRING_COLUMNS:
        if str(result.relation_assessments[column].dtype) != "str":
            raise BessPlanningFeatureParcelAggregationError(
                "relation assessment string dtype is invalid"
            )
    if (
        str(result.relation_assessments["bess_cnig_selected_for_parcel_status"].dtype)
        != "bool"
        or str(
            result.relation_assessments[
                "bess_cnig_resulting_parcel_status_priority"
            ].dtype
        )
        != "Int64"
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "relation assessment dtype is invalid"
        )
    _validate_parcel_frame(result.parcels, "parcel output")
    _validate_local_domains(result.parcels, result.relation_assessments)
    source_parcels = result.parcels.drop(columns=list(PARCEL_COLUMNS))
    source_parcels = gpd.GeoDataFrame(
        source_parcels, geometry=result.parcels.geometry.name, crs=result.parcels.crs
    )
    source_relations = result.relation_assessments.drop(columns=list(RELATION_COLUMNS))
    if result.source_parcels_content_sha256 != _frame_sha256(
        source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "source parcel content SHA256 is invalid"
        )
    if result.source_application_relations_content_sha256 != _frame_sha256(
        source_relations,
        "landscout.bess_cnig_parcel_aggregation.source_application_relations",
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "source application relation content SHA256 is invalid"
        )
    lineage = _ApplicationLineage(
        source_document_id=result.source_document_id,
        source_archive_sha256=result.source_archive_sha256,
        cnig_profile=result.cnig_profile,
        cnig_profile_sha256=result.cnig_profile_sha256,
        policy_profile=result.policy_profile,
        policy_sha256=result.policy_sha256,
        policy_complete_result_content_sha256=result.policy_complete_result_content_sha256,
        complete_result_content_sha256=result.application_complete_result_content_sha256,
    )
    _validate_application_relations(source_relations, lineage)
    expected_parcels, expected_relations = _aggregate_frames(
        source_parcels, source_relations, lineage
    )
    _compare_frame(result.parcels, expected_parcels, "parcel output")
    _compare_frame(
        result.relation_assessments, expected_relations, "relation assessments"
    )
    rebuilt = _result_with_hashes(result)
    for field in (
        "relation_assessments_content_sha256",
        "parcels_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt, field):
            raise BessPlanningFeatureParcelAggregationError(f"{field} is invalid")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_source_locks`

**Exact signature**

```python
def _validate_source_locks(
    result: BessPlanningFeatureParcelAggregationResult
    | BessPlanningFeatureParcelAggregationArtifactManifest,
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent source locks; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((actual != expected for actual, expected in comparisons))`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('parcel aggregation source lock differs')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_frame_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_source_locks`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_source_locks`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_validate_source_locks`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_validate_source_locks`.

**Complete source-ordered implementation**

```python
def _validate_source_locks(
    result: BessPlanningFeatureParcelAggregationResult
    | BessPlanningFeatureParcelAggregationArtifactManifest,
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> None:
    comparisons = (
        (result.source_document_id, application.source_document_id),
        (result.source_archive_sha256, application.source_archive_sha256),
        (result.cnig_profile, application.cnig_profile),
        (result.cnig_profile_sha256, application.cnig_profile_sha256),
        (
            result.cnig_complete_result_content_sha256,
            application.cnig_complete_result_content_sha256,
        ),
        (result.policy_profile, application.policy_profile),
        (result.policy_sha256, application.policy_sha256),
        (
            result.policy_complete_result_content_sha256,
            application.policy_complete_result_content_sha256,
        ),
        (
            result.application_result_hash_schema_version,
            application.result_hash_schema_version,
        ),
        (
            result.application_complete_result_content_sha256,
            application.complete_result_content_sha256,
        ),
        (
            result.source_application_relations_content_sha256,
            _frame_sha256(
                application.relations,
                "landscout.bess_cnig_parcel_aggregation.source_application_relations",
            ),
        ),
        (
            result.source_parcels_content_sha256,
            _frame_sha256(
                source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
            ),
        ),
    )
    if any(actual != expected for actual, expected in comparisons):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation source lock differs"
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_application_source`

**Exact signature**

```python
def _validate_application_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent application source; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Source-complete application validation failed')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `_validate_application_source`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_application_source`.

**Complete source-ordered implementation**

```python
def _validate_application_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
) -> None:
    try:
        validate_bess_planning_feature_application_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
            application_result,
        )
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Source-complete application validation failed"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `aggregate_bess_planning_feature_policy_to_parcels`

**Exact signature**

```python
def aggregate_bess_planning_feature_policy_to_parcels(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Validate the application once and aggregate its relations to every parcel.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Parcel aggregation failed safely')`, `re-raise`.

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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_aggregation_fixture` via `aggregate_bess_planning_feature_policy_to_parcels`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` via `aggregate_bess_planning_feature_policy_to_parcels`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `module.aggregate_bess_planning_feature_policy_to_parcels`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `module.aggregate_bess_planning_feature_policy_to_parcels`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.

**Complete source-ordered implementation**

```python
def aggregate_bess_planning_feature_policy_to_parcels(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    """Validate the application once and aggregate its relations to every parcel."""
    try:
        _validate_application_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
            application_result,
        )
        result = _build_result(parcels, application_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Parcel aggregation failed safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_parcel_aggregation_result`

**Exact signature**

```python
def validate_bess_planning_feature_parcel_aggregation_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
```

**Purpose**

Independently validate and rebuild one persisted parcel aggregation result.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Parcel aggregation result validation failed safely')`, `BessPlanningFeatureParcelAggregationError(f'Aggregation {field} differs')`, `re-raise`.

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

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `module.validate_bess_planning_feature_parcel_aggregation_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `module.validate_bess_planning_feature_parcel_aggregation_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `validate_bess_planning_feature_parcel_aggregation_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `validate_bess_planning_feature_parcel_aggregation_result`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.

**Complete source-ordered implementation**

```python
def validate_bess_planning_feature_parcel_aggregation_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    application_result: BessPlanningFeatureApplicationResult,
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
    """Independently validate and rebuild one persisted parcel aggregation result."""
    try:
        _validate_result_envelope(result)
        _validate_source_locks(result, parcels, application_result)
        _validate_application_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
            application_result,
        )
        expected = _build_result(parcels, application_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureParcelAggregationError(
                    f"Aggregation {field} differs"
                )
        _compare_frame(result.parcels, expected.parcels, "parcels")
        _compare_frame(
            result.relation_assessments, expected.relation_assessments, "relations"
        )
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Parcel aggregation result validation failed safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_unique_json_object`

**Exact signature**

```python
def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for unique json object; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- Guard with a raise path: `key in output`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError(f'Duplicate JSON aggregation artifact key: {key!r}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output[key]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`.
- callback/function object: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`.
- callback/function object: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `json.loads(manifest_file.read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`.
- callback/property argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=module._unique_json_object)`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._unique_json_object`.

**Complete source-ordered implementation**

```python
def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise BessPlanningFeatureParcelAggregationError(
                f"Duplicate JSON aggregation artifact key: {key!r}"
            )
        output[key] = value
    return output
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_read_verified_artifact`

**Exact signature**

```python
def _read_verified_artifact(
    path: Path, record: BessPlanningFeatureParcelAggregationArtifactRecord
) -> pd.DataFrame:
```

**Purpose**

Reads verified artifact; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `path.name != record.filename`.
- Guard with a raise path: `len(payload) != record.size_bytes`.
- Guard with a raise path: `sha256(payload).hexdigest() != record.sha256`.
- Guard with a raise path: `len(frame) != record.row_count`.
- Guard with a raise path: `deterministic_frame_schema_signature(frame) != record.frame_schema_signature`.
- Guard with a raise path: `record.geospatial`.
- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None or CRS.from_user_input(frame.crs).to_json_dict() != record.crs`.
- Guard with a raise path: `isinstance(frame, gpd.GeoDataFrame)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Aggregation artifact SHA256 differs')`, `BessPlanningFeatureParcelAggregationError('Aggregation artifact byte size differs')`, `BessPlanningFeatureParcelAggregationError('Aggregation artifact filename differs')`, `BessPlanningFeatureParcelAggregationError('Aggregation artifact frame schema differs')`, `BessPlanningFeatureParcelAggregationError('Aggregation artifact row count differs')`, `BessPlanningFeatureParcelAggregationError('Aggregation parcel artifact CRS differs')`, `BessPlanningFeatureParcelAggregationError('Relation assessment artifact is unexpectedly geospatial')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `gpd.read_parquet`, `path.read_bytes`, `pd.read_parquet`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_read_verified_artifact`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_read_verified_artifact`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._read_verified_artifact`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._read_verified_artifact`.

**Complete source-ordered implementation**

```python
def _read_verified_artifact(
    path: Path, record: BessPlanningFeatureParcelAggregationArtifactRecord
) -> pd.DataFrame:
    if path.name != record.filename:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact filename differs"
        )
    payload = path.read_bytes()
    if len(payload) != record.size_bytes:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact byte size differs"
        )
    if sha256(payload).hexdigest() != record.sha256:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact SHA256 differs"
        )
    buffer = BytesIO(payload)
    frame: pd.DataFrame = (
        gpd.read_parquet(buffer) if record.geospatial else pd.read_parquet(buffer)
    )
    if len(frame) != record.row_count:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact row count differs"
        )
    if deterministic_frame_schema_signature(frame) != record.frame_schema_signature:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact frame schema differs"
        )
    if record.geospatial:
        if (
            not isinstance(frame, gpd.GeoDataFrame)
            or frame.crs is None
            or CRS.from_user_input(frame.crs).to_json_dict() != record.crs
        ):
            raise BessPlanningFeatureParcelAggregationError(
                "Aggregation parcel artifact CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation assessment artifact is unexpectedly geospatial"
        )
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_parcel_aggregation_artifacts`

**Exact signature**

```python
def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Load byte-sealed outputs and bind them to exact lightweight upstreams.

**Return contract**

- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(loaded_parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Explicit raise expressions: `BessPlanningFeatureParcelAggregationError('Parcel artifact is not geospatial')`, `BessPlanningFeatureParcelAggregationError(f'Aggregation artifact scalar {field} differs from upstream rebuild')`, `BessPlanningFeatureParcelAggregationError(f'Parcel aggregation artifacts are invalid: {error}')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `Path(manifest_path).read_text`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- callback/property argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams` via `inspect.signature(module.load_bess_planning_feature_parcel_aggregation_artifacts)`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams` via `module.load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module.load_bess_planning_feature_parcel_aggregation_artifacts`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module.load_bess_planning_feature_parcel_aggregation_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `module.load_bess_planning_feature_parcel_aggregation_artifacts`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `module.load_bess_planning_feature_parcel_aggregation_artifacts`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    load_bess_planning_feature_parcel_aggregation_artifacts as _load_aggregation_artifacts,
)`.

**Complete source-ordered implementation**

```python
def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    """Load byte-sealed outputs and bind them to exact lightweight upstreams."""
    try:
        validate_bess_planning_feature_application_result_envelope(application_result)
        _validate_parcel_frame(source_parcels, "source parcels")
        payload = json.loads(
            Path(manifest_path).read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
        )
        manifest = BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(
            payload
        )
        _validate_source_locks(manifest, source_parcels, application_result)
        records = {record.artifact_role: record for record in manifest.artifacts}
        loaded_parcels = _read_verified_artifact(Path(parcels_path), records["PARCELS"])
        loaded_relations = _read_verified_artifact(
            Path(relation_assessments_path), records["RELATION_ASSESSMENTS"]
        )
        if not isinstance(loaded_parcels, gpd.GeoDataFrame):
            raise BessPlanningFeatureParcelAggregationError(
                "Parcel artifact is not geospatial"
            )
        result = BessPlanningFeatureParcelAggregationResult(
            **{field: getattr(manifest, field) for field in RESULT_SCALAR_FIELDS},
            parcels=loaded_parcels,
            relation_assessments=loaded_relations,
        )
        _validate_result_envelope(result)
        expected = _build_result(source_parcels, application_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureParcelAggregationError(
                    f"Aggregation artifact scalar {field} differs from upstream rebuild"
                )
        for field in RESULT_FRAME_FIELDS:
            _compare_frame(
                getattr(result, field),
                getattr(expected, field),
                f"artifact {field}",
            )
        return result
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"Parcel aggregation artifacts are invalid: {error}"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `bess_cnig_parcel_aggregation_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 2 | `bess_cnig_parcel_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `bess_cnig_parcel_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `bess_cnig_parcel_status_priority` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `bess_cnig_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 6 | `bess_cnig_exact_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 7 | `bess_cnig_unresolved_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 8 | `bess_cnig_touch_only_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 9 | `bess_cnig_selected_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 10 | `bess_cnig_lower_priority_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 11 | `bess_cnig_distinct_exact_status_count` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 12 | `bess_cnig_multiple_exact_statuses` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 13 | `bess_cnig_selected_feature_ids_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `bess_cnig_unresolved_feature_ids_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `bess_cnig_touch_only_feature_ids_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 16 | `bess_cnig_confidence_aggregation_method` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `bess_cnig_formal_review_required` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `bess_cnig_aggregation_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 19 | `bess_cnig_policy_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 20 | `bess_cnig_local_feature_text_interpreted` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 21 | `bess_cnig_local_regulation_content_interpreted` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 22 | `bess_cnig_legal_conclusion_produced` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 23 | `bess_cnig_parcel_status_aggregated` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 24 | `bess_cnig_parcel_rejection_performed` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 25 | `bess_cnig_score_calculated` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 26 | `bess_cnig_policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 27 | `bess_cnig_policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 28 | `bess_cnig_policy_result_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 29 | `bess_cnig_application_result_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `bess_cnig_parcel_relation_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `bess_cnig_selected_for_parcel_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `bess_cnig_resulting_parcel_aggregation_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `bess_cnig_resulting_parcel_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `bess_cnig_resulting_parcel_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `bess_cnig_resulting_parcel_status_priority` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |

### `PARCEL_STRING_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_STRING_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `bess_cnig_parcel_aggregation_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 2 | `bess_cnig_parcel_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `bess_cnig_parcel_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `bess_cnig_selected_feature_ids_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `bess_cnig_unresolved_feature_ids_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `bess_cnig_touch_only_feature_ids_json` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `bess_cnig_confidence_aggregation_method` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `bess_cnig_aggregation_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `bess_cnig_policy_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `bess_cnig_policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `bess_cnig_policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 12 | `bess_cnig_policy_result_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `bess_cnig_application_result_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `PARCEL_INTEGER_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_INTEGER_COLUMNS = (
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `bess_cnig_parcel_status_priority` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 2 | `bess_cnig_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 3 | `bess_cnig_exact_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 4 | `bess_cnig_unresolved_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 5 | `bess_cnig_touch_only_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 6 | `bess_cnig_selected_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 7 | `bess_cnig_lower_priority_controlling_relation_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 8 | `bess_cnig_distinct_exact_status_count` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |

### `PARCEL_BOOL_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_BOOL_COLUMNS = (
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_formal_review_required",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `bess_cnig_multiple_exact_statuses` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 2 | `bess_cnig_formal_review_required` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `bess_cnig_local_feature_text_interpreted` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `bess_cnig_local_regulation_content_interpreted` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `bess_cnig_legal_conclusion_produced` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `bess_cnig_parcel_status_aggregated` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 7 | `bess_cnig_parcel_rejection_performed` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `bess_cnig_score_calculated` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `RELATION_STRING_COLUMNS` — canonical or derived frame-column schema

```python
RELATION_STRING_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `bess_cnig_parcel_relation_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `bess_cnig_resulting_parcel_aggregation_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `bess_cnig_resulting_parcel_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `bess_cnig_resulting_parcel_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `BessPlanningFeatureParcelAggregationArtifactManifest` | re-exported/defined Python symbol | `defined in `src/landscout/stages/aggregate_bess_planning_feature_policy.py`` | yes |
| `BessPlanningFeatureParcelAggregationError` | re-exported/defined Python symbol | `defined in `src/landscout/stages/aggregate_bess_planning_feature_policy.py`` | yes |
| `BessPlanningFeatureParcelAggregationResult` | re-exported/defined Python symbol | `defined in `src/landscout/stages/aggregate_bess_planning_feature_policy.py`` | yes |
| `aggregate_bess_planning_feature_policy_to_parcels` | re-exported/defined Python symbol | `defined in `src/landscout/stages/aggregate_bess_planning_feature_policy.py`` | yes |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | re-exported/defined Python symbol | `defined in `src/landscout/stages/aggregate_bess_planning_feature_policy.py`` | yes |
| `validate_bess_planning_feature_parcel_aggregation_result` | re-exported/defined Python symbol | `defined in `src/landscout/stages/aggregate_bess_planning_feature_policy.py`` | yes |

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
