# `src/landscout/stages/apply_bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/apply_bess_planning_feature_policy.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.
- Source SHA256: `911527985762d94e9e029aa6babc27e4aa89cb7ba3bf4c15ccebbef0d6fb6060`

## 1. STEP 7F.1A.4 contract delta

- Uses strict/frozen upstream policy/config contracts and independently revalidates supplied result envelopes before local source-bound comparison.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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
- `from pathlib import Path`
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
    APPLICATION_SCOPE,
    FLAG_COLUMNS,
    POLICY_COLUMNS,
    POLICY_SCOPE,
    STRING_POLICY_COLUMNS,
    ApplicationStatus,
    validate_bess_application_feature_catalogs,
    validate_bess_application_relation_frame,
)`
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.common.planning_overlay import technical_overlay_tolerance`
- `from landscout.common.strict_json import loads_strict_json_object`
- `from landscout.sources.gpu_fr import GpuPlanningDocument`
- `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "BessPlanningFeatureApplicationArtifactManifest",
    "BessPlanningFeatureApplicationError",
    "BessPlanningFeatureApplicationResult",
    "apply_bess_planning_feature_policy",
    "load_bess_planning_feature_application_artifacts",
    "validate_bess_planning_feature_application_result",
    "validate_bess_planning_feature_application_result_envelope",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `BessPlanningFeatureApplicationArtifactManifest`
  - `BessPlanningFeatureApplicationError`
  - `BessPlanningFeatureApplicationResult`
  - `apply_bess_planning_feature_policy`
  - `load_bess_planning_feature_application_artifacts`
  - `validate_bess_planning_feature_application_result`
  - `validate_bess_planning_feature_application_result_envelope`

### `RESULT_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RESULT_HASH_SCHEMA_VERSION = 2
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARTIFACT_MANIFEST_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARTIFACT_KIND`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ArtifactRole`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ArtifactRole = Literal[
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARTIFACT_ROLES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = (
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `SURFACE_FEATURES`
  - `LINE_FEATURES`
  - `POINT_FEATURES`
  - `RELATIONS`

### `RELATION_FEATURE_AGREEMENT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RELATION_FEATURE_AGREEMENT_COLUMNS = (
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
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `source_feature_id`
  - `source_identity_kind`
  - `source_identity_field`
  - `logical_layer`
  - `feature_family`
  - `geometry_kind`
  - `type_code_raw`
  - `subtype_code_raw`
  - `label_raw`
  - `text_raw`
  - `source_document_id`
  - `source_archive_sha256`
  - `source_layer`
  - `source_validity_date_raw`
  - `regulation_filename_raw`
  - `official_code_status`
  - `official_code_label`
  - `official_legal_reference`
  - `official_regulation_reference`
  - `official_code_source_url`
  - `official_code_profile`
  - `official_code_profile_sha256`

### `SHA_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CODE_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
CODE_PATTERN = re.compile(r"[0-9]{2}")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `RESULT_FRAME_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RESULT_FRAME_FIELDS = (
    "surface_features",
    "line_features",
    "point_features",
    "relations",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `surface_features`
  - `line_features`
  - `point_features`
  - `relations`

### `RESULT_SCALAR_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureApplicationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `BessPlanningFeatureApplicationError`

**Source purpose:** Raised when exact feature-policy propagation cannot be proven.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_canonical_value` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_canonical_value` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_validate_application_geometry` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_application_geometry` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_canonical_json_sha256` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_canonical_json_sha256` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_policy_lookup` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_policy_lookup` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_feature_rows_by_id` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_feature_rows_by_id` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_validate_relation_rows` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_relation_rows` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_validate_coded_policy_compatibility` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_coded_policy_compatibility` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_compare_frame` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_compare_frame` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_read_verified_artifact` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_read_verified_artifact` via `BessPlanningFeatureApplicationError`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationError`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationError`
- import: `tests.unit.test_apply_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_m_and_zm_application_geometries_are_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_inconsistent_official_status_and_policy_match_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_complete_relation_facts_must_match_referenced_feature` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_relation_feature_id_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_application_relation_pair_is_rejected_locally` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_feature_id_is_exact_and_portable` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_parcel_id_is_exact` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_application_relation_type_is_rejected_locally` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_invalid_policy_domains_fail_local_validation` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_literal_null_replacements_are_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_official_and_application_statuses_cannot_contradict` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_any_true_row_boundary_flag_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_malformed_local_result_fast_fails_before_heavy_validation` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_application_source_lock_mutation_fast_fails` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_pair_artifact_fails_local_loading` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_geometry_role_is_intrinsic` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_metric_must_match_geometry` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_catalog_requires_canonical_crs_and_global_identity` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_identity_is_validated_locally` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_participates_in_global_policy_mapping` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_locks_policy_result_schema_exactly` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_locks_cnig_result_schema_exactly` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_z_geoparquet_artifact_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_wrong_dtype_artifact_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_artifact_manifest_rejects_invalid_contract` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_uses_strict_json_before_artifact_read` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_physical_replacement_before_loading_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_row_lineage_must_match_application_envelope` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_resolved_official_row_requires_label_and_envelope_profile` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_unknown_official_row_rejects_invented_label_or_url` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_feature_prefix_has_exact_canonical_schema` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_relation_prefix_has_exact_canonical_schema` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_all_null_raw_column_transition` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `BessPlanningFeatureApplicationError`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `BessPlanningFeatureApplicationError`

**Exact class source**

```python
class BessPlanningFeatureApplicationError(ValueError):
    """Raised when exact feature-policy propagation cannot be proven."""
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

### `BessPlanningFeatureApplicationArtifactRecord`

**Source purpose:** One physical output record within the application manifest.

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

- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactRecord._validate_record` via `BessPlanningFeatureApplicationArtifactRecord`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_read_verified_artifact` via `BessPlanningFeatureApplicationArtifactRecord`

**Exact class source**

```python
class BessPlanningFeatureApplicationArtifactRecord(_StrictModel):
    """One physical output record within the application manifest."""

    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: dict[StrictStr, object]
    geospatial: StrictBool
    crs: dict[StrictStr, object] | None

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        signature_geometry = self.frame_schema_signature.get("geometry_column")
        if expected_geospatial:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        return self
```

### `BessPlanningFeatureApplicationResult`

**Source purpose:** Immutable exact policy propagation over coded features and relations.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | `result_hash_schema_version: int` |
| `application_scope` | `str` | `required` | `application_scope: str` |
| `policy_scope` | `str` | `required` | `policy_scope: str` |
| `local_feature_text_interpreted` | `bool` | `required` | `local_feature_text_interpreted: bool` |
| `local_regulation_content_interpreted` | `bool` | `required` | `local_regulation_content_interpreted: bool` |
| `legal_conclusion_produced` | `bool` | `required` | `legal_conclusion_produced: bool` |
| `parcel_status_aggregated` | `bool` | `required` | `parcel_status_aggregated: bool` |
| `parcel_rejection_performed` | `bool` | `required` | `parcel_rejection_performed: bool` |
| `score_calculated` | `bool` | `required` | `score_calculated: bool` |
| `policy_profile` | `str` | `required` | `policy_profile: str` |
| `policy_sha256` | `str` | `required` | `policy_sha256: str` |
| `policy_result_hash_schema_version` | `int` | `required` | `policy_result_hash_schema_version: int` |
| `policy_complete_result_content_sha256` | `str` | `required` | `policy_complete_result_content_sha256: str` |
| `cnig_profile` | `str` | `required` | `cnig_profile: str` |
| `cnig_profile_sha256` | `str` | `required` | `cnig_profile_sha256: str` |
| `cnig_result_hash_schema_version` | `int` | `required` | `cnig_result_hash_schema_version: int` |
| `cnig_complete_result_content_sha256` | `str` | `required` | `cnig_complete_result_content_sha256: str` |
| `source_document_id` | `str` | `required` | `source_document_id: str` |
| `source_archive_sha256` | `str` | `required` | `source_archive_sha256: str` |
| `cnig_surface_features_content_sha256` | `str` | `required` | `cnig_surface_features_content_sha256: str` |
| `cnig_line_features_content_sha256` | `str` | `required` | `cnig_line_features_content_sha256: str` |
| `cnig_point_features_content_sha256` | `str` | `required` | `cnig_point_features_content_sha256: str` |
| `cnig_relations_content_sha256` | `str` | `required` | `cnig_relations_content_sha256: str` |
| `surface_features_content_sha256` | `str` | `required` | `surface_features_content_sha256: str` |
| `line_features_content_sha256` | `str` | `required` | `line_features_content_sha256: str` |
| `point_features_content_sha256` | `str` | `required` | `point_features_content_sha256: str` |
| `relations_content_sha256` | `str` | `required` | `relations_content_sha256: str` |
| `complete_result_content_sha256` | `str` | `required` | `complete_result_content_sha256: str` |
| `surface_features` | `gpd.GeoDataFrame` | `required` | `surface_features: gpd.GeoDataFrame` |
| `line_features` | `gpd.GeoDataFrame` | `required` | `line_features: gpd.GeoDataFrame` |
| `point_features` | `gpd.GeoDataFrame` | `required` | `point_features: gpd.GeoDataFrame` |
| `relations` | `pd.DataFrame` | `required` | `relations: pd.DataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_relations` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_parcel_summary` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_aggregate_frames` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_build_result` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_component_metadata` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_component_sha256` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_complete_result_sha256` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_result_with_hashes` via `BessPlanningFeatureApplicationResult`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_relation_rows` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result_envelope` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `BessPlanningFeatureApplicationResult`
- constructor call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationResult`
- import: `tests.unit.test_apply_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_application_fixture` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_write_application_artifacts` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_coordinated_policy_mutation` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_coordinated_feature_id_mutation` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_zero_relation_feature` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_surface_touch_with_positive_area` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_replace_application_frame` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_coordinated_referenced_lineage_mutation` via `BessPlanningFeatureApplicationResult`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_swap_referenced_feature_values` via `BessPlanningFeatureApplicationResult`

**Exact class source**

```python
class BessPlanningFeatureApplicationResult:
    """Immutable exact policy propagation over coded features and relations."""

    result_hash_schema_version: int
    application_scope: str
    policy_scope: str
    local_feature_text_interpreted: bool
    local_regulation_content_interpreted: bool
    legal_conclusion_produced: bool
    parcel_status_aggregated: bool
    parcel_rejection_performed: bool
    score_calculated: bool
    policy_profile: str
    policy_sha256: str
    policy_result_hash_schema_version: int
    policy_complete_result_content_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_surface_features_content_sha256: str
    cnig_line_features_content_sha256: str
    cnig_point_features_content_sha256: str
    cnig_relations_content_sha256: str
    surface_features_content_sha256: str
    line_features_content_sha256: str
    point_features_content_sha256: str
    relations_content_sha256: str
    complete_result_content_sha256: str
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame
```

### `BessPlanningFeatureApplicationArtifactManifest`

**Source purpose:** Strict four-file physical artifact envelope.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `artifact_kind` | `Literal['BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT']` | `required` | `artifact_kind: Literal["BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"]` |
| `result_hash_schema_version` | `StrictInt` | `required` | `result_hash_schema_version: StrictInt` |
| `application_scope` | `Literal['FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY']` | `required` | `application_scope: Literal["FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"]` |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` |
| `local_feature_text_interpreted` | `StrictBool` | `required` | `local_feature_text_interpreted: StrictBool` |
| `local_regulation_content_interpreted` | `StrictBool` | `required` | `local_regulation_content_interpreted: StrictBool` |
| `legal_conclusion_produced` | `StrictBool` | `required` | `legal_conclusion_produced: StrictBool` |
| `parcel_status_aggregated` | `StrictBool` | `required` | `parcel_status_aggregated: StrictBool` |
| `parcel_rejection_performed` | `StrictBool` | `required` | `parcel_rejection_performed: StrictBool` |
| `score_calculated` | `StrictBool` | `required` | `score_calculated: StrictBool` |
| `policy_profile` | `StrictStr` | `required` | `policy_profile: StrictStr` |
| `policy_sha256` | `StrictStr` | `required` | `policy_sha256: StrictStr` |
| `policy_result_hash_schema_version` | `StrictInt` | `required` | `policy_result_hash_schema_version: StrictInt` |
| `policy_complete_result_content_sha256` | `StrictStr` | `required` | `policy_complete_result_content_sha256: StrictStr` |
| `cnig_profile` | `StrictStr` | `required` | `cnig_profile: StrictStr` |
| `cnig_profile_sha256` | `StrictStr` | `required` | `cnig_profile_sha256: StrictStr` |
| `cnig_result_hash_schema_version` | `StrictInt` | `required` | `cnig_result_hash_schema_version: StrictInt` |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | `cnig_complete_result_content_sha256: StrictStr` |
| `source_document_id` | `StrictStr` | `required` | `source_document_id: StrictStr` |
| `source_archive_sha256` | `StrictStr` | `required` | `source_archive_sha256: StrictStr` |
| `cnig_surface_features_content_sha256` | `StrictStr` | `required` | `cnig_surface_features_content_sha256: StrictStr` |
| `cnig_line_features_content_sha256` | `StrictStr` | `required` | `cnig_line_features_content_sha256: StrictStr` |
| `cnig_point_features_content_sha256` | `StrictStr` | `required` | `cnig_point_features_content_sha256: StrictStr` |
| `cnig_relations_content_sha256` | `StrictStr` | `required` | `cnig_relations_content_sha256: StrictStr` |
| `surface_features_content_sha256` | `StrictStr` | `required` | `surface_features_content_sha256: StrictStr` |
| `line_features_content_sha256` | `StrictStr` | `required` | `line_features_content_sha256: StrictStr` |
| `point_features_content_sha256` | `StrictStr` | `required` | `point_features_content_sha256: StrictStr` |
| `relations_content_sha256` | `StrictStr` | `required` | `relations_content_sha256: StrictStr` |
| `complete_result_content_sha256` | `StrictStr` | `required` | `complete_result_content_sha256: StrictStr` |
| `artifacts` | `tuple[BessPlanningFeatureApplicationArtifactRecord, ...]` | `required` | `artifacts: tuple[BessPlanningFeatureApplicationArtifactRecord, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `BessPlanningFeatureApplicationArtifactManifest`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeatureApplicationArtifactManifest`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationArtifactManifest`
- import: `tests.unit.test_apply_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_write_application_artifacts` via `BessPlanningFeatureApplicationArtifactManifest`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_filenames_are_casefold_unique` via `BessPlanningFeatureApplicationArtifactManifest`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_manifest_rejects_nonportable_filename` via `BessPlanningFeatureApplicationArtifactManifest`

**Exact class source**

```python
class BessPlanningFeatureApplicationArtifactManifest(_StrictModel):
    """Strict four-file physical artifact envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"]
    result_hash_schema_version: StrictInt
    application_scope: Literal["FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"]
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    parcel_status_aggregated: StrictBool
    parcel_rejection_performed: StrictBool
    score_calculated: StrictBool
    policy_profile: StrictStr
    policy_sha256: StrictStr
    policy_result_hash_schema_version: StrictInt
    policy_complete_result_content_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_surface_features_content_sha256: StrictStr
    cnig_line_features_content_sha256: StrictStr
    cnig_point_features_content_sha256: StrictStr
    cnig_relations_content_sha256: StrictStr
    surface_features_content_sha256: StrictStr
    line_features_content_sha256: StrictStr
    point_features_content_sha256: StrictStr
    relations_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    artifacts: tuple[BessPlanningFeatureApplicationArtifactRecord, ...]

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application artifact manifest schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application result hash schema")
        if any(
            value is not False
            for value in (
                self.local_feature_text_interpreted,
                self.local_regulation_content_interpreted,
                self.legal_conclusion_produced,
                self.parcel_status_aggregated,
                self.parcel_rejection_performed,
                self.score_calculated,
            )
        ):
            raise ValueError("application boundary flags must all be false")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.cnig_profile, "cnig_profile"),
            (self.source_document_id, "source_document_id"),
        ):
            _exact_string(exact_value, label)
        if self.policy_result_hash_schema_version != 1:
            raise ValueError("policy result hash schema must be exactly 1")
        if self.cnig_result_hash_schema_version != 5:
            raise ValueError("CNIG result hash schema must be exactly 5")
        for field in RESULT_SCALAR_FIELDS:
            if field.endswith("sha256"):
                _sha256_string(getattr(self, field), field)
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError(
                "application artifact roles are missing, extra, or unordered"
            )
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("application artifact filenames contain a duplicate")
        return self
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_exact_string`

**Purpose:** Implements `exact string` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

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
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_sha256_string` via `_exact_string`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_sha256_string` via `_exact_string`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_exact_string`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_exact_string`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_exact_string`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_exact_string`

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

**Purpose:** Implements `sha256 string` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

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
- direct call: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactRecord._validate_record` via `_sha256_string`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactRecord._validate_record` via `_sha256_string`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_sha256_string`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_sha256_string`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_sha256_string`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_sha256_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string` | `landscout.stages.apply_bess_planning_feature_policy._exact_string` |
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

### `BessPlanningFeatureApplicationArtifactRecord._validate_record`

**Purpose:** Implements `validate record` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `BessPlanningFeatureApplicationArtifactRecord`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("artifact row_count must be a non-negative integer")` under lexical guard `type(self.row_count) is not int or self.row_count < 0`.
  - `ValueError("artifact size_bytes must be a positive integer")` under lexical guard `type(self.size_bytes) is not int or self.size_bytes < 1`.
  - `ValueError("artifact geospatial flag differs from its role")` under lexical guard `self.geospatial is not expected_geospatial`.
  - `ValueError("geospatial artifact CRS is missing or inconsistent")` under lexical guard `expected_geospatial`.
  - `ValueError("geospatial artifact geometry column is missing")` under lexical guard `expected_geospatial`.
  - `ValueError("non-geospatial artifact must not declare a CRS")` under lexical guard `expected_geospatial`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_portable_parquet_filename` | `landscout.common.artifact_paths.validate_portable_parquet_filename` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_string` | `landscout.stages.apply_bess_planning_feature_policy._sha256_string` |
| `self.frame_schema_signature.get` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.frame_schema_signature.get` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        signature_geometry = self.frame_schema_signature.get("geometry_column")
        if expected_geospatial:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `BessPlanningFeatureApplicationArtifactManifest._validate_manifest`

**Purpose:** Implements `validate manifest` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `BessPlanningFeatureApplicationArtifactManifest`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("unsupported application artifact manifest schema")` under lexical guard `type(self.schema_version) is not int<br>            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`.
  - `ValueError("unsupported application result hash schema")` under lexical guard `type(self.result_hash_schema_version) is not int<br>            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
  - `ValueError("application boundary flags must all be false")` under lexical guard `any(<br>            value is not False<br>            for value in (<br>                self.local_feature_text_interpreted,<br>                self.local_regulation_content_interpreted,<br>                self.legal_conclusion_produced,<br>                self.parcel_status_aggregated,<br>                self.parcel_rejection_performed,<br>                self.score_calculated,<br>            )<br>        )`.
  - `ValueError("policy result hash schema must be exactly 1")` under lexical guard `self.policy_result_hash_schema_version != 1`.
  - `ValueError("CNIG result hash schema must be exactly 5")` under lexical guard `self.cnig_result_hash_schema_version != 5`.
  - `ValueError(<br>                "application artifact roles are missing, extra, or unordered"<br>            )` under lexical guard `roles != ARTIFACT_ROLES`.
  - `ValueError("application artifact filenames contain a duplicate")` under lexical guard `len(filenames) != len(set(filenames))`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.apply_bess_planning_feature_policy._exact_string` |
| `field.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_string` | `landscout.stages.apply_bess_planning_feature_policy._sha256_string` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application artifact manifest schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application result hash schema")
        if any(
            value is not False
            for value in (
                self.local_feature_text_interpreted,
                self.local_regulation_content_interpreted,
                self.legal_conclusion_produced,
                self.parcel_status_aggregated,
                self.parcel_rejection_performed,
                self.score_calculated,
            )
        ):
            raise ValueError("application boundary flags must all be false")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.cnig_profile, "cnig_profile"),
            (self.source_document_id, "source_document_id"),
        ):
            _exact_string(exact_value, label)
        if self.policy_result_hash_schema_version != 1:
            raise ValueError("policy result hash schema must be exactly 1")
        if self.cnig_result_hash_schema_version != 5:
            raise ValueError("CNIG result hash schema must be exactly 5")
        for field in RESULT_SCALAR_FIELDS:
            if field.endswith("sha256"):
                _sha256_string(getattr(self, field), field)
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError(
                "application artifact roles are missing, extra, or unordered"
            )
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("application artifact filenames contain a duplicate")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_value`

**Purpose:** Implements `null value` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

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
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_canonical_value` via `_null_value`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_canonical_value` via `_null_value`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_null_safe_equal` via `_null_value`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_null_safe_equal` via `_null_value`

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

**Purpose:** Implements `canonical value` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

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
  - `{<br>            "coordinate_dimension": coordinate_dimension,<br>            "wkb_hex": to_wkb(<br>                value,<br>                hex=True,<br>                output_dimension=2,<br>                byte_order=1,<br>                include_srid=False,<br>            ),<br>        }`
  - `value.isoformat()`
  - `_canonical_value(value.item())`
  - `value`
  - `int(value)`
  - `number`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                "Application geometry coordinate dimension must be exactly 2D"<br>            )` under lexical guard `isinstance(value, BaseGeometry)`.
  - `BessPlanningFeatureApplicationError(<br>                "Application integrity payload contains non-finite data"<br>            )` under lexical guard `isinstance(value, Real)`.
  - `BessPlanningFeatureApplicationError(<br>        f"Unsupported application integrity value {type(value).__name__}"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_canonical_value` via `_canonical_value`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_canonical_value` via `_canonical_value`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_frame_payload` via `_canonical_value`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_frame_payload` via `_canonical_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_null_value` | `landscout.stages.apply_bess_planning_feature_policy._null_value` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `get_coordinate_dimension` | `shapely.get_coordinate_dimension` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `to_wkb` | `shapely.to_wkb` |
| `value.isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.apply_bess_planning_feature_policy._canonical_value` |
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
        coordinate_dimension = int(get_coordinate_dimension(value))
        if coordinate_dimension != 2:
            raise BessPlanningFeatureApplicationError(
                "Application geometry coordinate dimension must be exactly 2D"
            )
        return {
            "coordinate_dimension": coordinate_dimension,
            "wkb_hex": to_wkb(
                value,
                hex=True,
                output_dimension=2,
                byte_order=1,
                include_srid=False,
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
            raise BessPlanningFeatureApplicationError(
                "Application integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeatureApplicationError(
        f"Unsupported application integrity value {type(value).__name__}"
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_payload`

**Purpose:** Implements `frame payload` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

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
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_component_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_component_sha256` via `_frame_payload`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_compare_frame` via `_frame_payload`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_compare_frame` via `_frame_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `_canonical_value` | `landscout.stages.apply_bess_planning_feature_policy._canonical_value` |
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

### `_validate_application_geometry`

**Purpose:** Require supplied application geometry to remain canonical two-dimensional.

**Exact signature**

```python
def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                f"{label} active geometry column is missing"<br>            )` under lexical guard `geometry_name not in frame.columns`.
  - `BessPlanningFeatureApplicationError(<br>                    f"{label} geometry at row {position} is missing or invalid"<br>                )` under lexical guard `not isinstance(geometry, BaseGeometry)`.
  - `BessPlanningFeatureApplicationError(<br>                    f"{label} geometry at row {position} must be canonical 2D"<br>                )` under lexical guard `int(get_coordinate_dimension(geometry)) != 2`.
  - `re-raise`.
  - `BessPlanningFeatureApplicationError(<br>            f"{label} geometry contract is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_validate_application_geometry`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_validate_application_geometry`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    """Require supplied application geometry to remain canonical two-dimensional."""

    try:
        geometry_name = frame.geometry.name
        if geometry_name not in frame.columns:
            raise BessPlanningFeatureApplicationError(
                f"{label} active geometry column is missing"
            )
        for position, geometry in enumerate(frame.geometry.array):
            if not isinstance(geometry, BaseGeometry):
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} is missing or invalid"
                )
            if int(get_coordinate_dimension(geometry)) != 2:
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} must be canonical 2D"
                )
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"{label} geometry contract is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_json_sha256`

**Purpose:** Implements `canonical json sha256` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _canonical_json_sha256(value: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(encoded).hexdigest()`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>            "Application integrity payload is not canonical JSON"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_component_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_component_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_complete_result_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_complete_result_sha256` via `_canonical_json_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `sha256(encoded).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(encoded).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(
            "Application integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_safe_equal`

**Purpose:** Implements `null safe equal` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `left` | positional-or-keyword | `object` | `required` |
| `right` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `left is None and right is None`
  - `bool(left == right)`
  - `False`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `_null_safe_equal`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `_null_safe_equal`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_null_safe_equal`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_null_safe_equal`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_coded_policy_compatibility` via `_null_safe_equal`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_coded_policy_compatibility` via `_null_safe_equal`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_null_value` | `landscout.stages.apply_bess_planning_feature_policy._null_value` |
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
def _null_safe_equal(left: object, right: object) -> bool:
    left = _null_value(left)
    right = _null_value(right)
    if left is None or right is None:
        return left is None and right is None
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_lookup`

**Purpose:** Implements `policy lookup` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `lookup`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                "Compiled policy contains a duplicate exact code pair"<br>            )` under lexical guard `key in lookup`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_policy_lookup`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_policy_lookup`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `policy.policy_table.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |

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
| In-memory mutation | `lookup[key] = row` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    lookup: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in policy.policy_table.to_dict("records"):
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in lookup:
            raise BessPlanningFeatureApplicationError(
                "Compiled policy contains a duplicate exact code pair"
            )
        lookup[key] = row
    return lookup
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_values`

**Purpose:** Implements `policy values` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `dict[str, object] \| None` | `required` |
| `application_status` | positional-or-keyword | `ApplicationStatus` | `required` |
| `policy` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "bess_cnig_policy_application_status": application_status,<br>        "bess_cnig_precheck_status": None if row is None else row["precheck_status"],<br>        "bess_cnig_precheck_confidence": None if row is None else row["confidence"],<br>        "bess_cnig_status_priority": None if row is None else row["status_priority"],<br>        "bess_cnig_rationale": None if row is None else row["rationale"],<br>        "bess_cnig_required_human_action": (<br>            None if row is None else row["required_human_action"]<br>        ),<br>        "bess_cnig_limitations": None if row is None else row["limitations"],<br>        "bess_cnig_application_scope": APPLICATION_SCOPE,<br>        "bess_cnig_policy_scope": policy.policy_scope,<br>        "bess_cnig_local_feature_text_interpreted": False,<br>        "bess_cnig_local_regulation_content_interpreted": False,<br>        "bess_cnig_legal_conclusion_produced": False,<br>        "bess_cnig_parcel_status_aggregated": False,<br>        "bess_cnig_parcel_rejection_performed": False,<br>        "bess_cnig_score_calculated": False,<br>        "bess_cnig_policy_profile": policy.policy_profile,<br>        "bess_cnig_policy_sha256": policy.policy_sha256,<br>        "bess_cnig_policy_result_sha256": policy.complete_result_content_sha256,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_policy_values`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_policy_values`

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
def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
    return {
        "bess_cnig_policy_application_status": application_status,
        "bess_cnig_precheck_status": None if row is None else row["precheck_status"],
        "bess_cnig_precheck_confidence": None if row is None else row["confidence"],
        "bess_cnig_status_priority": None if row is None else row["status_priority"],
        "bess_cnig_rationale": None if row is None else row["rationale"],
        "bess_cnig_required_human_action": (
            None if row is None else row["required_human_action"]
        ),
        "bess_cnig_limitations": None if row is None else row["limitations"],
        "bess_cnig_application_scope": APPLICATION_SCOPE,
        "bess_cnig_policy_scope": policy.policy_scope,
        "bess_cnig_local_feature_text_interpreted": False,
        "bess_cnig_local_regulation_content_interpreted": False,
        "bess_cnig_legal_conclusion_produced": False,
        "bess_cnig_parcel_status_aggregated": False,
        "bess_cnig_parcel_rejection_performed": False,
        "bess_cnig_score_calculated": False,
        "bess_cnig_policy_profile": policy.policy_profile,
        "bess_cnig_policy_sha256": policy.policy_sha256,
        "bess_cnig_policy_result_sha256": policy.complete_result_content_sha256,
    }
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_assign_policy_columns`

**Purpose:** Implements `assign policy columns` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `rows` | positional-or-keyword | `list[dict[str, object]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_assign_policy_columns`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `_assign_policy_columns`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `_assign_policy_columns`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `_assign_policy_columns`

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
| In-memory mutation | `values[column] = pd.array([row[column] for row in rows], dtype="str")`<br>`values["bess_cnig_status_priority"] = pd.array(<br>        [row["bess_cnig_status_priority"] for row in rows], dtype="Int64"<br>    )`<br>`values[column] = pd.array([row[column] for row in rows], dtype="bool")`<br>`frame[column] = values[column]` |
| Direct parameter mutation | `frame[column] = values[column]` |

**Complete source-ordered implementation**

```python
def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
    values: dict[str, object] = {}
    for column in STRING_POLICY_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="str")
    values["bess_cnig_status_priority"] = pd.array(
        [row["bess_cnig_status_priority"] for row in rows], dtype="Int64"
    )
    for column in FLAG_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="bool")
    for column in POLICY_COLUMNS:
        frame[column] = values[column]
    return frame
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_apply_feature_catalog`

**Purpose:** Apply exact family/type/subtype policy to one already-coded catalog.

**Exact signature**

```python
def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalog` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `applied`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>            "Coded feature catalog is not geospatial"<br>        )` under lexical guard `not isinstance(catalog, gpd.GeoDataFrame)`.
  - `BessPlanningFeatureApplicationError(<br>            "Coded feature catalog already contains BESS policy columns"<br>        )` under lexical guard `any(column in catalog.columns for column in POLICY_COLUMNS)`.
  - `BessPlanningFeatureApplicationError(<br>            "Coded feature catalog lacks exact policy lookup fields"<br>        )` under lexical guard `not required.issubset(catalog.columns)`.
  - `BessPlanningFeatureApplicationError(<br>                "Feature type code is not an exact two-character string"<br>            )` under lexical guard `not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None`.
  - `BessPlanningFeatureApplicationError(<br>                "Feature subtype code is not an exact two-character string"<br>            )` under lexical guard `not isinstance(subtype_code, str)<br>            or CODE_PATTERN.fullmatch(subtype_code) is None`.
  - `BessPlanningFeatureApplicationError(<br>                    f"Resolved official feature has no exact policy row: {key}"<br>                )` under lexical guard `official_status == "RESOLVED_OFFICIAL"`.
  - `BessPlanningFeatureApplicationError(<br>                    f"Unknown official feature unexpectedly matches policy row: {key}"<br>                )` under lexical guard `official_status == "RESOLVED_OFFICIAL"`.
  - `BessPlanningFeatureApplicationError(<br>                "Feature official-code status is invalid"<br>            )` under lexical guard `official_status == "RESOLVED_OFFICIAL"`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `_apply_feature_catalog`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `_apply_feature_catalog`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_policy_lookup` | `landscout.stages.apply_bess_planning_feature_policy._policy_lookup` |
| `catalog.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `CODE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `lookup.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy_rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_policy_values` | `landscout.stages.apply_bess_planning_feature_policy._policy_values` |
| `catalog.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_assign_policy_columns` | `landscout.stages.apply_bess_planning_feature_policy._assign_policy_columns` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `_validate_application_geometry` | `landscout.stages.apply_bess_planning_feature_policy._validate_application_geometry` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `_validate_application_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | `policy_rows.append(_policy_values(policy_row, application_status, policy))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
    """Apply exact family/type/subtype policy to one already-coded catalog."""

    if not isinstance(catalog, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog is not geospatial"
        )
    if any(column in catalog.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog already contains BESS policy columns"
        )
    required = {
        "planning_feature_id",
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        "official_code_status",
    }
    if not required.issubset(catalog.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog lacks exact policy lookup fields"
        )
    lookup = _policy_lookup(policy)
    policy_rows: list[dict[str, object]] = []
    for row in catalog.to_dict("records"):
        type_code = row["type_code_raw"]
        subtype_code = row["subtype_code_raw"]
        if not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None:
            raise BessPlanningFeatureApplicationError(
                "Feature type code is not an exact two-character string"
            )
        if (
            not isinstance(subtype_code, str)
            or CODE_PATTERN.fullmatch(subtype_code) is None
        ):
            raise BessPlanningFeatureApplicationError(
                "Feature subtype code is not an exact two-character string"
            )
        key = (str(row["feature_family"]), type_code, subtype_code)
        official_status = row["official_code_status"]
        policy_row = lookup.get(key)
        if official_status == "RESOLVED_OFFICIAL":
            if policy_row is None:
                raise BessPlanningFeatureApplicationError(
                    f"Resolved official feature has no exact policy row: {key}"
                )
            application_status: ApplicationStatus = "APPLIED_EXACT_POLICY"
        elif official_status == "UNKNOWN_CODE_PAIR":
            if policy_row is not None:
                raise BessPlanningFeatureApplicationError(
                    f"Unknown official feature unexpectedly matches policy row: {key}"
                )
            application_status = "UNRESOLVED_CODE_PAIR"
        else:
            raise BessPlanningFeatureApplicationError(
                "Feature official-code status is invalid"
            )
        policy_rows.append(_policy_values(policy_row, application_status, policy))
    output = catalog.copy(deep=True)
    _assign_policy_columns(output, policy_rows)
    applied = gpd.GeoDataFrame(output, geometry=catalog.geometry.name, crs=catalog.crs)
    _validate_application_geometry(applied, "applied feature catalog")
    return applied
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_feature_rows_by_id`

**Purpose:** Implements `feature rows by id` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*catalogs` | variadic positional | `gpd.GeoDataFrame` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `indexed`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                    "Enriched feature ID must be an exact string"<br>                )` under lexical guard `not isinstance(feature_id, str) or not feature_id`.
  - `BessPlanningFeatureApplicationError(<br>                    "Enriched planning feature ID is not globally unique"<br>                )` under lexical guard `feature_id in indexed`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `_feature_rows_by_id`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_relations` via `_feature_rows_by_id`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_feature_rows_by_id`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_feature_rows_by_id`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `catalog.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |

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
| In-memory mutation | `indexed[feature_id] = row` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
    indexed: dict[str, dict[str, object]] = {}
    for catalog in catalogs:
        for row in catalog.to_dict("records"):
            feature_id = row["planning_feature_id"]
            if not isinstance(feature_id, str) or not feature_id:
                raise BessPlanningFeatureApplicationError(
                    "Enriched feature ID must be an exact string"
                )
            if feature_id in indexed:
                raise BessPlanningFeatureApplicationError(
                    "Enriched planning feature ID is not globally unique"
                )
            indexed[feature_id] = row
    return indexed
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_apply_relations`

**Purpose:** Propagate feature policy to relations only through planning_feature_id.

**Exact signature**

```python
def _apply_relations(
    relations: pd.DataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_assign_policy_columns(output, policy_rows)`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError("Coded relations must be a DataFrame")` under lexical guard `not isinstance(relations, pd.DataFrame) or isinstance(<br>        relations, gpd.GeoDataFrame<br>    )`.
  - `BessPlanningFeatureApplicationError(<br>            "Coded relations already contain BESS policy columns"<br>        )` under lexical guard `any(column in relations.columns for column in POLICY_COLUMNS)`.
  - `BessPlanningFeatureApplicationError(<br>            "Coded relations lack feature-policy agreement fields"<br>        )` under lexical guard `not required.issubset(relations.columns)`.
  - `BessPlanningFeatureApplicationError(<br>                f"Relation references unknown planning feature ID: {feature_id!r}"<br>            )` under lexical guard `feature is None`.
  - `BessPlanningFeatureApplicationError(<br>                    f"Relation {column} differs from referenced feature"<br>                )` under lexical guard `not _null_safe_equal(relation[column], feature[column])`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `_apply_relations`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `_apply_relations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_feature_rows_by_id` | `landscout.stages.apply_bess_planning_feature_policy._feature_rows_by_id` |
| `relations.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `features.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_equal` | `landscout.stages.apply_bess_planning_feature_policy._null_safe_equal` |
| `policy_rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_assign_policy_columns` | `landscout.stages.apply_bess_planning_feature_policy._assign_policy_columns` |

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
| In-memory mutation | `policy_rows.append({column: feature[column] for column in POLICY_COLUMNS})` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _apply_relations(
    relations: pd.DataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> pd.DataFrame:
    """Propagate feature policy to relations only through planning_feature_id."""

    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("Coded relations must be a DataFrame")
    if any(column in relations.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded relations already contain BESS policy columns"
        )
    required = {"planning_feature_id", *RELATION_FEATURE_AGREEMENT_COLUMNS}
    if not required.issubset(relations.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded relations lack feature-policy agreement fields"
        )
    features = _feature_rows_by_id(surface_features, line_features, point_features)
    policy_rows: list[dict[str, object]] = []
    for relation in relations.to_dict("records"):
        feature_id = relation["planning_feature_id"]
        feature = features.get(str(feature_id))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                f"Relation references unknown planning feature ID: {feature_id!r}"
            )
        for column in RELATION_FEATURE_AGREEMENT_COLUMNS:
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Relation {column} differs from referenced feature"
                )
        policy_rows.append({column: feature[column] for column in POLICY_COLUMNS})
    output = relations.copy(deep=True)
    return _assign_policy_columns(output, policy_rows)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_component_metadata`

**Purpose:** Implements `component metadata` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "result_hash_schema_version": result.result_hash_schema_version,<br>        "application_scope": result.application_scope,<br>        "policy_scope": result.policy_scope,<br>        "local_feature_text_interpreted": result.local_feature_text_interpreted,<br>        "local_regulation_content_interpreted": (<br>            result.local_regulation_content_interpreted<br>        ),<br>        "legal_conclusion_produced": result.legal_conclusion_produced,<br>        "parcel_status_aggregated": result.parcel_status_aggregated,<br>        "parcel_rejection_performed": result.parcel_rejection_performed,<br>        "score_calculated": result.score_calculated,<br>        "policy_profile": result.policy_profile,<br>        "policy_sha256": result.policy_sha256,<br>        "policy_result_hash_schema_version": (result.policy_result_hash_schema_version),<br>        "policy_complete_result_content_sha256": (<br>            result.policy_complete_result_content_sha256<br>        ),<br>        "cnig_profile": result.cnig_profile,<br>        "cnig_profile_sha256": result.cnig_profile_sha256,<br>        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,<br>        "cnig_complete_result_content_sha256": (<br>            result.cnig_complete_result_content_sha256<br>        ),<br>        "source_document_id": result.source_document_id,<br>        "source_archive_sha256": result.source_archive_sha256,<br>        "cnig_surface_features_content_sha256": (<br>            result.cnig_surface_features_content_sha256<br>        ),<br>        "cnig_line_features_content_sha256": result.cnig_line_features_content_sha256,<br>        "cnig_point_features_content_sha256": (<br>            result.cnig_point_features_content_sha256<br>        ),<br>        "cnig_relations_content_sha256": result.cnig_relations_content_sha256,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_component_sha256` via `_component_metadata`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_component_sha256` via `_component_metadata`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_complete_result_sha256` via `_component_metadata`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_complete_result_sha256` via `_component_metadata`

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
def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "application_scope": result.application_scope,
        "policy_scope": result.policy_scope,
        "local_feature_text_interpreted": result.local_feature_text_interpreted,
        "local_regulation_content_interpreted": (
            result.local_regulation_content_interpreted
        ),
        "legal_conclusion_produced": result.legal_conclusion_produced,
        "parcel_status_aggregated": result.parcel_status_aggregated,
        "parcel_rejection_performed": result.parcel_rejection_performed,
        "score_calculated": result.score_calculated,
        "policy_profile": result.policy_profile,
        "policy_sha256": result.policy_sha256,
        "policy_result_hash_schema_version": (result.policy_result_hash_schema_version),
        "policy_complete_result_content_sha256": (
            result.policy_complete_result_content_sha256
        ),
        "cnig_profile": result.cnig_profile,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_surface_features_content_sha256": (
            result.cnig_surface_features_content_sha256
        ),
        "cnig_line_features_content_sha256": result.cnig_line_features_content_sha256,
        "cnig_point_features_content_sha256": (
            result.cnig_point_features_content_sha256
        ),
        "cnig_relations_content_sha256": result.cnig_relations_content_sha256,
    }
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_component_sha256`

**Purpose:** Implements `component sha256` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `role` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": f"landscout.bess_planning_feature_application.{role}",<br>            **_component_metadata(result),<br>            "frame": _frame_payload(frame),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_result_with_hashes` via `_component_sha256`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_result_with_hashes` via `_component_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.apply_bess_planning_feature_policy._canonical_json_sha256` |
| `_component_metadata` | `landscout.stages.apply_bess_planning_feature_policy._component_metadata` |
| `_frame_payload` | `landscout.stages.apply_bess_planning_feature_policy._frame_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": f"landscout.bess_planning_feature_application.{role}",
            **_component_metadata(result),
            "frame": _frame_payload(frame),
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_complete_result_sha256`

**Purpose:** Implements `complete result sha256` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": "landscout.bess_planning_feature_application.result",<br>            **_component_metadata(result),<br>            "surface_features_content_sha256": (result.surface_features_content_sha256),<br>            "line_features_content_sha256": result.line_features_content_sha256,<br>            "point_features_content_sha256": result.point_features_content_sha256,<br>            "relations_content_sha256": result.relations_content_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_result_with_hashes` via `_complete_result_sha256`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_result_with_hashes` via `_complete_result_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.apply_bess_planning_feature_policy._canonical_json_sha256` |
| `_component_metadata` | `landscout.stages.apply_bess_planning_feature_policy._component_metadata` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_planning_feature_application.result",
            **_component_metadata(result),
            "surface_features_content_sha256": (result.surface_features_content_sha256),
            "line_features_content_sha256": result.line_features_content_sha256,
            "point_features_content_sha256": result.point_features_content_sha256,
            "relations_content_sha256": result.relations_content_sha256,
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_with_hashes`

**Purpose:** Implements `result with hashes` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _result_with_hashes(
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
  - `replace(<br>        components,<br>        complete_result_content_sha256=_complete_result_sha256(components),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `_result_with_hashes`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `_result_with_hashes`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_result_with_hashes`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_result_with_hashes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_component_sha256` | `landscout.stages.apply_bess_planning_feature_policy._component_sha256` |
| `_complete_result_sha256` | `landscout.stages.apply_bess_planning_feature_policy._complete_result_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_component_sha256`<br>`_complete_result_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _result_with_hashes(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
    components = replace(
        result,
        surface_features_content_sha256=_component_sha256(
            result, result.surface_features, "surface_features"
        ),
        line_features_content_sha256=_component_sha256(
            result, result.line_features, "line_features"
        ),
        point_features_content_sha256=_component_sha256(
            result, result.point_features, "point_features"
        ),
        relations_content_sha256=_component_sha256(
            result, result.relations, "relations"
        ),
    )
    return replace(
        components,
        complete_result_content_sha256=_complete_result_sha256(components),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_result`

**Purpose:** Implements `build result` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coded` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `policy` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_result_with_hashes(result)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `_build_result`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `_build_result`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_build_result`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_build_result`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_build_result`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_build_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_apply_feature_catalog` | `landscout.stages.apply_bess_planning_feature_policy._apply_feature_catalog` |
| `_apply_relations` | `landscout.stages.apply_bess_planning_feature_policy._apply_relations` |
| `BessPlanningFeatureApplicationResult` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult` |
| `_result_with_hashes` | `landscout.stages.apply_bess_planning_feature_policy._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
    surface = _apply_feature_catalog(coded.surface_features, policy)
    line = _apply_feature_catalog(coded.line_features, policy)
    point = _apply_feature_catalog(coded.point_features, policy)
    relations = _apply_relations(coded.relations, surface, line, point)
    result = BessPlanningFeatureApplicationResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        application_scope=APPLICATION_SCOPE,
        policy_scope=policy.policy_scope,
        local_feature_text_interpreted=False,
        local_regulation_content_interpreted=False,
        legal_conclusion_produced=False,
        parcel_status_aggregated=False,
        parcel_rejection_performed=False,
        score_calculated=False,
        policy_profile=policy.policy_profile,
        policy_sha256=policy.policy_sha256,
        policy_result_hash_schema_version=policy.result_hash_schema_version,
        policy_complete_result_content_sha256=policy.complete_result_content_sha256,
        cnig_profile=coded.profile,
        cnig_profile_sha256=coded.profile_sha256,
        cnig_result_hash_schema_version=coded.result_hash_schema_version,
        cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
        source_document_id=coded.source_document_id,
        source_archive_sha256=coded.source_archive_sha256,
        cnig_surface_features_content_sha256=coded.surface_features_content_sha256,
        cnig_line_features_content_sha256=coded.line_features_content_sha256,
        cnig_point_features_content_sha256=coded.point_features_content_sha256,
        cnig_relations_content_sha256=coded.relations_content_sha256,
        surface_features_content_sha256="",
        line_features_content_sha256="",
        point_features_content_sha256="",
        relations_content_sha256="",
        complete_result_content_sha256="",
        surface_features=surface,
        line_features=line,
        point_features=point,
        relations=relations,
    )
    return _result_with_hashes(result)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_relation_rows`

**Purpose:** Implements `validate relation rows` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[dict[int, str], dict[str, int]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `validate_bess_application_relation_frame(<br>            frame,<br>            label=label,<br>            policy_profile=result.policy_profile,<br>            policy_sha256=result.policy_sha256,<br>            policy_result_sha256=result.policy_complete_result_content_sha256,<br>            source_document_id=result.source_document_id,<br>            source_archive_sha256=result.source_archive_sha256,<br>            cnig_profile=result.cnig_profile,<br>            cnig_profile_sha256=result.cnig_profile_sha256,<br>        )`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(str(error))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_validate_relation_rows`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_result_envelope` via `_validate_relation_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_bess_application_relation_frame` | `landscout.common.bess_application_contract.validate_bess_application_relation_frame` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
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
def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
    try:
        return validate_bess_application_relation_frame(
            frame,
            label=label,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result_envelope`

**Purpose:** Implements `validate result envelope` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>            "result must be a BessPlanningFeatureApplicationResult"<br>        )` under lexical guard `not isinstance(result, BessPlanningFeatureApplicationResult)`.
  - `BessPlanningFeatureApplicationError("unsupported result hash schema")` under lexical guard `type(result.result_hash_schema_version) is not int<br>        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
  - `BessPlanningFeatureApplicationError("application result scope is invalid")` under lexical guard `result.application_scope != APPLICATION_SCOPE<br>        or result.policy_scope != POLICY_SCOPE`.
  - `BessPlanningFeatureApplicationError(str(error))`.
  - `BessPlanningFeatureApplicationError(<br>            "policy result hash schema must be exactly 1"<br>        )` under lexical guard `result.policy_result_hash_schema_version != 1`.
  - `BessPlanningFeatureApplicationError(<br>            "CNIG result hash schema must be exactly 5"<br>        )` under lexical guard `result.cnig_result_hash_schema_version != 5`.
  - `BessPlanningFeatureApplicationError(<br>            "application result boundary flags must all be false"<br>        )` under lexical guard `any(<br>        value is not False<br>        for value in (<br>            result.local_feature_text_interpreted,<br>            result.local_regulation_content_interpreted,<br>            result.legal_conclusion_produced,<br>            result.parcel_status_aggregated,<br>            result.parcel_rejection_performed,<br>            result.score_calculated,<br>        )<br>    )`.
  - `BessPlanningFeatureApplicationError(f"{label} must be geospatial")` under lexical guard `not isinstance(frame, gpd.GeoDataFrame)`.
  - `BessPlanningFeatureApplicationError(<br>                f"{label} policy schema is invalid"<br>            )` under lexical guard `frame.columns.duplicated().any()`.
  - `BessPlanningFeatureApplicationError(str(error))`.
  - `BessPlanningFeatureApplicationError("relations must be a DataFrame")` under lexical guard `not isinstance(result.relations, pd.DataFrame) or isinstance(<br>        result.relations, gpd.GeoDataFrame<br>    )`.
  - `BessPlanningFeatureApplicationError("relations policy schema is invalid")` under lexical guard `result.relations.columns.duplicated().any()`.
  - `BessPlanningFeatureApplicationError(<br>            "relation policy mapping differs from the feature mapping"<br>        )` under lexical guard `any(<br>        feature_mapping[0].get(priority) != status<br>        for priority, status in relation_mapping[0].items()<br>    ) or any(<br>        feature_mapping[1].get(status) != priority<br>        for status, priority in relation_mapping[1].items()<br>    )`.
  - `BessPlanningFeatureApplicationError(<br>                "Application relation references an unknown feature"<br>            )` under lexical guard `feature is None`.
  - `BessPlanningFeatureApplicationError(<br>                    f"Application relation {column} differs from its feature"<br>                )` under lexical guard `not _null_safe_equal(relation[column], feature[column])`.
  - `BessPlanningFeatureApplicationError(<br>                    "Application relation feature metric is not numeric"<br>                )` under lexical guard `kind == "POINT"`.
  - `BessPlanningFeatureApplicationError(<br>                "Application relation feature metric differs from its feature"<br>            )` under lexical guard `not metric_equal`.
  - `BessPlanningFeatureApplicationError(str(error))` under lexical guard `field.endswith("sha256")`.
  - `BessPlanningFeatureApplicationError(f"{field} is invalid")` under lexical guard `getattr(result, field) != getattr(rebuilt, field)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result_envelope` via `_validate_result_envelope`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result_envelope` via `_validate_result_envelope`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `_validate_result_envelope`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `_validate_result_envelope`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_validate_result_envelope`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_validate_result_envelope`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_validate_result_envelope`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_validate_result_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.apply_bess_planning_feature_policy._exact_string` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `validate_bess_application_feature_catalogs` | `landscout.common.bess_application_contract.validate_bess_application_feature_catalogs` |
| `result.relations.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.relations.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_relation_rows` | `landscout.stages.apply_bess_planning_feature_policy._validate_relation_rows` |
| `feature_mapping[0].get` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_mapping[0].items` | `unresolved local/third-party receiver; no ownership inferred` |
| `feature_mapping[1].get` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_mapping[1].items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_feature_rows_by_id` | `landscout.stages.apply_bess_planning_feature_policy._feature_rows_by_id` |
| `result.relations.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `feature_rows.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_equal` | `landscout.stages.apply_bess_planning_feature_policy._null_safe_equal` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `abs` | `unresolved local/third-party receiver; no ownership inferred` |
| `technical_overlay_tolerance` | `landscout.common.planning_overlay.technical_overlay_tolerance` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `field.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_string` | `landscout.stages.apply_bess_planning_feature_policy._sha256_string` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.apply_bess_planning_feature_policy._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_string`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | `technical_overlay_tolerance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
    if not isinstance(result, BessPlanningFeatureApplicationResult):
        raise BessPlanningFeatureApplicationError(
            "result must be a BessPlanningFeatureApplicationResult"
        )
    if (
        type(result.result_hash_schema_version) is not int
        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureApplicationError("unsupported result hash schema")
    if (
        result.application_scope != APPLICATION_SCOPE
        or result.policy_scope != POLICY_SCOPE
    ):
        raise BessPlanningFeatureApplicationError("application result scope is invalid")
    for exact_value, label in (
        (result.policy_profile, "policy_profile"),
        (result.cnig_profile, "cnig_profile"),
        (result.source_document_id, "source_document_id"),
    ):
        try:
            _exact_string(exact_value, label)
        except ValueError as error:
            raise BessPlanningFeatureApplicationError(str(error)) from error
    if result.policy_result_hash_schema_version != 1:
        raise BessPlanningFeatureApplicationError(
            "policy result hash schema must be exactly 1"
        )
    if result.cnig_result_hash_schema_version != 5:
        raise BessPlanningFeatureApplicationError(
            "CNIG result hash schema must be exactly 5"
        )
    if any(
        value is not False
        for value in (
            result.local_feature_text_interpreted,
            result.local_regulation_content_interpreted,
            result.legal_conclusion_produced,
            result.parcel_status_aggregated,
            result.parcel_rejection_performed,
            result.score_calculated,
        )
    ):
        raise BessPlanningFeatureApplicationError(
            "application result boundary flags must all be false"
        )
    for frame, label in (
        (result.surface_features, "surface features"),
        (result.line_features, "line features"),
        (result.point_features, "point features"),
    ):
        if not isinstance(frame, gpd.GeoDataFrame):
            raise BessPlanningFeatureApplicationError(f"{label} must be geospatial")
        if frame.columns.duplicated().any():
            raise BessPlanningFeatureApplicationError(
                f"{label} policy schema is invalid"
            )
        deterministic_frame_schema_signature(frame)
    try:
        feature_mapping = validate_bess_application_feature_catalogs(
            result.surface_features,
            result.line_features,
            result.point_features,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error
    if not isinstance(result.relations, pd.DataFrame) or isinstance(
        result.relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("relations must be a DataFrame")
    if result.relations.columns.duplicated().any():
        raise BessPlanningFeatureApplicationError("relations policy schema is invalid")
    relation_mapping = _validate_relation_rows(result.relations, "relations", result)
    if any(
        feature_mapping[0].get(priority) != status
        for priority, status in relation_mapping[0].items()
    ) or any(
        feature_mapping[1].get(status) != priority
        for status, priority in relation_mapping[1].items()
    ):
        raise BessPlanningFeatureApplicationError(
            "relation policy mapping differs from the feature mapping"
        )
    feature_rows = _feature_rows_by_id(
        result.surface_features, result.line_features, result.point_features
    )
    for relation in result.relations.to_dict("records"):
        feature = feature_rows.get(str(relation["planning_feature_id"]))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                "Application relation references an unknown feature"
            )
        for column in (*RELATION_FEATURE_AGREEMENT_COLUMNS, *POLICY_COLUMNS):
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Application relation {column} differs from its feature"
                )
        kind = relation["geometry_kind"]
        relation_metric, feature_metric = {
            "SURFACE": ("feature_area_m2", "feature_area_m2"),
            "LINE": ("source_line_length_m", "feature_length_m"),
            "POINT": ("point_member_count", "point_member_count"),
        }[kind]
        if kind == "POINT":
            metric_equal = _null_safe_equal(
                relation[relation_metric], feature[feature_metric]
            )
        else:
            actual_value = relation[relation_metric]
            expected_value = feature[feature_metric]
            if (
                isinstance(actual_value, bool)
                or not isinstance(actual_value, Real)
                or isinstance(expected_value, bool)
                or not isinstance(expected_value, Real)
            ):
                raise BessPlanningFeatureApplicationError(
                    "Application relation feature metric is not numeric"
                )
            actual = float(actual_value)
            expected = float(expected_value)
            metric_equal = abs(actual - expected) <= technical_overlay_tolerance(
                max(abs(actual), abs(expected))
            )
        if not metric_equal:
            raise BessPlanningFeatureApplicationError(
                "Application relation feature metric differs from its feature"
            )
    for field in RESULT_SCALAR_FIELDS:
        if field.endswith("sha256"):
            try:
                _sha256_string(getattr(result, field), field)
            except ValueError as error:
                raise BessPlanningFeatureApplicationError(str(error)) from error
    rebuilt = _result_with_hashes(result)
    for field in (
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt, field):
            raise BessPlanningFeatureApplicationError(f"{field} is invalid")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_bess_planning_feature_application_result_envelope`

**Purpose:** Validate one application envelope without reconstructing source inputs.

**Exact signature**

```python
def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `validate_bess_planning_feature_application_result_envelope`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::load_bess_planning_feature_parcel_aggregation_artifacts` via `validate_bess_planning_feature_application_result_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_envelope` | `landscout.stages.apply_bess_planning_feature_policy._validate_result_envelope` |

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
def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
    """Validate one application envelope without reconstructing source inputs."""

    _validate_result_envelope(result)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_coded_policy_compatibility`

**Purpose:** Implements `validate coded policy compatibility` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _validate_coded_policy_compatibility(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coded` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `policy` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                f"Policy and coded result differ for {label}"<br>            )` under lexical guard `actual != expected`.
  - `BessPlanningFeatureApplicationError(<br>            "Policy and code dictionary pair sets must be non-empty"<br>        )` under lexical guard `not coded_rows or not policy_rows`.
  - `BessPlanningFeatureApplicationError(<br>            "Policy and code dictionary pair sets differ"<br>        )` under lexical guard `set(policy_rows) != set(coded_rows)`.
  - `BessPlanningFeatureApplicationError(<br>                f"Policy official meaning differs from code dictionary for pair {key}"<br>            )` under lexical guard `any(<br>            not _null_safe_equal(actual, expected)<br>            for actual, expected in meaning_comparisons<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_validate_coded_policy_compatibility`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_validate_coded_policy_compatibility`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `coded.code_dictionary.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy.policy_table.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded_rows.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_equal` | `landscout.stages.apply_bess_planning_feature_policy._null_safe_equal` |

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
def _validate_coded_policy_compatibility(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
    comparisons = (
        (policy.source_document_id, coded.source_document_id, "document ID"),
        (policy.source_archive_sha256, coded.source_archive_sha256, "archive SHA256"),
        (policy.cnig_profile, coded.profile, "CNIG profile"),
        (
            policy.cnig_profile_schema_version,
            coded.profile_schema_version,
            "CNIG profile schema",
        ),
        (policy.cnig_profile_sha256, coded.profile_sha256, "CNIG profile SHA256"),
        (
            policy.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "CNIG result hash schema",
        ),
        (
            policy.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "CNIG complete result SHA256",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Policy and coded result differ for {label}"
            )
    coded_rows = {
        (row["feature_family"], row["type_code"], row["subtype_code"]): row
        for row in coded.code_dictionary.to_dict("records")
    }
    policy_rows = {
        (row["feature_family"], row["type_code"], row["subtype_code"]): row
        for row in policy.policy_table.to_dict("records")
    }
    if not coded_rows or not policy_rows:
        raise BessPlanningFeatureApplicationError(
            "Policy and code dictionary pair sets must be non-empty"
        )
    if set(policy_rows) != set(coded_rows):
        raise BessPlanningFeatureApplicationError(
            "Policy and code dictionary pair sets differ"
        )
    for key, coded_row in coded_rows.items():
        policy_row = policy_rows[key]
        meaning_comparisons = (
            (policy_row["official_label"], coded_row["official_label"]),
            (
                policy_row["official_legal_reference"],
                coded_row["legal_reference"],
            ),
            (
                policy_row["official_regulation_reference"],
                coded_row["regulation_or_annex_reference"],
            ),
        )
        if any(
            not _null_safe_equal(actual, expected)
            for actual, expected in meaning_comparisons
        ):
            raise BessPlanningFeatureApplicationError(
                f"Policy official meaning differs from code dictionary for pair {key}"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_source_locks`

**Purpose:** Implements `validate source locks` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult
    | BessPlanningFeatureApplicationArtifactManifest,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult \| BessPlanningFeatureApplicationArtifactManifest` | `required` |
| `coded` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `policy` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                f"Application source lock differs for {label}"<br>            )` under lexical guard `actual != expected`.
  - `BessPlanningFeatureApplicationError(<br>                f"Application source lock differs for {label}"<br>            )` under lexical guard `actual != expected`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_validate_source_locks`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_validate_source_locks`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_validate_source_locks`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_validate_source_locks`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |

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
def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult
    | BessPlanningFeatureApplicationArtifactManifest,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
    comparisons = (
        (result.policy_profile, policy.policy_profile, "policy profile"),
        (result.policy_sha256, policy.policy_sha256, "policy SHA256"),
        (
            result.policy_result_hash_schema_version,
            policy.result_hash_schema_version,
            "policy result hash schema",
        ),
        (
            result.policy_complete_result_content_sha256,
            policy.complete_result_content_sha256,
            "policy result SHA256",
        ),
        (result.cnig_profile, coded.profile, "CNIG profile"),
        (result.cnig_profile_sha256, coded.profile_sha256, "CNIG profile SHA256"),
        (
            result.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "CNIG result hash schema",
        ),
        (
            result.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "CNIG result SHA256",
        ),
        (result.source_document_id, coded.source_document_id, "document ID"),
        (result.source_archive_sha256, coded.source_archive_sha256, "archive SHA256"),
        (
            result.cnig_surface_features_content_sha256,
            coded.surface_features_content_sha256,
            "coded surface SHA256",
        ),
        (
            result.cnig_line_features_content_sha256,
            coded.line_features_content_sha256,
            "coded line SHA256",
        ),
        (
            result.cnig_point_features_content_sha256,
            coded.point_features_content_sha256,
            "coded point SHA256",
        ),
        (
            result.cnig_relations_content_sha256,
            coded.relations_content_sha256,
            "coded relations SHA256",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Application source lock differs for {label}"
            )

    policy_coded_comparisons = (
        (policy.source_document_id, coded.source_document_id, "policy document ID"),
        (
            policy.source_archive_sha256,
            coded.source_archive_sha256,
            "policy archive SHA256",
        ),
        (policy.cnig_profile, coded.profile, "policy CNIG profile"),
        (
            policy.cnig_profile_schema_version,
            coded.profile_schema_version,
            "policy CNIG profile schema",
        ),
        (
            policy.cnig_profile_sha256,
            coded.profile_sha256,
            "policy CNIG profile SHA256",
        ),
        (
            policy.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "policy CNIG result hash schema",
        ),
        (
            policy.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "policy CNIG result SHA256",
        ),
    )
    for actual, expected, label in policy_coded_comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Application source lock differs for {label}"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_policy_source`

**Purpose:** Implements `validate policy source` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _validate_policy_source(
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

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>            "Source-complete BESS planning-feature policy validation failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `_validate_policy_source`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `_validate_policy_source`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_validate_policy_source`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_validate_policy_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_bess_planning_feature_policy_result` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |

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
def _validate_policy_source(
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
) -> None:
    try:
        validate_bess_planning_feature_policy_result(
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
        )
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "Source-complete BESS planning-feature policy validation failed"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `apply_bess_planning_feature_policy`

**Purpose:** Validate once, then propagate exact compiled policy to features and relations.

**Exact signature**

```python
def apply_bess_planning_feature_policy(
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
) -> BessPlanningFeatureApplicationResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeatureApplicationResult`.

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

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `re-raise`.
  - `BessPlanningFeatureApplicationError(<br>            "BESS planning-feature policy application failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- import: `tests.unit.test_apply_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::_application_fixture` via `apply_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::_application_fixture` via `apply_bess_planning_feature_policy`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_and_relation_inputs_are_preserved_and_not_mutated` via `apply_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_feature_and_relation_inputs_are_preserved_and_not_mutated` via `apply_bess_planning_feature_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_policy_source` | `landscout.stages.apply_bess_planning_feature_policy._validate_policy_source` |
| `_build_result` | `landscout.stages.apply_bess_planning_feature_policy._build_result` |
| `_validate_result_envelope` | `landscout.stages.apply_bess_planning_feature_policy._validate_result_envelope` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |

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
def apply_bess_planning_feature_policy(
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
) -> BessPlanningFeatureApplicationResult:
    """Validate once, then propagate exact compiled policy to features and relations."""

    try:
        _validate_policy_source(
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
        )
        result = _build_result(coded_result, policy_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature policy application failed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compare_frame`

**Purpose:** Implements `compare frame` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

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
  - `BessPlanningFeatureApplicationError(<br>            f"Application {label} differs from rebuilt result"<br>        )` under lexical guard `_frame_payload(actual) != _frame_payload(expected)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_compare_frame`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `_compare_frame`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_compare_frame`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_compare_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_frame_payload` | `landscout.stages.apply_bess_planning_feature_policy._frame_payload` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |

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
        raise BessPlanningFeatureApplicationError(
            f"Application {label} differs from rebuilt result"
        )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_bess_planning_feature_application_result`

**Purpose:** Independently rebuild exact policy propagation from every source input.

**Exact signature**

```python
def validate_bess_planning_feature_application_result(
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
    result: BessPlanningFeatureApplicationResult,
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
| `result` | positional-or-keyword | `BessPlanningFeatureApplicationResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                    f"Application {field} differs from rebuilt result"<br>                )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `re-raise`.
  - `BessPlanningFeatureApplicationError(<br>            "BESS planning-feature application result validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- direct call: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `validate_bess_planning_feature_application_result`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `validate_bess_planning_feature_application_result`
- import: `tests.unit.test_apply_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `validate_bess_planning_feature_application_result`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `validate_bess_planning_feature_application_result`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `validate_bess_planning_feature_application_result`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_valid_four_file_manifest_and_verified_byte_readback` via `validate_bess_planning_feature_application_result`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `validate_bess_planning_feature_application_result`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_lineage_defect_fast_fails_before_policy_source_validation` via `validate_bess_planning_feature_application_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_envelope` | `landscout.stages.apply_bess_planning_feature_policy._validate_result_envelope` |
| `_validate_source_locks` | `landscout.stages.apply_bess_planning_feature_policy._validate_source_locks` |
| `_validate_policy_source` | `landscout.stages.apply_bess_planning_feature_policy._validate_policy_source` |
| `_build_result` | `landscout.stages.apply_bess_planning_feature_policy._build_result` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `_compare_frame` | `landscout.stages.apply_bess_planning_feature_policy._compare_frame` |

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
def validate_bess_planning_feature_application_result(
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
    result: BessPlanningFeatureApplicationResult,
) -> None:
    """Independently rebuild exact policy propagation from every source input."""

    try:
        _validate_result_envelope(result)
        _validate_source_locks(result, coded_result, policy_result)
        _validate_policy_source(
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
        )
        expected = _build_result(coded_result, policy_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureApplicationError(
                    f"Application {field} differs from rebuilt result"
                )
        for actual, rebuilt, label in (
            (result.surface_features, expected.surface_features, "surface features"),
            (result.line_features, expected.line_features, "line features"),
            (result.point_features, expected.point_features, "point features"),
            (result.relations, expected.relations, "relations"),
        ):
            _compare_frame(actual, rebuilt, label)
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature application result validation failed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_read_verified_artifact`

**Purpose:** Implements `read verified artifact` within the file role: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

**Exact signature**

```python
def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `record` | positional-or-keyword | `BessPlanningFeatureApplicationArtifactRecord` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>            f"Artifact {record.artifact_role} filename differs"<br>        )` under lexical guard `path.name != record.filename`.
  - `BessPlanningFeatureApplicationError(<br>            f"Artifact {record.artifact_role} byte size differs"<br>        )` under lexical guard `len(payload) != record.size_bytes`.
  - `BessPlanningFeatureApplicationError(<br>            f"Artifact {record.artifact_role} SHA256 differs"<br>        )` under lexical guard `sha256(payload).hexdigest() != record.sha256`.
  - `BessPlanningFeatureApplicationError(<br>            f"Artifact {record.artifact_role} row count differs"<br>        )` under lexical guard `len(frame) != record.row_count`.
  - `BessPlanningFeatureApplicationError(<br>            f"Artifact {record.artifact_role} frame schema differs"<br>        )` under lexical guard `signature != record.frame_schema_signature`.
  - `BessPlanningFeatureApplicationError(<br>                f"Artifact {record.artifact_role} geospatial contract differs"<br>            )` under lexical guard `record.geospatial`.
  - `BessPlanningFeatureApplicationError(<br>                f"Artifact {record.artifact_role} CRS differs"<br>            )` under lexical guard `record.geospatial`.
  - `BessPlanningFeatureApplicationError(<br>            "Relations artifact unexpectedly loaded as geospatial"<br>        )` under lexical guard `record.geospatial`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_read_verified_artifact`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_read_verified_artifact`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `BytesIO` | `io.BytesIO` |
| `gpd.read_parquet` | `geopandas.read_parquet` |
| `pd.read_parquet` | `pandas.read_parquet` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input(frame.crs).to_json_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.read_bytes`<br>`gpd.read_parquet`<br>`pd.read_parquet` |
| Filesystem/archive write or publication | `CRS.from_user_input(frame.crs).to_json_dict` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
    if path.name != record.filename:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} filename differs"
        )
    payload = path.read_bytes()
    if len(payload) != record.size_bytes:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} byte size differs"
        )
    if sha256(payload).hexdigest() != record.sha256:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} SHA256 differs"
        )
    buffer = BytesIO(payload)
    frame: pd.DataFrame
    if record.geospatial:
        frame = gpd.read_parquet(buffer)
    else:
        frame = pd.read_parquet(buffer)
    if len(frame) != record.row_count:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} row count differs"
        )
    signature = deterministic_frame_schema_signature(frame)
    if signature != record.frame_schema_signature:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} frame schema differs"
        )
    if record.geospatial:
        if not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} geospatial contract differs"
            )
        if CRS.from_user_input(frame.crs).to_json_dict() != record.crs:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Relations artifact unexpectedly loaded as geospatial"
        )
    return frame
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `load_bess_planning_feature_application_artifacts`

**Purpose:** Load byte-sealed outputs and bind them to exact validated upstream results.

**Exact signature**

```python
def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_result: BessPlanningFeaturePolicyResult,
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
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `policy_result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessPlanningFeatureApplicationError(<br>                    f"Application artifact scalar {field} differs from upstream rebuild"<br>                )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `re-raise`.
  - `BessPlanningFeatureApplicationError(<br>            f"BESS planning-feature application artifacts are invalid: {error}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`
- import: `tests.unit.test_apply_bess_planning_feature_policy::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    load_bess_planning_feature_application_artifacts as _load_application_artifacts,
)`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_load_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `_load_application_artifacts`
- direct call: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_load_application_artifacts`
- value/type reference: `tests.unit.test_apply_bess_planning_feature_policy::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `_load_application_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_feature_code_result_envelope` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result_envelope` |
| `validate_bess_planning_feature_policy_result_envelope` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result_envelope` |
| `_validate_coded_policy_compatibility` | `landscout.stages.apply_bess_planning_feature_policy._validate_coded_policy_compatibility` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `Path(manifest_path).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `BessPlanningFeatureApplicationArtifactManifest.model_validate` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.model_validate` |
| `_validate_source_locks` | `landscout.stages.apply_bess_planning_feature_policy._validate_source_locks` |
| `_read_verified_artifact` | `landscout.stages.apply_bess_planning_feature_policy._read_verified_artifact` |
| `BessPlanningFeatureApplicationResult` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_result_envelope` | `landscout.stages.apply_bess_planning_feature_policy._validate_result_envelope` |
| `_build_result` | `landscout.stages.apply_bess_planning_feature_policy._build_result` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `_compare_frame` | `landscout.stages.apply_bess_planning_feature_policy._compare_frame` |

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
def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
    """Load byte-sealed outputs and bind them to exact validated upstream results."""

    try:
        validate_planning_feature_code_result_envelope(coded_result)
        validate_bess_planning_feature_policy_result_envelope(policy_result)
        _validate_coded_policy_compatibility(coded_result, policy_result)
        payload = loads_strict_json_object(Path(manifest_path).read_bytes())
        manifest = BessPlanningFeatureApplicationArtifactManifest.model_validate(
            payload
        )
        _validate_source_locks(manifest, coded_result, policy_result)
        paths = {
            "SURFACE_FEATURES": Path(surface_features_path),
            "LINE_FEATURES": Path(line_features_path),
            "POINT_FEATURES": Path(point_features_path),
            "RELATIONS": Path(relations_path),
        }
        records = {record.artifact_role: record for record in manifest.artifacts}
        loaded = {
            role: _read_verified_artifact(paths[role], records[role])
            for role in ARTIFACT_ROLES
        }
        result = BessPlanningFeatureApplicationResult(
            **{field: getattr(manifest, field) for field in RESULT_SCALAR_FIELDS},
            surface_features=loaded["SURFACE_FEATURES"],
            line_features=loaded["LINE_FEATURES"],
            point_features=loaded["POINT_FEATURES"],
            relations=loaded["RELATIONS"],
        )
        _validate_result_envelope(result)
        expected = _build_result(coded_result, policy_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureApplicationError(
                    f"Application artifact scalar {field} differs from upstream rebuild"
                )
        for field in RESULT_FRAME_FIELDS:
            _compare_frame(
                getattr(result, field),
                getattr(expected, field),
                f"artifact {field}",
            )
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"BESS planning-feature application artifacts are invalid: {error}"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `RESULT_HASH_SCHEMA_VERSION`, `ARTIFACT_MANIFEST_SCHEMA_VERSION`, `RELATION_FEATURE_AGREEMENT_COLUMNS`, `RESULT_FRAME_FIELDS`, `RESULT_SCALAR_FIELDS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `BessPlanningFeatureApplicationArtifactManifest` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest` |
| `BessPlanningFeatureApplicationError` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError` |
| `BessPlanningFeatureApplicationResult` | `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult` |
| `apply_bess_planning_feature_policy` | `landscout.stages.apply_bess_planning_feature_policy.apply_bess_planning_feature_policy` |
| `load_bess_planning_feature_application_artifacts` | `landscout.stages.apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts` |
| `validate_bess_planning_feature_application_result` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result` |
| `validate_bess_planning_feature_application_result_envelope` | `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result_envelope` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Apply a validated BESS CNIG policy exactly to coded features and relations."""

from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from io import BytesIO
from numbers import Integral, Real
from pathlib import Path
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
    model_validator,
)
from pyproj import CRS
from shapely import get_coordinate_dimension, to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.bess_application_contract import (
    APPLICATION_SCOPE,
    FLAG_COLUMNS,
    POLICY_COLUMNS,
    POLICY_SCOPE,
    STRING_POLICY_COLUMNS,
    ApplicationStatus,
    validate_bess_application_feature_catalogs,
    validate_bess_application_relation_frame,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.planning_overlay import technical_overlay_tolerance
from landscout.common.strict_json import loads_strict_json_object
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)

__all__ = [
    "BessPlanningFeatureApplicationArtifactManifest",
    "BessPlanningFeatureApplicationError",
    "BessPlanningFeatureApplicationResult",
    "apply_bess_planning_feature_policy",
    "load_bess_planning_feature_application_artifacts",
    "validate_bess_planning_feature_application_result",
    "validate_bess_planning_feature_application_result_envelope",
]

RESULT_HASH_SCHEMA_VERSION = 2
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"

ArtifactRole = Literal[
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
]

ARTIFACT_ROLES: tuple[ArtifactRole, ...] = (
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
)
RELATION_FEATURE_AGREEMENT_COLUMNS = (
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
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
CODE_PATTERN = re.compile(r"[0-9]{2}")


class BessPlanningFeatureApplicationError(ValueError):
    """Raised when exact feature-policy propagation cannot be proven."""


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


class BessPlanningFeatureApplicationArtifactRecord(_StrictModel):
    """One physical output record within the application manifest."""

    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: dict[StrictStr, object]
    geospatial: StrictBool
    crs: dict[StrictStr, object] | None

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        signature_geometry = self.frame_schema_signature.get("geometry_column")
        if expected_geospatial:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        return self


@dataclass(frozen=True)
class BessPlanningFeatureApplicationResult:
    """Immutable exact policy propagation over coded features and relations."""

    result_hash_schema_version: int
    application_scope: str
    policy_scope: str
    local_feature_text_interpreted: bool
    local_regulation_content_interpreted: bool
    legal_conclusion_produced: bool
    parcel_status_aggregated: bool
    parcel_rejection_performed: bool
    score_calculated: bool
    policy_profile: str
    policy_sha256: str
    policy_result_hash_schema_version: int
    policy_complete_result_content_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_surface_features_content_sha256: str
    cnig_line_features_content_sha256: str
    cnig_point_features_content_sha256: str
    cnig_relations_content_sha256: str
    surface_features_content_sha256: str
    line_features_content_sha256: str
    point_features_content_sha256: str
    relations_content_sha256: str
    complete_result_content_sha256: str
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame


RESULT_FRAME_FIELDS = (
    "surface_features",
    "line_features",
    "point_features",
    "relations",
)
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureApplicationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)


class BessPlanningFeatureApplicationArtifactManifest(_StrictModel):
    """Strict four-file physical artifact envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"]
    result_hash_schema_version: StrictInt
    application_scope: Literal["FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"]
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    parcel_status_aggregated: StrictBool
    parcel_rejection_performed: StrictBool
    score_calculated: StrictBool
    policy_profile: StrictStr
    policy_sha256: StrictStr
    policy_result_hash_schema_version: StrictInt
    policy_complete_result_content_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_surface_features_content_sha256: StrictStr
    cnig_line_features_content_sha256: StrictStr
    cnig_point_features_content_sha256: StrictStr
    cnig_relations_content_sha256: StrictStr
    surface_features_content_sha256: StrictStr
    line_features_content_sha256: StrictStr
    point_features_content_sha256: StrictStr
    relations_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    artifacts: tuple[BessPlanningFeatureApplicationArtifactRecord, ...]

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application artifact manifest schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application result hash schema")
        if any(
            value is not False
            for value in (
                self.local_feature_text_interpreted,
                self.local_regulation_content_interpreted,
                self.legal_conclusion_produced,
                self.parcel_status_aggregated,
                self.parcel_rejection_performed,
                self.score_calculated,
            )
        ):
            raise ValueError("application boundary flags must all be false")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.cnig_profile, "cnig_profile"),
            (self.source_document_id, "source_document_id"),
        ):
            _exact_string(exact_value, label)
        if self.policy_result_hash_schema_version != 1:
            raise ValueError("policy result hash schema must be exactly 1")
        if self.cnig_result_hash_schema_version != 5:
            raise ValueError("CNIG result hash schema must be exactly 5")
        for field in RESULT_SCALAR_FIELDS:
            if field.endswith("sha256"):
                _sha256_string(getattr(self, field), field)
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError(
                "application artifact roles are missing, extra, or unordered"
            )
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("application artifact filenames contain a duplicate")
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
        coordinate_dimension = int(get_coordinate_dimension(value))
        if coordinate_dimension != 2:
            raise BessPlanningFeatureApplicationError(
                "Application geometry coordinate dimension must be exactly 2D"
            )
        return {
            "coordinate_dimension": coordinate_dimension,
            "wkb_hex": to_wkb(
                value,
                hex=True,
                output_dimension=2,
                byte_order=1,
                include_srid=False,
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
            raise BessPlanningFeatureApplicationError(
                "Application integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeatureApplicationError(
        f"Unsupported application integrity value {type(value).__name__}"
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


def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    """Require supplied application geometry to remain canonical two-dimensional."""

    try:
        geometry_name = frame.geometry.name
        if geometry_name not in frame.columns:
            raise BessPlanningFeatureApplicationError(
                f"{label} active geometry column is missing"
            )
        for position, geometry in enumerate(frame.geometry.array):
            if not isinstance(geometry, BaseGeometry):
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} is missing or invalid"
                )
            if int(get_coordinate_dimension(geometry)) != 2:
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} must be canonical 2D"
                )
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"{label} geometry contract is invalid"
        ) from error


def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(
            "Application integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _null_safe_equal(left: object, right: object) -> bool:
    left = _null_value(left)
    right = _null_value(right)
    if left is None or right is None:
        return left is None and right is None
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False


def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    lookup: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in policy.policy_table.to_dict("records"):
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in lookup:
            raise BessPlanningFeatureApplicationError(
                "Compiled policy contains a duplicate exact code pair"
            )
        lookup[key] = row
    return lookup


def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
    return {
        "bess_cnig_policy_application_status": application_status,
        "bess_cnig_precheck_status": None if row is None else row["precheck_status"],
        "bess_cnig_precheck_confidence": None if row is None else row["confidence"],
        "bess_cnig_status_priority": None if row is None else row["status_priority"],
        "bess_cnig_rationale": None if row is None else row["rationale"],
        "bess_cnig_required_human_action": (
            None if row is None else row["required_human_action"]
        ),
        "bess_cnig_limitations": None if row is None else row["limitations"],
        "bess_cnig_application_scope": APPLICATION_SCOPE,
        "bess_cnig_policy_scope": policy.policy_scope,
        "bess_cnig_local_feature_text_interpreted": False,
        "bess_cnig_local_regulation_content_interpreted": False,
        "bess_cnig_legal_conclusion_produced": False,
        "bess_cnig_parcel_status_aggregated": False,
        "bess_cnig_parcel_rejection_performed": False,
        "bess_cnig_score_calculated": False,
        "bess_cnig_policy_profile": policy.policy_profile,
        "bess_cnig_policy_sha256": policy.policy_sha256,
        "bess_cnig_policy_result_sha256": policy.complete_result_content_sha256,
    }


def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
    values: dict[str, object] = {}
    for column in STRING_POLICY_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="str")
    values["bess_cnig_status_priority"] = pd.array(
        [row["bess_cnig_status_priority"] for row in rows], dtype="Int64"
    )
    for column in FLAG_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="bool")
    for column in POLICY_COLUMNS:
        frame[column] = values[column]
    return frame


def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
    """Apply exact family/type/subtype policy to one already-coded catalog."""

    if not isinstance(catalog, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog is not geospatial"
        )
    if any(column in catalog.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog already contains BESS policy columns"
        )
    required = {
        "planning_feature_id",
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        "official_code_status",
    }
    if not required.issubset(catalog.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog lacks exact policy lookup fields"
        )
    lookup = _policy_lookup(policy)
    policy_rows: list[dict[str, object]] = []
    for row in catalog.to_dict("records"):
        type_code = row["type_code_raw"]
        subtype_code = row["subtype_code_raw"]
        if not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None:
            raise BessPlanningFeatureApplicationError(
                "Feature type code is not an exact two-character string"
            )
        if (
            not isinstance(subtype_code, str)
            or CODE_PATTERN.fullmatch(subtype_code) is None
        ):
            raise BessPlanningFeatureApplicationError(
                "Feature subtype code is not an exact two-character string"
            )
        key = (str(row["feature_family"]), type_code, subtype_code)
        official_status = row["official_code_status"]
        policy_row = lookup.get(key)
        if official_status == "RESOLVED_OFFICIAL":
            if policy_row is None:
                raise BessPlanningFeatureApplicationError(
                    f"Resolved official feature has no exact policy row: {key}"
                )
            application_status: ApplicationStatus = "APPLIED_EXACT_POLICY"
        elif official_status == "UNKNOWN_CODE_PAIR":
            if policy_row is not None:
                raise BessPlanningFeatureApplicationError(
                    f"Unknown official feature unexpectedly matches policy row: {key}"
                )
            application_status = "UNRESOLVED_CODE_PAIR"
        else:
            raise BessPlanningFeatureApplicationError(
                "Feature official-code status is invalid"
            )
        policy_rows.append(_policy_values(policy_row, application_status, policy))
    output = catalog.copy(deep=True)
    _assign_policy_columns(output, policy_rows)
    applied = gpd.GeoDataFrame(output, geometry=catalog.geometry.name, crs=catalog.crs)
    _validate_application_geometry(applied, "applied feature catalog")
    return applied


def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
    indexed: dict[str, dict[str, object]] = {}
    for catalog in catalogs:
        for row in catalog.to_dict("records"):
            feature_id = row["planning_feature_id"]
            if not isinstance(feature_id, str) or not feature_id:
                raise BessPlanningFeatureApplicationError(
                    "Enriched feature ID must be an exact string"
                )
            if feature_id in indexed:
                raise BessPlanningFeatureApplicationError(
                    "Enriched planning feature ID is not globally unique"
                )
            indexed[feature_id] = row
    return indexed


def _apply_relations(
    relations: pd.DataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> pd.DataFrame:
    """Propagate feature policy to relations only through planning_feature_id."""

    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("Coded relations must be a DataFrame")
    if any(column in relations.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded relations already contain BESS policy columns"
        )
    required = {"planning_feature_id", *RELATION_FEATURE_AGREEMENT_COLUMNS}
    if not required.issubset(relations.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded relations lack feature-policy agreement fields"
        )
    features = _feature_rows_by_id(surface_features, line_features, point_features)
    policy_rows: list[dict[str, object]] = []
    for relation in relations.to_dict("records"):
        feature_id = relation["planning_feature_id"]
        feature = features.get(str(feature_id))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                f"Relation references unknown planning feature ID: {feature_id!r}"
            )
        for column in RELATION_FEATURE_AGREEMENT_COLUMNS:
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Relation {column} differs from referenced feature"
                )
        policy_rows.append({column: feature[column] for column in POLICY_COLUMNS})
    output = relations.copy(deep=True)
    return _assign_policy_columns(output, policy_rows)


def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "application_scope": result.application_scope,
        "policy_scope": result.policy_scope,
        "local_feature_text_interpreted": result.local_feature_text_interpreted,
        "local_regulation_content_interpreted": (
            result.local_regulation_content_interpreted
        ),
        "legal_conclusion_produced": result.legal_conclusion_produced,
        "parcel_status_aggregated": result.parcel_status_aggregated,
        "parcel_rejection_performed": result.parcel_rejection_performed,
        "score_calculated": result.score_calculated,
        "policy_profile": result.policy_profile,
        "policy_sha256": result.policy_sha256,
        "policy_result_hash_schema_version": (result.policy_result_hash_schema_version),
        "policy_complete_result_content_sha256": (
            result.policy_complete_result_content_sha256
        ),
        "cnig_profile": result.cnig_profile,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_surface_features_content_sha256": (
            result.cnig_surface_features_content_sha256
        ),
        "cnig_line_features_content_sha256": result.cnig_line_features_content_sha256,
        "cnig_point_features_content_sha256": (
            result.cnig_point_features_content_sha256
        ),
        "cnig_relations_content_sha256": result.cnig_relations_content_sha256,
    }


def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": f"landscout.bess_planning_feature_application.{role}",
            **_component_metadata(result),
            "frame": _frame_payload(frame),
        }
    )


def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_planning_feature_application.result",
            **_component_metadata(result),
            "surface_features_content_sha256": (result.surface_features_content_sha256),
            "line_features_content_sha256": result.line_features_content_sha256,
            "point_features_content_sha256": result.point_features_content_sha256,
            "relations_content_sha256": result.relations_content_sha256,
        }
    )


def _result_with_hashes(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
    components = replace(
        result,
        surface_features_content_sha256=_component_sha256(
            result, result.surface_features, "surface_features"
        ),
        line_features_content_sha256=_component_sha256(
            result, result.line_features, "line_features"
        ),
        point_features_content_sha256=_component_sha256(
            result, result.point_features, "point_features"
        ),
        relations_content_sha256=_component_sha256(
            result, result.relations, "relations"
        ),
    )
    return replace(
        components,
        complete_result_content_sha256=_complete_result_sha256(components),
    )


def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
    surface = _apply_feature_catalog(coded.surface_features, policy)
    line = _apply_feature_catalog(coded.line_features, policy)
    point = _apply_feature_catalog(coded.point_features, policy)
    relations = _apply_relations(coded.relations, surface, line, point)
    result = BessPlanningFeatureApplicationResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        application_scope=APPLICATION_SCOPE,
        policy_scope=policy.policy_scope,
        local_feature_text_interpreted=False,
        local_regulation_content_interpreted=False,
        legal_conclusion_produced=False,
        parcel_status_aggregated=False,
        parcel_rejection_performed=False,
        score_calculated=False,
        policy_profile=policy.policy_profile,
        policy_sha256=policy.policy_sha256,
        policy_result_hash_schema_version=policy.result_hash_schema_version,
        policy_complete_result_content_sha256=policy.complete_result_content_sha256,
        cnig_profile=coded.profile,
        cnig_profile_sha256=coded.profile_sha256,
        cnig_result_hash_schema_version=coded.result_hash_schema_version,
        cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
        source_document_id=coded.source_document_id,
        source_archive_sha256=coded.source_archive_sha256,
        cnig_surface_features_content_sha256=coded.surface_features_content_sha256,
        cnig_line_features_content_sha256=coded.line_features_content_sha256,
        cnig_point_features_content_sha256=coded.point_features_content_sha256,
        cnig_relations_content_sha256=coded.relations_content_sha256,
        surface_features_content_sha256="",
        line_features_content_sha256="",
        point_features_content_sha256="",
        relations_content_sha256="",
        complete_result_content_sha256="",
        surface_features=surface,
        line_features=line,
        point_features=point,
        relations=relations,
    )
    return _result_with_hashes(result)


def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
    try:
        return validate_bess_application_relation_frame(
            frame,
            label=label,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error


def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
    if not isinstance(result, BessPlanningFeatureApplicationResult):
        raise BessPlanningFeatureApplicationError(
            "result must be a BessPlanningFeatureApplicationResult"
        )
    if (
        type(result.result_hash_schema_version) is not int
        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureApplicationError("unsupported result hash schema")
    if (
        result.application_scope != APPLICATION_SCOPE
        or result.policy_scope != POLICY_SCOPE
    ):
        raise BessPlanningFeatureApplicationError("application result scope is invalid")
    for exact_value, label in (
        (result.policy_profile, "policy_profile"),
        (result.cnig_profile, "cnig_profile"),
        (result.source_document_id, "source_document_id"),
    ):
        try:
            _exact_string(exact_value, label)
        except ValueError as error:
            raise BessPlanningFeatureApplicationError(str(error)) from error
    if result.policy_result_hash_schema_version != 1:
        raise BessPlanningFeatureApplicationError(
            "policy result hash schema must be exactly 1"
        )
    if result.cnig_result_hash_schema_version != 5:
        raise BessPlanningFeatureApplicationError(
            "CNIG result hash schema must be exactly 5"
        )
    if any(
        value is not False
        for value in (
            result.local_feature_text_interpreted,
            result.local_regulation_content_interpreted,
            result.legal_conclusion_produced,
            result.parcel_status_aggregated,
            result.parcel_rejection_performed,
            result.score_calculated,
        )
    ):
        raise BessPlanningFeatureApplicationError(
            "application result boundary flags must all be false"
        )
    for frame, label in (
        (result.surface_features, "surface features"),
        (result.line_features, "line features"),
        (result.point_features, "point features"),
    ):
        if not isinstance(frame, gpd.GeoDataFrame):
            raise BessPlanningFeatureApplicationError(f"{label} must be geospatial")
        if frame.columns.duplicated().any():
            raise BessPlanningFeatureApplicationError(
                f"{label} policy schema is invalid"
            )
        deterministic_frame_schema_signature(frame)
    try:
        feature_mapping = validate_bess_application_feature_catalogs(
            result.surface_features,
            result.line_features,
            result.point_features,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error
    if not isinstance(result.relations, pd.DataFrame) or isinstance(
        result.relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("relations must be a DataFrame")
    if result.relations.columns.duplicated().any():
        raise BessPlanningFeatureApplicationError("relations policy schema is invalid")
    relation_mapping = _validate_relation_rows(result.relations, "relations", result)
    if any(
        feature_mapping[0].get(priority) != status
        for priority, status in relation_mapping[0].items()
    ) or any(
        feature_mapping[1].get(status) != priority
        for status, priority in relation_mapping[1].items()
    ):
        raise BessPlanningFeatureApplicationError(
            "relation policy mapping differs from the feature mapping"
        )
    feature_rows = _feature_rows_by_id(
        result.surface_features, result.line_features, result.point_features
    )
    for relation in result.relations.to_dict("records"):
        feature = feature_rows.get(str(relation["planning_feature_id"]))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                "Application relation references an unknown feature"
            )
        for column in (*RELATION_FEATURE_AGREEMENT_COLUMNS, *POLICY_COLUMNS):
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Application relation {column} differs from its feature"
                )
        kind = relation["geometry_kind"]
        relation_metric, feature_metric = {
            "SURFACE": ("feature_area_m2", "feature_area_m2"),
            "LINE": ("source_line_length_m", "feature_length_m"),
            "POINT": ("point_member_count", "point_member_count"),
        }[kind]
        if kind == "POINT":
            metric_equal = _null_safe_equal(
                relation[relation_metric], feature[feature_metric]
            )
        else:
            actual_value = relation[relation_metric]
            expected_value = feature[feature_metric]
            if (
                isinstance(actual_value, bool)
                or not isinstance(actual_value, Real)
                or isinstance(expected_value, bool)
                or not isinstance(expected_value, Real)
            ):
                raise BessPlanningFeatureApplicationError(
                    "Application relation feature metric is not numeric"
                )
            actual = float(actual_value)
            expected = float(expected_value)
            metric_equal = abs(actual - expected) <= technical_overlay_tolerance(
                max(abs(actual), abs(expected))
            )
        if not metric_equal:
            raise BessPlanningFeatureApplicationError(
                "Application relation feature metric differs from its feature"
            )
    for field in RESULT_SCALAR_FIELDS:
        if field.endswith("sha256"):
            try:
                _sha256_string(getattr(result, field), field)
            except ValueError as error:
                raise BessPlanningFeatureApplicationError(str(error)) from error
    rebuilt = _result_with_hashes(result)
    for field in (
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt, field):
            raise BessPlanningFeatureApplicationError(f"{field} is invalid")


def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
    """Validate one application envelope without reconstructing source inputs."""

    _validate_result_envelope(result)


def _validate_coded_policy_compatibility(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
    comparisons = (
        (policy.source_document_id, coded.source_document_id, "document ID"),
        (policy.source_archive_sha256, coded.source_archive_sha256, "archive SHA256"),
        (policy.cnig_profile, coded.profile, "CNIG profile"),
        (
            policy.cnig_profile_schema_version,
            coded.profile_schema_version,
            "CNIG profile schema",
        ),
        (policy.cnig_profile_sha256, coded.profile_sha256, "CNIG profile SHA256"),
        (
            policy.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "CNIG result hash schema",
        ),
        (
            policy.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "CNIG complete result SHA256",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Policy and coded result differ for {label}"
            )
    coded_rows = {
        (row["feature_family"], row["type_code"], row["subtype_code"]): row
        for row in coded.code_dictionary.to_dict("records")
    }
    policy_rows = {
        (row["feature_family"], row["type_code"], row["subtype_code"]): row
        for row in policy.policy_table.to_dict("records")
    }
    if not coded_rows or not policy_rows:
        raise BessPlanningFeatureApplicationError(
            "Policy and code dictionary pair sets must be non-empty"
        )
    if set(policy_rows) != set(coded_rows):
        raise BessPlanningFeatureApplicationError(
            "Policy and code dictionary pair sets differ"
        )
    for key, coded_row in coded_rows.items():
        policy_row = policy_rows[key]
        meaning_comparisons = (
            (policy_row["official_label"], coded_row["official_label"]),
            (
                policy_row["official_legal_reference"],
                coded_row["legal_reference"],
            ),
            (
                policy_row["official_regulation_reference"],
                coded_row["regulation_or_annex_reference"],
            ),
        )
        if any(
            not _null_safe_equal(actual, expected)
            for actual, expected in meaning_comparisons
        ):
            raise BessPlanningFeatureApplicationError(
                f"Policy official meaning differs from code dictionary for pair {key}"
            )


def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult
    | BessPlanningFeatureApplicationArtifactManifest,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
    comparisons = (
        (result.policy_profile, policy.policy_profile, "policy profile"),
        (result.policy_sha256, policy.policy_sha256, "policy SHA256"),
        (
            result.policy_result_hash_schema_version,
            policy.result_hash_schema_version,
            "policy result hash schema",
        ),
        (
            result.policy_complete_result_content_sha256,
            policy.complete_result_content_sha256,
            "policy result SHA256",
        ),
        (result.cnig_profile, coded.profile, "CNIG profile"),
        (result.cnig_profile_sha256, coded.profile_sha256, "CNIG profile SHA256"),
        (
            result.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "CNIG result hash schema",
        ),
        (
            result.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "CNIG result SHA256",
        ),
        (result.source_document_id, coded.source_document_id, "document ID"),
        (result.source_archive_sha256, coded.source_archive_sha256, "archive SHA256"),
        (
            result.cnig_surface_features_content_sha256,
            coded.surface_features_content_sha256,
            "coded surface SHA256",
        ),
        (
            result.cnig_line_features_content_sha256,
            coded.line_features_content_sha256,
            "coded line SHA256",
        ),
        (
            result.cnig_point_features_content_sha256,
            coded.point_features_content_sha256,
            "coded point SHA256",
        ),
        (
            result.cnig_relations_content_sha256,
            coded.relations_content_sha256,
            "coded relations SHA256",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Application source lock differs for {label}"
            )

    policy_coded_comparisons = (
        (policy.source_document_id, coded.source_document_id, "policy document ID"),
        (
            policy.source_archive_sha256,
            coded.source_archive_sha256,
            "policy archive SHA256",
        ),
        (policy.cnig_profile, coded.profile, "policy CNIG profile"),
        (
            policy.cnig_profile_schema_version,
            coded.profile_schema_version,
            "policy CNIG profile schema",
        ),
        (
            policy.cnig_profile_sha256,
            coded.profile_sha256,
            "policy CNIG profile SHA256",
        ),
        (
            policy.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "policy CNIG result hash schema",
        ),
        (
            policy.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "policy CNIG result SHA256",
        ),
    )
    for actual, expected, label in policy_coded_comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Application source lock differs for {label}"
            )


def _validate_policy_source(
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
) -> None:
    try:
        validate_bess_planning_feature_policy_result(
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
        )
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "Source-complete BESS planning-feature policy validation failed"
        ) from error


def apply_bess_planning_feature_policy(
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
) -> BessPlanningFeatureApplicationResult:
    """Validate once, then propagate exact compiled policy to features and relations."""

    try:
        _validate_policy_source(
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
        )
        result = _build_result(coded_result, policy_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature policy application failed safely"
        ) from error


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureApplicationError(
            f"Application {label} differs from rebuilt result"
        )


def validate_bess_planning_feature_application_result(
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
    result: BessPlanningFeatureApplicationResult,
) -> None:
    """Independently rebuild exact policy propagation from every source input."""

    try:
        _validate_result_envelope(result)
        _validate_source_locks(result, coded_result, policy_result)
        _validate_policy_source(
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
        )
        expected = _build_result(coded_result, policy_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureApplicationError(
                    f"Application {field} differs from rebuilt result"
                )
        for actual, rebuilt, label in (
            (result.surface_features, expected.surface_features, "surface features"),
            (result.line_features, expected.line_features, "line features"),
            (result.point_features, expected.point_features, "point features"),
            (result.relations, expected.relations, "relations"),
        ):
            _compare_frame(actual, rebuilt, label)
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature application result validation failed safely"
        ) from error


def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
    if path.name != record.filename:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} filename differs"
        )
    payload = path.read_bytes()
    if len(payload) != record.size_bytes:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} byte size differs"
        )
    if sha256(payload).hexdigest() != record.sha256:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} SHA256 differs"
        )
    buffer = BytesIO(payload)
    frame: pd.DataFrame
    if record.geospatial:
        frame = gpd.read_parquet(buffer)
    else:
        frame = pd.read_parquet(buffer)
    if len(frame) != record.row_count:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} row count differs"
        )
    signature = deterministic_frame_schema_signature(frame)
    if signature != record.frame_schema_signature:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} frame schema differs"
        )
    if record.geospatial:
        if not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} geospatial contract differs"
            )
        if CRS.from_user_input(frame.crs).to_json_dict() != record.crs:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Relations artifact unexpectedly loaded as geospatial"
        )
    return frame


def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
    """Load byte-sealed outputs and bind them to exact validated upstream results."""

    try:
        validate_planning_feature_code_result_envelope(coded_result)
        validate_bess_planning_feature_policy_result_envelope(policy_result)
        _validate_coded_policy_compatibility(coded_result, policy_result)
        payload = loads_strict_json_object(Path(manifest_path).read_bytes())
        manifest = BessPlanningFeatureApplicationArtifactManifest.model_validate(
            payload
        )
        _validate_source_locks(manifest, coded_result, policy_result)
        paths = {
            "SURFACE_FEATURES": Path(surface_features_path),
            "LINE_FEATURES": Path(line_features_path),
            "POINT_FEATURES": Path(point_features_path),
            "RELATIONS": Path(relations_path),
        }
        records = {record.artifact_role: record for record in manifest.artifacts}
        loaded = {
            role: _read_verified_artifact(paths[role], records[role])
            for role in ARTIFACT_ROLES
        }
        result = BessPlanningFeatureApplicationResult(
            **{field: getattr(manifest, field) for field in RESULT_SCALAR_FIELDS},
            surface_features=loaded["SURFACE_FEATURES"],
            line_features=loaded["LINE_FEATURES"],
            point_features=loaded["POINT_FEATURES"],
            relations=loaded["RELATIONS"],
        )
        _validate_result_envelope(result)
        expected = _build_result(coded_result, policy_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureApplicationError(
                    f"Application artifact scalar {field} differs from upstream rebuild"
                )
        for field in RESULT_FRAME_FIELDS:
            _compare_frame(
                getattr(result, field),
                getattr(expected, field),
                f"artifact {field}",
            )
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"BESS planning-feature application artifacts are invalid: {error}"
        ) from error
```
