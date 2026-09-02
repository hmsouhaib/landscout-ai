# `src/landscout/stages/aggregate_bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/aggregate_bess_planning_feature_policy.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.
- Source SHA256: `27bc7dcc9c67fead2c6f0638b033aab6e98282cfd2d865aec37dbf11b681c598`

## 1. STEP 7F.1A.4.2 contract delta

- Validates aggregation artifact schema/CRS evidence through the strict canonical-JSON freezer before retaining or comparing it.
- Unsupported leaves are rejected rather than retained or stringified; existing valid JSON shapes, schemas, hashes, and business boundaries remain unchanged.

## 2. Purpose and architectural position

Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `import re`
- `from collections.abc import Mapping`
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
    field_serializer,
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
- `from landscout.common.immutable_mapping import (
    freeze_json_mapping,
    to_plain_json_value,
)`
- `from landscout.common.planning_overlay import technical_overlay_tolerance`
- `from landscout.common.strict_json import loads_strict_json, loads_strict_json_object`
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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `BessPlanningFeatureParcelAggregationArtifactManifest`
  - `BessPlanningFeatureParcelAggregationError`
  - `BessPlanningFeatureParcelAggregationResult`
  - `aggregate_bess_planning_feature_policy_to_parcels`
  - `load_bess_planning_feature_parcel_aggregation_artifacts`
  - `validate_bess_planning_feature_parcel_aggregation_result`

### `RESULT_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RESULT_HASH_SCHEMA_VERSION = 1
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARTIFACT_MANIFEST_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 1
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `APPLICATION_RESULT_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
APPLICATION_RESULT_HASH_SCHEMA_VERSION = 2
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `AGGREGATION_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
AGGREGATION_SCOPE = "PARCEL_POLICY_AGGREGATION_ONLY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CONFIDENCE_METHOD`

- Category: module constant or closed domain.
- Exact declaration:

```python
CONFIDENCE_METHOD = "LOWEST_CONFIDENCE_FOR_SELECTED_STATUS"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARTIFACT_KIND`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CONTROLLING_RELATION_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
CONTROLLING_RELATION_TYPES = frozenset({"AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CONTEXT_RELATION_TYPES`

- Category: module constant or closed domain.
- Exact declaration:

```python
CONTEXT_RELATION_TYPES = frozenset({"TOUCH_ONLY", "BOUNDARY_TOUCH"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `AGGREGATION_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `RELATION_ROLES`

- Category: module constant or closed domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CONFIDENCE_RANK`

- Category: module constant or closed domain.
- Exact declaration:

```python
CONFIDENCE_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `LOW`
  - `MEDIUM`
  - `HIGH`

### `SHA_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

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

### `PARCEL_STRING_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_parcel_aggregation_status`
  - `bess_cnig_parcel_precheck_status`
  - `bess_cnig_parcel_precheck_confidence`
  - `bess_cnig_selected_feature_ids_json`
  - `bess_cnig_unresolved_feature_ids_json`
  - `bess_cnig_touch_only_feature_ids_json`
  - `bess_cnig_confidence_aggregation_method`
  - `bess_cnig_aggregation_scope`
  - `bess_cnig_policy_scope`
  - `bess_cnig_policy_profile`
  - `bess_cnig_policy_sha256`
  - `bess_cnig_policy_result_sha256`
  - `bess_cnig_application_result_sha256`

### `PARCEL_INTEGER_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_parcel_status_priority`
  - `bess_cnig_controlling_relation_count`
  - `bess_cnig_exact_controlling_relation_count`
  - `bess_cnig_unresolved_controlling_relation_count`
  - `bess_cnig_touch_only_relation_count`
  - `bess_cnig_selected_relation_count`
  - `bess_cnig_lower_priority_controlling_relation_count`
  - `bess_cnig_distinct_exact_status_count`

### `PARCEL_BOOL_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_multiple_exact_statuses`
  - `bess_cnig_formal_review_required`
  - `bess_cnig_local_feature_text_interpreted`
  - `bess_cnig_local_regulation_content_interpreted`
  - `bess_cnig_legal_conclusion_produced`
  - `bess_cnig_parcel_status_aggregated`
  - `bess_cnig_parcel_rejection_performed`
  - `bess_cnig_score_calculated`

### `RELATION_STRING_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RELATION_STRING_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `bess_cnig_parcel_relation_role`
  - `bess_cnig_resulting_parcel_aggregation_status`
  - `bess_cnig_resulting_parcel_precheck_status`
  - `bess_cnig_resulting_parcel_precheck_confidence`

### `ArtifactRole`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ArtifactRole = Literal["PARCELS", "RELATION_ASSESSMENTS"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARTIFACT_ROLES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = ("PARCELS", "RELATION_ASSESSMENTS")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `PARCELS`
  - `RELATION_ASSESSMENTS`

### `RESULT_FRAME_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RESULT_FRAME_FIELDS = ("relation_assessments", "parcels")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `relation_assessments`
  - `parcels`

### `RESULT_SCALAR_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureParcelAggregationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `BessPlanningFeatureParcelAggregationError`

**Source purpose:** Raised when parcel aggregation integrity cannot be proven.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_value` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_value` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_sha256` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_sha256` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_feature_id` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_feature_id` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_json_ids` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_json_ids` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_parcel_frame` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_parcel_frame` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_relations` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_relations` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_relation_parcel_areas` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_relation_parcel_areas` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_local_domains` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_local_domains` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_relation_priority` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_relation_priority` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_compare_frame` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_compare_frame` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_read_verified_artifact` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_read_verified_artifact` via `BessPlanningFeatureParcelAggregationError`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationError`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_local_corruption_fast_fails_before_heavy_validation` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_local_cross_table_corruption_is_rejected` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_every_inherited_application_relation_domain_is_validated_locally` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unresolved_relation_cannot_contain_a_decision` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_all_application_identity_scope_and_boundary_fields_are_intrinsic` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_application_relation_suffix_dtype_is_validated_locally` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_status_and_priority_mapping_is_one_to_one_at_every_level` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_parcel_feature_identity_is_rejected_for_every_role` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_deferred_feature_id_is_rejected_independently_of_json_role` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_invalid_relation_parcel_id_is_rejected` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_unknown_relation_type_is_rejected_by_shared_relation_contract` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_priority_cannot_map_to_two_statuses` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_document_wide_same_status_cannot_map_to_two_priorities` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_selected_relation_role_requires_selected_status_and_priority` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_malformed_parcel_geometry_is_rejected_intrinsically` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_duplicate_output_columns_are_rejected_intrinsically` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_only_application_result_schema_two_is_accepted` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_noncanonical_feature_ids_are_rejected` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_authorized_status_artifact_fails_local_verified_byte_loading` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_no_relation_parcel_rejects_textual_null_identity` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_persisted_feature_id_json_must_be_portable_and_canonical` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_artifact_manifest_corruption_is_rejected` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_uses_strict_json_before_artifact_read` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_physical_replacement_is_rejected` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `BessPlanningFeatureParcelAggregationError`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `BessPlanningFeatureParcelAggregationError`

**Exact class source**

```python
class BessPlanningFeatureParcelAggregationError(ValueError):
    """Raised when parcel aggregation integrity cannot be proven."""
```

### `_ApplicationLineage`

**Source purpose:** Defines `_ApplicationLineage`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `source_document_id` | `str` | `required` | `source_document_id: str` |
| `source_archive_sha256` | `str` | `required` | `source_archive_sha256: str` |
| `cnig_profile` | `str` | `required` | `cnig_profile: str` |
| `cnig_profile_sha256` | `str` | `required` | `cnig_profile_sha256: str` |
| `policy_profile` | `str` | `required` | `policy_profile: str` |
| `policy_sha256` | `str` | `required` | `policy_sha256: str` |
| `policy_complete_result_content_sha256` | `str` | `required` | `policy_complete_result_content_sha256: str` |
| `complete_result_content_sha256` | `str` | `required` | `complete_result_content_sha256: str` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_relations` via `_ApplicationLineage`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `_ApplicationLineage`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_ApplicationLineage`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_ApplicationLineage`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_ApplicationLineage`

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

**Source purpose:** Defines `_StrictModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `BessPlanningFeatureParcelAggregationArtifactRecord`

**Source purpose:** Defines `BessPlanningFeatureParcelAggregationArtifactRecord`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `artifact_role` | `ArtifactRole` | `required` | `artifact_role: ArtifactRole` |
| `filename` | `StrictStr` | `required` | `filename: StrictStr` |
| `row_count` | `StrictInt` | `required` | `row_count: StrictInt` |
| `size_bytes` | `StrictInt` | `required` | `size_bytes: StrictInt` |
| `sha256` | `StrictStr` | `required` | `sha256: StrictStr` |
| `frame_schema_signature` | `dict[StrictStr, object]` | `required` | `frame_schema_signature: dict[StrictStr, object]` |
| `geospatial` | `StrictBool` | `required` | `geospatial: StrictBool` |
| `crs` | `dict[StrictStr, object] \| None` | `required` | `crs: dict[StrictStr, object] \| None` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::BessPlanningFeatureParcelAggregationArtifactRecord._validate_record` via `BessPlanningFeatureParcelAggregationArtifactRecord`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_read_verified_artifact` via `BessPlanningFeatureParcelAggregationArtifactRecord`

**Exact class source**

```python
class BessPlanningFeatureParcelAggregationArtifactRecord(_StrictModel):
    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: Mapping[StrictStr, object]
    geospatial: StrictBool
    crs: Mapping[StrictStr, object] | None

    @field_serializer("frame_schema_signature", "crs")
    def _serialize_immutable_json_mapping(
        self, value: Mapping[str, object] | None
    ) -> object:
        return to_plain_json_value(value)

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
        frozen_signature = freeze_json_mapping(self.frame_schema_signature)
        frozen_crs = freeze_json_mapping(self.crs) if self.crs is not None else None
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be non-negative")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be positive")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geo = self.artifact_role == "PARCELS"
        if self.geospatial is not expected_geo:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = frozen_signature.get("crs")
        if expected_geo:
            if frozen_crs is None or signature_crs != frozen_crs:
                raise ValueError("parcel artifact CRS is missing or inconsistent")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("relation artifact must not declare CRS")
        object.__setattr__(
            self,
            "frame_schema_signature",
            frozen_signature,
        )
        if frozen_crs is not None:
            object.__setattr__(self, "crs", frozen_crs)
        return self
```

### `BessPlanningFeatureParcelAggregationResult`

**Source purpose:** Defines `BessPlanningFeatureParcelAggregationResult`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | `result_hash_schema_version: int` |
| `aggregation_scope` | `str` | `required` | `aggregation_scope: str` |
| `policy_scope` | `str` | `required` | `policy_scope: str` |
| `local_feature_text_interpreted` | `bool` | `required` | `local_feature_text_interpreted: bool` |
| `local_regulation_content_interpreted` | `bool` | `required` | `local_regulation_content_interpreted: bool` |
| `legal_conclusion_produced` | `bool` | `required` | `legal_conclusion_produced: bool` |
| `parcel_status_aggregated` | `bool` | `required` | `parcel_status_aggregated: bool` |
| `parcel_rejection_performed` | `bool` | `required` | `parcel_rejection_performed: bool` |
| `score_calculated` | `bool` | `required` | `score_calculated: bool` |
| `source_document_id` | `str` | `required` | `source_document_id: str` |
| `source_archive_sha256` | `str` | `required` | `source_archive_sha256: str` |
| `cnig_profile` | `str` | `required` | `cnig_profile: str` |
| `cnig_profile_sha256` | `str` | `required` | `cnig_profile_sha256: str` |
| `cnig_complete_result_content_sha256` | `str` | `required` | `cnig_complete_result_content_sha256: str` |
| `policy_profile` | `str` | `required` | `policy_profile: str` |
| `policy_sha256` | `str` | `required` | `policy_sha256: str` |
| `policy_complete_result_content_sha256` | `str` | `required` | `policy_complete_result_content_sha256: str` |
| `application_result_hash_schema_version` | `int` | `required` | `application_result_hash_schema_version: int` |
| `application_complete_result_content_sha256` | `str` | `required` | `application_complete_result_content_sha256: str` |
| `source_parcels_content_sha256` | `str` | `required` | `source_parcels_content_sha256: str` |
| `source_application_relations_content_sha256` | `str` | `required` | `source_application_relations_content_sha256: str` |
| `relation_assessments_content_sha256` | `str` | `required` | `relation_assessments_content_sha256: str` |
| `parcels_content_sha256` | `str` | `required` | `parcels_content_sha256: str` |
| `complete_result_content_sha256` | `str` | `required` | `complete_result_content_sha256: str` |
| `relation_assessments` | `pd.DataFrame` | `required` | `relation_assessments: pd.DataFrame` |
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_component_metadata` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_result_with_hashes` via `BessPlanningFeatureParcelAggregationResult`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeatureParcelAggregationResult`
- constructor call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationResult`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_aggregation_fixture` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationResult`
- constructor call: `tests.unit.test_aggregate_bess_planning_feature_policy::_load_legacy_local_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_load_legacy_local_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_build_from_relations` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_write_artifacts` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_rehash_coordinated_result` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_duplicate_selected_pair_result` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_invalid_lower_feature_id_result` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_cross_parcel_priority_conflict_result` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_surface_touch_semantic_corruption_result` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_coherent_parcel_area_mutation` via `BessPlanningFeatureParcelAggregationResult`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_self_consistent_parcel_area_artifact_is_rejected` via `BessPlanningFeatureParcelAggregationResult`

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

**Source purpose:** Defines `BessPlanningFeatureParcelAggregationArtifactManifest`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `artifact_kind` | `Literal['BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT']` | `required` | `artifact_kind: Literal["BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"]` |
| `result_hash_schema_version` | `StrictInt` | `required` | `result_hash_schema_version: StrictInt` |
| `aggregation_scope` | `Literal['PARCEL_POLICY_AGGREGATION_ONLY']` | `required` | `aggregation_scope: Literal["PARCEL_POLICY_AGGREGATION_ONLY"]` |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` |
| `local_feature_text_interpreted` | `StrictBool` | `required` | `local_feature_text_interpreted: StrictBool` |
| `local_regulation_content_interpreted` | `StrictBool` | `required` | `local_regulation_content_interpreted: StrictBool` |
| `legal_conclusion_produced` | `StrictBool` | `required` | `legal_conclusion_produced: StrictBool` |
| `parcel_status_aggregated` | `StrictBool` | `required` | `parcel_status_aggregated: StrictBool` |
| `parcel_rejection_performed` | `StrictBool` | `required` | `parcel_rejection_performed: StrictBool` |
| `score_calculated` | `StrictBool` | `required` | `score_calculated: StrictBool` |
| `source_document_id` | `StrictStr` | `required` | `source_document_id: StrictStr` |
| `source_archive_sha256` | `StrictStr` | `required` | `source_archive_sha256: StrictStr` |
| `cnig_profile` | `StrictStr` | `required` | `cnig_profile: StrictStr` |
| `cnig_profile_sha256` | `StrictStr` | `required` | `cnig_profile_sha256: StrictStr` |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | `cnig_complete_result_content_sha256: StrictStr` |
| `policy_profile` | `StrictStr` | `required` | `policy_profile: StrictStr` |
| `policy_sha256` | `StrictStr` | `required` | `policy_sha256: StrictStr` |
| `policy_complete_result_content_sha256` | `StrictStr` | `required` | `policy_complete_result_content_sha256: StrictStr` |
| `application_result_hash_schema_version` | `StrictInt` | `required` | `application_result_hash_schema_version: StrictInt` |
| `application_complete_result_content_sha256` | `StrictStr` | `required` | `application_complete_result_content_sha256: StrictStr` |
| `source_parcels_content_sha256` | `StrictStr` | `required` | `source_parcels_content_sha256: StrictStr` |
| `source_application_relations_content_sha256` | `StrictStr` | `required` | `source_application_relations_content_sha256: StrictStr` |
| `relation_assessments_content_sha256` | `StrictStr` | `required` | `relation_assessments_content_sha256: StrictStr` |
| `parcels_content_sha256` | `StrictStr` | `required` | `parcels_content_sha256: StrictStr` |
| `complete_result_content_sha256` | `StrictStr` | `required` | `complete_result_content_sha256: StrictStr` |
| `artifacts` | `tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]` | `required` | `artifacts: tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest` via `BessPlanningFeatureParcelAggregationArtifactManifest`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureParcelAggregationArtifactManifest`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationArtifactManifest`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_load_legacy_local_aggregation_artifacts` via `BessPlanningFeatureParcelAggregationArtifactManifest`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_write_artifacts` via `BessPlanningFeatureParcelAggregationArtifactManifest`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_filenames_are_casefold_unique` via `BessPlanningFeatureParcelAggregationArtifactManifest`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_manifest_rejects_nonportable_filename` via `BessPlanningFeatureParcelAggregationArtifactManifest`

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


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_exact_string`

**Purpose:** Implements `exact string` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _exact_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError(f"{label} must be an exact non-empty string")` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_sha256_string` via `_exact_string`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_sha256_string` via `_exact_string`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_exact_string`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_exact_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_sha256_string`

**Purpose:** Implements `sha256 string` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _sha256_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `text`
- Explicit raise paths:
  - `ValueError(f"{label} must be a lowercase SHA256")` under lexical guard `SHA_PATTERN.fullmatch(text) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::BessPlanningFeatureParcelAggregationArtifactRecord._validate_record` via `_sha256_string`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::BessPlanningFeatureParcelAggregationArtifactRecord._validate_record` via `_sha256_string`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest` via `_sha256_string`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest` via `_sha256_string`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_sha256_string`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_sha256_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string` | `landscout.stages.aggregate_bess_planning_feature_policy._exact_string` |
| `SHA_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `BessPlanningFeatureParcelAggregationArtifactRecord._serialize_immutable_json_mapping`

**Purpose:** Pydantic field serializer for `frame_schema_signature` and `crs`.

- Exact signature: `def _serialize_immutable_json_mapping( self, value: Mapping[str, object] | None ) -> object:`
- Exact decorator: `@field_serializer("frame_schema_signature", "crs")`.
- Algorithm: pass the retained immutable mapping (or `None`) to `to_plain_json_value`, returning a fresh plain JSON-compatible dictionary/list/scalar structure without exposing mutable retained state.

### `BessPlanningFeatureParcelAggregationArtifactRecord._validate_record`

**Purpose:** Validate one parcel-aggregation artifact record and retain only strict canonical immutable schema/CRS evidence.

- Exact signature: `def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:`
- Exact decorator: `@model_validator(mode="after")`.
- Ordered algorithm:
  1. Validate and freeze `frame_schema_signature` through `freeze_json_mapping`.
  2. Validate and freeze `crs` through `freeze_json_mapping` when present.
  3. Validate the portable filename.
  4. Require a non-negative exact-integer row count.
  5. Require a positive exact-integer byte size.
  6. Validate the lowercase SHA256.
  7. Derive the expected geospatial flag from the `PARCELS` role.
  8. Compare the canonical signature CRS with the canonical record CRS for parcel artifacts.
  9. Reject CRS evidence for non-geospatial relation assessments.
  10. Retain only the frozen canonical signature and CRS mappings, then return `self`.
- Direct in-memory effect: `object.__setattr__` replaces the two validated Pydantic fields with their immutable canonical values; no caller-owned collection is retained.

### `BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest`

**Purpose:** Implements `validate manifest` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `BessPlanningFeatureParcelAggregationArtifactManifest`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("unsupported parcel aggregation artifact schema")` under lexical guard `type(self.schema_version) is not int<br>            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`.
  - `ValueError("unsupported parcel aggregation result schema")` under lexical guard `type(self.result_hash_schema_version) is not int<br>            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
  - `ValueError("parcel aggregation boundary flags are invalid")` under lexical guard `any(<br>            value is not expected<br>            for value, expected in (<br>                (self.local_feature_text_interpreted, False),<br>                (self.local_regulation_content_interpreted, False),<br>                (self.legal_conclusion_produced, False),<br>                (self.parcel_status_aggregated, True),<br>                (self.parcel_rejection_performed, False),<br>                (self.score_calculated, False),<br>            )<br>        )`.
  - `ValueError("application result schema must be exactly 2")` under lexical guard `type(self.application_result_hash_schema_version) is not int<br>            or self.application_result_hash_schema_version<br>            != APPLICATION_RESULT_HASH_SCHEMA_VERSION`.
  - `ValueError("parcel aggregation artifact roles differ")` under lexical guard `roles != ARTIFACT_ROLES`.
  - `ValueError("parcel aggregation artifact filename is duplicated")` under lexical guard `len(filenames) != len(set(filenames))`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `field.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_string` | `landscout.stages.aggregate_bess_planning_feature_policy._sha256_string` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `record.filename.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_string` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_value`

**Purpose:** Implements `null value` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _null_value(value: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `value`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_value` via `_null_value`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_value` via `_null_value`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_local_domains` via `_null_value`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_local_domains` via `_null_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.isna` | `pandas.isna` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_value`

**Purpose:** Implements `canonical value` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _canonical_value(value: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `{<br>            "coordinate_dimension": dimension,<br>            "wkb_hex": to_wkb(<br>                value, hex=True, output_dimension=2, byte_order=1, include_srid=False<br>            ),<br>        }`
  - `value.isoformat()`
  - `_canonical_value(value.item())`
  - `value`
  - `int(value)`
  - `number`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>                "Parcel aggregation geometry must be canonical 2D"<br>            )` under lexical guard `isinstance(value, BaseGeometry)`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "Aggregation payload contains non-finite data"<br>            )` under lexical guard `isinstance(value, Real)`.
  - `BessPlanningFeatureParcelAggregationError(<br>        f"Unsupported aggregation integrity value {type(value).__name__}"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_value` via `_canonical_value`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_canonical_value` via `_canonical_value`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_frame_payload` via `_canonical_value`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_frame_payload` via `_canonical_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_null_value` | `landscout.stages.aggregate_bess_planning_feature_policy._null_value` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `get_coordinate_dimension` | `shapely.get_coordinate_dimension` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `to_wkb` | `shapely.to_wkb` |
| `value.isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.aggregate_bess_planning_feature_policy._canonical_value` |
| `value.item` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isfinite` | `math.isfinite` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_payload`

**Purpose:** Implements `frame payload` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "schema": deterministic_frame_schema_signature(frame),<br>        "index": [_canonical_value(value) for value in frame.index.tolist()],<br>        "rows": [<br>            [_canonical_value(value) for value in row]<br>            for row in frame.itertuples(index=False, name=None)<br>        ],<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_frame_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_frame_sha256` via `_frame_payload`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_result_with_hashes` via `_frame_payload`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_result_with_hashes` via `_frame_payload`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_compare_frame` via `_frame_payload`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_compare_frame` via `_frame_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `_canonical_value` | `landscout.stages.aggregate_bess_planning_feature_policy._canonical_value` |
| `frame.index.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.itertuples` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_sha256`

**Purpose:** Implements `canonical sha256` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _canonical_sha256(value: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(payload).hexdigest()`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "Aggregation payload is not canonical JSON"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_frame_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_frame_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_result_with_hashes` via `_canonical_sha256`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_result_with_hashes` via `_canonical_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_sha256`

**Purpose:** Implements `frame sha256` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `domain` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": domain,<br>            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,<br>            "frame": _frame_payload(frame),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `_frame_sha256`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `_frame_sha256`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_frame_sha256`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_frame_sha256`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_source_locks` via `_frame_sha256`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_source_locks` via `_frame_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.aggregate_bess_planning_feature_policy._canonical_sha256` |
| `_frame_payload` | `landscout.stages.aggregate_bess_planning_feature_policy._frame_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_feature_id`

**Purpose:** Implements `validate feature id` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_feature_id(value: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "Feature ID is not an exact portable string"<br>        )` under lexical guard `not isinstance(value, str)<br>        or not value<br>        or value != value.strip()<br>        or value in NULL_LITERALS<br>        or PurePosixPath(value).is_absolute()<br>        or PureWindowsPath(value).is_absolute()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_json_ids` via `_validate_feature_id`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_json_ids` via `_validate_feature_id`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_json_ids` via `_validate_feature_id`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_json_ids` via `_validate_feature_id`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath(value).is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `PurePosixPath` | `pathlib.PurePosixPath` |
| `PureWindowsPath(value).is_absolute` | `unresolved local/third-party receiver; no ownership inferred` |
| `PureWindowsPath` | `pathlib.PureWindowsPath` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_json_ids`

**Purpose:** Implements `json ids` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _json_ids(values: list[object]) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `values` | positional-or-keyword | `list[object]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(",", ":"))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `_json_ids`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `_json_ids`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_feature_id` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_feature_id` |
| `json.dumps` | `json.dumps` |

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
def _json_ids(values: list[object]) -> str:
    ids = sorted({_validate_feature_id(value) for value in values})
    return json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_json_ids`

**Purpose:** Implements `validate json ids` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_json_ids(value: object, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            f"{label} must be canonical JSON"<br>        )` under lexical guard `not isinstance(value, str)`.
  - `BessPlanningFeatureParcelAggregationError(<br>            f"{label} must be canonical JSON"<br>        )`.
  - `BessPlanningFeatureParcelAggregationError(f"{label} must be a JSON array")` under lexical guard `not isinstance(parsed, list)`.
  - `BessPlanningFeatureParcelAggregationError(f"{label} is not canonical")` under lexical guard `len(ids) != len(set(ids)) or ids != sorted(ids) or value != canonical`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_local_domains` via `_validate_json_ids`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_local_domains` via `_validate_json_ids`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `loads_strict_json` | `landscout.common.strict_json.loads_strict_json` |
| `_validate_feature_id` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_feature_id` |
| `json.dumps` | `json.dumps` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _validate_json_ids(value: object, label: str) -> None:
    if not isinstance(value, str):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        )
    try:
        parsed = loads_strict_json(value)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_parcel_frame`

**Purpose:** Implements `validate parcel frame` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            f"{label} must be a GeoDataFrame"<br>        )` under lexical guard `not isinstance(frame, gpd.GeoDataFrame)`.
  - `BessPlanningFeatureParcelAggregationError(<br>            f"{label} contains duplicate columns"<br>        )` under lexical guard `frame.columns.duplicated().any()`.
  - `BessPlanningFeatureParcelAggregationError(f"{label} lacks parcel_id")` under lexical guard `"parcel_id" not in frame.columns`.
  - `ValueError("active geometry column is absent")` under lexical guard `geometry_name not in frame.columns`.
  - `ValueError("CRS is absent")` under lexical guard `frame.crs is None`.
  - `BessPlanningFeatureParcelAggregationError(<br>            f"{label} geometry or CRS contract is invalid"<br>        )`.
  - `BessPlanningFeatureParcelAggregationError(<br>            f"{label} parcel IDs must be unique exact strings"<br>        )` under lexical guard `parcel_ids.isna().any()<br>        or parcel_ids.duplicated().any()<br>        or any(<br>            not isinstance(value, str)<br>            or not value<br>            or value != value.strip()<br>            or value in NULL_LITERALS<br>            for value in parcel_ids<br>        )`.
  - `BessPlanningFeatureParcelAggregationError(<br>                f"{label} requires valid canonical 2D polygon geometry"<br>            )` under lexical guard `geometry is None<br>            or geometry.is_empty<br>            or not geometry.is_valid<br>            or geometry.geom_type not in {"Polygon", "MultiPolygon"}<br>            or int(get_coordinate_dimension(geometry)) != 2`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_validate_parcel_frame`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_validate_parcel_frame`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_validate_parcel_frame`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_validate_parcel_frame`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_parcel_frame`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_parcel_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `parcel_ids.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_ids.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_ids.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_ids.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `get_coordinate_dimension` | `shapely.get_coordinate_dimension` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_application_relations`

**Purpose:** Implements `validate application relations` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_application_relations(
    frame: object,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `object` | `required` |
| `application` | positional-or-keyword | `BessPlanningFeatureApplicationResult \| _ApplicationLineage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "Application relations must be a DataFrame"<br>        )` under lexical guard `not isinstance(frame, pd.DataFrame) or isinstance(frame, gpd.GeoDataFrame)`.
  - `BessPlanningFeatureParcelAggregationError(str(error))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_validate_application_relations`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_validate_application_relations`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_validate_application_relations`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_validate_application_relations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `validate_bess_application_relation_frame` | `landscout.common.bess_application_contract.validate_bess_application_relation_frame` |
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_relation_parcel_areas`

**Purpose:** Implements `validate relation parcel areas` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_relation_parcel_areas(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "parcel metric-area calculation failed"<br>        )`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "parcel metric areas must be finite and positive"<br>        )` under lexical guard `not np.isfinite(areas).all() or (areas <= 0).any()`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "relation references an unknown parcel for metric area"<br>            )` under lexical guard `measured is None`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "relation parcel metric area must be numeric"<br>            )` under lexical guard `isinstance(stored, bool) or not isinstance(stored, Real)`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "relation parcel metric area must be finite"<br>            )` under lexical guard `not math.isfinite(actual)`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "relation parcel metric area differs from parcel geometry"<br>            )` under lexical guard `abs(actual - measured) > tolerance`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "parcel active geometry changed during metric validation"<br>        )` under lexical guard `parcels.geometry.name != geometry_name`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_validate_relation_parcel_areas`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_validate_relation_parcel_areas`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `parcels["parcel_id"].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.geometry.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.index.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input(calculation.crs).equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `CRS.from_epsg` | `pyproj.CRS.from_epsg` |
| `calculation.to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `calculation.geometry.area.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `np.isfinite(areas).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.isfinite` | `numpy.isfinite` |
| `(areas <= 0).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `calculation["parcel_id"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `areas.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations[<br>        ["parcel_id", "parcel_metric_area_m2"]<br>    ].itertuples` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isfinite` | `math.isfinite` |
| `technical_overlay_tolerance` | `landscout.common.planning_overlay.technical_overlay_tolerance` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `abs` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `parcels.geometry.copy`<br>`calculation.to_crs`<br>`calculation.geometry.area.to_numpy`<br>`technical_overlay_tolerance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_local_domains`

**Purpose:** Implements `validate local domains` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_local_domains(parcels: gpd.GeoDataFrame, relations: pd.DataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>                "parcel aggregation status is outside the allowed domain"<br>            )` under lexical guard `aggregation_status not in AGGREGATION_STATUSES`.
  - `BessPlanningFeatureParcelAggregationError(<br>                    "parcel precheck status is outside the allowed domain"<br>                )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                    "parcel confidence is outside the allowed domain"<br>                )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                    "parcel status priority must be a positive integer"<br>                )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "non-decision parcel contains an invented decision"<br>            )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "parcel relation role is outside the allowed domain"<br>            )` under lexical guard `role not in RELATION_ROLES`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "parcel relation selected flag contradicts its role"<br>            )` under lexical guard `selected is not (role == "SELECTED_CONTROLLING")`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "relation aggregation status is outside the allowed domain"<br>            )` under lexical guard `aggregation_status not in AGGREGATION_STATUSES`.
  - `BessPlanningFeatureParcelAggregationError(<br>                    "relation parcel status is outside the allowed domain"<br>                )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                    "relation parcel confidence is outside the allowed domain"<br>                )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                    "relation parcel priority must be a positive integer"<br>                )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "non-decision relation contains an invented parcel decision"<br>            )` under lexical guard `aggregation_status == "AGGREGATED_EXACT_POLICY"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_validate_local_domains`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_validate_local_domains`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `_null_value` | `landscout.stages.aggregate_bess_planning_feature_policy._null_value` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_json_ids` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_json_ids` |
| `relations.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_relation_priority`

**Purpose:** Implements `relation priority` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _relation_priority(row: dict[str, object]) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `int(value)`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "Applied relation priority must be a positive integer"<br>        )` under lexical guard `isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `_relation_priority`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `_relation_priority`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |

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
def _relation_priority(row: dict[str, object]) -> int:
    value = row["bess_cnig_status_priority"]
    if isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0:
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation priority must be a positive integer"
        )
    return int(value)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_parcel_summary`

**Purpose:** Implements `parcel summary` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _parcel_summary(
    parcel_relations: list[dict[str, object]],
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[dict[str, object], list[dict[str, object]]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[dict[str, object], list[dict[str, object]]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcel_relations` | positional-or-keyword | `list[dict[str, object]]` | `required` |
| `application` | positional-or-keyword | `BessPlanningFeatureApplicationResult \| _ApplicationLineage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `summary, assessed`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "Relation type is outside the aggregation contract"<br>        )` under lexical guard `len(controlling) + len(contextual) != len(parcel_relations)`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "Controlling application status is invalid"<br>        )` under lexical guard `len(exact) + len(unresolved) != len(controlling)`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "Applied relation status and priority are invalid"<br>            )` under lexical guard `isinstance(priority, bool)<br>            or not isinstance(priority, Integral)<br>            or int(priority) <= 0<br>            or not isinstance(status, str)`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "Applied relation status and priority mapping is not one-to-one"<br>        )` under lexical guard `any(len(statuses) != 1 for statuses in priority_statuses.values()) or any(<br>        len(priority_values) != 1 for priority_values in status_priorities.values()<br>    )`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "Selected relation confidence is invalid"<br>            )` under lexical guard `unresolved`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_parcel_summary`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_parcel_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `priorities.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `priority_statuses.setdefault(normalized_priority, set()).add` | `unresolved local/third-party receiver; no ownership inferred` |
| `priority_statuses.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `status_priorities.setdefault(status, set()).add` | `unresolved local/third-party receiver; no ownership inferred` |
| `status_priorities.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `priority_statuses.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `status_priorities.values` | `unresolved local/third-party receiver; no ownership inferred` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `next` | `unresolved local/third-party receiver; no ownership inferred` |
| `iter` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_relation_priority` | `landscout.stages.aggregate_bess_planning_feature_policy._relation_priority` |
| `min` | `unresolved local/third-party receiver; no ownership inferred` |
| `assessed.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `roles.count` | `unresolved local/third-party receiver; no ownership inferred` |
| `_json_ids` | `landscout.stages.aggregate_bess_planning_feature_policy._json_ids` |

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
| In-memory mutation | `priorities.append(normalized_priority)`<br>`priority_statuses.setdefault(normalized_priority, set()).add(status)`<br>`priority_statuses.setdefault(normalized_priority, set())`<br>`status_priorities.setdefault(status, set()).add(normalized_priority)`<br>`status_priorities.setdefault(status, set())`<br>`assessed.append(<br>            {<br>                **row,<br>                "bess_cnig_parcel_relation_role": role,<br>                "bess_cnig_selected_for_parcel_status": role == "SELECTED_CONTROLLING",<br>                "bess_cnig_resulting_parcel_aggregation_status": aggregation_status,<br>                "bess_cnig_resulting_parcel_precheck_status": selected_status,<br>                "bess_cnig_resulting_parcel_precheck_confidence": selected_confidence,<br>                "bess_cnig_resulting_parcel_status_priority": selected_priority,<br>            }<br>        )` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_assign_columns`

**Purpose:** Implements `assign columns` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _assign_columns(
    frame: pd.DataFrame, rows: list[dict[str, object]], columns: tuple[str, ...]
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `rows` | positional-or-keyword | `list[dict[str, object]]` | `required` |
| `columns` | positional-or-keyword | `tuple[str, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_assign_columns`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `_assign_columns`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.array` | `pandas.array` |

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
| In-memory mutation | `frame[column] = pd.array(values, dtype="Int64")`<br>`frame[column] = pd.array(values, dtype="bool")`<br>`frame[column] = pd.array(values, dtype="str")` |
| Direct parameter mutation | `frame[column] = pd.array(values, dtype="Int64")`<br>`frame[column] = pd.array(values, dtype="bool")`<br>`frame[column] = pd.array(values, dtype="str")` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_aggregate_frames`

**Purpose:** Implements `aggregate frames` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _aggregate_frames(
    source_parcels: gpd.GeoDataFrame,
    source_relations: pd.DataFrame,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[gpd.GeoDataFrame, pd.DataFrame]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `source_relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `application` | positional-or-keyword | `BessPlanningFeatureApplicationResult \| _ApplicationLineage` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parcels, assessments`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "Aggregation columns already exist on source inputs"<br>        )` under lexical guard `any(column in source_parcels.columns for column in PARCEL_COLUMNS) or any(<br>        column in source_relations.columns for column in RELATION_COLUMNS<br>    )`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "Aggregation inputs lack parcel_id"<br>        )` under lexical guard `"parcel_id" not in source_parcels or "parcel_id" not in source_relations`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "Relation references an unknown parcel"<br>        )` under lexical guard `any(value not in known for value in source_relations["parcel_id"])`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `_aggregate_frames`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `_aggregate_frames`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_aggregate_frames`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_aggregate_frames`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_parcel_frame` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_parcel_frame` |
| `_validate_application_relations` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_application_relations` |
| `_validate_relation_parcel_areas` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_relation_parcel_areas` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_ids.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_relations.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `grouped[str(row["parcel_id"])].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_parcel_summary` | `landscout.stages.aggregate_bess_planning_feature_policy._parcel_summary` |
| `summaries.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `assessment_rows.extend` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_assign_columns` | `landscout.stages.aggregate_bess_planning_feature_policy._assign_columns` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `source_relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `assessed_by_parcel[str(row["parcel_id"])].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `ordered_assessed.append` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `grouped[str(row["parcel_id"])].append(row)`<br>`summaries.append(summary)`<br>`assessment_rows.extend(assessed)`<br>`assessed_by_parcel[str(row["parcel_id"])].append(row)`<br>`cursor[parcel_id] += 1`<br>`ordered_assessed.append(item)` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_component_metadata`

**Purpose:** Implements `component metadata` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _component_metadata(
    result: BessPlanningFeatureParcelAggregationResult,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureParcelAggregationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        field: getattr(result, field)<br>        for field in RESULT_SCALAR_FIELDS<br>        if field<br>        not in {<br>            "relation_assessments_content_sha256",<br>            "parcels_content_sha256",<br>            "complete_result_content_sha256",<br>        }<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_result_with_hashes` via `_component_metadata`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_result_with_hashes` via `_component_metadata`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_with_hashes`

**Purpose:** Implements `result with hashes` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _result_with_hashes(
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
  - `replace(components, complete_result_content_sha256=complete)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `_result_with_hashes`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `_result_with_hashes`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_result_with_hashes`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_result_with_hashes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_component_metadata` | `landscout.stages.aggregate_bess_planning_feature_policy._component_metadata` |
| `_canonical_sha256` | `landscout.stages.aggregate_bess_planning_feature_policy._canonical_sha256` |
| `_frame_payload` | `landscout.stages.aggregate_bess_planning_feature_policy._frame_payload` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_result`

**Purpose:** Implements `build result` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _build_result(
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `application` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_result_with_hashes(result)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `_build_result`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `_build_result`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_build_result`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_build_result`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_build_result`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_build_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_aggregate_frames` | `landscout.stages.aggregate_bess_planning_feature_policy._aggregate_frames` |
| `BessPlanningFeatureParcelAggregationResult` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult` |
| `_frame_sha256` | `landscout.stages.aggregate_bess_planning_feature_policy._frame_sha256` |
| `_result_with_hashes` | `landscout.stages.aggregate_bess_planning_feature_policy._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_frame_sha256`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compare_frame`

**Purpose:** Implements `compare frame` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `actual` | positional-or-keyword | `pd.DataFrame` | `required` |
| `expected` | positional-or-keyword | `pd.DataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            f"{label} differs from deterministic aggregation"<br>        )` under lexical guard `_frame_payload(actual) != _frame_payload(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_compare_frame`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_result_envelope` via `_compare_frame`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_compare_frame`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_compare_frame`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_compare_frame`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_compare_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_frame_payload` | `landscout.stages.aggregate_bess_planning_feature_policy._frame_payload` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |

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
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} differs from deterministic aggregation"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result_envelope`

**Purpose:** Implements `validate result envelope` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_result_envelope(
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureParcelAggregationResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError("result has the wrong type")` under lexical guard `not isinstance(result, BessPlanningFeatureParcelAggregationResult)`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "unsupported parcel aggregation result schema"<br>        )` under lexical guard `type(result.result_hash_schema_version) is not int<br>        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "parcel aggregation scope is invalid"<br>        )` under lexical guard `result.aggregation_scope != AGGREGATION_SCOPE<br>        or result.policy_scope != POLICY_SCOPE`.
  - `BessPlanningFeatureParcelAggregationError(str(error))` under lexical guard `field.endswith("sha256")`.
  - `BessPlanningFeatureParcelAggregationError(str(error))`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "application result schema must be exactly 2"<br>        )` under lexical guard `type(result.application_result_hash_schema_version) is not int<br>        or result.application_result_hash_schema_version<br>        != APPLICATION_RESULT_HASH_SCHEMA_VERSION`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "parcel aggregation flags are invalid"<br>        )` under lexical guard `any(<br>        value is not expected<br>        for value, expected in (<br>            (result.local_feature_text_interpreted, False),<br>            (result.local_regulation_content_interpreted, False),<br>            (result.legal_conclusion_produced, False),<br>            (result.parcel_status_aggregated, True),<br>            (result.parcel_rejection_performed, False),<br>            (result.score_calculated, False),<br>        )<br>    )`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "aggregation output frame types are invalid"<br>        )` under lexical guard `not isinstance(result.parcels, gpd.GeoDataFrame)<br>        or not isinstance(result.relation_assessments, pd.DataFrame)<br>        or isinstance(result.relation_assessments, gpd.GeoDataFrame)`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "parcel output contains duplicate columns"<br>        )` under lexical guard `result.parcels.columns.duplicated().any()`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "relation assessments contain duplicate columns"<br>        )` under lexical guard `result.relation_assessments.columns.duplicated().any()`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "aggregation output suffix schema is invalid"<br>        )` under lexical guard `tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) != PARCEL_COLUMNS<br>        or tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])<br>        != RELATION_COLUMNS`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "parcel aggregation string dtype is invalid"<br>            )` under lexical guard `str(result.parcels[column].dtype) != "str"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "parcel aggregation integer dtype is invalid"<br>            )` under lexical guard `str(result.parcels[column].dtype) != "Int64"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "parcel aggregation bool dtype is invalid"<br>            )` under lexical guard `str(result.parcels[column].dtype) != "bool"`.
  - `BessPlanningFeatureParcelAggregationError(<br>                "relation assessment string dtype is invalid"<br>            )` under lexical guard `str(result.relation_assessments[column].dtype) != "str"`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "relation assessment dtype is invalid"<br>        )` under lexical guard `str(result.relation_assessments["bess_cnig_selected_for_parcel_status"].dtype)<br>        != "bool"<br>        or str(<br>            result.relation_assessments[<br>                "bess_cnig_resulting_parcel_status_priority"<br>            ].dtype<br>        )<br>        != "Int64"`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "source parcel content SHA256 is invalid"<br>        )` under lexical guard `result.source_parcels_content_sha256 != _frame_sha256(<br>        source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"<br>    )`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "source application relation content SHA256 is invalid"<br>        )` under lexical guard `result.source_application_relations_content_sha256 != _frame_sha256(<br>        source_relations,<br>        "landscout.bess_cnig_parcel_aggregation.source_application_relations",<br>    )`.
  - `BessPlanningFeatureParcelAggregationError(f"{field} is invalid")` under lexical guard `getattr(result, field) != getattr(rebuilt, field)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `_validate_result_envelope`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `_validate_result_envelope`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_result_envelope`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_result_envelope`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_result_envelope`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_result_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `field.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_string` | `landscout.stages.aggregate_bess_planning_feature_policy._sha256_string` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.aggregate_bess_planning_feature_policy._exact_string` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relation_assessments.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relation_assessments.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_parcel_frame` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_parcel_frame` |
| `_validate_local_domains` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_local_domains` |
| `result.parcels.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `result.relation_assessments.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_frame_sha256` | `landscout.stages.aggregate_bess_planning_feature_policy._frame_sha256` |
| `_ApplicationLineage` | `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage` |
| `_validate_application_relations` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_application_relations` |
| `_aggregate_frames` | `landscout.stages.aggregate_bess_planning_feature_policy._aggregate_frames` |
| `_compare_frame` | `landscout.stages.aggregate_bess_planning_feature_policy._compare_frame` |
| `_result_with_hashes` | `landscout.stages.aggregate_bess_planning_feature_policy._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_string`<br>`_frame_sha256`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `result.parcels.drop(columns=list(PARCEL_COLUMNS))`<br>`result.relation_assessments.drop(columns=list(RELATION_COLUMNS))` |
| Direct parameter mutation | `result.parcels.drop(columns=list(PARCEL_COLUMNS))`<br>`result.relation_assessments.drop(columns=list(RELATION_COLUMNS))` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_locks`

**Purpose:** Implements `validate source locks` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

**Exact signature**

```python
def _validate_source_locks(
    result: BessPlanningFeatureParcelAggregationResult
    | BessPlanningFeatureParcelAggregationArtifactManifest,
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureParcelAggregationResult \| BessPlanningFeatureParcelAggregationArtifactManifest` | `required` |
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `application` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "parcel aggregation source lock differs"<br>        )` under lexical guard `any(actual != expected for actual, expected in comparisons)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_source_locks`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_source_locks`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_source_locks`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_source_locks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_frame_sha256` | `landscout.stages.aggregate_bess_planning_feature_policy._frame_sha256` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_frame_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_application_source`

**Purpose:** Implements `validate application source` within the file role: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `policy_config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig \| str \| Path` | `required` |
| `policy_result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |
| `application_result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>            "Source-complete application validation failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `_validate_application_source`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `_validate_application_source`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_application_source`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_application_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_bess_planning_feature_application_result` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `aggregate_bess_planning_feature_policy_to_parcels`

**Purpose:** Validate the application once and aggregate its relations to every parcel.

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

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `policy_config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig \| str \| Path` | `required` |
| `policy_result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |
| `application_result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `re-raise`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "Parcel aggregation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::_aggregation_fixture` via `aggregate_bess_planning_feature_policy_to_parcels`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::_aggregation_fixture` via `aggregate_bess_planning_feature_policy_to_parcels`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` via `aggregate_bess_planning_feature_policy_to_parcels`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved` via `aggregate_bess_planning_feature_policy_to_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_application_source` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_application_source` |
| `_build_result` | `landscout.stages.aggregate_bess_planning_feature_policy._build_result` |
| `_validate_result_envelope` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_result_envelope` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_bess_planning_feature_parcel_aggregation_result`

**Purpose:** Independently validate and rebuild one persisted parcel aggregation result.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `policy_config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig \| str \| Path` | `required` |
| `policy_result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |
| `application_result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |
| `result` | positional-or-keyword | `BessPlanningFeatureParcelAggregationResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>                    f"Aggregation {field} differs"<br>                )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `re-raise`.
  - `BessPlanningFeatureParcelAggregationError(<br>            "Parcel aggregation result validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_local_corruption_fast_fails_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_local_corruption_fast_fails_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_representative_intrinsic_failures_all_precede_heavy_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `validate_bess_planning_feature_parcel_aggregation_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `validate_bess_planning_feature_parcel_aggregation_result`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `validate_bess_planning_feature_parcel_aggregation_result`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_parcel_area_defect_fast_fails_before_application_source_validation` via `validate_bess_planning_feature_parcel_aggregation_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_envelope` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_result_envelope` |
| `_validate_source_locks` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_source_locks` |
| `_validate_application_source` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_application_source` |
| `_build_result` | `landscout.stages.aggregate_bess_planning_feature_policy._build_result` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `_compare_frame` | `landscout.stages.aggregate_bess_planning_feature_policy._compare_frame` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_read_verified_artifact`

**Purpose:** Read one byte-sealed aggregation artifact and prove its physical content against the immutable manifest record.

- Exact signature: `def _read_verified_artifact( path: Path, record: BessPlanningFeatureParcelAggregationArtifactRecord ) -> pd.DataFrame:`
- Ordered algorithm:
  1. Require the physical basename to equal the manifest filename.
  2. Read exact bytes and verify byte size and SHA256.
  3. Load geospatial or plain Parquet according to the record flag.
  4. Verify row count.
  5. Rebuild the deterministic frame schema, convert it with `freeze_json_mapping`, and compare it with the immutable manifest signature.
  6. For parcel artifacts, require a GeoDataFrame and CRS, canonicalize the physical CRS through `CRS.to_json_dict()` and `freeze_json_mapping`, and compare it with the immutable record CRS.
  7. Reject a non-geospatial relation-assessment artifact that loads as a GeoDataFrame; otherwise return the frame.
- Side effects: reads artifact bytes and parses Parquet in memory; performs SHA256 and CRS/schema validation; writes nothing and does not mutate the record.

### `load_bess_planning_feature_parcel_aggregation_artifacts`

**Purpose:** Load byte-sealed outputs and bind them to exact lightweight upstreams.

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

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureParcelAggregationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `manifest_path` | positional-or-keyword | `str \| Path` | `required` |
| `parcels_path` | positional-or-keyword | `str \| Path` | `required` |
| `relation_assessments_path` | positional-or-keyword | `str \| Path` | `required` |
| `source_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `application_result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessPlanningFeatureParcelAggregationError(<br>                "Parcel artifact is not geospatial"<br>            )` under lexical guard `not isinstance(loaded_parcels, gpd.GeoDataFrame)`.
  - `BessPlanningFeatureParcelAggregationError(<br>                    f"Aggregation artifact scalar {field} differs from upstream rebuild"<br>                )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `re-raise`.
  - `BessPlanningFeatureParcelAggregationError(<br>            f"Parcel aggregation artifacts are invalid: {error}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    load_bess_planning_feature_parcel_aggregation_artifacts,
    validate_bess_planning_feature_parcel_aggregation_result,
)`
- import: `tests.unit.test_aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.aggregate_bess_planning_feature_policy import (
    load_bess_planning_feature_parcel_aggregation_artifacts as _load_aggregation_artifacts,
)`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_load_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `_load_aggregation_artifacts`
- direct call: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_load_aggregation_artifacts`
- value/type reference: `tests.unit.test_aggregate_bess_planning_feature_policy::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_load_aggregation_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_bess_planning_feature_application_result_envelope` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result_envelope` |
| `_validate_parcel_frame` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_parcel_frame` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `Path(manifest_path).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.model_validate` |
| `_validate_source_locks` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_source_locks` |
| `_read_verified_artifact` | `landscout.stages.aggregate_bess_planning_feature_policy._read_verified_artifact` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `BessPlanningFeatureParcelAggregationResult` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_result_envelope` | `landscout.stages.aggregate_bess_planning_feature_policy._validate_result_envelope` |
| `_build_result` | `landscout.stages.aggregate_bess_planning_feature_policy._build_result` |
| `_compare_frame` | `landscout.stages.aggregate_bess_planning_feature_policy._compare_frame` |

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
        payload = loads_strict_json_object(Path(manifest_path).read_bytes())
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.




## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `RESULT_HASH_SCHEMA_VERSION`, `ARTIFACT_MANIFEST_SCHEMA_VERSION`, `APPLICATION_RESULT_HASH_SCHEMA_VERSION`, `PARCEL_COLUMNS`, `RELATION_COLUMNS`, `PARCEL_STRING_COLUMNS`, `PARCEL_INTEGER_COLUMNS`, `PARCEL_BOOL_COLUMNS`, `RELATION_STRING_COLUMNS`, `RESULT_FRAME_FIELDS`, `RESULT_SCALAR_FIELDS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `BessPlanningFeatureParcelAggregationArtifactManifest` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest` |
| `BessPlanningFeatureParcelAggregationError` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError` |
| `BessPlanningFeatureParcelAggregationResult` | `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult` |
| `aggregate_bess_planning_feature_policy_to_parcels` | `landscout.stages.aggregate_bess_planning_feature_policy.aggregate_bess_planning_feature_policy_to_parcels` |
| `load_bess_planning_feature_parcel_aggregation_artifacts` | `landscout.stages.aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts` |
| `validate_bess_planning_feature_parcel_aggregation_result` | `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Aggregate exact BESS CNIG feature-policy relations to preserved parcels."""

from __future__ import annotations

import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from io import BytesIO
from numbers import Integral, Real
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
    field_serializer,
    model_validator,
)
from pyproj import CRS
from shapely import get_coordinate_dimension, to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.bess_application_contract import (
    ALLOWED_CONFIDENCES,
    ALLOWED_PRECHECK_STATUSES,
    NULL_LITERALS,
    POLICY_SCOPE,
    validate_bess_application_relation_frame,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.immutable_mapping import (
    freeze_json_mapping,
    to_plain_json_value,
)
from landscout.common.planning_overlay import technical_overlay_tolerance
from landscout.common.strict_json import loads_strict_json, loads_strict_json_object
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)

__all__ = [
    "BessPlanningFeatureParcelAggregationArtifactManifest",
    "BessPlanningFeatureParcelAggregationError",
    "BessPlanningFeatureParcelAggregationResult",
    "aggregate_bess_planning_feature_policy_to_parcels",
    "load_bess_planning_feature_parcel_aggregation_artifacts",
    "validate_bess_planning_feature_parcel_aggregation_result",
]

RESULT_HASH_SCHEMA_VERSION = 1
ARTIFACT_MANIFEST_SCHEMA_VERSION = 1
APPLICATION_RESULT_HASH_SCHEMA_VERSION = 2
AGGREGATION_SCOPE = "PARCEL_POLICY_AGGREGATION_ONLY"
CONFIDENCE_METHOD = "LOWEST_CONFIDENCE_FOR_SELECTED_STATUS"
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"

CONTROLLING_RELATION_TYPES = frozenset({"AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"})
CONTEXT_RELATION_TYPES = frozenset({"TOUCH_ONLY", "BOUNDARY_TOUCH"})
AGGREGATION_STATUSES = frozenset(
    {
        "AGGREGATED_EXACT_POLICY",
        "UNRESOLVED_CONTROLLING_CODE_PAIR",
        "TOUCH_ONLY_RELATIONS_ONLY",
        "NO_PLANNING_FEATURE_RELATION",
    }
)
RELATION_ROLES = frozenset(
    {
        "SELECTED_CONTROLLING",
        "LOWER_PRIORITY_CONTROLLING",
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    }
)
CONFIDENCE_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")

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
RELATION_STRING_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
)

ArtifactRole = Literal["PARCELS", "RELATION_ASSESSMENTS"]
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = ("PARCELS", "RELATION_ASSESSMENTS")


class BessPlanningFeatureParcelAggregationError(ValueError):
    """Raised when parcel aggregation integrity cannot be proven."""


@dataclass(frozen=True)
class _ApplicationLineage:
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    policy_profile: str
    policy_sha256: str
    policy_complete_result_content_sha256: str
    complete_result_content_sha256: str


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value


def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text


class BessPlanningFeatureParcelAggregationArtifactRecord(_StrictModel):
    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: Mapping[StrictStr, object]
    geospatial: StrictBool
    crs: Mapping[StrictStr, object] | None

    @field_serializer("frame_schema_signature", "crs")
    def _serialize_immutable_json_mapping(
        self, value: Mapping[str, object] | None
    ) -> object:
        return to_plain_json_value(value)

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
        frozen_signature = freeze_json_mapping(self.frame_schema_signature)
        frozen_crs = freeze_json_mapping(self.crs) if self.crs is not None else None
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be non-negative")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be positive")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geo = self.artifact_role == "PARCELS"
        if self.geospatial is not expected_geo:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = frozen_signature.get("crs")
        if expected_geo:
            if frozen_crs is None or signature_crs != frozen_crs:
                raise ValueError("parcel artifact CRS is missing or inconsistent")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("relation artifact must not declare CRS")
        object.__setattr__(
            self,
            "frame_schema_signature",
            frozen_signature,
        )
        if frozen_crs is not None:
            object.__setattr__(self, "crs", frozen_crs)
        return self


@dataclass(frozen=True)
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


RESULT_FRAME_FIELDS = ("relation_assessments", "parcels")
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureParcelAggregationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)


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


def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    return {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }


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


def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "frame": _frame_payload(frame),
        }
    )


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


def _json_ids(values: list[object]) -> str:
    ids = sorted({_validate_feature_id(value) for value in values})
    return json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(",", ":"))


def _validate_json_ids(value: object, label: str) -> None:
    if not isinstance(value, str):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        )
    try:
        parsed = loads_strict_json(value)
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


def _relation_priority(row: dict[str, object]) -> int:
    value = row["bess_cnig_status_priority"]
    if isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0:
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation priority must be a positive integer"
        )
    return int(value)


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


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} differs from deterministic aggregation"
        )


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
    if (
        freeze_json_mapping(deterministic_frame_schema_signature(frame))
        != record.frame_schema_signature
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact frame schema differs"
        )
    if record.geospatial:
        if (
            not isinstance(frame, gpd.GeoDataFrame)
            or frame.crs is None
            or freeze_json_mapping(CRS.from_user_input(frame.crs).to_json_dict())
            != record.crs
        ):
            raise BessPlanningFeatureParcelAggregationError(
                "Aggregation parcel artifact CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation assessment artifact is unexpectedly geospatial"
        )
    return frame


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
        payload = loads_strict_json_object(Path(manifest_path).read_bytes())
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
