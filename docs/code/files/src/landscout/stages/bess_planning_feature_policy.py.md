# `src/landscout/stages/bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/bess_planning_feature_policy.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.
- Source SHA256: `bfb8f2bcb90764557f17e1af21284167d2824777775d32ed58401ec031ad2954`

## 1. STEP 7F.1A.4 contract delta

- Uses strict duplicate-safe policy YAML, frozen/deeply immutable decision inputs, and public-boundary reconstruction without changing policy meaning or hashes.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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

### Internal LandScout imports

- `from landscout.common.artifact_paths import validate_portable_parquet_filename`
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.common.immutable_mapping import freeze_mapping`
- `from landscout.common.strict_json import loads_strict_json_object`
- `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- `from landscout.sources.gpu_fr import GpuPlanningDocument`
- `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "BessPlanningFeaturePolicyArtifactManifest",
    "BessPlanningFeaturePolicyConfig",
    "BessPlanningFeaturePolicyError",
    "BessPlanningFeaturePolicyResult",
    "compile_bess_planning_feature_policy",
    "load_bess_planning_feature_policy_artifacts",
    "load_bess_planning_feature_policy_config",
    "validate_bess_planning_feature_policy_result",
    "validate_bess_planning_feature_policy_result_envelope",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `BessPlanningFeaturePolicyArtifactManifest`
  - `BessPlanningFeaturePolicyConfig`
  - `BessPlanningFeaturePolicyError`
  - `BessPlanningFeaturePolicyResult`
  - `compile_bess_planning_feature_policy`
  - `load_bess_planning_feature_policy_artifacts`
  - `load_bess_planning_feature_policy_config`
  - `validate_bess_planning_feature_policy_result`
  - `validate_bess_planning_feature_policy_result_envelope`

### `POLICY_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POLICY_SCHEMA_VERSION = 1
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

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
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POLICY_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ARTIFACT_KIND`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `FeatureFamily`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PrecheckStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
PrecheckStatus = Literal[
    "LIKELY_MATERIAL_CONSTRAINT",
    "MATERIAL_REVIEW_REQUIRED",
    "DESIGN_REVIEW_REQUIRED",
    "CONTEXT_REVIEW_REQUIRED",
    "UNKNOWN",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `Confidence`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ALLOWED_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ALLOWED_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ALLOWED_CONFIDENCES`

- Category: module constant or closed domain.
- Exact declaration:

```python
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
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

### `SHA_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POLICY_TABLE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POLICY_TABLE_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "official_legal_reference",
    "official_regulation_reference",
    "precheck_status",
    "confidence",
    "status_priority",
    "rationale",
    "required_human_action",
    "limitations",
    "policy_scope",
    "local_feature_text_interpreted",
    "local_regulation_content_interpreted",
    "legal_conclusion_produced",
    "policy_profile",
    "policy_sha256",
    "cnig_profile",
    "cnig_profile_sha256",
    "cnig_complete_result_content_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `feature_family`
  - `type_code`
  - `subtype_code`
  - `official_label`
  - `official_legal_reference`
  - `official_regulation_reference`
  - `precheck_status`
  - `confidence`
  - `status_priority`
  - `rationale`
  - `required_human_action`
  - `limitations`
  - `policy_scope`
  - `local_feature_text_interpreted`
  - `local_regulation_content_interpreted`
  - `legal_conclusion_produced`
  - `policy_profile`
  - `policy_sha256`
  - `cnig_profile`
  - `cnig_profile_sha256`
  - `cnig_complete_result_content_sha256`

### `POLICY_TABLE_DTYPES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POLICY_TABLE_DTYPES = tuple(
    "int64"
    if column == "status_priority"
    else "bool"
    if column
    in {
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    }
    else "str"
    for column in POLICY_TABLE_COLUMNS
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POLICY_TABLE_SCHEMA_SIGNATURE`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POLICY_TABLE_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(POLICY_TABLE_COLUMNS),
    "dtypes": list(POLICY_TABLE_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `NULL_REFERENCE_LITERALS`

- Category: module constant or closed domain.
- Exact declaration:

```python
NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `POLICY_RESULT_SCALAR_FIELDS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POLICY_RESULT_SCALAR_FIELDS = (
    "policy_schema_version",
    "result_hash_schema_version",
    "policy_profile",
    "policy_scope",
    "policy_sha256",
    "source_document_id",
    "source_archive_sha256",
    "cnig_profile",
    "cnig_profile_schema_version",
    "cnig_profile_sha256",
    "cnig_result_hash_schema_version",
    "cnig_complete_result_content_sha256",
    "policy_table_content_sha256",
    "complete_result_content_sha256",
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `policy_schema_version`
  - `result_hash_schema_version`
  - `policy_profile`
  - `policy_scope`
  - `policy_sha256`
  - `source_document_id`
  - `source_archive_sha256`
  - `cnig_profile`
  - `cnig_profile_schema_version`
  - `cnig_profile_sha256`
  - `cnig_result_hash_schema_version`
  - `cnig_complete_result_content_sha256`
  - `policy_table_content_sha256`
  - `complete_result_content_sha256`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `BessPlanningFeaturePolicyError`

**Source purpose:** Raised when the official-code BESS policy cannot be proven exact.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- constructor call: `landscout.stages.bess_planning_feature_policy::_canonical_json_sha256` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_canonical_json_sha256` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_config` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_config` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_resolved_policy_config` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_resolved_policy_config` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_canonical_value` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_canonical_value` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_validate_source_lock` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_source_lock` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_dictionary_by_pair` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_dictionary_by_pair` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_validate_policy_table_rows` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_table_rows` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result_envelope` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result_envelope` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyError`
- constructor call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyError`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyError`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_null_reference_literal_is_rejected_by_local_envelope` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_source_lock_mismatch_is_rejected` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_duplicate_yaml_key_is_rejected` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_in_memory_config_is_revalidated_before_compilation` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_table_mutation_is_rejected` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_manifest_mismatch` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_uses_strict_json_before_parquet_read` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_parquet_replacement` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_locally_invalid_result_fast_fails_before_source_validation` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_forged_matching_lock_still_runs_source_complete_validation` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_rejects_canonical_empty_policy_table` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_cnig_profile_schema_two` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_cnig_result_schema_five` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_validates_every_intrinsic_row_contract` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1` via `BessPlanningFeaturePolicyError`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_controls_malformed_result_type` via `BessPlanningFeaturePolicyError`

**Exact class source**

```python
class BessPlanningFeaturePolicyError(ValueError):
    """Raised when the official-code BESS policy cannot be proven exact."""
```

### `_StrictPolicyModel`

**Source purpose:** Defines `_StrictPolicyModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

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
class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `PolicyTableSchemaSignature`

**Source purpose:** Immutable persisted schema identity for the normalized policy table.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `columns` | `tuple[StrictStr, ...]` | `required` | `columns: tuple[StrictStr, ...]` |
| `dtypes` | `tuple[StrictStr, ...]` | `required` | `dtypes: tuple[StrictStr, ...]` |
| `index_class` | `StrictStr` | `required` | `index_class: StrictStr` |
| `index_names` | `tuple[StrictStr \| None, ...]` | `required` | `index_names: tuple[StrictStr \| None, ...]` |
| `index_level_dtypes` | `tuple[StrictStr, ...]` | `required` | `index_level_dtypes: tuple[StrictStr, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class PolicyTableSchemaSignature(_StrictPolicyModel):
    """Immutable persisted schema identity for the normalized policy table."""

    columns: tuple[StrictStr, ...]
    dtypes: tuple[StrictStr, ...]
    index_class: StrictStr
    index_names: tuple[StrictStr | None, ...]
    index_level_dtypes: tuple[StrictStr, ...]
```

### `PolicySourceLock`

**Source purpose:** Defines `PolicySourceLock`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `StrictStr` | `required` | `document_id: StrictStr` |
| `archive_sha256` | `StrictStr` | `required` | `archive_sha256: StrictStr` |
| `cnig_profile` | `StrictStr` | `required` | `cnig_profile: StrictStr` |
| `cnig_profile_schema_version` | `StrictInt` | `required` | `cnig_profile_schema_version: StrictInt` |
| `cnig_profile_sha256` | `StrictStr` | `required` | `cnig_profile_sha256: StrictStr` |
| `cnig_result_hash_schema_version` | `StrictInt` | `required` | `cnig_result_hash_schema_version: StrictInt` |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | `cnig_complete_result_content_sha256: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicySourceLock._validate_lock` via `PolicySourceLock`

**Exact class source**

```python
class PolicySourceLock(_StrictPolicyModel):
    document_id: StrictStr
    archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr

    @model_validator(mode="after")
    def _validate_lock(self) -> PolicySourceLock:
        _exact_string(self.document_id, "document_id")
        _sha256_string(self.archive_sha256, "archive_sha256")
        _exact_string(self.cnig_profile, "cnig_profile")
        _sha256_string(self.cnig_profile_sha256, "cnig_profile_sha256")
        _sha256_string(
            self.cnig_complete_result_content_sha256,
            "cnig_complete_result_content_sha256",
        )
        for value, label in (
            (self.cnig_profile_schema_version, "cnig_profile_schema_version"),
            (self.cnig_result_hash_schema_version, "cnig_result_hash_schema_version"),
        ):
            if type(value) is not int or value < 1:
                raise ValueError(f"{label} must be a strict positive integer")
        return self
```

### `PolicyEntry`

**Source purpose:** Defines `PolicyEntry`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `feature_family` | `FeatureFamily` | `required` | `feature_family: FeatureFamily` |
| `type_code` | `StrictStr` | `required` | `type_code: StrictStr` |
| `subtype_code` | `StrictStr` | `required` | `subtype_code: StrictStr` |
| `expected_official_label` | `StrictStr` | `required` | `expected_official_label: StrictStr` |
| `expected_legal_reference` | `StrictStr \| None` | `required` | `expected_legal_reference: StrictStr \| None` |
| `expected_regulation_reference` | `StrictStr \| None` | `required` | `expected_regulation_reference: StrictStr \| None` |
| `precheck_status` | `PrecheckStatus` | `required` | `precheck_status: PrecheckStatus` |
| `confidence` | `Confidence` | `required` | `confidence: Confidence` |
| `rationale` | `StrictStr` | `required` | `rationale: StrictStr` |
| `required_human_action` | `StrictStr` | `required` | `required_human_action: StrictStr` |
| `limitations` | `StrictStr` | `required` | `limitations: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicyEntry._validate_entry` via `PolicyEntry`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_entries_sha256` via `PolicyEntry`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `PolicyEntry`

**Exact class source**

```python
class PolicyEntry(_StrictPolicyModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    expected_official_label: StrictStr
    expected_legal_reference: StrictStr | None
    expected_regulation_reference: StrictStr | None
    precheck_status: PrecheckStatus
    confidence: Confidence
    rationale: StrictStr
    required_human_action: StrictStr
    limitations: StrictStr

    @model_validator(mode="after")
    def _validate_entry(self) -> PolicyEntry:
        if CODE_PATTERN.fullmatch(self.type_code) is None:
            raise ValueError("type_code must be an exact two-character digit string")
        if CODE_PATTERN.fullmatch(self.subtype_code) is None:
            raise ValueError("subtype_code must be an exact two-character digit string")
        _exact_string(self.expected_official_label, "expected_official_label")
        _optional_exact_string(
            self.expected_legal_reference, "expected_legal_reference"
        )
        _optional_exact_string(
            self.expected_regulation_reference,
            "expected_regulation_reference",
        )
        _exact_string(self.rationale, "rationale")
        _exact_string(self.required_human_action, "required_human_action")
        _exact_string(self.limitations, "limitations")
        return self
```

### `BessPlanningFeaturePolicyConfig`

**Source purpose:** Defines `BessPlanningFeaturePolicyConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `profile` | `StrictStr` | `required` | `profile: StrictStr` |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` |
| `local_feature_text_interpreted` | `StrictBool` | `required` | `local_feature_text_interpreted: StrictBool` |
| `local_regulation_content_interpreted` | `StrictBool` | `required` | `local_regulation_content_interpreted: StrictBool` |
| `legal_conclusion_produced` | `StrictBool` | `required` | `legal_conclusion_produced: StrictBool` |
| `source_lock` | `PolicySourceLock` | `required` | `source_lock: PolicySourceLock` |
| `status_priority` | `dict[PrecheckStatus, StrictInt]` | `required` | `status_priority: dict[PrecheckStatus, StrictInt]` |
| `canonical_policy_entries_sha256` | `StrictStr` | `required` | `canonical_policy_entries_sha256: StrictStr` |
| `entries` | `tuple[PolicyEntry, ...]` | `required` | `entries: tuple[PolicyEntry, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeaturePolicyConfig`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_config` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_resolved_policy_config` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_sha256` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_source_lock` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_table` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyConfig`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_validated_config` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_policy_text_drift` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_source_lock_drift` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_status_priority_contract_is_strict` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_unknown_yaml_field_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_malformed_sha256_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `BessPlanningFeaturePolicyConfig`

**Exact class source**

```python
class BessPlanningFeaturePolicyConfig(_StrictPolicyModel):
    schema_version: StrictInt
    profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    source_lock: PolicySourceLock
    status_priority: dict[PrecheckStatus, StrictInt]
    canonical_policy_entries_sha256: StrictStr
    entries: tuple[PolicyEntry, ...]

    @model_validator(mode="after")
    def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
        if (
            type(self.schema_version) is not int
            or self.schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError(
                f"policy schema version must equal {POLICY_SCHEMA_VERSION}"
            )
        _exact_string(self.profile, "profile")
        if self.policy_scope != POLICY_SCOPE:
            raise ValueError("policy_scope is unsupported")
        if (
            self.local_feature_text_interpreted is not False
            or self.local_regulation_content_interpreted is not False
            or self.legal_conclusion_produced is not False
        ):
            raise ValueError(
                "policy interpretation and legal-conclusion flags must be false"
            )
        if set(self.status_priority) != ALLOWED_STATUSES:
            raise ValueError(
                "status priority must contain every allowed status exactly once"
            )
        priorities = list(self.status_priority.values())
        if any(type(value) is not int or value <= 0 for value in priorities):
            raise ValueError("status priority values must be strict positive integers")
        if len(set(priorities)) != len(priorities):
            raise ValueError("status priority values must be unique")
        keys = [
            (entry.feature_family, entry.type_code, entry.subtype_code)
            for entry in self.entries
        ]
        if len(keys) != len(set(keys)):
            raise ValueError(
                "policy entries contain a duplicate family/type/subtype pair"
            )
        if keys != sorted(keys):
            raise ValueError(
                "policy entries must use deterministic family/type/subtype order"
            )
        _sha256_string(
            self.canonical_policy_entries_sha256,
            "canonical_policy_entries_sha256",
        )
        if _policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256:
            raise ValueError(
                "canonical policy-entry SHA256 differs from policy entries"
            )
        object.__setattr__(
            self, "status_priority", freeze_mapping(self.status_priority)
        )
        return self
```

### `BessPlanningFeaturePolicyResult`

**Source purpose:** Immutable normalized policy table and its source-complete hash envelope.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `policy_schema_version` | `int` | `required` | `policy_schema_version: int` |
| `result_hash_schema_version` | `int` | `required` | `result_hash_schema_version: int` |
| `policy_profile` | `str` | `required` | `policy_profile: str` |
| `policy_scope` | `str` | `required` | `policy_scope: str` |
| `policy_sha256` | `str` | `required` | `policy_sha256: str` |
| `source_document_id` | `str` | `required` | `source_document_id: str` |
| `source_archive_sha256` | `str` | `required` | `source_archive_sha256: str` |
| `cnig_profile` | `str` | `required` | `cnig_profile: str` |
| `cnig_profile_schema_version` | `int` | `required` | `cnig_profile_schema_version: int` |
| `cnig_profile_sha256` | `str` | `required` | `cnig_profile_sha256: str` |
| `cnig_result_hash_schema_version` | `int` | `required` | `cnig_result_hash_schema_version: int` |
| `cnig_complete_result_content_sha256` | `str` | `required` | `cnig_complete_result_content_sha256: str` |
| `policy_table_content_sha256` | `str` | `required` | `policy_table_content_sha256: str` |
| `complete_result_content_sha256` | `str` | `required` | `complete_result_content_sha256: str` |
| `policy_table` | `pd.DataFrame` | `required` | `policy_table: pd.DataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeaturePolicyResult`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_policy_lookup` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_policy_values` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_apply_feature_catalog` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_coded_policy_compatibility` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_source_locks` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_component_metadata` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_table_sha256` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_complete_result_sha256` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_result_with_hashes` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_table_rows` via `BessPlanningFeaturePolicyResult`
- constructor call: `landscout.stages.bess_planning_feature_policy::_build_result` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result_envelope` via `BessPlanningFeaturePolicyResult`
- constructor call: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyResult`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `BessPlanningFeaturePolicyResult`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_artifact_manifest` via `BessPlanningFeaturePolicyResult`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_write_artifacts` via `BessPlanningFeaturePolicyResult`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_checked_in_policy_result` via `BessPlanningFeaturePolicyResult`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_rehash_policy_table` via `BessPlanningFeaturePolicyResult`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_canonical_empty_policy_result` via `BessPlanningFeaturePolicyResult`

**Exact class source**

```python
class BessPlanningFeaturePolicyResult:
    """Immutable normalized policy table and its source-complete hash envelope."""

    policy_schema_version: int
    result_hash_schema_version: int
    policy_profile: str
    policy_scope: str
    policy_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_schema_version: int
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    policy_table_content_sha256: str
    complete_result_content_sha256: str
    policy_table: pd.DataFrame
```

### `BessPlanningFeaturePolicyArtifactManifest`

**Source purpose:** Strict physical binding between one policy table and its hash envelope.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `artifact_kind` | `Literal['BESS_CNIG_FEATURE_POLICY_RESULT']` | `required` | `artifact_kind: Literal["BESS_CNIG_FEATURE_POLICY_RESULT"]` |
| `policy_schema_version` | `StrictInt` | `required` | `policy_schema_version: StrictInt` |
| `result_hash_schema_version` | `StrictInt` | `required` | `result_hash_schema_version: StrictInt` |
| `policy_profile` | `StrictStr` | `required` | `policy_profile: StrictStr` |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` |
| `policy_sha256` | `StrictStr` | `required` | `policy_sha256: StrictStr` |
| `source_document_id` | `StrictStr` | `required` | `source_document_id: StrictStr` |
| `source_archive_sha256` | `StrictStr` | `required` | `source_archive_sha256: StrictStr` |
| `cnig_profile` | `StrictStr` | `required` | `cnig_profile: StrictStr` |
| `cnig_profile_schema_version` | `StrictInt` | `required` | `cnig_profile_schema_version: StrictInt` |
| `cnig_profile_sha256` | `StrictStr` | `required` | `cnig_profile_sha256: StrictStr` |
| `cnig_result_hash_schema_version` | `StrictInt` | `required` | `cnig_result_hash_schema_version: StrictInt` |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | `cnig_complete_result_content_sha256: StrictStr` |
| `policy_table_content_sha256` | `StrictStr` | `required` | `policy_table_content_sha256: StrictStr` |
| `complete_result_content_sha256` | `StrictStr` | `required` | `complete_result_content_sha256: StrictStr` |
| `parquet_filename` | `StrictStr` | `required` | `parquet_filename: StrictStr` |
| `parquet_row_count` | `StrictInt` | `required` | `parquet_row_count: StrictInt` |
| `parquet_size_bytes` | `StrictInt` | `required` | `parquet_size_bytes: StrictInt` |
| `parquet_sha256` | `StrictStr` | `required` | `parquet_sha256: StrictStr` |
| `policy_table_schema_signature` | `PolicyTableSchemaSignature` | `required` | `policy_table_schema_signature: PolicyTableSchemaSignature` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `BessPlanningFeaturePolicyArtifactManifest`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyArtifactManifest`

**Exact class source**

```python
class BessPlanningFeaturePolicyArtifactManifest(_StrictPolicyModel):
    """Strict physical binding between one policy table and its hash envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_CNIG_FEATURE_POLICY_RESULT"]
    policy_schema_version: StrictInt
    result_hash_schema_version: StrictInt
    policy_profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    policy_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    policy_table_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    parquet_filename: StrictStr
    parquet_row_count: StrictInt
    parquet_size_bytes: StrictInt
    parquet_sha256: StrictStr
    policy_table_schema_signature: PolicyTableSchemaSignature

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError(
                "artifact manifest schema version must equal "
                f"{ARTIFACT_MANIFEST_SCHEMA_VERSION}"
            )
        if (
            type(self.policy_schema_version) is not int
            or self.policy_schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError("artifact policy schema version is unsupported")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("artifact result hash schema version is unsupported")
        if (
            type(self.cnig_profile_schema_version) is not int
            or self.cnig_profile_schema_version != 2
        ):
            raise ValueError("artifact CNIG profile schema version is unsupported")
        if (
            type(self.cnig_result_hash_schema_version) is not int
            or self.cnig_result_hash_schema_version != 5
        ):
            raise ValueError("artifact CNIG result hash schema version is unsupported")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.source_document_id, "source_document_id"),
            (self.cnig_profile, "cnig_profile"),
        ):
            _exact_string(exact_value, label)
        for hash_value, label in (
            (self.policy_sha256, "policy_sha256"),
            (self.source_archive_sha256, "source_archive_sha256"),
            (self.cnig_profile_sha256, "cnig_profile_sha256"),
            (
                self.cnig_complete_result_content_sha256,
                "cnig_complete_result_content_sha256",
            ),
            (self.policy_table_content_sha256, "policy_table_content_sha256"),
            (self.complete_result_content_sha256, "complete_result_content_sha256"),
            (self.parquet_sha256, "parquet_sha256"),
        ):
            _sha256_string(hash_value, label)
        for integer_value, label, allow_zero in (
            (self.parquet_row_count, "parquet_row_count", True),
            (self.parquet_size_bytes, "parquet_size_bytes", False),
        ):
            minimum = 0 if allow_zero else 1
            if type(integer_value) is not int or integer_value < minimum:
                raise ValueError(f"{label} is invalid")
        validate_portable_parquet_filename(self.parquet_filename, "parquet_filename")
        return self
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_exact_string`

**Purpose:** Implements `exact string` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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
  - `ValueError(<br>            f"{label} must be an exact non-empty string without edge whitespace"<br>        )` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_optional_exact_string` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_optional_exact_string` via `_exact_string`
- direct call: `landscout.stages.bess_planning_feature_policy::_sha256_string` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_sha256_string` via `_exact_string`
- direct call: `landscout.stages.bess_planning_feature_policy::PolicySourceLock._validate_lock` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicySourceLock._validate_lock` via `_exact_string`
- direct call: `landscout.stages.bess_planning_feature_policy::PolicyEntry._validate_entry` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicyEntry._validate_entry` via `_exact_string`
- direct call: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `_exact_string`
- direct call: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_exact_string`
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_policy_table_rows` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_table_rows` via `_exact_string`
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_exact_string`

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
        raise ValueError(
            f"{label} must be an exact non-empty string without edge whitespace"
        )
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_optional_exact_string`

**Purpose:** Implements `optional exact string` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _optional_exact_string(value: object, label: str) -> str | None:
```

- Exact decorators: none.
- Declared return annotation: `str | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `_exact_string(value, label)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::PolicyEntry._validate_entry` via `_optional_exact_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicyEntry._validate_entry` via `_optional_exact_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |

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
def _optional_exact_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _exact_string(value, label)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_sha256_string`

**Purpose:** Implements `sha256 string` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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
- direct call: `landscout.stages.bess_planning_feature_policy::PolicySourceLock._validate_lock` via `_sha256_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicySourceLock._validate_lock` via `_sha256_string`
- direct call: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `_sha256_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `_sha256_string`
- direct call: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_sha256_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_sha256_string`
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_sha256_string`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_sha256_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |
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

### `PolicySourceLock._validate_lock`

**Purpose:** Implements `validate lock` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_lock(self) -> PolicySourceLock:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `PolicySourceLock`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(f"{label} must be a strict positive integer")` under lexical guard `type(value) is not int or value < 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |
| `_sha256_string` | `landscout.stages.bess_planning_feature_policy._sha256_string` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _validate_lock(self) -> PolicySourceLock:
        _exact_string(self.document_id, "document_id")
        _sha256_string(self.archive_sha256, "archive_sha256")
        _exact_string(self.cnig_profile, "cnig_profile")
        _sha256_string(self.cnig_profile_sha256, "cnig_profile_sha256")
        _sha256_string(
            self.cnig_complete_result_content_sha256,
            "cnig_complete_result_content_sha256",
        )
        for value, label in (
            (self.cnig_profile_schema_version, "cnig_profile_schema_version"),
            (self.cnig_result_hash_schema_version, "cnig_result_hash_schema_version"),
        ):
            if type(value) is not int or value < 1:
                raise ValueError(f"{label} must be a strict positive integer")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `PolicyEntry._validate_entry`

**Purpose:** Implements `validate entry` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_entry(self) -> PolicyEntry:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `PolicyEntry`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("type_code must be an exact two-character digit string")` under lexical guard `CODE_PATTERN.fullmatch(self.type_code) is None`.
  - `ValueError("subtype_code must be an exact two-character digit string")` under lexical guard `CODE_PATTERN.fullmatch(self.subtype_code) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `CODE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |
| `_optional_exact_string` | `landscout.stages.bess_planning_feature_policy._optional_exact_string` |
| `model_validator` | `pydantic.model_validator` |

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
def _validate_entry(self) -> PolicyEntry:
        if CODE_PATTERN.fullmatch(self.type_code) is None:
            raise ValueError("type_code must be an exact two-character digit string")
        if CODE_PATTERN.fullmatch(self.subtype_code) is None:
            raise ValueError("subtype_code must be an exact two-character digit string")
        _exact_string(self.expected_official_label, "expected_official_label")
        _optional_exact_string(
            self.expected_legal_reference, "expected_legal_reference"
        )
        _optional_exact_string(
            self.expected_regulation_reference,
            "expected_regulation_reference",
        )
        _exact_string(self.rationale, "rationale")
        _exact_string(self.required_human_action, "required_human_action")
        _exact_string(self.limitations, "limitations")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_json_sha256`

**Purpose:** Implements `canonical json sha256` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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
  - `BessPlanningFeaturePolicyError(<br>            "Policy integrity payload is not canonical JSON"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_policy_entries_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_entries_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.bess_planning_feature_policy::_policy_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.bess_planning_feature_policy::_policy_table_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_table_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.bess_planning_feature_policy::_complete_result_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_complete_result_sha256` via `_canonical_json_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
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
        raise BessPlanningFeaturePolicyError(
            "Policy integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_entries_sha256`

**Purpose:** Implements `policy entries sha256` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `entries` | positional-or-keyword | `tuple[PolicyEntry, ...]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256([entry.model_dump(mode="json") for entry in entries])`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `_policy_entries_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `_policy_entries_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.bess_planning_feature_policy._canonical_json_sha256` |
| `entry.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
    return _canonical_json_sha256([entry.model_dump(mode="json") for entry in entries])
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `BessPlanningFeaturePolicyConfig._validate_policy`

**Purpose:** Implements `validate policy` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `BessPlanningFeaturePolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(<br>                f"policy schema version must equal {POLICY_SCHEMA_VERSION}"<br>            )` under lexical guard `type(self.schema_version) is not int<br>            or self.schema_version != POLICY_SCHEMA_VERSION`.
  - `ValueError("policy_scope is unsupported")` under lexical guard `self.policy_scope != POLICY_SCOPE`.
  - `ValueError(<br>                "policy interpretation and legal-conclusion flags must be false"<br>            )` under lexical guard `self.local_feature_text_interpreted is not False<br>            or self.local_regulation_content_interpreted is not False<br>            or self.legal_conclusion_produced is not False`.
  - `ValueError(<br>                "status priority must contain every allowed status exactly once"<br>            )` under lexical guard `set(self.status_priority) != ALLOWED_STATUSES`.
  - `ValueError("status priority values must be strict positive integers")` under lexical guard `any(type(value) is not int or value <= 0 for value in priorities)`.
  - `ValueError("status priority values must be unique")` under lexical guard `len(set(priorities)) != len(priorities)`.
  - `ValueError(<br>                "policy entries contain a duplicate family/type/subtype pair"<br>            )` under lexical guard `len(keys) != len(set(keys))`.
  - `ValueError(<br>                "policy entries must use deterministic family/type/subtype order"<br>            )` under lexical guard `keys != sorted(keys)`.
  - `ValueError(<br>                "canonical policy-entry SHA256 differs from policy entries"<br>            )` under lexical guard `_policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `self.status_priority.values` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.status_priority.values` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_string` | `landscout.stages.bess_planning_feature_policy._sha256_string` |
| `_policy_entries_sha256` | `landscout.stages.bess_planning_feature_policy._policy_entries_sha256` |
| `object.__setattr__` | `unresolved local/third-party receiver; no ownership inferred` |
| `freeze_mapping` | `landscout.common.immutable_mapping.freeze_mapping` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `self.status_priority.values` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_string`<br>`_policy_entries_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
        if (
            type(self.schema_version) is not int
            or self.schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError(
                f"policy schema version must equal {POLICY_SCHEMA_VERSION}"
            )
        _exact_string(self.profile, "profile")
        if self.policy_scope != POLICY_SCOPE:
            raise ValueError("policy_scope is unsupported")
        if (
            self.local_feature_text_interpreted is not False
            or self.local_regulation_content_interpreted is not False
            or self.legal_conclusion_produced is not False
        ):
            raise ValueError(
                "policy interpretation and legal-conclusion flags must be false"
            )
        if set(self.status_priority) != ALLOWED_STATUSES:
            raise ValueError(
                "status priority must contain every allowed status exactly once"
            )
        priorities = list(self.status_priority.values())
        if any(type(value) is not int or value <= 0 for value in priorities):
            raise ValueError("status priority values must be strict positive integers")
        if len(set(priorities)) != len(priorities):
            raise ValueError("status priority values must be unique")
        keys = [
            (entry.feature_family, entry.type_code, entry.subtype_code)
            for entry in self.entries
        ]
        if len(keys) != len(set(keys)):
            raise ValueError(
                "policy entries contain a duplicate family/type/subtype pair"
            )
        if keys != sorted(keys):
            raise ValueError(
                "policy entries must use deterministic family/type/subtype order"
            )
        _sha256_string(
            self.canonical_policy_entries_sha256,
            "canonical_policy_entries_sha256",
        )
        if _policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256:
            raise ValueError(
                "canonical policy-entry SHA256 differs from policy entries"
            )
        object.__setattr__(
            self, "status_priority", freeze_mapping(self.status_priority)
        )
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `load_bess_planning_feature_policy_config`

**Purpose:** Load a strict offline BESS policy for official CNIG feature-code pairs.

**Exact signature**

```python
def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BessPlanningFeaturePolicyConfig.model_validate(payload)`
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError("BESS CNIG policy must be a mapping")` under lexical guard `not isinstance(payload, Mapping)`.
  - `re-raise`.
  - `BessPlanningFeaturePolicyError(str(error))`.
  - `BessPlanningFeaturePolicyError(<br>            "BESS CNIG feature policy is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- direct call: `landscout.stages.bess_planning_feature_policy::_resolved_policy_config` via `load_bess_planning_feature_policy_config`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_resolved_policy_config` via `load_bess_planning_feature_policy_config`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- direct call: `tests.unit.test_bess_planning_feature_policy::_checked_in_policy_result` via `load_bess_planning_feature_policy_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_checked_in_policy_result` via `load_bess_planning_feature_policy_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_checked_in_policy_pins_all_twelve_exact_muret_decisions` via `load_bess_planning_feature_policy_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_checked_in_policy_pins_all_twelve_exact_muret_decisions` via `load_bess_planning_feature_policy_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_checked_in_policy_complete_snapshot_is_immutable` via `load_bess_planning_feature_policy_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_checked_in_policy_complete_snapshot_is_immutable` via `load_bess_planning_feature_policy_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_policy_text_drift` via `load_bess_planning_feature_policy_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_policy_text_drift` via `load_bess_planning_feature_policy_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_source_lock_drift` via `load_bess_planning_feature_policy_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_source_lock_drift` via `load_bess_planning_feature_policy_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_duplicate_yaml_key_is_rejected` via `load_bess_planning_feature_policy_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_duplicate_yaml_key_is_rejected` via `load_bess_planning_feature_policy_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `Path(path).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path(path).read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
    """Load a strict offline BESS policy for official CNIG feature-code pairs."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise BessPlanningFeaturePolicyError("BESS CNIG policy must be a mapping")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except BessPlanningFeaturePolicyError:
        raise
    except StrictYamlError as error:
        raise BessPlanningFeaturePolicyError(str(error)) from error
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_resolved_policy_config`

**Purpose:** Implements `resolved policy config` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `load_bess_planning_feature_policy_config(config)`
  - `BessPlanningFeaturePolicyConfig.model_validate(payload)`
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>            "in-memory BESS planning-feature policy config is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_resolved_policy_config`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_resolved_policy_config`
- direct call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_resolved_policy_config`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_resolved_policy_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |

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
def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
    if not isinstance(config, BessPlanningFeaturePolicyConfig):
        return load_bess_planning_feature_policy_config(config)
    try:
        payload = config.model_dump(mode="python", warnings="error")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "in-memory BESS planning-feature policy config is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_sha256`

**Purpose:** Implements `policy sha256` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(config.model_dump(mode="json"))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_build_result` via `_policy_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `_policy_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.bess_planning_feature_policy._canonical_json_sha256` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
    return _canonical_json_sha256(config.model_dump(mode="json"))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `BessPlanningFeaturePolicyArtifactManifest._validate_manifest`

**Purpose:** Implements `validate manifest` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `BessPlanningFeaturePolicyArtifactManifest`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(<br>                "artifact manifest schema version must equal "<br>                f"{ARTIFACT_MANIFEST_SCHEMA_VERSION}"<br>            )` under lexical guard `type(self.schema_version) is not int<br>            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`.
  - `ValueError("artifact policy schema version is unsupported")` under lexical guard `type(self.policy_schema_version) is not int<br>            or self.policy_schema_version != POLICY_SCHEMA_VERSION`.
  - `ValueError("artifact result hash schema version is unsupported")` under lexical guard `type(self.result_hash_schema_version) is not int<br>            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
  - `ValueError("artifact CNIG profile schema version is unsupported")` under lexical guard `type(self.cnig_profile_schema_version) is not int<br>            or self.cnig_profile_schema_version != 2`.
  - `ValueError("artifact CNIG result hash schema version is unsupported")` under lexical guard `type(self.cnig_result_hash_schema_version) is not int<br>            or self.cnig_result_hash_schema_version != 5`.
  - `ValueError(f"{label} is invalid")` under lexical guard `type(integer_value) is not int or integer_value < minimum`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |
| `_sha256_string` | `landscout.stages.bess_planning_feature_policy._sha256_string` |
| `validate_portable_parquet_filename` | `landscout.common.artifact_paths.validate_portable_parquet_filename` |
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
def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError(
                "artifact manifest schema version must equal "
                f"{ARTIFACT_MANIFEST_SCHEMA_VERSION}"
            )
        if (
            type(self.policy_schema_version) is not int
            or self.policy_schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError("artifact policy schema version is unsupported")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("artifact result hash schema version is unsupported")
        if (
            type(self.cnig_profile_schema_version) is not int
            or self.cnig_profile_schema_version != 2
        ):
            raise ValueError("artifact CNIG profile schema version is unsupported")
        if (
            type(self.cnig_result_hash_schema_version) is not int
            or self.cnig_result_hash_schema_version != 5
        ):
            raise ValueError("artifact CNIG result hash schema version is unsupported")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.source_document_id, "source_document_id"),
            (self.cnig_profile, "cnig_profile"),
        ):
            _exact_string(exact_value, label)
        for hash_value, label in (
            (self.policy_sha256, "policy_sha256"),
            (self.source_archive_sha256, "source_archive_sha256"),
            (self.cnig_profile_sha256, "cnig_profile_sha256"),
            (
                self.cnig_complete_result_content_sha256,
                "cnig_complete_result_content_sha256",
            ),
            (self.policy_table_content_sha256, "policy_table_content_sha256"),
            (self.complete_result_content_sha256, "complete_result_content_sha256"),
            (self.parquet_sha256, "parquet_sha256"),
        ):
            _sha256_string(hash_value, label)
        for integer_value, label, allow_zero in (
            (self.parquet_row_count, "parquet_row_count", True),
            (self.parquet_size_bytes, "parquet_size_bytes", False),
        ):
            minimum = 0 if allow_zero else 1
            if type(integer_value) is not int or integer_value < minimum:
                raise ValueError(f"{label} is invalid")
        validate_portable_parquet_filename(self.parquet_filename, "parquet_filename")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_value`

**Purpose:** Implements `null value` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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
- direct call: `landscout.stages.bess_planning_feature_policy::_null_safe_equal` via `_null_value`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_null_safe_equal` via `_null_value`
- direct call: `landscout.stages.bess_planning_feature_policy::_canonical_value` via `_null_value`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_canonical_value` via `_null_value`
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_policy_table_rows` via `_null_value`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_table_rows` via `_null_value`

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

### `_null_safe_equal`

**Purpose:** Implements `null safe equal` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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
  - `normalized_left is None and normalized_right is None`
  - `bool(normalized_left == normalized_right)`
  - `False`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `_null_safe_equal`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `_null_safe_equal`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_null_value` | `landscout.stages.bess_planning_feature_policy._null_value` |
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
    normalized_left = _null_value(left)
    normalized_right = _null_value(right)
    if normalized_left is None or normalized_right is None:
        return normalized_left is None and normalized_right is None
    try:
        return bool(normalized_left == normalized_right)
    except (TypeError, ValueError):
        return False
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_value`

**Purpose:** Implements `canonical value` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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
  - `value.isoformat()`
  - `_canonical_value(value.item())`
  - `value`
  - `int(value)`
  - `number`
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>                "Policy integrity payload contains non-finite data"<br>            )` under lexical guard `isinstance(value, Real)`.
  - `BessPlanningFeaturePolicyError(<br>        f"Policy integrity payload contains unsupported {type(value).__name__}"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_canonical_value` via `_canonical_value`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_canonical_value` via `_canonical_value`
- direct call: `landscout.stages.bess_planning_feature_policy::_frame_payload` via `_canonical_value`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_frame_payload` via `_canonical_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_null_value` | `landscout.stages.bess_planning_feature_policy._null_value` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.bess_planning_feature_policy._canonical_value` |
| `value.item` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isfinite` | `math.isfinite` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _canonical_value(value: object) -> object:
    value = _null_value(value)
    if value is None:
        return None
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
            raise BessPlanningFeaturePolicyError(
                "Policy integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeaturePolicyError(
        f"Policy integrity payload contains unsupported {type(value).__name__}"
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_payload`

**Purpose:** Implements `frame payload` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

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
- direct call: `landscout.stages.bess_planning_feature_policy::_policy_table_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_table_sha256` via `_frame_payload`
- direct call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_frame_payload`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_frame_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `_canonical_value` | `landscout.stages.bess_planning_feature_policy._canonical_value` |
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

### `_validate_source_lock`

**Purpose:** Implements `validate source lock` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig` | `required` |
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>                f"Policy source lock differs from validated {label}"<br>            )` under lexical guard `configured != actual`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_validate_source_lock`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_validate_source_lock`
- direct call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_validate_source_lock`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_validate_source_lock`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |

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
def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    lock = config.source_lock
    comparisons = (
        (lock.document_id, coded_result.source_document_id, "document ID"),
        (lock.archive_sha256, coded_result.source_archive_sha256, "archive SHA256"),
        (lock.cnig_profile, coded_result.profile, "CNIG profile"),
        (
            lock.cnig_profile_schema_version,
            coded_result.profile_schema_version,
            "CNIG profile schema version",
        ),
        (lock.cnig_profile_sha256, coded_result.profile_sha256, "CNIG profile SHA256"),
        (
            lock.cnig_result_hash_schema_version,
            coded_result.result_hash_schema_version,
            "CNIG result hash schema version",
        ),
        (
            lock.cnig_complete_result_content_sha256,
            coded_result.complete_result_content_sha256,
            "CNIG complete result SHA256",
        ),
    )
    for configured, actual, label in comparisons:
        if configured != actual:
            raise BessPlanningFeaturePolicyError(
                f"Policy source lock differs from validated {label}"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_dictionary_by_pair`

**Purpose:** Implements `dictionary by pair` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `indexed`
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>                "Validated CNIG code dictionary contains a duplicate pair"<br>            )` under lexical guard `key in indexed`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `_dictionary_by_pair`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `_dictionary_by_pair`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `coded_result.code_dictionary.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |

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
| In-memory mutation | `indexed[key] = row` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    rows = coded_result.code_dictionary.to_dict("records")
    indexed: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in rows:
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in indexed:
            raise BessPlanningFeaturePolicyError(
                "Validated CNIG code dictionary contains a duplicate pair"
            )
        indexed[key] = row
    return indexed
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_policy_completeness`

**Purpose:** Implements `validate policy completeness` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig` | `required` |
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `dictionary`
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>            f"Policy is missing validated CNIG pair(s): {missing}"<br>        )` under lexical guard `missing`.
  - `BessPlanningFeaturePolicyError(<br>            f"Policy contains extra CNIG pair(s): {extra}"<br>        )` under lexical guard `extra`.
  - `BessPlanningFeaturePolicyError(<br>                f"Policy official label mismatch for pair {key}"<br>            )` under lexical guard `entry.expected_official_label != row["official_label"]`.
  - `BessPlanningFeaturePolicyError(<br>                f"Policy legal reference mismatch for pair {key}"<br>            )` under lexical guard `not _null_safe_equal(entry.expected_legal_reference, row["legal_reference"])`.
  - `BessPlanningFeaturePolicyError(<br>                f"Policy regulation reference mismatch for pair {key}"<br>            )` under lexical guard `not _null_safe_equal(<br>            entry.expected_regulation_reference,<br>            row["regulation_or_annex_reference"],<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_build_result` via `_validate_policy_completeness`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `_validate_policy_completeness`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_dictionary_by_pair` | `landscout.stages.bess_planning_feature_policy._dictionary_by_pair` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `dictionary.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_equal` | `landscout.stages.bess_planning_feature_policy._null_safe_equal` |

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
def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    dictionary = _dictionary_by_pair(coded_result)
    entries: dict[tuple[str, str, str], PolicyEntry] = {
        (entry.feature_family, entry.type_code, entry.subtype_code): entry
        for entry in config.entries
    }
    missing = sorted(set(dictionary) - set(entries))
    extra = sorted(set(entries) - set(dictionary))
    if missing:
        raise BessPlanningFeaturePolicyError(
            f"Policy is missing validated CNIG pair(s): {missing}"
        )
    if extra:
        raise BessPlanningFeaturePolicyError(
            f"Policy contains extra CNIG pair(s): {extra}"
        )
    for key, row in dictionary.items():
        entry = entries[key]
        if entry.expected_official_label != row["official_label"]:
            raise BessPlanningFeaturePolicyError(
                f"Policy official label mismatch for pair {key}"
            )
        if not _null_safe_equal(entry.expected_legal_reference, row["legal_reference"]):
            raise BessPlanningFeaturePolicyError(
                f"Policy legal reference mismatch for pair {key}"
            )
        if not _null_safe_equal(
            entry.expected_regulation_reference,
            row["regulation_or_annex_reference"],
        ):
            raise BessPlanningFeaturePolicyError(
                f"Policy regulation reference mismatch for pair {key}"
            )
    return dictionary
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_table`

**Purpose:** Implements `policy table` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig` | `required` |
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `dictionary` | positional-or-keyword | `dict[tuple[str, str, str], dict[str, object]]` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_build_result` via `_policy_table`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `_policy_table`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `output[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `output["status_priority"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `output[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `output.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `rows.append(<br>            {<br>                "feature_family": entry.feature_family,<br>                "type_code": entry.type_code,<br>                "subtype_code": entry.subtype_code,<br>                "official_label": official["official_label"],<br>                "official_legal_reference": official["legal_reference"],<br>                "official_regulation_reference": (<br>                    official["regulation_or_annex_reference"]<br>                ),<br>                "precheck_status": entry.precheck_status,<br>                "confidence": entry.confidence,<br>                "status_priority": config.status_priority[entry.precheck_status],<br>                "rationale": entry.rationale,<br>                "required_human_action": entry.required_human_action,<br>                "limitations": entry.limitations,<br>                "policy_scope": config.policy_scope,<br>                "local_feature_text_interpreted": (<br>                    config.local_feature_text_interpreted<br>                ),<br>                "local_regulation_content_interpreted": (<br>                    config.local_regulation_content_interpreted<br>                ),<br>                "legal_conclusion_produced": config.legal_conclusion_produced,<br>                "policy_profile": config.profile,<br>                "policy_sha256": policy_hash,<br>                "cnig_profile": coded_result.profile,<br>                "cnig_profile_sha256": coded_result.profile_sha256,<br>                "cnig_complete_result_content_sha256": (<br>                    coded_result.complete_result_content_sha256<br>                ),<br>            }<br>        )`<br>`output[column] = pd.array(output[column].tolist(), dtype="str")`<br>`output["status_priority"] = output["status_priority"].astype("int64")`<br>`output[column] = output[column].astype("bool")`<br>`output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for entry in config.entries:
        key = (entry.feature_family, entry.type_code, entry.subtype_code)
        official = dictionary[key]
        rows.append(
            {
                "feature_family": entry.feature_family,
                "type_code": entry.type_code,
                "subtype_code": entry.subtype_code,
                "official_label": official["official_label"],
                "official_legal_reference": official["legal_reference"],
                "official_regulation_reference": (
                    official["regulation_or_annex_reference"]
                ),
                "precheck_status": entry.precheck_status,
                "confidence": entry.confidence,
                "status_priority": config.status_priority[entry.precheck_status],
                "rationale": entry.rationale,
                "required_human_action": entry.required_human_action,
                "limitations": entry.limitations,
                "policy_scope": config.policy_scope,
                "local_feature_text_interpreted": (
                    config.local_feature_text_interpreted
                ),
                "local_regulation_content_interpreted": (
                    config.local_regulation_content_interpreted
                ),
                "legal_conclusion_produced": config.legal_conclusion_produced,
                "policy_profile": config.profile,
                "policy_sha256": policy_hash,
                "cnig_profile": coded_result.profile,
                "cnig_profile_sha256": coded_result.profile_sha256,
                "cnig_complete_result_content_sha256": (
                    coded_result.complete_result_content_sha256
                ),
            }
        )
    output = pd.DataFrame(rows, columns=POLICY_TABLE_COLUMNS)
    string_columns = tuple(
        column
        for column in POLICY_TABLE_COLUMNS
        if column
        not in {
            "status_priority",
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        }
    )
    for column in string_columns:
        output[column] = pd.array(output[column].tolist(), dtype="str")
    output["status_priority"] = output["status_priority"].astype("int64")
    for column in (
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    ):
        output[column] = output[column].astype("bool")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_component_metadata`

**Purpose:** Implements `component metadata` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "policy_schema_version": result.policy_schema_version,<br>        "result_hash_schema_version": result.result_hash_schema_version,<br>        "policy_profile": result.policy_profile,<br>        "policy_scope": result.policy_scope,<br>        "policy_sha256": result.policy_sha256,<br>        "source_document_id": result.source_document_id,<br>        "source_archive_sha256": result.source_archive_sha256,<br>        "cnig_profile": result.cnig_profile,<br>        "cnig_profile_schema_version": result.cnig_profile_schema_version,<br>        "cnig_profile_sha256": result.cnig_profile_sha256,<br>        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,<br>        "cnig_complete_result_content_sha256": (<br>            result.cnig_complete_result_content_sha256<br>        ),<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_policy_table_sha256` via `_component_metadata`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_table_sha256` via `_component_metadata`
- direct call: `landscout.stages.bess_planning_feature_policy::_complete_result_sha256` via `_component_metadata`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_complete_result_sha256` via `_component_metadata`

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
def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
    return {
        "policy_schema_version": result.policy_schema_version,
        "result_hash_schema_version": result.result_hash_schema_version,
        "policy_profile": result.policy_profile,
        "policy_scope": result.policy_scope,
        "policy_sha256": result.policy_sha256,
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_profile": result.cnig_profile,
        "cnig_profile_schema_version": result.cnig_profile_schema_version,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
    }
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_table_sha256`

**Purpose:** Implements `policy table sha256` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": "landscout.bess_cnig_feature_policy.table",<br>            **_component_metadata(result),<br>            "frame": _frame_payload(result.policy_table),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_result_with_hashes` via `_policy_table_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_result_with_hashes` via `_policy_table_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.bess_planning_feature_policy._canonical_json_sha256` |
| `_component_metadata` | `landscout.stages.bess_planning_feature_policy._component_metadata` |
| `_frame_payload` | `landscout.stages.bess_planning_feature_policy._frame_payload` |

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
def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.table",
            **_component_metadata(result),
            "frame": _frame_payload(result.policy_table),
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_complete_result_sha256`

**Purpose:** Implements `complete result sha256` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": "landscout.bess_cnig_feature_policy.result",<br>            **_component_metadata(result),<br>            "policy_table_content_sha256": result.policy_table_content_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_result_with_hashes` via `_complete_result_sha256`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_result_with_hashes` via `_complete_result_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.bess_planning_feature_policy._canonical_json_sha256` |
| `_component_metadata` | `landscout.stages.bess_planning_feature_policy._component_metadata` |

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
def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.result",
            **_component_metadata(result),
            "policy_table_content_sha256": result.policy_table_content_sha256,
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_with_hashes`

**Purpose:** Implements `result with hashes` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        component,<br>        complete_result_content_sha256=_complete_result_sha256(component),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_build_result` via `_result_with_hashes`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `_result_with_hashes`
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_result_with_hashes`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_result_with_hashes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_policy_table_sha256` | `landscout.stages.bess_planning_feature_policy._policy_table_sha256` |
| `_complete_result_sha256` | `landscout.stages.bess_planning_feature_policy._complete_result_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_policy_table_sha256`<br>`_complete_result_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
    component = replace(
        result, policy_table_content_sha256=_policy_table_sha256(result)
    )
    return replace(
        component,
        complete_result_content_sha256=_complete_result_sha256(component),
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_policy_table_rows`

**Purpose:** Implements `validate policy table rows` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>                f"policy table row {position} feature family is invalid"<br>            )` under lexical guard `family not in {"PRESCRIPTION", "INFORMATION"}`.
  - `BessPlanningFeaturePolicyError(<br>                    f"policy table row {position} {label} is invalid"<br>                )` under lexical guard `not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None`.
  - `BessPlanningFeaturePolicyError(<br>                "policy table contains a duplicate code pair"<br>            )` under lexical guard `key in records`.
  - `BessPlanningFeaturePolicyError(str(error))`.
  - `BessPlanningFeaturePolicyError(<br>                    f"{field} contains a literal null replacement"<br>                )` under lexical guard `isinstance(value, str) and value in NULL_REFERENCE_LITERALS`.
  - `BessPlanningFeaturePolicyError(str(error))`.
  - `BessPlanningFeaturePolicyError(<br>                f"policy table row {position} status is invalid"<br>            )` under lexical guard `status not in ALLOWED_STATUSES`.
  - `BessPlanningFeaturePolicyError(<br>                f"policy table row {position} confidence is invalid"<br>            )` under lexical guard `confidence not in ALLOWED_CONFIDENCES`.
  - `BessPlanningFeaturePolicyError(<br>                f"policy table row {position} priority is invalid"<br>            )` under lexical guard `type(priority) is not int or priority <= 0`.
  - `BessPlanningFeaturePolicyError(<br>                "policy table status and priority mapping is not one-to-one"<br>            )` under lexical guard `previous_status != status or previous_priority != priority`.
  - `BessPlanningFeaturePolicyError(<br>                f"policy table row {position} scope differs from result"<br>            )` under lexical guard `row["policy_scope"] != result.policy_scope`.
  - `BessPlanningFeaturePolicyError(<br>                    f"policy table row {position} {field} must be false"<br>                )` under lexical guard `row[field] is not False`.
  - `BessPlanningFeaturePolicyError(<br>                f"policy table row {position} result lineage differs"<br>            )` under lexical guard `row["policy_profile"] != result.policy_profile<br>            or row["policy_sha256"] != result.policy_sha256<br>            or row["cnig_profile"] != result.cnig_profile<br>            or row["cnig_profile_sha256"] != result.cnig_profile_sha256<br>            or row["cnig_complete_result_content_sha256"]<br>            != result.cnig_complete_result_content_sha256`.
  - `BessPlanningFeaturePolicyError("policy table pair order is not canonical")` under lexical guard `ordered_keys != sorted(ordered_keys)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_validate_policy_table_rows`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_result_envelope` via `_validate_policy_table_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `CODE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_value` | `landscout.stages.bess_planning_feature_policy._null_value` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `priority_to_status.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `status_to_priority.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `ordered_keys.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `priority_to_status.setdefault(priority, status)`<br>`status_to_priority.setdefault(status, priority)`<br>`records[key] = row`<br>`ordered_keys.append(key)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
    records: dict[tuple[str, str, str], dict[str, object]] = {}
    ordered_keys: list[tuple[str, str, str]] = []
    priority_to_status: dict[int, str] = {}
    status_to_priority: dict[str, int] = {}
    for position, row in enumerate(result.policy_table.to_dict("records")):
        family = row["feature_family"]
        type_code = row["type_code"]
        subtype_code = row["subtype_code"]
        if family not in {"PRESCRIPTION", "INFORMATION"}:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} feature family is invalid"
            )
        for value, label in (
            (type_code, "type code"),
            (subtype_code, "subtype code"),
        ):
            if not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {label} is invalid"
                )
        key = (family, type_code, subtype_code)
        if key in records:
            raise BessPlanningFeaturePolicyError(
                "policy table contains a duplicate code pair"
            )
        for field, label in (
            ("official_label", "official label"),
            ("rationale", "rationale"),
            ("required_human_action", "required human action"),
            ("limitations", "limitations"),
        ):
            try:
                _exact_string(row[field], f"policy row {position} {label}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        for field in (
            "official_legal_reference",
            "official_regulation_reference",
        ):
            value = row[field]
            if _null_value(value) is None:
                continue
            if isinstance(value, str) and value in NULL_REFERENCE_LITERALS:
                raise BessPlanningFeaturePolicyError(
                    f"{field} contains a literal null replacement"
                )
            try:
                _exact_string(value, f"policy row {position} {field}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        status = row["precheck_status"]
        confidence = row["confidence"]
        priority = row["status_priority"]
        if status not in ALLOWED_STATUSES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} status is invalid"
            )
        if confidence not in ALLOWED_CONFIDENCES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} confidence is invalid"
            )
        if type(priority) is not int or priority <= 0:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} priority is invalid"
            )
        previous_status = priority_to_status.setdefault(priority, status)
        previous_priority = status_to_priority.setdefault(status, priority)
        if previous_status != status or previous_priority != priority:
            raise BessPlanningFeaturePolicyError(
                "policy table status and priority mapping is not one-to-one"
            )
        if row["policy_scope"] != result.policy_scope:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} scope differs from result"
            )
        for field in (
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        ):
            if row[field] is not False:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {field} must be false"
                )
        if (
            row["policy_profile"] != result.policy_profile
            or row["policy_sha256"] != result.policy_sha256
            or row["cnig_profile"] != result.cnig_profile
            or row["cnig_profile_sha256"] != result.cnig_profile_sha256
            or row["cnig_complete_result_content_sha256"]
            != result.cnig_complete_result_content_sha256
        ):
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} result lineage differs"
            )
        records[key] = row
        ordered_keys.append(key)
    if ordered_keys != sorted(ordered_keys):
        raise BessPlanningFeaturePolicyError("policy table pair order is not canonical")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_result`

**Purpose:** Implements `build result` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `BessPlanningFeaturePolicyConfig` | `required` |
| `coded_result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_result_with_hashes(result)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_build_result`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_build_result`
- direct call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_build_result`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_build_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_policy_completeness` | `landscout.stages.bess_planning_feature_policy._validate_policy_completeness` |
| `_policy_sha256` | `landscout.stages.bess_planning_feature_policy._policy_sha256` |
| `BessPlanningFeaturePolicyResult` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult` |
| `_policy_table` | `landscout.stages.bess_planning_feature_policy._policy_table` |
| `_result_with_hashes` | `landscout.stages.bess_planning_feature_policy._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_policy_sha256`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
    dictionary = _validate_policy_completeness(config, coded_result)
    policy_hash = _policy_sha256(config)
    result = BessPlanningFeaturePolicyResult(
        policy_schema_version=config.schema_version,
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        policy_profile=config.profile,
        policy_scope=config.policy_scope,
        policy_sha256=policy_hash,
        source_document_id=coded_result.source_document_id,
        source_archive_sha256=coded_result.source_archive_sha256,
        cnig_profile=coded_result.profile,
        cnig_profile_schema_version=coded_result.profile_schema_version,
        cnig_profile_sha256=coded_result.profile_sha256,
        cnig_result_hash_schema_version=coded_result.result_hash_schema_version,
        cnig_complete_result_content_sha256=(
            coded_result.complete_result_content_sha256
        ),
        policy_table_content_sha256="",
        complete_result_content_sha256="",
        policy_table=_policy_table(config, coded_result, dictionary, policy_hash),
    )
    return _result_with_hashes(result)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result_envelope`

**Purpose:** Implements `validate result envelope` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>            "result must be a BessPlanningFeaturePolicyResult"<br>        )` under lexical guard `type(result) is not BessPlanningFeaturePolicyResult`.
  - `BessPlanningFeaturePolicyError(f"unsupported {label} version")` under lexical guard `type(version) is not int or version != expected`.
  - `BessPlanningFeaturePolicyError("result policy scope is invalid")` under lexical guard `result.policy_scope != POLICY_SCOPE`.
  - `BessPlanningFeaturePolicyError(str(error))`.
  - `BessPlanningFeaturePolicyError("policy table must be a DataFrame")` under lexical guard `not isinstance(result.policy_table, pd.DataFrame) or isinstance(<br>        result.policy_table, gpd.GeoDataFrame<br>    )`.
  - `BessPlanningFeaturePolicyError("policy table schema is invalid")` under lexical guard `result.policy_table.columns.duplicated().any()<br>        or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS`.
  - `BessPlanningFeaturePolicyError("policy table schema is invalid")` under lexical guard `deterministic_frame_schema_signature(result.policy_table)<br>        != POLICY_TABLE_SCHEMA_SIGNATURE`.
  - `BessPlanningFeaturePolicyError(<br>            "policy table must contain at least one policy entry"<br>        )` under lexical guard `result.policy_table.empty`.
  - `BessPlanningFeaturePolicyError(str(error))`.
  - `BessPlanningFeaturePolicyError("policy table hash is invalid")` under lexical guard `result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256`.
  - `BessPlanningFeaturePolicyError("complete result hash is invalid")` under lexical guard `result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result_envelope` via `_validate_result_envelope`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result_envelope` via `_validate_result_envelope`
- direct call: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `_validate_result_envelope`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_artifacts` via `_validate_result_envelope`
- direct call: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_validate_result_envelope`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_validate_result_envelope`
- direct call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_validate_result_envelope`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_validate_result_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `_exact_string` | `landscout.stages.bess_planning_feature_policy._exact_string` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `field.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_sha256_string` | `landscout.stages.bess_planning_feature_policy._sha256_string` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_policy_table_rows` | `landscout.stages.bess_planning_feature_policy._validate_policy_table_rows` |
| `_result_with_hashes` | `landscout.stages.bess_planning_feature_policy._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_sha256_string`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
    if type(result) is not BessPlanningFeaturePolicyResult:
        raise BessPlanningFeaturePolicyError(
            "result must be a BessPlanningFeaturePolicyResult"
        )
    for version, expected, label in (
        (result.policy_schema_version, POLICY_SCHEMA_VERSION, "policy schema"),
        (
            result.result_hash_schema_version,
            RESULT_HASH_SCHEMA_VERSION,
            "result hash schema",
        ),
        (result.cnig_profile_schema_version, 2, "CNIG profile schema"),
        (result.cnig_result_hash_schema_version, 5, "CNIG result hash schema"),
    ):
        if type(version) is not int or version != expected:
            raise BessPlanningFeaturePolicyError(f"unsupported {label} version")
    if result.policy_scope != POLICY_SCOPE:
        raise BessPlanningFeaturePolicyError("result policy scope is invalid")
    for value, label in (
        (result.policy_profile, "policy profile"),
        (result.source_document_id, "source document ID"),
        (result.cnig_profile, "CNIG profile"),
    ):
        try:
            _exact_string(value, label)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    if not isinstance(result.policy_table, pd.DataFrame) or isinstance(
        result.policy_table, gpd.GeoDataFrame
    ):
        raise BessPlanningFeaturePolicyError("policy table must be a DataFrame")
    if (
        result.policy_table.columns.duplicated().any()
        or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if (
        deterministic_frame_schema_signature(result.policy_table)
        != POLICY_TABLE_SCHEMA_SIGNATURE
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if result.policy_table.empty:
        raise BessPlanningFeaturePolicyError(
            "policy table must contain at least one policy entry"
        )
    for field in POLICY_RESULT_SCALAR_FIELDS:
        if not field.endswith("_sha256"):
            continue
        try:
            _sha256_string(getattr(result, field), field)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    _validate_policy_table_rows(result)
    rebuilt = _result_with_hashes(result)
    if result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256:
        raise BessPlanningFeaturePolicyError("policy table hash is invalid")
    if result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256:
        raise BessPlanningFeaturePolicyError("complete result hash is invalid")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_bess_planning_feature_policy_result_envelope`

**Purpose:** Validate one compiled-policy envelope without rebuilding CNIG sources.

**Exact signature**

```python
def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `re-raise`.
  - `BessPlanningFeaturePolicyError(<br>            "BESS planning-feature policy result envelope is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `validate_bess_planning_feature_policy_result_envelope`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `validate_bess_planning_feature_policy_result_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_envelope` | `landscout.stages.bess_planning_feature_policy._validate_result_envelope` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |

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
def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Validate one compiled-policy envelope without rebuilding CNIG sources."""

    try:
        _validate_result_envelope(result)
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS planning-feature policy result envelope is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `load_bess_planning_feature_policy_artifacts`

**Purpose:** Load and locally validate one physically sealed compiled-policy artifact.

**Exact signature**

```python
def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parquet_path` | positional-or-keyword | `str \| Path` | `required` |
| `manifest_path` | positional-or-keyword | `str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>                "Artifact manifest Parquet filename differs from the supplied file"<br>            )` under lexical guard `manifest.parquet_filename != parquet.name`.
  - `BessPlanningFeaturePolicyError(<br>                "Artifact manifest Parquet size differs from the supplied file"<br>            )` under lexical guard `len(parquet_payload) != manifest.parquet_size_bytes`.
  - `BessPlanningFeaturePolicyError(<br>                "Artifact manifest Parquet SHA256 differs from the supplied file"<br>            )` under lexical guard `sha256(parquet_payload).hexdigest() != manifest.parquet_sha256`.
  - `BessPlanningFeaturePolicyError(<br>                "Artifact manifest Parquet row count differs from the supplied file"<br>            )` under lexical guard `len(table) != manifest.parquet_row_count`.
  - `BessPlanningFeaturePolicyError(<br>                "Artifact manifest policy-table schema differs from the supplied file"<br>            )` under lexical guard `actual_schema != declared_schema`.
  - `re-raise`.
  - `BessPlanningFeaturePolicyError(<br>            f"BESS CNIG feature policy artifacts are invalid: {error}"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `loads_strict_json_object` | `landscout.common.strict_json.loads_strict_json_object` |
| `manifest_file.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyArtifactManifest.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.model_validate` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `parquet.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(parquet_payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `pd.read_parquet` | `pandas.read_parquet` |
| `BytesIO` | `io.BytesIO` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `manifest.policy_table_schema_signature.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyResult` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_result_envelope` | `landscout.stages.bess_planning_feature_policy._validate_result_envelope` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `manifest_file.read_bytes`<br>`parquet.read_bytes`<br>`pd.read_parquet` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(parquet_payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Load and locally validate one physically sealed compiled-policy artifact."""

    try:
        parquet = Path(parquet_path)
        manifest_file = Path(manifest_path)
        payload = loads_strict_json_object(manifest_file.read_bytes())
        manifest = BessPlanningFeaturePolicyArtifactManifest.model_validate(payload)
        if manifest.parquet_filename != parquet.name:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet filename differs from the supplied file"
            )
        parquet_payload = parquet.read_bytes()
        if len(parquet_payload) != manifest.parquet_size_bytes:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet size differs from the supplied file"
            )
        if sha256(parquet_payload).hexdigest() != manifest.parquet_sha256:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet SHA256 differs from the supplied file"
            )
        table = pd.read_parquet(BytesIO(parquet_payload))
        if len(table) != manifest.parquet_row_count:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet row count differs from the supplied file"
            )
        actual_schema = deterministic_frame_schema_signature(table)
        declared_schema = manifest.policy_table_schema_signature.model_dump(mode="json")
        if actual_schema != declared_schema:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest policy-table schema differs from the supplied file"
            )
        result = BessPlanningFeaturePolicyResult(
            **{name: getattr(manifest, name) for name in POLICY_RESULT_SCALAR_FIELDS},
            policy_table=table,
        )
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            f"BESS CNIG feature policy artifacts are invalid: {error}"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_coded_source`

**Purpose:** Implements `validate coded source` within the file role: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

**Exact signature**

```python
def _validate_coded_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
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

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>            "Source-complete CNIG result validation failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_validate_coded_source`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `_validate_coded_source`
- direct call: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_validate_coded_source`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `_validate_coded_source`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |

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
def _validate_coded_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    try:
        validate_planning_feature_code_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "Source-complete CNIG result validation failed"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `compile_bess_planning_feature_policy`

**Purpose:** Compile the exact source-locked policy without applying it to features.

**Exact signature**

```python
def compile_bess_planning_feature_policy(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyResult`.

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

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `re-raise`.
  - `BessPlanningFeaturePolicyError(<br>            "BESS CNIG feature policy compilation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- direct call: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `compile_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `compile_bess_planning_feature_policy`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_source_lock_mismatch_is_rejected` via `compile_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_source_lock_mismatch_is_rejected` via `compile_bess_planning_feature_policy`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `compile_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `compile_bess_planning_feature_policy`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `compile_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `compile_bess_planning_feature_policy`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `compile_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `compile_bess_planning_feature_policy`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `compile_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `compile_bess_planning_feature_policy`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_in_memory_config_is_revalidated_before_compilation` via `compile_bess_planning_feature_policy`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_in_memory_config_is_revalidated_before_compilation` via `compile_bess_planning_feature_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_resolved_policy_config` | `landscout.stages.bess_planning_feature_policy._resolved_policy_config` |
| `_validate_source_lock` | `landscout.stages.bess_planning_feature_policy._validate_source_lock` |
| `_validate_coded_source` | `landscout.stages.bess_planning_feature_policy._validate_coded_source` |
| `_build_result` | `landscout.stages.bess_planning_feature_policy._build_result` |
| `_validate_result_envelope` | `landscout.stages.bess_planning_feature_policy._validate_result_envelope` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |

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
def compile_bess_planning_feature_policy(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Compile the exact source-locked policy without applying it to features."""

    try:
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        result = _build_result(config, coded_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy compilation failed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_bess_planning_feature_policy_result`

**Purpose:** Rebuild and validate a normalized policy from every factual source input.

**Exact signature**

```python
def validate_bess_planning_feature_policy_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    result: BessPlanningFeaturePolicyResult,
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
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessPlanningFeaturePolicyError(<br>                    f"result {field} differs from rebuilt policy"<br>                )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `BessPlanningFeaturePolicyError(<br>                "policy table differs from rebuilt policy"<br>            )` under lexical guard `_frame_payload(result.policy_table) != _frame_payload(expected.policy_table)`.
  - `re-raise`.
  - `BessPlanningFeaturePolicyError(<br>            "BESS CNIG feature policy result validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `validate_bess_planning_feature_policy_result`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `validate_bess_planning_feature_policy_result`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status` via `validate_bess_planning_feature_policy_result`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status` via `validate_bess_planning_feature_policy_result`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_table_mutation_is_rejected` via `validate_bess_planning_feature_policy_result`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_table_mutation_is_rejected` via `validate_bess_planning_feature_policy_result`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `validate_bess_planning_feature_policy_result`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `validate_bess_planning_feature_policy_result`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_persisted_parquet_and_json_readback_is_source_complete` via `validate_bess_planning_feature_policy_result`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_persisted_parquet_and_json_readback_is_source_complete` via `validate_bess_planning_feature_policy_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_envelope` | `landscout.stages.bess_planning_feature_policy._validate_result_envelope` |
| `_resolved_policy_config` | `landscout.stages.bess_planning_feature_policy._resolved_policy_config` |
| `_validate_source_lock` | `landscout.stages.bess_planning_feature_policy._validate_source_lock` |
| `_validate_coded_source` | `landscout.stages.bess_planning_feature_policy._validate_coded_source` |
| `_build_result` | `landscout.stages.bess_planning_feature_policy._build_result` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `_frame_payload` | `landscout.stages.bess_planning_feature_policy._frame_payload` |

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
def validate_bess_planning_feature_policy_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Rebuild and validate a normalized policy from every factual source input."""

    try:
        _validate_result_envelope(result)
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        expected = _build_result(config, coded_result)
        for field in POLICY_RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeaturePolicyError(
                    f"result {field} differs from rebuilt policy"
                )
        if _frame_payload(result.policy_table) != _frame_payload(expected.policy_table):
            raise BessPlanningFeaturePolicyError(
                "policy table differs from rebuilt policy"
            )
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy result validation failed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `POLICY_SCHEMA_VERSION`, `RESULT_HASH_SCHEMA_VERSION`, `ARTIFACT_MANIFEST_SCHEMA_VERSION`, `POLICY_TABLE_COLUMNS`, `POLICY_TABLE_DTYPES`, `POLICY_TABLE_SCHEMA_SIGNATURE`, `POLICY_RESULT_SCALAR_FIELDS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `BessPlanningFeaturePolicyArtifactManifest` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest` |
| `BessPlanningFeaturePolicyConfig` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig` |
| `BessPlanningFeaturePolicyError` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError` |
| `BessPlanningFeaturePolicyResult` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |
| `load_bess_planning_feature_policy_artifacts` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_artifacts` |
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `validate_bess_planning_feature_policy_result` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` |
| `validate_bess_planning_feature_policy_result_envelope` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result_envelope` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Compile a source-locked BESS policy for official CNIG feature-code meanings."""

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

from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.immutable_mapping import freeze_mapping
from landscout.common.strict_json import loads_strict_json_object
from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)

__all__ = [
    "BessPlanningFeaturePolicyArtifactManifest",
    "BessPlanningFeaturePolicyConfig",
    "BessPlanningFeaturePolicyError",
    "BessPlanningFeaturePolicyResult",
    "compile_bess_planning_feature_policy",
    "load_bess_planning_feature_policy_artifacts",
    "load_bess_planning_feature_policy_config",
    "validate_bess_planning_feature_policy_result",
    "validate_bess_planning_feature_policy_result_envelope",
]

POLICY_SCHEMA_VERSION = 1
RESULT_HASH_SCHEMA_VERSION = 1
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
PrecheckStatus = Literal[
    "LIKELY_MATERIAL_CONSTRAINT",
    "MATERIAL_REVIEW_REQUIRED",
    "DESIGN_REVIEW_REQUIRED",
    "CONTEXT_REVIEW_REQUIRED",
    "UNKNOWN",
]
Confidence = Literal["HIGH", "MEDIUM", "LOW"]

ALLOWED_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
CODE_PATTERN = re.compile(r"[0-9]{2}")
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")

POLICY_TABLE_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "official_legal_reference",
    "official_regulation_reference",
    "precheck_status",
    "confidence",
    "status_priority",
    "rationale",
    "required_human_action",
    "limitations",
    "policy_scope",
    "local_feature_text_interpreted",
    "local_regulation_content_interpreted",
    "legal_conclusion_produced",
    "policy_profile",
    "policy_sha256",
    "cnig_profile",
    "cnig_profile_sha256",
    "cnig_complete_result_content_sha256",
)
POLICY_TABLE_DTYPES = tuple(
    "int64"
    if column == "status_priority"
    else "bool"
    if column
    in {
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    }
    else "str"
    for column in POLICY_TABLE_COLUMNS
)
POLICY_TABLE_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(POLICY_TABLE_COLUMNS),
    "dtypes": list(POLICY_TABLE_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
POLICY_RESULT_SCALAR_FIELDS = (
    "policy_schema_version",
    "result_hash_schema_version",
    "policy_profile",
    "policy_scope",
    "policy_sha256",
    "source_document_id",
    "source_archive_sha256",
    "cnig_profile",
    "cnig_profile_schema_version",
    "cnig_profile_sha256",
    "cnig_result_hash_schema_version",
    "cnig_complete_result_content_sha256",
    "policy_table_content_sha256",
    "complete_result_content_sha256",
)


class BessPlanningFeaturePolicyError(ValueError):
    """Raised when the official-code BESS policy cannot be proven exact."""


class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class PolicyTableSchemaSignature(_StrictPolicyModel):
    """Immutable persisted schema identity for the normalized policy table."""

    columns: tuple[StrictStr, ...]
    dtypes: tuple[StrictStr, ...]
    index_class: StrictStr
    index_names: tuple[StrictStr | None, ...]
    index_level_dtypes: tuple[StrictStr, ...]


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(
            f"{label} must be an exact non-empty string without edge whitespace"
        )
    return value


def _optional_exact_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _exact_string(value, label)


def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text


class PolicySourceLock(_StrictPolicyModel):
    document_id: StrictStr
    archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr

    @model_validator(mode="after")
    def _validate_lock(self) -> PolicySourceLock:
        _exact_string(self.document_id, "document_id")
        _sha256_string(self.archive_sha256, "archive_sha256")
        _exact_string(self.cnig_profile, "cnig_profile")
        _sha256_string(self.cnig_profile_sha256, "cnig_profile_sha256")
        _sha256_string(
            self.cnig_complete_result_content_sha256,
            "cnig_complete_result_content_sha256",
        )
        for value, label in (
            (self.cnig_profile_schema_version, "cnig_profile_schema_version"),
            (self.cnig_result_hash_schema_version, "cnig_result_hash_schema_version"),
        ):
            if type(value) is not int or value < 1:
                raise ValueError(f"{label} must be a strict positive integer")
        return self


class PolicyEntry(_StrictPolicyModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    expected_official_label: StrictStr
    expected_legal_reference: StrictStr | None
    expected_regulation_reference: StrictStr | None
    precheck_status: PrecheckStatus
    confidence: Confidence
    rationale: StrictStr
    required_human_action: StrictStr
    limitations: StrictStr

    @model_validator(mode="after")
    def _validate_entry(self) -> PolicyEntry:
        if CODE_PATTERN.fullmatch(self.type_code) is None:
            raise ValueError("type_code must be an exact two-character digit string")
        if CODE_PATTERN.fullmatch(self.subtype_code) is None:
            raise ValueError("subtype_code must be an exact two-character digit string")
        _exact_string(self.expected_official_label, "expected_official_label")
        _optional_exact_string(
            self.expected_legal_reference, "expected_legal_reference"
        )
        _optional_exact_string(
            self.expected_regulation_reference,
            "expected_regulation_reference",
        )
        _exact_string(self.rationale, "rationale")
        _exact_string(self.required_human_action, "required_human_action")
        _exact_string(self.limitations, "limitations")
        return self


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
        raise BessPlanningFeaturePolicyError(
            "Policy integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
    return _canonical_json_sha256([entry.model_dump(mode="json") for entry in entries])


class BessPlanningFeaturePolicyConfig(_StrictPolicyModel):
    schema_version: StrictInt
    profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    source_lock: PolicySourceLock
    status_priority: dict[PrecheckStatus, StrictInt]
    canonical_policy_entries_sha256: StrictStr
    entries: tuple[PolicyEntry, ...]

    @model_validator(mode="after")
    def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
        if (
            type(self.schema_version) is not int
            or self.schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError(
                f"policy schema version must equal {POLICY_SCHEMA_VERSION}"
            )
        _exact_string(self.profile, "profile")
        if self.policy_scope != POLICY_SCOPE:
            raise ValueError("policy_scope is unsupported")
        if (
            self.local_feature_text_interpreted is not False
            or self.local_regulation_content_interpreted is not False
            or self.legal_conclusion_produced is not False
        ):
            raise ValueError(
                "policy interpretation and legal-conclusion flags must be false"
            )
        if set(self.status_priority) != ALLOWED_STATUSES:
            raise ValueError(
                "status priority must contain every allowed status exactly once"
            )
        priorities = list(self.status_priority.values())
        if any(type(value) is not int or value <= 0 for value in priorities):
            raise ValueError("status priority values must be strict positive integers")
        if len(set(priorities)) != len(priorities):
            raise ValueError("status priority values must be unique")
        keys = [
            (entry.feature_family, entry.type_code, entry.subtype_code)
            for entry in self.entries
        ]
        if len(keys) != len(set(keys)):
            raise ValueError(
                "policy entries contain a duplicate family/type/subtype pair"
            )
        if keys != sorted(keys):
            raise ValueError(
                "policy entries must use deterministic family/type/subtype order"
            )
        _sha256_string(
            self.canonical_policy_entries_sha256,
            "canonical_policy_entries_sha256",
        )
        if _policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256:
            raise ValueError(
                "canonical policy-entry SHA256 differs from policy entries"
            )
        object.__setattr__(
            self, "status_priority", freeze_mapping(self.status_priority)
        )
        return self


def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
    """Load a strict offline BESS policy for official CNIG feature-code pairs."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise BessPlanningFeaturePolicyError("BESS CNIG policy must be a mapping")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except BessPlanningFeaturePolicyError:
        raise
    except StrictYamlError as error:
        raise BessPlanningFeaturePolicyError(str(error)) from error
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy is invalid"
        ) from error


def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
    if not isinstance(config, BessPlanningFeaturePolicyConfig):
        return load_bess_planning_feature_policy_config(config)
    try:
        payload = config.model_dump(mode="python", warnings="error")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "in-memory BESS planning-feature policy config is invalid"
        ) from error


def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
    return _canonical_json_sha256(config.model_dump(mode="json"))


@dataclass(frozen=True)
class BessPlanningFeaturePolicyResult:
    """Immutable normalized policy table and its source-complete hash envelope."""

    policy_schema_version: int
    result_hash_schema_version: int
    policy_profile: str
    policy_scope: str
    policy_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_schema_version: int
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    policy_table_content_sha256: str
    complete_result_content_sha256: str
    policy_table: pd.DataFrame


class BessPlanningFeaturePolicyArtifactManifest(_StrictPolicyModel):
    """Strict physical binding between one policy table and its hash envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_CNIG_FEATURE_POLICY_RESULT"]
    policy_schema_version: StrictInt
    result_hash_schema_version: StrictInt
    policy_profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    policy_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    policy_table_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    parquet_filename: StrictStr
    parquet_row_count: StrictInt
    parquet_size_bytes: StrictInt
    parquet_sha256: StrictStr
    policy_table_schema_signature: PolicyTableSchemaSignature

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError(
                "artifact manifest schema version must equal "
                f"{ARTIFACT_MANIFEST_SCHEMA_VERSION}"
            )
        if (
            type(self.policy_schema_version) is not int
            or self.policy_schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError("artifact policy schema version is unsupported")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("artifact result hash schema version is unsupported")
        if (
            type(self.cnig_profile_schema_version) is not int
            or self.cnig_profile_schema_version != 2
        ):
            raise ValueError("artifact CNIG profile schema version is unsupported")
        if (
            type(self.cnig_result_hash_schema_version) is not int
            or self.cnig_result_hash_schema_version != 5
        ):
            raise ValueError("artifact CNIG result hash schema version is unsupported")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.source_document_id, "source_document_id"),
            (self.cnig_profile, "cnig_profile"),
        ):
            _exact_string(exact_value, label)
        for hash_value, label in (
            (self.policy_sha256, "policy_sha256"),
            (self.source_archive_sha256, "source_archive_sha256"),
            (self.cnig_profile_sha256, "cnig_profile_sha256"),
            (
                self.cnig_complete_result_content_sha256,
                "cnig_complete_result_content_sha256",
            ),
            (self.policy_table_content_sha256, "policy_table_content_sha256"),
            (self.complete_result_content_sha256, "complete_result_content_sha256"),
            (self.parquet_sha256, "parquet_sha256"),
        ):
            _sha256_string(hash_value, label)
        for integer_value, label, allow_zero in (
            (self.parquet_row_count, "parquet_row_count", True),
            (self.parquet_size_bytes, "parquet_size_bytes", False),
        ):
            minimum = 0 if allow_zero else 1
            if type(integer_value) is not int or integer_value < minimum:
                raise ValueError(f"{label} is invalid")
        validate_portable_parquet_filename(self.parquet_filename, "parquet_filename")
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


def _null_safe_equal(left: object, right: object) -> bool:
    normalized_left = _null_value(left)
    normalized_right = _null_value(right)
    if normalized_left is None or normalized_right is None:
        return normalized_left is None and normalized_right is None
    try:
        return bool(normalized_left == normalized_right)
    except (TypeError, ValueError):
        return False


def _canonical_value(value: object) -> object:
    value = _null_value(value)
    if value is None:
        return None
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
            raise BessPlanningFeaturePolicyError(
                "Policy integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeaturePolicyError(
        f"Policy integrity payload contains unsupported {type(value).__name__}"
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


def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    lock = config.source_lock
    comparisons = (
        (lock.document_id, coded_result.source_document_id, "document ID"),
        (lock.archive_sha256, coded_result.source_archive_sha256, "archive SHA256"),
        (lock.cnig_profile, coded_result.profile, "CNIG profile"),
        (
            lock.cnig_profile_schema_version,
            coded_result.profile_schema_version,
            "CNIG profile schema version",
        ),
        (lock.cnig_profile_sha256, coded_result.profile_sha256, "CNIG profile SHA256"),
        (
            lock.cnig_result_hash_schema_version,
            coded_result.result_hash_schema_version,
            "CNIG result hash schema version",
        ),
        (
            lock.cnig_complete_result_content_sha256,
            coded_result.complete_result_content_sha256,
            "CNIG complete result SHA256",
        ),
    )
    for configured, actual, label in comparisons:
        if configured != actual:
            raise BessPlanningFeaturePolicyError(
                f"Policy source lock differs from validated {label}"
            )


def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    rows = coded_result.code_dictionary.to_dict("records")
    indexed: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in rows:
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in indexed:
            raise BessPlanningFeaturePolicyError(
                "Validated CNIG code dictionary contains a duplicate pair"
            )
        indexed[key] = row
    return indexed


def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    dictionary = _dictionary_by_pair(coded_result)
    entries: dict[tuple[str, str, str], PolicyEntry] = {
        (entry.feature_family, entry.type_code, entry.subtype_code): entry
        for entry in config.entries
    }
    missing = sorted(set(dictionary) - set(entries))
    extra = sorted(set(entries) - set(dictionary))
    if missing:
        raise BessPlanningFeaturePolicyError(
            f"Policy is missing validated CNIG pair(s): {missing}"
        )
    if extra:
        raise BessPlanningFeaturePolicyError(
            f"Policy contains extra CNIG pair(s): {extra}"
        )
    for key, row in dictionary.items():
        entry = entries[key]
        if entry.expected_official_label != row["official_label"]:
            raise BessPlanningFeaturePolicyError(
                f"Policy official label mismatch for pair {key}"
            )
        if not _null_safe_equal(entry.expected_legal_reference, row["legal_reference"]):
            raise BessPlanningFeaturePolicyError(
                f"Policy legal reference mismatch for pair {key}"
            )
        if not _null_safe_equal(
            entry.expected_regulation_reference,
            row["regulation_or_annex_reference"],
        ):
            raise BessPlanningFeaturePolicyError(
                f"Policy regulation reference mismatch for pair {key}"
            )
    return dictionary


def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for entry in config.entries:
        key = (entry.feature_family, entry.type_code, entry.subtype_code)
        official = dictionary[key]
        rows.append(
            {
                "feature_family": entry.feature_family,
                "type_code": entry.type_code,
                "subtype_code": entry.subtype_code,
                "official_label": official["official_label"],
                "official_legal_reference": official["legal_reference"],
                "official_regulation_reference": (
                    official["regulation_or_annex_reference"]
                ),
                "precheck_status": entry.precheck_status,
                "confidence": entry.confidence,
                "status_priority": config.status_priority[entry.precheck_status],
                "rationale": entry.rationale,
                "required_human_action": entry.required_human_action,
                "limitations": entry.limitations,
                "policy_scope": config.policy_scope,
                "local_feature_text_interpreted": (
                    config.local_feature_text_interpreted
                ),
                "local_regulation_content_interpreted": (
                    config.local_regulation_content_interpreted
                ),
                "legal_conclusion_produced": config.legal_conclusion_produced,
                "policy_profile": config.profile,
                "policy_sha256": policy_hash,
                "cnig_profile": coded_result.profile,
                "cnig_profile_sha256": coded_result.profile_sha256,
                "cnig_complete_result_content_sha256": (
                    coded_result.complete_result_content_sha256
                ),
            }
        )
    output = pd.DataFrame(rows, columns=POLICY_TABLE_COLUMNS)
    string_columns = tuple(
        column
        for column in POLICY_TABLE_COLUMNS
        if column
        not in {
            "status_priority",
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        }
    )
    for column in string_columns:
        output[column] = pd.array(output[column].tolist(), dtype="str")
    output["status_priority"] = output["status_priority"].astype("int64")
    for column in (
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    ):
        output[column] = output[column].astype("bool")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output


def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
    return {
        "policy_schema_version": result.policy_schema_version,
        "result_hash_schema_version": result.result_hash_schema_version,
        "policy_profile": result.policy_profile,
        "policy_scope": result.policy_scope,
        "policy_sha256": result.policy_sha256,
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_profile": result.cnig_profile,
        "cnig_profile_schema_version": result.cnig_profile_schema_version,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
    }


def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.table",
            **_component_metadata(result),
            "frame": _frame_payload(result.policy_table),
        }
    )


def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.result",
            **_component_metadata(result),
            "policy_table_content_sha256": result.policy_table_content_sha256,
        }
    )


def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
    component = replace(
        result, policy_table_content_sha256=_policy_table_sha256(result)
    )
    return replace(
        component,
        complete_result_content_sha256=_complete_result_sha256(component),
    )


def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
    records: dict[tuple[str, str, str], dict[str, object]] = {}
    ordered_keys: list[tuple[str, str, str]] = []
    priority_to_status: dict[int, str] = {}
    status_to_priority: dict[str, int] = {}
    for position, row in enumerate(result.policy_table.to_dict("records")):
        family = row["feature_family"]
        type_code = row["type_code"]
        subtype_code = row["subtype_code"]
        if family not in {"PRESCRIPTION", "INFORMATION"}:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} feature family is invalid"
            )
        for value, label in (
            (type_code, "type code"),
            (subtype_code, "subtype code"),
        ):
            if not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {label} is invalid"
                )
        key = (family, type_code, subtype_code)
        if key in records:
            raise BessPlanningFeaturePolicyError(
                "policy table contains a duplicate code pair"
            )
        for field, label in (
            ("official_label", "official label"),
            ("rationale", "rationale"),
            ("required_human_action", "required human action"),
            ("limitations", "limitations"),
        ):
            try:
                _exact_string(row[field], f"policy row {position} {label}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        for field in (
            "official_legal_reference",
            "official_regulation_reference",
        ):
            value = row[field]
            if _null_value(value) is None:
                continue
            if isinstance(value, str) and value in NULL_REFERENCE_LITERALS:
                raise BessPlanningFeaturePolicyError(
                    f"{field} contains a literal null replacement"
                )
            try:
                _exact_string(value, f"policy row {position} {field}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        status = row["precheck_status"]
        confidence = row["confidence"]
        priority = row["status_priority"]
        if status not in ALLOWED_STATUSES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} status is invalid"
            )
        if confidence not in ALLOWED_CONFIDENCES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} confidence is invalid"
            )
        if type(priority) is not int or priority <= 0:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} priority is invalid"
            )
        previous_status = priority_to_status.setdefault(priority, status)
        previous_priority = status_to_priority.setdefault(status, priority)
        if previous_status != status or previous_priority != priority:
            raise BessPlanningFeaturePolicyError(
                "policy table status and priority mapping is not one-to-one"
            )
        if row["policy_scope"] != result.policy_scope:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} scope differs from result"
            )
        for field in (
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        ):
            if row[field] is not False:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {field} must be false"
                )
        if (
            row["policy_profile"] != result.policy_profile
            or row["policy_sha256"] != result.policy_sha256
            or row["cnig_profile"] != result.cnig_profile
            or row["cnig_profile_sha256"] != result.cnig_profile_sha256
            or row["cnig_complete_result_content_sha256"]
            != result.cnig_complete_result_content_sha256
        ):
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} result lineage differs"
            )
        records[key] = row
        ordered_keys.append(key)
    if ordered_keys != sorted(ordered_keys):
        raise BessPlanningFeaturePolicyError("policy table pair order is not canonical")


def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
    dictionary = _validate_policy_completeness(config, coded_result)
    policy_hash = _policy_sha256(config)
    result = BessPlanningFeaturePolicyResult(
        policy_schema_version=config.schema_version,
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        policy_profile=config.profile,
        policy_scope=config.policy_scope,
        policy_sha256=policy_hash,
        source_document_id=coded_result.source_document_id,
        source_archive_sha256=coded_result.source_archive_sha256,
        cnig_profile=coded_result.profile,
        cnig_profile_schema_version=coded_result.profile_schema_version,
        cnig_profile_sha256=coded_result.profile_sha256,
        cnig_result_hash_schema_version=coded_result.result_hash_schema_version,
        cnig_complete_result_content_sha256=(
            coded_result.complete_result_content_sha256
        ),
        policy_table_content_sha256="",
        complete_result_content_sha256="",
        policy_table=_policy_table(config, coded_result, dictionary, policy_hash),
    )
    return _result_with_hashes(result)


def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
    if type(result) is not BessPlanningFeaturePolicyResult:
        raise BessPlanningFeaturePolicyError(
            "result must be a BessPlanningFeaturePolicyResult"
        )
    for version, expected, label in (
        (result.policy_schema_version, POLICY_SCHEMA_VERSION, "policy schema"),
        (
            result.result_hash_schema_version,
            RESULT_HASH_SCHEMA_VERSION,
            "result hash schema",
        ),
        (result.cnig_profile_schema_version, 2, "CNIG profile schema"),
        (result.cnig_result_hash_schema_version, 5, "CNIG result hash schema"),
    ):
        if type(version) is not int or version != expected:
            raise BessPlanningFeaturePolicyError(f"unsupported {label} version")
    if result.policy_scope != POLICY_SCOPE:
        raise BessPlanningFeaturePolicyError("result policy scope is invalid")
    for value, label in (
        (result.policy_profile, "policy profile"),
        (result.source_document_id, "source document ID"),
        (result.cnig_profile, "CNIG profile"),
    ):
        try:
            _exact_string(value, label)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    if not isinstance(result.policy_table, pd.DataFrame) or isinstance(
        result.policy_table, gpd.GeoDataFrame
    ):
        raise BessPlanningFeaturePolicyError("policy table must be a DataFrame")
    if (
        result.policy_table.columns.duplicated().any()
        or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if (
        deterministic_frame_schema_signature(result.policy_table)
        != POLICY_TABLE_SCHEMA_SIGNATURE
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if result.policy_table.empty:
        raise BessPlanningFeaturePolicyError(
            "policy table must contain at least one policy entry"
        )
    for field in POLICY_RESULT_SCALAR_FIELDS:
        if not field.endswith("_sha256"):
            continue
        try:
            _sha256_string(getattr(result, field), field)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    _validate_policy_table_rows(result)
    rebuilt = _result_with_hashes(result)
    if result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256:
        raise BessPlanningFeaturePolicyError("policy table hash is invalid")
    if result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256:
        raise BessPlanningFeaturePolicyError("complete result hash is invalid")


def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Validate one compiled-policy envelope without rebuilding CNIG sources."""

    try:
        _validate_result_envelope(result)
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS planning-feature policy result envelope is invalid"
        ) from error


def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Load and locally validate one physically sealed compiled-policy artifact."""

    try:
        parquet = Path(parquet_path)
        manifest_file = Path(manifest_path)
        payload = loads_strict_json_object(manifest_file.read_bytes())
        manifest = BessPlanningFeaturePolicyArtifactManifest.model_validate(payload)
        if manifest.parquet_filename != parquet.name:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet filename differs from the supplied file"
            )
        parquet_payload = parquet.read_bytes()
        if len(parquet_payload) != manifest.parquet_size_bytes:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet size differs from the supplied file"
            )
        if sha256(parquet_payload).hexdigest() != manifest.parquet_sha256:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet SHA256 differs from the supplied file"
            )
        table = pd.read_parquet(BytesIO(parquet_payload))
        if len(table) != manifest.parquet_row_count:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet row count differs from the supplied file"
            )
        actual_schema = deterministic_frame_schema_signature(table)
        declared_schema = manifest.policy_table_schema_signature.model_dump(mode="json")
        if actual_schema != declared_schema:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest policy-table schema differs from the supplied file"
            )
        result = BessPlanningFeaturePolicyResult(
            **{name: getattr(manifest, name) for name in POLICY_RESULT_SCALAR_FIELDS},
            policy_table=table,
        )
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            f"BESS CNIG feature policy artifacts are invalid: {error}"
        ) from error


def _validate_coded_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    try:
        validate_planning_feature_code_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "Source-complete CNIG result validation failed"
        ) from error


def compile_bess_planning_feature_policy(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Compile the exact source-locked policy without applying it to features."""

    try:
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        result = _build_result(config, coded_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy compilation failed safely"
        ) from error


def validate_bess_planning_feature_policy_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Rebuild and validate a normalized policy from every factual source input."""

    try:
        _validate_result_envelope(result)
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        expected = _build_result(config, coded_result)
        for field in POLICY_RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeaturePolicyError(
                    f"result {field} differs from rebuilt policy"
                )
        if _frame_payload(result.policy_table) != _frame_payload(expected.policy_table):
            raise BessPlanningFeaturePolicyError(
                "policy table differs from rebuilt policy"
            )
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy result validation failed safely"
        ) from error
```
