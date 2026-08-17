# `src/landscout/stages/bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/bess_planning_feature_policy.py`
- File type: Python source
- Layer: policy compilation stage
- Domain: planning
- Responsibility: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.
- Source SHA256: `9ca9a70b5930e6e3054dd80bf83e04a658916d64d24133162140f713bd5c23d0`

## 1. Purpose

Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

## 2. Position in LandScout architecture

This file belongs to the **policy compilation stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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
- `import yaml`
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
- `from landscout.sources.gpu_fr import GpuPlanningDocument`
- `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`

## 4. Contract taxonomy

### A. Python constants

#### `POLICY_SCHEMA_VERSION`

```python
POLICY_SCHEMA_VERSION = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` (value reference).

#### `RESULT_HASH_SCHEMA_VERSION`

```python
RESULT_HASH_SCHEMA_VERSION = 1
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_build_result` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` (value reference).

#### `ARTIFACT_MANIFEST_SCHEMA_VERSION`

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` (value reference).

#### `POLICY_SCOPE`

```python
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` (value reference).

#### `ARTIFACT_KIND`

```python
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `ALLOWED_STATUSES`

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

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` (value reference).

#### `ALLOWED_CONFIDENCES`

```python
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` (value reference).

#### `CODE_PATTERN`

```python
CODE_PATTERN = re.compile(r"[0-9]{2}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry._validate_entry` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` (value reference).

#### `SHA_PATTERN`

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::_sha256_string` (value reference).

#### `POLICY_TABLE_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::<module>` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_policy_table` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` (value reference).

#### `POLICY_TABLE_DTYPES`

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

Canonical Pandas/GeoPandas dtype contract aligned with the named schema. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::<module>` (value reference).

#### `POLICY_TABLE_SCHEMA_SIGNATURE`

```python
POLICY_TABLE_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(POLICY_TABLE_COLUMNS),
    "dtypes": list(POLICY_TABLE_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` (value reference).

#### `NULL_REFERENCE_LITERALS`

```python
NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` (value reference).

#### `POLICY_RESULT_SCALAR_FIELDS`

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

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` (value reference), `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` (value reference).


### B. Type aliases and closed domains

#### `FeatureFamily`

```python
FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
```

Official planning-feature family domain: PRESCRIPTION or INFORMATION. Enforced/consumed by `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry` (type annotation).

#### `PrecheckStatus`

```python
PrecheckStatus = Literal[
    "LIKELY_MATERIAL_CONSTRAINT",
    "MATERIAL_REVIEW_REQUIRED",
    "DESIGN_REVIEW_REQUIRED",
    "CONTEXT_REVIEW_REQUIRED",
    "UNKNOWN",
]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. Enforced/consumed by `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry` (type annotation), `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig` (type annotation).

#### `Confidence`

```python
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
```

Written-zoning evidence confidence domain: HIGH, MEDIUM, or LOW. Enforced/consumed by `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry` (type annotation).


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
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


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `BessPlanningFeaturePolicyError`

**Purpose:** Raised when the official-code BESS policy cannot be proven exact.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_json_sha256` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_construct_unique_mapping` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_config` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_resolved_policy_config` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_value` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_source_lock` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_dictionary_by_pair` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_completeness` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result_envelope` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_unique_json_object` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_coded_source` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyError`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyError`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_null_reference_literal_is_rejected_by_local_envelope` via `pytest.raises(BessPlanningFeaturePolicyError, match='reference|null|missing')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_source_lock_mismatch_is_rejected` via `pytest.raises(BessPlanningFeaturePolicyError, match='lock|source|CNIG')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected` via `pytest.raises(BessPlanningFeaturePolicyError, match='missing|pair')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback` via `pytest.raises(BessPlanningFeaturePolicyError, match='extra|pair')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate` via `pytest.raises(BessPlanningFeaturePolicyError, match='missing|extra|pair')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected` via `pytest.raises(BessPlanningFeaturePolicyError, match=message)`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_yaml_key_is_rejected` via `pytest.raises(BessPlanningFeaturePolicyError, match='Duplicate YAML')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_in_memory_config_is_revalidated_before_compilation` via `pytest.raises(BessPlanningFeaturePolicyError, match='in-memory|canonical')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_table_mutation_is_rejected` via `pytest.raises(BessPlanningFeaturePolicyError, match='hash|table|rebuilt')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `pytest.raises(BessPlanningFeaturePolicyError, match='table|rebuilt')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_manifest_mismatch` via `pytest.raises(BessPlanningFeaturePolicyError, match=message)`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_duplicate_json_key` via `pytest.raises(BessPlanningFeaturePolicyError, match='Duplicate JSON')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_parquet_replacement` via `pytest.raises(BessPlanningFeaturePolicyError, match='size|SHA|hash')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `pytest.raises(BessPlanningFeaturePolicyError, match='type|schema|hash|result')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `pytest.raises(BessPlanningFeaturePolicyError, match='lock|document')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `pytest.raises(BessPlanningFeaturePolicyError, match='Source-complete|source')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator` via `pytest.raises(BessPlanningFeaturePolicyError, match='hash')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `pytest.raises(BessPlanningFeaturePolicyError, match='CNIG|cnig|schema|version')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_rejects_canonical_empty_policy_table` via `pytest.raises(BessPlanningFeaturePolicyError, match='policy|table|empty|entry')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_cnig_profile_schema_two` via `pytest.raises(BessPlanningFeaturePolicyError, match='profile schema|schema')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_cnig_result_schema_five` via `pytest.raises(BessPlanningFeaturePolicyError, match='CNIG result|schema')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_validates_every_intrinsic_row_contract` via `pytest.raises(BessPlanningFeaturePolicyError, match='policy|pair|order|code|status|confidence|priority|scope|flag|CNIG|null|schema')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1` via `pytest.raises(BessPlanningFeaturePolicyError, match='type|result')`.
- expected exception type: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_controls_malformed_result_type` via `pytest.raises(BessPlanningFeaturePolicyError)`.

**Exact class source**

```python
class BessPlanningFeaturePolicyError(ValueError):
    """Raised when the official-code BESS policy cannot be proven exact."""
```

### `_StrictPolicyModel`

**Purpose:** Validates the planning contract carried by its explicit validators and inherited fields.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `PolicyTableSchemaSignature`

**Purpose:** Immutable persisted schema identity for the normalized policy table.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `columns` | `columns: tuple[StrictStr, ...]` | Structured `columns` collection owned by `PolicyTableSchemaSignature`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `dtypes` | `dtypes: tuple[StrictStr, ...]` | `PolicyTableSchemaSignature.dtypes` represents the `dtypes` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `index_class` | `index_class: StrictStr` | `PolicyTableSchemaSignature.index_class` represents the `index_class` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `index_names` | `index_names: tuple[StrictStr \| None, ...]` | Structured `index names` collection owned by `PolicyTableSchemaSignature`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `index_level_dtypes` | `index_level_dtypes: tuple[StrictStr, ...]` | `PolicyTableSchemaSignature.index_level_dtypes` represents the `index_level_dtypes` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Interface consumers**

- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest` via `PolicyTableSchemaSignature`.

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

**Purpose:** Exact upstream document/archive/CNIG or planning-result identity that the owning policy must match before compilation/application.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `document_id` | `document_id: StrictStr` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `archive_sha256` | `archive_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: StrictStr` | Official CNIG profile identity propagated through this policy/result lineage. |
| `cnig_profile_schema_version` | `cnig_profile_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_profile_sha256` | `cnig_profile_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_result_hash_schema_version` | `cnig_result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_complete_result_content_sha256` | `cnig_complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |

**Validators (exact source)**

`_validate_lock`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `PolicySourceLock`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig` via `PolicySourceLock`.

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

**Purpose:** One exact CNIG family/type/subtype policy row with official meaning, precheck outcome, confidence, priority, rationale, action, limitations, and false legal/interpretation flags.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `feature_family` | `feature_family: FeatureFamily` | `PolicyEntry.feature_family` represents the `feature_family` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `type_code` | `type_code: StrictStr` | `PolicyEntry.type_code` represents the `type_code` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `subtype_code` | `subtype_code: StrictStr` | `PolicyEntry.subtype_code` represents the `subtype_code` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `expected_official_label` | `expected_official_label: StrictStr` | `PolicyEntry.expected_official_label` carries the expected official label used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |
| `expected_legal_reference` | `expected_legal_reference: StrictStr \| None` | `PolicyEntry.expected_legal_reference` carries the expected legal reference used by the reproduced constructors and validators; its declared type is `StrictStr | None` and no legal meaning is inferred beyond that owner. |
| `expected_regulation_reference` | `expected_regulation_reference: StrictStr \| None` | `PolicyEntry.expected_regulation_reference` carries the expected regulation reference used by the reproduced constructors and validators; its declared type is `StrictStr | None` and no legal meaning is inferred beyond that owner. |
| `precheck_status` | `precheck_status: PrecheckStatus` | `PolicyEntry.precheck_status` represents the `precheck_status` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `confidence` | `confidence: Confidence` | Configured evidence-confidence value used by the owning policy row or result. |
| `rationale` | `rationale: StrictStr` | `PolicyEntry.rationale` carries the rationale used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |
| `required_human_action` | `required_human_action: StrictStr` | `PolicyEntry.required_human_action` carries the required human action used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |
| `limitations` | `limitations: StrictStr` | `PolicyEntry.limitations` carries the limitations used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |

**Validators (exact source)**

`_validate_entry`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry._validate_entry` via `PolicyEntry`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_policy_entries_sha256` via `PolicyEntry`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig` via `PolicyEntry`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_completeness` via `PolicyEntry`.

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

**Purpose:** Validates the planning contract carried by `schema_version`, `profile`, `policy_scope`, `local_feature_text_interpreted`, `local_regulation_content_interpreted`, `legal_conclusion_produced`, `source_lock`, `status_priority`, `canonical_policy_entries_sha256`, `entries`.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `profile` | `profile: StrictStr` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_scope` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `local_feature_text_interpreted` | `local_feature_text_interpreted: StrictBool` | Boolean `local feature text interpreted` flag on `BessPlanningFeaturePolicyConfig`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `local_regulation_content_interpreted` | `local_regulation_content_interpreted: StrictBool` | Boolean `local regulation content interpreted` flag on `BessPlanningFeaturePolicyConfig`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `legal_conclusion_produced` | `legal_conclusion_produced: StrictBool` | Boolean `legal conclusion produced` flag on `BessPlanningFeaturePolicyConfig`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `source_lock` | `source_lock: PolicySourceLock` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `status_priority` | `status_priority: dict[PrecheckStatus, StrictInt]` | `BessPlanningFeaturePolicyConfig.status_priority` represents the `status_priority` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `canonical_policy_entries_sha256` | `canonical_policy_entries_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `entries` | `entries: tuple[PolicyEntry, ...]` | Structured `entries` collection owned by `BessPlanningFeaturePolicyConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Validators (exact source)**

`_validate_policy`:

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
        return self
```

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_source` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_policy_source` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_config` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_resolved_policy_config` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_policy_sha256` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_source_lock` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_completeness` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_compiled_fixture` via `BessPlanningFeaturePolicyConfig`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_validated_config` via `BessPlanningFeaturePolicyConfig`.

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
        return self
```

### `_UniqueKeyLoader`

**Purpose:** Private PyYAML SafeLoader subclass whose mapping constructor is replaced to reject duplicate YAML keys.

**Kind:** PyYAML loader subclass.

**Inheritance:** `yaml.SafeLoader`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- No repository construction/import/property/decorator reference was found; the exact declaration is retained because it participates in the module's runtime/framework namespace.

**Exact class source**

```python
class _UniqueKeyLoader(yaml.SafeLoader):
    pass
```

### `BessPlanningFeaturePolicyResult`

**Purpose:** Immutable normalized policy table and its source-complete hash envelope.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `policy_schema_version` | `policy_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `result_hash_schema_version` | `result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `policy_profile` | `policy_profile: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_scope` | `policy_scope: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_sha256` | `policy_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_document_id` | `source_document_id: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: str` | Official CNIG profile identity propagated through this policy/result lineage. |
| `cnig_profile_schema_version` | `cnig_profile_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_profile_sha256` | `cnig_profile_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_result_hash_schema_version` | `cnig_result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_complete_result_content_sha256` | `cnig_complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_table_content_sha256` | `policy_table_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_table` | `policy_table: pd.DataFrame` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_source` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_policy_lookup` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_policy_values` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_coded_policy_compatibility` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_source_locks` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_policy_source` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_component_metadata` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_complete_result_sha256` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_result_with_hashes` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `BessPlanningFeaturePolicyResult`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result_envelope` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyResult`.
- constructor call: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyResult`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_compiled_fixture` via `BessPlanningFeaturePolicyResult`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_artifact_manifest` via `BessPlanningFeaturePolicyResult`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_write_artifacts` via `BessPlanningFeaturePolicyResult`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `BessPlanningFeaturePolicyResult`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_rehash_policy_table` via `BessPlanningFeaturePolicyResult`.
- type annotation: `tests/unit/test_bess_planning_feature_policy.py::_canonical_empty_policy_result` via `BessPlanningFeaturePolicyResult`.

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

**Purpose:** Strict physical binding between one policy table and its hash envelope.

**Kind:** Pydantic model.

**Inheritance:** `_StrictPolicyModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `artifact_kind` | `artifact_kind: Literal["BESS_CNIG_FEATURE_POLICY_RESULT"]` | `BessPlanningFeaturePolicyArtifactManifest.artifact_kind` represents the `artifact_kind` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `policy_schema_version` | `policy_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `result_hash_schema_version` | `result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `policy_profile` | `policy_profile: StrictStr` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_scope` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_sha256` | `policy_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_document_id` | `source_document_id: StrictStr` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: StrictStr` | Official CNIG profile identity propagated through this policy/result lineage. |
| `cnig_profile_schema_version` | `cnig_profile_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_profile_sha256` | `cnig_profile_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_result_hash_schema_version` | `cnig_result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_complete_result_content_sha256` | `cnig_complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_table_content_sha256` | `policy_table_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `parquet_filename` | `parquet_filename: StrictStr` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `parquet_row_count` | `parquet_row_count: StrictInt` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `parquet_size_bytes` | `parquet_size_bytes: StrictInt` | Measured physical Parquet artifact size in bytes. |
| `parquet_sha256` | `parquet_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_table_schema_signature` | `policy_table_schema_signature: PolicyTableSchemaSignature` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |

**Validators (exact source)**

`_validate_manifest`:

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

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `BessPlanningFeaturePolicyArtifactManifest`.

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
- Explicit raise expressions: `ValueError(f'{label} must be an exact non-empty string without edge whitespace')`.

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_optional_exact_string` via `_exact_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `_exact_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry._validate_entry` via `_exact_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_exact_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_exact_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `_exact_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_optional_exact_string`

**Exact signature**

```python
def _optional_exact_string(value: object, label: str) -> str | None:
```

**Purpose**

Private `planning` helper for optional exact string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
_exact_string(value, label)

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry._validate_entry` via `_optional_exact_string`.

**Complete source-ordered implementation**

```python
def _optional_exact_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _exact_string(value, label)
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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `_sha256_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_sha256_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_sha256_string`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_sha256_string`.

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

### `PolicySourceLock._validate_lock`

**Exact signature**

```python
def _validate_lock(self) -> PolicySourceLock:
```

**Purpose**

Rejects malformed or inconsistent lock; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `PolicySourceLock`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `type(value) is not int or value < 1`.
- Explicit raise expressions: `ValueError(f'{label} must be a strict positive integer')`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `PolicyEntry._validate_entry`

**Exact signature**

```python
def _validate_entry(self) -> PolicyEntry:
```

**Purpose**

Rejects malformed or inconsistent entry; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `PolicyEntry`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `CODE_PATTERN.fullmatch(self.type_code) is None`.
- Guard with a raise path: `CODE_PATTERN.fullmatch(self.subtype_code) is None`.
- Explicit raise expressions: `ValueError('subtype_code must be an exact two-character digit string')`, `ValueError('type_code must be an exact two-character digit string')`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_json_sha256`

**Exact signature**

```python
def _canonical_json_sha256(value: object) -> str:
```

**Purpose**

Private `planning` helper for canonical json sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(encoded).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('Policy integrity payload is not canonical JSON')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(encoded).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_policy_entries_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_policy_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_complete_result_sha256` via `_canonical_json_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_entries_sha256`

**Exact signature**

```python
def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
```

**Purpose**

Private `planning` helper for policy entries sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256([entry.model_dump(mode='json') for entry in entries])
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_policy_entries_sha256`.

**Complete source-ordered implementation**

```python
def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
    return _canonical_json_sha256([entry.model_dump(mode="json") for entry in entries])
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeaturePolicyConfig._validate_policy`

**Exact signature**

```python
def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Rejects malformed or inconsistent policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `type(self.schema_version) is not int or self.schema_version != POLICY_SCHEMA_VERSION`.
- Guard with a raise path: `self.policy_scope != POLICY_SCOPE`.
- Guard with a raise path: `self.local_feature_text_interpreted is not False or self.local_regulation_content_interpreted is not False or self.legal_conclusion_produced is not False`.
- Guard with a raise path: `set(self.status_priority) != ALLOWED_STATUSES`.
- Guard with a raise path: `any((type(value) is not int or value <= 0 for value in priorities))`.
- Guard with a raise path: `len(set(priorities)) != len(priorities)`.
- Guard with a raise path: `len(keys) != len(set(keys))`.
- Guard with a raise path: `keys != sorted(keys)`.
- Guard with a raise path: `_policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256`.
- Explicit raise expressions: `ValueError('canonical policy-entry SHA256 differs from policy entries')`, `ValueError('policy entries contain a duplicate family/type/subtype pair')`, `ValueError('policy entries must use deterministic family/type/subtype order')`, `ValueError('policy interpretation and legal-conclusion flags must be false')`, `ValueError('policy_scope is unsupported')`, `ValueError('status priority must contain every allowed status exactly once')`, `ValueError('status priority values must be strict positive integers')`, `ValueError('status priority values must be unique')`, `ValueError(f'policy schema version must equal {POLICY_SCHEMA_VERSION}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_policy_entries_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_construct_unique_mapping`

**Exact signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Private `planning` helper for construct unique mapping; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[object, object]`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `key in result`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError(f'Duplicate YAML policy key: {key!r}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `result[key]`.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.

**Complete source-ordered implementation**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise BessPlanningFeaturePolicyError(f"Duplicate YAML policy key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_policy_config`

**Exact signature**

```python
def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Load a strict offline BESS policy for official CNIG feature-code pairs.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, Mapping)`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('BESS CNIG feature policy is invalid')`, `BessPlanningFeaturePolicyError('BESS CNIG policy must be a mapping')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `Path(path).read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_resolved_policy_config` via `load_bess_planning_feature_policy_config`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `load_bess_planning_feature_policy_config`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_pins_all_twelve_exact_muret_decisions` via `load_bess_planning_feature_policy_config`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_complete_snapshot_is_immutable` via `load_bess_planning_feature_policy_config`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_policy_text_drift` via `load_bess_planning_feature_policy_config`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_source_lock_drift` via `load_bess_planning_feature_policy_config`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_yaml_key_is_rejected` via `load_bess_planning_feature_policy_config`.

**Complete source-ordered implementation**

```python
def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
    """Load a strict offline BESS policy for official CNIG feature-code pairs."""

    try:
        payload = yaml.load(
            Path(path).read_text(encoding="utf-8"), Loader=_UniqueKeyLoader
        )
        if not isinstance(payload, Mapping):
            raise BessPlanningFeaturePolicyError("BESS CNIG policy must be a mapping")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy is invalid"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_policy_config`

**Exact signature**

```python
def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Private `planning` helper for resolved policy config; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
load_bess_planning_feature_policy_config(config)

BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('in-memory BESS planning-feature policy config is invalid')`.

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_resolved_policy_config`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_resolved_policy_config`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_sha256`

**Exact signature**

```python
def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
```

**Purpose**

Private `planning` helper for policy sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256(config.model_dump(mode='json'))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `_policy_sha256`.

**Complete source-ordered implementation**

```python
def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
    return _canonical_json_sha256(config.model_dump(mode="json"))
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeaturePolicyArtifactManifest._validate_manifest`

**Exact signature**

```python
def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
```

**Purpose**

Rejects malformed or inconsistent manifest; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyArtifactManifest`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`.
- Guard with a raise path: `type(self.policy_schema_version) is not int or self.policy_schema_version != POLICY_SCHEMA_VERSION`.
- Guard with a raise path: `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `type(self.cnig_profile_schema_version) is not int or self.cnig_profile_schema_version != 2`.
- Guard with a raise path: `type(self.cnig_result_hash_schema_version) is not int or self.cnig_result_hash_schema_version != 5`.
- Guard with a raise path: `type(integer_value) is not int or integer_value < minimum`.
- Explicit raise expressions: `ValueError('artifact CNIG profile schema version is unsupported')`, `ValueError('artifact CNIG result hash schema version is unsupported')`, `ValueError('artifact policy schema version is unsupported')`, `ValueError('artifact result hash schema version is unsupported')`, `ValueError(f'artifact manifest schema version must equal {ARTIFACT_MANIFEST_SCHEMA_VERSION}')`, `ValueError(f'{label} is invalid')`.

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_null_safe_equal` via `_null_value`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_value` via `_null_value`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `_null_value`.

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

### `_null_safe_equal`

**Exact signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

**Purpose**

Private `planning` helper for null safe equal; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
normalized_left is None and normalized_right is None

bool(normalized_left == normalized_right)

False
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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_completeness` via `_null_safe_equal`.

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

value.isoformat()

_canonical_value(value.item())

value

int(value)

number

value
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, Real)`.
- Guard with a raise path: `not math.isfinite(number)`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('Policy integrity payload contains non-finite data')`, `BessPlanningFeaturePolicyError(f'Policy integrity payload contains unsupported {type(value).__name__}')`.

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.

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

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_frame_payload`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_frame_payload`.

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

### `_validate_source_lock`

**Exact signature**

```python
def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent source lock; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `configured != actual`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError(f'Policy source lock differs from validated {label}')`.

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_validate_source_lock`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_validate_source_lock`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_dictionary_by_pair`

**Exact signature**

```python
def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Private `planning` helper for dictionary by pair; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
indexed
```

**Validation and exceptions**

- Guard with a raise path: `key in indexed`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('Validated CNIG code dictionary contains a duplicate pair')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `indexed[key]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_completeness` via `_dictionary_by_pair`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_completeness`

**Exact signature**

```python
def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Rejects malformed or inconsistent policy completeness; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
dictionary
```

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `extra`.
- Guard with a raise path: `entry.expected_official_label != row['official_label']`.
- Guard with a raise path: `not _null_safe_equal(entry.expected_legal_reference, row['legal_reference'])`.
- Guard with a raise path: `not _null_safe_equal(entry.expected_regulation_reference, row['regulation_or_annex_reference'])`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError(f'Policy contains extra CNIG pair(s): {extra}')`, `BessPlanningFeaturePolicyError(f'Policy is missing validated CNIG pair(s): {missing}')`, `BessPlanningFeaturePolicyError(f'Policy legal reference mismatch for pair {key}')`, `BessPlanningFeaturePolicyError(f'Policy official label mismatch for pair {key}')`, `BessPlanningFeaturePolicyError(f'Policy regulation reference mismatch for pair {key}')`.

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `_validate_policy_completeness`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_table`

**Exact signature**

```python
def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for policy table; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
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
- In-memory mutation: `output.index`, `output['status_priority']`, `output[column]`, `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `_policy_table`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_metadata`

**Exact signature**

```python
def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for component metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'policy_schema_version': result.policy_schema_version, 'result_hash_schema_version': result.result_hash_schema_version, 'policy_profile': result.policy_profile, 'policy_scope': result.policy_scope, 'policy_sha256': result.policy_sha256, 'source_document_id': result.source_document_id, 'source_archive_sha256': result.source_archive_sha256, 'cnig_profile': result.cnig_profile, 'cnig_profile_schema_version': result.cnig_profile_schema_version, 'cnig_profile_sha256': result.cnig_profile_sha256, 'cnig_result_hash_schema_version': result.cnig_result_hash_schema_version, 'cnig_complete_result_content_sha256': result.cnig_complete_result_content_sha256}
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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_component_metadata`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_complete_result_sha256` via `_component_metadata`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_table_sha256`

**Exact signature**

```python
def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

**Purpose**

Private `planning` helper for policy table sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': 'landscout.bess_cnig_feature_policy.table', **_component_metadata(result), 'frame': _frame_payload(result.policy_table)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_result_with_hashes` via `_policy_table_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_complete_result_sha256`

**Exact signature**

```python
def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

**Purpose**

Private `planning` helper for complete result sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': 'landscout.bess_cnig_feature_policy.result', **_component_metadata(result), 'policy_table_content_sha256': result.policy_table_content_sha256})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_result_with_hashes` via `_complete_result_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Exact signature**

```python
def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Private `planning` helper for result with hashes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(component, complete_result_content_sha256=_complete_result_sha256(component))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_complete_result_sha256`, `_policy_table_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_table_rows`

**Exact signature**

```python
def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
```

**Purpose**

Rejects malformed or inconsistent policy table rows; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `ordered_keys != sorted(ordered_keys)`.
- Guard with a raise path: `family not in {'PRESCRIPTION', 'INFORMATION'}`.
- Guard with a raise path: `key in records`.
- Guard with a raise path: `status not in ALLOWED_STATUSES`.
- Guard with a raise path: `confidence not in ALLOWED_CONFIDENCES`.
- Guard with a raise path: `type(priority) is not int or priority <= 0`.
- Guard with a raise path: `previous_status != status or previous_priority != priority`.
- Guard with a raise path: `row['policy_scope'] != result.policy_scope`.
- Guard with a raise path: `row['policy_profile'] != result.policy_profile or row['policy_sha256'] != result.policy_sha256 or row['cnig_profile'] != result.cnig_profile or (row['cnig_profile_sha256'] != result.cnig_profile_sha256) or (row['cnig_complete_result_content_sha256'] != result.cnig_complete_result_content_sha256)`.
- Guard with a raise path: `not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None`.
- Guard with a raise path: `isinstance(value, str) and value in NULL_REFERENCE_LITERALS`.
- Guard with a raise path: `row[field] is not False`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('policy table contains a duplicate code pair')`, `BessPlanningFeaturePolicyError('policy table pair order is not canonical')`, `BessPlanningFeaturePolicyError('policy table status and priority mapping is not one-to-one')`, `BessPlanningFeaturePolicyError(f'policy table row {position} confidence is invalid')`, `BessPlanningFeaturePolicyError(f'policy table row {position} feature family is invalid')`, `BessPlanningFeaturePolicyError(f'policy table row {position} priority is invalid')`, `BessPlanningFeaturePolicyError(f'policy table row {position} result lineage differs')`, `BessPlanningFeaturePolicyError(f'policy table row {position} scope differs from result')`, `BessPlanningFeaturePolicyError(f'policy table row {position} status is invalid')`, `BessPlanningFeaturePolicyError(f'policy table row {position} {field} must be false')`, `BessPlanningFeaturePolicyError(f'policy table row {position} {label} is invalid')`, `BessPlanningFeaturePolicyError(f'{field} contains a literal null replacement')`, `BessPlanningFeaturePolicyError(str(error))`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `ordered_keys`, `priority_to_status`, `records[key]`, `status_to_priority`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_validate_policy_table_rows`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

**Exact signature**

```python
def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Constructs result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyResult`.
- Every observed return expression is reproduced without truncation:
```python
_result_with_hashes(result)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_policy_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_build_result`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_build_result`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Exact signature**

```python
def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
```

**Purpose**

Rejects malformed or inconsistent result envelope; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(result) is not BessPlanningFeaturePolicyResult`.
- Guard with a raise path: `result.policy_scope != POLICY_SCOPE`.
- Guard with a raise path: `not isinstance(result.policy_table, pd.DataFrame) or isinstance(result.policy_table, gpd.GeoDataFrame)`.
- Guard with a raise path: `result.policy_table.columns.duplicated().any() or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS`.
- Guard with a raise path: `deterministic_frame_schema_signature(result.policy_table) != POLICY_TABLE_SCHEMA_SIGNATURE`.
- Guard with a raise path: `result.policy_table.empty`.
- Guard with a raise path: `result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256`.
- Guard with a raise path: `result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256`.
- Guard with a raise path: `type(version) is not int or version != expected`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('complete result hash is invalid')`, `BessPlanningFeaturePolicyError('policy table hash is invalid')`, `BessPlanningFeaturePolicyError('policy table must be a DataFrame')`, `BessPlanningFeaturePolicyError('policy table must contain at least one policy entry')`, `BessPlanningFeaturePolicyError('policy table schema is invalid')`, `BessPlanningFeaturePolicyError('result must be a BessPlanningFeaturePolicyResult')`, `BessPlanningFeaturePolicyError('result policy scope is invalid')`, `BessPlanningFeaturePolicyError(f'unsupported {label} version')`, `BessPlanningFeaturePolicyError(str(error))`.

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result_envelope` via `_validate_result_envelope`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `_validate_result_envelope`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_validate_result_envelope`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_validate_result_envelope`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_policy_result_envelope`

**Exact signature**

```python
def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
```

**Purpose**

Validate one compiled-policy envelope without rebuilding CNIG sources.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('BESS planning-feature policy result envelope is invalid')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- direct call: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `validate_bess_planning_feature_policy_result_envelope`.

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
- Explicit raise expressions: `BessPlanningFeaturePolicyError(f'Duplicate JSON artifact key: {key!r}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output[key]`.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `json.loads(manifest_file.read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`.

**Complete source-ordered implementation**

```python
def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise BessPlanningFeaturePolicyError(
                f"Duplicate JSON artifact key: {key!r}"
            )
        output[key] = value
    return output
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_policy_artifacts`

**Exact signature**

```python
def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Load and locally validate one physically sealed compiled-policy artifact.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `manifest.parquet_filename != parquet.name`.
- Guard with a raise path: `len(parquet_payload) != manifest.parquet_size_bytes`.
- Guard with a raise path: `sha256(parquet_payload).hexdigest() != manifest.parquet_sha256`.
- Guard with a raise path: `len(table) != manifest.parquet_row_count`.
- Guard with a raise path: `actual_schema != declared_schema`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('Artifact manifest Parquet SHA256 differs from the supplied file')`, `BessPlanningFeaturePolicyError('Artifact manifest Parquet filename differs from the supplied file')`, `BessPlanningFeaturePolicyError('Artifact manifest Parquet row count differs from the supplied file')`, `BessPlanningFeaturePolicyError('Artifact manifest Parquet size differs from the supplied file')`, `BessPlanningFeaturePolicyError('Artifact manifest policy-table schema differs from the supplied file')`, `BessPlanningFeaturePolicyError(f'BESS CNIG feature policy artifacts are invalid: {error}')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `manifest_file.read_text`, `parquet.read_bytes`, `pd.read_parquet`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(parquet_payload).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.

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
        payload = json.loads(
            manifest_file.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
        )
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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_coded_source`

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

**Purpose**

Rejects malformed or inconsistent coded source; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('Source-complete CNIG result validation failed')`.

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

- direct call: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_validate_coded_source`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_validate_coded_source`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `compile_bess_planning_feature_policy`

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

**Purpose**

Compile the exact source-locked policy without applying it to features.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('BESS CNIG feature policy compilation failed safely')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::_compiled_fixture` via `compile_bess_planning_feature_policy`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_source_lock_mismatch_is_rejected` via `compile_bess_planning_feature_policy`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected` via `compile_bess_planning_feature_policy`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback` via `compile_bess_planning_feature_policy`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate` via `compile_bess_planning_feature_policy`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected` via `compile_bess_planning_feature_policy`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_in_memory_config_is_revalidated_before_compilation` via `compile_bess_planning_feature_policy`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_policy_result`

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

**Purpose**

Rebuild and validate a normalized policy from every factual source input.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `_frame_payload(result.policy_table) != _frame_payload(expected.policy_table)`.
- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Explicit raise expressions: `BessPlanningFeaturePolicyError('BESS CNIG feature policy result validation failed safely')`, `BessPlanningFeaturePolicyError('policy table differs from rebuilt policy')`, `BessPlanningFeaturePolicyError(f'result {field} differs from rebuilt policy')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`.
- direct call: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_policy_source` via `validate_bess_planning_feature_policy_result`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status` via `validate_bess_planning_feature_policy_result`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_policy_table_mutation_is_rejected` via `validate_bess_planning_feature_policy_result`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `validate_bess_planning_feature_policy_result`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_persisted_parquet_and_json_readback_is_source_complete` via `validate_bess_planning_feature_policy_result`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `POLICY_TABLE_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `type_code` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `subtype_code` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `official_label` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `official_legal_reference` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `official_regulation_reference` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `precheck_status` | Pandas nullable string dtype | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 8 | `confidence` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `status_priority` | NumPy int64 | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 10 | `rationale` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `required_human_action` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `limitations` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `policy_scope` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `local_feature_text_interpreted` | non-null Boolean dtype | non-null under this dtype contract | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `local_regulation_content_interpreted` | non-null Boolean dtype | non-null under this dtype contract | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 16 | `legal_conclusion_produced` | non-null Boolean dtype | non-null under this dtype contract | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `policy_profile` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `policy_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 19 | `cnig_profile` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 20 | `cnig_profile_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 21 | `cnig_complete_result_content_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |

### `POLICY_TABLE_DTYPES` — dtype contract aligned with a canonical schema

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

### `POLICY_TABLE_SCHEMA_SIGNATURE` — portable schema/index signature

```python
POLICY_TABLE_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(POLICY_TABLE_COLUMNS),
    "dtypes": list(POLICY_TABLE_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `columns` | ['feature_family', 'type_code', 'subtype_code', 'official_label', 'official_legal_reference', 'official_regulation_reference', 'precheck_status', 'confidence', 'status_priority', 'rationale', 'required_human_action', 'limitations', 'policy_scope', 'local_feature_text_interpreted', 'local_regulation_content_interpreted', 'legal_conclusion_produced', 'policy_profile', 'policy_sha256', 'cnig_profile', 'cnig_profile_sha256', 'cnig_complete_result_content_sha256'] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `dtypes` | ['str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'int64', 'str', 'str', 'str', 'str', 'bool', 'bool', 'bool', 'str', 'str', 'str', 'str', 'str'] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `index_class` | pandas.Index | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `index_names` | [None] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `index_level_dtypes` | ['int64'] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `BessPlanningFeaturePolicyArtifactManifest` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `BessPlanningFeaturePolicyConfig` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `BessPlanningFeaturePolicyError` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `BessPlanningFeaturePolicyResult` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `compile_bess_planning_feature_policy` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `load_bess_planning_feature_policy_artifacts` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `load_bess_planning_feature_policy_config` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `validate_bess_planning_feature_policy_result` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |
| `validate_bess_planning_feature_policy_result_envelope` | public symbol defined in this module | `defined in `src/landscout/stages/bess_planning_feature_policy.py`` | yes |

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
